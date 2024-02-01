---
title: Alpha Vantage
---

Alpha Vantage provides realtime and historical financial prices through data APIs and spreadsheets. You can request a [free API key](https://www.alphavantage.co/support/) with lifetime access covering the majority of the datasets for up to 25 requests per day. Realtime quotes and some other resources however are premium.

The [API documentation](https://www.alphavantage.co/documentation/) is very well written with many examples. These examples can be executed in the browser with a provided demo API-key.  If you want to execute your own queries, you need the free API key.

Download the NVIDIA historical prices.

`https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NVDA&apikey=my_API_key`

This will return some metadata and the last 100 historical quotes in the browser window. If you want all available historical prices, use the option "outputsize=full".

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

    As of January 2024, Alpha Vantage changed some parameters and PP's JSON Quote Feed is no longer functional for this URL. The `Path to Date` and `Path to Close` JSON paths below result in an error; even if they are, according to the [JSONPath Online Evaluator](https://jsonpath.com/)a valid JSON path.

    - Path to Date: `$.[Time Series (Daily)].*~`
    - Path to Close: `$.[Time Series (Daily)].[*].[4. close]`



