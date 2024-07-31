---
title: Keeping the portfolio up-to-date
---

The synchronisation between your physical and digital (PP) portfolio is crucial for making informed decisions. The status of your physical portfolio —such as market value, balance total, and cash flows— should mirror your digital (PP) portfolio to ensure accurate decision-making. For instance, the rebalancing feature (see [previous section](./rebalancing.md)) provides suggestions to buy or sell stocks based on the recorded holdings in your digital portfolio.

After making physical transactions with your broker or bank, you need to update your PP portfolio. This can be done manually or automatically:

- **Manual Update**: You create transactions in PP based on the information from your bank or broker. Refer to [Reference > Transaction Menu](../reference/transaction/index.md) for details about all available transactions.
  
- **Automatic Import**: You can import transaction data from your bank automatically. Depending on the format, this can be done using PDF documents or CSV files. It is very important that the structure and format of your data match the required format from the import wizard. For example, your CSV file might use a semicolon as a list separator (common in European countries). The import wizard should match this setting.

  - **Importing a CSV File**: Use the menu `File > Import > CSV files (comma-separated values)` to import historical quotes, accounts, securities, and transactions. See [Reference > File > Import](../reference/file/import.md#csv-files-comma-separated-values) for further information.
  
  - **Importing PDF Documents**: Banks and brokers often provide account statements on paper or in PDF format. PP can read PDF documents from more than 90 banks or brokers. To verify if your bank is supported, try to import a PDF document. The import wizard will either recognise it automatically or display an error message listing all the banks/brokers it has tried. You can also search the [forum](https://forum.portfolio-performance.info/c/english/) using the term `PDF import` or `PDF import [name-of-your-bank-or-broker]` to see if an importer for your institution is available or if there are any issues with it. See [Reference > File > Import > PDF Bank Documents](../reference/file/import.md#pdf-bank-documents) for further information, including how to request a new importer for your bank.
