---
title: Deposit accounts
---

A deposit account serves as a central hub for managing cash flow within the portfolio, allowing users to allocate funds for investment activities and track incoming and outgoing cash transactions. One can visualize it as a list, akin to a shopping list, where transactions such as withdrawals and deposits of digital money are recorded. There can be many deposit accounts within one portfolio, for example, for different currencies that are traded. As part of the installation process, at least one security account and one deposit account have already been created.

Figure: Example of Deposit Accounts. {class="pp-figure"}

![](images/sb-accounts-deposit-accounts.png)


## Main pane

In Figure 1 (main pane), there are four deposit accounts. It may seem unnecessary to include the currency in the name of an account, as the currency is already specified for each deposit account in the third column of Figure 1. However, including the currency in the name of the deposit account can be helpful in situations where you need to select a deposit account from a list, such as when buying a security. In these cases, having the currency clearly displayed in the name of the account can help you quickly and accurately choose the correct one.

You can use different names for accounts depending on your preferences and needs. For example, if you wish to keep your dividends and taxes separate, you could create two accounts named `Dividends`" and `Taxes`.

Figure: Add account. {class=align-right style="width:20%"}

![](images/create-new-account.png)

To create a new deposit account, click on the green + icon located at the top right (refer to Figure 2). Then, select the option `Add account`. Since you're in the Deposit Account view, a new deposit account named `No Name` will be created with the default currency of the portfolio. To rename the account, simply double-click on the Name field and enter the desired name. Remember also to change the currency if needed by double-clicking on the currency field (e.g., EUR) and selecting another currency from the dropdown menu. While navigating the currency list, you can use the first letter of the desired currency for faster navigation. Initially, the balance of the newly created deposit account will be zero.

A deposit account can be negative. However, good practice requires that you first add a deposit of a large enough sum to cover the subsequent buy transactions, just as you would do with a real broker.

To deactivate an account, right-click on the account and choose `Deactivate account` from the context menu. The account name will appear greyed out and will no longer be visible in the list of deposit accounts when making a deposit transaction. With the Filter icon (top right), you can hide inactive accounts.

You can delete a deposit account using the context menu. However, it is important to note that you can only delete an account if there are no transactions associated with it.

If you want to delete an account that has transactions, you will need to first delete the transactions that are linked to that account. Once all transactions have been removed, you can then delete the account itself.

Using the Show or Hide columns option (accessible via the :gear: gear icon at the top right), you can customize the view by hiding or adding columns. The available columns for display include: `Cash account`, `Balance`, `Currency`, `Note`, and `Attributes`. See also [How-to > User Interface](../../../how-to/user-interface.md) for more detailed information about handling the table.

## Information pane

The information pane at the bottom displays the transactions of the selected deposit account in the main pane. It consists of two tabs: Transactions and Account balance chart. The Transactions tab displays fields such as date, type, amount, and balance of each transaction. The Account Balance chart provides a graphical representation of the account balance. Due to fewer data points compared to a historical prices graph, the chart may appear more blocked. Figure 3 illustrates the balance of the `Broker-1 (EUR)` account, where the early spikes are the result from deposits followed by purchases on the next day.

Figure: Example of the Account Balance Chart. {class=pp-figure}

![](images/sb-accounts-deposit-accounts-balance-chart.png)

The context menu, accessed by right-clicking on the chart, offers the same options as many other charts; for example, you can refer to the [chart menu of the `All Securities` info pane](../../view/securities/all-securities.md#chart-menu) for more information. There are no other configuration settings.

## Troubleshoot Balance Discrepancy

If you notice any discrepancies in a deposit account between the calculated balance of PP and the actual balance of the bank/broker, you can use the context menu to troubleshoot the issue. To do so, right-click on the account in the main pane and select "Troubleshoot Balance Discrepancy" from the menu.

This will open a dialog box displaying the calculated monthly balances for the selected deposit account. In the "Expected balance" column, you can enter the balance that you expect according to your bank account statement. Portfolio Performance (PP) will then use the calculated difference to try to identify any transactions that may be causing the discrepancy. For example, PP may find transactions that were made to a different account or are dated in the future.

<video width="100%"  controls>
  <source src="../images/troubleshoot-balance-discrepancy.mp4" type="video/mp4">
</video>

