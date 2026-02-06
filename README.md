# Yeager's RPM Repository

RPM packages for Fedora, RHEL, CentOS, and other RPM-based distributions.

## Quick Install

```bash
# Add repository
sudo tee /etc/yum.repos.d/yeager.repo << 'EOF'
[yeager]
name=Yeager's Translation Tools
baseurl=https://yeager.github.io/rpm-repo
enabled=1
gpgcheck=0
EOF

# Install packages
sudo dnf install l10n-lint po-translate tp-lint
```

## Available Packages

| Package | Description |
|---------|-------------|
| **l10n-lint** | Linter for localization files (.po, .ts) |
| **po-translate** | Batch translate PO and TS files |
| **tp-lint** | Translation Project linter and statistics |

## Manual Download

Packages available in [packages/noarch/](packages/noarch/).

## Debian/Ubuntu

For APT packages, see [yeager/debian-repo](https://github.com/yeager/debian-repo).

```bash
curl -fsSL https://yeager.github.io/debian-repo/yeager.gpg | sudo gpg --dearmor -o /usr/share/keyrings/yeager.gpg
echo 'deb [signed-by=/usr/share/keyrings/yeager.gpg] https://yeager.github.io/debian-repo stable main' | sudo tee /etc/apt/sources.list.d/yeager.list
sudo apt update && sudo apt install l10n-lint
```

## Source Code

| Project | Repository |
|---------|------------|
| l10n-lint | [github.com/yeager/l10n-lint](https://github.com/yeager/l10n-lint) |
| po-translate | [github.com/yeager/po-translate](https://github.com/yeager/po-translate) |
| tp-lint | [github.com/yeager/tp-lint](https://github.com/yeager/tp-lint) |

## Requirements

- Python 3.8+

## License

All packages are GPL-3.0-or-later.

---
*RPM packages are built automatically from debian-repo releases.*
