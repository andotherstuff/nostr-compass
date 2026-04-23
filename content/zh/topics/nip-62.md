---
title: "NIP-62：Vanish Requests"
date: 2026-01-13
translationOf: /en/topics/nip-62.md
translationDate: 2026-04-22
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-62 定义了 vanish requests，也就是 kind `62` events，用于请求特定 relays 删除某个请求 pubkey 产生的所有 events。默认情况下，这种请求是面向特定 relay 的；如果使用特殊的 `ALL_RELAYS` tag 值，它也可以被广播成全网请求。

## 工作原理

vanish request 是一个由希望移除自己历史记录的 pubkey 签名的 kind `62` event。其 tag 列表中必须至少包含一个 `relay` 值，用来指明应该执行该请求的 relay。

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

`content` 字段可以包含给 relay 运营者看的理由或法律说明。除非用户明确想要发起全网 vanish 请求，否则客户端应把这个 event 直接发送给目标 relays，而不是广泛发布。

## Relay 行为

当 relay 看到 vanish request，并在 `relay` tag 中找到了自己的服务 URL 时，它必须完整删除该 pubkey 截至请求 `created_at` 之前的所有 events。规范还要求 relay 删除那些通过 `p` tag 指向已 vanish pubkey 的 [NIP-59](/zh/topics/nip-59/)（Gift Wrap）events，这样用户收到的私信也会随同其自身 events 一起被移除。

relay 还必须确保这些已删除 events 不能再被重新广播回该 relay。它可以出于记账目的保留这个已签名的 vanish request 本身。

## 全局请求

若要请求每一个看到该 event 的 relay 都删除相关数据，tag 值应使用全大写 `ALL_RELAYS`：

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

客户端应把这种形式尽可能广播到更多 relays。

## 为什么重要

NIP-62 为客户端与 relay 运营者提供了一种共享的删除信号，超越了临时性的审核 API 或 relay 专属 dashboard。用户可以发布一条已签名请求，让每个 relay 使用同一种 event 格式处理它。

它也超越了 [NIP-09](/zh/topics/nip-09/)。NIP-09 删除的是单个 events，而 relays 也未必会配合；NIP-62 则要求被打上 tag 的 relays 删除该 pubkey 的全部内容，并阻止这些 events 被重新导入。

## 实现

- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - 客户端侧 vanish request 支持
- [rust-nostr PR #1315](https://github.com/rust-nostr/nostr/pull/1315) - Memory backend 支持
- [rust-nostr PR #1316](https://github.com/rust-nostr/nostr/pull/1316) - LMDB backend 支持
- [rust-nostr PR #1317](https://github.com/rust-nostr/nostr/pull/1317) - SQLite backend 支持
- [rust-nostr PR #1318](https://github.com/rust-nostr/nostr/pull/1318) - 面向 relay-specific vanish 的数据库测试覆盖
- [nostream PR #544](https://github.com/Cameri/nostream/pull/544) - 将 NIP-62 right-to-vanish 加入广告能力列表

---

**主要来源：**
- [NIP-62 Specification](https://github.com/nostr-protocol/nips/blob/master/62.md)
- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - 客户端侧 vanish 支持
- [rust-nostr PR #1315](https://github.com/rust-nostr/nostr/pull/1315)
- [rust-nostr PR #1316](https://github.com/rust-nostr/nostr/pull/1316)
- [rust-nostr PR #1317](https://github.com/rust-nostr/nostr/pull/1317)
- [rust-nostr PR #1318](https://github.com/rust-nostr/nostr/pull/1318)
- [nostream PR #544](https://github.com/Cameri/nostream/pull/544)

**提及于：**
- [Newsletter #5：Notable Code Changes](/zh/newsletters/2026-01-13-newsletter/)
- [Newsletter #12：rust-nostr](/zh/newsletters/2026-03-04-newsletter/)
- [Newsletter #16：Amethyst ships NIP-62 support](/zh/newsletters/2026-04-01-newsletter/)
- [Newsletter #16：NIP Deep Dive](/zh/newsletters/2026-04-01-newsletter/)
- [Newsletter #19：nostream NIP-62 support](/en/newsletters/2026-04-22-newsletter/)

**另请参阅：**
- [NIP-09：Event Deletion Request](/zh/topics/nip-09/)
- [NIP-17：Private Direct Messages](/zh/topics/nip-17/)
- [NIP-59：Gift Wrap](/zh/topics/nip-59/)
