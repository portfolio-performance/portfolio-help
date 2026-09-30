---
title: Alpha Vantage
---

Alpha Vantage 通过数据 API 和电子表格提供实时及历史金融价格。你可以申请一个[免费 API 密钥](https://www.alphavantage.co/support/)，终身可用，每日最多 25 次请求，可覆盖大部分数据集。但实时报价和其他一些资源属于付费项。

[API 文档](https://www.alphavantage.co/documentation/)写得非常出色，附有大量示例。这些示例可以在浏览器中用提供的演示 API 密钥执行。如果你想执行自己的查询，则需要那个免费 API 密钥。

下载 NVIDIA 的历史价格。

`https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NVDA&apikey=my_API_key`

浏览器窗口中会返回一些元数据和最近 100 条历史报价。如果你想获取全部可用的历史价格，请使用选项 "outputsize=full"。

```
{
    "Meta Data": {
        "1. Information": "Daily Prices (open, high, low, close) and Volumes",
        "2. Symbol": "NVDA",
        "3. Last Refreshed": "2024-01-25",
        "4. Output Size": "Compact",
        "5. Time Zone": "US/Eastern"
    },
    "Time Series (Daily)": {
        "2024-01-25": {
            "1. open": "623.5000",
            "2. high": "627.1900",
            "3. low": "608.5000",
            "4. close": "616.1700",
            "5. volume": "48277684"
        },
        "2024-01-24": {
            "1. open": "603.0400",
            "2. high": "628.4900",
            "3. low": "599.3800",
            "4. close": "613.6200",
            "5. volume": "55706870"
        }
    }
}

```

!!! Note

    自 2024 年 1 月起，Alpha Vantage 更改了部分参数，PP 的 JSON 报价馈送对该 URL 已不再适用。下面的 `Path to Date` 与 `Path to Close` JSON 路径会报错；尽管根据 [JSONPath Online Evaluator](https://jsonpath.com/)，它们是有效的 JSON 路径。

    - Path to Date: `$.[Time Series (Daily)].*~`
    - Path to Close: `$.[Time Series (Daily)].[*].[4. close]`

