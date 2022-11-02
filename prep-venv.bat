echo off
REM ========================================================================================
REM Sets a new Virtual Environment for the Project.
REM This will clean the folder from any old virtual environment and create a new one.
REM ========================================================================================

cls

REM check if environment exists and make sure it is not active.
if exist venv\ (
  echo Exiting virtual environment...
  call .\venv\Scripts\deactivate
) else (
  echo No virtual environment found...
)

echo Removing old venv...
rmdir /S /Q venv
rmdir /S /Q __pycache_

REM Some checks first
echo Python path:
where python

REM Make sure you have pip (if needed)
python -m ensurepip
python -m pip install --upgrade pip --user

REM Creates a main.py file...
if exist main.py (
    REM main.py exists do nothing
) else (
    echo Creating a new main.py
    echo print("Hello World!") > main.py	
)

REM Create Virtual Environment
echo Creating virtual environment...
python -m venv .\venv

REM Activate Virtual Environment

echo Activating virtual environment...
call .\venv\Scripts\activate 

REM Upgrade package installer (if needed)
python -m pip install --upgrade pip


REM Install all required packages...
if exist requirements.txt (
	echo Installing required packages...
    pip install -r requirements.txt
) else (
	echo requirements.txt does not exist do nothing	
)

REM Check again where python is now
where python

echo done!
