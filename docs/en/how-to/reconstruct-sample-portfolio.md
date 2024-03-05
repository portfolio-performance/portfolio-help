---
title: Reconstructing the sample-portfolio.xml file
---



# Portfolio transactions

- 2020-01-01: Deposit of starting capital - EUR 5,000 on account Broker-A (EUR).
- 2020-01-03: Purchase of Daimler AG. Due to a spin-off on 2021-12-10 into Mercedes-Benz and Daimler Trucks, you should search for the Mercedes share.( ISIN: DE0007100000). Portfolio Report can deliver the historical prices. Make a purchase of 20 shares at the historical price of 49.07 EUR.
- 2020-07-09: Dividend from Mercedes benz. Lookup at https://www.investing.com/dividends-calendar/ (set filter to company). Take 20% as global tax rate and 1% as fee.
- 2020-07-01: transfer 2700 EUR from Broker-A (EUR) to Broker-A (USD). The exchange rate is 0.8929 USD/EUR. The total amount of USD = 3024 USD.
- 2020-07-01: buy 1 share of Amazon at the price of 2878 USD. Include 1% fees and 2% taxes, totaling into 2962.80 USD net. Use CSV-file to import prices from before split
- 2021-12-10: record spin-off Daimler Truck Holding with distribution ratio 2-for-1. This will result in 10 shares at 28 EUR/share!!!! apparently it is 29.775 EUR/share (see how-to-recording-spin-off.). Create a dividend payment from old daimler of 14€/share.
- 2022-06-05 (weekend): make split of Amazon. see how-to-record split. Results in 10 shares at lower prices.
- 2022-10-28: Purchase of German bond (2022 - 2029); ISIN : DE0001102622; WKN: 110262. Historical quotes and quote feed at https://www.investing.com/rates-bonds/de0001102622-historical-data. Fees and taxes are arbitrary set to respectively 1% and 2% of the Gross Amount (for every transaction; except dividends).
- 2023-01-02; inheriting (delivery inbound) a 50 g [Degussa gold bar](https://shop.degussa-goldhandel.de/gold/goldbarren). Create a new empty security with USD as currency. Add Table on Webpage as Quote Feed and ariva.de as URL. because the gold price is in ounce (oz), enter 50/28.3495231.
- 2023- 01-15: sell the gold bar. Put the result in the USD-deposit account.
- 2023-01-29: buy 10 shares of (splitted) Amazon. To illustrate later-on the FIFO principle when selling 15 shares of amazon.
- 2023-07-01: add the MSCI World index to your portfolio(ticker symbol= ^990100-USD-STRD). In order to use it on a chart for bench marking, do we need to purchase a small amount of it?
- Add a watchlist for MSCI World index; eventually add the Dow Jones index.
- 2023-07-01: Add and purchase the IShares tracker ISHSIII-CORE MSCI WLD DLA (IE00B4L5Y983) which replicates the MSCI index. Buy 
- 2023-11-15: cash first coupon of German Bond (2.10%). Record it as a dividend. Place result (14.70 EUR) in EUR deposit.
- 2024-01-05: sell 10 shares of Amazon.  Place result in EUR deposit (1582.57 EUR)
- 2024-01-06: buy some bitcoins. Have no experience with. Added security BTCs and purchased 
- 2024-03-06: withdraw all USD from USD deposit for travel expenses (2286.70 USD) 




https://fsapi.gold.org/api/goldprice/v11/chart/price/usd/oz/1677768823962,1709391615090


https://fsapi.gold.org/api/goldprice/v11/chart/price/usd/oz/{TODAY:dd.MM.yyyy:-P2M},{TODAY}
https://www.ariva.de/goldpreis_gold-kurs/kurse/historische-kurse

https://www.gold.org/goldhub/data/gold-prices

https://fsapi.gold.org/api/goldprice/v11/chart/price/usd/oz/1677768823962,1709391615090

https://www.degussa-goldhandel.de/preise/preisliste/

dynamische URL

https://help.portfolio-performance.info/de/kursdaten_laden/#ticker






