#!/bin/bash

# Add the directory containing gunicorn to PATH
export PATH=$PATH:/usr/local/bin

# Navigate to the project directory
PROJECT_DIR="/home/ec2-user/auditions"
if [ -d "$PROJECT_DIR" ]; then
    cd "$PROJECT_DIR"
else
    echo "Directory $PROJECT_DIR does not exist."
    exit 1
fi

# Replace with your server start command, e.g., using Gunicorn
gunicorn --workers 3 auditions.wsgi:application --bind 0.0.0.0:8000 --daemon
