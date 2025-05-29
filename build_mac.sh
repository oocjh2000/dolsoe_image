#!/bin/bash
# macOS build script
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pyinstaller --onefile process_images_gui.py
pyinstaller --onefile process_images.py
echo "Build finished. Executables are in the dist folder."
