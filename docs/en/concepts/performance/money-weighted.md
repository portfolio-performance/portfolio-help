---
title: Money weighted rate of return
---
# The money-weighted rate of return
The money-weighted rate of return is in fact identical to the Internal Rate of Return (IRR) technique used in project management. This calculation considers both the timing (when) and the amount (how much) of the cash flows within the reporting period. A cash flow is any amount of money that is added to or withdrawn from a portfolio. The base formula for the IRR calculation is:

$$\mathrm{MVE = MVB \times (1 + IRR)^{\frac{RD}{365}} + \sum_{t=1} ^{n}CF_t \times (1+IRR)^{\frac{RD_t}{365}} \qquad \text{(Eq 1)}}$$

where *n* = the number of cash flows in the reporting period, $CF_t$ = cash flow at time *t* within the period, and $RD_t$ = the number of remaining days within the period. For MVB, $RD$ equals the entire period, represented in days. To annualize the return rate, you need to divide the remaining days by 365. To calculate the periodic return rate (for the entire period), divide by the number of days of the period.

Equation 1 closely resembles the calculation of Future Value. In Figure 1, assuming a 10% interest on your investments, the initial 1000 EUR capital will grow to 1331 EUR in three years. Additional cashflows of 500 EUR and 1000 EUR in the following years will result in 605 EUR and 1100 EUR respectively. The Future Value of the total investment will then be 3036 EUR in three years.

Figure: Visualization of Future Value calculation.{class=pp-figure}

![](images/info-irr-future-value.svg) 

Calculating IRR is in fact the inverse of calculating the future value (FV) of an investment. You don't know the interest rate or IRR, but you do know the MVB, the MVE, and the intermittent cashflows. According to Eq. 1 (assuming year as time unit):

`3036 EUR = 1000 EUR x (1 + IRR)^3 + 500 EUR x (1 + IRR)^2 + 1000 EUR x (1 + IRR)^1`

Since PP uses days as standard period, we need to divide the remaining number of days that the cash flow could influence the performance by 365 to obtain a decimal representation of the yearly period. $\mathrm{CF_t \times (1+IRR)^{\frac{RD_t}{365}}}$ is thus the expected future value of the cash flow CF at time *t* by the the end of the period with an annual interest rate = IRR. Please note that in the absence of any cash flows, Equation 1 resembles the simple return formula [MVE = MVB x (1 + r)](./index.md).

The IRR is the annual interest rate that is necessary to bring the beginning value of the investment (MVB) and all subsequent cash flows to the end value (MVE). To produce the specified cash flows within the given time period, your portfolio needs to grow each year by a percentage equal to the Internal Rate of Return (IRR).

Unfortunately, there is no easy way to derive the value of IRR from Equation 1. Software tools such as Excel have functions like IRR and XIRR, that employ a brute-force approach, iteratively solving the equation with various "guesses" of IRR until a suitable match is identified. In the examples below we will use the Goal Seek method of Excel to illustrate the solution.

!!! Important
    Performance is always calculated for a certain period of time *and* an investment unit. This unit could encompass the entire portfolio, comprising all security and deposit accounts, a particular security account containing multiple securities, an individual security (e.g., share-1), or even a specific trade within a security.

## IRR at portfolio level
The following examples will calculate the IRR for the whole portfolio. For example, our demo-portfolio-03 contains two securities and one deposit account. The resulting IRR should not be extrapolated to an individual security. It's the performance of the whole portfolio. Of course, you can calculate the IRR for a [specific security](#irr-on-security-level) or even [trade](#irr-on-trade-level) in PP. 


### Example 1: one buy transaction
In our [demo-portfolio-03](../../assets/demo-portfolio-03.xml) all transactions take place within a holding period of three years, starting at `2020-06-12`. Consequently, the MVB for this period is 0 EUR because the portfolio is empty at the beginning of the period. The following transactions occur in the holding period (see Figure 1 below).

Figure: Overview of transactions - Deposit (3x), Buy (3x), Dividend, and partial Sell.{class=pp-figure}

![](images/info-irr-example-transactions.png) 

Figure: Graph of historical quotes and transactions of share-1. {class=pp-figure}

![](images/info-irr-example-share-1.png)

Figure: Graph of historical quotes and transactions of share-2. {class=pp-figure}

![](images/info-irr-example-share-2.png)

Assume that *only*  two transactions have occurred: the deposit (155 EUR) and the purchase of `share-1`. However, from the perspective of the Portfolio, there is only one cash inflow of 155 EUR into a deposit account. Whether this deposit is used for a purchase is irrelevant in assessing the portfolio's performance. The positive or negative impact of this choice will be evident in the MVE. Calculating the IRR in this context should be straightforward.

- MVB = 0 EUR at 2020-06-12. The period length is three years or 1095 days.
- First cash inflow on January 15, 2021. This deposit will remain in the portfolio (be it as a purchase of share-1) for an additional 878 days until MVE at 2023-06-12.
- MVE = 10 shares at quote 19.006 EUR; in total 190.06 EUR. The deposit account is empty.

Plugging in these values into Equation 1 gives: `190 EUR = 0 EUR x (1+IRR)^1095/365 + 155 EUR x (1+IRR)^878/365` Since MVB = 0, we can derive the IRR directly: `IRR = (190.06/155)^(365/878) - 1` or 8.85%.

In order to generate a MVE of 190.06 EUR, the initial cash flow CF1 of 155 EUR must grow at 8.85% per year for 2.41 years or 878 remaining days.

### Example 2: multiple buy transactions
When dealing with multiple cash flows, deriving the Internal Rate of Return (IRR) becomes more complex. Take, for example, the three buying transactions from Figure 1. The same logic as mentioned earlier still applies, albeit with a bit more complexity.

- MVB is still zero EUR at 2020-06-12. The period length is three years or 1095 days.
- Three cash flows (see Figure 1). The remaining days in the reporting period are respectively 878, 514, and 255 days.
- MVE = 15 shares at a quoted price of 19.006 EUR, and 5 shares at 13.77 EUR, totaling 396.85 EUR. The deposit account is empty.

$$
\mathrm{MVE = MVB \times (1 + IRR)^{\frac{1095}{365}} + CF_1 \times (1+IRR)^{\frac{878}{365}} + CF_2 \times (1+IRR)^{\frac{514}{365}} +  CF_3 \times (1+IRR)^{\frac{255}{365}}  \quad (Eq  3)}
$$

Figure 4 illustrates the calculation in Excel ([download workbook](../../assets/demo-portfolio-03-calculation.xlsx)). The initial cash flow of 155 EUR will have grown to 219.68 EUR, if the holding period was 878 days and the yearly interest rate was 15.60%. The second buy will increase from 84 EUR to 103.03 EUR. The profit of `share-2` appears smaller due to the smaller amount of holding days. The calculation of IRR can be simulated in Excel using the `Data > Goal Seek method` (see Figure 4). The method tries to set the value of the calculated MVE (cell F11) to the observed MVE (manual input) by iteratively changing the value of IRR, until a match (15.60%) is found.

Please note that the individual calculated end values of the shares do not necessarily correspond with the observed individual end values. Compare for example the expected and observed value of `share-2`. The observed value is much higher. Only the sum of the whole portfolio match and the same calculated IRR is applied to all shares. PP can - of course- also calculate the IRR for individual securities; see below to calculate the performance of [individual securities](#irr-on-security-level) and [trades](#irr-on-trade-level).

Figure: IRR-calculation for three buy-transactions. {class=pp-figure}

![](images/info-irr-caluclation-excel-buys-only.png)

### Example 3: buy - dividend - sell transactions
Whether dividend payments and selling securities should be considered as cash flows depends on the context. In demo-portfolio-03, the outcomes of dividend and selling transactions are deposited in a cash account, which is part of the portfolio. Consequently, there isn't any 'external' cash flow. For example, selling shares will decrease the security account of the portfolio but increase the deposit account. There isn't any cash flowing out of the portfolio. Note also that the cash account is included in the portfolio valuation at the end of the period (MVE), meaning that the value of MVE already incorporates dividends and sales. 

If the dividend payment is "consumed" (you bought yourself a coffee from it), resulting in an external cash flow (withdrawal), this transaction should be recorded in PP as a removal. Similarly, if you choose to reinvest the dividend or the proceeds from a sale, it necessitates recording a new transaction in PP.

As evident in Figure 5, MVE comprises the paid dividend and the outcome of the sale transaction (both held in a deposit account), in addition to the valuation on the end date of the remaining shares from the portfolio. This aligns with what PP displays in the calculation tab.  The MVE is the total of all deposit and securities accounts.

Figure: IRR-calculation for buy-sell-dividend transactions. {class=pp-figure}

![](images/info-irr-caluclation-excel-buys-dividend-sell.png)

If you should like to consider the dividend and sale as a cash flow, then you should change the transaction date to the holding period end date. Indeed, before the end date, these payments essentially remain dormant on the cash account, without actively contributing to the portfolio. As the number of remaining days in the period reaches zero, the formula will simplify to the face value of the dividend and sale.

`MVE = 426.82 = 155 x 1.2^(878/365) + 84 x 1.2^(514/365) + 67 x 1.2^(255/365)`

### Example 4: MVB > 0
In the previous examples, all transactions took place within the reporting period. This isn't always the case. It is very important to distinguish the following cases:

  1. $CF_t$ occurs before the beginning of the reporting period (MVB date).  PP will calculate the value of $CF_t$ through historic quotes at time *t*. The market value of the investment at time *t* is used in the calculation, not the purchase value. The holding period is the entire reporting period.

  2. $CF_t$ occurs after the beginning but before the end of the reporting period. The value of $CF_t$ is known through the transaction data. The holding period is the number of remaining days from time *t* until the end of the reporting period.

  3. $CF_t$ falls after the end of the reporting period. $CF_t$ does not contribute to MVE and is omitted from the calculation of IRR for that reporting period.

 Consider a scenario where the holding period is only *two* years (from 2021-06-12 to 2023-06-12), or 730 days. Since the first buy of `share-1` occurs outside of this period (item 1 from above), the quoted price of `share-1` at the beginning of the period is used rather than the actual buying price.

- MVB = 177.94 EUR, representing 10 shares of `share-1` at the closing price of 17.794 EUR on June 11, 2021 (= the closing price from the day before the start of the period).
- Additional buys: two additional buys within the reporting period with respective remaining days of 514 and 255 days and known buying transaction price. Remember, the dividend and sale will be valuated at end date in the MVE.
- MVE = 426.82 EUR, including 125 EUR on the cash account from dividend and sale.

The resulting formula with IRR = 17.63% is:

`MVE = 426.82 EUR = 177.94 x 1.18^(730/365) + 84 x 1.18^(514/365) + 67 x 1.18^(255/365)`

Figure: IRR-calculation for a 2 year holding period (MVB > 0).{class=pp-figure}

![](images/info-irr-caluclation-excel-2y-period.png)


## IRR at security level

The value of IRR, calculated at portfolio level, doesn't say much about the performance of a specific security. For example, the IRR of demo-portfolio-03 (3 years reporting period) is 20.28% (see Figure 6). The security IRR of `share-2` is 112.53% (see Figure 8 at the top). A quick look at Figure 4 should clarify why: the security is acquired at the lowest price throughout the entire period.

You can obtain the IRR for each security separately using the menu `View > Reports > Securities`. The calculation closely resembles that of the portfolio. However, the following deviates from the portfolio calculation.

Figure: IRR-calculation for individual securities.{class=pp-figure}

![](images/info-irr-calculation-securities.png)

- The most appropriate cash flow to consider when calculating the security's IRR appears to be the debited amount of the transaction, which encompasses the gross value plus taxes and fees. However, it's important to note that taxes are *excluded* from the calculation of security IRR. This exclusion is justified as taxes are not directly associated with a specific security, they are imposed by the government (sometimes collected at later dates), and are beyond the investor's control. Unlike fees, which can be influenced to some extent, taxes cannot. Therefore, the cash flow to consider for the security IRR calculation is the debit note of the transaction minus taxes.

- In contrast to the portfolio IRR, dividends and sale results are treated as a cashflows; leaving the "security" at the transaction date in Security IRR calculations. Selling the security (at a good or bad time) and paying dividends will impact the performance of the security. As a result, deposit accounts are *not* included in the Security IRR calculation.

- With a multi-transaction security, the purchase price and value could be somewhat tricky to obtain. For instance, the remaining 10 shares of `share-1` are the outcome of two purchase transactions and one sell transaction. Following the FIFO principle (First In, First Out), these 10 shares consist of the 5 remaining shares from the first buy and the 5 shares from the second buy. This results in an average price of 15.50 EUR (see example 6).

### Example 5: a security with one buy transaction

A straightforward example is illustrated by the IRR calculation of `share-2`. The single buy transaction falls within every holding period (1,2, or 3 years). The transaction debit note minus taxes is used to determine the cash flow; e.g. 66 EUR.

- MVB = 0 EUR.
- First cashflow: 8 shares at 8 EUR/share + 2 EUR fees. Remaining days = 255 for a 3 year period, ending at 2023-06-12.
- MVE = 111.76 EUR or 8 shares at 13.97 EUR/share.

Inserting these values into Equation 1 gives
`111.76 = 0 x (1+IRR)^1095/365 + 66 x (1+IRR)^255/365`

`IRR = ((111.76/66)^(365/255)) - 1 = 112.53% ` (see Figure 8)

### Example 6: a security with multiple transactions

As can be seen in Figure 2, `share-1` has multiple transactions, 2x buy, partial sell and dividend. It's important to get the dates and cash flows correct, see Figure 9.

Figure: IRR-calculation for individual security with multiple transactions.{class=pp-figure}

![](images/info-irr-calculation-multiple-securities.png)

The first and second cashflow is rather straightforward. 10 shares at 15 EUR/share + 3 EUR fees and 5 shares at 16 EUR/share plus 3 EUR fees. Assuming an IRR = 18% (see Figure 8), the calculated end value of share-1 = 153 x 1.18^(878/365) = 227.81 EUR. 

Please note that dividend payments and sales are recorded on the transaction date. This differs from the behavior observed in IRR calculations at the portfolio level. From the perspective of the security, both the dividend and sale amounts constitute a cash outflow, even if they are deposited into the portfolio. Due to this outflow, the cash flow is considered negative.

Inserting these values into Equation 2 gives:
`190.06 = 153 x (1+IRR)^(878/365) + 83 x (1+IRR)^(514/365) - 30 x (1+IRR)^(179/365) - 107 x (1 + IRR)^(61/365)` As can be seen from Figure 8, an IRR = 18.00% will fit the equation..


## IRR at trade level
A trade is formed by aggregating all buy and sell transactions related to a specific security. A trade can be `closed`, indicating that no further transactions can be conducted within this trade or `open`: more transactions are possible. The demo-project-03 contains 3 trades (see `Report > Performance > Trades`; Figure 10).  A *closed* trade starting with a buy of `share-1` on `2021-01-15` and ending with a partial sell on `2022-01-14`. The remaining shares initiate the second *open* trade, starting at `2022-01-14` and ending at the current date (e.g. `2023-06-12`). The third trade is also open because `share-2` hasn't been sold yet.

The performance of a trade is always calculated with the fees and taxes included.

Figure: IRR-calculation for trades.{class=pp-figure}

![](images/mnu-view-reports-trade-irr-example.png)

Please note that, in contrast with the portfolio and security IRR calculation, you can not set a reporting period.  A closed trade has a fixed begin and end date. All open trades have an end date set as of today.

Also note that PP follows a `FIFO principle` (First-In; First-Out) to determine which shares will be sold. The 5 shares sold on `2023-04-12` correspond to those acquired on `2021-01-15`, rather than the ones obtained on `2022-01-14`.

### Example 7: IRR calculation of a closed trade

Five shares of `share-1` were sold on April 12, 2023. The historical closing price on that day was 22.40 EUR/share. Fees and taxes were 7 EUR, giving a net transaction value of 105 EUR (see Figure 1) or the Exit value in Figure 10.

Because of the FIFO-principle, these 5 shares were from the 1th buy, meaning that they are purchased for 5 x 15 EUR = 75 EUR. The fees and taxes (5 EUR for 10 shares) are proportionally allocated, in this case, 5/2 = 2.5 EUR. The entry value of this closed trade is thus 77.50 EUR. The securities are held for 817 days (from `2021-01-15 till 2023-04-12`). Inserting these values in Equation 1 and solving for IRR gives:

`IRR = = (105/77.5)^(365/817) - 1 = 14.53%`

### Example 8: IRR calculation of an open trade

The open trade involving `share-2` is rather simple. Referring to Figure 1, these shares were acquired for a net value of 64 EUR + 3 EUR fees and taxes on `2022-09-30`, which was 255 days ago. The current value is 111.76 EUR, resulting in `IRR = (111.76/67)^(365/255) - 1 = 108% `.

!!! Important
    PP will always use the current date to calculate an open trade IRR. If you want to follow the previous example, you can try to change the system date on your computer and restart PP. 

The open trade involving `share-1` is a special case. Since it is an open trade, it ends on the current day (`2023-06-12`). The number of days between the purchase date and today is 696 days. The historical price on this date was 19.006 EUR/share. The exit value is thus 190.06 EUR.

The trade consists of shares that were bought in 2021 and in 2022. Five shares are from 2021. The cash flow of these shares is thus 77.5 EUR (see also paragraph above). Today, they are valuated at 95.03 EUR. The remaining 5 shares are from `2022-01-04` with a cash flow of 5 x 16 EUR/share + 4 EUR fees and taxes (see Figure 1). These 5 shares are also 95.03 EUR worth today (`2023-06-12`).

This corresponds with PP (see Figure 9 above): the exit value is 190.06 = 2 x 95.03 EUR and the entry value is 77.5 + 84 = 161.50 EUR. Inserting these values in Equation 1:

`190.06 = 77.5*(1+IRR)^(878/365) + 84*(1+IRR)^(514/365)`

Finding IRR with Goal Seek gives IRR = 9.16%.



