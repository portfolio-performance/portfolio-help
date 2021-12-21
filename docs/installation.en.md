---
title: Installation
---

# Installation

Download the compressed file, unpack it, and start it with a double click.

The XML/Portfolio file with your own data (securities, accounts, portfolios) is best saved somewhere under *My Documents*.

## macOS

Portfolio Performance is not signed with an Apple certificate. For this reason, [macOS Gatekeeper](https://en.wikipedia.org/wiki/Gatekeeper_(macOS)) treats this application in a special way when started for the first time. PP can be started with the following steps:


* Load and unpack PP (for example in the "Downloads" directory)
* Move PP to "Applications"
* Start PP by right-clicking and selecting "Open" in the context menu and select "Open" in the subsequent dialog messages.

## Linux

Portfolio Performance uses [Eclipse SWT](https://www.eclipse.org/swt/), and thus native libraries in Linux. GTK3 is used by default, but sometimes there are issues with certain themes. For example, one user reported an issue related to the ["oxygen-gtk" theme](https://github.com/buchen/portfolio/issues/1089#issuecomment-459698493).

You may install the dependencies in Ubuntu 18.04 by running the following command: `sudo apt install libwebkitgtk-3.0-0 default-jre`

If there are issues, you may try the following workarounds:

* Try a different GTK3 theme
* Force PP to use GTK2: ```env SWT_GTK3=0 PortfolioPerformance```
* Use an alternative input method: ```env GTK_IM_MODULE=ibus PortfolioPerformance```

## Workspace directory

In the *Workspace* directory, PP stores temporary data such as the current window size, recently opened files and directories, and other runtime information.

The workspace directory is located at:

* macOS: **~/Library/Application Support/name.abuchen.portfolio.product/workspace**
* Windows: **%LOCALAPPDATA%\PortfolioPerformance\workspace** where %LOCALAPPDATA% is usually located at **C:\Users\\{username}\AppData\Local**
* Linux: **~/.PortfolioPerformance/workspace**

!!! note "macOS"
    The "Library" directory is a hidden directory. The easiest way to access it is to enter "~/Library/" (without quotation marks) in Finder via the menu *Go* -> *Go to Folder...*

!!! note "Windows"
    The "LOCALAPPDATA" directory is a hidden directory. The easiest way to access it is to enter the key combination [Windows] + [R] and enter "%localappdata%" (without quotation marks) in the "Run" window.
