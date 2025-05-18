---
title: System overview example
description: Overview of the Portfolio Performance system components, detailing how transactions, performance calculations, and other factors influence the portfolio’s overall performance.
changes:
    - date: 2025-05-03
      author: Nirus2000
      description:
        - Adding YAML Source
---

The name PortfolioPerformance (PP) captures its purpose very well: managing an investment portfolio from a performance perspective. This focus contrasts with many proprietary broker apps, which primarily facilitate the technical execution of orders. The following text outlines the principal components. Follow the links to obtain more information about each component.

The portfolio has one [Securities Account](../../reference/view/accounts/security-account.md) (broker-A) and two [Deposit Accounts](../../reference/view/accounts/index.md) (in EUR and USD). The balance of the deposit accounts is the end balance on March 5, 2024. Three shares with their historical prices have been added ([All Securities](../../reference/view/securities/all-securities.md)). Only share-1 and share-2 have associated transactions and thus participate in the performance calculation. The [historical prices](../../how-to/downloading-historical-prices/index.md) are part of the [master security data](../../reference/file/new.md#historical-quotes). The Exchange Rates are provided in [View > General Data > Currencies](../../reference/view/general-data/currencies.md).

Figure: Portfolio Performance components and their relationships. {class=pp-figure}

![](../images/system-overview-example.svg)

At the center of the system are the Transactions ([All Transactions](../../reference/view/accounts/all-transactions.md)). There are six transactions involved in this example.

1. On March 1, 2024, a deposit of 300 EUR was made into broker-A's (EUR) deposit account to purchase shares.
2. Later the same day, 10 shares of share-1 were bought at 15 EUR per share. After deducting 5 EUR for fees and taxes, 155 EUR was credited to the broker-A (EUR) deposit account, leaving a balance of 145 EUR.
3. On March 3, 75 EUR was converted to USD at an exchange rate of 0.9248 USD/EUR, resulting in 81.10 USD. The balance of the broker-A (EUR) account decreased to 70 EUR, while broker-A (USD) held 81.10 USD.
4. Using the USD deposit account, 5 shares of share-2 were purchased at 15 USD per share, resulting in a Net Transaction Value of 78 USD. The balance of broker-A (USD) dropped to 3.10 USD.
5. A dividend of 1.5 EUR per share was paid on March 4. After deducting 7 EUR for fees and taxes, the balance of broker-A (EUR) increased by 15 EUR to 78 EUR.
6. On March 5, 5 shares of share-1 were sold at 12 EUR per share, resulting in a Net Transaction Value of 60 EUR. After deducting 11 EUR for fees and taxes, the balance of broker-A (EUR) increased to 127 EUR.

The transaction flow in the deposit accounts is clear to follow (as outlined above). Regarding the final balance of broker-A's securities account (129.13 EUR), on March 5, the account contains 5 shares of share-1, valued at 60 EUR, and 5 shares of share-2, valued at 75 USD. As the securities account's base currency is EUR, the USD value is converted to EUR using an exchange rate of 0.9217 USD/EUR, resulting in 69.13 EUR. This brings the total to EUR 129.13, representing the final balance of the securities account.

Performance is calculated on a daily basis. To compute it, you need the market value of the asset at the beginning (MVB) and end (MVE) of the day, along with the total net amount of incoming and outgoing cash flows. With these values, one can calculate the daily performance using the equation provided in Figure 1 (see also [reference > view > reports > performance](../../reference/view/reports/performance/index.md)). These daily performances can then be used to determine the cumulative performance. Let's analyze and compare the performance of share-1, share-2, and the overall portfolio across different days.

- **March 1**
    * share-1: Since the shares are purchased during the day, the market Value at the Beginning of the day (MVB) is zero EUR. MVE is 100 EUR; 10 shares at closing price of 10 EUR per share. To buy the stock, a net cash inflow of 103 EUR is needed (to pay the principal and fees). Taxes are NOT considered. There are no cash outflows. The daily performance = [100/(0 + 103)] - 1 = -0.0291 or -2.91%.
    * share-2: Allvalues are zero; the performance is also zero (technically, it should be undefined because you are dividing by zero).
    * portfolio: The portfolio contains all securities and deposit accounts. The MVE of the portfolio is the market value of share-1 (100 EUR), plus what is left in the deposit account (195 EUR) or in total 295 EUR. The daily performance is thus [295/(0+300)] - 1 = -0.0167 or -1.67%.
- **March 2**: there are no transactions, and the historical prices are stable. The daily performance is zero, and the cumulative performance stays at the same level for all assets.
- **March 3**
    * share-1: Nothing changes for share-1.
    * share-2: The MVE of share-2 is 76 USD (5 x 15 USD/share) or 75 x 0.9248 = 69.36 EUR. The total cash inflow is the MVE + fees = 76 USD. The daily performance is thus [75/(0 + 76)] - 1 = -0.0132 or -1.32%. The cumulative performance = [(1+0) x (1+0) x (1 -0.0132)] -1 = -1.32%. 
    * portfolio: The MVE of the portfolio is the sum of the MVEs of the two shares, plus what is left in the deposit accounts: 100 + 69.36 + 120 + 2.87 (USD 3.10 x 0.9248) = 292.23 EUR. The daily performance is [292.23/(295+0)] - 1 = -0.0094 or -0.094%. The cumulative performance = [(1 - 0.0167) x (1 + 0) x (1 -0.0094)] -1 = -2.59%.
- **March 4**
    * share-1: The capital gain and the dividend of share-1 positively impact both the daily and cumulative performance. The daily performance for share-1 is ((110 + 13)/100) -1 = 0.13 or 13%. The cumulative performance becomes: [(1-0.0291)x(1+0)x(1+0)x(1+0.23)] - 1= 19.42%.
    * share-2: The MVE decreases to 5 x 13 USD = 65 USD or 65 x 0.9220 = 59.93 EUR. The daily performance is (59.93/69.36) - 1 = -13.6%. The cumulative performance = [(1+0) x (1+0) x (1 -0.0132) x (1-0.1360)] -1 = -14.74%. 
    * portfolio: The portfolio performance becomes also positive. The MVE = 110 (share-1) + 59.93 (share-2) + 128 (deposit account in EUR) + (76 USD  x 0.9220) or 300.79 EUR. The daily performance is thus (300.79/292.23) - 1 = 0.0293 or 2.93%. The cumulative performance is [(1-0.0167)x(1+0)x(1-0.0094)x(1+0.0293)] - 1= 0.26%.
- **March 5**
    * share-1: There are 5 share-1 left. So, the MVE of share-1 is 5 x 12 = 60 EUR. But, 5 shares were sold: 5 x 12 minus fees = 55 EUR. The daily performance is [(60 + 55)/110] - 1 = 4.55%. The cumulative performance of share-1 is [(1-0.0291)x(1+0)x(1+0)x(1+0.23)x (1+0.0455)] - 1= 24.85%.
    * Share-2: Profits too from a capital gain. The MVE becomes 5 x 15 = 75 or 69.13 EUR. The daily performance is (69.13/59.93) - 1 = 15.35%. The cumulative performance of share-1 is [(1+0)x(1+0)x(1-0.0132)x(1-0.1360)x(1+0.1535)] - 1= -1.65%; slightly negative, due to the capital loss on March 4.
    * Portfolio: The MVE of the portfolio = 60 (share-1) + 69.13 (share-2) + 177 (deposit account in EUR) + (3.10 USD x 0.9217 = 2.86) or 308.99 EUR.  The daily performance is thus (308.99/300.79) - 1 = 0.0273 or 2.73%. The cumulative performance is [(1-0.0167)x(1+0)x(1-0.0094)x(1+0.0293)x(1+0.0273)] - 1 = 3.00%.
