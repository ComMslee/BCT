@echo off

rem Check if the release folder exists
if not exist release mkdir release

rem Change the current directory to the release folder
cd .\release

rem Run PyInstaller
..\venv\Scripts\pyinstaller.exe -F ..\src\main.py

rem Change the current directory back to the parent directory
cd ..

copy release\dist\main.exe release\push.exe /Y

pause