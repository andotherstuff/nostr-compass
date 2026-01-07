---
title: "NIP-87: Ecash Mint 검색"
date: 2026-01-07
draft: false
categories:
  - Ecash
  - Discovery
  - Protocol
---

NIP-87은 ecash mint(Cashu 및 Fedimint)가 Nostr에서 자신을 알리는 방법과 사용자가 다른 사람에게 mint를 추천하는 방법을 정의합니다.

## 이벤트 종류

- **kind 38172** - Cashu mint 공지(mint 운영자가 게시)
- **kind 38173** - Fedimint 공지(mint 운영자가 게시)
- **kind 38000** - Mint 추천(사용자가 게시)

## 작동 방식

1. **Mint 운영자**가 mint의 URL, 지원 기능, 네트워크(mainnet/testnet)를 게시합니다
2. mint를 신뢰하는 **사용자**가 선택적 리뷰와 함께 추천을 게시합니다
3. **다른 사용자**가 팔로우하는 사람들의 추천을 쿼리하여 신뢰할 수 있는 mint를 발견합니다

## Cashu Mint 공지

```json
{
  "id": "<event-id>",
  "pubkey": "<mint-operator-pubkey>",
  "created_at": 1736200000,
  "kind": 38172,
  "tags": [
    ["d", "<mint-pubkey>"],
    ["u", "https://mint.example.com"],
    ["nuts", "1,2,3,4,5,6,7"],
    ["n", "mainnet"]
  ],
  "content": "",
  "sig": "<signature>"
}
```

`nuts` 태그는 지원되는 NUT(Cashu를 위한 Notation, Usage, and Terminology 스펙)를 나열합니다.

## 사용자 추천

```json
{
  "id": "<event-id>",
  "pubkey": "<recommender-pubkey>",
  "created_at": 1736200000,
  "kind": 38000,
  "tags": [
    ["k", "38172"],
    ["d", "<mint-identifier>"],
    ["a", "38172:mint-pubkey:<d-tag>", "wss://relay"]
  ],
  "content": "이 mint를 몇 달간 사용해왔는데, 매우 신뢰할 만합니다",
  "sig": "<signature>"
}
```

사용자는 `content` 필드에 리뷰를 포함하고 특정 mint 공지 이벤트를 가리킬 수 있습니다.

---

**주요 자료:**
- [NIP-87 명세](https://github.com/nostr-protocol/nips/blob/master/87.md)

**언급된 곳:**
- [뉴스레터 #4: 릴리스](/ko/newsletters/2026-01-07-newsletter/#릴리스)

**관련 항목:**
- [NIP-60: Cashu 지갑](/ko/topics/nip-60/)
