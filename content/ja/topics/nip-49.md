---
title: "NIP-49: 秘密鍵暗号化"
date: 2026-03-11
translationOf: /en/topics/nip-49.md
translationDate: 2026-04-01
draft: false
categories:
  - NIP
  - 鍵管理
  - セキュリティ
---

NIP-49はクライアントがユーザーの秘密鍵をパスワードで暗号化し、その結果を`ncryptsec`文字列としてエンコードする方法を定義します。目標は生の`nsec`を保存するよりも強力なデフォルトを持ちながら、暗号化された鍵をクライアント間で容易に移動できるポータビリティです。

## 仕組み

クライアントは生の32バイトsecp256k1秘密鍵（16進数やbech32文字列ではなく）から開始します。ユーザーのパスワードからscryptを使用して一時的な対称鍵を導出し、鍵ごとのランダムなソルトと`LOG_N`として保存される調整可能なワークファクターを使用します。次にXChaCha20-Poly1305で秘密鍵を暗号化し、バージョニングと鍵処理メタデータを先頭に追加し、`ncryptsec`プレフィックスでbech32エンコードします。

```json
{
  "id": "4d47f4f0a6f6edbc1bbd7f4e2a45ec68f27cba91d6c6ab5cf28d8d87b0f3d57e",
  "pubkey": "1f8b4c3e7b0f9451d4f9b8a7c6e5d4c3b2a1908f7e6d5c4b3a29181716151413",
  "created_at": 1741699200,
  "kind": 30078,
  "tags": [
    ["d", "encrypted-key-backup"],
    ["format", "ncryptsec"],
    ["encryption", "nip49"]
  ],
  "content": "ncryptsec1qgg9947rlpvqu76pj5ecreduf9jxhselq2nae2kghhvd5g7dgjtcxfqtd67p9m0w57lspw8gsq6yphnm8623nsl8xn9j4jdzz84zm3frztj3z7s35vpzmqf6ksu8r89qk5z2zxfmu5gv8th8wclt0h4p",
  "sig": "6a8f6e4b2d1901735f0ad4b6e8c1f3a579d0e2b4c6f8a1d3e5f7091b2c3d4e5f11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

上記のイベントはコンテナの例であり、NIP-49の要件ではありません。NIP-49は暗号化された鍵のフォーマット自体を標準化しており、それを公開するための専用イベントkindではありません。クライアントは`ncryptsec`をローカルに保存したり、アプリ固有のストレージで同期したり、バックアップエクスポートとして提示したりできます。

## セキュリティモデル

NIP-49は2つのことを同時に行います。ユーザーパスワードを適切な暗号化鍵に変換し、メモリハードなKDFでブルートフォース回復の試みを遅延させます。ワークファクターが重要です。`LOG_N`の値が高いほど正規ユーザーの復号化は遅くなりますが、攻撃者のオフライン推測コストも引き上げます。

このフォーマットには、暗号化前に鍵が安全でない方法で扱われたことがあるかどうかを記述する1バイトフラグも含まれています。これは暗号文自体を変更しませんが、新たに生成された保護バックアップと、ラップされる前に平文で貼り付けられていた鍵を区別する方法をクライアントに提供します。

## 実装に関する注記

- パスワードは鍵導出前にUnicode NFKCに正規化され、クライアント間で一貫してパスワードを入力できます。
- XChaCha20-Poly1305は24バイトのnonceと認証付き暗号化を使用するため、暗号文の改ざんは復号化時にクリーンに失敗します。
- 対称鍵は使用後にゼロクリアして破棄すべきです。
- 仕様は暗号化された鍵をパブリックrelayに投稿することを推奨していません。多くの暗号化鍵を収集すると攻撃者のオフラインクラッキングポジションが改善されるためです。

## 実装

- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - NIP-49暗号化秘密鍵を使用したサインアップ互換性の追加

---

**主要ソース:**
- [NIP-49仕様](https://github.com/nostr-protocol/nips/blob/master/49.md)
- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - NIP-49を使用したクライアントサイドサインアップフロー

**掲載号:**
- [Newsletter #13: Formstr](/en/newsletters/2026-03-11-newsletter/#formstr)
- [Newsletter #13: NIPディープダイブ](/en/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-49-private-key-encryption)

**関連項目:**
- [NIP-46: Nostr Connect](/ja/topics/nip-46/)
- [NIP-55: Android署名アプリケーション](/ja/topics/nip-55/)
