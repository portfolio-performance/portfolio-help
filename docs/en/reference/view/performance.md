---
title: Performance
TODO: Risk indicators
---
Key performance and risk indicators are summarized in a dashboard, along with a calculation widget. The dashboard can be accessed through the menu `View > Reports > Performance` or with the sidebar (see figure 1).

Figure: Dashboard with key performance and risk indicators and calculation widget.{class=pp-figure}

![](images/performance-dashboard-3yrs.png)

Please note that the performance and risk indicators are always calculated for a specific [reporting period](../../concepts/reporting-period.md). By default, this is one year from today. You can change the period by selecting a different one or create a new one in the drop-down (top-right). In Figure 1, the reporting period is from Jun 12, 2020 till Jun 12, 2023. For the performance key indicators, the color green indicates a profit, while red signifies a loss. 


## Key performance indicators

### True Time-Weighted Rate of Return (cumulative)

The cumulative True Time-Weighted Rate of Return (TTWROR) is the geometric average of the daily returns within the reporting period. For each day within the reporting period, the daily return is calculated using Equation 1.

$$\mathrm{r = \frac{MV_t}{MV_{t-1} + CF_t} - 1 \qquad \text{(Eq 1)}}$$

where $MV_t$ = the market value of the portfolio at the end of day *t*, $MV_{t-1}$ = the market value of the previous day.  $CF_t$ is the incoming (positive) or outgoing (negative) cashflow for day *t*.

The calculation panel cannot, of course, display all the Initial and Final values of each day. For the first day of the reporting period $MV_t$ is equal to the `Initial value` in the calculation panel. For the last day of the reporting period, $MV_t$ is equal to the `Final value`. The sum of all cash flows in the period is given by the sum of the Performance neutralTransfers + Fees + Taxes + Earnings. 

After calculating the return rates of each period, they are cumulated or compounded with the following formula.

$$\mathrm{r = [(1 + r_1) \times (1 + r_2) \times (1 + r_3) \cdots (1 + r_{n-1}) \times (1 + r_n)] - 1 \qquad \text{Eq  2}}$$

where $r_t$ is the return rate from day *t*.

An in-depth explanation of the TTWOR calculation is given [Concepts > Performance > True Time-Weighted Rate of Return](../../concepts/performance/time-weighted.md).

### Internal Rate of Return (IRR)

The money-weighted rate of return or IRR of a reporting period is the annual interest rate that is necessary to bring the market value of the investment at the beginning of the period (MVB) and all subsequent cash flows to the market value (MVE) at the end of the reporting period. To generate the specified cash flows within the given time period, your portfolio must grow each year by a percentage equal to the IRR. The base formula for the IRR calculation is:

$$\mathrm{MVE = MVB \times (1 + IRR)^{\frac{RD_1}{365}} + \sum_{t=1} ^{n}CF_t \times (1+IRR)^{\frac{RD_t}{365}} \qquad \text{(Eq 1)}}$$

where *n* = the number of cash flows in the reporting period, $CF_t$ = cash flow at time *t* within the period, and $RD_t$ = the number of remaining days within the period. For MVB, the $RD_t$ equals the entire period, representing the period length in years. You can simplify the equation by treating the MVB as the initial cash flow. A cash flow is any amount of money that is added to or withdrawn from an investment. For an in-depth explanation, see  [Concepts > Performance > Money-Weighted Rate of Return](../../concepts/performance/money-weighted.md).
 
### Absolute Change

The absolute Change is the difference between the market value of the portfolio at the end date of the reporting period (MVE) and the market value at the beginning (MVB).

$$\mathrm{MVE - MVB\qquad \text{(Eq 3)}}$$

For example, in Figure 1 (calculation widget), the absolute change equals the Final Value (426.82 EUR) minus the Initial value (0 EUR).


Let's skip the first two key indicators and focus on the simpler ones first. The Absolute Change is 426.82 EUR. Take a look at the Calculation panel on the right side. The initial value of your portfolio as of June 12, 2020 was zero EURO and the final value is 426.82 EUR, which, of course, equals the absolute change.

### Delta

The Delta value (for the reporting period) is equal to the Absolute Change (see above) minus the external cash flows that occurred in the period.

$$\mathrm{(MVE - MVB) - \sum_{t=1} ^{n}CF_t {\qquad \text{(Eq 4)}}}$$

For example, the Delta in Figure 1 is 120.82 EUR. This value represents the actual return of securities in the portfolio. The absolute change in the portfolio is partly caused by external cash inflows (306 EUR to buy the securities). This money comes from an external source and should be subtracted from the Absolute change. They are summarized as Performance neutral Transfers in the calculation panel.

## Last Day
 
### Last Day: True Time-Weighted Rate of Return

One would assume that the Last Day is the same as the ending day of the reporting period. Unfortunately, it is not. It is the previous trading day before 'today' as can be seen when hovering over the label. Figure 1 is created on December 8, 2023. The market value of the portfolio was at that time 459.31 EUR. The last trading day before this date is 2023-12-07 with a MV = 455.84 EUR. There are no cashflows on the last day.

The TTWOR for that day is given by Eq. 1 or (459.31 - 155.84)/455.84 = 0.76%. 

### Last Day: Absolute Change
Equation 3 can be used to calculate the Absolute Change of the last day. It's obvious that the value equals 3.47 EUR = 459.31 EUR - 155.84 EUR.




## Risk indicators
### Maximum Drawdown
### Maximum Drawdown Duration
### Volatility
### Semivariance

By default, the dashboard contains three widgets (panels): `Key Indicators`, `Risk Indicators`, and `Calculation`. Right mouse click on an empty space of the canvas lets you add more widgets (see later).

!!! note
	The key and risk indicators consider the whole portfolio by default. However, you can narrow down the calculation to specific accounts or securities by right-clicking the indicator label and choosing a different data series.