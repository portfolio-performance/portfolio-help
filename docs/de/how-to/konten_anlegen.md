---
title: Konten anlegen
---

# Konten anlegen

*Portfolio Performance* nutzt Konten, um Bargeldbestände abzubilden. Mit ein paar Handgriffen kann man Konten für verschiedene Zwecke verwenden, zum Beispiel für:

* Depotverrechnungskonto bzw. Referenzkonto
* Termingeld
* Kündigungsgeld
* Tagesgeld
* P2P Kredite

## Allgemeine Einstellungen für alle Kontoarten

Im ersten Schritt ist es ratsam,  verschiedene Spalten unter Stammdaten –-> Konten anzulegen, die für die o.g. Kontoarten sinnvoll wären (z. B. für Termingeldkonten: Zinssatz, Anlagebeginn, Fälligkeit, Restlaufzeit in Tagen).

Dazu unter "Allgemeine Daten – Einstellungen" auf den Reiter "Attribute: Konten" klicken.


Abbildung: Individuelle Attribute.{class=pp-figure style="width:90%"}

![](images/manage_attributes.png)


Linksklick auf das Pluszeichen rechts oben im Fenster und aus der Liste der angebotenen Optionen die gewünschten Attribute hinzufügen.

Beispielsweise könnten das folgende Attribut sein:

* **Text**: um die Kontoart definieren zu können

    In der Spalte Name eine Beschreibung des Attributes eingeben (z. B. Kontoart).
    Mit der Tabulatortaste in die nächste Spalte springen und den Spaltennamen anpassen (z. B. Kontoart). Die Spalten Feldtyp und Quelle bleiben unverändert.

* **Prozentzahl**: für die Eingabe eines Zinssatzes bei Anlagekonten

    In den Spalten Name und Spaltenname jeweils die Beschreibung eingeben (z. B. Zinssatz).

* **Datum**: für die Eingabe von Anlagebeginn, Fälligkeitsdatum und ggf. einer Deadline für die Kündigung eines Termingeldes

    Sofern ein Datum für den Anlagebeginn sowie eines für die Fälligkeit der Anlage eingegeben werden soll, muss `Datum` zweimal als Attribut hinzugefügt werden und entsprechend beschriftet (Anlagebeginn / Fälligkeit) werden. Für die Einrichtung einer weiteren Spalte für ein Kündigungsdatum einfach ein weiteres Mal über das Pluszeichen das Attribut Datum hinzufügen und beschreiben.

## Konten anlegen

Nach Definieren der o.g. Attribute, wieder zurück zu "Konten" unter "Stammdaten" gehen.

Dort über das Symbol für "Einstellungen" rechts oben im Fenster können nun die neu definierten Attribute ausgewählt und als Spalte der Kontenübersicht hinzugefügt werden. Die Reihenfolge der Spalten kann durch Verschieben beliebig verändert werden, ebenso die Beschriftung der Spalten (Rechtsklick auf Spalte --> Spalte umbenennen).

Um die Spaltenbeschriftung zu kürzen, benennen wir die Spalte "Fälligkeit – Tage dazwischen" in "Restlaufzeit" um. In dieser Spalte wird die Anzahl der Tage bis zur Fälligkeit eines Termingeldes angezeigt (hier: -36 für 36 Tage vom 26. November 2022 bis zum 1. Januar 2023). Gleiches ist für die Anzahl Tage seit Anlagebeginn möglich, dazu einfach das Attribut "Anlagebeginn – Tage dazwischen" wie oben beschrieben als Spalte ergänzen.

In der Übersicht "Konten" unter "Stammdaten" werden neue Konten durch Linksklick auf das Pluszeichen rechts oben im Fenster hinzugefügt.

Durch einen Doppelklick auf ein Feld lassen sich die gewünschten Daten (Kontoart, Bankname, Zinssatz, Anlagebeginn, Fälligkeit) eingeben. Damit eine Restlaufzeit von *Portfolio Performance* automatisch angezeigt werden kann, muss das Datum im lokalen Format angegeben werden, z. B. DD.MM.JJJJ.

In diesem Beispiel sieht das dann wie folgt aus:

Abbildung: Stammdaten - Konten.{class=pp-figure style="width:90%"}

![](images/account_list.png)

Eine Spaltensortierung durch Anklicken des Spaltennamens (z. B. Kontoart, Zinssatz, Fälligkeit, Anzahl Tage bis zur Fälligkeit etc.) erstellt so eine einfache Übersicht absteigend nach Zinssatz oder Fälligkeit.

Buchungen können auf diesen Konten über einen Rechtsklick auf das entsprechende Konto vorgenommen werden oder über den Import von PDF oder CSV Dateien.


Abbildung: Konto - Kontextmenü.{class=pp-figure style="width:90%"}

![](images/account_list_context_menu.png)

Sofern es sich um ein Depotverrechnungskonto handelt, muss es unter "Stammdaten – Depots" in der Spalte "Referenzkonto" einem Depot noch zugeordnet werden.

Es können mehrere Verrechnungskonten in unterschiedlichen Währungen für dasselbe Depot geführt werden. Dazu unter "Stammdaten - Konten" die entsprechenden Konten anlegen, Kontowährung für jedes Verrechnungskonto auswählen und jedes dieser Konten demselben Depot unter "Stammdaten - Depots" zuordnen.
