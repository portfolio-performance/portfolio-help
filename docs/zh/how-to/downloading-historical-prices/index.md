---
title: 下载历史股票价格
---

图： 历史报价的数据来源。{class=align-right style="width:40%"}

![](../../reference/file/images/quote-feeds.png)

要找到既准确及时、又免费的历史价格数据源并不容易。Portfolio Performance 的数据源清单包含以下选项（见图 1）：[Alpha Vantage](alpha-vantage.md)、[EOD Historical Data](eodhd.md)、Finnhub、Leeway、Twelve Data、[Portfolio Performance（内置）](portfolioperformance.md)、Quandl 以及 [Yahoo Finance](yahoo-finance.md)。其余选项则主要适用于比特币和其他统计数据。

遗憾的是，其中许多选项的使用条款随着时间推移变得越来越严格。此处列出它们主要是出于兼容性的考虑。就实际使用而言，对于典型投资组合，只有 [Portfolio Performance（内置）](portfolioperformance.md) 和 [Yahoo Finance](yahoo-finance.md) 或 JSON 值得推荐。

下面讨论一些具体的使用场景。更多场景见[论坛](https://forum.portfolio-performance.info/t/quellen-fur-historische-kurse/46)（德语）。

## 非常久远的历史价格 {#very-old-historical-prices}

大多数金融服务通常只提供有限时间范围内的历史价格，例如最近一年，或自某个较近的特定日期起。然而，如果你恰好是那些在 1980 年代就买入 Apple 股票的幸运者之一，那么从头开始追踪你的绩效会是一件很惬意的事。


!!! note

    Apple 于 1980 年 12 月 12 日首次公开上市，每股开盘价为 `$`22。该公司在 NASDAQ 证券交易所挂牌，代码为 AAPL。此后该股票已分股五次，最近一次是在 2020 年，因此按分股调整后计算，首次公开上市时的股价为 $.10。

1. 选择 [Yahoo Finance](./yahoo-finance.md) 作为报价提供方帮不了你太多：它只会从今天起下载 3 个月的历史报价。

2. 选择 [JSON 报价提供方](./json.md) 则可以指定想要的价格区间。例如，下面的 URL 试图下载 30 年的数据：

    `https://query1.finance.yahoo.com/v8/finance/chart/NVDA?interval=1d&range=30y`

    实际上拿不到 30 年，但你能拿到直到 1991 年的数据，也就是大约 25 年的历史价格。

3. 通常，公司网站本身就包含这类信息。出人意料的是，Apple 官网并未提供下载历史数据的选项；你只能查询某些价格。另一方面，你可以查看[股息与分股](https://investor.apple.com/dividend-history/default.aspx)信息。[NASDAQ](https://www.nasdaq.com/market-activity/stocks/aapl/historical) 允许你下载一个 CSV 文件，但只能回溯 10 年。

4. 自然而然地，作为一只高关注度的股票，网上能找到更全面的数据。例如，[Kaggle](https://www.kaggle.com/datasets/meetnagadia/apple-stock-price-from-19802021) 提供了一份 1980-2021 年 Apple 股票价格的 CSV 文件。你可以下载该文件，将其导入历史价格，再让 Yahoo Finance 补上缺失的数据。

## 共同基金 {#mutual-funds}

假设你想跟踪欧洲的 [Fidelity Funds](https://www.fidelity.lu/funds/factsheet/LU0114720955) 旗下的 `Sustainable Health Care Fund`（ISIN：lu0114720955）。[Yahoo Finance](https://finance.yahoo.com/quote/FJ2U.F/history?p=FJ2U.F) 上只有最近一个价格。

[Investing.com](https://www.investing.com/funds/lu0114720955) 做得稍好一些，提供了自基金成立（2000-09-01）以来的历史数据。你可以把这些数据下载为 CSV 文件；参见[下载历史价格 > CSV 文件](./csv-file.md)一节。

当然，最全面的共同基金网站是 Morningstar。
你需要访问一个欧洲网站，例如 https://www.morningstar.co.uk/uk/funds/snapshot/snapshot.aspx?id=F0GBR04EBS&tab=13


## ETF 跟踪 {#etf-tracker}

## 债券 {#bonds}

## 黄金 {#gold}
