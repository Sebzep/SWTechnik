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