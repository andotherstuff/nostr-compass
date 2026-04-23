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

NIP-62は、vanish requestを定義します。これは、要求者のpubkeyに属するすべてのイベントを削除するよう特定relayへ求めるkind `62`イベントです。このrequestはデフォルトではrelay指定型で、特別な`ALL_RELAYS`タグ値を使えばglobal requestとしてbroadcastすることもできます。

## 仕組み

vanish requestは、自分の履歴削除を望むpubkeyが署名したkind `62`イベントです。tag listには、そのrequestを処理すべきrelayを示す`relay`値が最低1つ必要です。

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

`content`フィールドには、relay operator向けの理由や法的通知を入れられます。clientは、ユーザーがnetwork-wide vanish requestを意図していない限り、広く投稿するのではなく対象relayへ直接このイベントを送るべきです。

## Relay behavior

vanish requestを見て、`relay`タグ内に自分のservice URLがあるrelayは、そのpubkeyから発せられた`created_at`までのイベントを完全に削除しなければなりません。仕様はまた、relayが消えたpubkeyを`p`タグしていた[NIP-59](/ja/topics/nip-59/)（Gift Wrap）イベントも削除すべきだと述べています。これにより、受信DMもユーザー自身のイベントと一緒に消えます。

relayはさらに、その削除済みイベントが再broadcastされてrelayへ戻ることも防ぐ必要があります。帳簿目的で署名済みvanish request自体は保持してよいとされています。

## Global requests

イベントを見たすべてのrelayで削除を求める場合、タグ値は大文字の`ALL_RELAYS`になります。

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

clientはこの形式を、できるだけ多くのrelayへbroadcastするべきです。

## なぜ重要か

NIP-62は、ad hocなmoderation APIやrelay固有dashboardを超えて、clientとrelay operatorが共有できる削除シグナルを与えます。ユーザーは1つの署名済みrequestを公開し、各relayに同じevent formatで処理させられます。

これは[NIP-09](/ja/topics/nip-09/)も超えます。NIP-09は個別イベントを削除し、relayは従うかもしれません。NIP-62は、タグ付けされたrelayへ、そのpubkeyのすべてを削除し、それらイベントの再取り込みまで防ぐよう求めます。

## Implementations

- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - client側のvanish request support
- [rust-nostr PR #1315](https://github.com/rust-nostr/nostr/pull/1315) - Memory backend support
- [rust-nostr PR #1316](https://github.com/rust-nostr/nostr/pull/1316) - LMDB backend support
- [rust-nostr PR #1317](https://github.com/rust-nostr/nostr/pull/1317) - SQLite backend support
- [rust-nostr PR #1318](https://github.com/rust-nostr/nostr/pull/1318) - relay-specific vanish support向けdatabase test coverage
- [nostream PR #544](https://github.com/Cameri/nostream/pull/544) - advertiseされるfeature listへNIP-62 right-to-vanishを追加

---

**Primary sources:**
- [NIP-62 Specification](https://github.com/nostr-protocol/nips/blob/master/62.md)
- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - Client-side vanish support
- [rust-nostr PR #1315](https://github.com/rust-nostr/nostr/pull/1315)
- [rust-nostr PR #1316](https://github.com/rust-nostr/nostr/pull/1316)
- [rust-nostr PR #1317](https://github.com/rust-nostr/nostr/pull/1317)
- [rust-nostr PR #1318](https://github.com/rust-nostr/nostr/pull/1318)
- [nostream PR #544](https://github.com/Cameri/nostream/pull/544)

**Mentioned in:**
- [Newsletter #5: Notable Code Changes](/ja/newsletters/2026-01-13-newsletter/)
- [Newsletter #12: rust-nostr](/ja/newsletters/2026-03-04-newsletter/)
- [Newsletter #16: Amethyst ships NIP-62 support](/ja/newsletters/2026-04-01-newsletter/)
- [Newsletter #16: NIP Deep Dive](/ja/newsletters/2026-04-01-newsletter/)
- [Newsletter #19: nostream NIP-62 support](/en/newsletters/2026-04-22-newsletter/)

**See also:**
- [NIP-09: Event Deletion Request](/ja/topics/nip-09/)
- [NIP-17: Private Direct Messages](/ja/topics/nip-17/)
- [NIP-59: Gift Wrap](/ja/topics/nip-59/)
