---
title: Hack data file to add default Quote Feed
lastUpdate: 2023-11-05
---

Adding securities through the GUI adds a Quote Feed but this is not supported by csv imports. You can hack the XML file directly with a text editor using a replace to add the Quote Feed.

!!! Warning
    This is totally not supported and can break your data file so backup your data file and test the changes.

When the data file is updated it will look similar to the following with a YAHOO feed:

```html
<client>
  <version>51</version>
  <baseCurrency>AUD</baseCurrency>
  <securities>
    <security>
      <uuid>831d8a3e-7025-4b0f-b6ca-3ef5bf727eb4</uuid>
      <name>REA Group Ltd</name>
      <currencyCode>AUD</currencyCode>
      <tickerSymbol>REA.AX</tickerSymbol>
      <feed>YAHOO</feed>
      <prices>
```

Use the text editor to search and replace:

```html
</tickerSymbol> 
     <prices>
```

with

```html
</tickerSymbol>
      <feed>YAHOO</feed>
      <prices>
```

Any text editor that will work with end of line characters will work. For example, the image below shows the [np++](https://notepad-plus-plus.org/) Extended interface which uses a \n as new-line and the groups of 4 spaces are important:


![Example of np++ replace to add the Quote Feed](images/quote-feed.png){.pp-figure}
