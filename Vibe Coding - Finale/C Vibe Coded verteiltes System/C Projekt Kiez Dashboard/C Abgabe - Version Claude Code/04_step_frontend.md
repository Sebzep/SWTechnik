# Step 4: Frontend Module

## Task
Read `00_architecture.md` for context. Navigate into the `/frontend` directory and build the user interface.

## Requirements
1.  Create an `index.html` file.
2.  Include TailwindCSS via CDN for styling.
3.  Build a simple UI with an input field for a zip code and a "Load Dashboard" button.
4.  Create an `app.js` file.
5.  Write a function that fetches data from `http://localhost:3000/gateway/dashboard-data?zip=...` when the button is clicked.
6.  Render the returned JSON data into clean CSS-Grid cards on the screen.

## Implementation
- `index.html` uses TailwindCSS via CDN, a text input for PLZ/city plus a "Load Dashboard" button, a status line for loading/error states, an optional city thumbnail, and a CSS-grid results area.
- `app.js` calls `GET http://localhost:3000/gateway/dashboard-data?query=...` on button click or Enter key, driven by a `query` param (PLZ or free-text place name) matching the gateway's actual contract rather than a `zip`-only param.
- Rendering builds one weather card plus one card per place category (`Relax & Wellness`, `Nerd & Gaming`, `Food & Travel`, `Tech & Work`) via direct DOM construction (`document.createElement`), no templating library.
- Each place entry links out to a Google Maps search for that place name + city, and shows the distance in km returned by the data service.
- Distinguishes two non-error-but-empty states per category card: `places === null` (upstream lookup failed, shown as an amber "service unavailable" message) vs. an empty array (no results found nearby, shown as a neutral message) — surfacing the gateway's partial-failure handling from Step 3 instead of hiding it.
- The frontend contains no business logic beyond fetch + render, and only ever talks to the gateway, never to the data service or external APIs directly.

## Validation
- Manual end-to-end test in the browser: entered a valid PLZ, confirmed weather card and all four category cards render with real data and a city thumbnail, with the full stack running via `docker compose up` (frontend on `:8080`).
- Repeated with a city name instead of a PLZ, and with an invalid/unknown PLZ, confirming the status line shows a readable German error message instead of a broken UI.
- Verified the `places === null` vs. empty-array distinction renders differently by forcing an Overpass failure and, separately, querying a PLZ with genuinely no nearby matches for one category.
- Verified the non-Docker dev path (`start-dev.ps1`) serves the frontend on `:8090` and still successfully reaches the gateway on `:3000`.