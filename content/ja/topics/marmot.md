---
title: "Marmotプロトコル"
url: /ja/topics/marmot/
translationOf: /en/topics/marmot.md
translationDate: 2025-12-26
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---

Marmotは、Nostr上に構築されたエンドツーエンド暗号化グループメッセージングプロトコルで、前方秘匿性と侵害後セキュリティのためにMessage Layer Security（MLS）標準を使用します。

## 仕組み

MarmotはMLSベースの暗号化でNostrをグループチャット向けに拡張します。一対一のNIP-17 DMとは異なり、Marmotは暗号化の保証を維持しながらメンバーが参加・離脱できるセキュアなグループ通信を処理します。

## 主な機能

- MLSによる前方秘匿性と侵害後セキュリティ
- 動的なメンバーシップのためのグループ鍵管理
- MIP-05によるプライバシー保護プッシュ通知

---

**主要ソース:**
- [Marmotプロトコルリポジトリ](https://github.com/marmot-protocol/marmot)

**言及箇所:**
- [ニュースレター #1: ニュース](/ja/newsletters/2025-12-17-newsletter/#news)
- [ニュースレター #1: リリース](/ja/newsletters/2025-12-17-newsletter/#releases)

**関連項目:**
- [MIP-05: プライバシー保護プッシュ通知](/ja/topics/mip-05/)
- [NIP-17: プライベートダイレクトメッセージ](/ja/topics/nip-17/)
- [NIP-59: Gift Wrap](/ja/topics/nip-59/)
