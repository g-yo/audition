#!/bin/bash
set -e

# Navigate to the project directory
PROJECT_DIR="/home/ec2-user/auditions"
if [ -d "$PROJECT_DIR" ]; then
    cd "$PROJECT_DIR"
else
    echo "Directory $PROJECT_DIR does not exist."
    exit 1
fi

# Activate virtual environment if you have one
# source venv/bin/activate

# Run Django migrations
python3.12 manage.py migrate
