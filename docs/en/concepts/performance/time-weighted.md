---
title: Time-Weighted Rate of Return
---
The calculation of the time-weighted rate of return starts with dividing the reporting period into distinct holding periods. For each holding period, a return value is calculated and then compounded into an overall return. Each period carries equal weight; hence the name time-weighted rate of return. In the True Time-Weighted Rate Of Return methodology (TTWROR), performance is calculated using simple returns without any consideration for the total amount invested.

To minimize the computational effort, older methods utilized larger holding periods. A natural marker could be the dates of each cash flow.  The holding periods would be formed by: `Period Start --> CF1, CF1 --> CF2, CF2 --> CF3, ..., CFn-1 --> Period end`. A holding period starts at period start or immediately before a cash flow and ends just before the following cash flow or the period end: CF1 is included in HP1 but CF2 isn't. If any cash flow exists outside the reporting period, making the Market Value Begin > 0, then the first holding period must start at the beginning of the reporting period. Otherwise, the first period starts with the first CF. Figure 1 illustrates the various concepts, applied to our demo-portfolio-03, with a three-year reporting period, making MVB = 0.

Figure: Calculation of True Time-Weighted Rate of Return.{class=pp-figure}

![](images/info-ttwror-example-visualisation.svg)


For every holding period, the return rate is computed using Equation 1.

$$\mathrm{r = \frac{MV_t}{MV_{t-1} + CF_t} - 1 \qquad \text{(Eq 1)}}$$

where $MV_t$ = the market value of the portfolio at the end of holding period *t*, $MV_{t-1}$ = the market value of the previous holding period.  $CF_t$ is the incoming (positive) or outgoing (negative) cashflow in that period.

The return rate is thus corrected for the cashflow, occurring in that period. If the cash flow is incoming or positive, the MVB of the period is increased by it making the performance independent of the cash flow. For example, suppose that MV1 = 100, CF2 = 200, MV2 = 300 for a certain holding period. Without the correcting mechanism, the return would be calculated at 300% while in fact your portfolio hasn't changed and the performance should be 0%.

Please note that for  for each holding period, you require the market value of the portfolio *twice*: once at the end of the previous holding period and once at the end of the current one. 

After calculating the return rates of each period, they are compounded with the following formula.

$$\mathrm{r = [(1 + r_1) \times (1 + r_2) \times (1 + r_3) \cdots (1 + r_{n-1}) \times (1 + r_n)] - 1 \qquad \text{Eq  2}}$$

where $r_t$ is the return rate from holding period *t*.

# TTWROR at portfolio level

Our [demo-portfolio-03.xml](../../assets/demo-portfolio-03.xml) has three cash flows (see Figure 1). Because all cash flows fall within the reporting period, the first period (`Period start --> CF1`)could be omitted. The market value is zero at both the beginning and end of the period.

The market value is the sum of the value of all deposit and securities accounts. To determine the value of a security, the (historical) closing price is taken. A cashflow can be positive (inbound transfer) or negative (outbound transfer); assuming that fresh money is added at the beginning of the day (and hence is available to generate return) and removed at the end of the day.

For each period, you need $MV_{t-1}$ and the current $MV_{t}$ period. Because the market value is determined at the end of the trading day (closing price), $MV_{t-1}$ is also the value immediately before the cashflow at the beginning of the day.

!!! Note
    One could argue that, as we are required to add the cash flow to $MV_{t-1}$ (as per Equation 1), an alternative approach is to consider the market value of $MV_{t}$, which already includes this cash flow. However, it's important to note that throughout the day, market forces may cause fluctuations in $MV_{t-1}$, and these variations should be excluded when determining the market value at the beginning of the day, just before the cash flow.

Manually calculating these portfolio market values can be a tedious task. It involves multiplying the number of shares for each security by the historical price and then adding fees and other relevant factors. But in PP, you can also generate a spreadsheet for all days in the reporting period with these values (see below).

Figure: Manual calculation of cumulative and annual TTWROR.{class=pp-figure}

![](images/info-ttwror-manual-calculation.png)

As can be seen in Figure 2 [[download workbook](../../assets/demo-portfolio-03-calculation.xlsx)], the market value at the beginning of the HP1 is zero EUR (= the closing value of the previous period) and 160.26 at the end (immediately before the next cash flow). There was one inbound positive cashflow of 155 EUR, necessary for buying 10 shares of `share-1`. The return of this period = 160.26/(0 +155) = 3.39%. Thus, eliminating the effect of the incoming cash flow, your portfolio has grown with 3.39% during this holding period of 364 days.

Compounding these individual periodical returns into one portfolio return for the whole portfolio with Equation 2 results in a cumulative performance of 44.16%.

Since computer time is inexpensive nowadays, there's no need to define long holding periods to minimize manual computation. Therefore, PP employs a single day as the holding period. You can export a file with daily portfolio. Select the menu `View > Reports > Performance > Chart` and click the icon (top right) `Export Data as CSV`. Choose `Export Entire Portfolio` (see Figure 3 for an example).

The calculation is analogous to the explanation for manual calculation using longer holding periods. Before `2021-01-15`, all values are zero, as the first transaction occurred on that day. The `Delta in %` is equivalent to the value of *r* in the manual calculation. The formula is slightly different: `(MV_t + Outbound Transfer)/(MV_t-1 + Inbound transfer)`. The market value at the end of the period (day) is increased by all outbound transfers, such as withdrawals. In the manual calculation, a separate transfer would be used for this purpose.

Figure: Export TTWROR data from PP.{class=pp-figure}

![](images/info-ttwror-export-data-from-pp.png)

It's important to highlight that the performance for '2021-01-15' is negative. This is the result of the market value of the portfolio being smaller at that moment than the required cash flow, owing to the taxes and fees associated with acquiring the security. Fortunately, the subsequent market rally has led to a cumulative performance increase to 3.39%, aligning precisely with the manually calculated value for the first holding period.




