#!/bin/bash

# docker run docker script to shutdown and delete postgres container
docker compose rm pollogram-db-dev -s -f -v

# sleep for a bit while docker thinks
sleep 5

# run docker script to create and initiate postgres container
docker compose up pollogram-db-dev -d

echo "Postgres container restart complete."