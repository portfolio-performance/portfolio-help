---
title: Historische Kurse
---

Zur Berechnung der Wertentwicklung benötigt Portfolio Performance zwei Dinge: die historischen Aktienkurse und im Falle von Aktien in Fremdwährung die historischen Wechselkurse.

Die historischen Wechselkurse findest Du unter dem Menüpunkt `Ansicht --> Allgemeine Daten`. Diese Wechselkurse stammen von der [Europäischen Zentralbank](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html) (EZB) und reichen in der Regel bis zum Jahr 1999 zurück, als der EUR auf den Finanzmärkten eingeführt wurde. Es handelt sich dabei um Referenzkurse, die wahrscheinlich leicht von den tatsächlichen Buchungswerten abweichen.

Wertpapiere werden an Börsen wie der NASDAQ oder XETRA gehandelt, wo sich Käufer und Verkäufer auf einen Preis einigen. Historische Kurse sind die Börsenkurse von Wertpapieren zu verschiedenen Zeitpunkten. Der „Schlusskurs“ ist der letzte Kurs des Wertpapiers am Ende des Handelstages. Weitere Kursarten wären der Eröffnungskurs, der erste Kurs des Wertpapiers zu Beginn des Handelstages, der „Low“- und der „High“-Kurs, die den niedrigsten und höchsten Kurs des Wertpapiers während des Handelstages darstellen.

!!! Wichtig
    Portfolio Performance verwendet den „Schlusskurs“ für Berechnungen. Wenn ein aktueller Kurs verfügbar ist, wird dieser in den Schlusskurs integriert. Bei Bitcoins ist die Situation komplexer, da Kryptowährungen rund um die Uhr gehandelt werden. Um überhaupt einen Schlusskurs zu definieren, nutzt Portfolio Performance den letzten Kurs von 0:00 Uhr Deiner Systemzeit. Daher können die historischen Kurse eines Bitcoins von Benutzer zu Benutzer variieren.

Manchmal werden historische Kurse angepasst, um bestimmte Ereignisse widerzuspiegeln. Um eine Wertentwicklung vergleichbar zu machen, werden Ereignisse wie Aktiensplits, Dividenden, Fusionen, Kapitalerhöhungen oder -herabsetzungen aus dem reinen Börsenkurs herausgerechnet. Diese Kurse nennt man „bereinigte Kurse“. 

An Finanzdiensten, die historische Kurse veröffentlichen, mangelt es nicht. Allerdings sind die meisten von ihnen relativ teuer. Einige Quellen bieten historische Kurse auch kostenlos an, allerdings sind diese nicht immer frei von Fehlern. Fehler reichen dabei von falschen Kursen, Währungswechseln oder genereller Verfügbarkeit.
Portfolio Performance nutzt unter anderem *Alpha Vantage*, *Finnhub*, *Quandl*. Leider ändern sich die Nutzungsbedingungen immer mal wieder und unterliegen dann Limitierungen, zum Beispiel bei der Anzahl der Abfragen. In der Praxis bewährt sich Portfolio Report. Auch Yahoo Finance wird häufig genutzt, allerdings muss man hier immer mal mit Ausfällen und Kursfehlern rechnen. Im Abschnitt [how-to](../how-to/historische-aktienkurse/index.md) findest Du weitere Tipps und Tricks.

Börsen stellen in aller Regel historische Kurse zur Verfügung. Das gilt allerdings nur für Aktien, die auch an dieser Börse gelistet und damit handelbar sind. Mehrere Finanzwebseiten wie Yahoo Finance, Alpha Vantage und andere bieten auf ihren Seiten historische Kurse für verschiedene Wertpapiere und Börsenmärkte an.

Portfolio Performance bietet Dir mehrere Möglichkeiten, aktuelle sowie historische Kurse automatisch zu beziehen. Weiterhin kann Portfolio Performance historische Kurse aus CSV-Dateien importieren, sowie ganze Tabellen von einer Webseite herunterladen.
Portfolio Performance nutzt unter anderem APIs von Finanzdatenanbietern und bietet darüber hinaus die Möglichkeit, Daten via JSON Stream zu beziehen.

Eine automatisierte Anfrage ist eine Nachricht, die Informationen und Parameter enthält, die für den Zugriff auf den historischen Kurs-Feed erforderlich ist.
Der Server verarbeitet die Anfrage und sendet eine Antwort zurück. Bei der Antwort kann es sich um eine CSV-Datei oder einen strukturierten Text (JSON oder XML) handeln.

!!! Wichtig
    Technisch kannst Du Webseiten auslesen, die Tabellen mit historischen Kursen enthalten (beispielsweise Ariva.de). Allerdings verwenden die meisten Webseiten JavaScript und JSON, um Kurse anzuzeigen. Daher wird diese Möglichkeit gerne verwendet, wenn auf den gängigen Webseiten keine Kurse vorhanden sind.