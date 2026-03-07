---
title: "MLS (Message Layer Security)"
date: 2025-12-31
translationOf: /en/topics/mls.md
translationDate: 2026-03-07
draft: false
categories:
  - 暗号技術
  - プロトコル
  - メッセージング
  - プライバシー
---

Message Layer Security (MLS) は、end-to-end encrypted group messagingのためのIETFプロトコルです。時間とともにメンバー構成が変わるグループに対して、forward secrecyとpost-compromise securityを提供します。

## 仕組み

MLSは、TreeKEMと呼ばれるツリーベースの鍵合意構造を使います。

1. **Key Packages**: 各参加者がidentityと暗号鍵を含むkey packageを公開する
2. **Group State**: ratchet treeがグループの暗号状態を維持する
3. **Commits**: 参加、離脱、鍵ローテーションのたびにメンバーがtreeを更新する
4. **Message Encryption**: shared group secretから導出した鍵でcontentを暗号化する

## 重要性

MLSは、pairwise encryptionではうまく扱えない問題を解きます。メンバーが非同期に参加、離脱、鍵ローテーションする状況でも、グループメンバーシップと暗号状態を一貫させられます。

実用上の肝はtree構造です。更新のたびに全参加者が全員とpairwiseで再交渉する必要がないため、場当たり的なグループ鍵方式よりはるかに拡張しやすくなります。

## 標準化

- **RFC 9420** (2023年7月): コアMLSプロトコル仕様
- **RFC 9750** (2025年4月): システム統合のためのMLSアーキテクチャ

## Nostrでの採用

複数のNostrアプリケーションが、セキュアなグループメッセージングのためにMLSを使っています。

- **KeyChat**: モバイルとデスクトップ向けのMLSベース暗号化メッセージングアプリ
- **White Noise**: Marmot protocol統合と組み合わせたMLSベースのprivate messaging
- **Marmot Protocol**: MLSベースのgroup encryptionを提供するNostr拡張

MLSは、特にメンバー変動が多い場合、[NIP-04](/ja/topics/nip-04/)や[NIP-44](/ja/topics/nip-44/)単独より強いグループセキュリティ保証を提供します。

## トレードオフ

MLS自体は完全なmessaging productではありません。アプリケーション側で、identity、transport、spam対策、保存、そして競合処理を補う必要があります。

だからこそ、MarmotのようなNostrプロジェクトはMLSの上に追加ルールを重ねます。暗号方式は標準化されていても、その周辺のアプリケーションプロトコルは相互運用性にとって重要です。

---

**主要ソース:**
- [RFC 9420: MLS Protocol](https://datatracker.ietf.org/doc/rfc9420/)
- [RFC 9750: MLS Architecture](https://datatracker.ietf.org/doc/rfc9750/)
- [IETF MLS Working Group](https://datatracker.ietf.org/wg/mls/about/)
- [MLS Protocol Website](https://messaginglayersecurity.rocks/)

**言及箇所:**
- [Newsletter #3: Releases](/en/newsletters/2025-12-31-newsletter/#releases)
- [Newsletter #10](/en/newsletters/2026-02-18-newsletter/)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**関連項目:**
- [Marmot Protocol](/ja/topics/marmot/)
- [MIP-05: Privacy-Preserving Push Notifications](/ja/topics/mip-05/)
- [NIP-17: Private Direct Messages](/ja/topics/nip-17/)
- [NIP-44: Encrypted Payloads](/ja/topics/nip-44/)
