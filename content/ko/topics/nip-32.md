---
title: "NIP-32: 라벨링"
date: 2026-01-21
translationOf: /en/topics/nip-32.md
translationDate: 2026-01-28
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-32는 Nostr event, 사용자 및 기타 엔티티에 라벨을 첨부하기 위한 표준을 정의합니다. 라벨은 클라이언트가 분류, 콘텐츠 경고, 평판 시스템 및 중재에 사용할 수 있는 구조화된 메타데이터를 제공합니다.

## 작동 방식

라벨은 라벨 네임스페이스를 정의하는 `L` 태그와 해당 네임스페이스 내에서 특정 라벨을 적용하는 `l` 태그가 포함된 kind 1985 event를 사용합니다. 라벨이 적용되는 엔티티는 `e`(event), `p`(pubkey) 또는 `r`(relay URL) 같은 표준 태그를 통해 참조됩니다.

```json
{
  "kind": 1985,
  "tags": [
    ["L", "content-warning"],
    ["l", "nsfw", "content-warning"],
    ["e", "<event_id>"]
  ],
  "content": "Contains explicit imagery"
}
```

네임스페이스 시스템은 라벨 충돌을 방지합니다. "ugc-moderation" 네임스페이스의 "spam" 라벨은 "relay-report" 네임스페이스의 "spam"과 다른 의미를 갖습니다. 이를 통해 여러 라벨 시스템이 간섭 없이 공존할 수 있습니다.

## 사용 사례

콘텐츠 중재 시스템은 라벨을 사용하여 스팸, 불법 콘텐츠 또는 정책 위반을 표시합니다. 평판 시스템은 pubkey에 신뢰 점수 또는 인증 상태를 첨부합니다. 미디어 플랫폼은 콘텐츠 경고(NSFW, 폭력, 스포일러)를 적용합니다. Relay 운영자는 이의 제기 및 분쟁 해결을 위해 라벨을 사용합니다.

Trusted Relay Assertions 제안은 relay 이의 제기를 위해 NIP-32 라벨을 사용합니다. 운영자가 신뢰도 점수에 이의를 제기할 때, `L` = `relay-appeal`과 "spam", "censorship" 또는 "score" 같은 라벨 유형이 포함된 kind 1985 event를 게시합니다.

클라이언트 구현은 라벨을 소비하는 방식이 다양합니다. 일부 클라이언트는 팔로우한 사용자의 라벨을 추천으로 취급하고, 다른 클라이언트는 전문 라벨링 서비스를 쿼리합니다. 탈중앙화 설계는 사용자가 신뢰할 라벨러를 선택할 수 있게 합니다.

---

**주요 출처:**
- [NIP-32 명세](https://github.com/nostr-protocol/nips/blob/master/32.md) - 라벨링 표준

**언급된 곳:**
- [뉴스레터 #6: NIP 업데이트](/ko/newsletters/2026-01-21-newsletter/#nip-updates)

**참고:**
- [Trusted Relay Assertions](/ko/topics/trusted-relay-assertions/)
- [NIP-51: 목록](/ko/topics/nip-51/)
