# Übersetzungsanweisungen für das Portfolio-Help Manual

## Allgemeine Informationen

Dieses Dokument enthält Richtlinien für die Übersetzung des Portfolio-Help Manuals von Englisch ins Deutsche.

## Zielgruppe

- Entwickler
- Technische Dokumentationen
- Benutzer von Portfolio-Help

## Übersetzungsrichtlinien

### 1. Sprachliche Konventionen

#### Fachbegriffe
- Behalte technische Begriffe in englischer Form bei, wenn keine etablierte deutsche Übersetzung existiert
- Erstelle eine Glossar-Datei für häufig verwendete Begriffe
- Beispiele: "repository", "branch", "commit", "deployment"
- **Portfolio Performance** → *Portfolio Performance* (beibehalten)
- **IRR** → *Irr* (Internal Rate of Return) oder auch Interner Zinsfuß (IZF)
- **TTWROR** → *TTWROR* (Time-Weighted Rate of Return)
- **MVB** → *MVB* (Market Value Beginning) bedeuted auf Deutsch Marktwert zu Periodenbeginn
- **MVE** → *MVE* (Market Value End) bedeutet auf Deutsch Marktwert zum Periodenende
- **Cash flow** → *Cashflow*
- **Transaction** → *Transaktion*
- **Security** → *Wertpapier* oder *Aktie* muss im Kontext entschieden werden.

- **Security Account** → *Depot*

- **Cash Account** → Konto oder Verrechnungskonto muss im Kontext entschieden werden.

#### Grammatik und Stil
- Verwende aktive Sprache aber halte dich im Grundsatz an den Stiel aus dem Englischen Text
- Halte Sätze kurz und prägnant
- Verwende passende Formulierungen für technische Dokumentation

### 2. Formatierung

#### Markdown-Elemente
- Behalte alle Markdown-Formatierungen bei
- Übersetze nur den Textinhalt, nicht die Formatierung
- Beachte die korrekte Verwendung von Headings (#, ##, ###)
- Achte auf korrekte Listen und Aufzählungen
- Links zu Bilder aus dem Englsichen Original bleiebn voerst auch auf Englisch. Diese zu verlinken ist fürs erste OK.

#### Code-Blöcke
- Übersetze keine Code-Blöcke
- Kommentare in Code-Blöcken können übersetzt werden, wenn sinnvoll
- Variablen- und Funktionsnamen bleiben unverändert

### 3. Stilistische Richtlinien

#### Klarheit
- Verwende klare und prägnante Sprache
- Vermeide unnötige Wiederholungen
- Halte die Lesbarkeit hoch

#### Konsistenz
- Verwende konsistente Terminologie
- Erstelle eine Glossar-Datei für wichtige Begriffe
- Beachte die Namensgebung (z.B. "Portfolio-Help", "Dokumentation")

### 4. Spezielle Anweisungen

#### Bilder und Dateinamen
- Bilder werden nicht übersetzt
- Dateinamen und Pfade bleiben unverändert
- Links zu externen Ressourcen werden nicht übersetzt

#### Beispiele
- Beispiele sollten übersetzt werden, wenn sie verständlich sind
- Bei technischen Beispielen: Verwende den gleichen Code-Formatierungsstil

### 5. Qualitätssicherung

#### Prüfungen vor der Übersetzung
- Überprüfe die englische Version auf Vollständigkeit
- Stelle sicher, dass alle Links funktionieren
- Prüfe die Formatierung

#### Nach der Übersetzung
- Überprüfe die Übersetzung auf Konsistenz
- Prüfe, ob alle Markdown-Formatierungen erhalten geblieben sind
- Teste die Lesbarkeit in der Zielsprache

### 6. Glossar

| Englisch | Deutsch |
|----------|---------|
| Repository | Repository |
| Branch | Zweig |
| Commit | Commit |
| Deployment | Bereitstellung |
| Documentation | Dokumentation |
| Configuration | Konfiguration |

### 7. Wichtige Hinweise

1. **Konsistenz ist wichtig**: Verwende dieselben Begriffe in der gesamten Dokumentation
2. **Technische Genauigkeit**: Achte auf technische Korrektheit
3. **Lesbarkeit**: Die Übersetzung sollte flüssig und verständlich sein
4. **Formatierung**: Behalte die ursprüngliche Formatierung bei

## Kontakt für Fragen

Für Fragen zur Übersetzung wende dich an:
- [Sn1kk3r5]
- [https://forum.portfolio-performance.info/]

## Versionshistorie

- Version 1.0 (2024): Erste Version
```

### 4. Datei speichern und commiten

```bash
# Speichere die Datei
git add TRANSLATION_GUIDELINES.md
git commit -m "Add translation guidelines for documentation"
git push origin main