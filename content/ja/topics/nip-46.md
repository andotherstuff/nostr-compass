---
title: "NIP-46: Nostr Connect"
date: 2025-12-17
draft: false
categories:
  - Signing
  - Protocol
---

NIP-46はリモート署名を定義し、署名アプリケーションが鍵を保持しながらクライアントがNostrリレー経由で署名をリクエストできるようにします。

## 仕組み

1. 署名アプリが接続URI（`bunker://`または`nostrconnect://`）を生成
2. ユーザーがURIをクライアントに貼り付け
3. クライアントが署名リクエストを暗号化されたイベントとして署名アプリのリレーに送信
4. 署名アプリがユーザーに承認を求め、署名されたイベントを返す

## 接続方法

- **bunker://** - 署名アプリが開始する接続
- **nostrconnect://** - QRコードまたはディープリンク経由でクライアントが開始する接続

## サポートされる操作

- `sign_event` - 任意のイベントに署名
- `get_public_key` - 署名アプリの公開鍵を取得
- `nip04_encrypt/decrypt` - NIP-04暗号化操作
- `nip44_encrypt/decrypt` - NIP-44暗号化操作

---

**主要ソース:**
- [NIP-46仕様](https://github.com/nostr-protocol/nips/blob/master/46.md)

**言及箇所:**
- [ニュースレター #1: 注目のコード変更](/ja/newsletters/2025-12-17-newsletter/#amethyst-android)

**関連項目:**
- [NIP-55: Android署名アプリ](/ja/topics/nip-55/)

