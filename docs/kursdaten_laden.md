---
title: Kursdaten laden
---

# Kursdaten laden

## Yahoo Finance

## AlphaVantage

## CSV Import

## Tabelle auf einer Webseite

### Dynamische Kursdaten-URLs

Manche Seiten verteilen die Daten auf mehrere Requests. Wenn eines der Macros in der URL gefunden wird, wird die URL dynamisch zusammengesetzt und PP macht solange Aufrufe bis keine weiteren Kurse mehr gefunden werden.

In einer URL dürfen mehrere Marcos verwendet werden. Allerdings dürfen ```DATE``` und ```PAGE``` nicht gemeinsam verwendet werden, weil beide unterschiedliche Iterationen von URLs generieren.

[<i class="fa fa-comments-o" aria-hidden="true"></i> Forum](https://forum.portfolio-performance.info/t/dynamische-kursdaten-urls/2929/1)

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
