# Projektbeschreibung: Kiez-Dashboard (Local Highlights & Weather)

## 1. Vision & Ziel
Das Kiez-Dashboard ist eine interaktive Web-Anwendung, die dem Nutzer auf einen Blick die wichtigsten Informationen und Highlights zu seinem aktuellen Standort (basierend auf Postleitzahl und Stadt) liefert. 
Ziel ist es, ein aufgeräumtes UI zu schaffen, das aktuelle Wetterdaten mit themenspezifischen "Points of Interest" (POIs) kombiniert. Es dient als zentraler Hub, um die eigene Umgebung gezielt nach bestimmten Interessen zu scannen.

## 2. Kernfunktionen (Features)

### 2.1 Standort-Initialisierung
* Eingabefeld für Postleitzahl (z. B. "12047") und Stadt (z. B. "Berlin").
* Optional: Automatische Standortermittlung über die Geolocation API des Browsers.

### 2.2 Wetter-Widget
* Abruf der aktuellen Wetterdaten für die angegebene PLZ.
* Anzeige von Temperatur, Wetterlage (Icon) und einer kurzen Prognose für den Tag.
* *(Hinweis: Da Google keine klassische, kostenfreie Wetter-API mehr anbietet, kann hierfür z. B. die OpenWeatherMap API oder eine vergleichbare Alternative angebunden werden, während Google für die POIs zuständig bleibt).*

### 2.3 Thematische Highlight-Boards (POIs via Google Places API)
Das Dashboard bietet verschiedene "Themen-Kacheln", die über die Google Places API dynamisch gefüllt werden. Nutzer können auf ein Thema klicken, um sich die bestbewerteten Orte in der Nähe als Liste oder auf einer kleinen Karten-Ansicht anzeigen zu lassen:

* **Relax & Wellness:** Suche nach nahegelegenen Thermen, Spas oder Schwimmbädern zum Entspannen.
* **Nerd & Gaming:** Lokale Tabletop-Shops, Pen-&-Paper-Treffpunkte oder Brettspielcafés.
* **Food & Travel:** Authentische asiatische Küche (mit Fokus auf thailändische oder vietnamesische Restaurants) im aktuellen Kiez.
* **Tech & Work:** Coworking-Spaces, IT-Hubs oder ruhige Cafés zum Arbeiten und Lernen.

## 3. Architektur & Tech-Stack (Verteiltes System)

Das Projekt wird als klassisches **Client-Server-Modell** (Verteiltes System) umgesetzt:

* **Client (Frontend):** 
  * Ein responsives Dashboard-UI (z. B. HTML/CSS/Vanilla JS oder ein leichtgewichtiges Framework wie Vue.js).
  * Nutzt TailwindCSS für schnelles, modernes Vibe-Coding-Styling.
  * Hier passiert das Rendering und die Auswertung der Usereingaben.
* **APIs (Backend-Knoten):**
  * **Google Places API:** Nimmt die Geodaten (PLZ/Stadt) und die Such-Tags (z. B. "Therme", "Tabletop") entgegen und liefert strukturierte JSON-Daten mit Namen, Ratings und Öffnungszeiten zurück.
  * **Wetter-API:** Liefert die meteorologischen Echtzeitdaten.

## 4. Nächste Schritte (Roadmap)
1. **API-Keys generieren:** Google Cloud Console Projekt anlegen und Places API aktivieren; Wetter-API Key besorgen.
2. **UI-Prototyping:** Das Basis-Layout (Grid oder Flexbox) für das Dashboard mit Platzhaltern für das Wetter und die Themen-Kacheln bauen.
3. **Logik-Implementierung:** Fetch-Requests an die APIs schreiben und das JSON-Mapping für die Kacheln umsetzen.
4. **Refinement:** Fehlerbehandlung (Was passiert, wenn eine PLZ nicht gefunden wird?) und Feinschliff des Designs.