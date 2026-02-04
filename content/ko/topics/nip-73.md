---
title: "NIP-73 (지오태그)"
date: 2026-02-04
description: "NIP-73은 지리적 좌표와 식별자를 사용하여 Nostr event에 위치 태깅을 정의합니다."
---

NIP-73은 Nostr event에 지리적 위치 데이터를 첨부하는 방법을 명시합니다. 이를 통해 위치 기반 콘텐츠 발견 및 필터링이 가능합니다.

## 작동 방식

위치 데이터는 `g` (geohash) 태그를 통해 event에 추가됩니다. geohash 인코딩은 위도와 경도를 단일 문자열로 표현하며, 문자열 길이에 따라 정밀도가 결정됩니다. 문자열이 길수록 더 정확한 위치를 나타냅니다.

Event는 다양한 정밀도 수준의 여러 geohash 태그를 포함할 수 있어, 클라이언트가 다양한 세분화 수준에서 쿼리할 수 있습니다. 6자 geohash로 태그된 게시물은 대략 도시 블록 하나를 커버하고, 4자 geohash는 작은 도시를 커버합니다.

## 태그 형식

```json
{
  "tags": [
    ["g", "u4pruydqqvj", "geohash"],
    ["g", "u4pruyd", "geohash"],
    ["g", "u4pru", "geohash"]
  ]
}
```

## 국가 코드

NIP-73에 대한 최근 업데이트([PR #2205](https://github.com/nostr-protocol/nips/pull/2205))는 ISO 3166 국가 코드 지원을 추가하여, 정확한 좌표 없이도 국가 수준의 위치로 event를 태그할 수 있습니다:

```json
{
  "tags": [
    ["g", "US", "countryCode"]
  ]
}
```

## 구현

- 위치 인식 클라이언트가 체크인 및 로컬 발견을 위해 NIP-73 사용
- Relay 필터가 지역별로 콘텐츠를 제한하거나 우선순위 지정 가능
- 지도 애플리케이션이 지오태그된 노트를 표시

## 주요 출처

- [NIP-73 명세](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - ISO 3166 국가 코드 추가

## 관련 뉴스레터

- [Newsletter #8 (2026-02-04)](/ko/newsletters/2026-02-04-newsletter/) - 국가 코드 지원 병합
