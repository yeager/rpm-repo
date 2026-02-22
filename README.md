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

## Packages

53 packages. Same apps as the [Debian repository](https://github.com/yeager/debian-repo) minus Debian-specific tools.

## Author

Daniel Nylander — [danielnylander.se](https://danielnylander.se)
