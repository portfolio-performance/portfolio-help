---
title: Importing Interactive Brokers Flex Queries
---

Interactive Brokers allows clients to export account activity as an XML file.

## Creating an Activity Flex Query

You need to create a Flex Query for Portfolio Performance before being able to export data for the first time. See [Create an Activity Flex Query](https://www.ibkrguides.com/clientportal/performanceandstatements/activityflex.htm) at Interactive Brokers on how to create a new query.

Here are the necessary parameters:

- Select at least the following _Sections_ ("Select All" rows unless noted otherwise).
  - Account Information (select Account ID, Account Alias and Currency)
  - Cash Transactions
  - Corporate Actions
  - Sales Tax Details
  - Trades
- Change "Include Currency Rates?" to "Yes" under "General Configuration".

## Importing from an Activity Flex Query

Run the previously created Flex Query, see [Run a Flex Query](https://www.ibkrguides.com/clientportal/performanceandstatements/runflex.htm) at Interactive Brokers on how to do this.

In Portfolio Performance, use `File > Import > Interactive Brokers: Activity Flex Query` and select the XML you've just downloaded.

Note that you can import transactions from multiple Interactive Brokers accounts at the same time by changing the Flex Query to include multiple accounts via "Delivery Options", "Accounts".

### Automatically matching Interactive Brokers accounts to securities accounts

Interactive Brokers accounts have an ID like U1234567, which is not particularly memorable. The importer will therefore also consider the account alias when trying to match a transaction to a securities account.

For example, an Interactive Brokers account with ID U4242424 and alias "Hotblack Desiato" will match a securities account named either "U4242424" or "Hotblack Desiato".

### Handling transactions in multiple currencies

A single Interactive Brokers account has multiple foreign currency balances, but Portfolio Performance only supports a single reference account per securities account. The importer uses a rule of thumb to allow matching transactions in foreign currency to the correct deposit accounts.

The rule is that any deposit account which starts with the name of the reference account is considered a candidate. For example, if the reference deposit account is called "IB" accounts called "IB EUR", "IB CHF" match the rule of thumb.
