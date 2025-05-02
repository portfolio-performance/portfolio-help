---
title: Handling choice dividends
---
# Handling choice dividends

A dividend is the payment of a part of the company's profit to its shareholders. With a choice dividend, shareholders are given the option to choose between receiving cash payment (cash dividend) or additional shares of stock (stock dividend).

## Example NN Group

For example, the Dutch financial services company, [NN Group](https://www.nn-group.com/investors/share-information/dividend-policy-and-dividend-history.htm) provided its shareholders with the option to receive the interim dividend for 2023 of 1.12 EUR per share, either in cash or in shares. The [ex-dividend date](../concepts/PP-terminology.md) was set on August 31, 2023, with the dividend payment scheduled for September 25, 2023. The reference share price was determined at 36.2513 EUR by taking the average of five daily historical prices between 12 and 18 September 2023 on Euronext Amsterdam between 12 and 18 September 2023.

With this reference price the distribution ratio was established at 1-for-32.37 shares. Indeed, to receive one share of 36.2513 EUR, you need 32.37 shares x 1.12 EUR dividend.

Theoretically, the cash and stock dividend options should lead to the same gross result. Otherwise, shareholders would naturally gravitate towards the more advantageous choice. Let's consider a scenario where you hold 100 shares of the NN group at the ex-date. Opting for the cash dividend would yield 100 shares x 1.12 = 112 EUR gross. On the other hand, choosing the stock dividend would grant you approximately 3.09 shares (100 shares / 32.37), valued at 36.2513 EUR per share. This totals around 112.02 EUR gross, which is approximately equivalent to the cash dividend amount. Please note that fractional shares are not always possible; although Portfolio Performance can easily work with them. So a solution for the .09 shares may need to be found.

Of course, your choice will be influenced by your need for immediate liquidity (prompting for cash dividend) and your desire to further invest in this company (stock dividend).

Although theoretically equivalent in terms of the gross value, factors such as fees, taxes, and various fiscal and broker regulations will impact the final net amount of cash retained. In practice the choices do differ. For example, a Belgian (thus, foreign) shareholder with 100 shares will receive 68.12 EUR of cash dividend, while the stock dividend is valued at 72.93 EUR; approximately 7% more. This difference is primarily caused by the elimination of foreign taxes in the case of stock dividend.

!!! Note

    1. If you opt for *cash dividend*. You receive a Gross Amount of 100 x 1.12 = 112 EUR. The net value depends on the fiscal and broker regulations of your country. For example, as a *Belgian shareholder*, you pay 10% foreign taxes (=11.2 EUR), 30.24 EUR or 30% domestic taxes on the remaining value (112 - 11.2 = 100.8), 2.44 EUR or 2% broker fees + TVA 21%. The remaining net value is 100.8 - 30.24 - 2.44 = 68.12 EUR.

    2. You choose for *stock dividend*. The calculation becomes much more complex. Your broker need to solve the fractional share and you have to decide about the valuation of the newly acquired shares.

        - You are entitled to 100/32.37 = 3.0893 shares. So, you will receive three new shares and your broker will convert the fraction (.0893) to a cash dividend. In this case, the closest approximation is two shares; 32.37 x 0.0893 = 2.89 or rounded down (!) two shares.
        - The cash dividend follows the same rules as above. In this case, the Belgian broker does not charge a fee. The net cash dividend is thus 2 x 1.12 minus 10% foreign taxes and 30% domestic taxes = 1.41 EUR.
        - From the point of view of the (Belgian) government, the acquirement of 3 shares is the result of the dividend payment of the NN group. The total of all taxes is 
            - 30% of domestic taxes are withheld = 32.63 EUR
            - no foreign taxes because of the double-treaty between Belgium and The Netherlands
            - Stock exchange tax of 0.35% or 1.78 EUR.
            - TVA of 21% on the broker's fee: 0.74 EUR.
        - From the broker's point of view, you buy 3 shares. The total fees amount is apparently a fixed 3.5 EUR.
        - Rests the difficult question of valuation of the three newly acquired bonus shares. How much are they worth at dividend payment date? 
            - You could take the historical close price of the NN share on payment day: 3 x 36.33 EUR/share or 108.99 EUR.
            - You could also take the reference price which will lead to the total amount of 3 x 36.25 = 108.7632.
            -  Because the close price on the payment day isn't very different from the reference price (36.33 vs 36.25), both valuations will be practically the same here.
        - So, how much did you really receive from this stock dividend?
            - net dividend of the remaining shares: 1.41 EUR.
            - net price of the three newly acquired shares: 108.73 - 33.74 (taxes) - 3.5 (fees) = 71.52 EUR.
            - Total net value: 72.93 EUR.

Certainly, the calculation above applies only for a Belgian shareholder with a particular broker in 2024. The advantage of the stock dividend is primarily due to the foreign tax situation, which may differ significantly for shareholders in other countries, particularly Dutch shareholders.

!!! Important
    Note that in the case of cash dividend, you will receive money, while with the stock dividend, you have to invest additional money. Although you receive the shares, you also have to cover the associated taxes and fees.

## Recording the choice dividend in PP

There has been a lot of [debate](https://forum.portfolio-performance.info/t/dividend-paid-in-security-stock-dividend-reinvestment-plan-drip/13828/16) about how to book these transactions in PP. Many users suggest considering the choice of dividend as a sequence of receiving the dividend and purchasing the shares. A possible workflow is the following.

  - Book the gross dividend of all shares *without* fees and taxes. These will be paid for in the following step. This transaction has not been taken place in reality; so you have no note of this of your broker. Your designated deposit account will be increased by the gross amount of the dividend; e.g. 112 EUR in the previous example.
  - Purchase the allocated bonus shares at the same day with the reference price and the associated fees and taxes, you receive from your broker.
  - If you want to account for the minimal impact of the fraction shares (e.g. the dividend of 2 shares in the above example), you need to split the first dividend transaction in two.
    -  Book the dividend with fees and taxes of the fraction shares (e.g. 2). You should have a note from your broker of this.
    - Book the dividend of the other shares (e.g. 98) without fees and taxes (you do not have a note from your broker).

![Implementation in PP](images/reinvesting-dividends-pp-implementation.png){pp-figure}


