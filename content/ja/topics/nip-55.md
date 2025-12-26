---
title: "NIP-55: Android署名アプリケーション"
date: 2025-12-17
draft: false
categories:
  - Signing
  - Mobile
---

NIP-55はAndroidアプリケーションが専用の署名アプリから署名操作をリクエストする方法を定義し、ユーザーが複数のNostrクライアントを使用しながら秘密鍵を1つの安全な場所に保持できるようにします。

## 仕組み

NIP-55はAndroidのコンテンツプロバイダーインターフェースを使用して署名操作を公開します。署名アプリはコンテンツプロバイダーとして登録し、他のNostrアプリは秘密鍵に直接アクセスすることなく署名をリクエストできます。

フロー:
1. クライアントアプリが署名アプリのコンテンツプロバイダーを呼び出す
2. 署名アプリがユーザーに承認UIを表示
3. ユーザーがリクエストを承認または拒否
4. 署名アプリが署名（または拒否）をクライアントに返す

## 主要な操作

- **get_public_key** - ユーザーの公開鍵を取得（初期接続時に1回呼び出す）
- **sign_event** - Nostrイベントに署名
- **nip04_encrypt/decrypt** - NIP-04メッセージの暗号化または復号化
- **nip44_encrypt/decrypt** - NIP-44メッセージの暗号化または復号化

## 接続の開始

一般的な実装ミスはバックグラウンドプロセスから`get_public_key`を繰り返し呼び出すことです。仕様では初期接続セットアップ時に1回だけ呼び出し、結果をキャッシュすることを推奨しています。

---

**主要ソース:**
- [NIP-55仕様](https://github.com/nostr-protocol/nips/blob/master/55.md)

**言及箇所:**
- [ニュースレター #1: リリース](/ja/newsletters/2025-12-17-newsletter/#releases)
- [ニュースレター #2: ニュース](/ja/newsletters/2025-12-24-newsletter/#news)
- [ニュースレター #2: NIP更新](/ja/newsletters/2025-12-24-newsletter/#nip-updates)

**関連項目:**
- [NIP-46: Nostr Connect](/ja/topics/nip-46/)

