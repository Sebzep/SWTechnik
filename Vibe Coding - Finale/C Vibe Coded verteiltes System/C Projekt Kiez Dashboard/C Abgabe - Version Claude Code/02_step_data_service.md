# Step 2: Data Fetcher Module (Python)

## Task
Read `00_architecture.md` for context. Navigate into the `/data-service` directory and build the Python backend.

## Requirements
1.  Use Python with FastAPI.
2.  Create a `requirements.txt` containing `fastapi` and `uvicorn`.
3.  Create a `main.py` with two GET endpoints:
    * `/api/v1/weather?zip={zipcode}` -> Returns mock weather data (temperature, condition) as JSON.
    * `/api/v1/places?type={type}&zip={zipcode}` -> Returns an array of 3 mock locations (name, rating) as JSON.
4.  Create a `Dockerfile` for this specific module to run the Uvicorn server on port 8000.

## Implementation
- `requirements.txt`: `fastapi`, `uvicorn`, plus `requests` for outbound calls to external APIs.
- `main.py` grew beyond the two originally scoped endpoints into four, each owning exactly one external data source:
  - `/api/v1/resolve?query=...` — accepts either a 5-digit PLZ (via Zippopotam) or a free-text city name (via Open-Meteo Geocoding, with an umlaut-digraph fallback like `ue`→`u` for inputs typed without proper umlauts); returns city name + lat/lon.
  - `/api/v1/weather?lat=...&lon=...` — Open-Meteo Forecast current weather, mapped from numeric weather codes to German-language conditions via a lookup table.
  - `/api/v1/places?type=...&lat=...&lon=...` — Overpass API query built per category (`wellness`, `gaming`, `food`, `work`) from a filter map, deduplicated by name, distance computed with a haversine helper, sorted, top 3 returned.
  - `/api/v1/image?city=...` — Wikipedia REST summary API, returns a thumbnail URL or `null` if none found (never errors the whole dashboard just for a missing image).
- Deviation from the original requirement: mock JSON was replaced with live calls to free, keyless public APIs end-to-end (Zippopotam, Open-Meteo, Overpass, Wikipedia) — see `mission.md`/`techstack.md` in the parent project folder for the rationale.
- All outbound requests set a descriptive `User-Agent` header and a timeout; failures are surfaced as `HTTPException` with a German-language `detail` message rather than propagating raw exceptions.
- `Dockerfile` installs `requirements.txt` and runs `uvicorn main:app --host 0.0.0.0 --port 8000`.

## Validation
- Manual smoke tests via FastAPI's auto-generated `/docs` Swagger UI, and directly with `curl`/browser against `http://localhost:8000/api/v1/...` for each endpoint individually, before the gateway existed.
- Verified `/api/v1/resolve` with both a valid PLZ (e.g. `12047`) and a city name typed without umlauts (e.g. `Koeln`) to confirm the digraph-normalization fallback triggers correctly.
- Verified `/api/v1/places` returns at most 3 deduplicated, distance-sorted results per category, and returns `404` for an unknown category.
- Verified error paths return a `502`/`422` with a readable message instead of a raw stack trace when an upstream API is unreachable or the input is invalid (e.g. a non-existent PLZ).