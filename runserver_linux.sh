#!/bin/bash

# activate virtual environment
source .venv/bin/activate

# run server
#x-terminal-emulator -e "python3 ./stock/manage.py runserver" 
python3 ./stock/manage.py makemigrations portfolio funds currencies
python3 ./stock/manage.py migrate --database=local
python3 ./stock/manage.py migrate --database=remote
python3 ./stock/manage.py fetcher_command
python3 ./stock/manage.py runserver

# wait for the server to start
#sleep 3s

# open browser with a home page
#xdg-open http://localhost:8000
