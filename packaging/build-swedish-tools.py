#!/usr/bin/env python3
"""Build matching RPM/DEB snapshots from clean, pinned local source checkouts."""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tarfile

TARGETS = {
    'svlang': {'version': '0.2.0', 'release': '2', 'commit': 'd29fcbc33390fb87859b34698706e893b140b6a7',
               'summary': 'Swedish language tools for translators', 'license': 'MIT AND LGPL AND CC-BY-SA-2.5'},
    'swedish-tm': {'version': '20260918', 'release': '1', 'commit': '359390fce7a17db50de4722db14331cb9e9735b2',
                   'summary': 'Swedish translation memory for open source software', 'license': 'CC-BY-4.0'},
    'swedish-foss-terminology': {'version': '20260918', 'release': '1', 'commit': '73d68c8531a83a8429214fb9fb37cca5b5160f6a',
                                'summary': 'Swedish terminology for open source software', 'license': 'CC-BY-4.0'},
}


def run(*args, **kwargs):
    return subprocess.run(args, check=True, **kwargs)


def copy(source, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def stage(name, source, dest, info):
    share = dest / 'usr/share' / name
    share.mkdir(parents=True)
    copy(source / 'README.md', share / 'README.md')
    doc = dest / 'usr/share/doc' / name
    doc.mkdir(parents=True)
    (doc / 'README.md').symlink_to('../../' + name + '/README.md')
    provenance = {'repository': 'https://github.com/yeager/' + name, **info}
    (doc / 'source.json').write_text(json.dumps(provenance, indent=2) + '\n')
    if name == 'svlang':
        shutil.copytree(source / 'src/svlang', share / 'svlang', ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '*.bak'))
        launcher = dest / 'usr/bin/svlang'
        launcher.parent.mkdir(parents=True)
        launcher.write_text('#!/usr/bin/python3\nimport sys\nsys.path.insert(0, "/usr/share/svlang")\nfrom svlang.cli import main\nsys.exit(main())\n')
        launcher.chmod(0o755)
        man = dest / 'usr/share/man/man1/svlang.1.gz'
        man.parent.mkdir(parents=True)
        man.write_bytes(gzip.compress((source / 'data/man/svlang.1').read_bytes(), mtime=0))
        copy(source / 'LICENSE', doc / 'LICENSE')
        copy(source / 'debian/copyright', doc / 'copyright')
        with (doc / 'copyright').open('a') as out:
            out.write('\nBundled data notices from upstream:\n'
                      ' sv_wordlist.txt: Hunspell sv_SE wordlist (LGPL).\n'
                      ' folkets_sv_en.tsv: Folkets lexikon (CC BY-SA 2.5).\n')
        for po in (source / 'po').glob('*.po'):
            mo = dest / 'usr/share/locale' / po.stem / 'LC_MESSAGES/svlang.mo'
            mo.parent.mkdir(parents=True)
            run('msgfmt', '-o', str(mo), str(po))
    else:
        patterns = ['*.po', '*.tmx', 'stats.json'] if name == 'swedish-tm' else ['*.csv', '*.json', '*.tbx']
        for pattern in patterns:
            for path in source.glob(pattern):
                copy(path, share / path.name)
        shutil.copytree(source / 'scripts', share / 'scripts')
        (doc / 'copyright').write_text(f'Source: https://github.com/yeager/{name}\nLicense: CC-BY-4.0\n'
                                       'Attribution and source information: see README.md and bundled data.\n'
                                       'https://creativecommons.org/licenses/by/4.0/\n')


def main():
    os.umask(0o022)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sources', type=Path, required=True, help='directory containing the three source clones')
    parser.add_argument('--work', type=Path, required=True, help='new build directory')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    work, output = args.work.resolve(), args.output.resolve()
    work.mkdir(parents=True, exist_ok=False)
    output.mkdir(parents=True, exist_ok=True)
    top = work / 'rpmbuild'
    for directory in ('SOURCES', 'SPECS', 'BUILD', 'BUILDROOT', 'RPMS', 'SRPMS'):
        (top / directory).mkdir(parents=True)
    manifest = {}
    for name, info in TARGETS.items():
        repo = (args.sources / name).resolve()
        head = subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip()
        if head != info['commit'] or subprocess.check_output(['git', '-C', str(repo), 'status', '--porcelain']):
            raise SystemExit(f'{name}: expected clean checkout at {info["commit"]}')
        timestamp = int(subprocess.check_output(['git', '-C', str(repo), 'show', '-s', '--format=%ct', 'HEAD']))
        source = work / (name + '-source')
        source.mkdir()
        # Verify each exported byte against the pinned Git blob. This also
        # catches corruption in temporary source archives or staging copies.
        tree = subprocess.check_output(['git', '-C', str(repo), 'ls-tree', '-r', '-z', info['commit']])
        for entry in tree.split(b'\0'):
            if not entry:
                continue
            meta, filename = entry.split(b'\t', 1)
            mode, kind, oid = meta.decode().split()
            relative = filename.decode()
            if kind != 'blob' or mode not in ('100644', '100755'):
                raise SystemExit(f'unsupported source entry: {relative}')
            data = (repo / relative).read_bytes()
            actual = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
            if actual != oid:
                raise SystemExit(f'{name}: source checksum mismatch for {relative}')
            target = source / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            target.chmod(int(mode, 8) & 0o777)
            if target.read_bytes() != data:
                raise SystemExit(f'{name}: staging checksum mismatch for {relative}')
        payload = work / (name + '-payload')
        stage(name, source, payload, info)
        # Avoid checkout/build timestamps in the package payload.
        for path in sorted(payload.rglob('*'), reverse=True):
            if not path.is_symlink():
                path.chmod(0o755 if path.is_dir() or path.stat().st_mode & 0o111 else 0o644)
                os.utime(path, (timestamp, timestamp))
        source_tar = top / 'SOURCES' / (name + '-payload.tar')
        with tarfile.open(source_tar, 'w') as tar:
            def normalize(member):
                member.uid = member.gid = 0
                member.uname = member.gname = 'root'
                member.mtime = timestamp
                return member
            tar.add(payload / 'usr', arcname='usr', filter=normalize)
        recommends_rpm = 'Recommends: python3dist(polib), hunspell, hunspell-sv' if name == 'svlang' else ('Recommends: python3dist(polib), gettext' if name == 'swedish-tm' else '')
        spec = f'''Name: {name}
Version: {info['version']}
Release: {info['release']}
Summary: {info['summary']}
License: {info['license']}
URL: https://github.com/yeager/{name}
Source0: {source_tar.name}
BuildArch: noarch
AutoReqProv: no
Requires: python3 >= 3.10
{recommends_rpm}

%description
{info['summary']}.
Built from upstream commit {info['commit']}.

%prep
%setup -q -c -T
tar -xf %{{SOURCE0}}

%build

%install
mkdir -p %{{buildroot}}
cp -a usr %{{buildroot}}/

%files
%defattr(-,root,root,-)
/usr/share/{name}
%doc /usr/share/doc/{name}
'''
        if name == 'svlang':
            spec += '/usr/bin/svlang\n/usr/share/man/man1/svlang.1.gz\n/usr/share/locale/*/LC_MESSAGES/svlang.mo\n'
        spec_path = top / 'SPECS' / (name + '.spec')
        spec_path.write_text(spec)
        env = {**os.environ, 'SOURCE_DATE_EPOCH': str(timestamp)}
        run('rpmbuild', '-bb', '--define', f'_topdir {top}', '--define', '_rpmformat 4',
            '--define', '_binary_payload w7.xzdio', '--define', '__os_install_post %{nil}',
            '--define', 'use_source_date_epoch_as_buildtime 1', str(spec_path), env=env)
        rpm = next((top / 'RPMS/noarch').glob(name + '-' + info['version'] + '-*.rpm'))
        copy(rpm, output / rpm.name)
        debroot = work / (name + '-deb')
        shutil.copytree(payload, debroot, symlinks=True)
        control = debroot / 'DEBIAN'
        control.mkdir()
        recommends_deb = 'Recommends: python3-polib, hunspell, hunspell-sv\n' if name == 'svlang' else ('Suggests: python3-polib, gettext\n' if name == 'swedish-tm' else '')
        size = sum(p.stat().st_size for p in payload.rglob('*') if p.is_file() and not p.is_symlink())
        (control / 'control').write_text(f'''Package: {name}
Version: {info['version']}-{info['release']}
Architecture: all
Maintainer: Daniel Nylander <daniel@danielnylander.se>
Section: text
Priority: optional
Depends: python3 (>= 3.10)
{recommends_deb}Installed-Size: {(size + 1023) // 1024}
Homepage: https://github.com/yeager/{name}
Description: {info['summary']}
 Built from upstream commit {info['commit']}.
''')
        (control / 'md5sums').write_text(''.join(
            f'{hashlib.md5(p.read_bytes()).hexdigest()}  {p.relative_to(debroot)}\n'
            for p in sorted((debroot / 'usr').rglob('*')) if p.is_file() and not p.is_symlink()))
        deb = output / f'{name}_{info["version"]}-{info["release"]}_all.deb'
        run('dpkg-deb', '--build', '--root-owner-group', '-Zxz', '-z6', str(debroot), str(deb), env=env)
        manifest[name] = {**info, 'packages': {p.name: {'sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'size': p.stat().st_size}
                                             for p in (output / rpm.name, deb)}}
        print(f'Built RPM and DEB for {name}', flush=True)
    (output / 'build-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')


if __name__ == '__main__':
    main()
