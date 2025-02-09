---
title: Wertentwicklung
---

# Wertentwicklung messen

Die Messung der Wertentwicklung eines Finanzportfolios basiert auf dem Konzept der Rendite: die Wertsteigerung oder -minderung über einen bestimmten Zeitraum. Ein Beispiel: Dein Portfolio beginnt bei 100 EUR und wächst bis zum Ende des Zeitraums auf 104 EUR an, was einer Wertentwicklung von + 4 % entspricht. Das Beispiel zeigt Dir 3 Varianten, mit denen sich die Rendite (engl. ROR) (Rate of Return), also der Wertzuwachs berechnen lässt.

$$\mathrm{ = \frac{(MVE - MVB)}{MVB} \quad \Leftrightarrow \quad r = \frac{MVE}{MVB} -1 \quad \Leftrightarrow \quad MVE = MVB \times (1 + r) \quad (Eq  1)}$$

MVE entspricht dem Marktwert (Ertrag) am Ende des Berichtszeitraums, während MVB (Aufwand) dem Wert Deines Portfolios zu Beginn des gleichen Zeitraums entspricht.

- Der Prozentsatz von r (Rendite) gilt für den gesamten Zeitraum zwischen MVE und MVB (z.B. 3 Jahre, 6 Monate, ...). Es handelt sich *nicht* um einen annullierten Prozentwert.
- Innerhalb dieses Zeitraums gibt es keine weiteren Transaktionen. Der MVE wird ausschließlich durch den MVB und die Zeit beeinflusst.

Portfolio Performance verwendet zwei verschiedene Methoden, um die Rendite zu berechnen, wenn innerhalb des Berichtszeitraums zusätzliche Transaktionen stattfinden: geldgewichtet oder zeitgewichtet. Zusätzlich wird die Wertentwicklung auf Portfolio-, Wertpapier- oder Handelsebene (Zuflüsse/Abflüsse) unterschieden.

!!! Wichtig
    Die einfache Rendite (Rate of Return, ROR) reicht nicht aus, um die Wertentwicklung Deines Portfolios richtig zu erfassen, sobald Transaktionen während des Berichtszeitraums stattgefunden haben. Nehmen wir das Beispiel von oben. Dein Portfolio enthält eine Aktie, die zu Beginn des Jahres bei 100 EUR stand (MVB=100). Dank des positiven Kursverlaufs stieg der Kurs am Ende des Jahres auf 104 EUR pro Aktie. Vergleichen wir nun die folgenden Szenarien:

    - **Keine zusätzlichen Buchungen**: Du hast weder Käufe noch Verkäufe getätigt. Nach Gleichung 1 gilt: `r = (104-100)/100 = 0.04 -> 4%`. Dies scheint intuitiv richtig zu sein. Du hast 4 EUR Buchgewinn, was 4 % des ursprünglichen Wertes entspricht.

    - **Weitere Buchungen**: Du kaufst zu Beginn des Jahres eine weitere Aktie zu einem Kurs von 100 EUR. Der MVB beträgt immer noch 100 EUR, während der MVE jetzt zu `2 * 104 = 208` wird. Die Wertentwicklung beträgt somit sagenhafte 108 % bzw. `(208-100)/100`. Das fühlt sich aber nicht richtig an. Du *weißt*, dass die Wachstumsrate der Aktie des Unternehmens 4 % betrug. Natürlich hat Deine Gesamtinvestition von 200 € 8 EUR bzw. 4 % Rendite erzielt. Aber nicht auf die MVB von 100 EUR. Die zusätzliche Transaktion hat die einfache Renditeformel verfälscht.

## Geldgewichtete Rendite (IZF)
(engl. Money Weighted Rate of Return)

Die geldgewichtete bzw. Kapital gewichtete Rendite (IZF) verwendet die im Projektmanagement übliche Methode der **einfachen Renditeberechnung**. Bei dieser Berechnung werden sowohl der Zeitpunkt (wann) als auch der Betrag (wie viel) der Mittel, die innerhalb des Berichtszeitraums in das Portfolio fließen oder es verlassen, berücksichtigt.

Wenn Du Dir noch nicht sicher bist, ob Du das Prinzip der geldgewichteten Rendite verstanden hast, kannst Du [hier](geld-gewichtet.md) noch weiter ins Detail gehen. Die Formeln und Beispiele, die von einer einfachen Einzelaktienanlage bis hin zu mehreren Buchungen einschließlich Dividenden reichen, werden ausführlich erläutert. Die Beispiele basieren auf unserem Demo-Portfolio. Somit bist Du in der Lage, alle Berechnungen selbst nachzuvollziehen und nach Belieben zu verändern.

## Zeitgewichtete Rendite
(engl. Time Weighted Rate of Return)

Die zeitgewichtete Rendite (auch TTWROR) wird nicht durch den Anlagebetrag beeinflusst. Ob Du 1 EUR oder 100 EUR investierst, Du wirst die gleiche zeitgewichtete Rendite erzielen. Der Berichtszeitraum wird in mehrere Halteperioden unterteilt, und für jede Halteperiode wird ein Renditewert berechnet und dann zu einer Gesamtrendite zusammengefasst. Jede Periode hat das gleiche Gewicht, daher der Name zeitgewichtete Rendite. Bei dieser Methode wird die Wertentwicklung anhand der einfachen Renditen ohne Berücksichtigung des Gesamtinvestitionsbetrags berechnet.

Da auch dieses Thema samt Berechnung nicht ganz trivial ist, haben wir Dir [hier](zeit-gewichtet.md) anhand des Kommer Portfolios wieder einige Beispiele gebaut, mit deren Hilfe Du in die Thematik einsteigen kannst.

Zum Thema Renditeberechnung findest Du heute viele gute Videos auf den gängigen Plattformen.