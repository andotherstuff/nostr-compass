---
title: "NIP-07: ブラウザ拡張署名"
date: 2026-01-28
translationOf: /en/topics/nip-07.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Signing
  - Security
---

NIP-07は、ブラウザ拡張機能がWebベースのNostrクライアントに署名機能を提供するための標準インターフェースを定義し、秘密鍵をWebサイトに公開するのではなく、拡張機能内で安全に保持します。

## 仕組み

ブラウザ拡張機能はWebアプリが使用できる`window.nostr`オブジェクトを注入します：

```javascript
// 公開鍵を取得
const pubkey = await window.nostr.getPublicKey();

// イベントに署名
const signedEvent = await window.nostr.signEvent(unsignedEvent);

// 暗号化（NIP-04、レガシー）
const ciphertext = await window.nostr.nip04.encrypt(pubkey, plaintext);

// 復号化（NIP-04、レガシー）
const plaintext = await window.nostr.nip04.decrypt(pubkey, ciphertext);

// NIP-44メソッド（モダン、サポートされている場合）
// const ciphertext = await window.nostr.nip44.encrypt(pubkey, plaintext);
// const plaintext = await window.nostr.nip44.decrypt(pubkey, ciphertext);
```

## セキュリティモデル

- **鍵の分離**：秘密鍵は拡張機能から外に出ることはない
- **ユーザー承認**：拡張機能は各署名リクエストに対してプロンプトを表示できる
- **ドメイン制御**：拡張機能はどのサイトが署名をリクエストできるかを制限できる

## 実装

人気のあるNIP-07拡張機能には以下が含まれます：
- **Alby** - Nostr署名機能を持つLightningウォレット
- **nos2x** - 軽量なNostr署名者
- **Flamingo** - 機能豊富なNostr拡張機能

## 制限

- ブラウザのみ（モバイルサポートなし）
- 拡張機能のインストールが必要
- 各拡張機能で承認のUXが異なる

## 代替手段

- [NIP-46](/ja/topics/nip-46/) - Nostrリレーを介したリモート署名
- [NIP-55](/ja/topics/nip-55/) - Androidローカル署名者

## 関連

- [NIP-44](/ja/topics/nip-44/) - モダンな暗号化（NIP-04の置き換え）
- [NIP-46](/ja/topics/nip-46/) - リモート署名
