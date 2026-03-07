---
title: "NIP-73: 외부 콘텐츠 ID"
date: 2026-02-04
translationOf: /en/topics/nip-73.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Discovery
  - Metadata
---
NIP-73은 Nostr 이벤트 내에서 외부 콘텐츠를 참조하는 표준 방법을 정의한다. 식별자 자체에는 `i` 태그를, 식별자 유형에는 `k` 태그를 사용하여 클라이언트가 같은 책, 웹사이트, 팟캐스트 에피소드, 위치, 해시태그 또는 블록체인 객체에 대한 논의를 그룹화할 수 있다.

## 작동 방식

NIP-73을 사용하는 이벤트는 정규화된 외부 식별자를 포함하는 `i` 태그와 식별자의 종류를 설명하는 `k` 태그를 포함한다. 클라이언트는 같은 주제를 참조하는 모든 이벤트를 조회할 수 있다.

```json
{
  "tags": [
    ["i", "isbn:9780765382030"],
    ["k", "isbn"]
  ]
}
```

명세는 다음을 포함한 여러 식별자 계열을 다룬다:

- fragment가 없는 정규화된 웹 URL
- 도서용 ISBN
- 영화용 ISAN
- geohash 및 ISO 3166 국가 또는 행정구역 코드
- 팟캐스트 피드, 에피소드 및 퍼블리셔 GUID
- 해시태그
- 블록체인 트랜잭션 및 주소 식별자

## 정규화 규칙

NIP-73에서 독자에게 가장 중요한 세부사항은 정규화다. 같은 주제가 하나의 정규 문자열에 매핑되어야 하며, 그렇지 않으면 클라이언트가 같은 의미의 여러 식별자로 논의를 분산시킨다.

명세의 예시:

- geohash는 `geo:<value>`를 사용하며 소문자여야 한다
- 국가 및 행정구역 코드는 `iso3166:<code>`를 사용하며 대문자여야 한다
- ISBN은 하이픈을 생략한다
- 웹 URL은 fragment를 제거한다
- 블록체인 트랜잭션 해시는 소문자 hex를 사용한다

사소해 보이지만, 하나의 공유된 대화와 호환되지 않는 여러 인덱스의 차이를 만든다.

## 유용한 패턴

NIP-73은 콘텐츠 형식이 아닌 일반적인 참조 계층이다. 장문 노트가 도서 ISBN을 가리킬 수 있고, 리뷰가 영화 ISAN을 가리킬 수 있으며, 로컬 게시물이 매번 커스텀 태그를 만들지 않고도 geohash나 국가 코드를 가리킬 수 있다.

명세는 또한 `i` 태그의 두 번째 값으로 선택적 URL 힌트를 허용한다. 이를 통해 클라이언트가 식별자 유형에 대한 커스텀 렌더러가 없을 때 대체 링크를 제공한다.

## 왜 중요한가

Nostr는 이미 이벤트와 프로필에 대한 강력한 내부 참조를 가지고 있다. NIP-73은 이 개념을 Nostr 외부의 것들로 확장한다. 식별자가 정규화되면 댓글, 평점, 하이라이트 및 신뢰 어설션이 모두 다른 클라이언트에서 같은 외부 주제에 연결될 수 있다.

이것이 [NIP-85](/ko/topics/nip-85/)가 NIP-73 위에 구축되는 이유이기도 하다. Trusted Assertions는 사용자와 이벤트뿐만 아니라 책, 웹사이트, 해시태그, 위치 같은 NIP-73 식별자도 평가할 수 있다.

---

**주요 출처:**
- [NIP-73 명세](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - ISO 3166 국가 및 행정구역 코드 추가

**언급된 뉴스레터:**
- [Newsletter #8: NIP 업데이트](/en/newsletters/2026-02-04-newsletter/#nip-updates)
- [Newsletter #10: NIP-85 심층 분석](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)

**같이 보기:**
- [NIP-85: Trusted Assertions](/ko/topics/nip-85/)
