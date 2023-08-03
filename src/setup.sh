#!/bin/bash 

echo  "Building the Docker images using Dockerfile and docker-compose"
docker compose build

echo "Creating Docker containers using docker-compose up"
docker compose up -d

