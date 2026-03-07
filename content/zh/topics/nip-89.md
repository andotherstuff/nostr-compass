---
title: "NIP-89: 推荐应用处理程序"
date: 2026-01-07
translationOf: /en/topics/nip-89.md
translationDate: 2026-03-07
draft: false
categories:
  - Discovery
  - Clients
  - Protocol
---

NIP-89 定义了应用如何声明自身能力，以及用户如何推荐处理特定 event kind 的应用。

## 事件种类

- **kind 31990** - 应用处理程序（由应用开发者发布）
- **kind 31989** - 应用推荐（由用户发布）

## 工作原理

1. **应用** 发布处理程序事件，描述自己支持哪些 event kind，以及应如何打开内容
2. **用户** 推荐自己在特定 event kind 上使用的应用
3. **客户端** 查询推荐，为未知事件类型提供“打开方式...”功能

## 应用处理程序

```json
{
  "id": "<event-id>",
  "pubkey": "<app-developer-pubkey>",
  "created_at": 1736200000,
  "kind": 31990,
  "tags": [
    ["d", "<app-identifier>"],
    ["k", "30023"],
    ["web", "https://app.example.com/a/<bech32>", "naddr"],
    ["ios", "appname://open/<bech32>"]
  ],
  "content": "{\"name\": \"My App\", \"picture\": \"...\"}",
  "sig": "<signature>"
}
```

`k` 标签指定支持的 event kind。URL 模板使用 `<bech32>` 作为 NIP-19 编码实体的占位符。

如果多个支持的 kind 共享同一种路由模式，同一个处理程序事件可以同时公告它们。这让应用发现保持紧凑，也避免了在目标逻辑完全相同时为每个 kind 单独发布一个处理程序事件。

## 用户推荐

```json
{
  "id": "<event-id>",
  "pubkey": "<user-pubkey>",
  "created_at": 1736200000,
  "kind": 31989,
  "tags": [
    ["d", "30023"],
    ["a", "31990:app-pubkey:identifier", "wss://relay", "web"]
  ],
  "content": "",
  "sig": "<signature>"
}
```

`d` 标签表示被推荐的 event kind。多个 `a` 标签可以为不同平台推荐不同的应用。

## Client 标签

NIP-89 还定义了一个可选的 `client` 标签，发布应用可以把它附加到普通事件上。它记录客户端名称以及指向处理程序事件的引用，这样其他客户端就能显示一条帖子来自哪里，或者查询更完整的应用元数据。

这也带来隐私影响。规范明确指出，客户端应允许用户选择退出，因为在每条事件上公开发布软件身份，可能会暴露使用模式，而有些人并不希望这些模式被看见。

## 使用场景

- 发现可以显示长文章（kind 30023）的应用
- 查找支持特定事件类型的客户端
- 跨客户端的"用...打开"功能
- 检测客户端对加密支持的能力

## 信任与安全说明

NIP-89 提高了互操作性，但它也创造了一个重定向面。如果客户端从不受信任的中继查询任意处理程序公告，就可能把用户引导到恶意或具有误导性的应用。

这也是为什么推荐流程从你已关注的人开始。经过社交关系过滤的推荐并不完美，但它比把所有已发布的处理程序都视为同等可信要安全得多。

---

**主要来源：**
- [NIP-89 规范](https://github.com/nostr-protocol/nips/blob/master/89.md)

**提及于：**
- [第4期周刊：NIP 深度解析](/zh/newsletters/2026-01-07-newsletter/#nip-44-versioned-encryption)
- [第12期周刊：Damus](/zh/newsletters/2026-03-04-newsletter/#damus-nip-89-recommended-application-handlers)

**另请参阅：**
- [NIP-19：Bech32 编码实体](/zh/topics/nip-19/)
