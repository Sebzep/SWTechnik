# Kiez-Dashboard: Module & warum das ein verteiltes System ist

## Die drei Module

### 1. `data-service/` — Python (FastAPI), Port 8000
Der einzige Baustein, der mit der Außenwelt spricht. Er kennt keine PLZ-Eingabefelder oder HTML — er bekommt fertige Parameter (z. B. `lat`/`lon` oder eine PLZ) und liefert normalisiertes JSON zurück. Vier Endpunkte, jeder für genau eine externe Quelle zuständig:

- `/api/v1/resolve` — PLZ oder Ortsname → Koordinaten + Stadtname (Zippopotam + Open-Meteo Geocoding)
- `/api/v1/weather` — aktuelles Wetter für Koordinaten (Open-Meteo Forecast)
- `/api/v1/places` — POIs einer Kategorie (wellness/gaming/food/work) in der Nähe (Overpass API, OpenStreetMap-Daten)
- `/api/v1/image` — ein Vorschaubild zur Stadt (Wikipedia)

### 2. `api-gateway/` — Node.js (Express), Port 3000
Die Vermittlungsstelle ("Backend for Frontend"). Nimmt genau eine Anfrage vom Frontend entgegen (`/gateway/dashboard-data?query=...`), ruft dafür intern mehrere Endpunkte des Data-Service parallel auf (Wetter, Bild, vier Orts-Kategorien), fasst alle Antworten zu einem einzigen JSON-Objekt zusammen und schickt sie ans Frontend zurück. Das Frontend muss so nicht wissen, dass im Hintergrund fünf verschiedene Abfragen laufen.

### 3. `frontend/` — statisches HTML/CSS/JS + TailwindCSS
Die Oberfläche. Nimmt PLZ/Ort entgegen, zeigt Ladezustand/Fehler an, rendert die Antwort als Karten. Enthält keine eigene Fachlogik und redet ausschließlich mit dem API-Gateway — nie direkt mit dem Data-Service oder mit Zippopotam/Open-Meteo/Overpass/Wikipedia.

## Warum ist das ein verteiltes System?

Ein verteiltes System besteht aus mehreren eigenständigen Prozessen, die über ein Netzwerk (nicht über normale Funktionsaufrufe im selben Programm) zusammenarbeiten. Das trifft hier zu:

- **Getrennte Prozesse, getrennte Laufzeitumgebungen.** Frontend läuft im Browser, das Gateway ist ein eigener Node-Prozess, der Data-Service ein eigener Python-Prozess. Jedes Modul hat eigene Abhängigkeiten (`package.json` vs. `requirements.txt`) und könnte auf einem anderen Rechner laufen, ohne dass sich am Code etwas ändern müsste.
- **Kommunikation nur über HTTP.** Die drei Module rufen sich gegenseitig ausschließlich über REST-Endpunkte auf (`fetch(...)` im Frontend, `fetch`/`requests` zwischen Gateway und Data-Service). Es gibt keinen gemeinsamen Speicher und keinen direkten Funktionsaufruf über Modulgrenzen hinweg.
- **Klare, einseitige Abhängigkeitskette.** Frontend → Gateway → Data-Service → externe APIs. Jedes Modul kennt nur seinen direkten Nachbarn, nie die Schicht dahinter (das Frontend weiß z. B. nichts von Overpass oder Open-Meteo).
- **Unabhängig deploybar.** `docker-compose.yml` startet jedes Modul als eigenen Container mit eigenem Port; sie könnten genauso gut auf drei verschiedenen Servern laufen — die Docker-internen Hostnamen (`data-service`, `api-gateway`) sind bereits Netzwerkadressen, keine lokalen Importe.
- **Unabhängig austauschbar/skalierbar.** Der Data-Service könnte durch eine andere Sprache ersetzt werden, ohne dass Frontend oder Gateway etwas davon merken, solange die HTTP-Schnittstelle gleich bleibt — ein klassisches Merkmal verteilter Systeme (lose Kopplung über eine stabile Schnittstelle).

Kurz: Es ist kein Monolith mit internen Modulen, sondern drei getrennte Programme in getrennten Prozessen/Containern, die ausschließlich über Netzwerk-Requests miteinander reden.
