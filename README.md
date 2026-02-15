# RPM Package Repository

DNF/YUM repository for Daniel Nylander's localization and development tools.

## Quick Setup

```bash
sudo dnf config-manager --add-repo https://yeager.github.io/rpm-repo/yeager.repo
```

## Install Packages

```bash
sudo dnf install PACKAGE
```

## Available Packages

### GUI Applications (GTK4/Adwaita)

| Package | Description |
|---------|-------------|
| cldr-viewer | Browse and compare Unicode CLDR locale data |
| commonvoice-status | Mozilla Common Voice recording statistics |
| ddtp-translate | Translate Debian package descriptions via DDTP |
| desktop-editor | Visual .desktop file editor with translation support |
| elementary-l10n | elementary OS translation status via Weblate |
| fedora-l10n | Fedora translation progress via Weblate |
| font-preview | Preview and compare installed fonts |
| github-l10n | Scan GitHub repos for missing translations |
| l10n-glossary | Translation glossary editor (TBX/CSV/TSV) |
| l10n-preview | Preview translations with quality indicators |
| langpack-inspector | Inspect Ubuntu language pack coverage |
| libretranslate-gui | Translation assistant via LibreTranslate |
| locale-tester | Inspect and compare system locale settings |
| pcap-viewer | Analyze pcap/pcapng network captures |
| snap-l10n | Translation status of installed Snap packages |
| tm-manager | TMX translation memory manager |
| ubuntu-l10n | Ubuntu translation statistics from Launchpad |

### CLI Tools

| Package | Description |
|---------|-------------|
| l10n-lint | Translation file linter |
| l10n-conv | Universal l10n file converter |
| po-translate | Machine-translate PO files |
| po-diff | Diff two PO files |
| tp-lint | Translation project linter |
| svlang | Swedish language tools |
| makebread | Build tool for translation projects |

## License

All tools are GPL-3.0-or-later by Daniel Nylander <daniel@danielnylander.se>.
