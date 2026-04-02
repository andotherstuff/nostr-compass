---
title: "NIP-99: 分類リスティング"
date: 2026-03-11
translationOf: /en/topics/nip-99.md
translationDate: 2026-04-01
draft: false
categories:
  - NIP
  - 商取引
  - マーケットプレイス
---

NIP-99は商品、サービス、求人、レンタル、その他のオファー向けのアドレス可能な分類リスティングイベントを定義します。多くの現在のコマースクライアントが古い[NIP-15](/ja/topics/nip-15/)マーケットプレイス仕様の代わりにNIP-99で構築しているのは、よりシンプルなイベントモデルを提供するためです。

## 仕組み

アクティブなリスティングはkind `30402`を使用し、ドラフトや非アクティブなリスティングはkind `30403`を使用します。著者pubkeyが売り手またはオファー作成者です。`content`フィールドにはMarkdownで人間が読める説明が入り、タグにはタイトル、要約、価格、場所、ステータスなどの構造化フィールドが格納されます。

```json
{
  "id": "b3e392b11f5d4f28321cedd09303a748acfd0487aea5a7450b3481c60b6e4f87",
  "pubkey": "a695f6b60119d9521934a691347d9f78e8770b56da16bb255ee286ddf9fda919",
  "created_at": 1741699200,
  "kind": 30402,
  "tags": [
    ["d", "shopstr-handmade-wallet-001"],
    ["title", "Handmade leather wallet"],
    ["summary", "Brown bifold wallet with Bitcoin and Nostr branding"],
    ["published_at", "1741699200"],
    ["location", "Austin, TX"],
    ["price", "75000", "SAT"],
    ["status", "active"],
    ["t", "merch"],
    ["t", "bitcoin"]
  ],
  "content": "Full listing description in Markdown, shipping details, and contact terms.",
  "sig": "4a5c7e8f9012ab34cd56ef7890ab12cd34ef56ab78cd90ef12ab34cd56ef78900112233445566778899aabbccddeeff00112233445566778899aabbccddeeff"
}
```

イベントはアドレス可能であるため、売り手はpubkey、kind、`d`タグの同じアイデンティティタプルを維持しながらリスティングを更新できます。これにより、価格やステータスの変更のたびに新しい不変ノートを公開するよりも、クライアントにとってリスティングの改訂がクリーンになります。

## なぜ重要か

NIP-99の強みは、コアリスティングの形状を標準化しながら、異なるマーケットプレイスデザインの余地を残していることです。あるクライアントはローカル分類広告に、別のクライアントはサブスクリプションに、さらに別のクライアントはグローバル商品カタログに集中できます。すべてがイベント構造に合意すれば、売り手は一度公開するだけで、ある程度のクロスクライアント可視性を得られます。

この柔軟性は、現在のマーケットプレイスプロジェクトがNIP-99を好む理由も説明します。仕様は検索と表示をサポートするのに十分な構造を持ちながら、すべてのアプリを単一のエスクロー、配送、決済ワークフローに強制しません。

## 実装に関する注記

- `price`タグはオプションの頻度フィールドを追加することで、一回限りまたは定期的な支払いを記述できます。
- `t`タグはカテゴリまたは検索キーワードとして機能します。
- `image`タグにより、クライアントはMarkdownボディを解析せずにギャラリービューをレンダリングできます。
- マーケットプレイスがより豊富な商品コンテキストを望む場合、リスティングは`e`または`a`タグで関連イベントやドキュメントにリンクできます。

## 実装

- [Shopstr](https://github.com/shopstr-eng/shopstr) - エージェント向けMCPエンドポイントを持つNIP-99リスティングを使用したNostrマーケットプレイス
- [Milk Market](https://github.com/shopstr-eng/milk-market) - 混合支払いオプションを持つ同じリスティングレイヤー上に構築された食品マーケットプレイス

---

**主要ソース:**
- [NIP-99仕様](https://github.com/nostr-protocol/nips/blob/master/99.md)
- [Shopstr PR #234](https://github.com/shopstr-eng/shopstr/pull/234) - NIP-99リスティング上のMCPコマースエンドポイント
- [Milk Market PR #10](https://github.com/shopstr-eng/milk-market/pull/10) - マーケットプレイスリスティング上のサブスクリプションとマルチマーチャントチェックアウト

**掲載号:**
- [Newsletter #13: ShopstrとMilk MarketがMCPコマースサーフェスをオープン](/en/newsletters/2026-03-11-newsletter/#shopstr-and-milk-market-open-mcp-commerce-surfaces)

**関連項目:**
- [NIP-15: マーケットプレイスオファー](/ja/topics/nip-15/)
- [NIP-47: Nostr Wallet Connect](/ja/topics/nip-47/)
- [NIP-60: Cashuウォレット](/ja/topics/nip-60/)
