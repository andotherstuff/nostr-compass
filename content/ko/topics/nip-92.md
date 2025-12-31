---
title: "NIP-92: Media Attachments"
date: 2025-12-31
translationOf: /en/topics/nip-92.md
translationDate: 2025-12-31
draft: false
categories:
  - 미디어
  - 프로토콜
---

NIP-92는 리소스를 설명하는 인라인 메타데이터 태그와 함께 URL을 포함하여 사용자가 Nostr 이벤트에 미디어 파일을 첨부할 수 있게 합니다.

## 작동 방식

1. 사용자가 이벤트 콘텐츠에 직접 미디어 URL을 배치 (예: kind 1 텍스트 노트)
2. 해당하는 `imeta` (인라인 메타데이터) 태그가 각 URL에 대한 세부 정보를 제공
3. 클라이언트는 메타데이터를 기반으로 imeta URL을 리치 프리뷰로 대체 가능
4. 메타데이터는 일반적으로 작성 중 파일이 업로드될 때 자동 생성됨

## imeta 태그

각 `imeta` 태그는 `url`과 최소 하나의 다른 필드를 가져야 합니다. 지원되는 필드는 다음과 같습니다:

- `url` - 미디어 URL (필수)
- `m` - 파일의 MIME 타입
- `dim` - 이미지 크기 (너비 x 높이)
- `blurhash` - 프리뷰 생성을 위한 blurhash
- `alt` - 접근성을 위한 대체 텍스트
- `x` - SHA-256 해시 (NIP-94에서)
- `fallback` - 기본 URL 실패 시 대체 URL

## 예제

```json
["imeta",
  "url https://example.com/image.jpg",
  "m image/jpeg",
  "dim 1920x1080",
  "blurhash LKO2?U%2Tw=w]~RBVZRi}^Xu%LRj"
]
```

---

**주요 출처:**
- [NIP-92 사양](https://github.com/nostr-protocol/nips/blob/master/92.md)

**관련 언급:**
- [뉴스레터 #3: 12월 요약](/ko/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**참고:**
- [NIP-94: 파일 메타데이터](/ko/topics/nip-94/)
