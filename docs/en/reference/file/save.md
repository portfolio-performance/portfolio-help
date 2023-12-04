---
title: Save - Save As
---

# File &#10095; Save - Save As

With the menu `File > Save`, you can save your portfolio in an XML-file (eXtensible Markup Language) format using the existing name. It's equivalent to choosing `File > Save As`, with the latter having the added flexibility to change the name and file type. Six file formats are available.

## XML

All data of your portfolio is stored in one XML-file (eXtensible Markup Language). This is a human-readable file format. For example, the following xml-file [test.xml](../../assets/test.xml) is a very simple portfolio with one security (`share-1`) and two transactions (one deposit and one buy). You can view the xml-content by opening this file with a text editor (e.g. Notepad++). Here's a brief description of the main elements:

- `<securities>`: Contains information about securities, including details such as UUID, name, currency code, ticker symbol, feed, historical prices, and attributes.
    `<prices>`: Contains historical price information for a security.
    `<latest>`: Provides the latest details for a security, including high, low, and volume.

- `<accounts>`: Contains details about client accounts, including UUID, name, currency code, and transactions.

- `<transactions>`: Represents financial transactions within an account, including details such as UUID, date, currency code, amount, and type.

- `<portfolios>`: Contains references to portfolios associated with accounts.

- `<dashboards>`: Contains information about client dashboards, including name, configuration, columns, and widgets.

- `<properties>`: Holds client-specific properties, such as security chart details.
- `<settings>`: Contains various settings, including bookmarks and attribute types.
- `<configurationSets>`: Stores configuration sets with specific data.

Below you can see the xml code for the buying transaction in Figure 1.

Figure: Example of a buying transaction.{class=pp-figure}

![](./images/mnu-transaction-buy-share-microsoft.png)

This single buying transaction is represented with the following XML code.

``` xml
<transactions>
   <portfolio-transaction>
      <uuid>72bf2b32-60a5-4c99-ba6d-d3ab695624e5</uuid>
      <date>2023-09-10T00:00</date>
      <currencyCode>USD</currencyCode>
      <amount>174635</amount>
      <security reference="../../../../../../../../../securities/security"/>
      <crossEntry class="buysell" reference="../../../.."/>
      <shares>500000000</shares>
      <note>First buy on advice of ...</note>
      <units>
         <unit type="FEE">
            <amount currency="USD" amount="3000"/>
          </unit>
         <unit type="TAX">
            <amount currency="USD" amount="4500"/>
         </unit>
      </units>
      <updatedAt>2023-09-10T18:43:28.135529700Z</updatedAt>
         <type>BUY</type>
   </portfolio-transaction>
</transactions>

```

