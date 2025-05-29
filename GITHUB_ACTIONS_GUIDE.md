# 🚀 GitHub Actions 설정 및 사용 가이드

## 📋 목차
1. [초기 설정](#-초기-설정)
2. [워크플로우 실행](#-워크플로우-실행)
3. [빌드 모니터링](#-빌드-모니터링)
4. [릴리즈 관리](#-릴리즈-관리)
5. [문제 해결](#-문제-해결)

## 🔧 초기 설정

### 1. GitHub 저장소 생성
```bash
# 1. GitHub에서 새 저장소 생성
# 2. 로컬 프로젝트를 GitHub에 푸시
git init
git add .
git commit -m "🎉 Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/dolsoe_image.git
git branch -M main
git push -u origin main
```

### 2. Actions 권한 확인
- 저장소 설정 → **Actions** → **General**
- **Allow all actions and reusable workflows** 체크

### 3. 필수 파일 확인
```
📁 .github/
  └── 📁 workflows/
      └── 📄 build.yml ✅

📄 requirements.txt ✅
📄 process_images_gui.py ✅
```

## ▶️ 워크플로우 실행

### 🏷️ 자동 실행 (태그 기반)
```bash
# 릴리즈 태그 생성
git tag v1.0.0
git push origin v1.0.0

# 🎯 결과: 자동으로 3개 플랫폼 빌드 시작
```

### 🔧 수동 실행
1. GitHub 저장소 페이지 이동
2. **Actions** 탭 클릭
3. **🏗️ Build Multi-Platform Releases** 선택
4. **Run workflow** 버튼 클릭
5. 브랜치 선택 (보통 `main`)
6. **Run workflow** 확인

## 📊 빌드 모니터링

### 실시간 진행상황 확인
1. **Actions** 탭 → 실행 중인 워크플로우 클릭
2. 각 작업 상태 확인:
   - 🟡 대기 중 (Queued)
   - 🔵 실행 중 (In progress)
   - ✅ 성공 (Success)
   - ❌ 실패 (Failed)

### 빌드 로그 확인
```
Jobs:
├── 🪟 build (windows-latest) 
├── 🍎 build (macos-latest)
├── 🐧 build (ubuntu-latest)
└── 🚀 release (ubuntu-latest)
```

각 작업을 클릭하면 상세 로그를 볼 수 있습니다.

## 📦 릴리즈 관리

### 자동 생성되는 파일들
빌드 완료 후 **Releases** 섹션에 자동 생성:

```
📦 v1.0.0 릴리즈
├── 🪟 dolsoe-image-windows.exe
├── 🍎 dolsoe-image-macos
├── 🐧 dolsoe-image-linux
└── 📄 Source code (zip, tar.gz)
```

### 다운로드 링크 공유
```
https://github.com/YOUR_USERNAME/dolsoe_image/releases/latest
```

## 🔍 빌드 시간 예상

| 플랫폼 | 평균 빌드 시간 | 파일 크기 |
|--------|---------------|-----------|
| 🪟 Windows | 3-5분 | ~15MB |
| 🍎 macOS | 4-6분 | ~18MB |
| 🐧 Linux | 3-4분 | ~20MB |

## 🚨 문제 해결

### ❌ 자주 발생하는 에러들

#### 1. **의존성 설치 실패**
```yaml
# 해결: requirements.txt에 버전 명시
Pillow==10.0.0
pyinstaller==5.13.0
```

#### 2. **PyInstaller 빌드 실패**
```bash
# 로그에서 확인할 내용:
ModuleNotFoundError: No module named 'nicegui'
```
**해결책**: `requirements.txt`에 `nicegui`가 포함되어 있는지 확인

#### 3. **권한 문제**
```
Error: Resource not accessible by integration
```
**해결책**: 
1. 저장소 설정 → Actions → General
2. **Workflow permissions** → **Read and write permissions**

### 🔧 고급 설정

#### 캐시 최적화
```yaml
- name: 📦 Cache dependencies
  uses: actions/cache@v3
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
```

#### 병렬 실행 제한
```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

## 📈 사용 통계 확인

### Actions 사용량 모니터링
1. 설정 → **Billing and plans**
2. **Actions** 섹션에서 사용량 확인
3. 무료 계정: 월 2,000분 제한

### 최적화 팁
- 불필요한 의존성 제거
- 캐시 활용으로 빌드 시간 단축
- 조건부 실행으로 리소스 절약

## 🎯 다음 단계

### 추가 기능 구현
- [ ] 코드 품질 검사 (linting)
- [ ] 자동 테스트 실행
- [ ] 배포 자동화
- [ ] 슬랙/디스코드 알림

### 고급 워크플로우
```yaml
# 예: 코드 품질 검사 추가
- name: 🔍 Run linting
  run: |
    pip install flake8
    flake8 . --count --show-source --statistics
```

---

## 💡 유용한 링크

- [GitHub Actions 공식 문서](https://docs.github.com/en/actions)
- [PyInstaller 문서](https://pyinstaller.org/)
- [GitHub Marketplace (Actions)](https://github.com/marketplace?type=actions)

---

> **💡 팁**: 첫 번째 빌드는 시간이 오래 걸릴 수 있습니다. 이후 빌드는 캐시 덕분에 훨씬 빨라집니다! 