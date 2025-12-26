---
title: "NIP-11: リレー情報"
date: 2025-12-17
draft: false
categories:
  - Relay
  - Protocol
---

NIP-11はリレーが自身に関するメタデータを公開する方法を定義します。サポートしているNIP、制限、連絡先情報などが含まれます。

## 仕組み

クライアントは`Accept: application/nostr+json`ヘッダーを付けてリレーのWebSocket URLにHTTP GETリクエストを行うことでリレー情報を取得します。リレーは機能を記述したJSONドキュメントを返します。

## 主要フィールド

- **name** - 人間が読めるリレー名
- **description** - リレーの目的
- **supported_nips** - 実装されているNIPのリスト
- **limitation** - 最大メッセージサイズ、必要な認証などの制限
- **self** - リレー自身の公開鍵（リレーアイデンティティ用の新しいフィールド）

## ユースケース

- クライアントは接続前にリレーが必要な機能をサポートしているかチェックできる
- ディスカバリサービスがリレーの機能をインデックス化できる
- ユーザーが公開前にリレーのポリシーを確認できる

---

**主要ソース:**
- [NIP-11仕様](https://github.com/nostr-protocol/nips/blob/master/11.md)

**言及箇所:**
- [ニュースレター #1: NIP更新](/ja/newsletters/2025-12-17-newsletter/#nip-updates)

