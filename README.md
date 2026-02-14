# Yeager's RPM Repository

RPM packages for Fedora, openSUSE, RHEL, and other RPM-based distributions.

## Quick Install

```bash
# Add repository
sudo tee /etc/yum.repos.d/yeager.repo << 'EOF'
[yeager]
name=Yeager's Translation Tools
baseurl=https://yeager.github.io/rpm-repo/packages/
enabled=1
gpgcheck=0
EOF

# Install packages
sudo dnf install locale-tester l10n-preview desktop-editor tm-manager l10n-glossary font-preview fedora-l10n
```

## Available Packages

### Translation Tools (GTK4/Adwaita)
| Package | Version | Description |
|---------|---------|-------------|
| **fedora-l10n** | 0.1.0 | Fedora translation status via Weblate API |
| **tm-manager** | 0.1.0 | Translation Memory manager (TMX) with fuzzy search |
| **l10n-glossary** | 0.1.0 | Glossary/terminology editor with consistency checking |
| **l10n-preview** | 0.1.0 | Preview PO/TS translations in simulated UI elements |
| **desktop-editor** | 0.1.0 | Visual .desktop file editor with validation |
| **locale-tester** | 0.1.0 | Compare locale settings side by side |
| **font-preview** | 0.1.0 | Font browser with Unicode coverage per language |

### CLI Tools
| Package | Version | Description |
|---------|---------|-------------|
| **l10n-conv** | 1.0.0 | Universal l10n file converter (16 formats) |
| **l10n-lint** | 1.14.9 | Linter for localization files (.po, .ts) |
| **po-translate** | 1.5.0 | Batch translate PO/XLIFF files with DeepL |
| **po-diff** | 1.0.0 | Compare and diff PO files |
| **makebread** | 0.3.0 | Bread machine recipe manager |

## Debian/Ubuntu

For .deb packages (including Ubuntu-specific tools), see [yeager/debian-repo](https://github.com/yeager/debian-repo).

## Source Code

All projects: [github.com/yeager](https://github.com/yeager)

## Requirements

- Python 3.10+
- GTK 4, libadwaita (for GUI apps)

## License

All packages are GPL-3.0-or-later.

## Author

Daniel Nylander — [daniel@danielnylander.se](mailto:daniel@danielnylander.se)
https://danielnylander.se
