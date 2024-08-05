#!/bin/bash
set -e

# Update system packages
sudo yum update -y

# Install necessary packages
sudo yum install -y git
sudo yum groupinstall -y "Development Tools"
sudo yum install -y openssl-devel bzip2-devel libffi-devel

# Install Python 3.12
cd /usr/src
sudo wget https://www.python.org/ftp/python/3.12.0/Python-3.12.0.tgz
sudo tar xzf Python-3.12.0.tgz
cd Python-3.12.0
sudo ./configure --enable-optimizations
sudo make altinstall

# Create symlinks for convenience, if they don't already exist
if [ ! -L /usr/bin/python3.12 ]; then
    sudo ln -s /usr/local/bin/python3.12 /usr/bin/python3.12
fi

if [ ! -L /usr/bin/pip3.12 ]; then
    sudo ln -s /usr/local/bin/pip3.12 /usr/bin/pip3.12
fi

# Navigate to the project directory
PROJECT_DIR="/auditions"
if [ -d "$PROJECT_DIR" ]; then
    cd "$PROJECT_DIR"
else
    echo "Directory $PROJECT_DIR does not exist."
    exit 1
fi

# Install Python dependencies
if [ -f "requirements.txt" ]; then
    pip3.12 install -r requirements.txt
else
    echo "requirements.txt file not found."
    exit 1
fi
