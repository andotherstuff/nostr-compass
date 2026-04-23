---
title: "NIP-62: Vanish Requests"
date: 2026-01-13
translationOf: /en/topics/nip-62.md
translationDate: 2026-04-22
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-62는 vanish request, 즉 kind `62` 이벤트를 정의합니다. 이 이벤트는 특정 릴레이에 요청자의 pubkey에서 나온 모든 이벤트를 삭제해 달라고 요구합니다. 기본적으로 요청은 릴레이 대상이며, 특수한 `ALL_RELAYS` 태그 값을 사용하면 전역 요청으로도 브로드캐스트할 수 있습니다.

## 작동 방식

vanish request는 자신의 히스토리를 제거하고 싶은 pubkey가 서명한 kind `62` 이벤트입니다. 태그 목록에는 최소 하나 이상의 `relay` 값이 들어 있어야 하며, 여기에는 요청을 처리해야 할 릴레이가 명시됩니다.

```json
{
  "id": "a7b8c9d0e1f23456789012345678901234567890abcdef1234567890abcdef12",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1743465600,
  "kind": 62,
  "tags": [
    ["relay", "wss://relay.example.com"]
  ],
  "content": "Requesting deletion of all events from this relay.",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

`content` 필드에는 릴레이 운영자에게 전하는 사유나 법적 고지를 담을 수 있습니다. 클라이언트는 사용자가 네트워크 전역 vanish를 의도한 경우가 아니라면 이 이벤트를 널리 게시하기보다 대상 릴레이에 직접 보내야 합니다.

## 릴레이 동작

vanish request를 보고 자신의 서비스 URL이 `relay` 태그에 들어 있음을 확인한 릴레이는, 요청의 `created_at` 시점까지 해당 pubkey에서 나온 모든 이벤트를 완전히 삭제해야 합니다. 명세는 또한 릴레이가 vanished pubkey를 `p` 태그로 가리킨 [NIP-59](/ko/topics/nip-59/) (Gift Wrap) 이벤트도 삭제해야 한다고 말합니다. 따라서 사용자의 자체 이벤트뿐 아니라 들어오는 DM도 함께 제거됩니다.

릴레이는 삭제된 이벤트가 다시 브로드캐스트되어 재유입되지 않도록 해야 합니다. bookkeeping을 위해 서명된 vanish request 자체는 보관할 수 있습니다.

## 전역 요청

이 이벤트를 본 모든 릴레이에 삭제를 요청하려면 태그 값에 대문자 `ALL_RELAYS`를 사용합니다:

```json
{
  "kind": 62,
  "pubkey": "<32-byte-hex-pubkey>",
  "tags": [
    ["relay", "ALL_RELAYS"]
  ],
  "content": "Global vanish request"
}
```

클라이언트는 이 형태를 가능한 많은 릴레이에 브로드캐스트해야 합니다.

## 왜 중요한가

NIP-62는 임시 moderation API나 릴레이별 대시보드를 넘어서는, 클라이언트와 릴레이 운영자 사이의 공통 삭제 신호를 제공합니다. 사용자는 하나의 서명된 요청을 게시하고 각 릴레이가 동일한 이벤트 형식으로 이를 처리하게 할 수 있습니다.

또한 [NIP-09](/ko/topics/nip-09/)보다 더 나아갑니다. NIP-09는 개별 이벤트를 삭제하며 릴레이가 이를 따를 수 있습니다. NIP-62는 태그된 릴레이에 해당 pubkey의 모든 이벤트를 삭제하고, 그 이벤트가 다시 유입되지 않도록 요구합니다.

## 구현체

- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - 클라이언트 측 vanish request 지원
- [rust-nostr PR #1315](https://github.com/rust-nostr/nostr/pull/1315) - Memory backend 지원
- [rust-nostr PR #1316](https://github.com/rust-nostr/nostr/pull/1316) - LMDB backend 지원
- [rust-nostr PR #1317](https://github.com/rust-nostr/nostr/pull/1317) - SQLite backend 지원
- [rust-nostr PR #1318](https://github.com/rust-nostr/nostr/pull/1318) - 릴레이별 vanish 지원용 데이터베이스 테스트 추가
- [nostream PR #544](https://github.com/Cameri/nostream/pull/544) - 광고 기능 목록에 NIP-62 right-to-vanish 추가

---

**주요 출처:**
- [NIP-62 명세](https://github.com/nostr-protocol/nips/blob/master/62.md)
- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - 클라이언트 측 vanish 지원
- [rust-nostr PR #1315](https://github.com/rust-nostr/nostr/pull/1315)
- [rust-nostr PR #1316](https://github.com/rust-nostr/nostr/pull/1316)
- [rust-nostr PR #1317](https://github.com/rust-nostr/nostr/pull/1317)
- [rust-nostr PR #1318](https://github.com/rust-nostr/nostr/pull/1318)
- [nostream PR #544](https://github.com/Cameri/nostream/pull/544)

**언급된 뉴스레터:**
- [Newsletter #5: Notable Code Changes](/ko/newsletters/2026-01-13-newsletter/)
- [Newsletter #12: rust-nostr](/ko/newsletters/2026-03-04-newsletter/)
- [Newsletter #16: Amethyst ships NIP-62 support](/ko/newsletters/2026-04-01-newsletter/)
- [Newsletter #16: NIP Deep Dive](/ko/newsletters/2026-04-01-newsletter/)
- [Newsletter #19: nostream NIP-62 support](/en/newsletters/2026-04-22-newsletter/)

**같이 보기:**
- [NIP-09: 이벤트 삭제 요청](/ko/topics/nip-09/)
- [NIP-17: 비공개 DM](/ko/topics/nip-17/)
- [NIP-59: Gift Wrap](/ko/topics/nip-59/)
