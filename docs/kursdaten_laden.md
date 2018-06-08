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

In einer URL darf immer nur genau ein Macros vorkommen.

#### DATE

```DATE:<format>``` generiert eine Abfrage für jedes Datum mit dem angegebenen Format, und zwar

* wenn **keine** Kurse existieren, wird vom aktuellen Datum rückwärts in die Vergangenheit gesucht solange bis keine Kurse mehr gefunden werden;
* wenn historische **Kurse existieren**, dann wird vom letzten Kursdatum vorwärts bis zum aktuellen Datum eine URL generiert.

Das Datumsformat folgt den Regeln des [DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html) aus Java. Die wichtigsten Symbole sind ```y``` für das Jahr, ```M``` für den Monat im Jahr und ```d``` für den Tag im Monat.

Beispiele:
```
https://example.com/data?datum={DATE:yyyy-MM-dd}
https://example.com/data?month={DATE:yyyy-MM}
https://example.com/data?datum={DATE:yyyy-MM-31}
```

Wenn die identische URL mehrfach generiert wird, dann macht PP nur eine einzige Abfrage. Nehmen wir das Datumsformat aus dem letzten Beispiel: ```{DATE:yyyy-MM-31}``` Der Tag ist statisch auf 31 gesetzt. Es wird für jeden Tag in einem Monat die identische URL generiert, aber nur eine Abfrage zum Server gemacht.

#### PAGE

```PAGE``` fängt mit 1 an zu zählen bis keine weiteren Kurse mehr auf der Seite gefunden werden. 

```
https://example.com/data?page={PAGE}
```
