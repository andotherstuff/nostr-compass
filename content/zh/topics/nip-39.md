---
title: "NIP-39：个人资料中的外部身份"
date: 2026-02-11
draft: false
translationOf: /en/topics/nip-39.md
translationDate: 2026-03-07
categories:
  - NIPs
  - Identity
---

NIP-39 定义了用户如何使用 `i` 标签将外部身份声明附加到 Nostr 个人资料中。这些标签将 Nostr 公钥与 GitHub、Twitter、Mastodon 或 Telegram 等外部平台上的账户关联。

## 工作原理

用户在 kind 10011 事件中以 `i` 标签发布身份声明。每个标签包含一个 `platform:identity` 值以及一个证明指针，客户端可以用它来验证声明：

```json
{
  "kind": 10011,
  "tags": [
    ["i", "github:username", "gist-id"],
    ["i", "twitter:handle", "tweet-id"]
  ]
}
```

客户端根据平台和证明值重建证明 URL，然后检查外部帖子是否包含用户的 `npub`。这使得声明可以在各客户端之间移植，而无需中央验证者。

## 证明模型

重要的细节是，NIP-39 同时证明了两个身份的控制权：Nostr 密钥和外部账户。如果证明的任何一方消失，验证就会变弱。删除的 gist 或推文不会使历史事件无效，但会移除大多数客户端依赖的实时证明。

另一个有用的实现要点是获取策略。由于声明现在存放在 kind 0 之外，客户端可以决定是仅在个人资料详情视图中请求它们、仅为关注的用户请求，还是完全不请求。这避免了给本已频繁访问的 kind 0 路径增加更多负担。

## 当前状态

按照当前规范，身份声明存放在专用的 kind 10011 事件中，而非 kind 0 元数据中。这一分离源于精简 kind 0 个人资料获取的更广泛工作。

---

**主要来源：**
- [NIP-39：个人资料中的外部身份](https://github.com/nostr-protocol/nips/blob/master/39.md)
- [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) - 将身份声明从 kind 0 中移出

**提及于：**
- [Newsletter #9：NIP 更新](/zh/newsletters/2026-02-11-newsletter/#nip-updates)
- [Newsletter #12：Amethyst](/zh/newsletters/2026-03-04-newsletter/#amethyst-nip-39-nip-c0-nip-66)

**另请参阅：**
- [NIP-05：基于 DNS 的验证](/zh/topics/nip-05/)
