---
title: Installation
description: Guide to installing Portfolio Performance on Windows, macOS, and Linux – including installation files, package managers, and Flatpak.
changes:
  - date: 2025-05-03
    author: Nirus2000
    description: Updated from Java 17 to Java 21, removed images as they are too complex to maintain and add no value, synchronized the installation process between German and English
---

Portfolio Performance is available for macOS, Windows, and Linux. You can download the application in various ways as described below. The easiest way to get the latest version is usually via the installation files linked on the [homepage](https://www.portfolio-performance.info/). There you will also find a link to the release notes.

# Version Number in File Names

In the file names of the installers and ZIP files, you will typically find a version number in the format `X.X.X`. The first number (`X`) represents the major version; larger changes or new core features may lead to an increase here. The second number (`XX`) denotes a minor version, which usually includes new features or improvements. The third number (`X`) indicates a patch version, which mostly contains bug fixes and minor improvements.

# Windows

There are two main ways to install Portfolio Performance on Windows: via the installer or a ZIP file.

**Windows Installer (setup.exe):**

1.  Download the Windows Installer (e.g., `PortfolioPerformance-X.X.X-setup.exe`) from the [homepage](https://www.portfolio-performance.info/).
2.  On Windows 11, you may see a security warning about running an executable file. Click "More info" and then "Run anyway" to proceed.
3.  Double-click the downloaded `.exe` file to start the installation process.
4.  You can change the destination folder during installation. By default, it installs in the user directory (e.g., `C:\Users\<YourUsername>\Portfolio Performance`).
5.  The installation requires approximately 200 MB of free disk space.

**ZIP File:**

1.  Download the compressed ZIP file from the [homepage](https://www.portfolio-performance.info/).
2.  Choose a directory on your computer or even a portable USB drive (with at least 250 MB of free space) to extract the contents of the ZIP file.
3.  After extraction, you can run Portfolio Performance by double-clicking the executable file in the extracted folder. This method allows you to run Portfolio Performance without a traditional installation, making it portable.

**Regarding 32-bit vs. 64-bit Windows:** The Portfolio Performance installers and ZIP files available on the homepage are generally designed to work on both 64-bit versions of Windows. **Please note that support and maintenance for 32-bit versions of Windows has been discontinued.** The application itself is based on Java, which handles the underlying system architecture. If you encounter any issues, ensure that you have a compatible Java version installed (usually the latest recommended version).

# macOS

You can install Portfolio Performance on macOS either manually via a DMG file or using package managers like Brew or MacPorts.

**Manual Installation (DMG File):**

1.  Visit the [homepage](https://www.portfolio-performance.info/) and download the appropriate macOS package for your Mac:
    * **macOS - Intel:** For Macs with Intel processors.
    * **macOS - Silicon (aarch64):** For Macs with Apple Silicon processors (M1, M2, etc.).
2.  The downloaded file is a DMG (Disk Image) file, typically named like `PortfolioPerformance-0.XX.X-aarch64.dmg` (for Apple Silicon) or `PortfolioPerformance-0.XX.X-x86_64.dmg` (for Intel). A DMG file is a standard macOS format for distributing software.
3.  Double-click the DMG file to mount it. A virtual drive containing the Portfolio Performance application will appear in Finder.
4.  Drag the **PortfolioPerformance** icon from the mounted drive to the **Applications** folder. This will copy the application to your system.
5.  After copying, you can eject the virtual drive by clicking the eject icon in the Finder sidebar or by right-clicking on it and selecting "Eject". You can also delete the downloaded DMG file to save disk space.

**Installation with Package Managers:**

If you have a package manager like Brew or MacPorts installed on your Mac, you can use it to easily install Portfolio Performance:

* **Brew:** Open Terminal and run the command:
    ```bash
    brew install --cask portfolioperformance
    ```
* **MacPorts:** Open Terminal and run the command:
    ```bash
    sudo port install portfolio-performance
    ```
    You may be asked for your administrator password.

These package managers handle the download and installation of Portfolio Performance, as well as any necessary dependencies.

# Linux

The recommended method for installing Portfolio Performance on Linux is via Flatpak from [Flathub](https://flathub.org/apps/info.portfolio_performance.PortfolioPerformance).

**Installation via Flatpak (Recommended):**

1.  Ensure that Flatpak is installed on your Linux system. If not, you can find installation instructions for your distribution on the [Flatpak website](https://flatpak.org/setup/).
2.  Open a terminal and run the following command to install Portfolio Performance from Flathub:
    ```bash
    flatpak install flathub info.portfolio_performance.PortfolioPerformance
    ```
    Follow the prompts to complete the installation.

**Manual Installation:**

1.  Portfolio Performance requires (as of March 2024) Java 21. Check if it is already installed on your system. For Debian-based systems like Ubuntu, you can install it with the following command:
    ```bash
    sudo apt update
    sudo apt install openjdk-21-jre
    ```
    For other distributions, use the appropriate package manager (e.g., `yum` for Fedora/CentOS, `pacman` for Arch Linux).
2.  Go to the [Portfolio Performance Download page](https://www.portfolio-performance.info) and download the GZIP archive for your system architecture (either `x86_64` for 64-bit or `aarch64` for ARM64).
3.  Extract the downloaded GZIP archive to a suitable location, e.g., `/opt/portfolio-performance`. You can do this via the terminal:
    ```bash
    sudo tar -xzf PortfolioPerformance-*.tar.gz -C /opt/
    ```
    (Replace `PortfolioPerformance-*.tar.gz` with the actual file name).
4.  To run Portfolio Performance, navigate to the extracted directory in the terminal and execute the main application file (usually a shell script named `PortfolioPerformance` or similar). You might want to create a desktop shortcut for easier access.

# GitHub

The installation files for Portfolio Performance are also available in the author's [GitHub repository](https://github.com/portfolio-performance/portfolio/releases). This can be useful if you need to download a specific older version of the application. Simply click on the desired version number on the left side to access the download links.

If you are interested in contributing to the development of Portfolio Performance, you can find instructions on how to edit and compile the source code in the [Contributing rules](https://github.com/portfolio-performance/portfolio/blob/master/CONTRIBUTING.md#project-setup).

# Workspace Directory

The *Workspace* directory stores temporary information such as the current window size, the last opened files and directories, and other runtime information.

The Workspace directory is located:

* on macOS: **~/Library/Application Support/name.abuchen.portfolio.product/workspace**
* on Windows: **%LOCALAPPDATA%\PortfolioPerformance\workspace** where `%LOCALAPPDATA%` usually points to **C:\Users\\{Username}\AppData\Local**
* on Linux: **~/.PortfolioPerformance/workspace**

!!! note "macOS"
    The "Library" directory is a hidden directory. The easiest way to open it in Finder is via the menu *Go* -> *Go to Folder...* and enter `~/Library/` (without quotes).

!!! note "Windows"
    The "LOCALAPPDATA" directory is a hidden directory. The easiest way to open it is to press the \[Windows] + \[R] keys and enter `%localappdata%` (without quotes) in the "Run" window.
