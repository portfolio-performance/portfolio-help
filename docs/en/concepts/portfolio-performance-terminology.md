---
title: Portfolio Performance terminology
description: An alphabetical glossary of key terms and concepts used within Portfolio Performance, helping users better understand the application's fields, metrics, and functionalities.
changes:
    - date: 2025-05-03
      author: Nirus2000
      description:
        - Initial version of the "Portfolio Performance terminology" page.
        - Provides clear definitions of attributes, fields, and concepts used throughout the application.
todo: Holdings overview, Charts, Holdings, Performance, Calculation, Securities, Payments, Trades, Settings, Currencies
---

This page provides an overview of fundamental concepts and terminology used in **Portfolio Performance**. Core concepts such as accounts, transactions, reporting periods, acquisition prices, and performance are described in dedicated chapters (see sidebar). Below, you will find a glossary describing all attributes (also referred to as *fields* or *columns*) that appear throughout various sections of Portfolio Performance. You will also find explanations of transaction types and field value descriptions.

## Data Quality

These columns are found under `Securities` → `All Securities`:

- **Actual # Prices**: Number of stored historical prices.
- **Expected # Prices**: Number of expected historical prices, based on your calendar settings.
- **Missing # Prices**: The difference between stored and expected historical prices.
- **Date of Last Historical Price**: The date of the last downloaded historical price.
- **Date of First Historical Price**: The date of the first downloaded historical price.
- **Completeness of Historical Prices**: Describes the completeness of your historical price data. Minor deviations may arise due to regional holidays.
- **Absolute Performance**: A value-based metric that evaluates total profit or loss of an investment over a given period:  
`(Market value at end of period + Sales/Inflow + Dividends) - (Taxes + Fees + Starting value + Purchases/Inflow)`.  
Synonym: Total return.

## Master Data

The central hub for your accounts, securities accounts, savings plans, and an overview of all transactions is found in the navigation sidebar.

- **Accounts**: Store transactions related to business events or payment operations.
- **Securities Account (Depot)**: Contains the securities you currently own.
- **Reference Account**: The account used to settle transactions. For example, when buying a security, the depot value increases and the reference account is debited. Conversely, when selling, the depot decreases and the reference account is credited.
- **Savings Plans**: Overview of your savings plans, their execution intervals, and options to automate transactions.
- **Transactions**: A consolidated view of all transactions across accounts. The list can be filtered.

## Transaction Types

Commonly found in the context menu for accounts, depots, and securities.

- **Inbound Delivery**: Acquisition of a financial instrument without settlement via the reference account.
- **Outbound Delivery**: Sale of a financial instrument without settlement via the reference account.
- **Transfer**: Moves a security between depots. Creates an outgoing transaction in the source depot and an incoming transaction in the target depot.
- **Deposit**: Adds funds to Portfolio Performance for later use, e.g., to buy securities or monitor interest.
- **Withdrawal**: Removes funds or cash. Affects your portfolio’s performance.
- **Buy**: Acquires a financial product, debiting the reference account.
- **Sell**: Sells securities, crediting the counter-account.
- **Dividend**
- **Interest**
- **Interest Charge**
- **Taxes**: Payment to the government with no direct service in return.
- **Tax Refund**
- **Stock Split**
- **Fees**: Costs charged by service providers or brokers for executing transactions.
- **Fee Refund**

## Configurable Columns

- **Price Change (Period)**: Percentage difference between the last and first price over a chosen time span.
- **Price Change vs. Previous Day (Amount)** or **Δ Amount**: Absolute difference between the last retrieved price and the previous one.
- **Price Change vs. Previous Day (%)** or **Δ %**: Percentage difference between the last retrieved price and the previous one.
- **Price**: The last traded price of a security.
- **Distance to SMA (Days)**: The percentage difference between the current price and the simple moving average (SMA) over X days.
- **Distance from All-Time High (ATH)**: Indicates how far the current price is from the highest price within a specified period.
- **Acquisition Price**: The cumulative transaction value of all purchases (+) and sales (-) of a security within the reporting period.

## Securities

- **Currency**: The currency assigned to a security when created. Once a transaction is linked to a security, its currency cannot be changed.
- **Date**: The date of a transaction.

## Adding Stocks

- **Security**: A tradable financial instrument like stocks, bonds, cryptocurrencies, precious metals, etc.
- **Exchange**: A security may be traded on multiple exchanges (e.g., NVIDIA: NASDAQ [NVDA] or XETRA [NVD.DE]).
- **Name**: Initially taken from the data provider, but can be customized.

## Exchange Rates

- **Inactive**: A security can be marked inactive; it won't appear in transaction dialogs, and historical prices won’t update automatically.
- **ISIN (International Securities Identification Number)**: A unique 12-digit identifier used worldwide (especially by European brokers).
- **WKN (Wertpapierkennnummer)**: A 6-digit German identifier (largely replaced by ISIN).

## Deposits and Withdrawals

- **Deposit**: Adding funds to Portfolio Performance for later use, e.g., to purchase securities or monitor interest.
- **Withdrawal**: Removing funds or cash. This impacts the portfolio's performance.

## Dividends and Interest

- **Dividend**: Profit distribution from a company to its shareholders. This amount is credited to the reference account.
- **Interest**: Amount earned from capital investments (e.g., bonds or bank deposits).
- **Interest Charge**: Costs for borrowed capital (e.g., loan or credit interest).

## Taxes and Refunds

- **Taxes**: Payments made to the government without direct compensation.
- **Tax Refund**: Refund of taxes previously paid.

## Fees and Fee Refunds

- **Fees**: Costs charged by service providers or brokers for executing transactions.
- **Fee Refund**: Refund of previously paid fees.

## Purchases and Sales

- **Charge**: Total cost of a purchase transaction, including taxes and fees.
- **Proceeds**: Total amount realized from a sale transaction, minus taxes and fees. This amount is credited to the reference account.

## General

- **Note**: Allows adding comments to securities or transactions. Automatically filled when using the PDF importer but editable.
- **Units**: The number of securities you own. Decimal units are referred to as fractional shares.
- **Symbol (Ticker)**: Identifier of a security, often combined with an exchange code.
- **Target Currency**: Used to define conversion rates for currency exchanges.
- **Event**: Lets you document events, which are visible in charts and detailed views (e.g., stock splits).
- **Watchlist**: Create a customized list of securities with a configurable layout.
- **Widget**: Build your own dashboards with charts and metrics to analyze, compare, and evaluate your portfolio.
- **Exchange Rate**: Value of one currency relative to another.

## Price Providers

- **Price Provider (Historical)**: Data sources for historical prices (Alpha Vantage, Bitfinex, Binance, CoinGecko, EOD Historical Data, Finnhub, Eurostat HICP, ECB SDW, Kraken, PWP Leeway UG, Twelve Data, Quandl, Table from Website, VIA/CS Funds, Yahoo Finance, JSON, or none).
- **Price Provider (Current)**: Data source for current prices (same list as above). Alternatively, use "same as historical prices".
- **URL (Historical)**: The source URL for downloading historical prices.
- **URL (Current)**: The source URL for current prices.
- **Return**: Percentage change over a defined period.

## Risk Metrics

- **Risk Metrics**: Allow you to quantitatively assess the uncertainty of your investment (e.g., risk of total loss).
- **Maximum Drawdown**: The largest decline from a peak to a trough in portfolio value during a period.
- **Maximum Drawdown Duration**: The time between two portfolio peaks.
- **Semivolatility**: Indicator of downside risk (negative return deviations).
- **Volatility**: Indicator considering both positive and negative return deviations.

## General Data

- **Currencies**: Overview of ECB official exchange rates and a currency converter.
- **Settings**: Create custom attributes (additional columns) or bookmarks.

