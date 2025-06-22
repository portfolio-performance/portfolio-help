---
title: Request for a new PDF importer
description: Step-by-step guide on how to request a new PDF importer for Portfolio Performance, including how to collect, anonymize, and submit sample PDF transaction documents.
changes:
    - date: 2025-05-18
      author: Nirus2000
      description:
        - Adding YAML Source
        - Closes #129
        - Update instructions
---

# Request for a New PDF Importer

If Portfolio Performance doesn't have a PDF importer for your bank or broker, or for the specific type of transaction you need, you can request the development of this importer. Since Portfolio Performance developers don't have access to every bank or broker, you — as a user — must provide some sample PDF documents with **real** but **anonymised** examples of transactions with that specific bank or broker.

The following text outlines all the necessary steps. You can also watch the [accompanying video](#video-tutorial) at the bottom.

---

## Step-by-Step Guide

### 1. Collect a PDF Document

Collect a **PDF document** of each transaction that you would like to import into your Portfolio Performance portfolio. Ideally, you should provide an example of a **buy**, **sell**, and **dividend** transaction.

!!! Failure
    Don't use PDFs that are converted to PDF from a browser or self-scanned paper notes — only the **original documents** from the bank or broker are suitable.

---

### 2. Convert These PDFs to Text

Use the parser from PP, which can be found at:

`File > Import > Debug: Extract Text from PDF`

Figure: Menu File > Import {class="pp-figure"}

![Menu File Import](./images/mnuFile-import-debug.png)

You can use [this sample (fictitious) PDF document](../assets/SelfwealthBuy01.pdf) for testing. The extracted text will appear in the textbox below the instructions:

Figure: Extracted text from test PDF {class="pp-figure"}

![Extracted Text](./images/pdf-import-extract-text.png)


---

### 3. Anonymise Personal Information

Replace (anonymise) personal information in the extracted text, such as:

- your name
- your address
- your account number

You can do this by double-clicking on a word (e.g., your name). The text will be selected and replaced with random characters.

!!! Warning
    Personal info may occur at multiple places within the document.

Leave **all other information intact**, especially:

- amounts
- dates
- security names

**Important:** The following strings cannot be anonymised automatically and must be left unchanged:

- currencies (e.g. `EUR`)
- ISIN
- text containing: hyphen (`-`), period (`.`), comma (`,`), colon (`:`), apostrophe (`'`), slash (`/`)

!!! Danger
    Do **not** delete or add anything manually.

---

### 4. Copy or Save the Anonymised Text

Copy the anonymised text to the clipboard or save it to a text file — you will need this later when submitting your request.

---

## 5. Submit Your Request

### 5a. In the Forum

If there isn’t already an importer for your needs:

- Create a new thread in the [Portfolio Performance forum](https://forum.portfolio-performance.info/c/english/16) named:

  ```
  PDF Import from [your bank or broker]
  ```

- If an existing thread already matches your bank, post a reply instead. Example: [PDF import from SelfWealth](https://forum.portfolio-performance.info/t/pdf-import-from-selfwealth/17399)

- Add the anonymised, extracted text for each transaction type (buy/sell/dividend) separately.

Wrap the text in **triple quotes** so that it's properly formatted as code:

<pre>
```
Your extracted PDF debug ...
```
</pre>

!!! Note
    Is automatically inserted when extracting

!!! Tip
    If your transaction is in a foreign language, provide a translation or short explanation of the used terms.

---

### 5b. On GitHub

You can also report PDF debug output directly via GitHub:

- Go to the [GitHub issue form](https://github.com/portfolio-performance/portfolio/issues/new?template=pdf_report.yml)
- Fill out the form **completely**, and attach the anonymised extracted text.

---

## 6. Wait for a Reply

A developer will respond to your request. Once the importer is ready, it will be included in one of the upcoming Portfolio Performance updates.

---

# Video Tutorial

<video width="100%" controls>
  <source src="../../assets/videos/request-importer/PP-request-importer.mp4" type="video/mp4">
</video>
