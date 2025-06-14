---
title: Help > Trouble shooting
description: Troubleshooting guide for Portfolio Performance – viewing logs, resetting the UI, handling update errors, and key file locations for different operating systems.
changes:
  - date: 2025-06-14
    author: Nirus2000
    description:
      - Updated images
      - Add OS informations
---

On rare occasions, the Portfolio Performance app may malfunction or crash. Under the **Help** menu, three key options can assist in such cases.

## Show Error Log

Each time the app starts, it generates a log file. You can view this log from within the application via `Help > Show Error Log`. Double-clicking a message displays the full entry. If no error occurred, the log will be minimal:

Figure: Log after successful start-up {class="pp-figure"}  
![](./images/show-error-log-minimal.png)

When errors occur, they are listed sequentially:

Figure: Log after unsuccessful operation {class="pp-figure"}  
![](./images/show-error-log-multiple-errors.png)

Double-clicking an error entry opens more detailed information:

Figure: Detailed error view {class="pp-figure"}  
![](./images/show-error-log-multiple-errors-dbl-click.png)

If the portfolio can still be opened, you should correct the historical price source for the affected security. If not, open the XML file in a text editor and manually remove the faulty data source.

You can copy the log text to the clipboard, for example when asking for help in the [forum](https://forum.portfolio-performance.info/), or save it to a file.

## Save Error Log

The log file is automatically saved in your user directory. Its default location depends on your operating system:

- **Windows**:  
  `C:\Users\Your-name\AppData\Local\PortfolioPerformance\workspace\.metadata\`

- **macOS**:  
  `/Users/Your-name/Library/Application Support/name.abuchen.portfolio.ui/workspace/.metadata/`

- **Linux**:  
  `/home/Your-name/.portfolio-performance/workspace/.metadata/`

To export the current log to a `.log` file, use the command `Help > Save Error Log`.

This version contains more technical details than the in-app error window:

```
!SESSION 2025-06-07 14:12:08.240 -----------------------------------------------
eclipse.buildId=0.76.3.
java.version=21.0.5
java.vendor=Azul Systems, Inc.
BootLoader constants: OS=win32, ARCH=x86_64, WS=win32, NL=de_DE
Command-line arguments:  -os win32 -ws win32 -arch x86_64

This is a continuation of log file C:\Users\[Your-name]\AppData\Local\PortfolioPerformance\workspace\.metadata\.bak_0.log
Created Time: 2025-06-07 14:27:55.719

!ENTRY name.abuchen.portfolio.ui 4 0 2025-06-07 14:27:55.719
!MESSAGE Widget is disposed
!STACK 0
org.eclipse.swt.SWTException: Widget is disposed
	at org.eclipse.swt.SWT.error(SWT.java:4922)
	at org.eclipse.swt.SWT.error(SWT.java:4837)
...
```

When reporting issues on [GitHub](https://github.com/portfolio-performance/portfolio/issues), include this log file. Avoid uploading portfolios that contain sensitive data.

## Debug: Reset UI

The `Help > Debug: Reset UI` option opens a dialog. After confirming, restart the application:

Figure: Reset GUI dialog box {class="pp-figure"}  
![](./images/reset-UI.png)

Figure: Successful reset confirmation {class="pp-figure"}  
![](./images/reset-UI-successful.png)

Resetting the UI **does not** affect:

- Created views
- Custom reporting periods
- Recent Files list

It **does** reset:

- Window size and position
- Visibility/layout of panes
- Open files (not reopened on restart)

Use **Reset UI** as a minimal-impact first step when troubleshooting UI issues.

## Update Error

If the installation is corrupted or files are missing, automatic updates may fail. In such cases, an error message will appear:

Figure: Update error message {class="pp-figure"}  
![](./images/error-on-updating.png)

The recommended solution is to delete and reinstall the application.
