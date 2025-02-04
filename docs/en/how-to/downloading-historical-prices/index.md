---
title: Downloading Historical Stock Prices
---

Figure: Data sources Historical Quotes.{class=align-right style="width:40%"}

![](../../reference/file/images/quote-feeds.png)

Finding accurate and up-to-date but free data sources for historical prices can be challenging. The list of data sources in PP includes the following options (see Figure 1): [Alpha Vantage](alpha-vantage.md), [EOD Historical Data](eodhd.md), Finnhub, Leeway, Twelve Data, [Portfolio Report](portfolioreport.md), Quandl, and [Yahoo Finance](yahoo-finance.md). The remaining alternatives are tailored for bitcoins and other statistical data.

Unfortunately, the terms of use for many of these options have become increasingly restrictive over time. They are included here mainly for compatibility reasons. In practical terms, only [Portfolio Report](portfolioreport.md) and [Yahoo Finance](yahoo-finance.md) or JSON could be recommended for a typical portfolio.

Some specific use cases are discussed below. Many more are described in the [Forum](https://forum.portfolio-performance.info/t/quellen-fur-historische-kurse/46) (in German).

## Very old historical prices

Most financial services typically provide historical prices for a limited time period, such as the last year or since a specific recent date. However, if you happen to be one of the fortunate individuals who purchased Apple stock back in the 1980s, tracking your performance from the very beginning should be nice.


!!! note

    Apple went first public on December 12, 1980, opening at `$`22 a share. The company was listed on the NASDAQ stock exchange under the ticker symbol AAPL. The share has since split five times, most recently in 2020, so on a split-adjusted basis the IPO share price was $.10.

1. Choosing [Yahoo Finance](./yahoo-finance.md) as the Quote Feed provider will not get you very far: only 3 months of historical quotes are downloaded, starting from today.

2. Choosing the [JSON Quote Provider](./json.md) allows you to specify the desired period for prices. For instance, the following URL attempts to download 30 years of data:

    `https://query1.finance.yahoo.com/v8/finance/chart/NVDA?interval=1d&range=30y`

    It's not possible to obtain 30 years, but you do receive data until 1991, or about 25 years of historical prices.

3. Normally, company websites contain that kind of information. Surprisingly, The Apple website doesn't offer the option to download historical data; you only can look up some prices. On the other hand, you can access [dividend and split](https://investor.apple.com/dividend-history/default.aspx) information. [NASDAQ](https://www.nasdaq.com/market-activity/stocks/aapl/historical) allows you to download a CSV file that extends only 10 years into the past.

4. Naturally, being a high-profile stock, more extensive data can be found on the web. For instance, [Kaggle](https://www.kaggle.com/datasets/meetnagadia/apple-stock-price-from-19802021) provides a CSV file of Apple Stock Prices from 1980-2021. You could download this file, import it into the historical prices, and have Yahoo Finance append the missing data.

## Mutual funds

Suppose that you want to track the `Sustainable Health Care Fund` (ISIN: lu0114720955) of the European based [Fidelity Funds](https://www.fidelity.lu/funds/factsheet/LU0114720955). [Yahoo Finance](https://finance.yahoo.com/quote/FJ2U.F/history?p=FJ2U.F) has only the most recent price.

[Investing.com](https://www.investing.com/funds/lu0114720955) does a bit of a better job and provides historical data from the launch of the fund (2000-09-01). You can download these data as CSV file; see section on [Downloading historical prices > CSV File](./csv-file.md).

Of course the most extensive website for mutual funds is Morningstar
You need to visit a European website for example https://www.morningstar.co.uk/uk/funds/snapshot/snapshot.aspx?id=F0GBR04EBS&tab=13


## ETF tracker

## Bonds

## Gold

