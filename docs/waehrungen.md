---
title: Währungen
---

# Währungen

Portfolio Performance unterstützt Konten und Wertpapiere in Fremdwährungen.

* Die **Berichtswährung** stellt man unter *Berichte -> Vermögensaufstellung* oben rechts in der Werkzeugleiste ein.
* Beträge in der Berichtswährung werden üblicherweise ohne Währungskürzel dargestellt (damit die Ansichten nicht unnötig viele Informationen darstellen).
* Konten und Wertpapiere können in einer Fremdwährung geführt werden. In einem Portfolio können Wertpapiere unterschiedlichster Währung existieren. Ein Wertpapiere ohne Währung wird als *Aktienindex* interpretiert und kann entsprechend nicht gekauft werden.
* Neben den Wechselkursen der [Europäischen Zentralbank](#referenzwechselkurse-der-europaischen-zentralbank) kann man auch [benutzerdefinierte Wechselkurse](#benutzerdefinierte-wechselkurse) anlegen und - anlog zu Wertpapieren - aus den üblichen Quellen mit Kursen versorgen.
* Standardmässig rechnet PP bei monetären Beträgen mit 2 Nachkommastellen und bei Wechselkursen mit 4 Nachkommastellen. Wenn der Wechselkurse invertiert wird, rechnet PP mit 10 Nachkommastellen.
* Wechselkurse können in [Mengennotierung oder Preisnotierung](#notierung) dargestellt werden.
* Beträge in einer Buchung weden wenn möglich mit dem Wechselkurs aus der Buchung selbst umgerechnet.

Die verfügbaren Wechselkurse finden sich unter *Allgemeine Daten -> Währungen -> Wechselkurse*.

<a href="../images/assets/liste_waehrungen.png"><img alt="Allgemeine Daten - Währungen - Wechselkurse" src="../images/assets/liste_waehrungen.png" width="670" style="width: 100%; max-width: 670px; display: block; margin-left: auto; margin-right: auto;"/></a>

## Notierung

In den Einstellungen kann man zwischen **Mengennotierung** und **Preisnotierung** umstellen.

> Die Mengennotierung gibt den Preis einer Einheit der inländischen
Währung in Einheiten der ausländischen Währung an (am Beispiel von
Europa und den USA aus europäischer Sicht: Dollar je Euro). Dagegen
gibt die Preisnotierung den Preis einer Einheit der ausländischen
Währung in Einheiten der inländischen Währung an (Euro je Dollar
aus europäischer Sicht).

> In der Eurozone, Großbritannien, Australien und Neuseeland wird heute
mehrheitlich die Mengennotierung verwendet, während ansonsten die
Preisnotierung üblich ist, insbesondere auch in der Schweiz. [Quelle](https://de.wikipedia.org/wiki/Wechselkurs)


!!! example "Beispiele"
    Mengennotierung: EUR/USD 1,1232
    "Für einen Euro bekommt man 1,1232 US-Dollar."

    Preisnotierung: USD/EUR 0,89
    "Für einen US-Dollar muss man 0,89 Euro bezahlen."

## Währungsrechner

Mit dem Währungsrechner unter *Allgemeine Daten -> Währungen -> Währungsrechner* kann man nachvollziehen welche Wechselkurse PP für eine Umrechnung verwendet.

<a href="../images/assets/waehrungsrechner.png"><img alt="Währungsrechner" src="../images/assets/waehrungsrechner.png" width="471" style="width: 100%; max-width: 471px; display: block; margin-left: auto; margin-right: auto;"/></a>

PP gewichtet Wechselkurse und nutzt zur Umrechnung den Wechselkurs mit dem niedrigsten Gewicht:

* Benutzerdefinierte Wechselkurse haben ein Gewicht von 1
* Wechselkurse der EZB haben ein Gewicht von 2
* Invertierte Wechselkurse (Umkehrkurs) zählen zu dem Gewicht +2 hinzu
* Eine Kette von Wechselkursen (z.B. USD -> EUR -> CHD) zählt eine Gewicht von +1 hinzu

Mit diesen Gewichten wird sichergestellt, dass benutzerdefinierte Wechselkurse von denen der Europäischen Zentralbank genutzt werden. Andrerseits wird ein Wechselkurs der Europäischen Zentralbank dem Umkehrkurs eines benutzerdefinierten Wechselkurses vorgezogen. Ein direkter Wechselkurs wird einer Kette von Wechselkursen vorgezogen die zu der gleichen Umrechnung führen würden.

## Referenzwechselkurse der Europäischen Zentralbank

PP lädt automatisch beim Start die [Referenzwechselkurse der Europäischen Zentralbank (EZB)](https://www.ecb.europa.eu/stats/exchange/eurofxref/html/index.en.html). Damit kennt PP die Wechselkurse aller wichtigen Währungen vom US Dollar über den japanischen Yen, das britischen Pfund bis zum Schweizer Franken.

Laut Webseite werden die Wechselkurse der EZB gegen 16 Uhr aktualisiert:

> The reference rates are usually updated around 16:00 CET on every working day, except on TARGET closing days. They are based on a regular daily concertation procedure between central banks across Europe, which normally takes place at 14:15 CET. [Quelle](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html)

## Benutzerdefinierte Wechselkurse

