# Tech Stack – Kiez-Dashboard

## Modul A: Datendienst

**Sprache/Framework:** Python + FastAPI

FastAPI wurde gewählt, weil es typisierte Query-Parameter, automatische Validierung und eine Swagger-UI (`/docs`) kostenlos mitbringt – nützlich, um jeden Endpunkt einzeln zu testen, ohne das Gateway oder Frontend zu benötigen.

**Server:** Uvicorn (ASGI)

**Externe Datenquellen** (alle ohne API-Key):
- Zippopotam (`api.zippopotam.us`) – PLZ → Koordinaten/Stadtname
- Open-Meteo Geocoding – Ortsname → Koordinaten (Fallback, wenn keine PLZ eingegeben wird)
- Open-Meteo Forecast – aktuelles Wetter
- Overpass API (OpenStreetMap-Daten) – Orte je Kategorie im Umkreis
- Wikipedia REST Summary API – Vorschaubild zur Stadt

## Modul B: API-Gateway

**Sprache/Framework:** Node.js + Express

Express als schlanker HTTP-Server für die BFF-Rolle (Backend for Frontend); native `fetch` für die internen Aufrufe an den Datendienst, kein zusätzliches HTTP-Client-Paket nötig.

**Middleware:** `cors` (npm-Paket), damit das statische Frontend browserseitig zugreifen darf.

**Besonderheit:** eigene kleine Concurrency-Limit-Funktion (`mapWithConcurrencyLimit`) statt einer externen Queue-Bibliothek, um Overpass' Limit von 2 gleichzeitigen Anfragen einzuhalten.

## Modul C: Frontend

**Technologie:** statisches HTML/CSS/JavaScript (kein Build-Schritt, kein Framework)

**Styling:** TailwindCSS via CDN – schnelles, modernes Styling ohne eigene Build-Pipeline, passend zum Anspruch, jeden Teil des Codes ohne Toolchain nachvollziehen zu können.

**Rendering:** Vanilla JS mit direkter DOM-Erzeugung (`document.createElement`), keine Templating-Bibliothek.

## Infrastruktur & Orchestrierung

**Containerisierung:** Docker, ein `Dockerfile` pro Modul.

**Orchestrierung:** Docker Compose (`docker-compose.yml`) – startet alle drei Module mit festen Port-Mappings (8000/3000/8080) und internem Netzwerk, sodass das Gateway den Datendienst über den Hostnamen `data-service` statt über `localhost` erreicht.

**Alternative lokale Ausführung ohne Docker:** `start-dev.ps1`/`stop-dev.ps1` (PowerShell) starten Uvicorn, Node und einen einfachen `python -m http.server` direkt auf dem Host (Frontend dann auf Port 8090 statt 8080, da kein nginx dazwischenliegt).

## Versionsverwaltung

Git + GitHub, ein Repository für alle parallelen Tool-Implementierungen (Claude Code, Antigravity, Google Stitch) dieses Vergleichsprojekts.

## Entwicklungswerkzeug

Claude Code CLI – bewusst gewählt, um die Umsetzung ausschließlich über eine Kommandozeilen-gesteuerte KI-Entwicklung zu demonstrieren (im Gegensatz zu den IDE-basierten Vergleichsversionen). Jeder Baustein wurde in einem eigenen, dokumentierten Schritt (`01_step_infrastructure.md` bis `04_step_frontend.md`) angefordert und umgesetzt.

## Bewusste Abweichung vom ursprünglichen Tech-Stack der Spezifikation

Die ursprüngliche Projektbeschreibung sah Google Places API und OpenWeatherMap vor, beide direkt vom Frontend aus aufgerufen. Umgesetzt wurde stattdessen ausschließlich mit freien, schlüssellosen APIs hinter einem eigenen Backend (Datendienst + Gateway) – kein Secrets-Management nötig, dafür eine zusätzliche Schicht Server-Code.
