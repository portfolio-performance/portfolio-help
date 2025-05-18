---
title: Portfolio Performance Begriffsübersicht
description: Ein alphabetisches Glossar wichtiger Begriffe und Konzepte in Portfolio Performance, das Nutzern hilft, Felder, Kennzahlen und Funktionen der Anwendung besser zu verstehen.
changes:
    - date: 2025-05-03
      author: Nirus2000
      description:
        - Erste Version der Seite "Portfolio Performance Begriffsübersicht".
        - Bietet klare Definitionen von Attributen, Feldern und Konzepten innerhalb der Anwendung.
todo: Bestandsübersicht, Diagramme, Bestände, Performance, Berechnung, Wertpapiere, Zahlungen, Trades, Einstellungen, Währungen
---

Diese Seite bietet einen Überblick über grundlegende Konzepte und Begriffe, die in **Portfolio Performance** verwendet werden.  
Zentrale Konzepte wie Konten, Buchungen, Berichtszeiträume, Einstandspreise und Performance werden in eigenen Kapiteln erläutert (siehe Seitenleiste).  
Im Folgenden findest du ein Glossar, das alle Attribute (auch *Felder* oder *Spalten* genannt) beschreibt, die in verschiedenen Bereichen von Portfolio Performance vorkommen.  
Außerdem werden Buchungstypen und Feldwerte erklärt.

## Datenqualität

Diese Spalten findest du unter `Wertpapiere` → `Alle Wertpapiere`:

- **Tatsächliche # Kurse**: Anzahl der gespeicherten historischen Kurse.
- **Erwartete # Kurse**: Erwartete Anzahl historischer Kurse, basierend auf deinen Kalendereinstellungen.
- **Fehlende # Kurse**: Differenz zwischen gespeicherten und erwarteten historischen Kursen.
- **Datum des letzten historischen Kurses**: Datum des zuletzt heruntergeladenen historischen Kurses.
- **Datum des ersten historischen Kurses**: Datum des ersten heruntergeladenen historischen Kurses.
- **Vollständigkeit der historischen Kurse**: Beschreibt die Vollständigkeit deiner historischen Kursdaten. Geringe Abweichungen können durch regionale Feiertage entstehen.
- **Absolute Performance**: Wertbasierte Kennzahl zur Bewertung von Gewinn oder Verlust einer Anlage über einen Zeitraum:  
`(Marktwert am Ende + Verkäufe/Zuflüsse + Dividenden) - (Steuern + Gebühren + Startwert + Käufe/Zuflüsse)`  
**Synonym:** Gesamtrendite.

## Stammdaten

Der zentrale Bereich für deine Konten, Depots, Sparpläne und eine Übersicht aller Buchungen befindet sich in der Navigationsleiste.

- **Konten**: Speichern Buchungen im Zusammenhang mit Geschäftsvorfällen oder Zahlungsbewegungen.
- **Depot (Wertpapierdepot)**: Enthält die Wertpapiere, die du aktuell besitzt.
- **Referenzkonto**: Konto zur Abwicklung von Buchungen. Beispiel: Beim Kauf eines Wertpapiers steigt der Depotbestand, das Referenzkonto wird belastet. Beim Verkauf sinkt der Depotbestand, das Referenzkonto wird gutgeschrieben.
- **Sparpläne**: Übersicht deiner Sparpläne, ihrer Ausführungsintervalle und Optionen zur Automatisierung von Buchungen.
- **Buchungen**: Konsolidierte Ansicht aller Buchungen über alle Konten hinweg. Die Liste ist filterbar.

## Buchungstypen

Diese findest du häufig im Kontextmenü von Konten, Depots und Wertpapieren.

- **Einlieferung**: Zugang eines Wertpapiers ohne Abwicklung über das Referenzkonto.
- **Auslieferung**: Abgang eines Wertpapiers ohne Abwicklung über das Referenzkonto.
- **Umbuchung**: Verschiebt ein Wertpapier zwischen Depots. Erstellt eine Ausbuchung im Quell-Depot und eine Einbuchung im Ziel-Depot.
- **Einzahlung**: Fügt Geld zu Portfolio Performance hinzu, z. B. zum Kauf von Wertpapieren oder zur Zinsüberwachung.
- **Auszahlung**: Entnimmt Geld. Wirkt sich auf die Portfolio-Performance aus.
- **Kauf**: Erwerb eines Finanzprodukts, Belastung des Referenzkontos.
- **Verkauf**: Verkauf von Wertpapieren, Gutschrift auf das Gegenkonto.
- **Dividende**
- **Zinsen**
- **Zinsbelastung**
- **Steuern**: Zahlung an den Staat ohne direkte Gegenleistung.
- **Steuererstattung**
- **Aktien-Split**
- **Gebühren**: Kosten, die von Dienstleistern oder Brokern für die Durchführung von Transaktionen erhoben werden.
- **Gebührenerstattung**

## Konfigurierbare Spalten

- **Kursveränderung (Zeitraum)**: Prozentuale Differenz zwischen dem letzten und ersten Kurs über einen gewählten Zeitraum.
- **Kursveränderung Vortag (Betrag)** oder **Δ Betrag**: Absolute Differenz zwischen dem zuletzt abgerufenen Kurs und dem vorherigen.
- **Kursveränderung Vortag (%)** oder **Δ %**: Prozentuale Differenz zwischen dem zuletzt abgerufenen Kurs und dem vorherigen.
- **Kurs**: Letzter gehandelte Kurs eines Wertpapiers.
- **Abstand zur GD (Tage)**: Prozentuale Differenz zwischen aktuellem Kurs und gleitendem Durchschnitt (GD) über X Tage.
- **Abstand zum Allzeithoch (ATH)**: Zeigt an, wie weit der aktuelle Kurs vom höchsten Kurs innerhalb eines definierten Zeitraums entfernt ist.
- **Einstandspreis**: Kumulierte Transaktionswerte aller Käufe (+) und Verkäufe (-) eines Wertpapiers im Berichtszeitraum.

## Wertpapiere

- **Währung**: Die beim Anlegen eines Wertpapiers zugewiesene Währung. Sobald Buchungen existieren, kann die Währung nicht mehr geändert werden.
- **Datum**: Datum einer Buchung.

## Wertpapiere hinzufügen

- **Wertpapier**: Ein handelbares Finanzinstrument wie Aktien, Anleihen, Kryptowährungen, Edelmetalle etc.
- **Börse**: Ein Wertpapier kann an mehreren Börsen gehandelt werden (z. B. NVIDIA: NASDAQ [NVDA] oder XETRA [NVD.DE]).
- **Name**: Wird zunächst vom Datenanbieter übernommen, kann aber angepasst werden.

## Wechselkurse

- **Inaktiv**: Ein Wertpapier kann als inaktiv markiert werden; es erscheint nicht mehr in Buchungsdialogen und historische Kurse werden nicht mehr aktualisiert.
- **ISIN (Internationale Wertpapierkennnummer)**: Eine eindeutige, weltweit verwendete 12-stellige Kennung (insbesondere bei europäischen Brokern).
- **WKN (Wertpapierkennnummer)**: Eine 6-stellige deutsche Kennung (weitgehend durch ISIN ersetzt).

## Einzahlungen und Abhebungen

- **Einzahlung**: Hinzufügen von Geldern zu Portfolio Performance für eine spätere Verwendung, z. B. um Wertpapiere zu kaufen oder Zinsen zu überwachen.
- **Abhebung**: Entnahme von Geldern oder Bargeld. Dies beeinflusst die Performance des Portfolios.

## Dividenden und Zinsen

- **Dividende**: Auszahlung von Gewinnen durch das Unternehmen an die Aktionäre. Diese wird dem Referenzkonto gutgeschrieben.
- **Zinsen**: Betrag, den Sie aus Kapitalanlagen (z. B. Anleihen oder Bankguthaben) erhalten.
- **Zinsbelastung**: Kosten für geliehenes Kapital (z. B. Kredit- oder Darlehenszinsen).

## Steuern und Rückerstattungen

- **Steuern**: Zahlungen an den Staat ohne direkte Gegenleistung.
- **Steuerrückerstattung**: Rückerstattung von bereits gezahlten Steuern.

## Gebühren und Gebührenrückerstattung

- **Gebühren**: Kosten, die von Dienstleistern oder Brokern für die Ausführung von Transaktionen erhoben werden.
- **Gebührenrückerstattung**: Rückerstattung von zuvor gezahlten Gebühren.

## Käufe und Verkäufe

- **Belastung**: Gesamtkosten einer Kaufbuchung inklusive Steuern und Gebühren.
- **Erlös**: Gesamtbetrag, der bei einer Verkaufstransaktion erzielt wird, abzüglich Steuern und Gebühren. Dieser Betrag wird dem Referenzkonto gutgeschrieben.

## Allgemein

- **Notiz**: Ermöglicht das Hinzufügen von Kommentaren zu Wertpapieren oder Buchungen. Wird beim PDF-Import automatisch ausgefüllt, ist aber editierbar.
- **Stückzahl**: Die Anzahl der gehaltenen Wertpapiere. Dezimalstücke nennt man Bruchstücke (Fractional Shares).
- **Symbol (Ticker)**: Kennung eines Wertpapiers, meist kombiniert mit Börsencode.
- **Zielwährung**: Dient zur Definition von Umrechnungskursen bei Währungswechseln.
- **Ereignis**: Ermöglicht das Dokumentieren von Ereignissen, die in Diagrammen und Detailansichten sichtbar sind (z. B. Aktien-Splits).
- **Beobachtungsliste**: Erstelle eine benutzerdefinierte Liste von Wertpapieren mit konfigurierbarem Layout.
- **Widget**: Baue eigene Dashboards mit Diagrammen und Kennzahlen zur Analyse, zum Vergleich und zur Bewertung deines Portfolios.
- **Wechselkurs**: Wert einer Währung im Verhältnis zu einer anderen.

## Kurslieferanten

- **Kurslieferant (Historisch)**: Datenquellen für historische Kurse (Alpha Vantage, Bitfinex, Binance, CoinGecko, EOD Historical Data, Finnhub, Eurostat HICP, EZB SDW, Kraken, PWP Leeway UG, Twelve Data, Quandl, Tabelle von Webseite, VIA/CS Fonds, Yahoo Finance, JSON oder keine).
- **Kurslieferant (Aktuell)**: Datenquelle für aktuelle Kurse (gleiche Liste wie oben). Alternativ „gleich wie historische Kurse“ verwenden.
- **URL (Historisch)**: Quell-URL zum Herunterladen historischer Kurse.
- **URL (Aktuell)**: Quell-URL für aktuelle Kurse.
- **Rendite**: Prozentuale Veränderung über einen definierten Zeitraum.

## Risikokennzahlen

- **Risikokennzahlen**: Ermöglichen die quantitative Bewertung der Unsicherheit einer Anlage (z. B. Risiko des Totalverlusts).
- **Maximaler Drawdown**: Der größte Rückgang vom Höchststand zum Tiefpunkt im Portfoliowert innerhalb eines Zeitraums.
- **Dauer maximaler Drawdown**: Zeitraum zwischen zwei Höchstständen.
- **Semivolatilität**: Indikator für das Verlustrisiko (negative Renditeabweichungen).
- **Volatilität**: Indikator, der sowohl positive als auch negative Renditeabweichungen berücksichtigt.

## Allgemeine Daten

- **Währungen**: Übersicht über EZB-Referenzkurse und einen Währungsrechner.
- **Einstellungen**: Ermöglicht das Anlegen eigener Attribute (zusätzlicher Spalten) oder Lesezeichen.
