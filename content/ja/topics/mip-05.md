---
title: "MIP-05: プライバシー保護プッシュ通知"
url: /ja/topics/mip-05/
translationOf: /en/topics/mip-05.md
translationDate: 2025-12-26
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Messaging
  - Protocol
---

MIP-05は、ユーザーのプライバシーを維持するプッシュ通知プロトコルを定義し、従来のプッシュシステムがサーバーにデバイストークンとユーザーIDを知らせる必要がある問題を解決します。

## 仕組み

- デバイストークンはECDH+HKDFとChaCha20-Poly1305で暗号化
- エフェメラル鍵が通知間の相関を防止
- 3イベントゴシッププロトコル（kind 447-449）が暗号化トークンをグループメンバー間で同期
- NIP-59 gift wrappingによるデコイトークンがグループサイズを隠蔽

## プライバシー保証

- プッシュ通知サーバーはユーザーを識別できない
- グループメンバーシップは通知パターンから露出しない
- デバイストークンはメッセージ間で相関付けできない

## イベントKind

- **Kind 447**: 暗号化デバイストークンの公開
- **Kind 448**: トークン同期リクエスト
- **Kind 449**: トークン同期レスポンス

---

**主要ソース:**
- [MIP-05 PR](https://github.com/marmot-protocol/marmot/pull/18)

**言及箇所:**
- [ニュースレター #1: ニュース](/ja/newsletters/2025-12-17-newsletter/#news)

**関連項目:**
- [Marmotプロトコル](/ja/topics/marmot/)
- [NIP-59: Gift Wrap](/ja/topics/nip-59/)
