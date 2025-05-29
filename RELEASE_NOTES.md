# 🖼️ 돌쇠 이미지 처리기 v1.0.0

> 📸 이미지 EXIF 회전 정보 자동 처리 및 메타데이터 제거 도구의 첫 번째 정식 릴리즈입니다!

## 🎉 주요 특징

### ✨ 핵심 기능
- **📱 EXIF 회전 정보 자동 처리**: 스마트폰 사진의 회전 정보를 자동으로 적용
- **🧹 메타데이터 완전 제거**: 개인정보 보호를 위한 EXIF 데이터 완전 삭제  
- **🖥️ 이중 인터페이스**: GUI와 CLI 모두 지원으로 다양한 사용 환경에 대응
- **⚡ 일괄 처리**: 여러 이미지를 한 번에 안전하게 처리
- **📦 실행 파일 지원**: Python 설치 없이도 사용 가능한 독립 실행 파일 제공

### 🖼️ 지원 포맷
JPEG, PNG, BMP, GIF 포맷을 완벽 지원합니다.

## 🚀 빠른 시작

### 실행 파일 사용 (권장)
1. [Releases](../../releases) 페이지에서 운영체제에 맞는 실행 파일 다운로드
2. 다운로드한 파일을 실행
3. GUI에서 이미지 선택 후 처리 시작!

### 소스코드 실행
```bash
# 저장소 클론
git clone https://github.com/your-username/dolsoe_image.git
cd dolsoe_image

# 의존성 설치
pip install -r requirements.txt

# GUI 실행
python process_images_gui.py

# 또는 CLI 사용
python process_images.py *.jpg -o processed/
```

## 📥 다운로드

| 플랫폼 | 파일 | 크기 | SHA256 |
|--------|------|------|--------|
| 🪟 Windows | `dolsoe-image-v1.0.0-win.exe` | ~15MB | `계산예정` |
| 🍎 macOS | `dolsoe-image-v1.0.0-macos` | ~18MB | `계산예정` |
| 📦 Source | `Source code (zip)` | ~50KB | `계산예정` |

## 🎯 사용 사례

### 📱 스마트폰 사진 정리
세로로 찍었는데 가로로 보이는 사진들을 올바른 방향으로 자동 회전

### 🌐 안전한 웹 업로드  
위치정보, 촬영시간 등 개인정보가 담긴 EXIF 데이터를 완전 제거

### 📊 대량 이미지 정리
수백 장의 이미지를 일관된 방향으로 일괄 정리

## ⚠️ 알려진 제한사항

- 매우 큰 이미지 파일(100MB+)의 경우 처리 시간이 오래 걸릴 수 있습니다
- RAW 포맷(.CR2, .NEF 등)은 현재 지원하지 않습니다  
- GUI에서 대용량 배치 처리 시 진행률이 표시되지 않습니다

## 🔄 업그레이드 방법

첫 번째 릴리즈이므로 업그레이드 과정이 없습니다. 향후 버전에서는 자동 업데이트 안내를 제공할 예정입니다.

## 🛠️ 기술적 세부사항

- **언어**: Python 3.6+
- **주요 라이브러리**: Pillow (PIL), Tkinter
- **빌드 도구**: PyInstaller
- **지원 OS**: Windows 10+, macOS 10.14+, Ubuntu 18.04+

## 📝 전체 변경사항

이는 첫 번째 릴리즈로, 모든 기능이 새롭게 추가되었습니다. 자세한 내용은 [CHANGELOG.md](CHANGELOG.md)를 참조하세요.

## 🐛 버그 리포트 및 기능 요청

문제를 발견하거나 새로운 기능을 제안하고 싶으시면 [Issues](../../issues) 페이지를 이용해 주세요.

## 🤝 기여

이 프로젝트에 기여하고 싶으시면 [기여 가이드](README.md#-기여하기)를 확인해 주세요.

## 📄 라이선스

이 소프트웨어는 [MIT 라이선스](LICENSE) 하에 배포됩니다.

---

<div align="center">

**✨ 돌쇠 이미지 처리기를 사용해 주셔서 감사합니다! ✨**

Made with ❤️ by 돌쇠 | [GitHub](https://github.com/your-username/dolsoe_image)

</div> 