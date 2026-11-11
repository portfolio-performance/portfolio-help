---
title: 安装
description: 在 Windows、macOS 与 Linux 上安装 Portfolio Performance 的指南——包括安装文件、包管理器与 Flatpak。
changes:
  - date: 2025-05-03
    author: Nirus2000
    description: 从 Java 17 更新为 Java 21；删除图片（维护成本过高且无实际价值）；同步德文版与英文版的安装流程
---

Portfolio Performance 提供 macOS、Windows 与 Linux 版本。你可以按下述方式下载该应用程序。获取最新版本最简便的办法，通常是通过[主页](https://www.portfolio-performance.info/)上提供的安装文件。主页上也有发布说明的链接。

# 文件名中的版本号

在安装程序与 ZIP 文件的文件名中，通常会看到形如 `X.X.X` 的版本号。第一个数字（`X`）代表主版本号；较大的变更或新的核心功能会使其递增。第二个数字（`XX`）表示次版本号，通常包含新功能或改进。第三个数字（`X`）表示修订版本号，多半包含缺陷修复与小幅改进。

# Windows

在 Windows 上安装 Portfolio Performance 主要有两种方式：使用安装程序，或使用 ZIP 文件。

**Windows 安装程序（setup.exe）：**

1.  从[主页](https://www.portfolio-performance.info/)下载 Windows 安装程序（例如 `PortfolioPerformance-X.X.X-setup.exe`）。
2.  在 Windows 11 上，你可能会看到有关运行可执行文件的安全警告。点击"更多信息"，再点击"仍要运行"以继续。
3.  双击下载得到的 `.exe` 文件，开始安装过程。
4.  你可以在安装过程中更改目标文件夹。默认安装在用户目录下（例如 `C:\Users\<YourUsername>\Portfolio Performance`）。
5.  安装大约需要 200 MB 的可用磁盘空间。

**ZIP 文件：**

1.  从[主页](https://www.portfolio-performance.info/)下载压缩的 ZIP 文件。
2.  在你的电脑上选择一个目录，甚至可以选择便携式 U 盘（至少有 250 MB 可用空间），把 ZIP 文件的内容解压到其中。
3.  解压完成后，你只需双击解压目录中的可执行文件即可运行 Portfolio Performance。这种方式无需传统安装过程即可运行，因而具有便携性。

**关于 32 位与 64 位 Windows：** 主页上提供的 Portfolio Performance 安装程序与 ZIP 文件通常都可在 64 位 Windows 上运行。**请注意，对 32 位 Windows 的支持与维护已经终止。** 应用程序本身基于 Java，由 Java 处理底层系统架构。如果遇到任何问题，请确认已安装兼容的 Java 版本（通常是最新推荐版本）。

# macOS

在 macOS 上，你既可以通过 DMG 文件手动安装 Portfolio Performance，也可以使用 Brew 或 MacPorts 等包管理器安装。

**手动安装（DMG 文件）：**

1.  访问[主页](https://www.portfolio-performance.info/)，下载适合你的 Mac 的 macOS 安装包：
    * **macOS - Intel：** 适用于搭载 Intel 处理器的 Mac。
    * **macOS - Silicon (aarch64)：** 适用于搭载 Apple Silicon 处理器（M1、M2 等）的 Mac。
2.  下载得到的文件是 DMG（磁盘映像）文件，名称通常形如 `PortfolioPerformance-0.XX.X-aarch64.dmg`（Apple Silicon）或 `PortfolioPerformance-0.XX.X-x86_64.dmg`（Intel）。DMG 是 macOS 分发软件的标准格式。
3.  双击 DMG 文件进行挂载。Finder 中会出现一个包含 Portfolio Performance 应用程序的虚拟磁盘。
4.  把挂载磁盘中的 **PortfolioPerformance** 图标拖到 **应用程序** 文件夹。这会把应用程序复制到你的系统中。
5.  复制完成后，你可以点击 Finder 边栏中的推出图标将其推出，也可以在该虚拟磁盘上右键点击并选择"推出"。你也可以删除下载得到的 DMG 文件以节省磁盘空间。

**使用包管理器安装：**

如果你的 Mac 上已安装 Brew 或 MacPorts 之类的包管理器，可以用它轻松安装 Portfolio Performance：

* **Brew：** 打开终端，运行以下命令：
    ```bash
    brew install --cask portfolioperformance
    ```
* **MacPorts：** 打开终端，运行以下命令：
    ```bash
    sudo port install portfolio-performance
    ```
    系统可能会要求你输入管理员密码。

这些包管理器会一并处理 Portfolio Performance 的下载与安装，以及所需的全部依赖项。

# Linux

在 Linux 上安装 Portfolio Performance，推荐通过 [Flathub](https://flathub.org/apps/info.portfolio_performance.PortfolioPerformance) 使用 Flatpak。

**通过 Flatpak 安装（推荐）：**

1.  确认你的 Linux 系统已安装 Flatpak。若尚未安装，可在 [Flatpak 网站](https://flatpak.org/setup/)上找到针对你所用发行版的安装说明。
2.  打开终端，运行以下命令，从 Flathub 安装 Portfolio Performance：
    ```bash
    flatpak install flathub info.portfolio_performance.PortfolioPerformance
    ```
    按照提示完成安装。

**手动安装：**

1.  Portfolio Performance 需要 Java 21（截至 2024 年 3 月）。请检查系统中是否已安装。对于 Ubuntu 等基于 Debian 的系统，可用以下命令安装：
    ```bash
    sudo apt update
    sudo apt install openjdk-21-jre
    ```
    对于其他发行版，请使用相应的包管理器（例如 Fedora/CentOS 用 `yum`，Arch Linux 用 `pacman`）。
2.  前往 [Portfolio Performance 下载页面](https://www.portfolio-performance.info)，下载适合你系统架构的 GZIP 压缩包（64 位用 `x86_64`，ARM64 用 `aarch64`）。
3.  把下载的 GZIP 压缩包解压到合适的位置，例如 `/opt/portfolio-performance`。你可以在终端中完成：
    ```bash
    sudo tar -xzf PortfolioPerformance-*.tar.gz -C /opt/
    ```
    （将 `PortfolioPerformance-*.tar.gz` 替换为实际文件名。）
4.  要运行 Portfolio Performance，请在终端中进入解压后的目录，执行主应用程序文件（通常是一个名为 `PortfolioPerformance` 或类似名称的 shell 脚本）。你可能想创建一个桌面快捷方式以便访问。

# GitHub

Portfolio Performance 的安装文件在作者的 [GitHub 仓库](https://github.com/portfolio-performance/portfolio/releases)中也提供。如果你需要下载应用程序的某个较早版本，这会很有用。只需点击左侧的所需版本号即可访问下载链接。

如果你有意参与 Portfolio Performance 的开发，可在[贡献规则](https://github.com/portfolio-performance/portfolio/blob/master/CONTRIBUTING.md#project-setup)中找到如何编辑与编译源代码的说明。

# Workspace 目录

*Workspace* 目录存放临时信息，例如当前窗口尺寸、最近打开的文件与目录，以及其他运行时信息。

Workspace 目录的位置：

* 在 macOS 上：**~/Library/Application Support/name.abuchen.portfolio.product/workspace**
* 在 Windows 上：**%LOCALAPPDATA%\PortfolioPerformance\workspace**，其中 `%LOCALAPPDATA%` 通常指向 **C:\Users\\{Username}\AppData\Local**
* 在 Linux 上：**~/.PortfolioPerformance/workspace**

!!! note "macOS"
    "Library" 目录是隐藏目录。在 Finder 中打开它最简便的方式是使用菜单 *前往* -> *前往文件夹...*，然后输入 `~/Library/`（不含引号）。

!!! note "Windows"
    "LOCALAPPDATA" 目录是隐藏目录。打开它最简便的方式是按 \[Windows] + \[R] 键，并在"运行"窗口中输入 `%localappdata%`（不含引号）。