---
title: Save - Save As - Save All
---

# File &rsaquo; Save - Save As - Save All

## Save

Figure: File format picker.{class=align-right style="width:20%"}

![](./images/pick-file-format.png)

With the menu `File > Save`, you can save your portfolio, using its existing name and file format without any further interference. If the file hasn't been saved before, a `Pick the file format` dialog box will appear (see Figure 1), presenting three choices. These options will be explained in the subsequent section. After selecting the file format, you can proceed as if you had started with the `File > Save As` option from the menu.

## Save As

The `File > Save As` option offers the three file format choices as submenus. In the subsequent step, you can input the file name and designate the file location. This option allows you to create a new copy of a previously saved file in a different file format and/or with a different name, leaving the original file intact.

## Save All

If more than one portfolio is open, the aforementioned commands will solely save the active portfolio. Utilize the `Save All` option to save all open files simultaneously. 

Figure: Dialog after closing app with two updated portfolios.{class=pp-figure}

![](./images/app-close.png)

Closing a portfolio that has been modified since opening will trigger a dialog `'xxx.xml is modified. Do you want to save the changes?`. Closing the application with multiple updated projects will prompt the dialog from Figure 2.

## XML format

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

Below you can see the xml code for the buying transaction in Figure 3.

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
As you can see, there is nearly a one-to-one relationship between the input form of the buy transaction and the XML. Please note that -internally- PP works with nano units (10^9) for the number of shares and hecto units (10^2) for the price.

The PortfolioPerformance mobile app, introduced in February 2024, does not support the XML file format.


## Password protected (AES-256)

AES-256 encryption is a method of securing your data by converting it into a code that can only be accessed with a unique key. This encryption technique uses a 256-bit key, which is a string of 256 zeros and ones, to encrypt and decrypt the data. When data is encrypted using AES-256, it is transformed into a random sequence of characters that is unreadable without the key. In order to generate this key, PP needs a password that is at least 6 characters. However, a password that is longer and more complex will have more randomness and unpredictability, which means it is harder to guess.

Figure: Saving a portfolio with AES-256 encryption needs a password.{class=pp-figure}

![](./images/mnu-save-encrypted.png)


## Binary

An XML file is a human-readable file format (see above for an example). A binary format is more compact and efficient and therefore a file can be opened and saved much faster. However, it is no longer human-readable. More info is available in [Issue #2363](https://github.com/portfolio-performance/portfolio/issues/2363); watch for example the comparison in opening speed of a 720 securities & 1.3 MB historical prices project.

Distinguishing a password-protected or binary file from a regular XML file one is possible by examining the file extension. Encrypted and binary files have the extension .portfolio instead of XML.