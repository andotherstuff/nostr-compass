---
title: "NIP-24: 추가 메타데이터 필드"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Identity
---

NIP-24는 기본 name, about, picture 외에 kind 0 사용자 메타데이터에 대한 추가 선택적 필드를 정의합니다.

## 추가 메타데이터 필드

- **display_name**: `name`보다 더 풍부한 문자를 가진 대체 큰 이름
- **website**: 이벤트 작성자와 관련된 웹 URL
- **banner**: 선택적 배경 표시를 위한 넓은(~1024x768) 사진 URL
- **bot**: 콘텐츠가 전체 또는 부분적으로 자동화되었음을 나타내는 불리언
- **birthday**: 선택적 year, month, day 필드가 있는 객체

## 표준 태그

NIP-24는 또한 범용 태그를 표준화합니다:
- `r`: 웹 URL 참조
- `i`: 외부 식별자
- `title`: 다양한 이벤트 유형의 이름
- `t`: 해시태그(소문자여야 함)

---

**주요 출처:**
- [NIP-24 사양](https://github.com/nostr-protocol/nips/blob/master/24.md)

**언급된 곳:**
- [뉴스레터 #1: NIP 업데이트](/ko/newsletters/2025-12-17-newsletter/#nip-updates)

**참고:**
- [NIP-01: 기본 프로토콜](/ko/topics/nip-01/)

