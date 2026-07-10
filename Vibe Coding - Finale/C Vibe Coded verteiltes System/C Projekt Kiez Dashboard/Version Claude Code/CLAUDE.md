# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Context

This folder is one of several parallel implementations of the same assignment, built with different AI coding tools for comparison (see `../Version Antigravity`, `../Stitch Layout`). This one is built specifically using **Claude Code CLI** — that constraint matters: the point of this folder is to demonstrate CLI-driven, step-by-step development, not just to produce a working app.

Full feature spec: `../projektbeschreibung Kiez Dashboard.md` (Kiez-Dashboard — local highlights + weather for a given postal code/city, combining a weather widget with themed Google Places POI tiles: Relax & Wellness, Nerd & Gaming, Food & Travel, Tech & Work).

## Assignment requirements (binding)

From the top-level task (`../../Grand Finale - Alle Erfahrungen.md`):
- Must be a **distributed system** — a client-server app with clearly separate modules, not a monolith.
- Must be built/proven via CLI (this folder's purpose), while also proving the *other* tool (VS Code-like IDE) was installed and used elsewhere.
- Must be understood completely — be able to explain any part of the code, not just accept generated output.
- Must be developed in **small, incremental steps, each documented in its own markdown file** (see `Commando1.md` — subsequent steps should follow the same `CommandoN.md` naming pattern, one file per prompt/step).

## Architecture (per projektbeschreibung)

Client-server split:
- **Client**: static frontend (HTML/CSS/JS), TailwindCSS via CDN for styling. Renders the dashboard, handles user input (PLZ/city), no business logic beyond fetch + render.
- **APIs (backend nodes)**: Google Places API for POI tiles, a separate weather API (Google no longer offers a free weather API — e.g. OpenWeatherMap) for the weather widget. These are external services the client calls directly, not a custom backend — the "distributed system" boundary is client ↔ third-party API services, so keep API-calling code isolated per service (don't intermix Places-fetching logic with weather-fetching logic in the same function/module).

## Current state

No code has been written yet in this folder. `Commando1.md` holds the first prompt: build `index.html` + `style.css` (Tailwind via CDN) implementing the dashboard layout (projektbeschreibung §2, §3.1) — icon-based placeholder tiles, and a settings menu with working toggle switches.

## Style precedent

`../Version Antigravity/index.html` is a sibling implementation of the same spec (different tool). It uses Tailwind CDN with `darkMode: "class"`, Material Symbols Outlined icons, and a custom Material-3-style color palette defined inline in `tailwind.config`. Not required to match, but useful as a reference for one way the layout/spec was already interpreted.

## Workflow for this folder

- Each new build step gets its own `CommandoN.md` file recording the prompt/instruction given, before or alongside implementation — this is graded, not optional.
- No build tooling: plain static HTML/CSS/JS + Tailwind CDN. Serve locally with any static server (e.g. `npx serve .`) to view.
