---
title: Reconstructing the sample-portfolio.xml file
---
In order to reconstruct the sample-portfolio.xml file, you first need to create a new portfolio with the menu `File > New > File` (see [Getting Started](../getting-started/create-portfolio.md)). Choose your base currency. Set it to EUR if you want to follow the sample portfolio. Add a security account (e.g. `Stocks`) and a reference deposit account (e.g. `EUR-account`). Finish the wizard. Add more security and deposit accounts.

The sample portfolio contains the following security accounts: `Stocks`, `Bonds`, `Funds`, `Crypto`, and `Gold`. They all have the same `EUR-account` as reference.

The sample portfolio contains the following deposit accounts: `EUR-account`, `USD-account`, `GBP-account`, `JPY-acount`, `ZAR-account`... [*The choice of multiple currency accounts should emphasis the international character/open mindedness of the software*]

In the `All Securities` view, add your securities. The sample portfolio contains the following securities.

**Gold & other precious metals**

    - Gold: [see how-to > Retrieving gold and other precious metals prices](./gold-prices.md) to create a security that can hold Degussa 30 oz gold bars.
    - other metal: ??

**Bonds**
    - Government: e.g. Germany 10Y YTM (Bund)Germany 10 Year bond
    - Corporate bond: e.g. Rolls-Royce, 5.75% 15oct2027, GBP (XS2244321787)
    - do we place here also "iShares Core Euro Government Bond UCITS ETF (Dist)" or does it belong with "funds"?

**Crypto**
    - see existing kommer.xml : Bitcoin BTC
    - other: ?

**Funds**
    - some ETF from kommer.xml (but there are too many?): I should keep: iShares Core Euro Government Bond UCITS ETF (Dist) (see above) and iShares MSCI EM UCITS ETF (Dist) (because our stock from EM is probably limited)
    - I should add: iShares Core S&P 500 ETF (to illustrate the S&P 500 index) or an ETF that replicates the MSCI world or all countries. 

**Stock**
    
    - [Stock should be spread over countries and sectors from GICS]. For example:

    1. Energy: Royal Dutch Shell (Netherlands/GB)
    2. Materials: Rio Tinto (GB/Australia) [also choice dividend]
    3. Industrials: Bombardier Inc (Canada)
    4. Consumer Discretionary: Daimler AG (Germany) [also spin-off Mercedes ...] & Amazon (USA) [also split]
    5. Consumer Staples: The Procter & Gamble Company (United States)
    6. Health Care: Novartis AG (Switzerland)
    7. Financials: HSBC Holdings plc (United Kingdom)
    8. Information Technology: Sony (Japan)
    9. Telecommunication Services: Deutsche telekom (Germany)
    10. Utilities: Engie SA (France)
    11. Real Estate: Mariott International (United States)

For each security, info should be provide such as ticker, taxonomy, historical prices download instructions.

## Portfolio transactions

For each of the above securities, at least one buy or inbound delivery transaction should be made.  Other transactions (sell, dividend, ...) should also be present.

*Work in Progress*
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









