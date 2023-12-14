---
title: Performance
---
# Performance Measurement
The measurement of the performance of a financial portfolio is based on the concept of return: the increase or decrease of value over a specific period. For example, your portfolio starts at 100 EUR and grows to 120 EUR by the end of the period, resulting in a performance of + 20%. Equation 1 offers two versions of the base formula; also named the Simple Rate of Return (ROR).

$$\mathrm{r = \frac{(MVE - MVB)}{MVB} \quad \Leftrightarrow \quad 1 + r = \frac{MVE}{MVB} \quad \Leftrightarrow \quad MVE = MVB \times (1 + r) \quad (Eq  1)}$$

where MVE = the market value of the portfolio at the end of the reporting period, and MVB = the market value of the portfolio at the beginning of the period. Please note that:

- The rate of return percentage applies to the entire period (3 years, 6 months, ...) and is not an annual rate.
- There are no additional transactions within this specified period.

To address these concerns, PP employs two distinct approaches to calculate the rate of return when additional transactions occur within the reporting period: the money-weighted or time-weighted rate of return. It also differentiates between measuring performance on the portfolio, security, or trade level.

!!! Note
    The simple Rate of Return (ROR) isn't adequate for describing the performance of a portfolio when transactions occur in the reporting period. For instance, suppose your portfolio already contains one share valued at 100 EUR at the beginning of the year (MVB=100); an empty portfolio would pose even more problems due to dividing by zero in Equation 1. Thanks to the favorable  track record of the company issuing the share, its price increases to 104 EUR per share at the end of the year. Let's now compare the following scenarios:
    
    -  **No additional transactions**: you do nothing. According to Equation 1, r = (104-100)/100 = 4%. This seems intuitive correct. You gained 4 EUR, which is 4% of the initial value.
    - **Additional transactions**: you acquire  a second share at 100 EUR; right at the beginning of the year. MVB is still 100 EUR; while MVE becomes 2 * 104 = 208 EUR. The performance becomes a staggering 108% or (208-100)/100. This does not feel OK. You know that the growth rate of the company's share is 4%. Certainly, your total investment of 200€ has gained 8 EUR or 4% on 200 EUR; but not on the MVB of 100 EUR. The additional transaction has distorted the simple rate of return formula.

## The money-weighted rate of return
The money-weighted rate of return (MWR) employs the **Internal Rate of Return (IRR)** technique commonly used in project management. This calculation takes into account both the timing (when) and the amount (how much) of cash that flows into or out of the portfolio within the reporting period.

The money-weighted rate of return or IRR is the annual interest rate that is necessary to bring the beginning market value of the investment (MVB) and all subsequent cash flows to the end value (MVE). Your portfolio must grow each year by a percentage equal to the IRR to generate the specified cash flows within the given time period.

If you find the concept of IRR challenging, please start by first reading the [money-weighted section](./money-weighted.md). The calculation method is thoroughly explained by formulas and numerous examples, ranging from a simple single-share investment to multiple transactions including dividends. The examples are based on the our demo portfolio to solidify your understanding.

## Time-weighted Rate of Return
The time-weighted rate of return (TWR) is not influenced by the amount invested. Whether you invest one EUR or 100 EUR, you will achieve the same TWR. The reporting period is divided into several holding periods, and for each holding period, a return value is calculated and then compounded into an overall return. Each period carries equal weight; hence the name time-weighted rate of return. In the True Time-Weighted Rate Of Return methodology (TTWROR), performance is calculated using simple returns without any consideration for the total amount invested.

The TTWOR method is explained in depth in the [time-weighted section](./time-weighted.md) of this chapter.

A nice video about the calculation and difference between the money-weighted and time-weighted approach is given at the [Finance and Risk Corner](https://www.youtube.com/watch?v=moNiiau33u0).