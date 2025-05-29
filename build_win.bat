@echo off
REM Windows build script
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
pyinstaller --onefile process_images_gui.py
pyinstaller --onefile process_images.py
echo Build finished. Executables are in the dist folder.
