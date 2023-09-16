---
title: Reinvesting dividends
lastUpdate: 2023-09-16
---

How do you book the reinvestment of a dividend? What about DRIP? A dividend is the payment of a part of the company's profit to its shareholders. Sometimes you can choose to receive this dividend in cash or in shares. But how should you register this latter share dividend.

For example, at the annual general meeting of the NN Group, the shareholders approved a final dividend of EUR 1.56. The final dividend will be paid either fully in cash, after deduction of withholding tax if applicable, or fully in ordinary shares, at the election of the shareholders. The following example is about the choice dividend (300 shares) of a Dutch company, paid to a non-resident investor. The dividend is 1.56 EUR/share. The converting ratio is 1 new share for 29.43 old shares. The historical quote at the pay date is 45.91 EUR.

- you choose for *cash dividend*. You receive the net amount of 278.46 EUR.
300 shares * 1.56 EUR = 468 EUR minus foreign taxes (15% or 70.2 EUR), minus fees (0 EUR), minus domestic taxes (30% or 119.34 EUR).

- You choose for *share dividend*. You receive 10 shares at 45.91 and 5 cash dividends (6.63 EUR). You have to pay some fees (3.50 EUR) and domestic taxes (140.09 EUR).

Theoretically, there is no difference between the two choices. 300 shares/29.43 * 45.91 ~= 300 shares * 1.56 EUR.

In this example, the broker doesn't allow share fractions. So, you only receive 10 additional new shares (not 10.19 shares) for 295 old shares and a pay-out of the remaining 5 old shares dividend.

The domestic taxes are much larger for the share dividend (30%) than if you should buy the shares from your cash account(0.35%) (140.09 EUR). Of course, if the dividends are paid in cash, then you would also have paid domestic taxes. Either way, the government receives the same amount.

In this particular example, there is a small benefit because there are no foreign taxes (15%) in case of a share dividend.

There has been a lot of [debate](https://forum.portfolio-performance.info/t/dividend-paid-in-security-stock-dividend-reinvestment-plan-drip/13828/16) about how to book these transactions in PP. My understanding of the proposed procedure is:

  - book the dividends for all shares *without* fees and taxes. These will be paid for in the following step. If your broker doesn't allow for share fractions, you can use one transaction for the share dividend part (e.g. 295 in the example) without fees & taxes and another transaction with taxes and fees for the cash dividend. 
  - buy the allocated shares at the same day with the theoretical historical quote and the associated fees and taxes.

![Implementation in PP](images/reinvesting-dividends-pp-implementation.png){pp-figure}

Please note that in this example the total outflow is much larger the inflow from the dividend payment. This is because the number of reinvested shares is calculated on the gross amount. So, all taxes and fees are in surplus of this choice dividend.
