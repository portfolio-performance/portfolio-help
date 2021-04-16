---
title: Kursdaten laden
---

# Kursdaten laden

Historische Kurse sind extrem wichtig um eine Performance berechnen zu können. Wenn man nicht weiß wieviel ein Wertpapier vor einem Jahr wert war, dann helfen auch schicke Formeln nicht weiter. Allerdings ist es nicht einfach an gute und gleichzeitig kostenlose historische Kurse heranzukommen.

Die erste Anlaufstelle ist [Yahoo Finance](#yahoo-finance): sofern Yahoo Finance das Wertpapier kennt und auch Kurse hat, kann man bequem anhand des Tickers den Download direkt in PP konfigurieren. Allerdings ist die Abdeckung für deutsche Fonds oder ETFs nicht so prickelnd. Eine weitere Möglichkeit ist [AlphaVantage](#alphavantage): ebenfalls mit viel Gewicht auf den amerikanischen Markt. Allerdings erlaubt das kostenlose API nur wenige Aufrufe pro Minute.

Wenn diese zwei automatischen Quellen keine historischen Kurse bieten, muss man zu "halbautomatischen" Lösungen greifen. Die erste Möglichkeit ist eine URL zu hinterlegen auf der nach einer [Tabelle mit Kursinformationen](#tabelle-auf-einer-webseite) gesucht wird. Neben der Schwierigkeit überhaupt die passende Seite zu finden, kann es auch sein, dass die URLs sich immer wieder ändert so dass man mit Markos [dynamische Kursdaten-URLs](#dynamische-kursdaten-urls) zusammenbauen muss.

Und schließlich bleiben die manuellen Lösungen: die Kursdaten [per CSV-Datei](#csv-import) zu importieren oder manuell im Programm selbst zu erfassen.

[<i class="fa fa-comments-o" aria-hidden="true"></i> Forum: Quellen für historische Kurse](https://forum.portfolio-performance.info/t/quellen-fuer-historische-kurse/46)

## ETF - historische Kurse von Portfolio Report hinzufügen

Die Webseite Portfolio Report (PRep) (https://www.portfolio-report.net) speichert täglich ETF Schlusskurse. Diese Kurse können in Portfolio Performance (PPerf) als "historische" Kurse automatisch eingelesen werden. Dazu müssen die Kurse von PRep im PPerf "verbunden" werden.  
### Fall A
Ausgangslage: ein Wertpapier in PPerf existiert schon bzw. wurde neu angelegt - ISIN/Beschreibung/WKN sind also schon eingetragen. 
Vorgehen:

1. Im Portfolio Performance die ISIN eines Wertpapieres kopieren mit Doppelklick auf ISIN.

![grafik](https://user-images.githubusercontent.com/82599585/115005774-85b72a00-9ea8-11eb-8e55-417cb84fe17d.png)

2. Die Webseite https://www.portfolio-report.net/search öffnen, und nach der ISIN Nummer suchen lassen.

![grafik](https://user-images.githubusercontent.com/82599585/115006366-142bab80-9ea9-11eb-8c34-9774fe3b29bf.png)

3. Auf das Ergebnis (Results) klicken und die dann angezeigte URL kopieren. 

![grafik](https://user-images.githubusercontent.com/82599585/115006758-869c8b80-9ea9-11eb-9505-8ed852a3b06c.png)

4. Zurück im PPerf: in der Übersicht rechts-Klick auf das entsprechende Wertpapier und im Menu "mit Portfolio Report verknüpfen" anklicken.

![grafik](https://user-images.githubusercontent.com/82599585/115007011-d11e0800-9ea9-11eb-83ab-0d552c793852.png)

5. In dem sich öffnenden Fenster die URL aus Schritt 3 einfügen und mit OK bestätigen.

![grafik](https://user-images.githubusercontent.com/82599585/115007247-117d8600-9eaa-11eb-9901-701625a7d60d.png)

6. Das entsprechende Wertpapier mit Editieren (STRG+E) zum Bearbeiten öffnen. Das Wertpapier wird nun als mit PRep gekoppelt angezeigt.

![grafik](https://user-images.githubusercontent.com/82599585/115007862-bc8e3f80-9eaa-11eb-8f5c-5d3776be6765.png)

7. Im Reiter "Historische Kurse" als Kurslieferant "Portfolio Report" auswählen und mit OK bbestätigen.

![grafik](https://user-images.githubusercontent.com/82599585/115008149-12fb7e00-9eab-11eb-8779-8492ced89fa5.png)


### Fall B
Ausgangslage: ein Wertpapier wird in Portfolio Report gefunden, und wird mit "Drag and Drop" in Portfolio Performance eröffnet. Portfolio Performance sollte geöffnet sein.
Vorgehen:

1. Das Wertpapier in https://www.portfolio-report.net/search suchen/bestimmen. Nachdem das Resultat angezeigt wird, mit dem Cursor auf das Werpapier zeigen bis der Cursor sich in eine "Hand" verwandelt. 

![grafik](https://user-images.githubusercontent.com/82599585/115011485-f6f9db80-9eae-11eb-841b-0603485bc8bd.png)
![grafik](https://user-images.githubusercontent.com/82599585/115014111-32e27000-9eb2-11eb-970b-38a5531e5498.png)


2. Dann linke Maustaste drücken/halten und den Cursor nach Portfolio Performance in das Wertpapier Feld ziehen, loslassen. Automatisch öffnet sich das Editiermenu des entsprechenden Wertpapiers.

![grafik](https://user-images.githubusercontent.com/82599585/115012308-fada2d80-9eaf-11eb-8eb7-ec8463616ca8.png)
![grafik](https://user-images.githubusercontent.com/82599585/115012457-26f5ae80-9eb0-11eb-88de-26f244cc25aa.png)

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

Manche Seiten verteilen die Daten auf mehrere Requests. Wenn eines der Macros in der URL gefunden wird, wird die URL dynamisch zusammengesetzt und PP macht solange Aufrufe bis keine weiteren Kurse mehr gefunden werden.

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

Wenn die identische URL mehrfach generiert wird, dann macht PP nur eine einzige Abfrage. Nehmen wir das Datumsformat aus dem letzten Beispiel: ```{DATE:yyyy-MM-32}``` Der Tag ist statisch auf 32 gesetzt. Es wird für jeden Tag in einem Monat die identische URL generiert, aber nur eine Abfrage zum Server gemacht.

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
* ```<delta>``` ist eine Zeitspanne basierend auf den ISO-8601 Regeln wie in [Java](https://docs.oracle.com/javase/8/docs/api/java/time/Period.html#parse-java.lang.CharSequence-) implementiert. Die Zeitspanne kann optional mit einem Minuszeichen beginnen - dann wird sie vom aktuellen Datum abgezogen. Dann folgt ein ```P``` (für period) und anschliessend eine Zahl und ein Suffix - z.B. einem ```Y``` für Jahre, ```M``` für Monate, ```W``` für Wochen und einem ```D``` für Tage.

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
