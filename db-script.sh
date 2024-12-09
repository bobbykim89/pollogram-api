#!/bin/bash

echo "Please select action:"
echo "1) start db container"
echo "2) shut down db container"
echo "3) restart db container"

read script_select

case $script_select in
  1)
    # run docker script to create and initiate postgres container
    docker compose up pollogram-db-dev -d

    echo "Postgres container start complete."
    ;;
  2)
    # docker run docker script to shutdown and delete postgres container
    docker compose rm pollogram-db-dev -s -f -v

    echo "Postgres container shutdown complete."
    ;;
  3)
    # docker run docker script to shutdown and delete postgres container
    docker compose rm pollogram-db-dev -s -f -v

    # sleep for a bit while docker thinks
    sleep 5

    # run docker script to create and initiate postgres container
    docker compose up pollogram-db-dev -d

    echo "Postgres container restart complete."
    ;;
  *)
    echo "Invalid input. Please enter 1, 2, or 3."
    ;;
esac