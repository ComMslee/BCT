#!/bin/bash

# Check if the release folder exists
if [ ! -d "release" ]; then
    mkdir release
fi

# Change the current directory to the release folder
cd ./release

# Run PyInstaller
../venv_mac/bin/pyinstaller -w -F ../src/main.py

# Change the current directory back to the parent directory
cd ..

# Copy the main.exe to push.exe
cp release/dist/main.exe release/push.exe

echo "Conversion completed."
