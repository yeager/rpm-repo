#!/usr/bin/env python3
"""Import pinned RPM release assets and rebuild repository metadata."""
import hashlib
import json
import re
import subprocess
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = json.loads((ROOT / "maintenance/release-assets.json").read_text())
PACKAGES = ROOT / "packages"
PACKAGES.mkdir(exist_ok=True)


def header(path, source=None):
    out = subprocess.check_output([
        "rpm", "-qp", "--qf", "%{NAME}\\t%{EPOCHNUM}\\t%{VERSION}\\t%{RELEASE}\\t%{ARCH}\\n", str(path)
    ], text=True).strip().split("\t")
    if len(out) != 5:
        raise ValueError(f"Could not parse RPM header: {path}")
    if source is None:\n        source = path.name.endswith(".src.rpm")\n    if source:\n        out[-1] = "src"\n    return tuple(out)


def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

existing = {}
for path in PACKAGES.glob("*.rpm"):
    existing[header(path)] = path
changed = False
for asset in ASSETS:
    name = asset["name"]
    if not re.fullmatch(r"[A-Za-z0-9._+~-]+\.rpm", name):
        raise ValueError(f"Unsafe asset filename: {name!r}")
    target = PACKAGES / name
    temp = target.with_suffix(target.suffix + ".download")
    request = urllib.request.Request(asset["url"], headers={"User-Agent": "yeager-rpm-repo-import/1"})
    with urllib.request.urlopen(request, timeout=180) as response, temp.open("wb") as stream:
        while chunk := response.read(1024 * 1024):
            stream.write(chunk)
    if temp.stat().st_size != asset["size"]:
        raise ValueError(f"Size mismatch for {asset['repo']}:{name}")
    identity = header(temp, source=name.endswith(".src.rpm"))
    old_path = existing.get(identity)
    if old_path and old_path.name != name:
        if sha256(old_path) != sha256(temp):
            raise ValueError(f"Conflicting RPM NEVRA {identity}: {old_path.name} and {name}")
        temp.unlink()
        continue
    if target.exists() and sha256(target) == sha256(temp):
        temp.unlink()
        continue
    temp.replace(target)
    existing[identity] = target
    changed = True

count = len(list(PACKAGES.glob("*.rpm")))
readme = ROOT / "README.md"
content = readme.read_text()
content, n = re.subn(r"currently contains \*\*\d+ RPM packages\*\*", f"currently contains **{count} RPM packages**", content, count=1)
if n:
    readme.write_text(content)
subprocess.run(["createrepo_c", "--update", "--general-compress-type", "zstd", str(ROOT)], check=True)
print(f"Indexed {count} RPMs; changed={changed}")
