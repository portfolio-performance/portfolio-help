---
title: Internal Rate of Return
lastUpdate: 2023-10-31
---

The Internal Rate of Return (IRR) measures the performance of an investment between two dates ($t_{0}$ and $t_{n}$). It is expressed as an annual interest rate that is necessary to bring the initial value of the investment at time $t_{0}$ to the final value at time $t_{n}$. In PP, the reporting period is measured in days. The classic equation to explain the meaning of IRR is:

**Eq (1)**    $CF_{t0} = \frac{CF_{t1}}{(1 + IRR)^\frac{t_1}{365}}+\frac{CF_{t2}}{(1 + IRR)^\frac{t_2}{365}}+...+ \frac{CF_{tn}}{(1 + IRR)^\frac{t_n}{365}}$

$CF_{t0}$ is the initial cashflow at time $t_0$. It is the sum of all in- and outflows at that moment in time and represents your initial investment. $CF_{t1}$, $CF_{tn}$ are the net cashflows that your initial investment will yield. PP works with daily periods instead of the traditional annual periods. Therefore, $t_1$, $t_2$, and $t_n$ should be converted to the number of days between $t_0$ and $t_n$. Of course, if the period between $t_0$ and $t_n$ is, for example, 365 days, the exponent becomes 1 as in the more traditional version of the equation. Eq (1) is derived from the calculation of the [present value](../images/info-irr-future-present-value.svg) of a future cashflow.

The IRR can be measured for a specific trade, security or the whole portfolio. Here's a simple example. Additionally, there is also a more complex [Practical step-by-step example](irr-example.md), solved in PP.

!!! Example
    On `2021-01-15`, you purchased 10 shares at 17 EUR each.
    As of today (`2023-06-15`), the price has risen to 18.5 EUR per share. During this period, you received a dividend of 1.5 EUR per share on `2021-09-10` and a second dividend of 1.7 EUR per share on `2022-09-10`.

What is the performance or IRR of this security? Let's first have the timing and cashflows correct.


Table: Cash flows at different times of investment.

| Date       | $t_n$ | $CF_n$           |
|------------|-------|------------------|
| 2021-01-15 | 0d    | 170€             |
| 2021-09-15 | 243d  | 15€              |
| 2022-09-15 | 608d  | 17€              |
| 2023-06-15 | 881d  | 185€             |

According to (1)

$$CF_{t0} = 170 = \frac{15}{(1 + IRR)^\frac{243}{365}}+\frac{17}{(1 + IRR)^\frac{608}{365}}+ \frac{185}{(1 + IRR)^\frac{881}{365}}$$

What IRR will solve this equation (1)?

In Figure 1, we reverse the scenario: What's the value of $CF_{t0}$ if the IRR is, for example, 5% or 15%?

Figure: Calculating CF0 for IRR = 5% and 15%.{class=pp-figure}

![](../images/info-irr-calculations.svg)

If IRR = 15% then the combined future cashflows are worth 159.16 EUR in `2021-01-15`. So, you need less money (than 170 EUR) to get the same financial results.  The real IRR should be somewhat lower. With 5% however, you need 194.64 EUR to get the same total cashflows in 2021. After some guesswork and interpolation, you arrive at the exact IRR of <span style="color:red">**11.61%**</span>, which will precisely bring all future cash flows to the initial investment of 170 EUR.

In the previous example, the dividends are immediately "consumed": you got yourself a nice meal from it. In another scenario, you keep the dividends in your drawer - or in PP terminology: a deposit account -  until `2023-06-15` and cash them in at the same moment you sell the share. In that case, there are only two cashflows: $CF_{t0}$ = 170 EUR and $CF_{t881}$ = 15 + 17 +185 EUR.

Equation (1) has only two terms and could be solved for IRR rather easily.

**Eq (2)**    $CF_{t0} = \frac{CF_{t1}}{(1 + IRR)^\frac{t_1}{365}} \implies  IRR = \sqrt[\frac{t_1}{365}]{\frac{CF_{t1}}{CF_{t0}}}-1$

In this case, your initial investment of 170 EUR has an IRR = $\sqrt[\frac{881}{365}]{\frac{217}{170}}-1$ = <span style="color:red">**10.64%**</span>. Why is this IRR smaller than the previous one? Because you kept the dividend until a later date, the 15 EUR in `2021-09-15` is less worth in `2023-06-15`.

PP calculates three variants of IRR.

  + **Performance IRR**: this is the IRR for the whole project and a specific reporting period; see `side bar > Reports > Performance`.

  + **Security IRR**: the IRR of a selected security for a specific reporting period; see `sidebar > Reports > Performance > Securities`.

  + **Trade IRR**: the IRR of a buy-sell cycle of a selected security. See `sidebar > Reports > Performance > Trades`

The Performance and Security IRR are calculated for a specific [reporting period](./reporting-period.md); e.g. 1 year, 2 years, 3 years, custom period. It is very important to distinguish the following cases:

  + $t_0$ occurs before the start of the reporting period $RP_{start}$.  PP can calculate the value of $CF_0$ (through historic quotes or transaction price) at $RP_{start}$. The holding period is calculated from $RP_{start}$ for each CF.

  + $t_0$ occurs after $RP_{start}$ but before $RP_{end}$. The value of $CF_0$ is known. The holding period is calculated from $RP_{start}$.

  + $t_n$ falls after $RP_{end}$. All transactions after $RP_{end}$ do not contribute to the calculation of IRR for that reporting period.
