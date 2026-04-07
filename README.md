# Yeager RPM Repository

RPM packages for Linux tools and apps, published via GitHub Pages.

The repository currently contains **247 RPM packages**, including:
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
