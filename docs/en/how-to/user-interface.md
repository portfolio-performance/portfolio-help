---
title: User Interface
---
Figure 1 illustrates a typical opening screen of Portfolio Performance, featuring two open portfolios: `demo-portfolio-03.xml` and the built-in `kommer` portfolio. The active portfolio is `kommer`, and its contents are currently displayed on the screen.

Figure: Typical opening screen of the Portfolio Performance program. {class=pp-figure}

![](images/components-UI.svg)

## Components

Figure 1 showcases the user interface elements present upon selecting the `All Transactions` view, which can be accessed either through the sidebar or the menu option `View > All Transactions`. In this example, the last Dividend transaction is selected, resulting in the display of a chart showing the historical quotes of `Mercedes Benz Group` in the information pane.

- **Menu bar** containing five elements: `File`, `View`, `Transaction`, `Online`, and `Help`. This top menu remains identical across all views. However, submenus can be dynamic. For instance, the `Transfer between Accounts ...` menu item is only available when there is more than one deposit account. An image of all menus and submenus expanded [[available here]](menu.md) will provide you with a comprehensive understanding of the program's functionalities.
- **Open portfolios**: you can open multiple portfolios simultaneously. The highlighted project is visible below. Projects marked with a star (*) preceding their name has been changed and should be saved before closing. It is possible to display two projects [side by side](../how-to/copy-securities.md) in the UI.
-  The **Sidebar** serves as a convenient shortcut for accessing various views within the project. All available options can also be accessed through the `View` menu. It's important to note that the list in the sidebar mirrors the options available in the `View` menu, providing a one-to-one translation of the available views. The chosen view dictates the content displayed in the adjacent top and bottom panes. Next to the options `Securities` and `Taxonomies`, a very small (green) icon will let you add new elements.

    To hide or show the sidebar, you can use the menu option `View > Options > Hide/Show Sidebar`. Alternatively, you can use the shortcut key `Ctrl+K` for a more efficient workflow. This allows you to quickly toggle the sidebar visibility as needed.

- Dual-pane views: In PP, all views consist of dual-pane layouts, featuring a main pane and an information pane. When you select an item in the main pane, more detailed information about that item will be displayed in the information pane. If you prefer a single-pane view, you can hide the information pane (as described below), creating the illusion of a single pane view as in the Settings view. 
- **Main pane**: in the example of Figure 1, the main pane contains the `All Transactions` view. This is a list of all the transactions that you have made with your portfolio, such as deposits, withdrawals, buys, and sells. The default columns, such as `date`, `type`, `security`, ..., are initially visible. However, you have the flexibility to modify them using the Settings (cog) icon located in the top-right corner. Please, note that the data tools icons in the top-right corner are specific to this view and may not necessarily appear in other views.
- The **Information pane** follows the selection of the main pane. For example, selecting `NVIDIA Corp` in the main pane of Figure 1 will display the chart of this share in the information pane. You can hide/show the information pane with the menu `View > Options > Hide/Show Information Pane`. The shortcut key is `Ctrl+L`.
- **Divider bar**: the area occupied by the top and bottom panes can be adjusted using the divider bar. The divider bar can be dragged all the way to the top or bottom, allowing you to customize the layout according to your preferences. Additionally, there is a vertical divider bar located at the right border of the sidebar.
- **Scrollbars** appear when not all text can be displayed. In Figure 1, there are two vertical scrollbars and one horizontal.

## Table handling

The main pane in Figure 1 consists of a table. The first icon in the data tools lets you filter the rows in the tables, for example displaying only buy transactions. The second icon will let you export the table as displayed as a CSV-file. With the third icon (gear), you can show or hide columns in the table. 

Click the column heading to sort the table in ascending (&and;) or descending (&or;) order based on that column. You can rearrange any column by dragging its header. Drag the divider line between two columns to adjust the with of the left column or double click to best fit. You can rename or hide a column with the context menu (right-click on the column header). Adding, removing or resetting the columns to their original layout is done with the Show or hide columns icon (gear symbol top right). Clicking the Gear icon will show you all available columns.

## Shortcuts

- View
    - Show/hide sidebar: Ctrl+K (Windows)/ Cmd+K (Mac)
    - Show/hide information pane: Ctrl+L
- File
    - Save: Ctrl+S (Windows)/ Cmd+S (Mac)
    - Quit: Ctrl+Q (Windows)/ Cmd+Q (Mac)
