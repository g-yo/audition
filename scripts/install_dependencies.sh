#!/bin/bash
apt-get update
apt-get install -y python3-pip
pip3 install -r /var/www/html/auditions/requirements.txt
