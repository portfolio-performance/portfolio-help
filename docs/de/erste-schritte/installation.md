---
title: Installation
description: Anleitung zur Installation von Portfolio Performance auf Windows, macOS und Linux – inklusive Installationsdateien, Paketmanagern und Flatpak.
changes:
  - date: 2025-05-03
    author: Nirus2000
    description: Java 17 auf Java 21 aktualisiert, Bilder entfernt, da sie zu komplex zu pflegen sind und keinen Mehrwert bieten, Synchronisation des Installationsprozesses zwischen Deutsch und Englisch
---

Portfolio Performance ist für macOS, Windows und Linux verfügbar. Sie können die Anwendung auf verschiedene Arten herunterladen, wie unten beschrieben. Der einfachste Weg, die neueste Version zu erhalten, sind in der Regel die Installationsdateien, die auf der [Homepage](https://www.portfolio-performance.info/) verlinkt sind. Dort finden Sie auch einen Link zu den Versionshinweisen.

# Versionsnummer in Dateinamen

In den Dateinamen der Installationsprogramme und ZIP-Dateien finden Sie typischerweise eine Versionsnummer im Format `X.X.X`. Die erste Zahl (`X`) steht für die Hauptversion, größere Änderungen oder neue Kernfunktionen können hier zu einer Erhöhung führen. Die zweite Zahl (`XX`) bezeichnet eine Nebenversion, die in der Regel neue Funktionen oder Verbesserungen beinhaltet. Die dritte Zahl (`X`) kennzeichnet eine Patch-Version, die meist Fehlerbehebungen und kleinere Verbesserungen enthält.

# Windows

Es gibt zwei Hauptwege, Portfolio Performance unter Windows zu installieren: über den Installer oder eine ZIP-Datei.

**Windows Installer (setup.exe):**

1.  Laden Sie den Windows Installer (z. B. `PortfolioPerformance-X.X.X-setup.exe`) von der [Homepage](https://www.portfolio-performance.info/) herunter.
2.  Unter Windows 11 sehen Sie möglicherweise eine Sicherheitswarnung bezüglich der Ausführung einer ausführbaren Datei. Klicken Sie auf "Weitere Informationen" und dann auf "Trotzdem ausführen", um fortzufahren.
3.  Doppelklicken Sie auf die heruntergeladene `.exe`-Datei, um den Installationsprozess zu starten.
4.  Sie können den Zielordner während der Installation ändern. Standardmäßig wird im Benutzerverzeichnis installiert (z. B. `C:\Users\<IhrBenutzername>\Portfolio Performance`).
5.  Die Installation benötigt ungefähr 200 MB freien Speicherplatz.

**ZIP-Datei:**

1.  Laden Sie die komprimierte ZIP-Datei von der [Homepage](https://www.portfolio-performance.info/) herunter.
2.  Wählen Sie ein Verzeichnis auf Ihrem Computer oder sogar einen tragbaren USB-Stick (mit mindestens 250 MB freiem Speicherplatz), um den Inhalt der ZIP-Datei zu entpacken.
3.  Nach dem Entpacken können Sie Portfolio Performance ausführen, indem Sie auf die ausführbare Datei im entpackten Ordner doppelklicken. Diese Methode ermöglicht es Ihnen, Portfolio Performance ohne herkömmliche Installation auszuführen und macht es portabel.

**Bezüglich 32-Bit vs. 64-Bit Windows:** Die auf der Homepage verfügbaren Portfolio Performance Installer und ZIP-Dateien sind in der Regel so konzipiert, dass sie sowohl auf 64-Bit-Versionen von Windows funktionieren. **Bitte beachten Sie, dass die Unterstützung und Pflege für 32-Bit-Versionen von Windows eingestellt wurde.** Die Anwendung selbst basiert auf Java, das die zugrunde liegende Systemarchitektur handhabt. Sollten Sie Probleme haben, stellen Sie sicher, dass Sie eine kompatible Java-Version installiert haben (normalerweise die neueste empfohlene Version).

# macOS

Sie können Portfolio Performance unter macOS entweder manuell über eine DMG-Datei oder über Paketmanager wie Brew oder MacPorts installieren.

**Manuelle Installation (DMG-Datei):**

1.  Besuchen Sie die [Homepage](https://www.portfolio-performance.info/) und laden Sie das passende macOS-Paket für Ihren Mac herunter:
    * **macOS - Intel:** Für Macs mit Intel-Prozessoren.
    * **macOS - Silicon (aarch64):** Für Macs mit Apple Silicon Prozessoren (M1, M2 usw.).
2.  Die heruntergeladene Datei ist eine DMG-Datei (Disk Image), typischerweise benannt wie `PortfolioPerformance-0.XX.X-aarch64.dmg` (für Apple Silicon) oder `PortfolioPerformance-0.XX.X-x86_64.dmg` (für Intel). Eine DMG-Datei ist ein Standard-macOS-Format zur Verteilung von Software.
3.  Doppelklicken Sie auf die DMG-Datei, um sie zu mounten. Ein virtuelles Laufwerk mit der Portfolio Performance Anwendung erscheint im Finder.
4.  Ziehen Sie das **PortfolioPerformance** Symbol vom gemounteten Laufwerk in den **Programme** Ordner. Dadurch wird die Anwendung auf Ihr System kopiert.
5.  Nach dem Kopieren können Sie das virtuelle Laufwerk auswerfen, indem Sie auf das Auswurfsymbol in der Finder-Seitenleiste klicken oder mit der rechten Maustaste darauf klicken und "Auswerfen" wählen. Sie können auch die heruntergeladene DMG-Datei löschen, um Speicherplatz zu sparen.

**Installation mit Paketmanagern:**

Wenn Sie einen Paketmanager wie Brew oder MacPorts auf Ihrem Mac installiert haben, können Sie ihn verwenden, um Portfolio Performance einfach zu installieren:

* **Brew:** Öffnen Sie Terminal und führen Sie den Befehl aus:
    ```bash
    brew install --cask portfolioperformance
    ```
* **MacPorts:** Öffnen Sie Terminal und führen Sie den Befehl aus:
    ```bash
    sudo port install portfolio-performance
    ```
    Möglicherweise werden Sie nach Ihrem Administratorpasswort gefragt.

Diese Paketmanager übernehmen den Download und die Installation von Portfolio Performance sowie aller notwendigen Abhängigkeiten.

# Linux

Die empfohlene Methode zur Installation von Portfolio Performance unter Linux ist über Flatpak von [Flathub](https://flathub.org/apps/info.portfolio_performance.PortfolioPerformance).

**Installation via Flatpak (Empfohlen):**

1.  Stellen Sie sicher, dass Flatpak auf Ihrem Linux-System installiert ist. Wenn nicht, finden Sie Installationsanweisungen für Ihre Distribution auf der [Flatpak-Website](https://flatpak.org/setup/).
2.  Öffnen Sie ein Terminal und führen Sie den folgenden Befehl aus, um Portfolio Performance von Flathub zu installieren:
    ```bash
    flatpak install flathub info.portfolio_performance.PortfolioPerformance
    ```
    Folgen Sie den Anweisungen, um die Installation abzuschließen.

**Manuelle Installation:**

1.  Portfolio Performance benötigt (Stand März 2024) Java 21. Überprüfen Sie, ob es bereits auf Ihrem System installiert ist. Für Debian-basierte Systeme wie Ubuntu können Sie es mit folgendem Befehl installieren:
    ```bash
    sudo apt update
    sudo apt install openjdk-21-jre
    ```
    Verwenden Sie für andere Distributionen den entsprechenden Paketmanager (z. B. `yum` für Fedora/CentOS, `pacman` für Arch Linux).
2.  Gehen Sie zur [Portfolio Performance Download-Seite](https://www.portfolio-performance.info) und laden Sie das GZIP-Archiv für Ihre Systemarchitektur herunter (entweder `x86_64` für 64-Bit oder `aarch64` für ARM64).
3.  Entpacken Sie das heruntergeladene GZIP-Archiv an einem geeigneten Speicherort, z. B. `/opt/portfolio-performance`. Sie können dies über das Terminal tun:
    ```bash
    sudo tar -xzf PortfolioPerformance-*.tar.gz -C /opt/
    ```
    (Ersetzen Sie `PortfolioPerformance-*.tar.gz` durch den tatsächlichen Dateinamen).
4.  Um Portfolio Performance auszuführen, navigieren Sie im Terminal zum entpackten Verzeichnis und führen Sie die Hauptanwendungsdatei aus (normalerweise ein Shell-Skript namens `PortfolioPerformance` oder ähnlich). Möglicherweise möchten Sie eine Desktop-Verknüpfung für einen einfacheren Zugriff erstellen.

# GitHub

Die Installationsdateien für Portfolio Performance sind auch im [GitHub-Repository des Autors](https://github.com/portfolio-performance/portfolio/releases) verfügbar. Dies kann nützlich sein, wenn Sie eine bestimmte ältere Version der Anwendung herunterladen müssen. Klicken Sie einfach auf die gewünschte Versionsnummer auf der linken Seite, um zu den Download-Links zu gelangen.

Wenn Sie daran interessiert sind, zur Entwicklung von Portfolio Performance beizutragen, finden Sie Anweisungen zum Bearbeiten und Kompilieren des Quellcodes in den [Contributing rules](https://github.com/portfolio-performance/portfolio/blob/master/CONTRIBUTING.md#project-setup).

# Workspace Verzeichnis

Das *Workspace*-Verzeichnis speichert temporäre Informationen wie die aktuelle Fenstergröße, die zuletzt geöffneten Dateien und Verzeichnisse und andere Laufzeitinformationen.

Das Workspace-Verzeichnis liegt:

* unter macOS: **~/Library/Application Support/name.abuchen.portfolio.product/workspace**
* unter Windows: **%LOCALAPPDATA%\PortfolioPerformance\workspace** wobei `%LOCALAPPDATA%` üblicherweise nach **C:\Users\\{Benutzername}\AppData\Local** zeigt
* unter Linux: **~/.PortfolioPerformance/workspace**

!!! note "macOS"
    Das "Library"-Verzeichnis ist ein verstecktes Verzeichnis. Am einfachsten ist es im Finder über das Menü *Gehe zu* -> *Gehe zum Ordner...* den Ordner `~/Library/` (ohne Anführungszeichen) zu öffnen.

!!! note "Windows"
    Das "LOCALAPPDATA"-Verzeichnis ist ein verstecktes Verzeichnis. Am einfachsten ist es, die Tastenkombination \[Windows] + \[R] zu drücken und im "Ausführen"-Fenster `%localappdata%` (ohne Anführungszeichen) einzugeben.