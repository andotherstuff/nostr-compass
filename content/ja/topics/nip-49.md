---
title: "NIP-49: 秘密鍵暗号化"
date: 2026-03-11
translationOf: /en/topics/nip-49.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - 鍵管理
  - セキュリティ
---

NIP-49は、クライアントがユーザーの秘密鍵をパスワードで暗号化し、その結果を`ncryptsec`文字列としてエンコードする方法を定義します。目的は、生の`nsec`を保存するより強いデフォルトを保ちながら、暗号化済み鍵をクライアント間で持ち運びやすくすることです。

## 仕組み

クライアントは、hex文字列やbech32文字列ではなく、生の32-byte secp256k1秘密鍵から始めます。ユーザーのパスワードから、鍵ごとにランダムなsaltと`LOG_N`として保存される調整可能なwork factorを使って、scryptで一時的な対称鍵を導出します。その後、秘密鍵をXChaCha20-Poly1305で暗号化し、version情報と鍵の扱いに関するmetadataを前置し、`ncryptsec` prefixでbech32エンコードします。

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

上のイベントは例示用containerであり、NIP-49の必須要件ではありません。NIP-49が標準化するのは暗号化された鍵形式そのものであって、それを公開する専用イベントkindではありません。クライアントは`ncryptsec`をローカル保存したり、アプリ固有ストレージで同期したり、バックアップ文字列として提示したりできます。

## セキュリティモデル

NIP-49は2つのことを同時に行います。ユーザーパスワードを適切な暗号鍵に変換することと、メモリハードなKDFによって総当たり回復を遅くすることです。work factorは重要です。`LOG_N`が高いほど正規ユーザーの復号も遅くなりますが、攻撃者のoffline推測コストも上がります。

この形式には、暗号化前に鍵が安全でない扱いを受けたことがあるかを示す1-byte flagも含まれます。これはciphertextそのものを変えませんが、新しく安全に生成された保護バックアップと、暗号化前に平文で貼り付けられるなどした鍵をクライアントが区別する手掛かりになります。

## 実装メモ

- パスワードは鍵導出前にUnicode NFKCへ正規化されるため、クライアントやプラットフォームが違っても同じ入力で一貫して扱えます。
- XChaCha20-Poly1305は24-byte nonceと認証付き暗号を使うため、ciphertextの改ざんは復号時にきれいに失敗します。
- 対称鍵は使用後にzero化して破棄するべきです。
- 仕様は、暗号化済み鍵を公開Relayへ投稿することを推奨していません。多数の暗号文を集められるほど、攻撃者にとってoffline crackの条件が良くなるからです。

## 実装

- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - NIP-49暗号化秘密鍵を使ったsignup互換を追加

---

**主要ソース:**
- [NIP-49 Specification](https://github.com/nostr-protocol/nips/blob/master/49.md)
- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - NIP-49を使うクライアント側signupフロー

**言及箇所:**
- [Newsletter #13: Formstr](/ja/newsletters/2026-03-11-newsletter/#formstr)
- [Newsletter #13: NIP Deep Dive](/ja/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-49秘密鍵暗号化)

**関連項目:**
- [NIP-46: Nostr Connect](/ja/topics/nip-46/)
- [NIP-55: Android署名アプリケーション](/ja/topics/nip-55/)

