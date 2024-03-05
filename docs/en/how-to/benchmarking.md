---
title: Benchmarking your portfolio
---
Benchmarking your portfolio performance against financial indexes, such as the MSCI World Index, is a common practice in investment management. This process involves comparing the returns of your portfolio to the returns of a selected benchmark index. It also allows you to evaluate the performance of individual securities within your portfolio, helping you determine whether they are contributing positively to your overall returns or underperforming compared to the broader market.

A financial index is a hypothetical portfolio of investment holdings that represents a segment of the financial market. For example, the [MSCI World](https://www.msci.com/documents/10199/178e6643-6ae6-47b9-82be-e1fc565ededb), maintained by MSCI, formerly Morgan Stanley Capital International, is a widely followed global stock market index that tracks the performance of around 1500 large and mid-cap companies across 23 developed countries. The top three stock constituents are Apple, Microsoft Corp, and Nvidia (together about 10% of the hypothetical portfolio).

A list of all major indexes can be found at [investing.com](https://www.investing.com/indices/major-indices). Some major American indexes are [S&P 500](https://www.spglobal.com/spdji/en/indices/equity/sp-500/), [Dow Jones Industrial Average (DJIA)](https://www.spglobal.com/spdji/en/indices/equity/dow-jones-industrial-average/#overview), and the [Nasdaq Composite](https://www.nasdaq.com/market-activity/indexes/ixic). Some major European indexes are [Euro Stoxx 50](https://www.stoxx.com/index-details?symbol=SX5E), [Financial Times Stock Exchange 100](https://www.ftse.com/products/indices/UK), and the [Deutscher Aktienindex (DAX)](https://www.dax-index.de/en/). Most indexes have several variants and/or expressed in multiple currencies.

!!! Note Index variants

    An index variant refers to the specific way an index is calculated. Here are some common types of index variants (see [MSCI](https://www.msci.com/search?keywords=msci+world) for an example):

    1. **Price Return**: This variant only considers the price changes of the index's constituents. It does not take into account dividends or distributions.

    2. **Gross Return**: This variant includes both the price changes and the full dividends or distributions paid by the index's constituents. It assumes that all dividends or distributions are reinvested back into the index.

    3. **Net Return**: This variant is similar to the Total Return variant, but it takes into account the effect of dividend taxes (withholding taxes). It assumes that dividends or distributions, after tax deductions, are reinvested back into the index.

    4. **Total Return**: A total return index is similar to a gross return index in that it considers both the changes in the prices of the constituent securities and the reinvestment of dividends. However, a total return index may also account for other corporate actions, such as stock splits, rights issues, and spin-offs. This variant provides the most comprehensive view of an index's performance, taking into account all possible factors that could impact returns.

## Adding an index to your portfolio

You can either download the historical prices of the index and assign it to a new (empty) security or you can add an ETF that replicates the index.

1. Download the historical prices from investing.com. For example, the [MSCI World Net EUR Historical Data](https://www.investing.com/indices/msci-world-net-eur-historical-data). Select the correct time period and click the download button to receive a CSV-file (you need a free registration for that). Create a new empty instrument. See the section [File > Import](../reference/file/import.md#csv-files-comma-separated-values) and [How-to > Downloading Historical Prices](./downloading-historical-prices/csv-file.md#investingcom) for a detailed explanation how to import these historical prices. For appending the future daily prices, you can use the daily updated table from the last month. Set the Quote Feed of the Historical Quotes to `Table on website` and use the following Feed URL: https://www.investing.com/indices/msci-world-net-eur-historical-data. This Quote Feed will not overwrite the existing prices but will append new ones.
2. Many funds or ETF's replicate the MSCI World index. So, the historical prices of these ETF's are an exact copy of all the +- 1500 securities with their exact relative weight. For example As can be seen in Figure 1, their graphs are virtual identical.
