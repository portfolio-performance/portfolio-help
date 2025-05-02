---
title: Dividend
---

A dividend is a distribution of profits by a corporation to its shareholders. When the distribution is made in cash, you should use this transaction type. For a choice or stock dividend, refer to [Handling choice dividends](../../how-to/handling-choice-dividend.md) in the how-to section.

## Registering a dividend
With the `Transaction > Dividend` menu, you can record the dividend payment in your portfolio. You can also utilize the context menu by right-clicking. If a security was selected, the `security` field will be pre-filled for your convenience.

Figure: Dividend dialog box for same and different currency payments. {class=pp-figure}

![](images/dividend.svg)

- **Security**: A dividend is linked to a security, often a share in a company. However, dividends can also be used to record the [interest payment](../../getting-started/manage-portfolio/bonds.md#recording-the-interest-payment) on a bond. Use the drop-down to select the security from which the dividend originates.
- **Cash Account**: Since the dividend is a cash payment, you need a deposit account to record it. Please note that if the currency of the security and deposit account do not match, additional fields are added to the dialog box (Figure 1; right panel).
- **Date**: there are four [dates](https://www.investopedia.com/terms/d/dividend.asp) relevant regarding dividends. Perhaps the payment date is the most obvious to use in PP.
- **Shares**: a dividend is paid per share. The number of shares is automatically filled in upon selecting a date. You can change the number manually; reselecting another date will reset the number to the actual available at that time.
- **Dividend payment per share**: This is the amount agreed upon by the company to pay for each share.  Your broker will provide you with this information. The currency is determined by the share. Many financial websites, such as [Yahoo Finance](https://finance.yahoo.com/quote/MSFT/history?filter=div) or [investing.com](https://www.investing.com/dividends-calendar/), offer historical overviews of dividend payments.
- **Gross value**: The gross value is automatically calculated as shares multiplied by the dividend payment per share. You can modify this value, but doing so will consequently alter the dividend payment per share value.
- **Exchange rate**: This field appears if the currency of the security and the deposit account don't match. The [exchange rate](../view/general-data/currencies.md) is retrieved from the ECB for the entered date. The value can be changed manually. Selecting another date will retrieve a new value from the ECB. You can also use the `Invert` button to change the conversion direction, for example, from EUR to USD or vice versa. The gross value in the foreign currency is calculated, and additional fields for fees and taxes are included.
- **Fees and taxes**: Can be entered separately; also in the foreign currency.
- **Credit note**: This is the calculated net value, which is the Gross value minus fees and taxes. Modifying this value manually will affect the Gross value, and consequently, the dividend per share as well.
- **Note**: Additional textual info about this dividend payment.

## Effect on performance

The directly visible effect of a dividend registration is the increase in balance of the designated deposit account.  Take the following very simple project. Ten pieces of share-1 are purchased on January 1th, 2024 for 10 EUR/share. The reporting period runs to April 1, 2024 at which time share-1 quote has increased to 11 EUR/share.

The balance of the deposit account is zero EUR. The portfolio TTWROR = 10% and IRR = 46.56%. An in-depth explanation of the performance calculation in Portfolio Performance is given in [Concepts > Performance](../../concepts/performance/index.md).

- TTWROR: one holding period; MVB=0; MVE= 110; CF= 100. r = (110/(0+100))-1 = 10%
- IRR: because MVB = 0 and buy transaction was at the very beginning of the reporting period (remaining days = 91)
110 = 100 x (1+0.4656)^(91/365) or IRR = 46.56%. 

A dividend is paid on March 1, 2024 at 5 EUR/share. The fees and taxes were each 1 EUR. There are 31 days remaining in the reporting period. At that moment, the balance of the deposit account is increased with (10 x 0.5) - 1 - 1 = 3 EUR. Performance starts to differ between portfolio, security or (open) trade level.

- Portfolio level: as far as the portfolio concerned, there is only 1 cashflow (initial buy). The dividend is paid to the deposit account and stays within the portfolio. The deposit account, and therefore also the MVE is increased up with 3 EUR. 
    - TTWROR: one holding period; MVB=0; MVE= 113; CF= 100. r = (113/(0+100))-1 = 13%
    - IRR: = 100 x (1 + 0.6327)^(91/365)
- Security level: at this level, there are two cashflows: buy (100 EUR inflow) and dividend (3 EUR outflow).
    - TTWROR: r1 = (110/(0+100))-1 = 10%; r2 = (113/(100-3))-1

there are two cashflows: CF1 = 100 EUR at 2024-01-01 and CF2 = 3 EUR at 2024-03-01. 

<table>
  <tr style="background-color:darkgrey;">
    <th rowspan="1"></th>
    <th colspan="2" style="text-align:center;">Portfolio</th>
    <th colspan="2" style="text-align:center;">Security</th>
    <th style="text-align:center;">Trade</th>
  </tr>
  <tr>
    <th></th>
    <th style="text-align:center;">TTWROR</th>
    <th style="text-align:center;">IRR</th>
    <th style="text-align:center;">TTWROR</th>
    <th style="text-align:center;">IRR</th>
    <th style="text-align:center;">IRR</th>
  </tr>
  <tr>
    <td style="text-align:left;">Without dividend</td>
    <td style="text-align:center;">10%</td>
    <td style="text-align:center;">46.56%</td>
    <td style="text-align:center;">10%</td>
    <td style="text-align:center;">46.56%</td>
    <td style="text-align:center;">46.56%</td>
  </tr>
  <tr>
    <td style="text-align:left;">Dividend with fees & taxes (1 + 1 EUR)</td>
    <td style="text-align:center;">13%</td>
    <td style="text-align:center;">63.27%</td>
    <td style="text-align:center;">14%</td>
    <td style="text-align:center;">69.14%</td>
    <td style="text-align:center;">46.56%</td>
  </tr>
  <tr>
    <td style="text-align:left;">Dividend with fees (1 EUR)</td>
    <td style="text-align:center;">14%</td>
    <td style="text-align:center;">69.14%</td>
    <td style="text-align:center;">14%</td>
    <td style="text-align:center;">69.14%</td>
    <td style="text-align:center;">46.56%</td>
  </tr>
  <tr>
    <td style="text-align:left;">Dividend with taxes (1 EUR)</td>
    <td style="text-align:center;">14%</td>
    <td style="text-align:center;">69.14%</td>
    <td style="text-align:center;">15%</td>
    <td style="text-align:center;">75.17%</td>
    <td style="text-align:center;">46.56%</td>
  </tr>
</table>






