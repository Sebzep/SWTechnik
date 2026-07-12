# Step 1: Infrastructure and Scaffolding

## Task
Read `00_architecture.md` for context. Your task is to set up the foundational folder structure and the Docker orchestration for our distributed system.

## Requirements
1.  Create three empty directories in the root: `/data-service`, `/api-gateway`, and `/frontend`.
2.  Create a `docker-compose.yml` file in the root directory.
3.  Configure the docker-compose file to define the three services.
4.  Map the following ports to the host:
    * Data Service: 8000
    * API Gateway: 3000
    * Frontend: 8080 (use a simple nginx image to serve the static files)
5.  Ensure the API Gateway can communicate with the Data Service using Docker's internal networking.

## Implementation
- Created `/data-service`, `/api-gateway`, `/frontend` as empty scaffolding directories.
- Added `docker-compose.yml` in the repo root defining three services (`data-service`, `api-gateway`, `frontend`) on a shared default Compose network, with host port mappings `8000:8000`, `3000:3000`, `8080:80` (frontend served via `nginx:alpine`).
- The Compose network gives each service a DNS hostname matching its service name, so the gateway later reaches the data service at `http://data-service:8000` instead of `localhost`.
- Added `start-dev.ps1` / `stop-dev.ps1` as a non-Docker alternative for local development (uvicorn + node + `python -m http.server`, logging to `logs/*.log`); frontend runs on `:8090` there since nginx isn't in that path.

## Validation
- `docker compose config` to confirm the compose file parses and all three services/ports/network settings resolve as expected.
- `docker compose up` followed by `docker compose ps` to confirm all three containers reach a running state before any service logic existed.
- Confirmed cross-container DNS resolution (`data-service` hostname reachable from inside the `api-gateway` container) once Module A had a live endpoint to call (validated together with Step 3).