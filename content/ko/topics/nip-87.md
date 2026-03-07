---
title: "NIP-87: Ecash 민트 발견"
date: 2026-01-07
translationOf: /en/topics/nip-87.md
translationDate: 2026-03-07
draft: false
categories:
  - Ecash
  - Discovery
  - Protocol
---
NIP-87은 ecash 민트(Cashu 및 Fedimint)가 Nostr에서 자신을 알리는 방법과 사용자가 다른 사람에게 민트를 추천하는 방법을 정의한다.

## 이벤트 종류

- **kind 38172** - Cashu 민트 공지 (민트 운영자가 게시)
- **kind 38173** - Fedimint 공지 (민트 운영자가 게시)
- **kind 38000** - 민트 추천 (사용자가 게시)

## 작동 방식

1. **민트 운영자**가 민트의 URL, 지원 기능 및 네트워크(mainnet/testnet)를 게시한다
2. **사용자**가 신뢰하는 민트에 대해 선택적 리뷰와 함께 추천을 게시한다
3. **다른 사용자**가 팔로우하는 사람들의 추천을 조회하여 신뢰할 수 있는 민트를 발견한다

## Cashu 민트 공지

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

`nuts` 태그는 지원되는 NUT(Cashu의 Notation, Usage, and Terminology 명세)를 나열한다.

`d` 태그는 민트의 Cashu pubkey여야 하며, 이를 통해 민트가 나중에 메타데이터를 변경하거나 공지를 다시 게시하더라도 클라이언트에 하나의 안정적인 발견 식별자를 제공한다.

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
  "content": "I've used this mint for months, very reliable",
  "sig": "<signature>"
}
```

사용자는 `content` 필드에 리뷰를 포함하고 특정 민트 공지 이벤트를 가리킬 수 있다.

추천 이벤트는 매개변수화된 교체 가능 이벤트다. 사용자가 추천을 수정하거나, 리뷰 텍스트를 업데이트하거나, 여러 개의 오래된 추천 이벤트를 남기지 않고 민트 보증을 중단할 수 있어 유용하다.

## 신뢰 모델

NIP-87은 클라이언트에게 어떤 민트가 안전한지 알려주지 않는다. 운영자가 게시한 메타데이터와 사용자가 이미 신뢰하는 계정의 소셜 추천을 결합하는 방법을 제공한다.

이 구분이 중요한 이유는 민트 공지 이벤트에 대한 직접 조회가 노이즈가 많거나 악의적일 수 있기 때문이다. 명세는 소셜 추천을 우회하고 공지를 직접 조회할 때 스팸 방지 조치나 고품질 릴레이를 사용하도록 클라이언트에 명시적으로 경고한다.

## 상호운용성 참고사항

Cashu와 Fedimint는 서로 다른 연결 정보를 노출하므로 다른 공지 kind를 사용한다. Cashu 공지는 민트 URL과 지원되는 NUT를 게시하고, Fedimint 공지는 초대 코드와 지원되는 연합 모듈을 게시한다. 둘 다 지원하는 지갑은 두 형식 모두 파싱해야 한다.

---

**주요 출처:**
- [NIP-87 명세](https://github.com/nostr-protocol/nips/blob/master/87.md)

**언급된 뉴스레터:**
- [Newsletter #4: 릴리스](/en/newsletters/2026-01-07-newsletter/#releases)
- [Newsletter #7: Zeus](/en/newsletters/2026-01-28-newsletter/)

**같이 보기:**
- [Cashu](/ko/topics/cashu/)
- [NIP-60: Cashu 지갑](/ko/topics/nip-60/)
