---
title: "NIP-58: Badges"
date: 2026-01-28
translationOf: /en/topics/nip-58.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Identity
  - Reputation
---
NIP-58은 Nostr용 배지 시스템을 정의한다. 하나의 이벤트가 배지를 정의하고, 다른 이벤트가 배지를 수여하며, 세 번째 이벤트가 수신자에게 프로필에 표시할지 선택할 수 있게 한다.

## 작동 방식

### 배지 정의 (Kind 30009)

발행자가 주소 지정 가능 이벤트로 배지 정의를 생성한다:

```json
{
  "kind": 30009,
  "tags": [
    ["d", "early-adopter"],
    ["name", "Early Adopter"],
    ["description", "Joined before 2024"],
    ["image", "https://example.com/badge.png"],
    ["thumb", "https://example.com/badge-thumb.png"]
  ]
}
```

### 배지 수여 (Kind 8)

발행자가 한 명 이상의 사용자에게 배지를 수여한다:

```json
{
  "kind": 8,
  "tags": [
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["p", "recipient-pubkey"]
  ]
}
```

### 배지 표시 (Kind 30008)

사용자가 프로필에 표시할 배지를 선택한다:

```json
{
  "kind": 30008,
  "tags": [
    ["d", "profile_badges"],
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["e", "award-event-id"]
  ]
}
```

프로필 배지 이벤트에서 클라이언트는 `a`와 `e` 태그를 순서쌍으로 읽어야 한다. 대응하는 수여 이벤트가 없는 `a` 태그나, 대응하는 배지 정의가 없는 `e` 태그는 무시해야 한다.

## 활용 사례

- **커뮤니티 멤버십**: 그룹이나 커뮤니티 소속 표시
- **업적**: 기여 또는 마일스톤 인정
- **증명**: 제3자가 역할이나 지위를 보증
- **접근 제어**: 발행자 기반 배지를 이용한 기능 또는 공간 게이팅

## 신뢰 모델

배지의 가치는 전적으로 발행자의 평판에 달려 있다. 누구나 배지를 만들 수 있으므로 클라이언트는 다음을 해야 한다:

- 발행자 정보를 눈에 띄게 표시
- 신뢰하는 발행자 기준 필터링 허용
- 맥락 없이 배지를 권위적으로 취급하지 않음

배지 수여는 불변이며 양도 불가능하다. 이는 배지가 증명과 인정에는 적합하지만, 토큰화된 의미의 이식 가능한 자격증명으로는 적합하지 않음을 의미한다.

## 구현 참고사항

배지 정의는 주소 지정 가능 이벤트이므로 발행자가 배지 식별자를 변경하지 않고도 아트워크나 설명을 업데이트할 수 있다. 수여 이벤트는 특정 시점에 수신자를 해당 정의에 연결하는 영구 기록이다.

클라이언트도 표시 방식에 재량이 있다. 명세는 사용자가 나열한 것보다 적은 배지를 표시하거나 가용 공간에 맞는 썸네일 크기를 선택하는 것을 명시적으로 허용한다.

---

**주요 출처:**
- [NIP-58 명세](https://github.com/nostr-protocol/nips/blob/master/58.md)

**언급된 뉴스레터:**
- [Newsletter #7: Five Years of Nostr Januarys](/en/newsletters/2026-01-28-newsletter/)
- [Newsletter #15: Five Years of Nostr Februaries](/en/newsletters/2026-03-04-newsletter/)

**같이 보기:**
- [NIP-51: Lists](/ko/topics/nip-51/)
- [Web of Trust](/ko/topics/web-of-trust/)
