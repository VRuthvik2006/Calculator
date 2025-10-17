@echo off
echo Building Advanced Calculator GUI Executable...
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

REM Build the GUI executable with clean build
echo.
echo Building GUI executable with PyInstaller...
pyinstaller --onefile --windowed --name "AdvancedCalculatorGUI" ..\src\calculator_gui.py --clean

if errorlevel 1 (
    echo Error: Failed to build GUI executable
    pause
    exit /b 1
)

echo.
echo Build completed successfully!
echo The GUI executable is located in the 'dist' folder: dist\AdvancedCalculatorGUI.exe
echo.
echo Note: The --windowed flag ensures no console window appears when running the GUI.
echo.
pause