const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());

const DATA_SERVICE_URL = process.env.DATA_SERVICE_URL || 'http://data-service:8000';
const PLACE_TYPES = ['wellness', 'gaming', 'food', 'work'];

async function fetchJson(url) {
  const res = await fetch(url);
  const body = await res.json().catch(() => ({}));
  if (!res.ok) {
    throw Object.assign(new Error(body.detail || 'Data service error'), { status: res.status });
  }
  return body;
}

// Overpass (used for places lookups) only allows 2 concurrent queries per client.
const OVERPASS_CONCURRENCY = 2;

async function mapWithConcurrencyLimit(items, limit, fn) {
  const results = new Array(items.length);
  let next = 0;
  async function worker() {
    while (next < items.length) {
      const i = next++;
      results[i] = await fn(items[i]);
    }
  }
  await Promise.all(Array.from({ length: limit }, worker));
  return results;
}

app.get('/gateway/dashboard-data', async (req, res) => {
  const { query } = req.query;
  if (!query) {
    return res.status(400).json({ error: 'Missing required query parameter: query' });
  }

  try {
    const location = await fetchJson(`${DATA_SERVICE_URL}/api/v1/resolve?query=${encodeURIComponent(query)}`);
    const city = location.city;

    const [weather, image, placeEntries] = await Promise.all([
      fetchJson(`${DATA_SERVICE_URL}/api/v1/weather?lat=${location.lat}&lon=${location.lon}`),
      fetchJson(`${DATA_SERVICE_URL}/api/v1/image?city=${encodeURIComponent(city)}`),
      mapWithConcurrencyLimit(PLACE_TYPES, OVERPASS_CONCURRENCY, async (type) => {
        try {
          const places = await fetchJson(`${DATA_SERVICE_URL}/api/v1/places?type=${type}&lat=${location.lat}&lon=${location.lon}`);
          return [type, places];
        } catch (err) {
          console.error(`places lookup failed for ${type}:`, err.message);
          return [type, null];
        }
      }),
    ]);

    res.json({
      location,
      weather,
      image,
      places: Object.fromEntries(placeEntries),
    });
  } catch (err) {
    res.status(err.status || 502).json({ error: err.message || 'Failed to reach data service' });
  }
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`API Gateway listening on port ${PORT}`);
});
