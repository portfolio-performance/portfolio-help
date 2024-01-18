---
title: Portfolio Performance terminology
todo: target currency
---

Fundamental concepts such as account, transaction, reporting period, purchase value, and performance are described in a separate chapter (see sidebar). Below is an alphabetical list containing descriptions of all attributes, also referred to as fields or columns, used in various sections within PP.

- Actual # quotes: the number of quotes in the historic prices list of a security.

- Change in Price (period): the difference in historic quotes between the last and first quote of a specified time span, expressed as a percentage. The period may be denoted in years (e.g., 1 year, 2 years, 3 years) or as a date range (From yyyy-mm-dd to yyyy-mm-dd). If the duration is in years, the last date is today, and the first date is today minus x years.

- Change on Previous Day (amount) or Δ amount: the absolute difference between the latest retrieved quote and the previous one (which is most likely the quote from the previous day).

- Change on Previous Day (%) or Δ %: the difference between the latest retrieved quote and the previous one (which is most likely the quote from the previous day), expressed as a percentage.

- Completeness of historic quotes: the ratio between the actual and expected number of historic quotes of a security, expressed as a percentage.

- Currency: the currency for a security chosen at its creation, which becomes immutable after the initial transaction involving this security.

- Date of first historical quote: The first date for which you have historical prices of a security.

- Date of last historical quote: The last date for which you have historical prices of the security. It's important to note that having these dates does not necessarily mean you have all intermediate historical prices.

- Date of latest quote: the most recent date on which the current market value or price of a financial instrument, such as a stock, bond, or commodity, was publicly provided or updated.

- Distance to SMA (days): a metric that measures the difference between the current price (quote) of a share and the average price of that share over a specified number of past days (5, 20, 30, 38, 50, 90, 100, or 200 days), expressed as a percentage. The acronym "SMA" stands for "Simple Moving Average". For example, the average price of security for the last 5 daily quotes is (100 + 98 + 99 + 97 + 96)/5 = 98. The Distance to SMA (5 days) is (100-98)/98 = 2.04%.  

- Distance to ATH (period): a metric that shows how far the current price is from the highest price in the specified period (1 year, 2 years, 3 years or a date range From yyyy-mm-dd to yyyy-mm-dd). For example, the highest price of a security in the last year was 77.4 EUR. The current price is 71.96 EUR. So the Distance to ATH for a 1 year period is equal to (71.96 - 77.4)/77.4 or -7.03%.

- Exchange: a security may be traded on more than one exchange. For example, the NVIDIA stock is traded on Nasdaq (symbol NVDA, exchange NMS) or XETRA (symbol NVD.DE, exchange GER), and many more exchanges.

- Expected # quotes: given the nature and frequency of a security and the calendar in use, PP calculates the expected number of quotes for the time period between the Date of last and first historical quote. Weekend and holidays are taken into account.

- Inactive: A security can be set to active or inactive. If set to inactive, the security will not appear in buy or sell dialogs, and historical prices will not be updated automatically.

- ISIN: *International Securities Identification Number*. This is a unique twelve-digit code that is assigned to every security in the world. Mostly used by European brokers & banks.

- Latest Quote: the most recent quote of a security. You can refresh these values to the latest information using the menu option `Online > Update Quotes`.

- Name: the full name of the security according to the data source (see below) from which it is retrieved, e.g. Yahoo Finance.

- Net Transaction value: the total sum of costs of a transaction, including the taxes and fees.

- Purchase Value: the summed transaction value of each buy (+) and sell (-) transaction of a security, taken into account the [reporting period](reporting-period.md).

- Quote Feed (historic): data source or provider of the historic quotes: Alpha Vantage, Bitfinex Cryptocurrency Exchange, Binance Crypto Exchange, CoinGecko, EOD Historical Data, Finnhub, Inflation rate - Eurostat (HICP), ECB Statistical Data Warehouse, Kraken Cryptocurrency Exchange, PWP Leeway UG, Twelve Data, Quandl, Table on website, VIA/CS Funds, Yahoo Finance, Yahoo Finance (Adjusted Close), JSON, no automatic download.

- Quote Feed (latest): data source or provider of the latest quotes (same list as above) or could be set as "same as historical quotes".

- URL (historic quotes): the URL that should be provided, if the choice in Quote Feed is set to Table on website or JSON.

- URL (latest quotes): see above but for the latest quote provider.

- Source: data source used in `File > New Security` Search. Possible source are: [Yahoo Finance](https://finance.yahoo.com/) provides financial news and data including stock quotes, press releases, and financial reports. [CoinGecko](https://www.coingecko.com/) is a website with real-time information on most cryptocurrencies. [Portfolio Report](https://www.portfolio-report.net/search) is an open source project that aims to provide centralized portfolio performance data.

- Symbol: the abbreviation (ticker) used by the data source.

- Target Currency: 

- Type: can be Share, Bond, Cryptocurrency, Aktie (German for stock or share), Währung (=German for currency), Futures, etf, fonds (= funds).

- WKN: *Wertpapierkennnummer*. A German six-digit alphanumeric code for the identification of a security, now replaced by the ISIN code.

 

