---
title: Menu
description: Overview and explanation of the Portfolio Performance menu structure, including File, View, Transaction, Online, and Help menus.
changes:
    - date: 2025-05-18
      author: Nirus2000
      description:
        - Adding YAML Source
        - Update Help menu
---

Figure: Menu {class="pp-figure"}

![](./images/menu-system.svg)

```
File
├── New
│   ├── File
│   ├── Security
│   ├── Cryptocurrency
│   ├── Exchange Rate
│   ├── Consumer Price Index
│   ├── Taxonomy
│   └── Watchlist
├── Open... Ctrl+O
├── Open Recent
│   ├── ...
│   ├── Clear List
├── Save Ctrl+S
├── Save as... Ctrl+S
│   ├── Password protected (AES-256)
│   ├── Binary
│   ├── XML
├── Save All
├── Currency >
│   ├── EUR (Euro)
│   ├── USD (United States dollar)
│   ├── A - D >
│   │   ├── AED (United Arab Emirates dirham)
│   │   ├── ...
│   │   ├── DZD (Algerian dinar)
│   └── E - I >
│   ├── ...
├── Tools
│   ├── Sanity Check...
│   ├── Fix: Restore ...
├── Import
│   ├── PDF Bank Documents
│   ├── CSV files (comma-separated values)
│   ├── Templates >
│   │   ├── comdirect Musterdepot
│   │   ├── ...
│   │   ├── custom templates
│   ├── XML Documents (experimental)
│   ├── Interactive Brokers: Activity Flex Query
│   └── Debug: Create text from PDF...
├── Export
│   ├── CSV files (comma-separated values) .. Ctrl+Shift+S
│   ├── Portfolio Performance XML
├── Close File
└── Quit Ctrl+Q
```

```
View
├── Options
│   ├── Always start with 'All transactions' in this part
│   ├── Always start with last view
│   ├── Hide sidebar ... Ctrl+K
│   ├── Hide information pane ... Ctrl+L
│   ├── Discreet Mode
├── Securities
├── ├── All Securities
├── Accounts
├── ├── Deposit Accounts
├── ├── Securities Accounts
├── ├── Investment Plans
├── ├──All transactions
├── Reports
│   ├── Statement of Assets
|   |   |── Chart
|   |   ├── Holdings
│   ├── Performance
│       ├── Calculation
│       ├── Chart
│       ├── Return / Volatility
│       ├── Securities
│       ├── Payments
│       └── Trades
├── Taxonomies
├── General Data
├── ├── Currencies
└── ├──Settings
```

```
Transaction
├── Buy ...
├── Sell ...
├── Delivery (Inbound) ...
├── Delivery (Outbound) ...
├── Security  transfer ...
├── Dividend ...
├── Deposit ...
├── Removal ...
├── Interest ...
├── Interest Charge ...
├── Fees ...
├── Fees Refund ...
├── Taxes ...
├── Taxes Refund ...
└── Transfer between accounts ...
```

```
Online
├── Update Quotes ... Ctrl+U, K
├── Update Quotes (only active securities) ... Ctrl+U, A
└── Update Quotes (selected security) ... Ctrl+U, T
```

```
Help
├── Welcome
├── About Portfolio Performance
├── Preferences ...
├── Check for Updates ...
├── New & Noteworthy
├── Changelog
├── Manual
├── Forum
├── How-To's
├── Report an issue...
├── Join translation teams
├── Source Code on Github
├── Show Error Log
├── Save Error Log ...
└── Debug: Reset GUI ...
```
