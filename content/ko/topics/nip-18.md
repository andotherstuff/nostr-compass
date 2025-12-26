---
title: "NIP-18: 리포스트"
date: 2025-12-17
draft: false
categories:
  - Social
  - Protocol
---

NIP-18은 다른 플랫폼의 리트윗과 유사하게 이벤트를 리포스트하는 방법을 정의합니다.

## 구조

리포스트는 다음을 포함하는 kind 6 이벤트(kind 1 노트용) 또는 kind 16(일반 리포스트)입니다:
- 리포스트된 이벤트를 참조하는 `e` 태그
- 원 작성자를 참조하는 `p` 태그
- 선택적으로 `content` 필드에 전체 원본 이벤트

## 최근 변경 사항

`a` 태그 지원으로 교체 가능 이벤트의 리포스트 지원이 개선되었습니다. 이를 통해 주소 지정 가능 이벤트(kind 30000-39999)를 특정 이벤트 ID가 아닌 주소로 참조할 수 있습니다.

---

**주요 출처:**
- [NIP-18 사양](https://github.com/nostr-protocol/nips/blob/master/18.md)

**언급된 곳:**
- [뉴스레터 #1: NIP 업데이트](/ko/newsletters/2025-12-17-newsletter/#nip-updates)

**참고:**
- [NIP-01: 기본 프로토콜](/ko/topics/nip-01/)

