---
title: "NIP-62：消失请求"
date: 2026-01-13
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-62 定义了消失请求，这是一种用户请求 relay 删除其内容的机制。虽然 relay 没有义务遵守这些请求，但支持 NIP-62 可以让用户对其已发布的数据有更多控制权，并提供一种标准化的方式在网络中表达删除意图。

## 工作原理

消失请求是由想要删除内容的用户签署的 kind 62 event。请求可以通过在 `e` tag 中包含 event ID 来针对特定 event，或者通过完全省略 `e` tag 来请求删除该 pubkey 的所有内容。

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 62,
  "tags": [
    ["e", "event1234...", "wss://relay.example.com"],
    ["e", "event5678...", "wss://relay.example.com"]
  ],
  "content": "Removing old posts",
  "sig": "sig1234..."
}
```

`content` 字段可选地包含删除请求的人类可读原因。`e` tag 中的 relay 提示告诉 relay 原始 event 发布在哪里，尽管 relay 可能无论是否拥有指定的 event 都会遵守请求。

## Relay 行为

支持 NIP-62 的 relay 应该从其存储中删除指定的 event 并停止向订阅者提供它们。消失请求本身可能被保留作为请求删除的记录，这有助于防止已删除的 event 从其他 relay 重新导入。

当消失请求省略所有 `e` tag 时，relay 将其解释为请求删除该 pubkey 的所有 event。这是一个更激烈的操作，relay 可能会以不同方式处理，例如将该 pubkey 标记为「已消失」并拒绝接受或提供其任何 event。

Relay 不要求支持 NIP-62。Nostr 网络是去中心化的，每个 relay 运营者决定自己的数据保留策略。用户不应该仅仅因为发布了消失请求就假设他们的内容会在所有地方被删除。

## 隐私考虑

消失请求是一种尽力而为的删除机制，不是隐私保证。即使发布消失请求后，内容的副本可能仍存在于网络的其他地方，包括不支持 NIP-62 的其他 relay、客户端设备上的本地缓存、第三方存档或搜索引擎，以及备份中。

请求本身也是一个签名的 Nostr event，意味着它成为您公开记录的一部分。任何看到消失请求的人都知道您删除了某些东西，即使他们看不到删除的是什么。

对于必须保持私密的内容，请考虑使用 [NIP-17](/zh/topics/nip-17/) 等加密消息，而不是依赖事后删除。

---

**主要来源：**
- [NIP-62 规范](https://github.com/nostr-protocol/nips/blob/master/62.md)

**相关提及：**
- [Newsletter #5：值得关注的代码变更](/zh/newsletters/2026-01-13-newsletter/#rust-nostr-library)
