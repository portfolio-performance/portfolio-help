---
title: Performance
TODO: Risk indicators
---
Key performance and risk indicators are summarized in a dashboard, along with a calculation widget. The dashboard can be accessed through the menu `View > Reports > Performance` or with the sidebar (see figure 1).

Figure: Dashboard with key performance and risk indicators and calculation widget.{class=pp-figure}

![](../../images/performance-dashboard-3yrs.png)

Please note that the performance and risk indicators are always calculated for the entire portfolio and for a specific [reporting period](../../../../concepts/reporting-period.md). By default, this is one year from today. You can change the period by selecting a different one or create a new one in the drop-down (top-right). In Figure 1, the reporting period is `from Jun 12, 2020 till Jun 12, 2023`. For the performance key indicators, the color green indicates a profit, while red signifies a loss. 


## Key performance indicators

### True Time-Weighted Rate of Return (cumulative)

The cumulative True Time-Weighted Rate of Return (TTWROR) is the geometric average of the daily returns within the reporting period. For each day within the reporting period, the daily return is calculated using Equation 1. The cumulative return is computed with Equation 2.


$$\mathrm {r_{daily} = {\frac{MVE + CF_{out}}{MVB + CF_{in}} - 1 {\qquad \text{(Eq 1)}}}}$$

and

$$\mathrm {r_{cum} = [(1 + r_1) \times (1 + r_2) \times ... \times (1 + r_n)] - 1 {\qquad \text{(Eq 2)}}}$$

where MVE = the market value of the asset at the end of day, MVB = the market value at the beginning of the day (or the end of the previous day).  CF<sub>in</sub> and CF<sub>out</sub> represent the net incoming or outgoing cashflows for the day. When a stock pays a dividend, that's an outgoing cashflow from the stock's perspective. A deposit (for buying the stock) is a cash inflow, as is paying the associated fees.

An in-depth explanation of the TTWOR calculation is given [Concepts > Performance > True Time-Weighted Rate of Return](../../../../concepts/performance/time-weighted.md). A step-by-step calculation for a very simplified example can be found at [View > Reports > Performance > Chart](../performance/performance-chart.md).

### Internal Rate of Return (IRR)

The money-weighted rate of return or IRR of a reporting period is the annual interest rate that is necessary to bring the market value of the investment at the beginning of the period (MVB) and all subsequent cash flows to the market value (MVE) at the end of the reporting period. To generate the specified cash flows within the given time period, your portfolio must grow each year by a percentage equal to the IRR. The base formula for the IRR calculation is:

$$\mathrm{MVE = MVB \times (1 + IRR)^{\frac{RD_1}{365}} + \sum_{t=1} ^{n}CF_t \times (1+IRR)^{\frac{RD_t}{365}} \qquad \text{(Eq 3)}}$$

where *n* = the number of cash flows in the reporting period, $CF_t$ = cash flow at time *t* within the period, and $RD_t$ = the number of remaining days within the period. For MVB, the $RD_t$ equals the entire period, representing the period length in years. You can simplify the equation by treating the MVB as the initial cash flow. A cash flow is any amount of money that is added to or withdrawn from an investment. For an in-depth explanation, see  [Concepts > Performance > Money-Weighted Rate of Return](../../../../concepts/performance/money-weighted.md).
 
### Absolute Change

The absolute Change is the difference between the market value of the portfolio at the end date of the reporting period (MVE) and the market value at the beginning (MVB).

$$\mathrm{MVE - MVB\qquad \text{(Eq 4)}}$$

For example, in Figure 1 (calculation widget), the absolute change equals the Final Value (426.82 EUR) minus the Initial value (0 EUR).

### Delta

The Delta value (for the reporting period) is equal to the Absolute Change (see above) minus the external cash flows that occurred in the period.

$$\mathrm{(MVE - MVB) + \sum_{t=1} ^{n}CF_t {\qquad \text{(Eq 5)}}}$$

For example, the Delta in Figure 1 is 120.82 EUR. This value represents the actual return of securities in the portfolio. The absolute change in the portfolio is partly caused by external cash inflows (306 EUR to buy the securities). This money comes from an external source and should be subtracted from the Absolute change. They are summarized as Performance neutral Transfers in the calculation panel.

## Last Day
 
### Last Day: True Time-Weighted Rate of Return

One would assume that the Last Day is the same as the ending day of the reporting period. Unfortunately, it is not. It is the previous trading day before 'today' as can be seen when hovering over the label. Figure 1 is created on December 8, 2023. The market value of the portfolio was at that time 459.31 EUR. The last trading day before this date is 2023-12-07 with a MV = 455.84 EUR. There are no cashflows on the last day.

The TTWOR for that day is given by Eq. 1 or `(459.31 - 155.84)/455.84 = 0.76%`. 

### Last Day: Absolute Change
Equation 3 can be used to calculate the Absolute Change of the last day. It's obvious that the value equals `3.47 EUR = 459.31 EUR - 155.84 EUR`.




## Risk indicators
### Maximum Drawdown
### Maximum Drawdown Duration
### Volatility
### Semivariance

By default, the dashboard contains three widgets (panels): `Key Indicators`, `Risk Indicators`, and `Calculation`. Right mouse click on an empty space of the canvas lets you add more widgets (see later).

!!! note
	The key and risk indicators consider the whole portfolio by default. However, you can narrow down the calculation to specific accounts or securities by right-clicking the indicator label and choosing a different data series.