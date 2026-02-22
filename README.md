# Yeager RPM Repository

DNF-repo med översättningsverktyg, tillgänglighetsappar och systemverktyg av Daniel Nylander. **54 paket**.

## Installation

### Fedora 41+ / DNF 5

```bash
sudo dnf config-manager addrepo --from-repofile=https://yeager.github.io/rpm-repo/yeager.repo
```

### Fedora 40 / DNF 4

```bash
sudo dnf config-manager --add-repo https://yeager.github.io/rpm-repo/yeager.repo
```

### Manuell

Skapa `/etc/yum.repos.d/yeager.repo`:

```ini
[yeager]
name=Yeager Translation Tools
baseurl=https://yeager.github.io/rpm-repo/packages
enabled=1
gpgcheck=0
```

## Paket

### Översättning/L10n — GUI (GTK4/Adwaita)

| Paket | Version | Beskrivning |
|-------|---------|-------------|
| cldr-viewer | 0.1.9 | Unicode CLDR-data |
| commonvoice-status | 0.1.9 | Mozilla Common Voice statistik |
| ddtp-translate | 0.10.0 | Debian-paketbeskrivningar via DDTSS |
| desktop-editor | 0.2.8 | .desktop-filredigerare |
| fedora-l10n | 0.2.8 | Fedora översättningsstatus via Weblate |
| font-preview | 0.2.9 | Förhandsgranska typsnitt |
| github-l10n | 0.2.7 | GitHub-repon översättningsstatus |
| gnome-l10n | 0.2.1 | GNOME översättningsstatistik |
| l10n-glossary | 0.2.7 | Terminologiredigerare (TBX/CSV/TSV) |
| l10n-preview | 0.2.7 | Förhandsgranska översättningar |
| libretranslate-gui | 0.2.7 | LibreTranslate skrivbordsklient |
| linguaedit | 1.8.14 | PO-filredigerare (PySide6) |
| locale-tester | 0.2.7 | Testa locale-formatering |
| snap-l10n | 0.2.9 | Snap Store översättningsstatus |
| tm-manager | 0.2.9 | Översättningsminne (TMX/TBX) |
| vsdview | 0.4.2 | Microsoft Visio-filvisare |

### Översättning/L10n — CLI

| Paket | Version | Beskrivning |
|-------|---------|-------------|
| l10n-conv | 1.0.9 | Konvertera PO/XLIFF/TS/JSON |
| l10n-lint | 1.16.0 | Linter för översättningsfiler |
| po-diff | 1.0.1 | Jämför PO/TS-filer |
| po-translate | 1.5.6 | Batch-översätt med AI |
| svlang | 0.1.7 | Svensk språkkvalitetskontroll |
| tp-lint | 1.8.4 | Linter för översättningsprojekt |

### Barn/Tillgänglighet (GTK4/Adwaita)

| Paket | Version | Beskrivning |
|-------|---------|-------------|
| bildordbok | 0.3.2 | Bildordbok med ARASAAC |
| bildschema | 0.3.2 | Visuella scheman med ARASAAC |
| bildstod | 0.4.4 | Bildstöd med ARASAAC-piktogram |
| beloningskartan | 0.1.2 | Belöningskarta |
| fokuskompis | 0.2.2 | Fokushjälp med timer |
| kanslokartan | 0.1.2 | Känslokartan |
| ljudladan | 0.1.2 | Ljudbibliotek för avslappning |
| lugnarummet | 0.3.1 | Lugnt rum — avslappning |
| minnet | 0.1.2 | Minnesträningsspel |
| mittschema | 0.1.2 | Dagschema med bilder |
| ordbyggaren | 0.2.1 | Ordbyggare — stavningsträning |
| pecsbrada | 0.3.2 | PECS-kommunikationsbräda |
| rutinkompis | 0.3.2 | Rutinkompis med ARASAAC |
| socialaberattelser | 0.1.2 | Sociala berättelser |
| tidskollen | 0.2.1 | Visuell tidskoll |

### Nätverk/Säkerhet/System (GTK4/Adwaita)

| Paket | Version | Beskrivning |
|-------|---------|-------------|
| anpr-viewer | 0.2.0 | Registreringsskyltsigenkänning |
| cert-watch | 0.1.1 | TLS-certifikatövervakning |
| cve-monitor | 0.3.3 | CVE-sårbarhetsbevakning |
| firewall-manager | 0.1.1 | ufw/nftables-gränssnitt |
| ha-l10n | 0.2.1 | Home Assistant översättningsstatus |
| log-viewer | 0.1.1 | Journalctl-loggvisare |
| mqtt-dashboard | 0.1.1 | MQTT-dashboard |
| mqtt-inspector | 0.2.1 | MQTT-meddelandeinspektör |
| obd2-viewer | 0.2.1 | OBD2-diagnostikvisare |
| packetlens | 0.2.6 | Nätverkspaketanalys |
| process-explorer | 0.1.1 | Processhanterare |
| regex-tester | 0.1.1 | Visuell regex-testare |
| tts-tester | 0.2.1 | Text-till-tal-jämförelse |
| wifi-analyzer | 0.1.1 | WiFi-kanalanalys |
| zigbee-manager | 0.1.1 | Zigbee-enhetshanterare |

### Övrigt — GUI (GTK4/Adwaita)

| Paket | Version | Beskrivning |
|-------|---------|-------------|
| makebread | 0.4.0 | Recepthanterare för brödbak |
| scummvm-gtk | 0.1.0 | GTK4-gränssnitt för ScummVM |

## Underhållare

Daniel Nylander <daniel@danielnylander.se>
