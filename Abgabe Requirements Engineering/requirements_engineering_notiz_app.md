# Requirements Engineering – Notiz- und Organisations-App mit KI-Dashboard

## 1. Projektbeschreibung

Im Rahmen dieses Projekts soll eine moderne Notiz- und Organisations-App entwickelt werden. Ziel der Anwendung ist es, verschiedene organisatorische Funktionen wie Notizen, Aufgabenverwaltung und Terminplanung in einer zentralen Plattform zusammenzuführen. Hintergrund der Idee ist das Problem, dass viele Nutzer unterschiedliche Anwendungen parallel verwenden und dadurch schnell den Überblick verlieren.

Die Anwendung richtet sich insbesondere an Studierende, Berufstätige und allgemein an Personen mit vielen organisatorischen Aufgaben. Neben klassischen Organisationsfunktionen soll die Anwendung auch intelligente Unterstützung bieten. Dazu gehört ein KI-basiertes „Smart Dashboard“, das wichtige Fristen erkennt, Aufgaben priorisiert und Hinweise zur besseren Zeitplanung liefert.

Ein besonderes Merkmal der Anwendung ist die Möglichkeit, einzelne Notizen oder Termine zusätzlich mit einem separaten Passwort zu schützen. Dadurch können sensible Informationen verborgen werden.

Zusätzlich müssen Datenschutz, Benutzerfreundlichkeit und Wartbarkeit berücksichtigt werden. Besonders im Bereich der KI-Funktionen spielen Transparenz und Datensicherheit eine wichtige Rolle.

---

# 2. Einsatz von Requirements Engineering

Zur Analyse und Strukturierung des Projekts wurden verschiedene Methoden des Requirements Engineering eingesetzt.

Dabei wurden:
- funktionale Anforderungen,
- nicht-funktionale Anforderungen,
- Stakeholder,
- Risiken,
- Schnittstellen,
- Prioritäten,
- Abnahmekriterien,
- Abhängigkeiten sowie
- Datenschutzanforderungen

identifiziert und dokumentiert.

Die Anforderungen wurden anhand wichtiger Qualitätsmerkmale formuliert. Dazu gehören insbesondere:
- Verständlichkeit,
- Eindeutigkeit,
- Prüfbarkeit,
- Konsistenz,
- Nachverfolgbarkeit,
- Realisierbarkeit sowie
- Kundenorientierung.

---

# 3. Werkzeug A – Self-Made Werkzeug (Excel-Tabelle)

Für die erste Dokumentation wurde eine selbst erstellte Requirements-Tabelle verwendet. Die Struktur orientiert sich an klassischen Requirements-Engineering-Attributen.

## Beispielhafte Requirements

| ID | Datum | Author | Kurzbeschreibung | Lange Beschreibung | Status | Referenz auf Use Case | Referenz auf Dokumente | Wer nimmt ab? | Abnahmekriterium | Priorität | Konflikte | Abhängigkeiten | Juristische Relevanz | Historie | Kategorie |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FR-01 | 17.05.2026 | Sebastian | Notizen speichern | Das System MUSS das Erstellen und Speichern von Notizen ermöglichen. | Offen | UC-01 | Pflichtenheft | Product Owner | Notiz wird dauerhaft gespeichert | Hoch | Keine | Datenbankmodul | Nein | Erstellt 17.05.2026 | Funktional |
| FR-02 | 17.05.2026 | Sebastian | Aufgaben verwalten | Nutzer MÜSSEN Aufgaben erstellen, bearbeiten und löschen können. | Offen | UC-02 | Pflichtenheft | Product Owner | Aufgabe erscheint korrekt in der Liste | Hoch | Keine | Benutzerverwaltung | Nein | Erstellt 17.05.2026 | Funktional |
| FR-03 | 17.05.2026 | Sebastian | Terminverwaltung | Das System MUSS Termine mit Datum und Uhrzeit speichern können. | Offen | UC-03 | Pflichtenheft | Product Owner | Termin wird im Kalender angezeigt | Hoch | Keine | Kalender-Modul | Nein | Erstellt 17.05.2026 | Funktional |
| FR-04 | 17.05.2026 | Sebastian | Passwortschutz | Einzelne Notizen SOLLEN mit zusätzlichem Passwort geschützt werden können. | Offen | UC-04 | Sicherheitskonzept | Datenschutzbeauftragter | Passwortabfrage erscheint korrekt | Mittel | Konflikt mit Usability | Verschlüsselung | Ja (DSGVO) | Erstellt 17.05.2026 | Sicherheit |
| NFR-01 | 17.05.2026 | Sebastian | Performance | Die Anwendung SOLL innerhalb von maximal 2 Sekunden reagieren. | Offen | UC-SYS-01 | Architektur-Dokument | Entwicklerteam | Antwortzeit < 2 Sekunden | Hoch | Keine | Backend-Performance | Nein | Erstellt 17.05.2026 | Nicht-funktional |
| NFR-02 | 17.05.2026 | Sebastian | Datenschutz | Sensible Nutzerdaten MÜSSEN verschlüsselt gespeichert werden. | Offen | UC-SEC-01 | Sicherheitskonzept | Datenschutzbeauftragter | Verschlüsselung aktiv | Sehr hoch | Keine | Verschlüsselungsmodul | Ja (DSGVO) | Erstellt 17.05.2026 | Sicherheit |
| AI-01 | 17.05.2026 | Sebastian | KI-Fristenerkennung | Das Smart Dashboard MUSS wichtige Fristen automatisch erkennen. | Offen | UC-AI-01 | KI-Konzept | Product Owner | Fristenwarnung erscheint | Mittel | Fehlalarme möglich | KI-Modul | Nein | Erstellt 17.05.2026 | KI |
| AI-02 | 17.05.2026 | Sebastian | KI-Planungshilfe | Das System SOLL Vorschläge zur besseren Zeitplanung erzeugen. | Offen | UC-AI-02 | KI-Konzept | Product Owner | Vorschläge werden angezeigt | Mittel | Vertrauen der Nutzer | KI-Modul | Nein | Erstellt 17.05.2026 | KI |
| SYS-01 | 17.05.2026 | Sebastian | Google-Kalender | Das System MUSS eine Schnittstelle zu Google Calendar bereitstellen. | Offen | UC-INT-01 | API-Dokumentation | Entwicklerteam | Synchronisation funktioniert | Hoch | API-Änderungen | Internetverbindung | Nein | Erstellt 17.05.2026 | Schnittstelle |
| NFR-03 | 17.05.2026 | Sebastian | Benutzerfreundlichkeit | Die Benutzeroberfläche SOLL intuitiv bedienbar sein. | Offen | UC-UI-01 | UI-Konzept | Testnutzer | Nutzer finden Funktionen ohne Anleitung | Hoch | Konflikt mit Funktionsumfang | UI-Design | Nein | Erstellt 17.05.2026 | Usability |

---

# 4. Werkzeug B – Professionelles Werkzeug

Die Umsetzung in Monday.com und Airtable findet man unter \Kommerzielles Tool und \Self Made Too Airtable

---

# 5. Fazit

Durch den Einsatz von Requirements Engineering konnten die Anforderungen des Projekts strukturiert analysiert und dokumentiert werden. Besonders hilfreich war die Unterteilung in funktionale und nicht-funktionale Anforderungen.

Die Verwendung unterschiedlicher Werkzeuge zeigte außerdem die Unterschiede zwischen einer einfachen selbst erstellten Dokumentation und professionellen Requirements-Engineering-Systemen. Während Excel für kleinere Projekte ausreichend sein kann, bieten professionelle Werkzeuge wie Jira deutlich bessere Möglichkeiten zur Verwaltung, Nachverfolgbarkeit und Zusammenarbeit innerhalb eines Teams.

Das Projekt eignet sich besonders gut für den Einsatz von Requirements Engineering, da neben klassischen Organisationsfunktionen auch moderne Themen wie KI-Unterstützung, Datenschutz und Systemschnittstellen berücksichtigt werden müssen.
