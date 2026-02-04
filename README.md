# RPM Repository

RPM packages for Fedora, RHEL, CentOS, and other RPM-based distributions.

## Packages

| Package | Version | Description |
|---------|---------|-------------|
| l10n-lint | 1.3.6 | Linter for localization files (.po, .ts) |
| tp-lint | 1.5.6 | Translation Progress linter and report generator |
| po-translate | 1.3.3 | Batch translate .po and .ts files |

## Installation

### Manual download

Download packages from the [packages/noarch](packages/noarch/) directory.

### Using dnf/yum

```bash
# Download and install directly
sudo dnf install https://yeager.github.io/rpm-repo/packages/noarch/l10n-lint-1.3.6-2.noarch.rpm
sudo dnf install https://yeager.github.io/rpm-repo/packages/noarch/tp-lint-1.5.6-2.noarch.rpm
sudo dnf install https://yeager.github.io/rpm-repo/packages/noarch/po-translate-1.3.3-2.noarch.rpm
```

## Requirements

- Python 3.6+
