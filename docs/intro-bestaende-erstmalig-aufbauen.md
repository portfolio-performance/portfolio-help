# Bestände erstmalig aufbauen

In diesem Schritt vollziehen wir alle Transaktionen in unserem Depot nach, die zum heutigen Stand geführt haben. Das ist notwendig, um die Portfolio Performance (und darum ging es ja eigentlich) unter Berücksichtigung der Anlageentscheidungen der Vergangenheit berechnen zu können. Alternativ können wir auch einfach mit den aktuellen Beständen starten, oder zu einem ausgewählten Aufsetzpunkt in der Vergangenheit.

## Kauf oder Einlieferung?

Portfolio Performance bietet *Kauf, Verkauf, Einlieferung* und *Auslieferung* für die Buchung von Transaktionen an. Wo ist der Unterschied? 

<img src="../images/assets/kauf.png" alt="Kauf" style="zoom:50%;" /> <img src="../images/assets/einlieferung.png" alt="Einlieferung" style="zoom:50%;" />

Bei einem *Kauf* bucht *Portfolio Performance* den Kauf als Zugang im Depot, und belastet dazu das zugehörige Verrechnungskonto. 

Bei einer *Einlieferung* bucht *Portfolio Performance* nur den Zugang im Depot.

## Aufsetzpunkt festlegen

Es kommt auf die Zielsetzung an, wie weit wir die zurückliegenden Transaktionen in *Portfolio Performance* erfassen. 

Um die Performance des Portfolios von der ersten Einlage bis heute zu bestimmen, müssen wir alle Bewegungen auf dem Depot und Verrechnungskonto seit der Einrichtung nachvollziehen. Das ist einmalig ein bißchen Arbeit, schafft aber volle Transparenz (Variante A). Alternativ können wir mit den Beständen aus einem Depot-Auszug (Quartals- oder Jahresauszug) beginnen, dann können wir aber nur bis zu diesem Stichtag zurückschauen (Variante B).

### Variante A: Lückenlose Buchung aller zurückliegenden Transaktionen für Depot und Verrechnungskonto

Wollen wir die Performance der Bestände und Einlagen auf Depot und Verrechnungskonto rückwirkend nachvollziehen, müssen wir bei Null starten. Wir buchen rückwirkend

- alle *Käufe* und *Verkäufe* für das Depot inkl. Gebühren und Steuern 
- alle *Einlagen, Entnahmen, Zinsen* und *Steuern* für das Verrechnungskonto 

Das kann je nach Alter des Portfolios und Menge der Transaktionen etwas Mühe machen. Wenn längere Zeit größere Beträge auf dem Verrechnungskonto vorgehalten wurden, kann es interessant sein, sich ein Bild über den Einfluss auf die Wertentwicklung zu machen.

### Variante B: Anlage der Bestände zu einem Stichtag, danach lückenlose Buchung  

Basis sind die Kontoauszüge von Depot und Verrechnungskonto zu einem Stichtag. Wir betrachten die Bestände der Wertpapiere im Depot und das Guthaben auf dem Verrechnungskonto zum heutigen Stichtag als "vom Himmel gefallen". Dazu buchen wir 

- die Bestände zum Stichtag als *Einlieferung* in das Depot 
- den Stand des Verrechnungskontos zum Stichtag als *Einlage*.

Damit haben wir einen sauberen Aufsetzpunkt für die Buchung der Transaktionen nach dem Stichtag.

## Einlieferung ins Depot buchen

<img src="../images/assets/einlage-buchen.gif" alt="Einlage buchen" style="zoom:50%;" />

In der linken Navigationsleiste wählst du `Alle Wertpapiere`. Jetzt kannst du das Wertpapier in der Wertpapier-Übersicht auswählen und mit rechter Maustaste `Einlieferung ...` selektieren. Gib das Datum und die Anzahl *Stück* eintragen und klicke `Speichern`. 

<img src="../images/assets/trades.png" alt="trades" style="zoom:50%;" />

Eine Kontrolle kann über die Navigationsleiste *Trades* erfolgen, hier ist die Einlage jetzt in der Liste aufgeführt. Bei einem Eingabefehler kannst du die Buchung hier auch korrigieren (`rechte Maustaste > *Editieren ...*`) 

## Einlage ins Verrechnungskonto buchen

*... hier fehlt noch Text*

