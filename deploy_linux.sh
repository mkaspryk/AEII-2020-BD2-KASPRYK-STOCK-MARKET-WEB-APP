#!/bin/bash

# tested on Ubuntu 18.04 

# create virtualenv '.venv'
python3 -m venv .venv &&

# activate .venv
source .venv/bin/activate &&

# install all required packages
pip install -r ./requirements.txt &&

# run server
x-terminal-emulator -e "python3 ./stock/manage.py runserver" 

# wait for the server to start
sleep 3s

# start browser with a home page
xdg-open http://localhost:8000
