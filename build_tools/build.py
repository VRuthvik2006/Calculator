#!/usr/bin/env python3
"""
Build script for Advanced Calculator
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error: {description} failed")
        print(f"Command: {command}")
        print(f"Error output: {e.stderr}")
        return False

def main():
    print("Advanced Calculator Build Script")
    print("=" * 40)
    
    # Check if Python is available
    try:
        result = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
        print(f"Using Python: {result.stdout.strip()}")
    except Exception as e:
        print(f"Error checking Python version: {e}")
        return False
    
    # Install dependencies
    if not run_command(f"{sys.executable} -m pip install -r requirements.txt", "Installing dependencies"):
        return False
    
    # Build GUI executable
    build_command = f"{sys.executable} -m PyInstaller --onefile --windowed --name AdvancedCalculatorGUI calculator_gui.py --clean"
    if not run_command(build_command, "Building GUI executable"):
        return False
    
    # Check if executable was created
    if os.name == 'nt':  # Windows
        exe_path = "dist\\AdvancedCalculatorGUI.exe"
    else:  # Unix-like systems
        exe_path = "dist/AdvancedCalculatorGUI"
    
    if os.path.exists(exe_path):
        print(f"\n🎉 Build completed successfully!")
        print(f"📁 Executable location: {exe_path}")
        print(f"📏 File size: {os.path.getsize(exe_path) / (1024*1024):.1f} MB")
    else:
        print(f"\n❌ Build failed - executable not found at {exe_path}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)
    print("\nPress Enter to exit...")
    input()