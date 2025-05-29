# 🖼️ 돌쇠 이미지 처리기

> 📸 이미지 EXIF 회전 정보 자동 처리 및 메타데이터 제거 도구

![Python](https://img.shields.io/badge/Python-3.6+-blue?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=flat-square)

## ✨ 주요 기능

- 📱 **EXIF 회전 정보 자동 처리**: 스마트폰으로 촬영한 사진의 회전 정보를 자동으로 적용
- 🧹 **메타데이터 제거**: 개인정보가 포함될 수 있는 EXIF 메타데이터 완전 제거
- 🖥️ **다양한 인터페이스**: 명령어 도구와 직관적인 GUI 모두 지원
- ⚡ **일괄 처리**: 여러 이미지를 한 번에 처리
- 📦 **실행 파일 제공**: 별도 설치 없이 바로 사용 가능한 실행 파일
- 📊 **진행률 표시**: 이미지 처리 현황을 실시간으로 확인

## 🚀 빠른 시작

### GUI 버전 사용하기

```bash
python process_images_gui.py
```

1. **이미지 선택** 버튼을 클릭하여 처리할 이미지들을 선택
2. **출력 폴더 선택** 버튼을 클릭하여 결과를 저장할 폴더 지정 (선택사항)
3. **처리 시작** 버튼을 클릭하여 이미지 처리 실행
4. 하단 진행률 바를 통해 처리 현황을 확인

### 명령어 버전 사용하기

```bash
# 단일 이미지 처리
python process_images.py image1.jpg

# 여러 이미지 처리
python process_images.py image1.jpg image2.png image3.jpeg

# 출력 폴더 지정
python process_images.py *.jpg -o output_folder
```
명령어 실행 시 콘솔에 진행률이 표시됩니다.

## 📦 설치 및 설정

### 사전 요구사항

- Python 3.6 이상
- pip (Python 패키지 관리자)

### 설치 방법

1. **저장소 클론**
   ```bash
   git clone <repository-url>
   cd dolsoe_image
   ```

2. **가상환경 생성 (권장)**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **의존성 설치**
   ```bash
   pip install -r requirements.txt
   ```

### 실행 파일 빌드

프로그램을 실행 파일로 만들어 다른 컴퓨터에서도 사용할 수 있습니다.

**Windows:**
```bash
build_win.bat
```

**macOS:**
```bash
chmod +x build_mac.sh
./build_mac.sh
```

빌드가 완료되면 `dist/` 폴더에 실행 파일이 생성됩니다.

## 🎯 사용 사례

### 📱 스마트폰 사진 정리
스마트폰으로 촬영한 세로/가로 사진들이 컴퓨터에서 잘못 회전되어 보일 때

### 🌐 웹사이트 업로드
개인정보가 포함된 EXIF 데이터를 제거하여 안전하게 웹에 업로드

### 📊 이미지 데이터베이스 정리
대량의 이미지 파일들의 회전 정보를 일관성 있게 정리

## 🛠️ 기술 스택

- **[Pillow (PIL)](https://pillow.readthedocs.io/)**: 이미지 처리 및 EXIF 데이터 조작
- **[Tkinter](https://docs.python.org/3/library/tkinter.html)**: 크로스플랫폼 GUI 개발
- **[PyInstaller](https://pyinstaller.org/)**: 실행 파일 생성

## 📂 프로젝트 구조

```
dolsoe_image/
├── 📄 process_images.py      # 명령어 버전 메인 스크립트
├── 🖥️ process_images_gui.py  # GUI 버전 메인 스크립트
├── 📦 requirements.txt       # Python 의존성 목록
├── 🔧 build_win.bat         # Windows 빌드 스크립트
├── 🔧 build_mac.sh          # macOS 빌드 스크립트
├── 📁 dist/                 # 빌드된 실행 파일들
├── 📁 build/                # 빌드 임시 파일들
├── 📁 venv/                 # Python 가상환경
└── 📖 README.md             # 프로젝트 문서 (이 파일)
```

## ⚠️ 주의사항

- 처리된 이미지는 원본과 동일한 파일명으로 출력 폴더에 저장됩니다
- 원본 파일은 수정되지 않으므로 안전합니다
- EXIF 메타데이터가 완전히 제거되므로, 필요한 정보는 미리 백업하세요

## 🤝 기여하기

1. 이 저장소를 포크하세요
2. 새로운 기능 브랜치를 만드세요 (`git checkout -b feature/amazing-feature`)
3. 변경사항을 커밋하세요 (`git commit -m 'Add amazing feature'`)
4. 브랜치에 푸시하세요 (`git push origin feature/amazing-feature`)
5. Pull Request를 생성하세요

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 💬 문의 및 지원

문제가 발생하거나 개선 제안이 있으시면 [Issues](../../issues) 페이지에 등록해 주세요.

---

<div align="center">
  
**🌟 이 프로젝트가 도움이 되셨다면 별표를 눌러주세요! 🌟**

Made with ❤️ by 돌쇠

</div>
