---
title: "MLS (Message Layer Security)"
date: 2025-12-31
translationOf: /en/topics/mls.md
translationDate: 2025-12-31
draft: false
categories:
  - 暗号技術
  - プロトコル
  - メッセージング
  - プライバシー
---

Message Layer Security (MLS) は、エンドツーエンド暗号化グループメッセージング用のIETF標準化プロトコルです。2人から数千人の参加者までのグループに対して、前方秘匿性と侵害後の安全性を備えた効率的な鍵確立を提供します。

## 仕組み

MLSはTreeKEMと呼ばれるツリーベースの鍵合意構造を使用します：

1. **鍵パッケージ**: 各参加者がアイデンティティと暗号化鍵を含む鍵パッケージを公開
2. **グループ状態**: ラチェットツリーがグループの暗号状態を維持
3. **コミット**: メンバーが参加、退出、または鍵のローテーション時にツリーを更新
4. **メッセージ暗号化**: コンテンツはグループ共有シークレットから派生した鍵で暗号化

## 主要なセキュリティ特性

- **前方秘匿性**: 現在の鍵が漏洩しても過去のメッセージは安全なまま
- **侵害後の安全性**: 鍵ローテーション後、将来のメッセージは再び安全に
- **メンバー認証**: すべてのグループメンバーが暗号学的に検証される
- **非同期動作**: すべての参加者がオンラインでなくてもメンバーは参加/退出可能
- **スケーラビリティ**: 最大50,000人の参加者のグループに対して効率的

## 標準化

- **RFC 9420**（2023年7月）：コアMLSプロトコル仕様
- **RFC 9750**（2025年4月）：システム統合のためのMLSアーキテクチャ

## Nostrでの採用

複数のNostrアプリケーションがセキュアなグループメッセージングにMLSを使用しています：

- **KeyChat**: モバイルとデスクトップ向けのMLSベースの暗号化メッセージングアプリ
- **White Noise**: Marmotプロトコル統合によるMLSを使用したプライベートメッセージング
- **Marmot Protocol**: MLSベースのグループ暗号化を提供するNostr拡張

MLSは、メンバーが動的に参加・退出するグループチャットにおいて、NIP-04やNIP-44単独よりも強力なセキュリティ保証を提供します。

## 業界での採用

Nostr以外でも、MLSは以下で採用されています：
- Google Messages（GSMA Universal Profile 3.0経由のMLSを使用したRCS）
- Apple Messages（MLSのRCSサポートを発表）
- Cisco WebEx、Wickr、Matrix

---

**主要な情報源:**
- [RFC 9420: MLS Protocol](https://datatracker.ietf.org/doc/rfc9420/)
- [RFC 9750: MLS Architecture](https://datatracker.ietf.org/doc/rfc9750/)
- [IETF MLS Working Group](https://datatracker.ietf.org/wg/mls/about/)
- [MLS Protocol Website](https://messaginglayersecurity.rocks/)

**関連記事:**
- [Newsletter #3: リリース](/ja/newsletters/2025-12-31-newsletter/#releases)

**関連項目:**
- [Marmot Protocol](/ja/topics/marmot/)
- [MIP-05: プライバシー保護プッシュ通知](/ja/topics/mip-05/)
- [NIP-17: プライベートダイレクトメッセージ](/ja/topics/nip-17/)
- [NIP-44: 暗号化ペイロード](/ja/topics/nip-44/)
