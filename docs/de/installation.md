---
title: Installation
---

# Installation

Komprimierte Datei laden, auspacken und per Doppelklick starten.

Die XML/Portfolio Datei mit den eigenen Daten (Wertpapiere, Depots und Konten, Buchungen) speichert man am besten irgendwo unter *Eigene Dokumente*.

## macOS

- [Lade die DMG-Datei von Portfolio Performance herunter](https://www.portfolio-performance.info) (entweder für Intel oder für Apple Silicon)
- Doppelklicke die DMG-Datei, um sie zu öffnen.
- Ziehe das App-Symbol in den "Programme"-Ordner.

## Linux

Die präferierte Option ist [Portfolio Performance von Flathub](https://flathub.org/apps/info.portfolio_performance.PortfolioPerformance) zu installieren.


Alternativ kannst Du PP auch manuell installieren:

* Für Portfolio Performance ist aktuell (März 2023) Java 17 erforderlich. 
Falls noch nicht vorhanden (Beispiel für Systeme mit Debianbezug, wie z.B. Ubuntu):
```
sudo apt install openjdk-17-jre
```

* Lade und entpacke das GZIP Archive (entweder für x86_64 oder aarch64) an eine passende Stelle, z.B. /opt

## Windows

Die präferierte Option ist der [Windows-Installer](https://www.portfolio-performance.info). Damit wird PP (üblicherweise) in das Verzeichnis **C:\Users\{Benutzername}\AppData\Local\Programs\PortfolioPerformance** installiert wird. Diese Installation kann dann im Anschluss über die Online Aktualisierung einfach aktualisiert werden.

Wichtig in diesem Zusammenhang:
Bitte nicht erschrecken sollte euch der Windows Defender die Installation von Portfolio Performance blockieren. Der Grund hierfür ist die nicht vorhandene Signatur von Microsoft, Zertifikate sind sehr teuer, daher wurde bisher darauf verzichtet.

## Workspace Verzeichnis

Im *Workspace* Verzeichnis speichert PP temporäre Informationen wie die aktuelle Fenstergröße, die zuletzt geöffneten Dateien und Verzeichnisse und andere Laufzeitinformationen.

Das Workspace Verzeichnis liegt:

* unter macOS: **~/Library/Application Support/name.abuchen.portfolio.product/workspace**
* unter Windows: **%LOCALAPPDATA%\PortfolioPerformance\workspace** wobei %LOCALAPPDATA% üblicherweise nach **C:\Users\\{Benutzername}\AppData\Local** zeigt
* unter Linux: **~/.PortfolioPerformance/workspace**

!!! note "macOS"
    Das "Library" Verzeichnis ist ein verstecktes Verzeichnis. Am einfachsten ist es im Finder über das Menü *Gehe zu* -> *Gehe zum Ordner...* den Ordner "~/Library/" (ohne Anführungszeichen) zu öffnen.

!!! note "Windows"
    Das "LOCALAPPDATA" Verzeichnis ist ein verstecktes Verzeichnis. Am einfachsten ist es die Tastenkombination [Windows] + [R] zu drücken und im "Ausführen"-Fenster "%localappdata%" (ohne Anführungszeichen) eingeben.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI4MDIwMjM3NV19
-->
