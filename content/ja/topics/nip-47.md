---
title: "NIP-47: Nostr Wallet Connect"
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
---

NIP-47はNostrアプリケーションをLightningウォレットに接続するためのプロトコルを定義し、すべてのアプリにウォレット認証情報を公開することなく支払いを可能にします。

## 仕組み

ウォレット（Zeusなど）は特定のNostrリレーで支払いリクエストをリッスンするNWCサービスを実行します。アプリはウォレットのpubkeyとリレー情報を含む接続文字列を使用して接続します。支払いリクエストと応答はアプリとウォレット間で暗号化されます。

## ユースケース

- **Zapping** - 投稿、プロフィール、コンテンツクリエイターにsatsを送信
- **支払い** - どのNostrアプリからでもLightning請求書を支払い
- **サブスクリプション** - プレミアムコンテンツへの定期的な支払い

## 主な機能

- **バジェット制御** - 接続ごとに支出制限を設定
- **カスタムリレー** - ウォレット通信に独自のリレーを使用
- **並列支払い** - バッチ操作のために複数のzapを同時に処理

---

**主要ソース:**
- [NIP-47仕様](https://github.com/nostr-protocol/nips/blob/master/47.md)

**言及箇所:**
- [ニュースレター #1: ニュース](/ja/newsletters/2025-12-17-newsletter/#news)
- [ニュースレター #2: リリース](/ja/newsletters/2025-12-24-newsletter/#releases)

**関連項目:**
- [NIP-57: Zaps](/ja/topics/nip-57/)

