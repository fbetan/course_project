#!/bin/bash

echo "Using Virtual Environment"
source projectenv/bin/activate
cd project

echo "Migrating DB"

python3 manage.py makemigrations politicians
python3 manage.py migrate

echo "Running Test Suite"

python3 manage.py test

echo "Starting Server"
python3 manage.py runserver
