---
title: "NIP-99: 分類型リスティング"
date: 2026-03-11
translationOf: /en/topics/nip-99.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - コマース
  - マーケットプレイス
---

NIP-99は、商品、サービス、求人、賃貸、その他のoffer向けの、アドレス可能なclassified-listingイベントを定義します。古い[NIP-15](/ja/topics/nip-15/)のマーケットプレイス仕様より単純なイベントモデルを提供するため、現在の多くのコマース系クライアントはNIP-99を基盤にしています。

## 仕組み

有効なlistingにはkind `30402`を使い、draftやinactive listingにはkind `30403`を使います。著者pubkeyはsellerまたはoffer作成者です。`content`フィールドには人間が読めるMarkdown説明が入り、tagにはtitle、summary、price、location、statusなどの構造化フィールドが入ります。

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

このイベントはアドレス可能なので、sellerはpubkey、kind、`d`タグという同じidentity tupleを保ったままlistingを更新できます。価格やstatusが変わるたびにまったく新しい不変noteを出すより、クライアントにとってlisting改訂を扱いやすくします。

## なぜ重要か

NIP-99の強みは、コアとなるlisting形状を標準化しつつ、異なるマーケットプレイス設計の余地を残していることです。あるクライアントはローカル掲示板に集中し、別のクライアントはsubscriptionに集中し、さらに別のクライアントはグローバルな商品カタログに集中できます。イベント構造に合意していれば、sellerは1度公開するだけで、クライアントをまたいだ可視性をある程度得られます。

この柔軟性こそが、現在のマーケットプレイス系プロジェクトがNIP-99を好む理由でもあります。仕様は検索と表示を支えるのに十分な構造を持ちながら、エスクロー、配送、支払いフローをすべてのアプリに強制しません。

## 実装メモ

- `price`タグは、任意のfrequency fieldを追加することで単発支払いと定期支払いの両方を記述できます。
- `t`タグはカテゴリや検索キーワードとして機能します。
- `image`タグを使えば、クライアントはMarkdown本文を解析せずにgallery viewを描画できます。
- richerな商品文脈が必要なマーケットプレイスでは、listingから`e`タグや`a`タグで関連イベントや文書へリンクできます。

## 実装

- [Shopstr](https://github.com/shopstr-eng/shopstr) - agent向けMCP endpoint付きでNIP-99 listingを使うNostrマーケットプレイス
- [Milk Market](https://github.com/shopstr-eng/milk-market) - 同じlisting layer上に構築され、複数支払い方式を扱うfood marketplace

---

**主要ソース:**
- [NIP-99 Specification](https://github.com/nostr-protocol/nips/blob/master/99.md)
- [Shopstr PR #234](https://github.com/shopstr-eng/shopstr/pull/234) - NIP-99 listing上のMCP commerce endpoint
- [Milk Market PR #10](https://github.com/shopstr-eng/milk-market/pull/10) - marketplace listing上のsubscriptionとmulti-merchant checkout

**言及箇所:**
- [Newsletter #13: Shopstr and Milk Market Open MCP Commerce Surfaces](/ja/newsletters/2026-03-11-newsletter/)

**関連項目:**
- [NIP-15: Marketplace Offers](/ja/topics/nip-15/)
- [NIP-47: Nostr Wallet Connect](/ja/topics/nip-47/)
- [NIP-60: Cashuウォレット](/ja/topics/nip-60/)

