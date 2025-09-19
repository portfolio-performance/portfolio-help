---
title: Price Update Status
---

With the menu [Online](../../online.md), you can update the historical prices of some or all of your securities. Depending on your internet connection, the chosen data provider and the number of securities, this process may be very fast or noticeably slow.

The `Price Update Status` view (see Figure 1) provides a detailed status report of this (automatic) update process.

Figure: Menu View > Price Update Status.{class=pp-figure}

![](images/mnu-view-price-update-status.png)

The title at the top left shows the name of the view and the date of the displayed update. On the right, you will find several (drop-down) buttons and the `Show or hide colums`gear :gear: icon.

By default, the table below displays the following columns.

- Name of the security  
- Latest quote price  
- Date of the latest quote price 

The next six columns display the status, the feed, and any error messages related to the update process for both historical prices and the latest quote. The status can be:

- `Updated`  
- `No change`  
- `Skipped` – shown when the quote feed is set to `No automatic quote download`
  in the [security master data](../../file/new.md#security-master-data).  

The quote feed source is also defined in the security master data.

Using the :gear: icon, you can customise this view to display different columns.

The drop-down button `Update Quotes` (top) works similarly to the [Online](../../online.md) menu.  

- Selecting `In progress` gives you a temporary view of the update process while it is running.  
- Once the update is finished, all information is cleared. To keep the last status report (see Figure 1), select the `Completed` button.
- If the update process encounters an error (e.g. the source website is unavailable), you can view the error log using the `Error` button.  

There is also a dedicated `Migrate Portfolio Report` button for users who previously relied on the external Portfolio Report website as a data source and now wish to switch to the built-in Portfolio Performance data source.