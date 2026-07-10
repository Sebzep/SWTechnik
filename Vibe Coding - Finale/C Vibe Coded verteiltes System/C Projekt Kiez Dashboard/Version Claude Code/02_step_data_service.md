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