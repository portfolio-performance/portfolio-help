---
title: Delivery (Inbound - Outbound)
---
A Delivery (Inbound/Outbound) transaction resembles a Buy/Sell transaction, except that there is *NO** deposit or withdrawal from a deposit account involved. In a Delivery Outbound transaction, the securities simply disappear and are no longer visible in the securities account. In contrast, with an inbound delivery, it's as if the securities are acquired by magic, without any prior cash transaction. This scenario could occur, for instance, when inheriting securities (you got the stock 'for free'). Moreover, a Delivery (Inbound) transaction becomes necessary when setting up your portfolio at a later date than the original purchases, without you being able to register all past transactions. In such cases, the securities are recorded as acquired without a deposit.

Figure: Delivery (Inbound) and Delivery (Outbound) transaction - one currency.{pp-figure}

![](images/delivery-same-currency.svg)

## One currency

Each security account is paired with a corresponding cash account, which is automatically added upon creation. Since security-account-1 is linked to a cash account denominated in EUR, EUR is suggested as the default currency in Figure 1. The currency designation in the box (EUR) can be modified; the text to the right provides a description of the currency (Euro).

When the chosen currency for the transaction matches the currency of the security (share-1), no conversion is necessary. All other fields, such as date, shares, quote, etc., remain identical to those in the [buy-sell transaction](buy-sell.md).

## Two currencies

The transaction currency can be changed by choosing another security or security account. However, it's also possible to change the transaction currency directly with a given security and/or security account. To change the currency of the transaction, you can either:

- Click the textbox next to the security account. Use the scrollbar to find another currency and double click on it.
- Select the available currency (e.g. EUR) and type over it with the new currency (e.g. ZAR).
- Click the box and select the available currency (e.g. EUR). Then type the first letter of the desired currency (e.g. Z for ZAR). This action will reveal a list of all available currencies beginning with the letter Z to choose from.

An exchange rate from the ECB will be suggested. However, it's worth noting that fees and taxes are only applicable in the currency of the security, which is different from the setup in the buy-sell transaction.

!!! Important

    As depicted in Figure 2, you have the flexibility to select any currency from the [list of available currencies](../view/general-data/currencies.md) for conversion (more than 50 options). There's no requirement for a corresponding cash account in that currency. For instance, in Figure 2, the Chinese yuan is chosen, despite the absence of a cash account in CNY. Nor will a deposit account in that currency be created. It's important to remember that with a delivery transaction, a security seems to appear or disappear "magically".

Figure: Delivery (Inbound) and Delivery (Outbound) transaction - two currencies.{pp-figure}

![](images/delivery-different-currency.svg)







