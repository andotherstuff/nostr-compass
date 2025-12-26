---
title: "NIP-69: ピアツーピア取引"
date: 2025-12-17
draft: false
categories:
  - Trading
  - Protocol
---

NIP-69はNostr上でのピアツーピア取引のためのプロトコルを定義し、分断された流動性プールではなく複数のプラットフォーム間で統一されたオーダーブックを作成します。

## イベントKind

- **Kind 38383** - P2P注文イベント

## 注文構造

注文はタグを使用して取引パラメータを指定します:

- `d` - 注文ID
- `k` - 注文タイプ（買い/売り）
- `f` - 法定通貨（ISO 4217コード）
- `amt` - satoshi単位のBitcoin金額
- `fa` - 法定通貨金額
- `pm` - 受け入れる支払い方法
- `premium` - 価格プレミアム/ディスカウントのパーセンテージ
- `network` - 決済レイヤー（onchain、lightning、liquid）
- `expiration` - 注文の有効期限

## 注文のライフサイクル

注文はステータスを通じて進行します:
- `pending` - オープンでマッチング可能
- `in-progress` - カウンターパーティとの取引が開始
- `success` - 取引完了
- `canceled` - メイカーによって撤回
- `expired` - 有効期限切れ

## セキュリティ

`bond`タグは両当事者が支払う必要があるセキュリティデポジットを指定し、放棄や詐欺からの保護を提供します。

---

**主要ソース:**
- [NIP-69仕様](https://github.com/nostr-protocol/nips/blob/master/69.md)

**言及箇所:**
- [ニュースレター #1: NIP更新](/ja/newsletters/2025-12-17-newsletter/#nip-updates)
- [ニュースレター #1: リリース](/ja/newsletters/2025-12-17-newsletter/#releases)
- [ニュースレター #2: ニュース](/ja/newsletters/2025-12-24-newsletter/#news)

