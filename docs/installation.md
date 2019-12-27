---
title: Installation
---

# Installation

Komprimierte Datei laden, auspacken und per Doppelklick starten.

Die XML/Portfolio Datei mit den eigenen Daten (Wertpapiere, Depots und Konten, Buchungen) speichert man am besten irgendwo unter *Eigene Dokumente*.

## macOS

Portfolio Performance ist nicht mit einem Apple Zertifikat signiert. Aus diesem Grund behandelt der [macOS Gatekeeper](https://en.wikipedia.org/wiki/Gatekeeper_(macOS)) die Anwendung beim ersten Starten besonders. Mit folgenden Schritten lässt sich PP leicht starten:


* PP laden und auspacken (zum Beispiel im "Downloads" Verzeichnis)
* PP nach "Anwendungen" verschieben
* PP per Rechtsklick und "Öffnen" starten (per Kontextmenü (rechte Maustaste) den Menüpunkt "Öffnen" und in der anschließenden Meldung nochmals "Öffnen" wählen)

## Linux

Portfolio Performance nutzt [Eclipse SWT](https://www.eclipse.org/swt/) und damit unter Linux native Bibliotheken. Standardmässig wird dabei **GTK3** verwendet, allerdings gibt es bei verschiedenen Kombinationen mit Themes immer mal wieder Probleme. So meldete zum Beispiel ein Benutzer Probleme im Zusammenhang mit ["oxygen-gtk" Theme](https://github.com/buchen/portfolio/issues/1089#issuecomment-459698493).

Die notwendigen Abhängigkeiten lassen sich unter Ubuntu 18.04 mit `sudo apt install libwebkitgtk-3.0-0 default-jre` installieren.

Das Programm lässt sich mit folgendem Skript installieren:
```
#!/bin/bash

# Download/unpack current release to /opt/PortfolioPerformance/
pm_repo=buchen/portfolio #GitHub Repo
pm_release=`wget -qO- \
"https://api.github.com/repos/$pm_repo/releases/latest" \
| grep -Po '"tag_name": "\K.*?(?=")'` 
pm_file=PortfolioPerformance-$pm_release-linux.gtk.x86_64.tar.gz
pm_dl=https://github.com/$pm_repo/releases/download/$pm_release/$pm_file
pm_location=/opt/PortfolioPerformance/
sudo mkdir -p $pm_location
sudo wget $pm_dl -P $pm_location
sudo tar xfzv $pm_location/$pm_file -C $pm_location --strip 1
sudo rm $pm_location/$pm_file

# Create menu item
echo -e "[Desktop Entry]\n"\
"Version=$pm_release\n"\
"Name=Portfolio Performance\n"\
"Comment=Calculates the performance of an entire portfolio\n"\
"Comment[de]=Berechnet die Performance eines Gesamtportfolios\n"\
"Exec=$pm_location/PortfolioPerformance\n"\
"Terminal=false\n"\
"Encoding=UTF-8\n"\
"Type=Application\n"\
"Icon=$pm_location/icon.xpm\n"\
"Categories=Office;Finance\n"\
| sudo tee  /usr/share/applications/PortfolioPerformance.desktop
```


Wenn es Probleme gibt, dann bieten sich folgende Optionen an:

* Alternatives GTK3 Theme ausprobieren
* PP auf GTK2 zwingen: ```env SWT_GTK3=0 PortfolioPerformance```
* Alternative input method nutzen: ```env GTK_IM_MODULE=ibus PortfolioPerformance```

## Workspace Verzeichnis

Im *Workspace* Verzeichnis speichert PP temporäre Informationen wie die aktuelle Fenstergröße, die zuletzt geöffneten Dateien und Verzeichnisse und andere Laufzeitinformationen.

Das Workspace Verzeichnis liegt:

* unter macOS: **~/Library/Application Support/name.abuchen.portfolio.product/workspace**
* unter Windows: **%LOCALAPPDATA%\PortfolioPerformance\workspace** wobei %LOCALAPPDATA% überlicherweise nach **C:\Users\\{Benutzername}\AppData\Local** zeigt
* unter Linux: **~/.PortfolioPerformance/workspace**

!!! note "macOS"
    Das "Library" Verzeichnis ist ein verstecktes Verzeichnis. Am einfachsten ist es im Finder über das Menü *Gehe zu* -> *Gehe zum Ordner...* den Ordner "~/Library/" (ohne Anführungszeichen) zu öffnen.

!!! note "Windows"
    Das "LOCALAPPDATA" Verzeichnis ist ein verstecktes Verzeichnis. Am einfachsten ist es die Tastenkombination [Windows] + [R] zu drücken und im "Ausführen"-Fenster "%localappdata%" (ohne Anführungszeichen) eingeben.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI4MDIwMjM3NV19
-->
