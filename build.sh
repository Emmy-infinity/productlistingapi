#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Convert static files for your React assets / Admin panel
python manage.py collectstatic --no-input

# Apply database migrations to PostgreSQL
python manage.py migrate
