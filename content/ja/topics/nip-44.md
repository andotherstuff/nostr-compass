---
title: "NIP-44: Encrypted Payloads"
date: 2025-12-31
translationOf: /en/topics/nip-44.md
translationDate: 2026-04-22
draft: false
categories:
  - NIP
  - Cryptography
  - Privacy
---

NIP-44は、Nostr payload向けのversioned encryption標準を定義し、欠陥のあったNIP-04暗号方式を現代的な暗号primitiveで置き換えます。

## 仕組み

NIP-44 version 2は、多段階の暗号化プロセスを使います。

1. **Key Agreement**: 送信者と受信者の公開鍵間でECDH（secp256k1）を行い、shared secretを得る
2. **Key Derivation**: SHA256とsalt `nip44-v2`を使うHKDF-extractでconversation keyを作る
3. **Per-Message Keys**: ランダムnonceからHKDF-expandでChaCha key、nonce、HMAC keyを導出する
4. **Padding**: message長を隠すためにcontentへpaddingを入れる
5. **Encryption**: ChaCha20でpadding後のcontentを暗号化する
6. **Authentication**: HMAC-SHA256でmessage integrityを与える

出力はversion付きのbase64 payloadで、通常の署名付きNostrイベント内へ入ります。仕様は、clientが内側のNIP-44 payloadを復号する前に、外側のNIP-01イベント署名を検証することを求めています。

## 暗号設計の選択

- **AESよりChaCha20**: より高速で、multi-key attack耐性も高い
- **Poly1305よりHMAC-SHA256**: polynomial MACは偽造しやすい
- **SHA256**: 既存のNostr primitiveと一貫している
- **Versioned Format**: 将来のalgorithm更新を可能にする

## セキュリティ特性

- **Authenticated Encryption**: メッセージの改ざんを防ぐ
- **Length Hiding**: paddingでメッセージ長を隠す
- **Conversation Keys**: 継続する会話で同じkeyを使い、計算量を下げる
- **Audited**: Cure53のsecurity auditで悪用可能な脆弱性は見つからなかった

## 実装メモ

NIP-44は、NIP-04 payloadの単純な置き換えではありません。これは暗号化形式を定義するもので、direct-message event kind自体を定義するものではありません。実際のメッセージフローでこの暗号payloadをどう使うかは、[NIP-17](/ja/topics/nip-17/)や[NIP-59](/ja/topics/nip-59/)のような上位仕様が定義します。

plaintext入力はUTF-8テキストで、長さは1から65535バイトです。これは実装者にとって現実的な制約です。任意のbinary blobを暗号化したい場合は、追加のencodingか別のcontainer formatが必要になります。

## 制限

NIP-44は次のものを提供しません。
- **Forward Secrecy**: 鍵が侵害されると過去メッセージが露出する
- **Post-Compromise Security**: 鍵侵害後の回復性
- **Deniability**: 特定の鍵が署名したことを否認できる性質
- **Metadata Hiding**: relay architectureがprivacyを制限する

高いセキュリティ要件がある場合は、NIP-104（double ratchet）やMarmotのようなMLSベースのプロトコルのほうが強い保証を与えます。

## 履歴

NIP-44 revision 3は、独立したCure53 security auditの後、2023年12月にマージされました。これはNIP-17 private DMsとNIP-59 gift wrappingの暗号基盤になっています。

---

**Primary sources:**
- [NIP-44 Specification](https://github.com/nostr-protocol/nips/blob/master/44.md)
- [NIP-44 Reference Implementations](https://github.com/paulmillr/nip44)
- [Cure53 Audit Report](https://cure53.de/audit-report_nip44-implementations.pdf)

**Mentioned in:**
- [Newsletter #4: NIP Deep Dive](/ja/newsletters/2026-01-07-newsletter/)
- [Newsletter #3: December 2023](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #3: December 2024](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #12: Marmot](/ja/newsletters/2026-03-04-newsletter/)
- [Newsletter #13: Vector](/en/newsletters/2026-03-11-newsletter/)
- [Newsletter #19: nostter NIP-44 migration](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: nowhere encrypts Nostr traffic](/en/newsletters/2026-04-22-newsletter/)

**See also:**
- [NIP-04: Encrypted Direct Messages (deprecated)](/ja/topics/nip-04/)
- [NIP-17: Private Direct Messages](/ja/topics/nip-17/)
- [NIP-59: Gift Wrap](/ja/topics/nip-59/)
- [NIP-104: Double Ratchet Encryption](/ja/topics/nip-104/)
- [MLS: Message Layer Security](/ja/topics/mls/)
