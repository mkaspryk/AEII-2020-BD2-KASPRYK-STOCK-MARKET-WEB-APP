#!/bin/bash

# tested on Ubuntu 18.04 

if [[ $EUID != 0 ]]; then
	sudo "$0" "$@"
	exit $?
fi

# install pip and venv
apt update
apt install --upgrade python3-pip python3-venv
apt install libmysqlclient-dev

# create virtualenv '.venv'
python3 -m venv .venv

# activate .venv
source .venv/bin/activate

# install all required packages
pip install -r ./requirements.txt
