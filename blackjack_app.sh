#!/bin/bash

command_exists() {
  command -v "$1" >/dev/null 2>&1
}

# Check if either python or python3 is installed
if command_exists python; then
  PYTHON="python"
elif command_exists python3; then
  PYTHON="python3"
else
  echo "Error: Python or Python3 is not installed."
  echo "Please go to https://www.python.org/downloads/ to install the latest Python version."
  exit 1
fi

# Check if pip is installed
if ! command_exists pip; then
  echo "Error: pip is not installed."
  echo "Please make sure pip is installed alongside Python."
  exit 1
fi

# Create a virtual environment
$PYTHON -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

echo 'Hope you Enjoy!'
python main.py

# Deactivate the virtual environment
deactivate