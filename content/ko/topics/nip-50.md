---
title: "NIP-50: Search"
date: 2025-12-31
translationOf: /en/topics/nip-50.md
translationDate: 2025-12-31
draft: false
categories:
  - 프로토콜
  - 릴레이
---

NIP-50은 Nostr 릴레이를 위한 일반화된 검색 기능을 정의하며, 클라이언트가 태그나 ID에 의한 구조화된 쿼리를 넘어 전문 검색을 수행할 수 있게 합니다.

## 작동 방식

프로토콜은 REQ 메시지의 필터 객체에 `search` 필드를 추가합니다:

1. 클라이언트가 사람이 읽을 수 있는 검색 쿼리 제출 (예: "최고의 nostr 앱")
2. 릴레이가 이벤트 데이터(주로 `content` 필드)에 대해 쿼리를 해석하고 매칭
3. 결과는 시간순이 아닌 관련성으로 순위 지정
4. `limit` 필터는 관련성 정렬 후 적용

검색 필터는 `kinds` 및 `ids`와 같은 다른 제약 조건과 결합하여 더 구체적인 쿼리를 수행할 수 있습니다.

## 검색 확장

릴레이는 선택적으로 다음 확장 매개변수를 지원할 수 있습니다:

- `include:spam` - 기본 스팸 필터링 비활성화
- `domain:<domain>` - 검증된 NIP-05 도메인으로 필터링
- `language:<code>` - ISO 언어 코드로 필터링
- `sentiment:<value>` - 부정/중립/긍정 감정으로 필터링
- `nsfw:<true/false>` - NSFW 콘텐츠 포함 또는 제외

## 클라이언트 고려 사항

- 클라이언트는 `supported_nips` 필드를 통해 릴레이 기능을 확인해야 함
- 클라이언트 측 결과 검증 권장
- 모든 릴레이가 검색을 구현하는 것은 아님; 선택적 기능으로 남아 있음

---

**주요 출처:**
- [NIP-50 사양](https://github.com/nostr-protocol/nips/blob/master/50.md)

**언급:**
- [뉴스레터 #3: 12월 요약](/ko/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**참고:**
- [NIP-11: 릴레이 정보](/ko/topics/nip-11/)
