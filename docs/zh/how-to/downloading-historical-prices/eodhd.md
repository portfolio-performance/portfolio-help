---
title: EODHD
---

[EODHD](https://eodhd.com/)（End of Day Historical Data）网站全面涵盖了所有美国股票、ETF 和共同基金自设立以来的数据。此外，该平台还包含非美国证券交易所的历史数据，主要可回溯至 2000 年 1 月 3 日。

只需提供你的电子邮件地址，即可轻松获得一个[免费 API 令牌](https://eodhd.com/register)。该令牌每日有 20 次 API 请求的使用上限。不过，你只能获取最近一年的历史报价。

你可以在 Portfolio Performance 中用该 API 令牌配合自动报价馈送，正常使用没有问题。在设置（`帮助 > 首选项 > API 密钥`）中输入该令牌，并将 EOD Historical Data 选为报价馈送提供方。

如果你有某些特殊需求，也可以使用 JSON 报价馈送提供方（部分用例参见 [API 文档](https://eodhd.com/financial-apis/api-for-historical-data-and-volumes/)）。例如，下面的请求将获取 Apple 在 **2000 年 1 月**的历史价格。

*Feed URL*

`https://eodhd.com/api/eod/AAPL?from=2000-01-01&to=2000-01-31&period=d&api_token=demo&fmt=json`

*Path to Date* = `$[*].date`，*Path to Close* = $[*].close

在浏览器中输入该 URL 会显示如下（节选）JSON。
```
[
    {
        "date": "2000-12-01",
        "open": 17.0016,
        "high": 17.5,
        "low": 16.8112,
        "close": 17.0632,
        "adjusted_close": 0.2583,
        "volume": 385705600
    },
    {
        "date": "2000-12-04",
        "open": 17.1864,
        "high": 17.1864,
        "low": 16.436,
        "close": 16.688,
        "adjusted_close": 0.2526,
        "volume": 371520800
    },
    {
        "date": "2000-12-05",
        "open": 16.94,
        "high": 17.4384,
        "low": 16.3744,
        "close": 17.0016,
        "adjusted_close": 0.2574,
        "volume": 613978400
    }
]
```

这是一个对象数组；从根节点以 `$[*]` 访问。到日期的 JSON 路径由 `$[*].date` 构成，到收盘价的由 `$[*].close` 构成。
