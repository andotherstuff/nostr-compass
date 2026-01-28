---
title: "NIP-58: 배지"
date: 2026-01-28
translationOf: /en/topics/nip-58.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Identity
  - Reputation
---

NIP-58은 Nostr를 위한 배지 시스템을 정의하여, 발급자가 배지를 생성하고 사용자에게 수여하면 사용자가 프로필에 표시할 수 있게 합니다.

## 작동 방식

### 배지 정의 (Kind 30009)

발급자가 주소 지정 가능 event로 배지 정의를 생성합니다:

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

발급자가 사용자에게 배지를 수여합니다:

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

사용자가 프로필에 표시할 배지를 선택합니다:

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

## 사용 사례

- **커뮤니티 멤버십**: 그룹이나 커뮤니티 소속 증명
- **업적**: 기여나 이정표 인정
- **인증**: 제3자 증명 (직원, 크리에이터 등)
- **접근 제어**: 배지 소유 기반 콘텐츠나 기능 제한

## 신뢰 모델

배지 가치는 전적으로 발급자의 평판에 달려 있습니다. 누구나 배지를 만들 수 있으므로, 클라이언트는:
- 발급자 정보를 눈에 띄게 표시해야 합니다
- 사용자가 신뢰하는 발급자로 필터링할 수 있게 해야 합니다
- 맥락 없이 배지를 권위 있는 것으로 취급하지 않아야 합니다

## 관련 항목

- [NIP-51](/ko/topics/nip-51/) - 목록
- [Web of Trust](/ko/topics/web-of-trust/)
