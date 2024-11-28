#!/bin/bash

# docker run docker script to shutdown and delete postgres container
docker compose rm pollogram-db-dev -s -f -v

echo "Postgres container shutdown complete."