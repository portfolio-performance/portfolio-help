---
title: Performance
lastUpdate: 2023-11-02
---
The performance of a financial portfolio is often measured using the concept of return: the increase or decrease of the value of the portfolio over a specific period. Other names for this concept are Rate of Return (ROR) or Return on Investment (ROI).

$$r = \frac{(V_E - V_S)}{V_S} \qquad\mathrm{(Eq 1)}$$

where $V_E =$ the end value of the portfolio, and $V_S =$ the start value of the portfolio.

The *simple return* is calculated as the final portfolio value minus the initial portfolio value, divided by the initial portfolio value. This gives us a percentage change in the portfolio’s value over a specific period.

# Money-weighted Rate of Return

The money-weighted rate of return is essentially the Internal Rate of Return (IRR) of the cash flows associated with the portfolio. It takes into account both the timing and amount of cash flows into and out of the portfolio. The formula (see also [IRR theory](irr-theory.md)) looks like:
$$CF_{t0} = \frac{CF_{t1}}{(1 + IRR)^\frac{t_1}{365}}+\frac{CF_{t2}}{(1 + IRR)^\frac{t_2}{365}}+...+ \frac{CF_{tn}}{(1 + IRR)^\frac{t_n}{365}}$$

The formula for MWRR is derived by setting the initial investment value equal to the sum of the present values of future cash flows, each discounted at the MWRR itself, and solving for MWRR.

# Time-weighted Rate of Return
Time-weighted Rate of Return provide a popular alternative to the Money-weighted Rate of Return method in which each time period is given equal weight regardless of the amount invested.

In the *True* time-weighted methodology (TTWROR), performance is calculated for each sub-period between cash flows using simple returns.

From eq 1 it follows that
$$ 1 + r = \frac{V_E}{V_S}$$

If you consider multiple sub-periods, for example daily valuations of your portfolio, the *compounded* return could be written as (let $V_t$ equal to the value of the portfolio after the end of period *t* (e.g. day *t*).

$$\frac{V_1}{V_S}.\frac{V_2}{V_1}.\frac{V_3}{V_2} ... \frac{V_{n-1}}{V_{n-2}}.\frac{V_e}{V_{n-1}}= \frac{V_E}{V_S}= 1 + r$$

because each period will cancel itself out.

$$(1 + r_1) . (1 + r_2) . (1 + r_3) ... (1 + r_{n-1}) . (1 + r_n) = (1 + r)$$

