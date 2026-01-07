---
title: "NIP-87: Ecash 铸币厂可发现性"
date: 2026-01-07
draft: false
categories:
  - Ecash
  - Discovery
  - Protocol
---

NIP-87 定义了 ecash 铸币厂（Cashu 和 Fedimint）如何在 Nostr 上宣布自己，以及用户如何向他人推荐铸币厂。

## 事件类型

- **kind 38172** - Cashu 铸币厂公告（由铸币厂运营者发布）
- **kind 38173** - Fedimint 公告（由铸币厂运营者发布）
- **kind 38000** - 铸币厂推荐（由用户发布）

## 工作原理

1. **铸币厂运营者**发布其铸币厂的 URL、支持的功能和网络（mainnet/testnet）
2. **用户**信任某个铸币厂后，发布带有可选评价的推荐
3. **其他用户**查询他们关注的人的推荐来发现可信的铸币厂

## Cashu 铸币厂公告

```json
{
  "id": "<event-id>",
  "pubkey": "<mint-operator-pubkey>",
  "created_at": 1736200000,
  "kind": 38172,
  "tags": [
    ["d", "<mint-pubkey>"],
    ["u", "https://mint.example.com"],
    ["nuts", "1,2,3,4,5,6,7"],
    ["n", "mainnet"]
  ],
  "content": "",
  "sig": "<signature>"
}
```

`nuts` 标签列出支持的 NUT（Cashu 的符号、用法和术语规范）。

## 用户推荐

```json
{
  "id": "<event-id>",
  "pubkey": "<recommender-pubkey>",
  "created_at": 1736200000,
  "kind": 38000,
  "tags": [
    ["k", "38172"],
    ["d", "<mint-identifier>"],
    ["a", "38172:mint-pubkey:<d-tag>", "wss://relay"]
  ],
  "content": "I've used this mint for months, very reliable",
  "sig": "<signature>"
}
```

用户可以在 `content` 字段中包含评价，并指向特定的铸币厂公告事件。

---

**主要来源：**
- [NIP-87 规范](https://github.com/nostr-protocol/nips/blob/master/87.md)

**提及于：**
- [周刊 #4: 版本发布](/zh/newsletters/2026-01-07-newsletter/#releases)

**另请参阅：**
- [NIP-60: Cashu 钱包](/zh/topics/nip-60/)
