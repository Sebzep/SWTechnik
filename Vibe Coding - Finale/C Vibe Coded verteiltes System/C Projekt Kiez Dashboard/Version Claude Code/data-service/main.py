import json
import random
import re
from urllib.parse import quote

import requests
from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

ZIP_PATTERN = re.compile(r"^\d{5}$")

WEATHER_CODE_DESCRIPTIONS = {
    0: "Klarer Himmel",
    1: "Ueberwiegend klar",
    2: "Teilweise bewoelkt",
    3: "Bedeckt",
    45: "Nebel",
    48: "Reifnebel",
    51: "Leichter Nieselregen",
    53: "Nieselregen",
    55: "Starker Nieselregen",
    56: "Gefrierender Nieselregen",
    57: "Starker gefrierender Nieselregen",
    61: "Leichter Regen",
    63: "Regen",
    65: "Starker Regen",
    66: "Gefrierender Regen",
    67: "Starker gefrierender Regen",
    71: "Leichter Schneefall",
    73: "Schneefall",
    75: "Starker Schneefall",
    77: "Schneegriesel",
    80: "Leichte Regenschauer",
    81: "Regenschauer",
    82: "Heftige Regenschauer",
    85: "Leichte Schneeschauer",
    86: "Starke Schneeschauer",
    95: "Gewitter",
    96: "Gewitter mit Hagel",
    99: "Gewitter mit starkem Hagel",
}

PLACE_POOLS = {
    "wellness": ["Therme Oase", "Spa Lotus", "Schwimmbad Nordpark", "Sauna Vulkan", "Wellness Refugium", "Bade-Oase Sued"],
    "gaming": ["Brettspielcafe Wuerfel", "Tabletop Arena", "Pen & Paper Lounge", "Dice & Decks", "Nerd Nook", "Retro Arcade Ecke"],
    "food": ["Thai Garden", "Pho Saigon", "Bangkok Kitchen", "Saigon Street", "Thai Orchid", "Mekong Bistro"],
    "work": ["Coworking Hub", "IT Base Camp", "Cafe Ruhepol", "Deskspace Nord", "Silent Office Lounge", "Byte Cafe"],
}

ZIPPOPOTAM_URL = "http://api.zippopotam.us/de/{plz}"
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
WIKIPEDIA_SUMMARY_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/{title}"

REQUEST_HEADERS = {"User-Agent": "Kiez-Dashboard-SchoolProject/1.0 (SWTechnik Vibe-Coding Uebungsprojekt)"}

UMLAUT_DIGRAPHS = [("ue", "u"), ("oe", "o"), ("ae", "a")]


def normalize_umlaut_spelling(text: str) -> str:
    result = text
    for digraph, replacement in UMLAUT_DIGRAPHS:
        result = re.sub(digraph, replacement, result, flags=re.IGNORECASE)
    return result


def geocode_city(name: str):
    resp = requests.get(
        GEOCODING_URL,
        params={"name": name, "count": 1, "language": "de", "country_code": "DE"},
        headers=REQUEST_HEADERS,
        timeout=5,
    )
    resp.raise_for_status()
    return json.loads(resp.content).get("results")


@app.get("/api/v1/resolve")
def resolve_location(query: str = Query(...)):
    query = query.strip()
    if not query:
        raise HTTPException(status_code=422, detail="Bitte eine PLZ oder einen Ort eingeben.")

    if ZIP_PATTERN.match(query):
        try:
            resp = requests.get(ZIPPOPOTAM_URL.format(plz=query), headers=REQUEST_HEADERS, timeout=5)
        except requests.RequestException as exc:
            raise HTTPException(status_code=502, detail="PLZ-Dienst nicht erreichbar.") from exc
        if resp.status_code != 200:
            raise HTTPException(status_code=422, detail=f"Unbekannte Postleitzahl: {query}")
        place = json.loads(resp.content)["places"][0]
        return {
            "query": query,
            "zip": query,
            "city": place["place name"],
            "lat": float(place["latitude"]),
            "lon": float(place["longitude"]),
        }

    try:
        results = geocode_city(normalize_umlaut_spelling(query))
        if not results:
            results = geocode_city(query)
    except requests.RequestException as exc:
        raise HTTPException(status_code=502, detail="Geocoding-Dienst nicht erreichbar.") from exc

    if not results:
        raise HTTPException(status_code=422, detail=f"Unbekannter Ort: {query}")
    match = results[0]
    postcodes = match.get("postcodes") or []
    return {
        "query": query,
        "zip": postcodes[0] if postcodes else None,
        "city": match["name"],
        "lat": match["latitude"],
        "lon": match["longitude"],
    }


@app.get("/api/v1/weather")
def get_weather(lat: float = Query(...), lon: float = Query(...)):
    try:
        resp = requests.get(
            FORECAST_URL,
            params={"latitude": lat, "longitude": lon, "current_weather": "true"},
            headers=REQUEST_HEADERS,
            timeout=5,
        )
        resp.raise_for_status()
    except requests.RequestException as exc:
        raise HTTPException(status_code=502, detail="Wetterdienst nicht erreichbar.") from exc

    current = json.loads(resp.content)["current_weather"]
    condition = WEATHER_CODE_DESCRIPTIONS.get(current["weathercode"], "Unbekannt")
    return {"temperature": current["temperature"], "condition": condition}


@app.get("/api/v1/places")
def get_places(type: str, city: str = Query(...)):
    pool = PLACE_POOLS.get(type.lower())
    if pool is None:
        raise HTTPException(status_code=404, detail=f"Unbekannte Kategorie: {type}")

    rng = random.Random(f"{city.lower()}:{type.lower()}")
    names = rng.sample(pool, k=3)
    ratings = [round(rng.uniform(3.5, 5.0), 1) for _ in names]
    return [{"name": name, "rating": rating} for name, rating in zip(names, ratings)]


@app.get("/api/v1/image")
def get_image(city: str = Query(...)):
    try:
        resp = requests.get(
            WIKIPEDIA_SUMMARY_URL.format(title=quote(city, safe="")),
            headers=REQUEST_HEADERS,
            timeout=5,
            allow_redirects=True,
        )
    except requests.RequestException:
        return {"city": city, "url": None}

    if resp.status_code == 200:
        data = json.loads(resp.content)
        thumbnail = (data.get("originalimage") or data.get("thumbnail") or {}).get("source")
        if thumbnail:
            return {"city": city, "url": thumbnail}

    return {"city": city, "url": None}
