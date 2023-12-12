---
title: Performance
---

Naturally, your portfolio's performance is a top priority for you and PP, which is why the software is named as such. Key performance indicators are summarized in a dashboard, that can be accessed through the menu `View > Reports > Performance` or with the sidebar (see figure 1).

How is your demo portfolio doing? Set the Reporting period to a 3 year period; e.g. from June 12, 2020 until 2023. 

Figure: Dashboard with key performance indicators.{class=pp-figure}

![](../../../images/sb-reports-performance.png)

!!! note
	The key and risk indicators consider the whole portfolio by default. However, you can narrow down the calculation to specific accounts or securities by right-clicking the indicator label and choosing a different data series.

Let's skip the first two key indicators and focus on the simpler ones first. The Absolute Change is 426.82 EUR. Take a look at the Calculation panel on the right side. The initial value of your portfolio as of June 12, 2020 was zero EURO and the final value is 426.82 EUR, which, of course, equals the absolute change. You can check the final value with `sidebar > Reports > Performance > Calculation`. Click at the `Assets at End` heading tab. As you can see, there is 125 EUR in the deposit account from the dividend and sell transactions. `share-1` is valuated at 190.06 EUR (10 shares remaining x 19.06) and `share-2` at 111.76 (8 shares x 13.97). Taken together, this sums to 426.62 EUR, which represents the market value of your portfolio on June 12, 2023.

The Delta (for reporting period) is 120.82 EUR. This value represents the actual return of `share-1` and `share-2`. The final portfolio value of 426.82 EUR is partly caused by external cash inflows of 155 EUR and 84 EUR to buy `share-1` and 67 EUR to buy `share-2`. This money comes from an external source and should be subtracted from the Absolute change. They are summarized as Performance neutral Transfers in the calculation panel.

The Absolute change of the Last Day is negative (red). It remains the same for each reporting period. Hovering over the label gives some info. This value is the absolute change for a Reporting period of 1 trading day. Unfortunately, it's not the last day of the chosen reporting period; e.g. 11-12 Jun 2023, but the last trading day before 'today'.

What about the True Time-Weighted Rate of Return (TTWOR) and the Internal Rate of Return (IRR) indices? The IRR is a percentage that shows how well your portfolio performs, considering when and how much money you have put in or take out. TTWOR measure the growth of your investments without being influenced by the timing and size of your contributions or withdrawals. An in-depth explanation of both measurements is given at [Concepts > Performance](../../../concepts/performance/index.md)

How should you interpret the difference between the two measures? If you look at the chart of historical prices of `share-1` and `share-2`, it is immediately evident that the timing of purchase and sale was rather optimal.

????
When the Time-Weighted Rate of Return (TWR) is larger than the Internal Rate of Return (IRR), it typically means that you have successfully timed your buys and sells to take advantage of favorable market conditions. In this scenario, your investments have experienced significant growth due to buying low and selling high, which boosts the TWR. The TWR measures the performance of your investments over different time periods, and it doesn't consider the size and timing of your contributions or withdrawals. If these investments were made at opportune moments, it could lead to a TWR that appears more favorable compared to the IRR, which accounts for cash flows and their timing. This demonstrates your skill in making well-timed investment decisions, which can result in a higher TWR.
   The calculation is 

- Suppose you invest $100 in a portfolio that grows by 10% in the first year and 20% in the second year. Your TWR for the two-year period is (1.1 x 1.2) - 1 = 32%.
- However, if you withdraw $50 at the end of the first year and reinvest it at the beginning of the second year, your IRR for the two-year period is only 15%. This is because your IRR reflects the timing and size of your cash flows, while your TWR does not.
To calculate the IRR, you need to find the discount rate that makes the net present value of your cash flows equal to zero. In this case, the equation is: -100 + 50 / (1 + IRR) + 120 / (1 + IRR)^2 = 0. Solving for IRR, you get 0.15 or 15%.

You can see that the IRR is much lower than the TWR because you withdrew money when the portfolio was doing well and reinvested it when the portfolio was doing even better. This means you missed out on some of the portfolio’s growth potential.


By default, this dashboard contains three widgets (panels): `Key Indicators`, `Risk Indicators`, and `Calculation`. Right mouse click on an empty space of the canvas lets you add more widgets (see later).

# Key Indicators
## True Time-Weighted Rate of Return (cumulative)
The True Time-Weighted Rate of Return (TTWROR) is a financial metric used to evaluate the performance of your portfolio over time, eliminating the effects of cash flowing in or out of the portfolio.
## Internal Rate of Return (IRR)
The Internal Rate of Return (IRR) is a financial metric used to evaluate the potential profitability of an investment or project.
## Absolute Change
The difference between the initial investment and the current value of the investment.
## Delta (for period)
The difference between the value of the portfolio at the beginning of the period versus the end of the period.

# Risk indicators
## Maximum Drawdown
## Maximum Drawdown Duration
## Volatility
## Semivariance

# Last day
## True Time-Weighted Rate of Return (cumulative)
## Absolute Change (Absolute verandering)

# Calculation


With the icons (top right), you can
- Duplicate, Rename or Delete a Dashboard view
- Create a New Dashboard view
- Set the period (1 year, 2 years, ...)
- Create a New Column (gear icon)

