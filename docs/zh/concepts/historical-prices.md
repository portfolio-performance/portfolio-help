---
title: 历史价格
---
为计算绩效，Portfolio Performance 可能需要两类历史价格：证券的历史报价，以及在投资境外资产时的历史汇率。

你可以在菜单 `视图 > 常规数据 > 货币` 下找到历史汇率（见图 1）。这些汇率取自[欧洲中央银行](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html)（ECB），可追溯至 1999 年欧元进入金融市场之时。它们实际上是参考汇率，很可能与你的券商或银行所用的实际成交汇率略有差异。

图： 汇率。{class=pp-figure}

![](../reference/view/general-data/images/currencies.png)


证券在 NASDAQ、XETRA 等交易所市场交易，买卖双方在此就价格达成一致。历史报价即证券在不同时间点的价格。`收盘`价是证券在交易日当天的最后一个价格。其他类型还有：`开盘`价，即交易日开始时证券的第一个价格；`最低`与`最高`价，即交易日当天的最低价与最高价。`最新`价是交易所市场上可获得的证券最近价格。最新价可能与收盘价不同。

图： Yahoo Finance 上的历史价格。{class=pp-figure}

![](../how-to/downloading-historical-prices/images/yahoo-finance-webpage-aapl.png)


!!! Note
    Portfolio Performance 在绩效计算中使用 `收盘`价。若存在最新价，它会被计入收盘价。对比特币而言情况更复杂，因为它们 7×24 小时交易。Portfolio Performance 以（用户系统上的）午夜作为收盘价。因此，不同用户看到的比特币历史报价可能不同。

有时，历史报价会经过调整，以反映影响证券价值的某些事件，例如分股、股息或合并。这类报价称为 `调整后收盘`价。它们的用处在于比较证券的长期绩效，因为它们已计入份额数量变化以及向股东支付现金的影响。

发布历史价格的金融服务机构并不缺，但其中大多数价格不菲。许多机构也提供所谓的免费账户，但正如俗话所说：*如果免费，你就是产品*。为你的全部历史价格找到*优质*（准确、及时）又*免费*的数据源并不容易。Portfolio Performance 建议过 *Alpha Vantage*、*Finnhub*、*Quandl*，它们曾是极好的方案，但后来改变了服务内容，作为免费服务已不再那么有用。他们的使用条款，尤其是长期承诺，往往难以令人满意。实践中，目前只有 Portfolio Report 与 Yahoo Finance 还值得推荐（Yahoo Finance 自 2024 年底起也已将 CSV 下载置于付费墙之后）。一些技巧请见[操作指南一节](../how-to/downloading-historical-prices/index.md)。

交易所市场（应当）公布其交易证券的历史报价。Yahoo Finance、Alpha Vantage 等多家金融服务机构通过各自的网站，为不同证券和交易所市场提供历史报价。

从网络上获取金融数据主要有两种方式：下载 csv 文件，或使用 API（应用程序编程接口）获取数据。

两种方式都始于向该金融服务或网站发出一次请求。请求是一条消息，包含访问历史报价馈送所需的信息与参数。请求从客户端（即用户的设备或应用程序）发往服务器（即金融服务或网站）。服务器处理请求并返回响应。响应可能是一个 csv 文件，或是一段结构化文本（JSON 或 XML）。

在两种情况下，Portfolio Performance 都需要把其内部字段（如报价的日期与数值）与响应中的数据做映射。若映射成功，Portfolio Performance 便可在绩效计算中使用这些字段。

!!! note
    理论上，也可以抓取那些含有历史价格表格的网页（例如见图 2）。Portfolio Performance 支持这种方式，见[导入 HTML 表格](../reference/view/securities/all-securities.md#import-html-table)。但实际上，如今大多数服务提供方都使用 JavaScript 或其他妨碍此类抓取的技术。