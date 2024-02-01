---
title: EODHD
---

The [EODHD](https://eodhd.com/) (End of Day Historical Data) website provides comprehensive coverage of all U.S. stocks, ETFs, and mutual funds from their inception. Additionally, the platform encompasses historical data for non-U.S. stock exchanges, primarily dating back to January 3, 2000.

A [free API-token](https://eodhd.com/register) can be easily obtained by providing your email address. The token comes with a usage limit of 20 API requests per day. However, only historical quotes from the last year could be retrieved.

You can use the API-token with the automatic Quote Feed of PP from within PP works just fine. Enter the token in the Settings (Help > Preferences > API Keys) and choose EOD Historical Data as Quote Feed Provider.

If you have some special requirements, you can also use the JSON Quote Feed Provider (see [API documentation](https://eodhd.com/financial-apis/api-for-historical-data-and-volumes/) for some use cases). For example, the following request will retrieve the Apple historical prices from the **month January 2000**.

*Feed URL*

`https://eodhd.com/api/eod/AAPL?from=2000-01-01&to=2000-01-31&period=d&api_token=demo&fmt=json`

*Path to Date* = `$.[*].date` and *Path to Close* = $.[*].close

Entering the URL in a browser will display the following (abbreviated) JSON.
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

This is an array of objects; accessed from the root with `$.[*]`. The JSON path to the date is formed by `$.[*].date` and to the closing price with `$.[*].close`.