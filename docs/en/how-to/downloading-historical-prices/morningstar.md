---
title: Import fund data from Morningstar
lastUpdate: 2023-09-13
---
!!! info
    **Best** answer in [forum](https://forum.portfolio-performance.info/t/import-fund-data-from-morningstar/14516) from SimonFitz!

The website of Morningstar is quite famous for its extensive list of funds. With some magic, you can download historical data for specific funds from this website.

First go to the Chart page for the fund (or trust or EFT) on the Morningstar website; e.g. [https://www.morningstar.co.uk/uk/](https://www.morningstar.co.uk/uk/). I will use the Baillie Gifford Positive Change Fund B Accumulation fund (ISIN GB00BYVGKV59) as an example.

Remove any other benchmarks etc. the are charted (this is not necessary, but makes things easier). Open your browser's "developer tools" which is F12 in Firefox & Edge and probably other browsers as well. Go to the "Network" tab and press the clear button which looks like a bin; again, not necessary but makes things easier. Now press the "chart settings" button just above the chart, click "display options", and then click the "percentage" button - this switches the chart to show the actual fund price, rather than a percentage change, and handily for our purposes causes the Morningstar website to request a link that we can use in Portfolio Performance with a bit of modification. That link should display in the "network" screen of the browser's developer tools, so now right-click on the entry that comes from the "tools.morningstar.co.uk 44" domain and is of type "json" and select the Copy->Copy URL option. The link should be

``` html
https://tools.morningstar.co.uk/api/rest.svc/timeseries_price/
t92wz0sj7c?currencyId=GBP&idtype=Morningstar&frequency=daily&
startDate=2011-02-01&priceType=&outputType=COMPACTJSON&
id=F00000ZB0M]2]0]FOGBR$$ALL&applyTrackRecordExtension=true
```
You now need to change some options in the link and slightly simplify it as well so it becomes:

``` html
https://tools.morningstar.co.uk/api/rest.svc/timeseries_price/
t92wz0sj7c?currencyId=GBP&idtype=Morningstar&frequency=daily&
outputType=JSON&startDate=2020-12-31&id=F00000ZB0M]2]0]
FOGBR$$ALL
```

You can go to this link in your browser if you want to see the data. There are 4 options worth highlighting: frequency which will give you daily prices, outputType gives you a style of JSON that Portfolio Performance can parse, startDate lets you choose how far back to go, and id is the Morningstar reference for the security - so change that value for any other ones you want to use. The order of the options doesn't matter, but I find it easier to put the id at the end for when I'm setting up multiple securities.

Now in Portfolio Performance select JSON as the provider in the "Historical Quotes" tab of the security, and use the following values (see also figure 1):

```
Feed URL = the link just created
Path to Date = $.TimeSeries.Security[*].HistoryDetail[*].EndDate
Path to Close = $.TimeSeries.Security[*].HistoryDetail[*].Value
```

![Example of JSON provider for historical quotes](../images/morningstar.png){.pp-figure}

Always worth double-checking the displayed values against the Morningstar chart.
