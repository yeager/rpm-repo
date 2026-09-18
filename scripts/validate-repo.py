#!/usr/bin/env python3
"""Verify RPM metadata and every referenced package checksum before publishing."""
import hashlib
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = {'r': 'http://linux.duke.edu/metadata/repo', 'p': 'http://linux.duke.edu/metadata/common'}
metadata = ET.parse(ROOT / 'repodata/repomd.xml').getroot()
primary = None
for entry in metadata.findall('r:data', NS):
    path = ROOT / entry.find('r:location', NS).get('href')
    data = path.read_bytes()
    checksum = entry.find('r:checksum', NS)
    assert hashlib.new(checksum.get('type'), data).hexdigest() == checksum.text, path
    assert len(data) == int(entry.findtext('r:size', namespaces=NS)), path
    decoded = subprocess.check_output(['zstd', '-dq', '--stdout', str(path)])
    checksum = entry.find('r:open-checksum', NS)
    assert hashlib.new(checksum.get('type'), decoded).hexdigest() == checksum.text, path
    assert len(decoded) == int(entry.findtext('r:open-size', namespaces=NS)), path
    if entry.get('type') == 'primary':
        primary = ET.fromstring(decoded)
assert primary is not None
packages = primary.findall('p:package', NS)
assert len(packages) == int(primary.get('packages'))
indexed = set()
for package in packages:
    name = package.find('p:location', NS).get('href')
    assert name not in indexed, name
    indexed.add(name)
    path = (ROOT / name).resolve()
    assert path.is_relative_to((ROOT / 'packages').resolve()), name
    data = path.read_bytes()
    assert len(data) == int(package.find('p:size', NS).get('package')), name
    checksum = package.find('p:checksum', NS)
    assert hashlib.new(checksum.get('type'), data).hexdigest() == checksum.text, name
assert indexed == {str(p.relative_to(ROOT)) for p in (ROOT / 'packages').glob('*.rpm')}
print(f'{len(packages)} RPMs verified against published metadata')
