#!/bin/bash

# run docker script to create and initiate postgres container
docker compose up pollogram-db-dev -d

echo "Postgres container start complete."