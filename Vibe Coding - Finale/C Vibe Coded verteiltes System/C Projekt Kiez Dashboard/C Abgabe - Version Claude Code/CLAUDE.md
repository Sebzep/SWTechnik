# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Context

This folder is one of several parallel implementations of the same assignment, built with different AI coding tools for comparison (see `../Version Antigravity`, `../Stitch Layout`). This one is built specifically using **Claude Code CLI** — that constraint matters: the point of this folder is to demonstrate CLI-driven, step-by-step development, not just to produce a working app.

Full feature spec: `../projektbeschreibung Kiez Dashboard.md` (Kiez-Dashboard — local highlights + weather for a given postal code/city, combining a weather widget with themed POI tiles: Relax & Wellness, Nerd & Gaming, Food & Travel, Tech & Work).

## Assignment requirements (binding)

From the top-level task (`../../Grand Finale - Alle Erfahrungen.md`):
- Must be a **distributed system** — a client-server app with clearly separate modules, not a monolith.
- Must be built/proven via CLI (this folder's purpose), while also proving the *other* tool (VS Code-like IDE) was installed and used elsewhere.
- Must be understood completely — be able to explain any part of the code, not just accept generated output.
- Must be developed in **small, incremental steps, each documented in its own markdown file** — see `00_architecture.md` and `01_step_infrastructure.md` through `04_step_frontend.md`. Any further step gets its own `NN_step_<name>.md` file, same pattern.

## Architecture (as built — see `00_architecture.md`)

Three independent modules communicating via HTTP/REST, orchestrated with Docker Compose:

- **`data-service/`** (Module A) — Python/FastAPI. Owns all outbound calls to external data providers and normalizes their responses. Endpoints: `/api/v1/resolve` (PLZ or city name → lat/lon/city via Zippopotam + Open-Meteo geocoding), `/api/v1/weather` (Open-Meteo forecast), `/api/v1/places` (Overpass API, one query per category), `/api/v1/image` (Wikipedia summary API for a city thumbnail).
- **`api-gateway/`** (Module B) — Node.js/Express BFF. Exposes `/gateway/dashboard-data?query=...`, resolves the location then fans out to weather/image/places on the data-service concurrently (places lookups are limited to 2 concurrent requests — Overpass's own rate limit), merges everything into one JSON response, has CORS enabled. This is the *only* module the frontend talks to.
- **`frontend/`** (Module C) — static HTML/CSS/JS, TailwindCSS via CDN. No business logic beyond fetch + render; only ever calls the API gateway, never the data-service or external APIs directly.

**Deviation from the original spec worth knowing:** the spec originally called for Google Places API + OpenWeatherMap (called directly from the frontend, no BFF). The implementation instead uses free, keyless public APIs end-to-end (Zippopotam, Open-Meteo, Overpass, Wikipedia) fetched through the Python data-service, with the Node gateway as BFF in front of it — this is a stronger three-tier distributed-system story (and needs no API keys/secrets) but is a real divergence from the written spec, so it's worth being able to explain *why* in a walkthrough.

## Current state

All four build steps are implemented and working end-to-end: infrastructure/Docker scaffolding, data-service, api-gateway, frontend. No mock data remains — all endpoints hit live external services.

## Running it

Two ways to run, both already wired up:

- **Docker Compose** (`docker-compose.yml`): `docker compose up` — data-service on `:8000`, api-gateway on `:3000`, frontend served by nginx on `:8080`.
- **Local dev without Docker** (`start-dev.ps1` / `stop-dev.ps1`): starts uvicorn, node, and a plain `python -m http.server` for the frontend directly on the host, logging to `logs/*.log`. Frontend here is on `:8090` (not `:8080` — different from the Docker path since nginx isn't in the loop). Use `stop-dev.ps1` to tear it down again.

## Style precedent

`../Version Antigravity/index.html` is a sibling implementation of the same spec (different tool). It uses Tailwind CDN with `darkMode: "class"`, Material Symbols Outlined icons, and a custom Material-3-style color palette defined inline in `tailwind.config`. Not required to match, but useful as a reference for one way the layout/spec was already interpreted.

## Workflow for this folder

- Each new build step gets its own `NN_step_<name>.md` file recording the prompt/instruction given, before or alongside implementation — this is graded, not optional.
- Keep API-calling code isolated per external service (already the case in `data-service/main.py` — resolve/weather/places/image are separate functions/endpoints); don't intermix concerns when extending it.
