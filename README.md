# dolsoe_image

A small utility that corrects image orientation and removes metadata for "돌쇠배포" docx manuscripts.

## Usage

```
python process_images.py [-o OUTPUT_DIR] image1.jpg image2.png ...
```

The processed images are saved to `processed/` by default or to the directory provided with `-o`.

## Building an executable

This project can be bundled into a standalone executable using [PyInstaller](https://pyinstaller.org/).
Make sure Pillow is installed and run:

```
pyinstaller --onefile process_images.py
```

The resulting binary will appear in the `dist` folder.

