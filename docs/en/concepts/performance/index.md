---
title: Performance
---
The measurement of the performance of a financial portfolio is based on the concept of return: the increase or decrease of value over a specific period. For example, your portfolio starts at 100 EUR and grows to 120 EUR by the end of the period, resulting in a performance of + 20%. Equation 1 offers two versions of the base formula; also named the Rate of Return.

$$\mathrm{r = \frac{(MVE - MVB)}{MVB} \qquad \Leftrightarrow \qquad 1 + r = \frac{MVE}{MVB}\qquad (Eq  1)}$$

where MVE = the market value of the portfolio at the end of the reporting period, and MVB = the market value of the portfolio at the beginning of the period. Please note that:

- The rate of return percentage applies to the entire period (3 years, 6 months, ...) and is not an annual rate.
- There are no additional transactions within this specified period.

PP uses two different approaches to calculate the rate of return when additional transactions occur withing the reporting period: the money-weighted or time-weighted rate of return. It also distinguishes between the measuring the performance on portfolio, (individual) security, or trade level.

# The money-weighted rate of return
The money-weighted rate of return uses essentially the **Internal Rate of Return (IRR)** technique used in project management. This calculation considers both the timing (when) and the amount (how much) of the cash that moves into and out of the portfolio within the reporting period.

The money-weighted rate of return or IRR is the annual interest rate that is necessary to bring the beginning value of the investment (MVB) and all subsequent cash flows to the end value (MVE). To generate the specified cash flows within the given time period, your portfolio must grow each year by a percentage equal to the IRR.

If you find the concept of IRR challenging, please start by first reading the [money-weighted section](./money-weighted.md). The calculation method is thoroughly explained by formulas and numerous examples, ranging from a simple single-share investment to multiple transactions including dividends. The examples are based on the our demo portfolio to solidify your understanding.

# Time-weighted Rate of Return
The time-weighted rate of return is not influenced by the amount invested. Whether you invest one EUR or 100 EUR, you will achieve the same return. The reporting period is divided into several holding periods, and for each holding period, a return value is calculated and then compounded into an overall return. Each period carries equal weight; hence the name time-weighted rate of return. In the True Time-Weighted Rate Of Return methodology (TTWROR), performance is calculated using simple returns without any consideration for the total amount invested.

The TTWOR method is explained in depth in the [time-weighted section](./time-weighted.md) of this chapter.

A nice video about the calculation and difference between money-weighted and time-weighted approach is given by the following [CFA-level-1 exam video](https://www.youtube.com/watch?v=FePaJoXno_M).