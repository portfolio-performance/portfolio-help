---
title: EODHD
---

Die Website [EODHD](https://eodhd.com/) (End of Day Historical Data) bietet umfassende Informationen über alle US-Aktien, ETFs und Investmentfonds. Darüber hinaus umfasst die Plattform historische Daten für nicht US-Börsen, die hauptsächlich bis zum 3. Januar 2000 zurückreichen.

Ein [kostenloser API-Token](https://eodhd.com/register) kann einfach durch Angabe Deiner E-Mail-Adresse angefordert werden. Der Token ist beschränkt auf 20 API-Anfragen pro Tag. Es können jedoch nur historische Kurse aus dem letzten Jahr abgerufen werden.

Du kannst den API-Token mit der automatischen Kursabfrage von Portfolio Performance nutzen. Füge den Token in den Einstellungen ein (Hilfe > Einstellungen > API-Schlüssel) und wähle EOD Historical Data als Kurslieferant.

Wenn Du spezielle Anforderungen hast, dann kannst Du auch die JSON Kursabfrage verwenden (siehe [API Dokumentation](https://eodhd.com/financial-apis/api-for-historical-data-and-volumes/) für einige Anwendungsfälle). Die folgende Anfrage ruft zum Beispiel die historischen Apple-Kurse des **Monats Januar 2000** ab.

*Kurs URL*

`https://eodhd.com/api/eod/AAPL?from=2000-01-01&to=2000-01-31&period=d&api_token=demo&fmt=json`

*Pfad zu Datum* = `$[*].date` und *Pfad zu Kurs* = `$[*].close`

Gibst Du die Adresse in einen Browser ein, erhältst Du folgendes (gekürztes) JSON.

```
[
    {
        "date": "2000-12-01",
        "open": 17.0016,
        "high": 17.5,
        "low": 16.8112,
        "close": 17.0632,
        "adjusted_close": 0.2583,
        "volume": 385705600
    },
    {
        "date": "2000-12-04",
        "open": 17.1864,
        "high": 17.1864,
        "low": 16.436,
        "close": 16.688,
        "adjusted_close": 0.2526,
        "volume": 371520800
    },
    {
        "date": "2000-12-05",
        "open": 16.94,
        "high": 17.4384,
        "low": 16.3744,
        "close": 17.0016,
        "adjusted_close": 0.2574,
        "volume": 613978400
    }
]
```

Hierbei handelt es sich um ein Array von Objekten, auf das von der Basis mit `$[*]` zugegriffen wird. Der JSON-Pfad zum Datum wird mit `$[*].date` und zum Schlusskurs mit `$[*].close` gebildet.

