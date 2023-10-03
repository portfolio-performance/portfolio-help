---
title: Managing bonds
lastUpdate: 2023-10-03
---

A bond is a financial instrument that represents a debt obligation. When an entity, such as a government or corporation, issues a bond, they are borrowing money from investors. In return, they promise to pay back the principal amount along with periodic interest payments over a specified period [[1](https://www.investopedia.com/articles/bonds/08/bond-market-basics.asp)]. Bonds are not well-supported in PP but with a few simple workarounds mentioned in the [German forum](https://forum.portfolio-performance.info/t/verbuchung-von-anleihen/1537/43), you could manage them effectively. 

# Adding the bond as a security.

Let's assume you've purchased a Volkswagen bond. You received the following banknote as shown in Figure 1.

Figure: Banknote of buying a bond.{pp-figure}

![](../../images/info-bank-note-bond-vw.svg)



Before you can add the buying transaction, you must [create the security](../adding-securities.md) in the Securities account. Searching for the ISIN in PP does not yield any results, and searching by name returns the tradable Volkswagen shares. Therefore, you'll need to create an empty instrument and manually input the information for the bond. Historical prices for bonds are not as critical, but -if necessary- they can be obtained in table format from for example the [ariva.de website ](https://www.ariva.de/XS1972547696/kurse/historische-kurse?go=1&boerse_id=1&month=&clean_bezug=1). Keep in mind that the historical prices for bonds are represented as percentages, ranging from 0 to 100.

# Recording the buy transaction

Since historical prices are represented as numbers from 0 to 100, you can use this format also for the buying price. At maturity date, the bond will value 5000 EUR with a price of 100%. In terms of `shares` and `quotes`, this means 100 shares x 100 EUR. However, you buy the security at 91.76%. The Gross Value becomes 50 x 91.76 EUR = 4588 EUR. Fees and taxes can be registered as usual.

The bond depicted in Figure 1 matures on October 1, 2027, with an annual interest rate of 2.25%, payable each year on October 1. Since you acquired the bond on October 27, there have already been 26 days of accrued interest. At a rate of 2.25%, this amounts to 5000 EUR * 2.25% * 26/365, or 8.10 EUR. You have to pay this accrued interest at the purchase date, but you will get it back on the first interest payment on October 1, 2023.

To process the accrued interest correctly, there are a few options; (see [discussion](https://forum.portfolio-performance.info/t/verbuchung-von-anleihen/1537/43) on forum for a few variants).

1. Adapt the buying price. In case of the example in Figure 1, the buying price becomes 4588 EUR + 8.01 EUR accrued interest divided by 50 or 91.92 EUR. The disadvantage is that the price evolution and the performance calculation is not correct.

Figure: Workaround with adaptation of quote price to incorporate accrued interest.

![](../../images/mnu-transaction-buy-bond-vw-1.png){pp-figure}
2. To maintain a precise record of the purchase price, you could record the accrued interest as an additional `tax` (see Figure 3). The correct amount will be withdrawn from the deposit account. The quote price is correct. The 'false' taxes could be corrected at the first interest payment with a `Tax refund` transaction.

Figure: Workaround with adding accrued interest to taxes.{pp-figure}

![](../../images/mnu-transaction-buy-bond-vw-2.png)
3. The buy transaction of the bond security is recorded without the accrued interest. To handle the accrued interest, you transfer the correct amount (8.01 EUR), from the deposit account associated with the security to a separate deposit account. During the first interest payment, the accrued interest amount then is transferred back to the original deposit account associated with the security. 

# Recording the interest payment

You can record the interest payment with a "Transaction > Interest" transaction in the menu. Unfortunately, you cannot specify the security from which the interest originated; only a deposit account. It's an aggregate account for all interest payments, and there is no way to attribute that interest payment back to the performance of that specific security.

A better, albeit somewhat unintuitive, is to record the transaction as a `Transaction > Dividend`. Dividends are associated with specific securities, ensuring that the performance calculation of the security remains accurate.

What about the first interest payment? Depending on the selected option from above:

1. The accrued interest is fully booked as a dividend (see Figure 4). The accrued interest (for the seller) on the purchase date (8.01 EUR) has already been accounted for in the recorded purchase price.

Figure: Interest payment 2.25% of 5000 EUR.

![](../../images/mnu-transaction-dividend-vw-1.png)
2. The interest payment (112.50 EUR) is reduced by the amount that was already recorded as tax on the purchase date (8.01 EUR). With a `Tansaction > Tax refund` that amount is refunded.
3. The interest payment is reduced by the amount that was transferred to a separate account. The accrued interest amount then is transferred back to the original deposit account associated with the security.



