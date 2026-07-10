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
      Promise.all(
        PLACE_TYPES.map(async (type) => [
          type,
          await fetchJson(`${DATA_SERVICE_URL}/api/v1/places?type=${type}&city=${encodeURIComponent(city)}`),
        ])
      ),
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
