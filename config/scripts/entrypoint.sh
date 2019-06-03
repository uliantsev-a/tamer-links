#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
gunicorn --reload TamerLinks.wsgi:application -b 0.0.0.0:9000 -k gevent -w $(cat /proc/cpuinfo | grep 'core id' | wc -l)