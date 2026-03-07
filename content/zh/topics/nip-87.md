---
title: "NIP-87: Ecash 铸币厂可发现性"
date: 2026-01-07
translationOf: /en/topics/nip-87.md
translationDate: 2026-03-07
draft: false
categories:
  - Ecash
  - Discovery
  - Protocol
---

NIP-87 定义了 ecash 铸币厂（Cashu 和 Fedimint）如何在 Nostr 上发布自我公告，以及用户如何向他人推荐铸币厂。

## 事件种类

- **kind 38172** - Cashu 铸币厂公告（由铸币厂运营者发布）
- **kind 38173** - Fedimint 公告（由铸币厂运营者发布）
- **kind 38000** - 铸币厂推荐（由用户发布）

## 工作原理

1. **铸币厂运营者** 发布铸币厂的 URL、支持的功能以及所处网络（mainnet/testnet）
2. **用户** 为自己信任的铸币厂发布推荐，并可附带评价
3. **其他用户** 查询所关注账号的推荐，以发现可信的铸币厂

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

`nuts` 标签列出支持的 NUT（Cashu 的 Notation, Usage, and Terminology 规范）。

`d` 标签应当使用铸币厂的 Cashu pubkey。即使铸币厂之后更改元数据或重新发布公告，它也能为客户端提供一个稳定的发现标识符。

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

推荐事件属于 parameterized replaceable events。这一点很有用，因为用户可以修改推荐、更新评价文本，或停止为某个铸币厂背书，而不会留下多条过时的推荐事件。

## 信任模型

NIP-87 不会告诉客户端哪个铸币厂是安全的。它提供的是一种组合方式，让客户端将运营者自行发布的元数据与用户已信任账号给出的社交推荐结合起来。

这一区别很重要，因为直接查询铸币厂公告事件可能会遭遇噪声或恶意内容。规范明确提醒客户端，在绕过社交推荐、直接查询公告时，应使用防垃圾措施或高质量中继。

## 互操作说明

Cashu 和 Fedimint 使用不同的公告 kind，因为它们公开的连接细节不同。Cashu 公告发布铸币厂 URL 和支持的 NUT，而 Fedimint 公告发布邀请码和支持的 federation 模块。一个同时支持两者的钱包需要解析这两种格式。

---

**主要来源：**
- [NIP-87 规范](https://github.com/nostr-protocol/nips/blob/master/87.md)

**提及于：**
- [第4期周刊：版本发布](/zh/newsletters/2026-01-07-newsletter/#releases)
- [第7期周刊：Zeus](/zh/newsletters/2026-01-28-newsletter/)

**另请参阅：**
- [Cashu](/zh/topics/cashu/)
- [NIP-60: Cashu 钱包](/zh/topics/nip-60/)
