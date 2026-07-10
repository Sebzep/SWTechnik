# Projektbeschreibung: Google Stitch (Dein personalisierter Kiez-Teppich)

## 1. Vision & Ziel
"Google Stitch" ist ein modulares, hochgradig personalisierbares Kiez-Dashboard. Die App "verstitcht" (verbindet) Echtzeitdaten aus der Google Places API, Event-Feeds und Wetter-Diensten zu einer maßgeschneiderten Übersicht für die eigene Postleitzahl. 

Das Besondere: Das UI ist nicht starr. Der Nutzer entscheidet selbst, welche Themen-Sektionen ihn interessieren, und kann das Layout dynamisch per Drag-and-Drop an seine Vorlieben anpassen.

## 2. Das Modulare Dashboard (Sektionen)
Das UI besteht aus einem flexiblen Grid-Layout. Jede Sektion wird als eigenständige "Karte" (Widget) dargestellt:

*   **Sektion: Wetter**
    *   Zeigt das aktuelle Wetter und eine kurze Tagesprognose für die eingegebene PLZ.
*   **Sektion: Restaurants**
    *   Zieht über die Google Places API die am besten bewerteten Restaurants im Kiez (z. B. mit Filtermöglichkeit nach Küche wie Vietnamesisch/Thailändisch).
*   **Sektion: Cafés**
    *   Listet gemütliche Cafés, Röstereien oder Laptop-freundliche Arbeitsorte in der direkten Umgebung auf.
*   **Sektion: Events**
    *   Zeigt aktuelle Veranstaltungen, Flohmärkte, Kultur-Highlights oder Kiez-Events in der Stadt/PLZ (Anbindung über eine Event-API oder einen lokalen RSS/JSON-Feed).

## 3. Personalisierung & UI-Features (Die "Stitch"-Logik)

### 3.1 Sektions-Einstellungen (Aktivieren / Deaktivieren)
*   Über ein ausklappbares **Einstellungs-Menü (Sidebar oder Modal)** kann der Nutzer jede Sektion über einfache Toggle-Schalter (An/Aus) aktivieren oder deaktivieren.
*   Deaktivierte Sektionen verschwinden sofort aus dem Dashboard, um Platz zu sparen, und können jederzeit wieder zugeschaltet werden.

### 3.2 Dynamisches Verschieben (Drag-and-Drop)
*   Die Sektionen lassen sich flexibel anordnen. Wenn der Nutzer die Events lieber ganz oben links statt unten rechts sehen möchte, kann er die Kachel einfach per Maus (oder Touch) an die gewünschte Position ziehen.
*   *Vibe-Coding-Tipp:* Hierfür nutzen wir eine leichtgewichtige Bibliothek wie `SortableJS` oder natives HTML5 Drag and Drop, das die KI direkt fehlerfrei implementieren kann.

### 3.3 State Persistence (Speichern im Browser)
*   Damit die mühsam eingerichtete Anordnung und die aktivierten Sektionen nach einem Seiten-Reload nicht verloren gehen, wird der Zustand des Dashboards (Positionen und Sichtbarkeit) automatisch im `localStorage` des Browsers gespeichert.

## 4. Tech-Stack & Architektur

*   **Frontend:** HTML5, TailwindCSS (für das flexible Grid-Layout und die Karten-Designs), Vanilla JavaScript.
*   **Bibliotheken:** `SortableJS` (für flüssiges Drag-and-Drop ohne Framework-Overhead).
*   **Schnittstellen (Verteiltes System):**
    *   *Google Places API:* Liefert die POI-Daten für die Sektionen "Restaurants" und "Cafés".
    *   *Wetter-API (z. B. OpenWeather):* Liefert die meteorologischen Daten für das Wetter-Widget.
    *   *Event-API:* Liefert die lokalen Veranstaltungs-Highlights.

## 5. Roadmap für die KI (Vibe Coding Prompting)
1.  **Schritt 1:** Erstelle das Grundlayout mit einer Sidebar für die Einstellungen und einem CSS-Grid für die vier Hauptkacheln (Wetter, Restaurants, Cafés, Events).
2.  **Schritt 2:** Implementiere die Sichtbarkeits-Toggle in den Einstellungen, um Kacheln aus- und einzublenden.
3.  **Schritt 3:** Integriere `SortableJS`, damit die Kacheln verschoben werden können, und speichere das Layout im `localStorage`.
4.  **Schritt 4:** Binde die APIs (Google Places & Wetter) an, um die Platzhalter-Karten mit echten Daten aus dem Kiez zu füllen.