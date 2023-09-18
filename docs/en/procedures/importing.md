---
title: Importing a CSV-file
lastUpdate: 2023-09-05
---
In PP you can enter your transactions (buy, sell, dividends, … ) manually but you can also *import* those transactions from a CSV file (comma-separated values) or from a PDF document. Not all brokers, however, provide the format that PP needs. So, how should this CSV-file look? Suppose, you want to import the following transaction.

![Buying transaction example for import](images/import-buy-transaction.png){.pp-figure}

As you can see in figure 1, the following PP fields are  used: Security Name (share-2), the implied currency (USD), Securities Account (Broker-A), Deposit Account (Broker-A (EUR), Date & time, number of Shares (10), buying quote (5 USD), Gross Amount in USD (50), Exchange Rate (1.0785 EUR/USD), Gross Amount in EUR(46.36), Fees USD and EUR), Taxes (USD and EUR), Value or Debit Note (55.21), and a note (My Note). You don't have to provide all fields in the CSV-file; some of them aren't even possible e.g. implied currency and fees/taxes in the foreign currency.

With the menu `File > Import > CSV files (comma-separated values)` you can import all kind of transactions. A CSV file is simply a text file. The first line contains the names of the fields (columns); separated by commas. The second and following lines contain the data, also separated by commas. For example, the following print-out of a CSV-file contains three fields or columns and two lines of data.

```
Name,Type,Date,Value
Share-1,dividend,2023-05-21,1500
Share-2,buy,2023-06-01, 20
```

PP distinguishes between 5 types of import: Account Transactions, Portfolio Transactions, Securities, Historical Quotes, and Securities Account (see figure 2). To correctly use a type and import the data into PP, the CSV file must contain specific fields. Depending on the type of account, there are other required and optional fields.

![Import dialog window with the 5 types](images/import-types.png){.pp-figure}

The difference between each type is rather nebulous and not very good documented. The following definitions are tentative.

  + Account Transactions: will be used to register transactions within one account; for example the payment of a dividend (?)

  + Portfolio Transactions: for transactions between accounts. For example, the buying of a share involves adding shares to the Securities account and reducing the associated deposit account with money.

  + Securities: you can use this type to create securities in the All Securities account without also adding a transaction.

  + Historical Quotes: to create a table of historical quotes for a security.

  + Securities Account: with this type, you can create new securities within the All Securities account and at the same time a buy transaction in the All Transactions account.

Each type has required and optional fields. For example, the Historical Quotes type only needs the Date and the Quote. Instead of repeating the name of the share again and again for each date, you can select the security in the next pop-up window. The Account Transactions type has two required Fields: Value and Date. The Portfolio Transactions has three required fields: Value, Date, and Shares (see figure 3).

![Required and optional fields for the 5 types of import](images/import-required-optional-fields.png){.pp-figure}


## Importing buy/sell transactions
An easy way to discover which fields you need, is to export a demo transaction first. After selecting the transaction in All Transactions, click the Export button at the top-right of the window (up-pointing arrow). Choose “Selected transactions (CSV)”. If you should open this CSV-file with a text editor, it will look something like this:

```
Date,Type,Security,Shares,Quote,Amount,Fees,Taxes,Net Transaction Value,Cash Account,Offset Account,Note,Source
2023-05-25 00:00:00,Buy,share-2,10,5.50,55.00,4.10,6.20,65.30,Broker-A,Broker-A (EUR),My Note,
``` 
The first line contains the field names, separated by a comma. The second line contains the value of those fields. Notice that there is no value for the field Source. *Unfortunately*, the field names do not match with the required field names for the import nor with the labels used in the dialog box (e.g. Name vs Security Name, Net Transaction Value vs Value). Also, a new field is added (Type) but worse, a necessary field (Exchange Rate) is missing. Also, USD and EUR fees and taxes are added into a total amount in EUR.

Importing this transaction again (after deleting the original one) *will fail*.

In order to recreate the transaction of figure 1, you need at least the following fields. Restoring the split between USD and EUR fees and taxes seems to be impossible. You have to use the Portfolio Transactions type.

```
Date,Type,Security Name,Shares,Fees,Taxes,Value,Exchange Rate
2023-05-25 0:00,Buy,share-2,10,4.1,6.2,65.30,0.9091
```

 

## Importing dividends

![Dividend transaction example for import](images/import-dividend-transaction.png){.pp-figure}


Suppose that your broker can deliver a CSV-file with all the dividend payments from a past period. Of course, you would like to import this file in stead of entering manually all these dividend payments. The file content looks something like this (see figure 1 below).

![CSV table for importing two dividends](images/import-dividend-csv-table.png){.pp-figure}

Unfortunately, this is not enough information to use the Import CSV-function. From the three available columns of the CSV-file, two of them are recognized by PP: ISIN and Date (see figure 6). For the column Payment, you have to map this field to one of the PP fields. Because, it is a dividend you need to use the import type Account transactions. A dividend payment is a simple deposit transaction, which has no implications on the securities account.

According to the pop-up message of figure 6, there are two required fields: Date and Value, of which the last one is unmapped. This is because the name that your broker uses (Payment) is different from the required name (Value). You can however, double click on the Payment column to choose the correct field name.

![Dialog box for importing dividends](images/import-CSV-dialog.png){.pp-figure}


But how is PP able to recreate a dividend payment with only these two fields (date, value). It can't! You can only use this import to create a deposit in a Security and Cash account. If you want to create a dividend, you should also specify a type: Dividend. Specifying a number of shares or fees/taxes will also do the job.

Of course, PP does also need the name of the Cash and Securities account. You can enter this in the next step of the wizard or you can specify it in the CSV-file.

Let's take a simplified example (EUR-dividend in a EUR-cash account; see figure 7). The minimal info to register this dividend is:

```
type, Date, ISIN, Value
dividend, 2022-01-01, BE0974258874, 40
```

    + This will result in the following "dividend" transaction.

![Simplified buying transaction example for import](images/import-buy-transaction-simplified.png){.pp-figure}

Adding Fees and Taxes will calculate the Gross Amount. You cannot specify the Gross Amount in itself. Adding the number of Shares will calculate the dividend payment/share. It is also not possible to specify this in itself. So, a typical CSV-file for a dividend payment in the currency of the Cash account will look like:

```
Type, Date, ISIN, Value, fees, taxes, shares
dividend, 2022-01-01, BE0974258874, 200, 3, 2, 25
```
