# dolsoe_image

"돌쇠배포" 문서에서 사용할 이미지를 자동으로 회전하고 EXIF 정보를 제거하는 도구입니다. CLI와 간단한 GUI를 제공합니다.

## 요구 사항
Python 3.8 이상이 필요합니다. 의존 패키지는 `requirements.txt`에 정의되어 있습니다.

## 사용법

### CLI
```bash
python process_images.py [-o 출력폴더] 이미지1.jpg 이미지2.png ...
```

### GUI
```bash
python process_images_gui.py
```
이미지를 선택하고 출력 폴더를 지정한 뒤 **처리 시작** 버튼을 누르면 됩니다.

## 빌드 스크립트
윈도우와 macOS에서 실행 파일을 만들 수 있는 스크립트를 제공합니다.

### Windows
```cmd
build_win.bat
```

### macOS
```bash
./build_mac.sh
```

각 스크립트는 가상환경을 생성하여 의존성을 설치한 뒤 PyInstaller로 `dist/` 폴더에 실행 파일을 생성합니다.
