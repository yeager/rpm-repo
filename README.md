# Yeager RPM Repository

DNF repository with translation tools, accessibility apps, and system utilities by Daniel Nylander.

## Installation

```bash
sudo dnf config-manager --add-repo https://yeager.github.io/rpm-repo/packages/yeager.repo
```

Or manually create `/etc/yum.repos.d/yeager.repo`:

```ini
[yeager]
name=Yeager L10n Suite
baseurl=https://yeager.github.io/rpm-repo/packages
enabled=1
gpgcheck=0
```

## Packages (71)

### Translation & Localization Tools
- **cldr-viewer** — CLDR locale data viewer
- **commonvoice-status** — Mozilla Common Voice status viewer
- **desktop-editor** — Desktop file editor
- **fedora-l10n** — Fedora translation status viewer
- **font-preview** — Font preview with multilingual samples
- **github-l10n** — GitHub translation status viewer
- **gnome-l10n** — GNOME translation status viewer
- **ha-l10n** — Home Assistant translation status
- **l10n-conv** — Translation file converter (CLI)
- **l10n-glossary** — Translation glossary manager
- **l10n-lint** — Localization file linter (CLI)
- **l10n-preview** — Translation preview tool
- **langpack-inspector** — Language pack inspector
- **libretranslate-gui** — LibreTranslate GUI frontend
- **locale-tester** — Locale testing tool
- **po-diff** — PO/TS file differ (CLI)
- **po-translate** — AI-powered PO/TS batch translator (CLI)
- **snap-l10n** — Snap package translation status
- **svlang** — Swedish language tools (CLI)
- **tm-manager** — Translation Memory manager
- **tp-lint** — Translation Project linter (CLI)
- **tp-status** — Translation Project status viewer
- **tts-tester** — Text-to-speech testing tool

### Accessibility & Autism Apps
- **beloningskartan** — Reward chart for children
- **bildordbok** — Visual dictionary with pictograms
- **bildschema** — Visual schedule board
- **bildstod** — Visual support tool
- **bokstavsresan** — Letter learning journey
- **dagboken** — Personal diary app
- **energimataren** — Energy level tracker
- **fokuskompis** — Focus & task manager (ADHD/autism)
- **ilskehanteraren** — Anger management tool
- **kanslokartan** — Emotion map
- **kladvaljaren** — Clothing chooser
- **klocklararen** — Clock/time teacher
- **ljudladan** — Sound library
- **lugnarummet** — Calm room/relaxation app
- **matlagaren** — Cooking assistant
- **meningsbyggaren** — Sentence builder
- **minnet** — Memory training game
- **mittschema** — Personal schedule
- **ordbyggaren** — Word building exercise
- **ovningstavlan** — Exercise board
- **pauskollen** — Break/pause checker
- **pecsbrada** — PECS communication board
- **pengakollen** — Money awareness tool
- **raknestod** — Math support tool
- **rutinkompis** — Routine & habit tracker
- **samtalsstod** — Conversation support
- **socialaberattelser** — Social stories
- **stegvisaren** — Step-by-step guide
- **tidskollen** — Time awareness viewer
- **valjaren** — Choice maker

### System & Network Tools
- **anpr-viewer** — License plate recognition viewer
- **cert-watch** — TLS certificate monitor
- **cve-monitor** — CVE vulnerability monitor
- **firewall-manager** — Firewall management GUI
- **log-viewer** — System log viewer
- **mqtt-dashboard** — MQTT dashboard
- **mqtt-inspector** — MQTT message inspector
- **obd2-viewer** — OBD2 car diagnostics viewer
- **packetlens** — Network packet analyzer
- **pcap-viewer** — PCAP file viewer
- **process-explorer** — System process explorer
- **regex-tester** — Regular expression tester
- **scummvm-gtk** — ScummVM GTK frontend
- **sysinfo-gtk** — System information viewer
- **vsdview** — Visio file viewer
- **wifi-analyzer** — WiFi network analyzer
- **zigbee-manager** — Zigbee device manager

### Build Tools
- **makebread** — Build automation tool

## Author

Daniel Nylander — [danielnylander.se](https://danielnylander.se)
