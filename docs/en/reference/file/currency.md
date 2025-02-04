---
title: Currency
---
# File &rsaquo; Currency

Figure: Currency Picker. {class=align-right style="width:20%"}

![](images/currency-picker.png)

The base currency of the portfolio is established at the time of creation. In reports such as the `Statement of Assets`, some monetary values are preceded by a currency abbreviation (e.g., USD), while others are not. By default, only monetary values that are not expressed in the base currency are prefixed with the currency abbreviation.

!!! Note

    To display the currency code for all monetary values, navigate to the menu `Help > Preferences > Presentation` and enable the `Always display currency code for monetary values` option. The change will take effect upon the next startup of PP, and all values will be prefixed with the currency code.

To add or change a base currency, use the menu File > Currency. In Figure 1, the original base currency at the time of portfolio creation was EUR. An alternative base currency, USD, has already been added but is not yet set as the base currency (indicated by the unchecked box). To add AUD as another base currency option:

1. Click the "A - D" submenu in the Currency menu to expand the list of available currencies.
2. Locate and select "AUD" from the list.

Once added, you can set AUD as the base currency by checking the box next to it. This will change the base currency for the portfolio and may affect how monetary values are displayed in reports and other parts of the application.

In Figure 2, share-1 and bond-1 are European stocks traded in EUR, while share-2 is an American stock expressed in USD. The Statement of Assets report is generated twice: once with the base currency set to EUR (left panel) and once with the base currency set to USD (right panel). Please note that the quote price remains the same in both panels. However, the market value differs due to the different base currencies.

For example, the total market value in the left panel is 20,833.05 EUR, while in the right panel, it is 22,591.35 USD. According to the [Currency Converter](../view/general-data/currencies.md), the exchange rate on 2024-03-20 is 1.0844 EUR/USD. Using this exchange rate, you can confirm the conversion: 20,833.05 EUR x 1.0844 = 22,591.35 USD.

Figure: The Statement of Assets in two base currencies. {class=pp-figure}

![](images/currency-different-base-currencies.svg)



