---
title: Historical Prices
---
To calculate performance, PP requires two types of historical prices: the historical quotes of securities and in case of foreign investments, the historical exchange rates for currencies.

You can find the historical exchange rates under the menu View > Settings. These exchange rates are retrieved from [The European Central Bank](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html) (ECB) and go back until the year 1999 when the EUR was introduced on the financial markets. They are in fact reference rates and will probably differ slightly from the real transaction rates that your broker or bank will use.

Securities are traded on exchange markets such as NADAQ or XETRA, where buyers and sellers agree on a price. Historical quotes are the prices of securities at different points in time. The `Close` price is the last price of the security at the end of the trading day. Other types are the `Open` quote, the first price of the security at the start of the trading day, the `Low` and `High`quotes, which are the lowest and highest price of the security during the trading day. The `Latest` quote is the most recent price of the security available from the exchange market. The latest quote may not be the same as the close price.

!!! Note
    PP uses the `Close` quote in its performance calculations. If there is a Latest quote available, it will be integrated in the Close price. For Bitcoins, the situation is more complex because they are traded 24/24. PP uses midnight (on the users system) to set the Close Quote. So, the historical quotes of a bitcoin could vary between users.

Sometimes, the historical quotes are adjusted to reflect certain events that affect the value of the security, such as stock splits, dividends, or mergers. These are called the `Adjusted close` quotes. They are useful for comparing the long-term performance of the security, as they account for the changes in the number of shares or the amount of cash paid to the shareholders.

Exchange markets (must) publish the historical quotes of the securities they trade. Several financial services such as Yahoo Finance, Alpha Vantage, and others provide historical quotes for different securities and exchange markets through their websites.

!!! note
    Usually, a user navigates to a specific website to download a web page containing historical price data. The outcome is a well-crafted page featuring a table displaying daily stock prices. In theory, one could scrape this webpage. PP has even an option for that. However, in practice, most service providers utilize JavaScript or another technology that hinders this scraping process.

There are two primary methods for obtaining financial data from the web: downloading a csv file, or using an API (Application Programming Interface) to get the data.

Both methods start with a request to the financial service or website. A request is a message that contains the information and parameters needed to access the historical quote feed. A request is sent from the client, which is the user's device or application, to the server, which is the financial service or website. The server processes the request and sends back a response. The response could be a csv file, or a structured text (JSON or XML).

In both cases, PP needs to map its internal fields, such as date and value of the quote, with the data in the response. If successfully, PP can use these fields then in its performance calculation.

## Downloading a CSV file

A csv file is a comma-separated values file, which is a text file that stores tabular data. Each row in the file represents a record, and each column represents a field. For example, a typical historical quotes CSV file will contain two columns (date and quote) and several rows, one for each date with its corresponding historical quote. A csv file can be opened and edited by spreadsheet software and easily imported into PP.

Figure: Webpage from finance.yahoo.com to download the historical prices of NVIDIA.{class=pp-figure}

![](./images/yahoo-finance-webpage.png)

Each website may have a distinct approach for downloading a csv file of the historical data (see Figure 1). Typically, you need to navigate to the desired security and locate the download link on that webpage. For instance, after navigating to the website [Yahoo Finance](https://finance.yahoo.com), you can enter the name "NVIDIA" in the Search box at the top of the screen. Select the Historical Prices tab in the middle of the screen. From there, you can specify the Time Period and frequency before downloading a CSV file containing historical prices. Import this CSV file into Portfolio Performance using the menu `File > Import > CSV Files`, choosing the Historical Prices option and assign it to the correct security.

Hovering over the download link, you may have noticed the URL endpoint: `https://query1.finance.yahoo.com/v7/finance/download/NVDA?period1=1674359406&period2=1705895406&interval=1d&events=history&includeAdjustedClose=true` (see Figure 1 at the bottom of the image).

This is the request you send to the Yahoo server. It contains the ticker symbol of the security (NVDA), the time period expressed as Unix timestamps or the number of seconds that have elapsed since January 1, 1970, the frequency or interval (1d), the type of info you want (events=history), and the Adjusted Close price. The CSV file contains 7 columns: Date, Open, High, Low, Close, Volume, and Adj Close.

It's important to note that this method provides a snapshot of historical prices. To obtain the quotes of tomorrow, you should repeat the process. In practice, you need to combine this approach with one of the automatic quote download methods below. Remember that you can [keep the existing historical quotes](../reference/file/images/mnu-file-import-reload-quotes.png) in PP, even if you change the quote provider to automatic download.

!!! Note
    For instance, stock exchange markets usually offer a restricted period of historical data, typically one or two years. Therefore, you might import older historical quotes through a more specialised service. Subsequently, you could utilise an automatic quote feed such as PortfolioReport for the daily updates.

## Import the data with an API

An API is an application programming interface, which is a set of rules and protocols that allow different software applications to communicate and exchange data. An API can be used to request and receive historical quotes from a financial service in a structured and human-readable format, such as JSON (JavaScript Object Notation) or XML (Extensible Markup Language). For example, the following endpoint URL can be used to request NVIDIA's 5 most recent daily quotes from Yahoo Finance.

```
https://query1.finance.yahoo.com/v8/finance/chart/NVDA?interval=1d&range=5d
```

The response from the Yahoo server is a lengthy JSON document with all the historical quotes of the last 5 days (scroll down to see the quotes).

``` JSON
{
  "chart": {
    "result": [
      {
        "meta": {
          "currency": "USD",
          "symbol": "NVDA",
          "exchangeName": "NMS",
          "instrumentType": "EQUITY",
          "firstTradeDate": 917015400,
          "regularMarketTime": 1705957200,
          "gmtoffset": -18000,
          "timezone": "EST",
          "exchangeTimezoneName": "America/New_York",
          "regularMarketPrice": 596.54,
          "chartPreviousClose": 547.1,
          "priceHint": 2,
          "currentTradingPeriod": {
            "pre": {
              "timezone": "EST",
              "start": 1706000400,
              "end": 1706020200,
              "gmtoffset": -18000
            },
            "regular": {
              "timezone": "EST",
              "start": 1706020200,
              "end": 1706043600,
              "gmtoffset": -18000
            },
            "post": {
              "timezone": "EST",
              "start": 1706043600,
              "end": 1706058000,
              "gmtoffset": -18000
            }
          },
          "dataGranularity": "1d",
          "range": "5d",
          "validRanges": [
            "1d",
            "5d",
            "1mo",
            "3mo",
            "6mo",
            "1y",
            "2y",
            "5y",
            "10y",
            "ytd",
            "max"
          ]
        },
        "timestamp": [
          1705415400,
          1705501800,
          1705588200,
          1705674600,
          1705933800
        ],
        "indicators": {
          "quote": [
            {
              "close": [
                563.8200073242188,
                560.530029296875,
                571.0700073242188,
                594.9099731445312,
                596.5399780273438
              ],
              "open": [
                550.1799926757812,
                563.469970703125,
                572.5999755859375,
                579.8900146484375,
                600.489990234375
              ],
              "high": [
                568.3499755859375,
                564.7100219726562,
                576,
                595,
                603.3099975585938
              ],
              "low": [
                549,
                547.4000244140625,
                561.0700073242188,
                572.25,
                590.7000122070312
              ],
              "volume": [
                44958000,
                47439400,
                49165000,
                54210300,
                45213100
              ]
            }
          ],
          "adjclose": [
            {
              "adjclose": [
                563.8200073242188,
                560.530029296875,
                571.0700073242188,
                594.9099731445312,
                596.5399780273438
              ]
            }
          ]
        }
      }
    ],
    "error": null
  }
}

```
The JSON text from above has one top-level key: `chart`. This key contains an object with two keys: `result` and `error`.

- **result**: An array of objects, each object having two keys:

    - **meta**: Contains metadata about the equity, such as currency, symbol, exchange name, instrument type, ...
    - **timestamp**: An array of Unix timestamps, i.e. the dates of the quotes blow.
    - **indicators**: Contains two keys, `quote` with the close, low, high, ... values and `adjclose` with the adjusted close value.
- **error**: Contains error information, if any. In this case, it's `null`, indicating no error occurred.

PP knows about the Yahoo's endpoint URL and the structure of the JSON response. Therefore, it can extract the historical quotes automatically and you -as user- has only to specify that the quote provider is Yahoo. Let's imagine that PP doesn't know about Yahoo's API. Then, you have to specify yourself the URL endpoint and where in the json structure the dates and quotes are placed. You do this with the parameters Path to Date, Path to Close, path to ... (see figure 2).

Figure: Server response from JSON Quote Feed Provider. {class:pp-figure}

![](images/historical-quotes-json.png)


For most services, one needs to register and obtain an API key, which is a unique identifier that authenticates the user and grants access to the service. While numerous financial services provide seemingly free API keys, their terms of use and long-term commitment often prove inadequate. PP has, for compatibility reasons, maintained several of these services in its list of Quote Feed providers. Although once considered excellent solutions, they have changed their offerings and are no longer as useful as free services. In practical terms, only Portfolio Report and Yahoo Finance can be recommended for a typical portfolio.

