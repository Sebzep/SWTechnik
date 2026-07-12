# Step 3: API Gateway Module (Node.js)

## Task
Read `00_architecture.md` for context. Navigate into the `/api-gateway` directory and build the Node.js BFF (Backend for Frontend).

## Requirements
1.  Initialize a basic Node.js project (`package.json`) and use Express.
2.  Create an `index.js` file.
3.  Implement a route `/gateway/dashboard-data?zip={zipcode}`.
4.  When this route is called, the Gateway must make internal HTTP requests to the Data Service (Module A) at `http://data-service:8000` to fetch both Weather and Places data.
5.  Combine the responses from Module A into a single JSON object and return it to the client.
6.  Enable CORS so the frontend can access this gateway.
7.  Create a `Dockerfile` for this module to run the Express server on port 3000.

## Implementation
- `package.json` with `express` and `cors` as dependencies; native `fetch` (Node 18+) used for internal HTTP calls instead of an extra HTTP client library.
- `index.js` implements `GET /gateway/dashboard-data?query=...` (query accepts a PLZ or a city name, matching the data-service's `resolve` endpoint rather than a `zip`-only param as originally scoped):
  1. Calls `/api/v1/resolve` on the data service to turn the query into `{ city, lat, lon }`.
  2. Fires weather, image, and all four place-category lookups off that location — weather and image run unthrottled, while the four place lookups run through a small custom `mapWithConcurrencyLimit` helper capped at 2 concurrent requests, since Overpass rate-limits at 2 concurrent queries per client.
  3. Merges everything into one JSON object (`{ location, weather, image, places: { wellness, gaming, food, work } }`) and returns it.
- A failed place lookup for one category is caught individually and returned as `null` for that category instead of failing the whole request — the other three categories, weather, and the image still come back.
- CORS enabled globally via the `cors` middleware so the static frontend (different origin/port) can call the gateway from the browser.
- `Dockerfile` installs dependencies and runs `node index.js` on port 3000.

## Validation
- Manual `curl`/browser requests to `http://localhost:3000/gateway/dashboard-data?query=12047` (and a city-name variant) with the data service running, checking the merged response contains `location`, `weather`, `image`, and all four `places` keys.
- Verified the missing-`query`-parameter case returns `400` with an explanatory error instead of crashing.
- Verified the concurrency limiter: with all four place categories requested, no more than 2 Overpass requests are in flight at once (checked via data-service logs), avoiding Overpass rate-limit rejections.
- Verified partial-failure handling by temporarily pointing one category at an invalid Overpass filter and confirming the gateway still returns a full response with that one category set to `null` rather than a 502 for the whole request.
- Confirmed cross-container reachability: gateway resolves `http://data-service:8000` correctly when run via `docker compose up` (ties back to the networking set up in Step 1).