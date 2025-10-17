@echo off
echo Building Advanced Calculator Executable...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Install required dependencies
echo Installing dependencies...
pip install -r ..\requirements.txt

if errorlevel 1 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

REM Build the executable
echo.
echo Building executable with PyInstaller...
pyinstaller --onefile --name "AdvancedCalculator" --distpath ..\dist ..\src\calculator.py

if errorlevel 1 (
    echo Error: Failed to build executable
    pause
    exit /b 1
)

echo.
echo Build completed successfully!
echo The executable is located in the main folder: ..\dist\AdvancedCalculator.exe
echo.
pause