#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
#pip install -r requirements.txt
pip install django
pip install dj-database-url
pip install gunicorn
pip install psycopg2
pip install whitenoise
# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate