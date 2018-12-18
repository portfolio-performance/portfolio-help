---
title: Buchungen erfassen
---

# Buchungen erfassen

Für die Berechnung der Performance braucht Portfolio Performance die historischen Buchungen.

## Unterstützte Buchungstypen

Folgende Typen von Buchungen werden von PP unterstützt:

### Kauf / Verkauf

Mit einem Kauf wird ein Wertpapier mit der angegebenen Stückzahl dem Depot zugeführt und zur selben Zeit das angegebene Konto mit dem Betrag belastet. Käufe und Verkäufe sind - bis auf die erfassten Steuern und Gebühren - performanceneutrale Buchungen denn zunächst wird nur Geld in Aktien umgewandelt. Erst mit einer Kursänderung kommt es zu einer Performance.

Für Kauf- und Verkaufbuchungen kann, wie für alle Wertpapierbuchungen - eine **Uhrzeit** erfasst werden - z.B. die Handelszeit an der Börse. Die Peformance wird allerdings nur für ganze Tage berechnet. Die Uhrzeit hat nur informativen Charakter. Wenn man als Uhrzeit *00:00* erfasst, wird die Uhrzeit nicht in der Liste der Buchungen angezeigt (Idee: nur so viel Informationen wie notwendig anzeigen).


### Einlieferung / Auslieferung

Einlieferungen und Auslieferungen sind das Pendant zu Käufen und Verkäufen aber **ohne** eine Buchung auf dem Verrechnungskonto. Es gibt zwei typische Anwendungsfälle für diesen Buchungstyp: man bekommt Wertpapiere in sein Depot übertragen oder man möchte das Depot in PP abbilden ohne das Verrechnungskonto pflegen zu müssen.

Einlieferungen und Auslieferungen sind performanceneutral bis auf die ggf. erfassten Steuern und Gebühren.

## Buchungen importieren