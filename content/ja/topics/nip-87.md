---
title: "NIP-87: Ecashミント発見"
date: 2026-01-07
draft: false
categories:
  - Ecash
  - Discovery
  - Protocol
---

NIP-87は、ecashミント（CashuおよびFedimint）がNostr上で自身をアナウンスする方法と、ユーザーが他のユーザーにミントを推薦する方法を定義します。

## イベント種別

- **kind 38172** - Cashuミントアナウンス（ミント運営者が公開）
- **kind 38173** - Fedimintアナウンス（ミント運営者が公開）
- **kind 38000** - ミント推薦（ユーザーが公開）

## 仕組み

1. **ミント運営者**がミントのURL、サポートされている機能、ネットワーク（mainnet/testnet）を公開
2. **ユーザー**がミントを信頼する場合、オプションのレビュー付きで推薦を公開
3. **他のユーザー**がフォローしている人からの推薦をクエリして信頼できるミントを発見

## Cashuミントアナウンス

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

`nuts`タグはサポートされているNUT（Cashuの表記法、使用法、用語仕様）をリストします。

## ユーザー推薦

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

ユーザーは`content`フィールドにレビューを含め、特定のミントアナウンスイベントを指し示すことができます。

---

**主要ソース:**
- [NIP-87仕様](https://github.com/nostr-protocol/nips/blob/master/87.md)

**言及箇所:**
- [ニュースレター#4: リリース](/ja/newsletters/2026-01-07-newsletter/#releases)

**関連項目:**
- [NIP-60: Cashuウォレット](/ja/topics/nip-60/)
