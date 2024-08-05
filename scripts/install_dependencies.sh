#!/bin/bash
sudo yum update -y
sudo yum install -y git
sudo yum groupinstall -y "Development Tools"
sudo yum install -y openssl-devel bzip2-devel libffi-devel
cd /usr/src
sudo wget https://www.python.org/ftp/python/3.12.0/Python-3.12.0.tgz
sudo tar xzf Python-3.12.0.tgz
cd Python-3.12.0
sudo ./configure --enable-optimizations
sudo make altinstall
sudo ln -s /usr/local/bin/python3.12 /usr/bin/python3.12
sudo ln -s /usr/local/bin/pip3.12 /usr/bin/pip3.12
cd /var/www/html/auditions
pip3.12 install -r requirements.txt
