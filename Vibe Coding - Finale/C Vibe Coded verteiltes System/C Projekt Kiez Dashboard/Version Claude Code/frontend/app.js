const GATEWAY_URL = 'http://localhost:3000/gateway/dashboard-data';

const CATEGORY_LABELS = {
  wellness: 'Relax & Wellness',
  gaming: 'Nerd & Gaming',
  food: 'Food & Travel',
  work: 'Tech & Work',
};

const zipInput = document.getElementById('zip-input');
const loadButton = document.getElementById('load-button');
const resultsGrid = document.getElementById('results-grid');
const statusEl = document.getElementById('status');
const cityImageWrap = document.getElementById('city-image-wrap');
const cityImage = document.getElementById('city-image');

loadButton.addEventListener('click', loadDashboard);
zipInput.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') loadDashboard();
});

async function loadDashboard() {
  const query = zipInput.value.trim();
  if (!query) {
    setStatus('Bitte eine PLZ oder einen Ort eingeben.', true);
    return;
  }

  setStatus('Lade Daten...', false);
  resultsGrid.replaceChildren();
  cityImageWrap.classList.add('hidden');

  try {
    const res = await fetch(`${GATEWAY_URL}?query=${encodeURIComponent(query)}`);
    const data = await res.json();
    if (!res.ok) {
      throw new Error(data.error || `Gateway antwortete mit Status ${res.status}`);
    }
    renderDashboard(data);
    setStatus('', false);
  } catch (err) {
    setStatus(`Fehler: ${err.message}`, true);
  }
}

function renderDashboard(data) {
  if (data.image && data.image.url) {
    cityImage.src = data.image.url;
    cityImage.alt = data.location.city;
    cityImageWrap.classList.remove('hidden');
  }

  const cards = [buildWeatherCard(data.location, data.weather)];
  for (const [type, places] of Object.entries(data.places)) {
    cards.push(buildPlacesCard(data.location.city, type, places));
  }
  resultsGrid.replaceChildren(...cards);
}

function buildWeatherCard(location, weather) {
  const card = document.createElement('div');
  card.className = 'bg-white rounded-2xl shadow-md p-6 flex flex-col gap-2';

  const title = document.createElement('h2');
  title.className = 'text-lg font-semibold text-slate-800';
  title.textContent = location.zip ? `Wetter (${location.city}, PLZ ${location.zip})` : `Wetter (${location.city})`;

  const temp = document.createElement('p');
  temp.className = 'text-4xl font-bold text-indigo-600';
  temp.textContent = `${weather.temperature}°C`;

  const condition = document.createElement('p');
  condition.className = 'text-slate-500';
  condition.textContent = weather.condition;

  card.append(title, temp, condition);
  return card;
}

function buildPlacesCard(city, type, places) {
  const card = document.createElement('div');
  card.className = 'bg-white rounded-2xl shadow-md p-6 flex flex-col gap-3';

  const title = document.createElement('h2');
  title.className = 'text-lg font-semibold text-slate-800';
  title.textContent = CATEGORY_LABELS[type] || type;
  card.appendChild(title);

  const list = document.createElement('ul');
  list.className = 'flex flex-col gap-2';
  for (const place of places) {
    const li = document.createElement('li');

    const link = document.createElement('a');
    link.href = `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(`${place.name} ${city}`)}`;
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
    link.className = 'flex justify-between text-slate-600 hover:text-indigo-600 hover:underline';

    const name = document.createElement('span');
    name.textContent = place.name;

    const rating = document.createElement('span');
    rating.className = 'font-medium text-amber-500';
    rating.textContent = `★ ${place.rating}`;

    link.append(name, rating);
    li.appendChild(link);
    list.appendChild(li);
  }
  card.appendChild(list);
  return card;
}

function setStatus(message, isError) {
  statusEl.textContent = message;
  statusEl.className = `text-center text-sm mb-6 h-5 ${isError ? 'text-red-500' : 'text-slate-500'}`;
}
