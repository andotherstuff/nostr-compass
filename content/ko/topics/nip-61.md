---
title: "NIP-61: Nutzaps"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-61.md
translationDate: 2026-07-01
categories:
  - Zaps
  - Ecash
---

NIP-61은 Nostr 이벤트로 전달되는 P2P Cashu ecash 결제인 "nutzap"을 정의한다. 발신자는 수신자의 Nostr 키로 주소가 지정된 P2PK 잠금된 Cashu token을 게시하고, 수신자는 자신의 편의에 따라 mint에서 이를 상환한다. proof 자체가 가치를 담고 있으므로, NIP-61 결제는 수신자가 자신의 일정에 따라 상환할 수 있는 자체 포함된 token으로 도착하며, Lightning 채널이나 대화형 핸드셰이크가 필요하지 않다.

## 작동 방식

NIP-61은 두 가지 기존 프리미티브 위에 구축된다: [NIP-60](/ko/topics/nip-60/) Cashu 지갑과 Cashu의 P2PK 잠금. 흐름은 세 가지 event kind를 사용한다.

**Mint 추천 (kind 10019):** 수신자가 게시하는 대체 가능 이벤트로, nutzap을 받을 mint와 proof를 자신에게 잠그는 데 사용되는 Cashu 공개 키를 알린다. 발신자는 잠긴 token이 수신자가 상환할 수 있는 것인지 확인하기 위해 보내기 전에 이를 읽는다.

**Nutzap 이벤트 (kind 9321):** 결제 자체이다. Cashu proof (kind 10019의 수신자 nutzap pubkey로 P2PK 잠금), mint URL, zap된 노트를 식별하는 선택적 `e` 및 `a` tag, 수신자용 `p` tag를 담는다. 수신자는 일반적인 Nostr 구독을 통해 이를 수신하고, 해당 개인 키로 proof를 잠금 해제한 다음, NIP-60 지갑에 보관하거나 Lightning으로 melt한다.

**Nutzap 정보 (kind 7375):** NIP-60 token 이벤트와 동일한 형태의 캐시된 상태로, 상환된 nutzap proof를 기록하여 지갑이 resync 시 이중 계산하지 않도록 한다.

## 트레이드오프와 신뢰 모델

nutzap은 자체 포함된 ecash token이다. 수신자가 나중에 mint에 연락할 수 있는 한 결제를 상환할 수 있다. mint 자체는 신뢰할 수 있는 관리자이며, 이는 NIP-60과 동일한 신뢰 모델이고, 이 관리 선택은 오프라인 가능한 즉각적인 확정성을 갖춘 마이크로 결제의 명시적인 대가이다. NIP-57 zap은 수신자가 실시간으로 들어오는 HTLC를 수락하는 LNURL 엔드포인트가 있는 Lightning 노드를 실행하거나 호스팅해야 한다. Lightning 채널이 없는 휴대폰, 방화벽 뒤의 사용자, 그리고 오프라인 상태인 수신자는 모두 그 모델 밖에 있다.

kind 10019 광고는 소셜 계층 신뢰 게이트이다. 발신자는 수신자가 수락한 mint 중 하나를 선택하며, 이는 수신자의 상환 경로를 예측 가능하게 유지한다. 수신자 세트 외의 mint를 선택하는 발신자는 상환할 수 없는 token의 위험을 감수하므로, 지갑은 kind 10019를 먼저 읽는다.

## 워크플로

1. 수신자가 수락한 mint와 nutzap pubkey를 알리는 kind 10019를 게시한다
2. 발신자가 kind 10019를 읽고, 나열된 mint 중 하나에서 proof를 mint하고, 수신자의 nutzap pubkey에 P2PK 잠금을 건다
3. 발신자가 잠긴 proof, mint URL, 대상 tag가 있는 kind 9321을 게시한다
4. 수신자가 일반 Nostr 구독을 통해 kind 9321을 수신한다
5. 수신자가 자신의 nutzap 개인 키를 사용하여 proof를 잠금 해제하고, NIP-60 지갑에 보관하거나 Lightning으로 melt한다

## Nutzap 이벤트 예시

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1750162800,
  "kind": 9321,
  "tags": [
    ["proof", "{\"amount\":21,\"secret\":\"...\",\"C\":\"...\",\"id\":\"...\"}"],
    ["u", "https://mint.example.com"],
    ["e", "8b39f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3"],
    ["p", "c5d8a4e3b2a1f0e9d8c7b6a5949382716050403020100ffeeddccbbaa99887766"]
  ],
  "content": "Great post!",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

## 구현

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0)은 NIP-60/NIP-61 지갑 표면의 일부로 mint별 잔액 뷰가 있는 nutzap 렌더링을 출시했다 ([PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075))

---

**주요 출처:**
- [NIP-61 명세](https://github.com/nostr-protocol/nips/blob/master/61.md)
- [Amethyst PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075) - NIP-60 Cashu 지갑 및 NIP-61 nutzap 지원

**언급된 곳:**
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/ko/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**참고:**
- [NIP-57: Zaps](/ko/topics/nip-57/)
- [NIP-60: Cashu Wallet](/ko/topics/nip-60/)
- [Cashu](/ko/topics/cashu/)
