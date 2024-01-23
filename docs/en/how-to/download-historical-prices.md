---
title: Download Historical Prices
---

Figure: Data sources Historical Quotes.{class=align-right style="width:40%"}

![](../reference/file/images/quote-feeds.png)

Finding good (=precise, up-to-date) but free data sources for all your historical and latest prices of your portfolio can be challenging. PP already provides many alternatives (see Figure 1) and many more are described in the [Forum](https://forum.portfolio-performance.info/t/quellen-fur-historische-kurse/46) (in German).

There isn't a shortage of financial services, but their terms of use and, most importantly, their commitment in the long run fall short often. Many of the data sources in Figure 1 were once excellent solutions but have since changed their offerings and are not as useful anymore as free services. 

In practice, for a typical portfolio, Portfolio Report and Yahoo Finance could be recommended, in combination with HTML scraping and JSON. The other alternatives are either for other purposes (statistical data and bitcoins) or retained in the list for compatibility reasons.

There are three primary methods for obtaining financial data from the web: downloading a CSV file, using an API (Application Programming Interface), or scraping the data from a webpage. The website [finance.yahoo.com](https://finance.yahoo.com/quote/NVDA/history?p=NVDA) supports all three methods.

## Downloading a data file

Figure: Webpage from finance.yahoo.com to download the historical prices of NVIDIA.{class=pp-figure}

![](images/yahoo-finance-webpage.png)

Each website may have a distinct approach. Typically, you need to navigate to the desired security and locate the download link on that webpage. For instance, after navigating to the website [Yahoo Finance](https://finance.yahoo.com), you can enter the name "NVIDIA" in the Search box at the top of the screen. Select the Historical Prices tab in the middle of the screen. From there, you can specify the Time Period and frequency before downloading a CSV file containing historical prices. Import this CSV file into Portfolio Performance using the menu `File > Import > CSV Files`, choosing the Historical Prices option and assign it to the correct security.

It's important to note that this method provides a snapshot of historical prices. To obtain the quotes of tomorrow, you should repeat the process. In practice, you need to combine this approach with one of the automatic quote download methods below. Remember that you can [keep the existing historical quotes](../reference/file/images/mnu-file-import-reload-quotes.png), even if you change the quote provider to automatic download.

## Import the data with an API

An API is a set of rules and protocols that allows one software to communicate with another. In PP you can specify Yahoo Finance as Quote Feed provider (see Figure 1) and magically the historical prices are downloaded. In the background however, PP sends a request to the Yahoo website and formats the resulting JSON data into the table.

The sending request resembles a bit the following URL: [https://query1.finance.yahoo.com/v8/finance/chart/NVDA?metrics=high?&interval=1d&range=5d](https://query1.finance.yahoo.com/v8/finance/chart/NVDA?metrics=high?&interval=1d&range=5d). If you enter this URL in a webbrowser the following JSON code is returned (I've removed some non-essential info to shorten the output)

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
					"regularMarketTime": 1705698000,
					"gmtoffset": -18000,
					"timezone": "EST",
					"exchangeTimezoneName": "America/New_York",
					"regularMarketPrice": 594.91,
					"chartPreviousClose": 548.22,
					"priceHint": 2,
					"currentTradingPeriod": {
						"pre": {
							"timezone": "EST",
							"start": 1705654800,
							"end": 1705674600,
							"gmtoffset": -18000
						},
						"regular": {
							"timezone": "EST",
							"start": 1705674600,
							"end": 1705698000,
							"gmtoffset": -18000
						},
						"post": {
							"timezone": "EST",
							"start": 1705698000,
							"end": 1705712400,
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
					1705069800,
					1705415400,
					1705501800,
					1705588200,
					1705674600
				],
				"indicators": {
					"quote": [
						{
							"open": [
								546.2000122070312,
								550.1799926757812,
								563.469970703125,
								572.5999755859375,
								579.8900146484375
							],
							"volume": [
								35247900,
								44958000,
								47439400,
								49165000,
								54210300
							],
							"low": [
								543.2999877929688,
								549,
								547.4000244140625,
								561.0700073242188,
								572.25
							],
							"close": [
								547.0999755859375,
								563.8200073242188,
								560.530029296875,
								571.0700073242188,
								594.9099731445312
							],
							"high": [
								549.7000122070312,
								568.3499755859375,
								564.7100219726562,
								576,
								595
							]
						}
					],
					"adjclose": [
						{
							"adjclose": [
								547.0999755859375,
								563.8200073242188,
								560.530029296875,
								571.0700073242188,
								594.9099731445312
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
This is exactly the same code that you should receive if using the JSON Quote provider of PP.
Got Quote feed. Choose JSON and paste the URL. Click the button Show server response and choose JSON format.

another software but less handy is: https://jsonpath.com/

How does PP retrieve the dates and their corresponding quotes.
Navigate to the site [https://jsonpathfinder.com/](https://jsonpathfinder.com/) and paste the code in the left window. At the right you can find the path to the individual keys in the JSON data.
For example the path to the
 first date is $.chart.result[0].timestamp[0]
 second date is $.chart.result[0].timestamp[1]
 to all dates is $.chart.result[0].timestamp[*]

There are 5 types of quotes: open, low, high, close, adjclose.
 the first quote: $.chart.result[0].indicators.quote[0].close[0]
 all quotes: $.chart.result[0].indicators.quote[0].close[*]

Because yahoo is an important datasource, PP will perform all these actions in the background and will provide you with the quotes simply.

Something comparable can be done for a table on a website. For this, the raw html source code must be parsed.
does their ex

Some websites, such as finance.yahoo.com, provide APIs that allow users to access their data in a structured and standardized format. For example, one can use the Yahoo Finance API to get historical stock prices. 

However, not all websites offer APIs, or they may limit the amount and frequency of data that can be accessed through them. In such cases, one may need to scrape the web pages directly, using tools such as Python, BeautifulSoup, Selenium, or Octoparse1. These tools can parse the HTML code of the web pages and extract the relevant data, such as stock prices, company data, news articles, etc. However, scraping web pages directly requires more coding skills, and it may be more prone to errors and inconsistencies, as the web pages may change over time or block the scraping requests.

As you can see in Figure 4, the website [https://finance.yahoo.com/](https://finance.yahoo.com/) is selected. Searching this website for the historical prices of a stock named "Deutsche Telekom" (which is in reality `share-1`) will produce the following URL: [https://finance.yahoo.com/quote/DTE.DE/history?p=DTE.DE](https://finance.yahoo.com/quote/DTE.DE/history?p=DTE.DE). However, if you should consult this webpage, you will notice that the historical prices are by default only given for one year. Additional actions are required to set the time period. All of this is handled by PP.

    

The Quote Feed Provider and Exchange input boxes will provide PP with exactly this information.

Some of these Quote Feeds such as Alpha Vantage and EOD Historical Data need an API key.  Most of them are free but with some limitations. You need to register for this key on the website of the provider. The API keys then are stored in PP. You can set them with the menu `Help > Preferences > API keys`.

[ Text between [] should be treated as context. Make a rather formal instructional text of about 2 pages. Use short simple sentences. Use the text as a guidance to the structure and elaborate on the used concepts. Dont't use titles or headings. Lists are OK.]

Historical quotes
- to calculate the performance of a security, one needs some kind of historical quotes.
- securities are traded on exchange markets such as NASDAQ [give a few more examples].
- The mostly used historical quote is the close price of a security. Other possibilities are: open, low, high. [give a definition]
- The adjusted close and the latest quote are a special one. [define and explain why special]
- There are several financial services that provide historical quote feeds such as Yahoo Finance, Quandl, ...
- There are three main methods to download historical prices: (1) download a csv file, (2) use API, or (3) scrape a webpage [elaborate ]
- All three start with a request to the financial service/website. [Describe here in general the flow between client and server through request and response. Add an illustration or link to an appropriate illustration.]
- The response could be thus: a csv-file, a JSON text (mostly used in API) or a webpage. In all these cases, PP needs to map its internal fields such as date and quote with the sent fields. [describe the mapping process]
-  For some providers (Yahoo and PortfolioReport) this is done automatically by PP because it knows the structure of the response. For others this must be done manual but assisted by PP.

