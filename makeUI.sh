#!/bin/bash

# Run PySide6-uic to compile the UI file
./venv_mac/bin/pyside6-uic ./src/BCT_UI.ui -o ./src/MainUI.py

# Change the current directory back to the parent directory
cd ..

echo "Conversion completed."
