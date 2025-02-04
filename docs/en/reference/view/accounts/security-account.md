---
title: Security Accounts
---
The `Securities Accounts` view provides a [dual-pane view](../../../how-to/user-interface.md) of all security accounts within the portfolio. The main pane features a list of all securities accounts, while the information pane presents details about the selected account in the upper panel.

Figure: Example of Securities Accounts. {class=pp-figure}

![](images/sb-accounts-securities-accounts.png)

## Main pane

A security account will hold your securities and will be used for trading. Use the data tools icon  :octicons-feed-plus-16: to add a new account. For each account, the total market value of its assets is displayed as Volume of security deposits. A securities account is most often named after the broker or bank that you use for buying or selling. But other variants are possible. For example, you could collect all your bitcoin investments into a separate account `crypto` or you can differentiate between your account and that of your partner. 

It is worth noting that, although the portfolio has four deposit accounts (see [figure 1](images/sb-accounts-deposit-accounts.png) in the Deposit Accounts section), only one of them, named `Deposit Account`, is set as the reference account. This reference account is used for handling trades when no other account is explicitly assigned. The information pane (bottom panel) shows the `Statement of Assets` view for the selected security account.

## Information pane

The information pane features four tabs: `Statement of Assets`, `Transactions`, `Chart`, and `Holdings`.

### Statement of Assets
The `Statement of Assets` tab, depicted in Figure 1, is selected by default. It includes details such as the number of shares, the name and ISIN of the asset, the latest price or Quote, the purchase value, the total market value (computed as shares multiplied by Quote), and the percentage of the asset in the total portfolio. It is the same table as in the menu [View > Reports > Statement of Assets](../../view/reports/statement/index.md) but limited to the selected security account.

With the `Show or hide columns` :gear: icon, you can add numerous other fields such as purchase price, dividends, and many more. These fields are described in full detail in [View > Reports > Statement of Assets](../reports/statement/index.md#available-columns). The Export Data as CSV icon :material-upload: allows you to save the displayed table as a CSV-file.

### Transactions
This section presents a table that lists all transactions related to the chosen Securities Account. The table offers in-depth information about each transaction, such as the date, transaction type, security involved, quantity, price, fees, and other pertinent data. See [View > Accounts > All Transactions](all-transactions.md) for more information on the available fields and how to customize the table with the data tools.

### Chart

The `Chart` tab presents a specific line graph, displaying the market value over time of the selected account (e.g. Brokerage Account in Figure 2), the invested capital since the first transaction in this securities account, and the delta (difference) between those two.

Figure: Chart from Securities Account (information pane). {class=pp-figure}

![](images/sb-accounts-securities-accounts-chart.png)


Clicking on any point in the chart will reveal the actual data of all three time series. With the :gear: data tool, you can also add the `Taxes (Accumulated)` and `Fees (Accumulated)` time series to the chart. Please refer to the section on the [User Interface](../../../how-to/user-interface.md#) for more guidance on customizing the chart.

### Holdings

The Holdings chart from the Securities Account doesn't have any data tools. It's very similar to the portfolio holding chart; see [View > Reports > Statement of Assets > Holdings](../../view/reports/statement/holdings.md). Clicking any part of the chart will reveal some additional information.

Figure: Holdings Chart from Securities Account (information pane). {class=pp-figure}c

![](images/sb-accounts-securities-accounts-holdings.png)


## One or more security accounts?

Should you create only one security account to hold all your transactions?

- Each security account is associated with a corresponding deposit account, established at the time of creation. When selecting a security account for a buy or sell transaction, the reference deposit account is automatically chosen. Manual selection is unnecessary in this case. However, opting for a different deposit account for the transaction necessitates manual selection, involving an additional click.
- In the portfolio view, you see the combined data from all sub-accounts. This means you get a single, unified overview of your investments without having to check each account separately.
- On the other hand, the Reports > Statement of Assets > Holdings pie chart can become quite crowded for the entire portfolio. Splitting it up into separate accounts is an easy way to make it more manageable. With the filter, you can create any combination of security and deposit accounts to view. This filter can also be used in other views.
- If you hold the same securities in one account, it’s recommended to set up separate accounts. This is because PP uses the First-In-First-Out (FIFO) method, where the oldest pieces are always sold first. For instance, if both you and your partner have purchased the same security at different times, merging them into a single security account will always prioritize selling the oldest shares when executing sell orders.




