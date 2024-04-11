---
title: Deposit - Removal (withdrawal)
---

A deposit is the process of adding funds to a deposit account, while a removal (withdrawal) is the process of removing funds from an account. A deposit account is sometimes also called a `cash account`. 

Figure: Example of a deposit (in EUR) and removal (withdrawal) in USD. {class=pp-figure}

![](images/deposit-removal.svg)

Figure 1 illustrates a deposit of 15 EUR and a withdrawal of 14 USD. Although the deposit increases (debits) *your* account balance, it is termed a `Credit note` because the funds originate from a third party, whose account will be reduced (credited). This resembles a scenario such as returning goods, where you receive a credit note from the company.

The currency of the transaction is determined by the associated cash account. While adding the currency to the names of the deposit accounts may seem redundant, it can be helpful for quick identification when selecting an account from a drop-down menu. Naming them `deposit-account-1`, `deposit-account-2` will force you to remember that account-1 is for EUR and account-2 is for USD.

Implicit deposits or withdrawals can also occur through other transactions, such as a stock purchase, which automatically triggers a withdrawal of the equivalent value from a cash account.

A common mistake for beginners is to record a buy transaction without first ensuring that the necessary deposits are made. This can lead to a negative balance in the deposit account, which affects the market value of the portfolio at the end of the reporting period and consequently impacts the portfolio's performance. This effect is of course not visible in the performance of an individual security or trade.

It is not possible to attach an interest rate to a deposit account as is typically done with banks. As a result, funds placed into a deposit account maintain their exact value until the end of the reporting period (MVE). As a result, deposits and withdrawals on their own have no effect on the portfolio's performance. Assume a portfolio Market Value (MVB) of 100 EUR at the beginning of the reporting period and only one deposit of 50 EUR at the exact mid of the 1 year period (see [Concepts > Performance](../../concepts/performance/index.md) for more info about the calculation).

- TTWOR: `r = [150/(100 + 50)] - 1 = 0%`. 
- IRR: `150 = 100 x (1 + IRR)^1 + 50 x (1 + IRR)^1/2 = 0%`.

To assign an interest to a deposit account, you can use the menu `Transaction > Interest`.
