# Yeager RPM Repository

RPM packages for Linux tools and apps, published via GitHub Pages.

The repository currently contains **250 RPM packages**, including:
- ANPR Viewer
- PaintBrush
- Signal Lantern
- and related localization/development tools

## Setup

```bash
sudo dnf config-manager addrepo --from-repofile=https://yeager.github.io/rpm-repo/yeager.repo
sudo dnf makecache
```

## Install Signal Lantern

```bash
sudo dnf install signal-lantern
```

## Notes

- Repository URL: <https://yeager.github.io/rpm-repo>
- RPM metadata is published under `repodata/`
- The repository currently includes `signal-lantern-0.1.0-1.fc43.noarch.rpm`

## Swedish language tools

```bash
sudo dnf upgrade --refresh svlang
sudo dnf install swedish-tm swedish-foss-terminology
```

- `svlang-0.2.0-2.noarch.rpm` includes both lexicons and the corrected language checks.
- `swedish-tm-20260918-1.noarch.rpm` installs the repaired PO/TMX data in `/usr/share/swedish-tm/`.
- `swedish-foss-terminology-20260918-1.noarch.rpm` installs the corrected termbank and export script in `/usr/share/swedish-foss-terminology/`.

All three packages are architecture independent and require Python 3.10 or later.
The svlang launcher uses its private `/usr/share/svlang/` module directory so it
works across supported Python versions. Optional Hunspell and polib support is
expressed as recommended dependencies. Source revisions and SHA-256 checksums
are recorded in `maintenance/swedish-tools-20260918.json` and inside each package.

### Building these snapshots

Install `rpm`, `dpkg`, `gettext`, `tar`, `xz` and Python 3.10+ for the build script.
Check out the three source repositories at the commits recorded in the script,
then run (the build directory must not already exist):

```bash
python3 packaging/build-swedish-tools.py --sources /path/to/source-clones --work /tmp/swedish-package-build --output /tmp/swedish-packages
```

The builder produces both RPM v4 packages and matching DEB packages. No
host-specific Python bytecode or backup files are included. Regenerate repository
metadata with `createrepo_c --update .`, then validate with
`python3 scripts/validate-repo.py` (requires `zstd`) before committing to `main`.
