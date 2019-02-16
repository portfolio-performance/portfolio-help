---
title: Installation
---

# Installation

Komprimierte Datei laden, auspacken und per Doppelklick starten.

Die XML/Portfolio Datei mit den eigenen Daten (Wertpapiere, Depots und Konten, Buchungen) speichert man am besten irgendwo unter *Eigene Dokumente*.

## macOS

Portfolio Performance ist nicht mit einem Apple Zertifikat signiert. Darum kann es beim ersten Öffnen zu einer Meldung wie dieser kommen:

> “Portfolio Performance" kann nicht geöffnet werden, da es von einem nicht verifizierten Entwickler stammt

Für den ersten Start muss man zunächst per Kontextmenü (rechte Maustaste) den Menüpunkt *Öffnen* und in der anschließenden Meldung nochmals *Öffnen* wählen.

## Linux

Portfolio Performance nutzt [Eclipse SWT](https://www.eclipse.org/swt/) und damit unter Linux native Bibliotheken. Standardmässig wird dabei **GTK3** verwendet, allerdings gibt es bei verschiedenen Kombinationen mit Themes immer mal wieder Probleme. So meldete zum Beispiel ein Benutzer Probleme im Zusammenhang mit ["oxygen-gtk" Theme](https://github.com/buchen/portfolio/issues/1089#issuecomment-459698493).

PP kann man mit folgender Anweisung auf GTK2 zwingen:
```
env SWT_GTK3=0 PortfolioPerformance
```

## Workspace Verzeichnis

Im *Workspace* Verzeichnis speichert PP temporäre Informationen wie die aktuelle Fenstergröße, die zuletzt geöffneten Dateien und Verzeichnisse und andere Laufzeitinformationen.

Das Workspace Verzeichnis liegt:

* unter macOS: **~/Library/Application Support/name.abuchen.portfolio.product/workspace**
* unter Windows: **$LOCALAPPDATA$\PortfolioPerformance\workspace** wobei $LOCALAPPDATA$ überlicherweise nach **C:\Users\\{Benutzername}\AppData\Local** zeigt
* unter Linux: **~/.PortfolioPerformance/workspace**

!!! note "macOS"
    Das "Library" Verzeichnis ist ein verstecktes Verzeichnis. Am einfachsten ist es im Finder über das Menü *Gehe zu* -> *Gehe zum Ordner...* den Ordner "~/Library/" (ohne Anführungszeichen) zu öffnen.

!!! note "Windows"
    Das "LOCALAPPDATA" Verzeichnis ist ein verstecktes Verzeichnis. Am einfachsten ist es die Tastenkombination [Windows] + [R] zu drücken und im "Ausführen"-Fenster "%localappdata%" (ohne Anführungszeichen) eingeben.
