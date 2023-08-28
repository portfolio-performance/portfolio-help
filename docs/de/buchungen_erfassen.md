---
title: Buchungen erfassen
---

# Buchungen erfassen

Für die Berechnung der Performance braucht Portfolio Performance die historischen Buchungen.

## Unterstützte Buchungstypen

Folgende Typen von Buchungen werden von PP unterstützt:

### Wertpapier: Kauf / Verkauf

Mit einem Kauf wird ein Wertpapier mit der angegebenen Stückzahl dem Depot zugeführt und zur selben Zeit das angegebene Konto mit dem Betrag belastet. Käufe und Verkäufe sind - bis auf die erfassten Steuern und Gebühren - performanceneutrale Buchungen, denn zunächst wird nur Geld in Aktien umgewandelt. Erst mit einer Kursänderung kommt es zu einer Performance.

Für Kauf- und Verkaufsbuchungen kann - wie für alle Wertpapierbuchungen - eine **Uhrzeit** erfasst werden, z.B. die Handelszeit an der Börse. Die Uhrzeit hat nur informativen Charakter, da die Peformance nur für ganze Tage berechnet wird.  Wenn man als Uhrzeit *00:00* erfasst, wird die Uhrzeit nicht in der Liste der Buchungen angezeigt (Idee: nur so viel Informationen wie notwendig anzeigen).


### Wertpapier: Einlieferung / Auslieferung

Einlieferungen und Auslieferungen sind das Pendant zu Käufen und Verkäufen aber **ohne** eine Buchung auf dem Verrechnungskonto. Es gibt zwei typische Anwendungsfälle für diesen Buchungstyp: man bekommt Wertpapiere in sein Depot übertragen oder man möchte das Depot in PP abbilden ohne das Verrechnungskonto pflegen zu müssen.

Einlieferungen und Auslieferungen sind performanceneutral bis auf die ggf. erfassten Steuern und Gebühren.

### Wertpapier: Umbuchung

Ein Umbuchung bucht die angegebene Stückzahl an Wertpapieren von einem Depot in ein anderes Depot um.

Ein Umbuchung hat zunächst mal keine Auswirkung auf die Performance. Allerdings werden Umbuchungen dann relevant wenn man sich nur Teile der Datei anschaut, z.B. die Performance nur für eines der Depots. Dann wird als Einstandswert des Wertpapieres der Wert der Umbuchung herangezogen.

### Wertpapier: Dividende

Mit einer Dividende kann man - wer hätte das gedacht - Dividenden zu Wertpapiere erfassen - oder besser gesagt: jegliche performancerelevante Ausschüttung. Eine Dividendenbuchung muss zwingend auf einem Konto erfasst werden.

Optional kann man die Stückzahl eingeben auf die sich die Dividende bezieht. Dieser Wert wird bisher nur genutzt um Dividende pro Anteil in der Liste der Buchungen anzuzeigen.

## Buchungen importieren