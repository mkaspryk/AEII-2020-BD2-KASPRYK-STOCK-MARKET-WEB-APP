# Tested on Windows 10

# requires set-executionpolicy unrestricted

# create virtualenv '.venv'
python -m venv .venv

# activate .venv
.\.venv\Scripts\activate

# install all required packages
pip install -r .\requirements.txt