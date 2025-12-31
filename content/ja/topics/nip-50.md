---
title: "NIP-50: Search"
date: 2025-12-31
translationOf: /en/topics/nip-50.md
translationDate: 2025-12-31
draft: false
categories:
  - プロトコル
  - リレー
---

NIP-50は、Nostrリレーのための汎用検索機能を定義し、タグやIDによる構造化クエリを超えた全文検索をクライアントに可能にします。

## 仕組み

プロトコルはREQメッセージのフィルターオブジェクトに`search`フィールドを追加します：

1. クライアントが人間が読める検索クエリを送信（例：「最高のnostrアプリ」）
2. リレーがイベントデータ（主に`content`フィールド）に対してクエリを解釈・マッチング
3. 結果は時系列順ではなく関連性でランク付け
4. `limit`フィルターは関連性ソート後に適用

検索フィルターは`kinds`や`ids`などの他の制約と組み合わせて、より具体的なクエリを行うことができます。

## 検索拡張

リレーはオプションで以下の拡張パラメータをサポートできます：

- `include:spam` - デフォルトのスパムフィルタリングを無効化
- `domain:<domain>` - 検証済みNIP-05ドメインでフィルタリング
- `language:<code>` - ISO言語コードでフィルタリング
- `sentiment:<value>` - ネガティブ/ニュートラル/ポジティブなセンチメントでフィルタリング
- `nsfw:<true/false>` - NSFWコンテンツを含めるか除外

## クライアントの考慮事項

- クライアントは`supported_nips`フィールドを通じてリレー機能を確認すべき
- クライアント側での結果検証が推奨される
- すべてのリレーが検索を実装しているわけではない；オプション機能のまま

---

**主要ソース：**
- [NIP-50仕様](https://github.com/nostr-protocol/nips/blob/master/50.md)

**言及：**
- [ニュースレター #3：12月のまとめ](/ja/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**関連項目：**
- [NIP-11: リレー情報](/ja/topics/nip-11/)
