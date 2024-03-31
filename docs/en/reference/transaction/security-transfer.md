---
title: Security transfer
---

 As the name suggests, this transaction involves transferring a specified number of shares from one security account to another. It is only accessible in the menu when the portfolio includes more than one security account. The topic [Reference > View > Accounts > Securities Accounts](../view/accounts/security-account.md#one-or-more-security-accounts) summarizes some arguments for portfolios with only one security account or multiple accounts.

There are various scenarios where security transfers might be necessary. For instance, if you have multiple brokers each with their respective securities accounts, you might need to transfer a security between them, mirroring real-life scenarios where you move a security from one broker to another.

Another common scenario involves making provisions for the future, such as reserving some of your stocks for your children. While keeping the stocks in your portfolio, you may transfer a portion from the *parent* account to a *child* account. This segregation ensures that selling stocks from the parent account doesn't impact the performance of the child account, enabling separate performance tracking.

Figure: Security transfer dialog box.{class=pp-figure style="width:70%"}

![](images/security-transfer.png)

With three drop-down boxes, you can select the security, as well as the source and target security account. Several checks are conducted; for instance, you cannot transfer a security that is unavailable or insufficiently available in the source account. You also need to provide the date of the transfer, the number of shares and the quote price.

Although it's technically one transaction, behind the scenes, PP creates two "virtual" transactions (refer to Figure 2). The security transfer is divided into a Transfer (Outbound) of 4 shares from `security-account-1`, followed by a Transfer (Inbound) into `security-account-2`. However, both transactions are considered as a single entity. Editing one of them will trigger the Security Transfer dialog. Deleting one transaction will also remove the other.

Figure: Result of the Security Transfer transaction.{class=pp-figure}

![](images/security-transfer-result.png)

A consequence of the Security Transfer transaction is the creation of two open trades, as depicted in Figure 3. The first trade covers the remaining 6 shares in security-account-1, while the second trade comprises the four transferred shares in security-account-2. Both trades start at the date of the original security purchase; although one could argue that the second trade should start at the date of the transfer. They also share the same buying price and also here an argument could be made to use the quote price of the transfer. The date and quote price entered with the Security Transfer doesn't seem to be used at all.

Figure: Resulting trades from the Security Transfer transaction.{class=pp-figure}

![](images/security-transfer-result-trades.png)

## Setting the quote price

Why is a quote price required? What price should you enter: the purchase price, the historical price at the transfer date, zero? Why can't you *just* transfer the shares from one account to another? As mentioned in this [forum thread](https://forum.portfolio-performance.info/t/why-is-a-quote-price-needed-with-a-security-transfer-transaction/27874/3), it all has to do with performance tracking.

Considering the parent-child scenario from above, you want to transfer 4 shares of 10 available from your *parent* account to the *child* account (see figure 2). Suppose you purchased the stock at 10 EUR per share on Jan 1, 2023. The historical price at the time of transfer was 12 EUR/share, although you transferred it at 10 EUR/share (see figure 2) and today (2024-01-01) it has risen to 15 EUR per share. What is the performance of both the child and parent accounts?

Remember that for a performance calculation, you have to set a reporting period. Figure 4 displays the absolute performance and the IRR of the parent account for the reporting period 2023-01-01 until 2024-01-01.

Figure: Absolute performance and IRR of parent account (quote price transfer = 10 EUR). {class=pp-figure}

![](images/security-transfer-performance.png)

The formula for [absolute performance](../view/reports/performance/index.md#absolute-change) is: **MVE - MVB + CFout - CFin**

where MVE = Market Value at the End (of the reporting period), MVB = Market Value at the Beginning, CFout = cash flows out of the account, and CFin = cash flows into the account. The absolute performance of an account is the difference between the beginning and end value of that account, but corrected for the in- and outflows. If your account has a MVB of 100 EUR and 120 EUR at the end with no in- or outflows, then the absolute performance is 20 EUR.

Let's try to calculate the performance for the different accounts and quote prices.


**Reporting period 2023-01-01 until 2024-01-01**. Remember the reporting period spans from the end of the first day (e.g. 2023-01-01) to the end of the last day. 

1. If the quote price is set to the purchase price (10 EUR):

    * *Parent* account: `MVE (7 x 14) - MVB (10 x 10) + CFout (3 x 10) - CFin (0) = 28 EUR`.
    * *Child* account: `(3 x 14) - 0 + 0 - (3 x 10) = 12 EUR`.
  
        The market value of the security account *parent* at the end of the 2023-01-01 is 100 EUR (the shares were purchased during the day). The MVE is 98 EUR because the account contains 7 shares à 14 EUR.
        
        The MVE of the child account is 42 EUR (3 shares x 14 EUR). The MVB however is zero EUR. The child account doesn't have any shares at 2023-01-01. However, there is a CFin at 2023-03-01 of 3 x 10 EUR = 30 EUR.

        The formula for the IRR is given at [Reference > View > Reports > Performance](../view/reports/performance/index.md):

$$\mathrm{MVE = MVB \times (1 + IRR)^{\frac{RD_1}{365}} + \sum_{t=1} ^{n}CF_t \times (1+IRR)^{\frac{RD_t}{365}} \qquad \text{(Eq 3)}}$$

According to Figure 4, the IRR = 37.08% (transfer quote price = 10; reporting period 1 year).
Plugging these values in the formula give:

(7 x 14 EUR) = (10  x 10 EUR) x (1+IRR)^365/365 + (3 x 10) x (1 + IRR)^306/365

2. If the quote price is set to the historical price at the moment (12 EUR):

    * *Parent* account: `(7 x 14) - (10 x 10) + (3 x 12) - 0 = 34 EUR`.
    * *Child* account: `(3 x 14) - 0 + 0 - (3 x 12) = 6 EUR`.

3. If the quote price is set to zero; which is the same as not providing a price:

    * *Parent* account: `(7 x 14) - (10 x 10) + (3 x 0) - 0 = -2 EUR`.
    * *Child* account: `(3 x 14) - 0 + 0 - (3 x 0) = 42 EUR`.

As can be seen, the absolute performance varies a lot: from positive +28 EUR to negative -2 EUR for the parent account. The negative performance is, of course, very understandable. Transferring 3 shares out of the account for nothing, will severely impact the performance.

The performance of the portfolio should be the sum of the account performances, which in all three cases is equal to 40 EUR. The MVE of the portfolio is (7 + 3) * 14 EUR = 140 EUR. The MVB = 10 * 10 EUR = 100 EUR. The absolute performance of the portfolio is thus indeed 40 EUR.

**Reporting period 2023-09-01 until 2024-01-01**. 
Changing the reporting period has an impact on the MVB. For both the *parent* and *child* account, the MVB is influenced by the historical price at that moment times (12 EUR). For transfer quote price of 10 EUR, the absolute performance is:
- *Parent* account: `MVE (7 x 14) - MVB (7 x 12) + CFout (0) - CFin (0) = 14 EUR`.
- *Child* account: `(3 x 14) - (3 x 12) + 0 - 0 = 6 EUR`.

The security transfer was done at 2023-03-01; so no cashflows will occur after that date. The performance is determined only by MVB and MVE.

