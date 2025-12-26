---
title: "NIP-BE: Bluetooth Low Energy"
url: /ja/topics/nip-be/
translationOf: /en/topics/nip-be.md
translationDate: 2025-12-26
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Connectivity
---

NIP-BEは、NostrアプリケーションがBluetooth Low Energy経由で通信・同期する方法を規定し、オフライン対応アプリがインターネット接続なしで近くのデバイス間でデータを同期できるようにします。

## GATT構造

Nordic UART Serviceを使用し、2つのキャラクタリスティックを持ちます:
- **Writeキャラクタリスティック** - クライアントがサーバーにデータを送信
- **Readキャラクタリスティック** - サーバーがクライアントにデータを送信（通知経由）

## メッセージフレーミング

BLEはペイロード制限が小さい（バージョンにより20〜256バイト）ため、メッセージは:
- DEFLATEで圧縮
- 2バイトのインデックスと最終バッチフラグを持つチャンクに分割
- 最大64KBのサイズ制限

## ロールネゴシエーション

デバイスは発見時にアドバタイズされたUUIDを比較:
- 高いUUIDがGATTサーバー（リレーロール）になる
- 低いUUIDがGATTクライアントになる
- 単一ロールデバイス用の事前定義UUIDが存在

## 同期

標準的なNostrメッセージタイプ（`EVENT`、`EOSE`、`NEG-MSG`）を使用した半二重通信で、断続的な接続間でデータ同期を調整します。

## ユースケース

- 近くのデバイス間でのオフラインイベント同期
- インターネットなしでのメッシュ型メッセージ伝播
- ネットワーク利用不可時のバックアップ接続

---

**主要ソース:**
- [NIP-BE仕様](https://github.com/nostr-protocol/nips/blob/master/BE.md)

**言及箇所:**
- [ニュースレター #1: ニュース](/ja/newsletters/2025-12-17-newsletter/#news)
