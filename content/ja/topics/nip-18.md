---
title: "NIP-18: リポスト"
date: 2025-12-17
draft: false
categories:
  - Social
  - Protocol
---

NIP-18は他のプラットフォームでのリツイートに似た、イベントをリポストする方法を定義します。

## 構造

リポストはkind 6イベント（kind 1ノート用）またはkind 16（汎用リポスト）で、以下を含みます:
- リポストされたイベントを参照する`e`タグ
- 元の作成者を参照する`p`タグ
- オプションで、`content`フィールドに完全な元のイベント

## 最近の変更

`a`タグサポートにより置換可能イベントのリポストのサポートが改善されました。これにより、アドレス指定可能イベント（kind 30000-39999）のリポストが特定のイベントIDではなくアドレスで参照できます。

---

**主要ソース:**
- [NIP-18仕様](https://github.com/nostr-protocol/nips/blob/master/18.md)

**言及箇所:**
- [ニュースレター #1: NIP更新](/ja/newsletters/2025-12-17-newsletter/#nip-updates)

**関連項目:**
- [NIP-01: 基本プロトコル](/ja/topics/nip-01/)

