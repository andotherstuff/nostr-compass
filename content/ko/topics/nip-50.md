---
title: "NIP-50: 검색"
date: 2025-12-31
translationOf: /en/topics/nip-50.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Relay
---
NIP-50은 Nostr 릴레이를 위한 일반 검색 기능을 정의한다. NIP-01의 정확 매칭 필터 위에 전문 검색 스타일의 쿼리를 추가한다.

## 작동 방식

이 프로토콜은 `REQ` 메시지의 필터 객체에 `search` 필드를 추가한다:

1. 클라이언트가 `best nostr apps` 같은 사람이 읽을 수 있는 쿼리 문자열을 제출한다.
2. 릴레이가 해당 쿼리를 이벤트 데이터, 주로 `content` 필드에 대해 해석한다.
3. 결과는 `created_at`이 아닌 매칭 품질 순으로 정렬된다.
4. `limit`는 관련도 정렬 후에 적용된다.

검색 필터는 `kinds`, `ids`, authors 및 기타 일반 필터 필드와 결합하여 더 구체적인 쿼리를 만들 수 있다.

## 검색 확장

릴레이는 선택적으로 다음 확장 매개변수를 지원할 수 있다:

- `include:spam` - 기본 스팸 필터링 비활성화
- `domain:<domain>` - 검증된 NIP-05 도메인으로 필터링
- `language:<code>` - ISO 언어 코드로 필터링
- `sentiment:<value>` - 부정적, 중립적, 긍정적 감정으로 필터링
- `nsfw:<true/false>` - NSFW 콘텐츠 포함 또는 제외

릴레이는 지원하지 않는 확장을 무시해야 하므로, 클라이언트는 이를 보장이 아닌 힌트로 취급해야 한다.

## 상호운용성 참고사항

- 클라이언트는 `supported_nips` 필드를 통해 릴레이 기능을 확인해야 한다
- 클라이언트 측 결과 검증이 권장된다
- 모든 릴레이가 검색을 구현하지는 않으며, 선택적 기능으로 남아 있다

랭킹이 구현체에 따라 정의되므로, 동일한 쿼리가 다른 릴레이에서 다른 결과 세트를 반환할 수 있다. 재현율에 관심이 있는 클라이언트는 둘 이상의 검색 릴레이에 쿼리하고 결과를 병합해야 한다.

## 왜 중요한가

구조화된 필터는 원하는 작성자, kind, 또는 태그를 이미 알고 있을 때 잘 작동한다. 검색은 그 반대의 경우, 즉 발견을 위한 것이다. 따라서 NIP-50은 앱 디렉터리, 장기 아카이브, 공개 노트 검색에 유용하지만, 검색 품질은 각 릴레이의 인덱싱 및 스팸 필터링 선택에 크게 의존한다.

---

**주요 출처:**
- [NIP-50 사양](https://github.com/nostr-protocol/nips/blob/master/50.md)

**언급된 뉴스레터:**
- [Newsletter #3: 12월 회고](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #7: NIP 업데이트](/en/newsletters/2026-01-07-newsletter/)

**같이 보기:**
- [NIP-11: 릴레이 정보](/ko/topics/nip-11/)
