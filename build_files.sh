#!/bin/bash

echo "Install Project dependencies..."

python -m pip install -r requirements.txt

echo "Migrate DB..."

python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collect Static Files..."

python manage.py collectstatic --noinput