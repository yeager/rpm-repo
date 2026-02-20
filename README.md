# RPM Package Repository

DNF/YUM repository for Daniel Nylander's localization, accessibility, and development tools. **45 packages** available.

## Quick Setup

### Fedora 41+ / DNF 5

```bash
sudo dnf config-manager addrepo --from-repofile=https://yeager.github.io/rpm-repo/yeager.repo
```

### Fedora 40 and older / DNF 4

```bash
sudo dnf config-manager --add-repo https://yeager.github.io/rpm-repo/yeager.repo
```

### Manual Setup

Create `/etc/yum.repos.d/yeager.repo`:

```ini
[yeager]
name=Yeager's Translation Tools
baseurl=https://yeager.github.io/rpm-repo/packages
enabled=1
gpgcheck=0
```

## Install Packages

```bash
sudo dnf install PACKAGE
```

## Available Packages

### Localization — GUI (GTK4/Adwaita)

| Package | Description |
|---------|-------------|
| cldr-viewer | Browse and compare Unicode CLDR locale data |
| commonvoice-status | Mozilla Common Voice recording statistics |
| desktop-editor | Visual .desktop file editor with translation support |
| fedora-l10n | Fedora translation progress via Weblate |
| font-preview | Preview and compare installed fonts |
| github-l10n | Scan GitHub repos for missing translations |
| gnome-l10n | GNOME translation statistics viewer |
| l10n-glossary | Translation glossary editor (TBX/CSV/TSV) |
| l10n-preview | Preview translations with quality indicators |
| libretranslate-gui | Translation assistant via LibreTranslate |
| linguaedit | Professional PO file editor (PySide6) |
| locale-tester | Inspect and compare system locale settings |
| snap-l10n | Translation status of installed Snap packages |
| tm-manager | TMX translation memory manager |

### Localization — CLI

| Package | Description |
|---------|-------------|
| l10n-conv | Universal l10n file converter |
| l10n-lint | Translation file linter |
| makebread | Build tool for translation projects |
| po-diff | Diff two PO files |
| po-translate | Machine-translate PO files |
| svlang | Swedish language tools |
| tp-lint | Translation project linter |

### Accessibility / Barn & Tillgänglighet

| Package | Description |
|---------|-------------|
| bildordbok | Visual dictionary with ARASAAC pictograms |
| bildschema | Visual scheduling with ARASAAC pictograms |
| bildstod | Visual communication aid with ARASAAC pictograms |
| ordbyggaren | Word building tool for language development |
| pecsbrada | PECS communication board with ARASAAC pictograms |
| rutinkompis | Routine companion with ARASAAC pictograms |
| tidskollen | Visual time management tool |

### Network & Security

| Package | Description |
|---------|-------------|
| cert-watch | TLS certificate monitor |
| cve-monitor | CVE vulnerability tracker |
| firewall-manager | Firewall rule manager |
| mqtt-dashboard | MQTT broker dashboard |
| mqtt-inspector | MQTT message inspector |
| packetlens | Network packet capture viewer (pcap/pcapng) |
| wifi-analyzer | Wi-Fi network analyzer |

### System Tools

| Package | Description |
|---------|-------------|
| log-viewer | Structured log file viewer |
| process-explorer | Process and resource monitor |
| regex-tester | Regular expression testing tool |

### IoT

| Package | Description |
|---------|-------------|
| ha-l10n | Home Assistant translation status viewer |
| obd2-viewer | OBD-II vehicle diagnostics viewer |
| tts-tester | Text-to-speech engine tester |
| zigbee-manager | Zigbee device manager |

### Other

| Package | Description |
|---------|-------------|
| scummvm-gtk | GTK4 game launcher for ScummVM |
| vsdview | Microsoft Visio file viewer for Linux |

## License

All tools are GPL-3.0-or-later by Daniel Nylander <daniel@danielnylander.se>.
