---
title: Alpha Vantage
---

Alpha Vantage bietet Echtzeit- und historische Kursdaten über APIs und Tabellen. Du kannst einen [kostenlosen API-Schlüssel] (https://www.alphavantage.co/support/) anfordern, der die meisten Datensätze für bis zu 25 Anfragen pro Tag abdeckt. Echtzeit-Kurse und andere Daten sind jedoch kostenpflichtig.

Die [API-Dokumentation](https://www.alphavantage.co/documentation/) ist sehr gut beschrieben und enthält viele Beispiele. Diese Beispiele können im Browser mit einem mitgelieferten Demo-API-Schlüssel ausgeführt werden. Wenn du deine eigenen Abfragen ausführen möchtest, benötigst du einen persönlichen API-Schlüssel.

Herunterladen der historischen NVIDIA-Preise.

'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NVDA&apikey=my_API_key'

Die Antwort enthält einige Metadaten und die letzten 100 historischen Kurse, die im Browserfenster angezeigt werden. Wenn du alle verfügbaren historischen Kurse haben möchtest, verwende die Option "outputsize=full".

```
{
    "Meta Data": {
        "1. Information": "Daily Prices (open, high, low, close) and Volumes",
        "2. Symbol": "NVDA",
        "3. Last Refreshed": "2024-01-25",
        "4. Output Size": "Compact",
        "5. Time Zone": "US/Eastern"
    },
    "Time Series (Daily)": {
        "2024-01-25": {
            "1. open": "623.5000",
            "2. high": "627.1900",
            "3. low": "608.5000",
            "4. close": "616.1700",
            "5. volume": "48277684"
        },
        "2024-01-24": {
            "1. open": "603.0400",
            "2. high": "628.4900",
            "3. low": "599.3800",
            "4. close": "613.6200",
            "5. volume": "55706870"
        }
    }
}

```

!!! Note

    As of January 2024, Alpha Vantage changed some parameters and PP's JSON Quote Feed is no longer functional for this URL. The `Path to Date` and `Path to Close` JSON paths below result in an error; even if they are, according to the [JSONPath Online Evaluator](https://jsonpath.com/)a valid JSON path.

    - Path to Date: `$.[Time Series (Daily)].*~`
    - Path to Close: `$.[Time Series (Daily)].[*].[4. close]`



