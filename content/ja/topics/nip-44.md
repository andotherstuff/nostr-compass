---
title: "NIP-44: Encrypted Payloads"
date: 2025-12-31
translationOf: /en/topics/nip-44.md
translationDate: 2025-12-31
draft: false
categories:
  - NIP
  - 暗号技術
  - プライバシー
---

NIP-44は、Nostrペイロードのためのバージョン管理された暗号化標準を定義し、欠陥のあるNIP-04暗号化スキームを現代的な暗号プリミティブで置き換えます。

## 仕組み

NIP-44バージョン2は、複数のステップによる暗号化プロセスを使用します：

1. **鍵合意**：送信者と受信者の公開鍵間のECDH（secp256k1）が共有シークレットを生成
2. **鍵導出**：SHA256とソルト`nip44-v2`を使用したHKDF-extractが会話キーを作成
3. **メッセージごとのキー**：HKDF-expandがランダムなnonceからChaChaキー、nonce、HMACキーを導出
4. **パディング**：メッセージの長さを隠すためにコンテンツをパディング
5. **暗号化**：ChaCha20がパディングされたコンテンツを暗号化
6. **認証**：HMAC-SHA256がメッセージの完全性を提供

## 暗号選択

- **ChaCha20**（AESより優先）：より高速で、マルチキー攻撃への耐性が優れている
- **HMAC-SHA256**（Poly1305より優先）：多項式MACは偽造されやすい
- **SHA256**：既存のNostrプリミティブと一貫性がある
- **バージョン管理形式**：将来のアルゴリズムアップグレードを可能にする

## セキュリティ特性

- **認証付き暗号化**：メッセージは改ざんできない
- **長さの隠蔽**：パディングがメッセージサイズを隠す
- **会話キー**：継続的な会話に同じキーを使用し、計算を削減
- **監査済み**：Cure53のセキュリティ監査で悪用可能な脆弱性は発見されなかった

## 制限事項

NIP-44は以下を提供しません：
- **Forward Secrecy**：侵害されたキーは過去のメッセージを露出
- **Post-Compromise Security**：キー侵害後の回復
- **否認可能性**：メッセージは特定のキーによって署名されたことが証明可能
- **メタデータ隠蔽**：リレーアーキテクチャがプライバシーを制限

高セキュリティのニーズには、NIP-104（Double Ratchet）やMarmotのようなMLSベースのプロトコルがより強力な保証を提供します。

## 歴史

NIP-44リビジョン3は、Cure53による独立したセキュリティ監査の後、2023年12月にマージされました。NIP-17プライベートDMとNIP-59 gift wrappingの暗号基盤を形成しています。

---

**主要ソース：**
- [NIP-44仕様](https://github.com/nostr-protocol/nips/blob/master/44.md)
- [NIP-44リファレンス実装](https://github.com/paulmillr/nip44)
- [Cure53監査レポート](https://cure53.de/audit-report_nip44-implementations.pdf)

**言及：**
- [ニュースレター #3：2023年12月](/ja/newsletters/2025-12-31-newsletter/#december-2023-ecosystem-maturation)
- [ニュースレター #3：2024年12月](/ja/newsletters/2025-12-31-newsletter/#december-2024-protocol-advancement)

**関連項目：**
- [NIP-04: 暗号化ダイレクトメッセージ（非推奨）](/ja/topics/nip-04/)
- [NIP-17: プライベートダイレクトメッセージ](/ja/topics/nip-17/)
- [NIP-59: ギフトラップ](/ja/topics/nip-59/)
- [NIP-104: ダブルラチェット暗号化](/ja/topics/nip-104/)
- [MLS: メッセージレイヤーセキュリティ](/ja/topics/mls/)
