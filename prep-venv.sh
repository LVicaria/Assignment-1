#! /usr/bin/bash
# ========================================================================================
# Sets a new Virtual Environment for the Project.
# This will clean the folder from any old virtual environment and create a new one.
# ========================================================================================
# NOTE: It requires python3.10-venv package to be installed. Run "sudo apt install python3.10-venv"

clear

# Check if environment exists and make sure it is not active.
if [[ -d ./venv ]] then
  echo Exiting virtual environment...
  deactivate
else
  echo No virtual environment found...      
fi

echo Removing old venv...
rm -rf venv/
rm -rf __pycache__

# Some checks first
echo Python path:
whereis python

# Make sure you have pip (if needed)
python -m pip install --upgrade pip --user

# Creates a main.py file...
if [[ -f main.py ]] then
  echo main.py exists do nothing
else
  echo Creating a new main.py
  echo print\("Hello World!"\) > main.py      
fi

# Create Virtual Environment
echo Creating virtual environment...
python -m venv ./venv

# Activate Virtual Environment
echo Activating virtual environment...
source ./venv/bin/activate

# Run these manually after the environment is running.

# Upgrade package installer (if needed)
python -m pip install --upgrade pip

# Install all required packages...
if [[ -f requirements.txt ]] then
  echo Installing required packages...
  pip install -r requirements.txt
else
  echo requirements.txt does not exist do nothing	     
fi

# Check again where python is now
whereis python

echo done!
