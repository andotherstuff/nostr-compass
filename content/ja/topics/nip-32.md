---
title: "NIP-32: ラベリング"
date: 2026-01-21
translationOf: /en/topics/nip-32.md
translationDate: 2026-03-07
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-32は、Nostrイベント、ユーザー、その他のエンティティにラベルを付けるための標準を定義します。ラベルは、クライアントがカテゴリ分け、コンテンツ警告、評価システム、モデレーションに使用できる構造化されたメタデータを提供します。

## 仕組み

ラベルはkind 1985イベントを使用し、ラベル名前空間を定義する`L`タグと、その名前空間内の特定のラベルを適用する`l`タグを持ちます。ラベル付けされたエンティティは、`e`（イベント）、`p`（pubkey）、`r`（リレーURL）などの標準タグを通じて参照されます。

```json
{
  "kind": 1985,
  "tags": [
    ["L", "content-warning"],
    ["l", "nsfw", "content-warning"],
    ["e", "<event_id>"]
  ],
  "content": "Contains explicit imagery"
}
```

名前空間システムはラベルの衝突を防ぎます。「ugc-moderation」名前空間の「spam」ラベルは、「relay-report」名前空間の「spam」とは異なるセマンティクスを持ちます。これにより、複数のラベルシステムが干渉なく共存できます。

## なぜ重要か

設計上の重要点は、ラベルが事実ではなく主張だということです。kind 1985 eventは、あるactorがあるnamespaceで何かにラベルを付けたことを示すだけです。どのラベルを表示し、隠し、無視するかは、クライアント側がtrust policyを持って判断する必要があります。

そのためNIP-32はmoderation以外にも使えます。同じ構造でcontent warning、verification marker、分類体系、relay reputation dataを運べます。しかも、すべてのクライアントを1つのグローバル語彙に縛りません。

## 利用例

コンテンツモデレーションシステムはラベルを使用してスパム、違法コンテンツ、またはポリシー違反をマークします。評価システムは信頼スコアや検証ステータスをpubkeyに付与します。メディアプラットフォームはコンテンツ警告（NSFW、暴力、ネタバレ）を適用します。リレーオペレーターは異議申し立てや紛争解決にラベルを使用します。

Trusted Relay Assertions提案はリレーの異議申し立てにNIP-32ラベルを使用します。オペレーターが信頼スコアに異議を唱える場合、`L` = `relay-appeal`と「spam」、「censorship」、「score」などのラベルタイプを持つkind 1985イベントを公開します。

## 相互運用メモ

クライアントごとにラベルの取り込み方は異なります。フォロー中ユーザーのラベルを推薦として扱うものもあれば、専用のlabeling serviceを問い合わせるものもあります。分散型の設計により、どのlabelerを信頼するかはユーザーが選べますが、信頼文脈が見えないラベルは誤解を招くこともあります。

---

**主要ソース:**
- [NIP-32仕様](https://github.com/nostr-protocol/nips/blob/master/32.md) - ラベリング標準

**言及箇所:**
- [ニュースレター #6: NIP更新](/ja/newsletters/2026-01-21-newsletter/#nip-updates)

**関連項目:**
- [Trusted Relay Assertions](/ja/topics/trusted-relay-assertions/)
- [NIP-51: リスト](/ja/topics/nip-51/)
