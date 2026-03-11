---
title: "NIP-44: 暗号化ペイロード"
date: 2025-12-31
translationOf: /en/topics/nip-44.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - 暗号
  - プライバシー
---

NIP-44は、Nostrペイロード向けのバージョン付き暗号化標準を定義し、欠陥のあるNIP-04暗号化方式を現代的な暗号プリミティブで置き換えます。

## 仕組み

NIP-44 version 2は、多段階の暗号化手順を使います。

1. **鍵共有**: 送信者と受信者の公開鍵間のECDH（secp256k1）で共有秘密を生成
2. **鍵導出**: SHA256とsalt `nip44-v2`を使うHKDF-extractでconversation keyを生成
3. **メッセージごとの鍵**: ランダムnonceからHKDF-expandでChaCha key、nonce、HMAC keyを導出
4. **パディング**: contentをpaddingしてメッセージ長を隠す
5. **暗号化**: padding済みcontentをChaCha20で暗号化
6. **認証**: HMAC-SHA256でメッセージ完全性を提供

出力はバージョン付きbase64ペイロードとなり、通常の署名済みNostrイベントの中に入ります。仕様は、クライアントが内側のNIP-44ペイロードを復号する前に、外側のNIP-01イベント署名を検証することを要求します。

## 暗号方式の選択

- **AESではなくChaCha20**: 高速で、多鍵攻撃への耐性も高い
- **Poly1305ではなくHMAC-SHA256**: 多項式MACは偽造しやすい
- **SHA256**: 既存のNostrプリミティブとの整合性がある
- **バージョン付き形式**: 将来のアルゴリズム更新を可能にする

## セキュリティ特性

- **認証付き暗号化**: メッセージ改ざんを防ぐ
- **長さの秘匿**: paddingでメッセージ長を曖昧にする
- **会話鍵**: 継続する会話で同じ鍵を使い、計算量を減らす
- **監査済み**: Cure53のセキュリティ監査で悪用可能な脆弱性は見つからなかった

## 実装メモ

NIP-44はNIP-04ペイロードの単純な置き換えではありません。これは暗号化形式を定義するものであり、ダイレクトメッセージ用のイベントkindそのものを定義するわけではありません。[NIP-17](/ja/topics/nip-17/)や[NIP-59](/ja/topics/nip-59/)のようなプロトコルが、実際のメッセージフローでNIP-44暗号化ペイロードをどう使うかを定義します。

平文入力は1から65535 byteまでのUTF-8テキストです。これは実装者にとって実際の制約です。任意のバイナリblobを暗号化したいアプリケーションでは、追加のエンコードか別のcontainer formatが必要になります。

## 制限

NIP-44は次を提供しません。
- **前方秘匿性**: 鍵が漏れると過去のメッセージも露出する
- **侵害後安全性**: 鍵侵害後に安全性を回復する仕組み
- **否認可能性**: メッセージが特定鍵で署名されたことを否定できない
- **メタデータ秘匿**: Relayアーキテクチャの制約でプライバシーは限定される

高い安全性が必要なら、NIP-104（double ratchet）やMarmotのようなMLSベースのプロトコルの方が強い保証を提供します。

## 履歴

NIP-44 revision 3は、独立したCure53セキュリティ監査の後、2023年12月にマージされました。これはNIP-17プライベートDMとNIP-59 gift wrappingの暗号基盤になっています。

---

**主要ソース:**
- [NIP-44 Specification](https://github.com/nostr-protocol/nips/blob/master/44.md)
- [NIP-44 Reference Implementations](https://github.com/paulmillr/nip44)
- [Cure53 Audit Report](https://cure53.de/audit-report_nip44-implementations.pdf)

**言及箇所:**
- [Newsletter #4: NIP Deep Dive](/ja/newsletters/2026-01-07-newsletter/)
- [Newsletter #3: December 2023](/ja/newsletters/2025-12-31-newsletter/)
- [Newsletter #3: December 2024](/ja/newsletters/2025-12-31-newsletter/)
- [Newsletter #12: Marmot](/ja/newsletters/2026-03-04-newsletter/)
- [Newsletter #13: Vector](/ja/newsletters/2026-03-11-newsletter/)

**関連項目:**
- [NIP-04: Encrypted Direct Messages (deprecated)](/ja/topics/nip-04/)
- [NIP-17: プライベートダイレクトメッセージ](/ja/topics/nip-17/)
- [NIP-59: Gift Wrap](/ja/topics/nip-59/)
- [NIP-104: Double Ratchet Encryption](/ja/topics/nip-104/)
- [MLS: Message Layer Security](/ja/topics/mls/)

