#!/bin/bash

# activate virtual environment
source .venv/bin/activate

# run server
x-terminal-emulator -e "python3 ./stock/manage.py runserver" 

# wait for the server to start
sleep 3s

# open browser with a home page
xdg-open http://localhost:8000
