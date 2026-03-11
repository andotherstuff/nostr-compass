---
title: "NIP-39：个人资料中的外部身份"
date: 2026-02-11
translationOf: /en/topics/nip-39.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - 身份
---

NIP-39 定义了用户如何使用 `i` 标签将外部身份声明附加到自己的 Nostr 个人资料中。这些标签把 Nostr pubkey 与 GitHub、Twitter、Mastodon 或 Telegram 等外部平台上的账户关联起来。

## 工作原理

用户以 `i` 标签的形式，在 kind 10011 事件中发布身份声明。每个标签都包含一个 `platform:identity` 值，以及一个让客户端能够验证该声明的证明指针：

```json
{
  "id": "5f1c7b7e2c6f3d4a9b0e6a2d8c1f7e3b4a6d9c0e1f2a3b4c5d6e7f8091a2b3c4",
  "pubkey": "3bf0c63fcb8d0d8b6a8fcb3c7f5cb2a972f8a0b5a3d6d8790bb2d4e4f0d6b1c2",
  "created_at": 1741699200,
  "kind": 10011,
  "tags": [
    ["i", "github:alice", "9f5df4e2a8b14c1f9e6d2b7c4a1e8f90"],
    ["i", "twitter:alice_dev", "1898123456789012345"]
  ],
  "content": "",
  "sig": "8f4c62d8a7e9b1c3d5f7091a2b4c6d8e0f1234567890abcdeffedcba09876543211223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

客户端会根据平台和证明值重建证明 URL，然后检查外部帖子中是否包含用户的 `npub`。这让身份声明可以跨客户端携带，而无需依赖中心化验证者。

## 证明模型

这里最重要的细节是，NIP-39 同时证明了两个身份的控制权：Nostr 密钥和外部账户。如果证明链条中的任一侧消失，验证就会变弱。某个 gist 或 tweet 被删除，并不会让历史事件失效，但它确实会移除多数客户端所依赖的实时证明。

另一个值得注意的实现点在于抓取策略。由于这些声明现在位于 kind 0 之外，客户端可以决定只在个人资料详情页请求、只对已关注用户请求，或者完全不请求。这样可以避免给本就繁忙的 kind 0 路径继续加重负担。

## 实现情况

- [Amethyst PR #1747](https://github.com/vitorpamplona/amethyst/pull/1747) - 将外部身份作为独立的 kind 10011 事件发布
- [PR #2256](https://github.com/nostr-protocol/nips/pull/2256) - 在 NIP 集合中加入明确的 kind 10011 注册表引用

## 当前状态

按照当前规范，身份声明存在专门的 kind 10011 事件中，而不再放在 kind 0 元数据里。这个分离来自于更广泛的 kind 0 profile 抓取瘦身工作。

---

**主要来源：**
- [NIP-39：个人资料中的外部身份](https://github.com/nostr-protocol/nips/blob/master/39.md)
- [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) - 将身份声明移出 kind 0
- [PR #2256](https://github.com/nostr-protocol/nips/pull/2256) - 增加明确的 kind 10011 引用

**提及于：**
- [Newsletter #9：NIP 更新](/zh/newsletters/2026-02-11-newsletter/#nip-updates)
- [Newsletter #12：Amethyst](/zh/newsletters/2026-03-04-newsletter/#amethystnip-39nip-c0nip-66)
- [Newsletter #13：NIP 更新](/zh/newsletters/2026-03-11-newsletter/#nip-更新)

**另请参阅：**
- [NIP-05：基于 DNS 的验证](/zh/topics/nip-05/)
