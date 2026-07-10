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