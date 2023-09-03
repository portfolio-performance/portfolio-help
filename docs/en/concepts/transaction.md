---
title: Transaction types
---
<div style="float: right;">
<img src="../images/transaction-2023-06-23-10-27-29.png" alt="Transactions menu"  />
<figcaption> Figure 1: Transactions menu</figcaption>
</div>
A financial transaction is an agreement between a buyer and seller to exchange goods, services, or assets for payment. In case of PP, the exchange is about securities. Transactions are the core of PP. You can divide them broadly into security and deposit transactions (see figure 1).

- Security transactions are: buy, sell delivery (inbound), and delivery (outbound).
- Deposit transactions are: deposit, removal, interest, interest charge, fees, fees refund, taxes, tax refund.
- A dividend is a special transaction because it has both a security and deposit component.

Security transfer ... and Transfer between accounts ... are no real transactions but manual operations between accounts.

# Buy or Sell transaction
Figure 2 shows the input window to enter a simple buy transaction. The security (share-1) is quoted in EUR and the transaction is handled through an EUR deposit account. In figure 4 (sell transaction) a more complex situation is depicted. The security is quoted in USD but the transaction runs through a EUR deposit account.

## Buy

<img src="../images/transaction-2023-06-25a.svg" alt="Buying a EUR security" style="zoom:100%;" />
<figcaption> Figure 2: Buying a EUR security through a EUR deposit account</figcaption>

The minimum info that you should enter for a buying or selling transaction is:

  - Security: you can choose the security from the drop-down. If a particular security was already selected before the start of the transaction, this info is filled in. Please note that the currency is automatically set because each security has a currency associated with it.
  - Securities Account: choose with drop-down or already filled in, if you started from the Securities account.
  - Deposit Account: choose with drop-down or already filled in with the [account](/pp/account) of the security. If the currency of the deposit account is different from the security currency, then the Gross Amount and eventually Fees and Taxes (in the Security currency) have to be converted. So, you also need an Exchange Rate. See Figure 3 for an example.
  - Date of transaction: you can choose it from a calendar or enter it manually. With the field to the right (00:00), you can set the time. A 12 or 24 hours clock is set with menu Help > Preferences > Language > Country.
  - Shares: the number of securities that you buy or sell. This can be a decimal number.
  - Debit Note: this is the amount that you have to pay or receive as a result of this transaction. Other names are: Value or Net Value.

So, number of shares and debit note are sufficient. In this case, the gross value is the same as the debit note. So, the quote price could be calculated (gross value / shares).

The normal flow however is probably: shares * quote (price) >> gross value + fees + taxes >> debit note. There are a few peculiarities if you change something afterwards (see figure 3)


<img src="../images/transaction-2023-06-25b.svg" alt="Calculation flow" style="zoom:100%;" />
<figcaption> Figure 3: Calculation flow between Shares & Debit Note</figcaption>

-  Changing the debit note (afterwards) will change the Gross value and as a result of that also the quote price. The number of shares is untouched.
- Changing the Gross Value afterwards, will change the Debit note and the Quote Price. Fees and taxes and the number of shares is again untouched.

## Sell
For the Sell transaction we use an USD security that is cashed in an EUR deposit account. Three new fields appear upon selecting the EUR account: exchange rate, USD fees and USD taxes.

<img src="../images/transaction-2023-06-25c.svg" alt="Selling a USD security" style="zoom:100%;" />
<figcaption> Figure 4: Selling a USD security through an EUR deposit account</figcaption>

The quote is noted in USD and therefore automatically also the first Gross Value. 
Because, you want to cash this transaction in an EUR account, this USD value must be converted. From the moment, you select a deposit account with a different currency, the exchange rate field (XR) is populated with the correct rate for that date and currency. The website of the European Central Bank (ECB) is consulted for this. See menu View > Currencies > Currency Converter.

Changing dates later on will change the XR appropriately, even if you have entered manually an XR. So, setting the transaction date first is good practice.

You can enter fees and taxes in both currencies. The foreign fees and taxes will of course be converted using the same XR. There is no subtotal in local currency. So, the Credit Note is not a simple addition of the numbers above.

The calculation flow remain the same as in figure 3. For example, changing the Credit Note will change the Gross Value in EUR, which will change the Gross Value in USD (XR remains untouched), which will change the Quote price.

# Dividend transaction
Booking a dividend is almost like a buy or sale; except that the quote price is replaced with a field Dividend payment per shares (see figure 5)

<img src="../images/transaction-2023-06-25d.svg" alt="Booking a USD security" style="zoom:100%;" />
<figcaption> Figure 5: Booking a USD security dividend through an EUR deposit account</figcaption>

There is no separate function to book a "Dividend Investment Plan" (DRIP). One solution is to fully book all dividends with a buy transaction of the agreed-upon number of shares. More information at [Reinvesting dividends](/pp/reinvesting-dividends).
