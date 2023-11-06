---
title: Performance
lastUpdate: 2023-11-02
---
The measurement of the performance of a financial portfolio is based on the concept of return: the increase or decrease of the value of the portfolio over a specific period. A *simple* rate of return can be calculated as $r = \frac{(V_E - V_S)}{V_S}$ or the equivalent form $r = \frac{V_E}{V_S} - 1$ (Eq 1).

where $V_E =$ the end value of the portfolio, and $V_S =$ the start value of the portfolio.

For example, if you purchased a security for 100 EUR and can now sell it for 107 EUR, your simple rate of return is (107-100)/100 = 7%. This seems straightforward, but what does it truly signify? Did you acquire this security just one month ago, or was it a decade ago? To provide a more meaningful perspective, it's better to calculate an annualized rate of return.

Moreover, your approach to calculating returns should also accommodate scenarios involving multiple securities with cash inflows and outflows. To handle such situations effectively, you can choose between a *money-weighted* or *time-weighted* approach.

# Money-weighted Rate of Return

The money-weighted rate of return is essentially the Internal Rate of Return (IRR) of the cash flows associated with the portfolio. This calculation considers both the timing (when) and the amount (how much) of the cash moves into and out of the portfolio. The money-weighted rate of return or IRR is the annual interest rate that is necessary to bring the start value of the investment to the end value. To generate the specified cash flows within the given time period, your portfolio must grow each year by a percentage equal to the IRR.

The base formula to calculate the IRR (see also [IRR theory](irr-theory.md)) looks like:
$$CF_{t0} = \frac{CF_{t1}}{(1 + IRR)^\frac{t_1}{365}}+\frac{CF_{t2}}{(1 + IRR)^\frac{t_2}{365}}+...+ \frac{CF_{tn}}{(1 + IRR)^\frac{t_n}{365}} \qquad\mathrm{(Eq 2)}$$

For each cash flow CF at time $t_1$, $t_2$, ..., $t_n$, you calculate its present value by dividing it by ${(1 + IRR)^\frac{t_1}{365}}$, where t is the number of days from the reference time t0. This part discounts the future cash flows to their present values, considering the time value of money. Choosing an appropriate IRR will ensure that the sum of all discounted cash flows equals the initial investment or $CF_{t0}$.

It's easy to see from Eq 2 that the value of IRR is influenced by the magnitude of the cash flow. If the cash flow CF increases, the IRR must also become larger to balance the equation. If the exponent $\frac{t_2}{365}$ increases, the value of IRR should decrease. Therefore, IRR is a money-weighted rate of return.

In [IRR - Practical example](./irr-example.md), you will find a detailed and comprehensive explanation of the IRR calculation for our demonstration portfolio.

# Time-weighted Rate of Return
The time-weighted rate of return is not influenced by the amount invested. Whether you invest 1 EUR or 100 EUR, you will achieve the same return. The reporting period is divided into several holding periods, and for each holding period, a return value is calculated and then compounded into an overall return. Each period carries equal weight. In the True time-weighted methodology (TTWROR), performance is calculated using simple returns without any consideration for the total amount invested.

PP computes the TTWOR as follows. For each day within the reporting period, it collects the total portfolio value, inbound transfers, and outbound transfers. The portfolio value encompasses all deposit and securities accounts. To determine the value of a security, it multiplies the quantity by the (historical) price. Transfers encompass external cash flows, which can either enter the portfolio from outside (inbound) or exit it (outbound); assuming that fresh money is added at the beginning of the day (and hence is available to generate return) and removed at the end of the day. A dividend or sale transaction is not considered as a transfer; they remain within the portfolio. They are recorded in the cash account, thereby contributing to the increased valuation of the portfolio. A modified version of the simple return formula (see eq 1), including the transfers, is used to calculate the daily return value (named delta).

The total *compounded* return can be calculated as follows:
$$r = [(1 + r_1) * (1 + r_2) * (1 + r_3) ... (1 + r_{n-1}) * (1 + r_n)] - 1$$

This formula follows directly from Eq 1, which can be rewritten as:

$$\frac{V_1}{V_S} * \frac{V_2}{V_1} * \frac{V_3}{V_2} ... \frac{V_{n-1}}{V_{n-2}} * \frac{V_E}{V_{n-1}}= \frac{V_E}{V_S}= 1 + r$$

$V_t$ is the value of the portfolio after the end of period *t* and each sub-period effectively cancels itself out.
