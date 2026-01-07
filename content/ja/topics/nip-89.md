---
title: "NIP-89: 推奨アプリケーションハンドラー"
date: 2026-01-07
draft: false
categories:
  - Discovery
  - Clients
  - Protocol
---

NIP-89は、アプリケーションが自身の機能をアナウンスする方法と、ユーザーが特定のイベント種別を処理するアプリを推薦する方法を定義します。

## イベント種別

- **kind 31990** - アプリケーションハンドラー（アプリ開発者が公開）
- **kind 31989** - アプリ推薦（ユーザーが公開）

## 仕組み

1. **アプリケーション**がサポートするイベント種別とコンテンツを開く方法を説明するハンドラーイベントを公開
2. **ユーザー**が特定のイベント種別に使用しているアプリを推薦
3. **クライアント**が推薦をクエリして、未知のイベントタイプに「...で開く」機能を提供

## アプリケーションハンドラー

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

`k`タグはサポートされているイベント種別を指定します。URLテンプレートはNIP-19エンコードされたエンティティのプレースホルダーとして`<bech32>`を使用します。

## ユーザー推薦

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

`d`タグは推薦されているイベント種別です。複数の`a`タグで異なるプラットフォーム向けに異なるアプリを推薦できます。

## ユースケース

- 長文記事（kind 30023）を表示できるアプリの発見
- 特定のイベントタイプをサポートするクライアントの検索
- クロスクライアントの「...で開く」機能
- 暗号化サポートのためのクライアント機能の検出

---

**主要ソース:**
- [NIP-89仕様](https://github.com/nostr-protocol/nips/blob/master/89.md)

**言及箇所:**
- [ニュースレター#4: NIP詳細解説](/ja/newsletters/2026-01-07-newsletter/#nip-44-versioned-encryption)

**関連項目:**
- [NIP-19: Bech32エンコードエンティティ](/ja/topics/nip-19/)
