# 김치광장 쇼핑몰 - 모바일 최적화 가이드

## 📱 모바일 최적화 완료 사항

### 1. 반응형 디자인
- **태블릿 (900px 이하)**: 상품 2열 그리드, 갤러리 2열
- **모바일 (600px 이하)**: 완전한 모바일 레이아웃
- **작은 모바일 (400px 이하)**: 초소형 화면 최적화

### 2. 터치 최적화
- 모든 버튼과 링크는 최소 44px 터치 영역 확보
- 터치 피드백 (탭 하이라이트) 추가
- 호버 효과를 터치 디바이스에서 적절히 처리

### 3. 성능 최적화
- GPU 가속 활성화 (transform: translateZ(0))
- 이미지 렌더링 최적화
- 스크롤 성능 개선 (-webkit-overflow-scrolling)

### 4. 접근성
- 스크린 리더 지원
- 포커스 가시성 개선
- 키보드 네비게이션 지원

### 5. 모바일 UX 개선
- 노치(notch) 대응 (iPhone X 이상)
- 가로 모드 최적화
- 텍스트 크기 자동 조정

## 🧪 모바일 테스트 방법

### 1. 크롬 개발자 도구
```
1. F12 또는 Ctrl+Shift+I
2. 상단의 모바일 아이콘 클릭 (Toggle device toolbar)
3. 다양한 디바이스로 테스트:
   - iPhone SE (375px)
   - iPhone 12 Pro (390px)
   - Samsung Galaxy S20 (360px)
   - iPad (768px)
```

### 2. 실제 모바일 기기 테스트
```
1. 같은 Wi-Fi에 연결
2. 브라우저에서 컴퓨터 IP 주소로 접속
   예: http://192.168.0.10:포트번호/index.html
```

### 3. 온라인 도구
- [BrowserStack](https://www.browserstack.com/)
- [LambdaTest](https://www.lambdatest.com/)
- [Responsively App](https://responsively.app/) (무료)

## 📏 주요 브레이크포인트

```css
/* 태블릿 */
@media (max-width: 900px) { ... }

/* 모바일 */
@media (max-width: 600px) { ... }

/* 작은 모바일 */
@media (max-width: 400px) { ... }

/* 터치 디바이스 */
@media (hover: none) and (pointer: coarse) { ... }

/* 가로 모드 */
@media (max-height: 500px) and (orientation: landscape) { ... }
```

## ✅ 모바일 체크리스트

### 레이아웃
- [✓] 헤더가 모바일에서 세로로 정렬
- [✓] 검색창이 전체 너비 사용
- [✓] 카테고리 메뉴가 센터 정렬
- [✓] 상품 카드가 2열 → 1열로 변경

### 터치
- [✓] 모든 버튼이 쉽게 탭 가능
- [✓] 링크 간격이 충분함
- [✓] 탭 피드백이 명확함

### 성능
- [✓] 페이지 로딩 속도 빠름
- [✓] 스크롤이 부드러움
- [✓] 애니메이션이 버벅거리지 않음

### 콘텐츠
- [✓] 텍스트가 읽기 쉬움
- [✓] 이미지가 적절한 크기
- [✓] 버튼 텍스트가 명확함

## 🚀 추가 개선 권장사항

### 즉시 구현 가능
1. 실제 상품 이미지 추가
2. 로딩 스피너 구현
3. 무한 스크롤 또는 페이지네이션
4. 즐겨찾기/장바구니 기능

### 향후 고려사항
1. PWA (Progressive Web App) 변환
2. 오프라인 지원
3. 푸시 알림
4. 다크 모드 지원

## 📊 모바일 최적화 점수 목표

### Google Lighthouse 점수
- Performance: 90+ 
- Accessibility: 95+
- Best Practices: 90+
- SEO: 95+

### PageSpeed Insights
- Mobile: 85+
- Desktop: 90+

## 🔧 문제 해결

### 텍스트가 너무 작아요
→ `style.css`의 해당 미디어 쿼리에서 `font-size` 조정

### 터치 영역이 작아요
→ `padding`과 `min-height: 44px` 확인

### 스크롤이 버벅거려요
→ `will-change: transform` 추가

### 아이폰 노치가 가려요
→ `safe-area-inset` 패딩 확인

## 📞 지원

문제가 발생하면:
1. 개발자 도구 콘솔 확인
2. 브라우저 캐시 삭제
3. 다른 브라우저에서 테스트

---

**최종 업데이트**: 2026-06-12
**모바일 최적화 버전**: 1.0
