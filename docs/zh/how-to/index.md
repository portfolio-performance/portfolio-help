---
title: 操作指南
---
*操作指南*这一章结合实际场景讲解 *Portfolio Performance* 程序的功能与用法。查看侧边栏（或在侧边栏折叠时点击 <span style="color:red">:material-menu:</span> 菜单）即可浏览全部主题。下面按字母顺序提供每个主题的简要说明。

- [为投资组合设定基准](./benchmarking.md)：基准比对是指将你的投资组合的绩效与 *S&P 500* 等金融指数作比较。本节说明如何从 Yahoo Finance、investing.com 等来源查找并添加指数，也介绍如何在绩效图表中显示基准，以及如何将投资组合的绩效与这些基准作比较。

- [在投资组合之间复制证券](./copy-securities.md)：本页说明如何在 Portfolio Performance 软件的不同投资组合之间转移证券，涵盖 *拖放*、*导出与导入*、*复制与粘贴*（借助中间的 CSV 文件）等方式。本页还讨论了在 XML 文件之间复制的复杂之处。

- [下载历史价格](./downloading-historical-prices/index.md)提供了获取历史股票价格的多种方法与数据来源。多数证券都能由 [Portfolio Performance](downloading-historical-prices/portfolioperformance.md) 或 [Yahoo Finance](downloading-historical-prices/yahoo-finance.md) 覆盖。在某些情况下，可能需要更精细的方法，例如从 [CSV 文件](downloading-historical-prices/csv-file.md)下载、利用 [JSON 报价馈送提供方](downloading-historical-prices/json.md)获取数据，或抓取[网页上的表格](downloading-historical-prices/table-website.md)。此外还有许多其他来源，如 [Alpha Vantage](downloading-historical-prices/alpha-vantage.md)、[EODHD](downloading-historical-prices/eodhd.md) 与 [Morningstar](downloading-historical-prices/morningstar.md)。

- [处理选择权股息](handling-choice-dividend.md)讨论的是选择权股息：股东可以在现金支付与股票支付之间作选择。文中给出在 Portfolio Performance 中记录此类账目的实用方法。

- [导入以 GBX 计价证券](import-gbx.md)是一份简短的指南，介绍如何导入以 GBX（便士）计价的账目与证券，重点说明如何创建货币正确的证券，以及如何为 CSV 导入准备账目数据。

- [阅读源代码](inspect-source-code.md)说明如何查看 GitHub 上的 Portfolio Performance 源代码，以理解波动率指标等计算方法。

- 在投资组合管理中，记录[合并](recording-merger.md)、[分拆](recording-spin-off.md)或[分股](recording-stock-split.md)相当常见。这些页面以 Amazon 分股、Daimler Truck Holding AG 分拆、Unipol Gruppo 合并等真实案例为例，介绍各种方法。[破产](insolvency.md)一节说明如何处理已破产公司的证券，包括停用自动报价更新、删除历史价格，以及手动调整证券价值。

- 导入银行 PDF 对账单能省下大量时间。[申请新的 PDF 导入器](requesting-new-importer.md)针对特定银行或券商的账目提供指导，包括如何提取并匿名化 PDF 文本、如何在 Portfolio Performance 论坛上提交请求，以及如何等待开发者完成集成。

- [获取黄金及其他贵金属价格](./gold-prices.md)：本页讨论投资黄金的各种方式，包括实物黄金、ETF 以及黄金矿业公司的股票。文中说明如何从 Ariva.de、LBMA、Gold.org 等网站下载黄金历史价格。

- [用户界面概览](user-interface.md)
说明 Portfolio Performance 用户界面的构成元素，例如菜单栏、侧边栏、双窗格布局、主窗格内的表格，以及常用功能的键盘快捷键。

大多数技巧与经验最初都在 [Portfolio Performance 论坛](https://forum.portfolio-performance.info)上讨论。经常查看该论坛能让你更深入地了解 Portfolio Performance 程序。需注意论坛上相当一部分信息是德语的，你可以使用浏览器的翻译功能，以你习惯的语言阅读。
