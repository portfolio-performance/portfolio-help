---
title: Download Historical Prices
---

  As you can see in Figure 4, the website [https://finance.yahoo.com/](https://finance.yahoo.com/) is selected. Searching this website for the historical prices of a stock named "Deutsche Telekom" (which is in reality `share-1`) will produce the following URL: [https://finance.yahoo.com/quote/DTE.DE/history?p=DTE.DE](https://finance.yahoo.com/quote/DTE.DE/history?p=DTE.DE). However, if you should consult this webpage, you will notice that the historical prices are by default only given for one year. Additional actions are required to set the time period. All of this is handled by PP.
    
     

    The Quote Feed Provider and Exchange input boxes will provide PP with exactly this information.

    Some of these Quote Feeds such as Alpha Vantage and EOD Historical Data need an API key.  Most of them are free but with some limitations. You need to register for this key on the website of the provider. The API keys then are stored in PP. You can set them with the menu `Help > Preferences > API keys`.