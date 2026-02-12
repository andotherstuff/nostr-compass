---
title: "NIP-39：个人资料中的外部身份"
date: 2026-02-11
translationOf: /en/topics/nip-39.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Identity
---

NIP-39 定义了用户如何使用 `i` tag 将外部身份声明附加到其 Nostr 个人资料。这些 tag 将 Nostr pubkey 与 GitHub、Twitter 或 DNS 域名等外部平台上的账户关联起来。

## 工作原理

用户将身份声明发布为 `i` tag。每个 tag 包含一个平台标识符和一个证明 URL，外部账户通过该 URL 链接回 Nostr pubkey，建立双向验证：

```json
{
  "tags": [
    ["i", "github:username", "https://gist.github.com/username/proof"],
    ["i", "twitter:handle", "https://twitter.com/handle/status/proof_tweet_id"]
  ]
}
```

客户端通过获取证明 URL 并检查其中是否包含用户的 Nostr pubkey 来验证声明。这在不依赖中心化验证服务的情况下创建了一个身份连接网络。

## 近期变更

截至 2026 年 2 月，[PR #2216](https://github.com/nostr-protocol/nips/pull/2216) 将身份 tag 从 kind 0（用户元数据）event 提取到专用的 kind 10011。此举是 vitorpamplona kind 0 瘦身运动的一部分，原因是采用率低：几乎没有客户端实现 `i` tag 验证，但每次 kind 0 获取都要承担其开销。新的 kind 10011 让有兴趣的客户端可以单独获取身份声明。

---

**主要来源：**
- [NIP-39: External Identities in Profiles](https://github.com/nostr-protocol/nips/blob/master/39.md)

**提及于：**
- [新闻通讯 #9：NIP 更新](/zh/newsletters/2026-02-11-newsletter/#nip-更新)

**另见：**
- [NIP-05：基于 DNS 的验证](/zh/topics/nip-05/)
