---
title: JSON Quote Feed Provider
---

## Import the data with an API

Financial web services commonly expose their data, e.g. historical prices, through an Application Programming Interface (API). To access these historical prices through the API, users can send HTTP requests to specific API endpoints, specifying parameters such as date ranges, stock symbols, and any other relevant filters. The API endpoint (=server) processes these requests, retrieves the requested historical price data from its database, and returns the information in a structured format, often JSON or XML.

For example, the following [endpoint URL](https://eodhd.com/api/eod/AAPL?from=2024-01-15&to=2024-01-17&period=d&api_token=demo&fmt=json) can be used to request the historical quotes of Apple between 2024-01-15 and 2024-01-17 from the `eod historical data` website.

`https://eodhd.com/api/eod/AAPL?from=2024-01-15&to=2024-01-17&period=d&api_token=demo&fmt=json`

As of January, 2024, the demo API token or key provided is still valid. If it ceases to function in the future, kindly apply for a [free API key](./eodhd.md).

``` JSON
[
    {
        "date": "2024-01-16",
        "open": 182.16,
        "high": 184.26,
        "low": 180.93,
        "close": 183.63,
        "adjusted_close": 183.63,
        "volume": 65603000
    },
    {
        "date": "2024-01-17",
        "open": 181.27,
        "high": 182.93,
        "low": 180.3,
        "close": 182.68,
        "adjusted_close": 182.68,
        "volume": 47317400
    }
]

```

A JSON response can contain two kinds of elements: lists and objects. A list is an ordered collection of elements between [ ]. These can be accessed by their position. An object is an unordered collection of key-value pairs between { }. A key is a unique identifier for a value, and a value can be any type of data, such as a number, a string, a boolean, a list, or an object. A JSON response is a hierarchical structure, meaning that a list can contain other lists or objects, and an object can contain other lists or objects.

To access a specific value within this hierarchical structure, you need to specify the path from the root to the element. To access an element from a list, you need to use its index, which is a number that indicates its position in the list. The index starts from 0 for the first element. To access an element from an object, you need to use its key, which is a string that indicates its name in the object. The key is enclosed in double quotes " ".

A query language such as *JSONPath* (used by PP) represents the root of the JSON response with a $ symbol. To separate the elements in the path, you need to use a dot. For example, to access the close price on the second day, you need to use the path ``$[1].close``. This means that you start from the root $, then go to the second element in the list ``$[1]``, which is an object, then go to the value with the key "close" in the object ``$[1].close``, which is a number.

You need this JSON path to complete PP's JSON Quote Feed Provider. Use the following parameters to retrieve the historical quotes (see also Figure 1). For an explanation of the meaning of different quote prices, please check [Concepts > Historical Prices](../../concepts/historical-prices.md).

Figure: Server response from JSON Quote Feed Provider (EODHD). {class=pp-figure}

![](images/json-eodhd-parameters.png)


- Feed URL: `https://eodhd.com/api/eod/AAPL?from=2024-01-15&to=2024-01-17&period=d&api_token=demo&fmt=json`
- Path to Date: `$[*].date`
- Path to Close: `$[*].close`
- Path to Day's Low: `$[*].low`
- Path to Day's High: `$[*].high`
- Path to Volume: `$[*].volume`


Let's try a more complicated example. The following endpoint URL enables the retrieval of NVIDIA's two most recent daily quotes from Yahoo Finance (click the following link to see the result).

[https://query1.finance.yahoo.com/v8/finance/chart/NVDA?interval=1d&range=5d](https://query1.finance.yahoo.com/v8/finance/chart/NVDA?interval=1d&range=2d)


The response from the Yahoo server is a lengthy JSON document with all the historical quotes of the last 2 days. The output has been restructured and abbreviated for clarity (scroll down to see the quotes).

``` JSON
{
  "chart": {
    "result": [
      {
        "meta": {
          "currency": "USD", 
          "symbol": "NVDA"
        },
        "timestamp": [1705415400, 1705501800],
        "indicators": {
          "quote": [
            {
              "close": [563.82, 560.53],
              "open": [550.17, 563.46],
              "high": [568.34, 564.71],
              "low": [549, 547.40],
              "volume": [44958000, 47439400]
            }
          ],
          "adjclose": [
            {
              "adjclose": [563.82, 560.53]
            }
          ]
        }
      }
    ],
    "error": null
  }
}

```

The JSON response from above is an object, surrounded by { }. It contains meta data of the security, Unix timestamps from the two retrieved dates, and the different quote prices. You need a JSON path to retrieve the different values:

- Error code of the reponse: `$.chart.error`
- Metadata of the security: `$.chart.result[0].meta`. The result field is an array, even though there is only one element, probably because one can also ask data for multiple securities.
- Symbol name: `$.chart.result[0].meta.symbol`
- Requested dates: `$.chart.result[0].timestamp[*]`. The * serves as wildcard, facilitating the retrieval of all values.
- Second date: `$.chart.result[0].timestamp[1]`
- All available quotes (incl adjusted quotes): `$.chart.result[0].indicators`
- All non-adjusted quotes: `$.chart.result[0].indicators.quote[0]`
- Close quotes: `$.chart.result[0].indicators.quote[0].close`
- Close quote of the first date: `$.chart.result[0].indicators.quote[0].close[0]`

If you want to practice, you can use the [JSONPath Online Evaluator](https://jsonpath.com/). Copy the JSON result from the URL endpoint into the input window. Another practical tool is the [JSONPath Finder](https://jsonpathfinder.com/).

With the above information, it should be easy to provide the JSON Quote Feed provider of Portfolio Performance with the correct input.

Figure: JSON Quote Feed provider parameters. {class=pp-figure}

![](images/json-yahoo-parameters.png)


For most services, one needs to register and obtain an API key, which is a unique identifier that authenticates the user and grants access to the service. While numerous financial services provide seemingly free API keys, their terms of use and long-term commitment often prove inadequate. Portfolio Performance has, for compatibility reasons, maintained several of these services in its list of Quote Feed providers; e.g. Alpha Vantage, eodhd, .... Although once considered excellent solutions, they have changed their offerings and are no longer as useful as free services. In practical terms, only Portfolio Report and Yahoo Finance can be recommended for a typical portfolio.

