# Mission – Kiez-Dashboard

## Projektidee

Das „Kiez-Dashboard" ist eine Web-Anwendung, die auf Basis einer Postleitzahl oder eines Ortsnamens auf einen Blick zeigt, was in der unmittelbaren Umgebung interessant ist: aktuelles Wetter plus themenspezifische Orte in der Nähe, gruppiert nach Interessen statt nach einer unsortierten Trefferliste.

Die Anwendung richtet sich vor allem an:

- Personen, die neu in einem Kiez/einer Stadt sind und sich schnell orientieren wollen
- Nutzer mit klaren Freizeit-Interessen (Wellness, Gaming, Essen, Arbeiten unterwegs), die nicht durch eine generische Kartenansicht scrollen wollen
- Lernende/Prüfer im Rahmen dieses Moduls, für die nachvollziehbar sein muss, wie ein verteiltes System aus mehreren unabhängigen Diensten aufgebaut wird

Das System kombiniert Standort-Auflösung, Wetterdaten und vier thematische „Highlight-Boards" (Relax & Wellness, Nerd & Gaming, Food & Travel, Tech & Work) zu einem einzigen zusammengesetzten Dashboard.

## Problemstellung

Wetter-Apps und Orts-/Karten-Apps sind getrennte Werkzeuge, die der Nutzer selbst kombinieren muss. Klassische POI-Suchen (z. B. eine Karten-App) liefern zudem unsortierte, generische Ergebnislisten statt nach persönlichen Themen gruppierter Vorschläge. Es fehlt ein einziger Einstiegspunkt, der beides – Wetter und thematisch kuratierte Orte – für eine PLZ/einen Ort in einer Ansicht zusammenführt.

Technisch kommt hinzu: viele naheliegende Datenquellen (Google Places, klassische Wetter-APIs) sind kostenpflichtig oder erfordern API-Keys, was für ein Schulprojekt vermieden werden sollte.

## Ziel des Projekts

Ziel ist ein aufgeräumtes, funktionierendes Dashboard mit:

- Standort-Eingabe per PLZ oder Ortsname
- Live-Wetterdaten (Temperatur, Wetterlage) ohne API-Key
- vier thematischen Kacheln mit den jeweils nächstgelegenen Orten inkl. Entfernungsangabe
- einem Vorschaubild der Stadt

Gleichzeitig soll das Projekt als **verteiltes System** aus drei unabhängigen, eigenständig lauffähigen Modulen (Datendienst, API-Gateway, Frontend) demonstriert werden – nicht als Monolith. Das Projekt wird parallel mit unterschiedlichen KI-Coding-Werkzeugen umgesetzt (Claude Code CLI als Hauptimplementierung, siehe `C Abgabe - Version Claude Code/`, sowie Vergleichsversionen mit Antigravity und Google Stitch), um die Werkzeuge selbst zu vergleichen – die fachliche Mission des Produkts bleibt dabei über alle Versionen gleich.

Ein bewusster Kurswechsel gegenüber der ursprünglichen Spezifikation: statt Google Places API + OpenWeatherMap (beide erfordern API-Keys) nutzt die Claude-Code-Version ausschließlich freie, schlüssellose öffentliche APIs (Zippopotam, Open-Meteo, Overpass/OpenStreetMap, Wikipedia) hinter einem eigenen Python-Datendienst. Das ergibt eine stärkere Drei-Schichten-Architektur ohne Secrets-Management, weicht aber vom Wortlaut der ursprünglichen Projektbeschreibung ab.
