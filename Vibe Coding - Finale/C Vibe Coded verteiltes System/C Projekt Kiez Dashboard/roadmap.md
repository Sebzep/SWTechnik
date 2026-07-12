# Projekt-Roadmap – Kiez-Dashboard

## Vision

Ein verteiltes Web-Dashboard, das Wetter- und Orts-Informationen für eine PLZ/einen Ort ohne API-Keys zusammenführt und in kleinen, dokumentierten Schritten über eine CLI-gesteuerte KI-Entwicklung entsteht.

## Iteration 1 – Infrastruktur & Grundgerüst

**Ziele**
- Projektstruktur für ein Drei-Module-System anlegen
- Orchestrierung der Module über Docker Compose vorbereiten

**Features**
- Leere Modulordner `data-service/`, `api-gateway/`, `frontend/`
- `docker-compose.yml` mit drei Services und festen Port-Mappings (8000/3000/8080)
- Internes Docker-Netzwerk, damit das Gateway den Datendienst über den Hostnamen erreicht

**Ergebnis**
- Lauffähiges, aber inhaltsleeres Grundgerüst; alle drei Container starten und sind erreichbar.
- Dokumentiert in `C Abgabe - Version Claude Code/01_step_infrastructure.md`.

## Iteration 2 – Datendienst (Python/FastAPI)

**Ziele**
- Einzige Komponente definieren, die mit externen APIs spricht
- Saubere Trennung: ein Endpunkt pro externer Quelle

**Features**
- `/api/v1/resolve` (PLZ/Ort → Koordinaten via Zippopotam + Open-Meteo Geocoding)
- `/api/v1/weather` (Open-Meteo Forecast)
- `/api/v1/places` (Overpass API, eine Kategorie pro Aufruf)
- `/api/v1/image` (Wikipedia Summary API)

**Ergebnis**
- Datendienst liefert normalisiertes JSON für alle vier Datentypen, unabhängig testbar über `/docs` (FastAPI Swagger UI).
- Dokumentiert in `02_step_data_service.md`.

## Iteration 3 – API-Gateway (Node.js/Express)

**Ziele**
- Einzigen Einstiegspunkt für das Frontend schaffen (Backend for Frontend)
- Mehrere Datendienst-Aufrufe bündeln, ohne das Frontend mit Details zu belasten

**Features**
- `/gateway/dashboard-data?query=...` löst Standort auf und ruft Wetter, Bild und alle vier Orts-Kategorien parallel ab
- Begrenzte Parallelität (2 gleichzeitige Anfragen) für Overpass-Aufrufe wegen dessen Rate-Limit
- CORS aktiviert, damit das Frontend browserseitig zugreifen kann

**Ergebnis**
- Ein einziger Request vom Frontend genügt, um alle Dashboard-Daten zu erhalten.
- Dokumentiert in `03_step_api_gateway.md`.

## Iteration 4 – Frontend (statisches HTML/CSS/JS)

**Ziele**
- Bedienbare Oberfläche ohne eigene Fachlogik
- Ausschließliche Kommunikation über das Gateway

**Features**
- Eingabefeld für PLZ/Ort mit Lade- und Fehlerzuständen
- Wetter-Karte plus vier thematische Kacheln (Relax & Wellness, Nerd & Gaming, Food & Travel, Tech & Work)
- Verlinkung der gefundenen Orte auf Google Maps, Anzeige der Entfernung in km

**Ergebnis**
- Vollständiges, End-to-End funktionierendes Dashboard ohne Mock-Daten.
- Dokumentiert in `04_step_frontend.md`.

## Ausblick (mögliche weitere Iterationen)

- Geolocation-API des Browsers als Alternative zur manuellen PLZ-Eingabe
- Caching häufiger Anfragen im Gateway, um externe Rate-Limits (insb. Overpass) zu schonen
- Automatisierte Tests pro Modul (aktuell: manuelle Validierung je Schritt, siehe Validation-Abschnitte in den Step-Dokumenten)
