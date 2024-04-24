---
title: Kursdaten laden
---

# Kursdaten laden

Historische Kurse sind extrem wichtig um eine Performance berechnen zu können. Wenn man nicht weiß wieviel ein Wertpapier vor einem Jahr wert war, dann helfen auch schicke Formeln nicht weiter. Allerdings ist es nicht einfach an gute und gleichzeitig kostenlose historische Kurse heranzukommen.

Die erste Anlaufstelle ist [Yahoo Finance](#yahoo-finance): sofern Yahoo Finance das Wertpapier kennt und auch Kurse hat, kann man bequem anhand des Tickers den Download direkt in *Portfolio Performance* konfigurieren. Allerdings ist die Abdeckung für deutsche Fonds oder ETFs nicht so prickelnd. Eine weitere Möglichkeit ist [AlphaVantage](#alphavantage): ebenfalls mit viel Gewicht auf den amerikanischen Markt. Allerdings erlaubt das kostenlose API nur wenige Aufrufe pro Minute.

Wenn diese zwei automatischen Quellen keine historischen Kurse bieten, muss man zu "halbautomatischen" Lösungen greifen. Die erste Möglichkeit ist eine URL zu hinterlegen auf der nach einer [Tabelle mit Kursinformationen](#tabelle-auf-einer-webseite) gesucht wird. Neben der Schwierigkeit überhaupt die passende Seite zu finden, kann es auch sein, dass die URLs sich immer wieder ändert so dass man mit Markos [dynamische Kursdaten-URLs](#dynamische-kursdaten-urls) zusammenbauen muss.

Und schließlich bleiben die manuellen Lösungen: die Kursdaten [per CSV-Datei](#comman-separated-values-csv) zu importieren oder manuell im Programm selbst zu erfassen.

[<i class="fa fa-comments-o" aria-hidden="true"></i> Forum: Quellen für historische Kurse](https://forum.portfolio-performance.info/t/quellen-fuer-historische-kurse/46)

## Comman-separated Values (CSV)

[CSV](https://de.wikipedia.org/wiki/CSV_(Dateiformat)) steht für *Comma Separated Values*, also Werte die durch ein Komma getrennt werden.

### Allgemeines

Falls historische Kurse vorliegen, können sie einfach als CSV-Datei importiert werden. Dazu die Daten in einer Tabelle auflisten, die einzelnen Werte durch ein Komma, Tabstopp oder besser Semikolon trennen und als CSV-Datei speichern. Bei Kurswerte im Format EURO,Cent verbietet sich der Komma-Separator.

![grafik](https://user-images.githubusercontent.com/82599585/116431429-134f2e00-a848-11eb-937a-8bdb0ab967ef.png)

Dazu eignet sich ein Tabellenkalkulationsprogram bestens, so dass man sich nicht um die weitere Formatierung kümmern muss.

![grafik](https://user-images.githubusercontent.com/82599585/116431458-1a763c00-a848-11eb-994b-dfb4a472f721.png)

Dann wird die Datei als CSV-Datei gespeichert.

![grafik](https://user-images.githubusercontent.com/82599585/116431530-28c45800-a848-11eb-9084-4576d0af24cd.png)

### CSV Daten importieren

Mit Rechtsklick auf das Wertpapier --> Kurse --> CSV-Datei importieren das CSV-Import Fenster öffnen.

![grafik](https://user-images.githubusercontent.com/82599585/116431840-6e812080-a848-11eb-95ed-f2c1c3e9e7dc.png)

Portfolio Performance zeigt nun grün hinterlegt, welche Spalten als Datum und Kurs identifiziert wurden. Ein Häckchen zeigt ob eine Spaltenüberschrift vorhanden ist.

![grafik](https://user-images.githubusercontent.com/82599585/116431887-79d44c00-a848-11eb-8a40-dd845bd7830e.png)

Mit Doppelklick auf die entsprechende Stelle kann die Spaltenzuteilung geändert werden. Werden mehrere Kursspalten ausgewählt, wird der Wert der Letzten? eingelesen.

![grafik](https://user-images.githubusercontent.com/82599585/116431930-83f64a80-a848-11eb-873a-10df00c85ca8.png)

Ein Klick auf ok und die Daten sind sichtbar.

![grafik](https://user-images.githubusercontent.com/82599585/116431984-8fe20c80-a848-11eb-823f-4af73b74ec4e.png)

Daten, die von online Seiten stammen bereiten mitunter Enkodierungs-Probleme. Dann kann das Format nicht gelesen werden. Abhilfe schafft hier der Versuch die Enkodierungseinstellung zu ändern. UTF-8 ist neben windows-1252 ein gängiges Format.

![grafik](https://user-images.githubusercontent.com/82599585/116432053-9d979200-a848-11eb-93d7-ef3e288a87d3.png)

## Yahoo Finance

## AlphaVantage

## Tabelle auf einer Webseite

## JSON

Der Kurslieferant *JSON* kann mit Hilfe von [JsonPath](https://github.com/json-path/JsonPath/blob/master/README.md) Ausdrücken aus einem JSON (JavaScript Object Notation) Dokument Kurse extrahieren.

Es müssen zwei JsonPath Ausdrücke konfiguriert werden: **Pfad zum Datum** und **Pfad zum (Schluss)kurs**. Beide Ausdrücke müssen ein Array zurückgeben. Die Arrays müssen die gleiche Länge habe, d.h. zu jedem Datum gibt es auch einen Kurs und umgekehrt.

Die [URL darf Makros](#dynamische-kursdaten-urls) enthalten.

### Beispiele

Nehmen wir an die konfigurierte URL liefert folgendes JSON Dokument:

```json
{
    "isin": "IE00B3WJKG14",
    "totalCount": 2,
    "tradedInPercent": false,
    "data": [
        {
            "close": 10.336,
            "date": "2020-03-05",
            "high": 10.392,
            "low": 10.114,
            "open": 10.392,
            "turnoverEuro": 8039993.78,
            "turnoverPieces": 781747
        },
        {
            "close": 10.292,
            "date": "2020-03-04",
            "high": 10.374,
            "low": 10.172,
            "open": 10.224,
            "turnoverEuro": 4737489.8,
            "turnoverPieces": 461168
        }
    ]
}
```

Der Pfad zum Datum **$.data[*].date**. '$' steht für das Wurzelelement, mit der Wildcard '*' werden alle Einträge aus dem Array eingesammelt.

Als Schlusskurs verwenden wir das **close** Attribut und damit den Pfad **$.data[*].close**.

Ein zweites Beispiel sind die [LBMA/GOLD](https://www.quandl.com/data/LBMA/GOLD-Gold-Price-London-Fixing) Kurse von Quandl. Da es einen separaten [Quandl Kurslieferant](#quandl) gibt, kann man Kursinformationen von Quandl natürlich einfacher konfigurieren. Es dient hier als Beispiel für ein weiteres JSON.

```json
{
    "dataset": {
        "collapse": null,
        "column_index": null,
        "column_names": [
            "Date",
            "USD (AM)",
            "USD (PM)",
            "GBP (AM)",
            "GBP (PM)",
            "EURO (AM)",
            "EURO (PM)"
        ],
        "data": [
            [
                "2020-03-05",
                1647.45,
                1659.6,
                1274.47,
                1284.7,
                1474.63,
                1482.69
            ],
            [
                "2020-03-04",
                1644.8,
                1641.85,
                1286.73,
                1281.63,
                1475.06,
                1477.83
            ]
        ],
        "database_code": "LBMA",
        "database_id": 139,
        "dataset_code": "GOLD"
    }
}
```

**$.dataset.data[*][0]** extrahiert das Datum.

**$.dataset.data[*][6]** extrahiert das 7. Element (JsonPath fängt mit 0 an zu zählen). Von den **column_names** Attribut wissen wir, dass das 7. Element als **EURO (PM)** bezeichnet ist, also das Nachmittags Fixing in Euro.

Der Entwickler von JsonPath hat eine [kleine Anwendung](http://jsonpath.herokuapp.com) gebaut, mit der man interaktiv die JsonPath Ausdrücke testen kann. Die Anwendung scheint keine großen JSON Dokumente zu vertragen, darum macht es Sinn mit nur ein paar wenigen Kursen die Ausdrücke zu testen.

## Dynamische Kursdaten-URLs

Manche Seiten verteilen die Daten auf mehrere Requests. Wenn eines der Macros in der URL gefunden wird, wird die URL dynamisch zusammengesetzt und *Portfolio Performance* macht solange Aufrufe bis keine weiteren Kurse mehr gefunden werden.

In einer URL dürfen mehrere Marcos verwendet werden. Allerdings dürfen ```DATE``` und ```PAGE``` nicht gemeinsam verwendet werden, weil beide unterschiedliche Iterationen von URLs generieren.

[<i class="fa fa-comments-o" aria-hidden="true"></i> Forum: Dynamische Kursdaten-URLs](https://forum.portfolio-performance.info/t/dynamische-kursdaten-urls/2929/1)

#### CURRENCY

```CURRENCY``` ersetzt das dreistellige ISO Währungskürzel des Wertpapiers in der URL.

```
https://example.com/data?waehrung={CURRENCY}
```

#### DATE

```DATE:<format>``` generiert eine Abfrage für jedes Datum mit dem angegebenen Format, und zwar

* wenn **keine** Kurse existieren, wird vom aktuellen Datum rückwärts in die Vergangenheit gesucht solange bis keine Kurse mehr gefunden werden;
* wenn historische **Kurse existieren**, dann wird vom letzten Kursdatum vorwärts bis zum aktuellen Datum eine URL generiert.

Das Datumsformat folgt den Regeln des [DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html) aus Java. Die wichtigsten Symbole sind ```y``` für das Jahr, ```M``` für den Monat im Jahr und ```d``` für den Tag im Monat.

Beispiele:

```
https://example.com/data?month={DATE:yyyy-MM}
https://example.com/data?datum={DATE:yyyy-MM-32}
```

Wenn die identische URL mehrfach generiert wird, dann macht *Portfolio Performance* nur eine einzige Abfrage. Nehmen wir das Datumsformat aus dem letzten Beispiel: ```{DATE:yyyy-MM-32}``` Der Tag ist statisch auf 32 gesetzt. Es wird für jeden Tag in einem Monat die identische URL generiert, aber nur eine Abfrage zum Server gemacht.

Das Marco ```DATE``` darf in einer URL mehrfach auftauchen. Es wird dann das gleiche Datum verwendet. So kann man zum Beispiel mit ```{DATE:yyyy-MM-01}``` und ```{DATE:yyyy-MM-31}``` vom Monatsersten bis zum Monatsletzten selektieren.

!!! tip "Tipp"
    Warum den 32. und nicht den 31. als letzten Tag? [Al2Klimov](https://forum.portfolio-performance.info/t/dynamische-kursdaten-urls/2929/10) schreibt dazu im Forum: *Aus eigener Erfahrung u.a. als Berufsprogrammierer kann ich dieses “Ausreiz-Prinzip” vielerseits empfehlen: Entweder es fährt alles “gegen die Wand” (den 32. Monatstag gibts so nicht) oder alles funktioniert – aber bitteschön kein inkonsistenter Zustand dazwischen!*

!!! warning "Warnung"
    Mit dem Datumsformat ```yyyy-MM-dd``` wird für jeden Tag eine URL generiert und damit eine ganze Menge Abfragen gemacht. Das sollte man nach Möglichkeit vermeiden. Der Server könnte das als Fehlanwendung verstehen und überhaupt keine Daten mehr liefern.

#### ISIN

```ISIN``` ersetzt die ISIN des Wertpapiers in der URL.

```
https://example.com/data?isin={ISIN}
```

#### PAGE

```PAGE``` fängt mit 1 an zu zählen bis keine weiteren Kurse mehr auf der Seite gefunden werden.

```
https://example.com/data?page={PAGE}
```

#### TICKER

```TICKER``` ersetzt das Ticker Symbol des Wertpapiers in der URL.

```
https://example.com/data?ticker={TICKER}
```

#### TODAY

```TODAY:<format>:<delta>``` ersetzt das aktuelle Datum in der URL.

* ```<format>``` ist das Datumsformat nach den Regeln des [DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html) aus Java. Die wichtigsten Symbole sind ```y``` für das Jahr, ```M``` für den Monat im Jahr und ```d``` für den Tag im Monat.
* ```<delta>``` ist eine Zeitspanne basierend auf den ISO-8601 Regeln wie in [Java](https://docs.oracle.com/javase/8/docs/api/java/time/Period.html#parse-java.lang.CharSequence-) implementiert. Die Zeitspanne kann optional mit einem Minuszeichen beginnen - dann wird sie vom aktuellen Datum abgezogen. Dann folgt ein ```P``` (für period) und anschliessend eine Zahl und ein Suffix - z. B. einem ```Y``` für Jahre, ```M``` für Monate, ```W``` für Wochen und einem ```D``` für Tage.

```
// aktuelles Datum im ISO Format
https://example.com/data?datum={TODAY}

// aktuelles Datum im deutschen Datumsformat
https://example.com/data?datum={TODAY:dd.MM.yyyy}

// aktuelles Datum minus 1 Jahr
https://example.com/data?datum={TODAY:dd.MM.yyyy:-P1Y}

// aktuelles Datum minus 2 Monate
https://example.com/data?datum={TODAY:dd.MM.yyyy:-P2M}
```

#### WKN

```WKN``` ersetzt die Wertpapierkennnummer (WKN) in der URL.

```
https://example.com/data?wkn={WKN}
```
