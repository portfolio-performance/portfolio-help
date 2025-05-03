---
title: Table on Website
---

Stock exchanges like NASDAQ publish historical and real-time quotations for the shares traded on their platforms.  Financial websites such as ariva.de offer a broader range. These historical prices are typically contained in a table with headings such as Date, Open, Close, ...

Scraping this information from the website should be possible. Portfolio Performance offers two methods: automatic and manual scraping.

## Automatic scraping

ARIVA.DE is a German website that provides financial information and news, such as stock prices, market indices, commodities, currencies, funds, certificates, bonds, and more.

Figure: Historical prices on ARIVA.DE (English translation){class=pp-figure}

![](images/table-website-arriva-de.png)

The URL for the webpage of Figure 1 is:
`https://www.ariva.de/nvidia-aktie/kurse/historische-kurse`.  Inputting this URL in the Feed URL field of Figure 2 will result in the quotes of the current month being downloaded. 
Using this method to append the historical quotes will only be effective when you regularly update the quotes by opening the portfolio or using the Online menu. Please note that you could select a different month, which could be a solution if you skipped one or several months.

Figure: Historical prices on ARIVA.DE (English translation){class=pp-figure}

![](images/table-website-PP-arriva-de.png)

For some reason, the Volume info isn't retrieved, and neither are the High & Low quote from the Bourserama URL: `https://www.boursorama.com/cours/historique/NVDA`. Please be aware that this link will provide monthly quotes, even though daily quotes are displayed on the screen.

## Manual scraping

The above mentioned method doesn't always work. Some websites use JavaScript or other technologies to build the tables on the clients machine. For example, at the Finanzen.net website, the default URL `https://www.finanzen.net/historische-kurse/nvidia` will only display the current day's quote, requiring input of the start and end date to view other periods. In such cases, manual scraping could be employed to capture this data.

Figure: Manual scraping. {class=pp-figure}

![](../../reference/view/images/contxt-mnu-all-securities-bottom-panel-hist-quotes-import-html-table.png)


- Present the data in the preferred download format.
- Right-click on the table and choose `Page Source` from the context menu.
- Highlight all text using the shortcut Ctrl + A.
- Copy the text with the shortcut Ctrl + C.
- Navigate to the dialog box in Figure 3; refer to [All Securities view](../../reference/view/securities/all-securities.md#information-pane).
- Paste the text (Ctrl + V) in the highlighted zone.
- Click on Next and then Finish.


