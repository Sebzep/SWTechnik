# System Architecture: Distributed Dashboard

## 1. Overview
We are building a distributed web application consisting of three distinct modules (Microservices) that run independently and communicate via HTTP/REST.

## 2. Modules
* **Module A (Data Fetcher Service):** A Python (FastAPI) backend service. Its sole responsibility is to fetch external data (e.g., Weather, Places) and normalize the JSON responses.
* **Module B (API Gateway / BFF):** A Node.js (Express) server. It acts as a "Backend for Frontend". It receives requests from the frontend, routes them to Module A, and handles basic rate limiting or caching.
* **Module C (Frontend UI):** A static HTML/CSS/JS frontend using TailwindCSS. It strictly communicates only with Module B, never directly with Module A or external APIs.

## 3. Infrastructure
* All modules must be containerized.
* We use a `docker-compose.yml` file in the root directory to orchestrate the distributed system.