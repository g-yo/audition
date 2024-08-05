#!/bin/bash
cd /var/www/html/auditions
# Replace with your server start command, e.g., using Gunicorn
gunicorn --workers 3 auditions.wsgi:application --bind 0.0.0.0:8000 --daemon
