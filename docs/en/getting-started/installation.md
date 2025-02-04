---
title: Installation
lastUpdate: 2023-09-11
TODO: difference between windows installer & zip + adding how to install on macOS
TODO: explain third box in figure 3, the meaning of asc extension, and question windows 32 bits or 64 bits
---

PP is available for MacOS, Windows and Linux. You need to download it and do some installation steps. The easiest way to download and install the latest version of PP is by using one of the installer files at the [homepage](https://www.portfolio-performance.info/) (see fig 1). A link to the release notes of this latest version is also provided. 

![Homepage with download links for various packages (2023-09-03)](images/installation-download.png){.pp-figure}

# Windows
You can download the compressed *Zip-file* and extract it in a directory at your choice. Even a portable USB-stick (about 250 MB free space) is fine (run from stick).

You can also download the Windows - Installer (setup.exe). On Windows 11, you get a security warning about the dangers of running an exe-file. After that, double clicking on this file, will start the installation. You can change the destination folder. By default, the c:\user directory is taken. You need about 200 MB of free space (see figure 2).

![Windows Installer dialog box.](images/installation-win-installer-path.png){.pp-figure}

   + Windows: you can download the compressed Zip-file and extract it in a directory at your choice. Even an USB-stick (about 250 MB free space) is fine (run from stick). You can also download the installer file (setup.exe). On Windows 11, you get a security warning about the dangers to run a exe-file. Double clicking on this file, will start the installation. You need about 200 MB of free space.

# MacOS

- You can install the application manually by downloading the MacOS - Intel or MacOS - Silicon package, depending on your mac computer type.
   1. The following file appears in your downloads folder: PortfolioPerformance-0.72.2-aarch64.dmg (MacOs - Silicon). A DMG (Disk Image) file is a specialized file format developed by Apple for distributing software and storing data on macOS.
   2. Double-click the DMG file to mount it. A virtual disk will appear in Finder (see Figure 3).
   3. Drag and drop the icon PortfolioPerformance on the Application icon.
   4. After installation, you can delete the DMG file.

Figure: MacOS installation window. {class=pp-figure}

![](images/installation-macos-dmg.png)

- The easiest way to install Portfolio Performance is with a package installer such as Brew or MacPorts:
   - Brew: `brew install --cask portfolioperformance`
   - MacPorts: `sudo port install portfolio-performance`

# Linux

The preferred option is to install Portfolio Performance on Linux is using from [Flathub](https://flathub.org/apps/info.portfolio_performance.PortfolioPerformance).

Alternatively, you can install PP manually:

* Portfolio Performance currently (March 2023) requires Java 17. If not already available (example for Debian-related systems, such as Ubuntu):
```
sudo apt install openjdk-17-jre
```
* [Download](https://www.portfolio-performance.info) and unpack the GZIP archive (either for x86_64 or aarch64) to a suitable location, e.g. /opt

# Github   
The installer files are in fact stored in the [author's github repository](https://github.com/portfolio-performance/portfolio/releases). So, you can also download the program from this repository. If you ever should need a previous version, this is also the place to be (click on the version number at the left side).

![Github repository for downloading (previous) releases](images/installation-download-github.svg){.pp-figure}

You can edit and compile the source code; see [Contributing to Portfolio Performance](https://github.com/portfolio-performance/portfolio/blob/master/CONTRIBUTING.md#project-setup).