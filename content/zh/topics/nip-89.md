---
title: "NIP-89: 推荐应用处理程序"
date: 2026-01-07
draft: false
categories:
  - Discovery
  - Clients
  - Protocol
---

NIP-89 定义了应用如何宣布其能力，以及用户如何推荐处理特定事件类型的应用。

## 事件类型

- **kind 31990** - 应用处理程序（由应用开发者发布）
- **kind 31989** - 应用推荐（由用户发布）

## 工作原理

1. **应用**发布处理程序事件，描述它们支持哪些事件类型以及如何打开内容
2. **用户**推荐他们用于特定事件类型的应用
3. **客户端**查询推荐以提供未知事件类型的"用...打开"功能

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

`k` 标签指定支持的事件类型。URL 模板使用 `<bech32>` 作为 NIP-19 编码实体的占位符。

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

`d` 标签是被推荐的事件类型。多个 `a` 标签可以为不同平台推荐不同的应用。

## 使用场景

- 发现可以显示长文章（kind 30023）的应用
- 查找支持特定事件类型的客户端
- 跨客户端的"用...打开"功能
- 检测客户端对加密支持的能力

---

**主要来源：**
- [NIP-89 规范](https://github.com/nostr-protocol/nips/blob/master/89.md)

**提及于：**
- [周刊 #4: NIP 深度解析](/zh/newsletters/2026-01-07-newsletter/#nip-44-versioned-encryption)

**另请参阅：**
- [NIP-19: Bech32 编码实体](/zh/topics/nip-19/)
