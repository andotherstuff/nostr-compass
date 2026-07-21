---
title: "Gamma Markets"
date: 2026-07-15
translationOf: /en/topics/gamma-markets.md
translationDate: 2026-07-15
draft: false
categories:
  - Commerce
  - Marketplace
  - Protocol
---

Gamma Marketsは、[NIP-99](/ja/topics/nip-99/) classified listingsの上に直接構築されたe-commerce向けの取り決めのセットで、Nostrマーケットプレイス開発者のワーキンググループ、すなわちShopstr、Cypher、Plebeian Market、Conduit Marketの各チームによって共同で開発されました。NIP-99自身が未定義のまま残す、配送、order flow、コレクション、レビューの取り決めを埋めます。

## 仕組み

Gamma Marketsは、NIP-99の既存のkind `30402` listing eventの周りに、そのeventの形を変えることなく、5つのevent kindを追加します。

- **Kind 30405** - product collection。`a` tagを介して複数のlistingをまとめる
- **Kind 30406** - 配送オプション。国ごとの価格設定と、任意の重量ベースまたは距離ベースの費用ルール付き
- **Kind 16** - order message。作成(type 1)、支払いリクエスト(type 2)、ステータス更新(type 3)、配送更新(type 4)
- **Kind 14** - 一般的なbuyer/merchant間のコミュニケーション
- **Kind 17** - 支払いレシート
- **Kind 31555** - product review。特定のseller pubkeyとlistingの`d` tag宛て

merchantの支払い設定は、そのkind `0` profile metadataの`payment_preference` tagを介して宣言され、clientは[NIP-89](/ja/topics/nip-89/) application recommendationsを通じて互換アプリを発見します。order communicationは[NIP-17](/ja/topics/nip-17/) private messagesの上に構築され、独自の新しい暗号化方式を持ちません。

この仕様を特徴づける設計上の選択は、何も継承しない(cascadeしない)ことです。コレクションに属する、または配送オプションを使うlistingは、親の設定を自動的に継承する代わりに、`a` tagで明示的にそれを参照します。これは、productがstallの通貨と配送テーブルを暗黙のうちに継承していた、古い[NIP-15](/ja/topics/nip-15/) stallモデルからの意図的な離脱です。

### 例: order作成(kind 16、type 1)

```json
{
  "kind": 16,
  "content": "Please leave the package with the doorman.",
  "tags": [
    ["p", "<merchant-pubkey>"],
    ["subject", "New order"],
    ["type", "1"],
    ["order", "order-8f21"],
    ["amount", "115000"],
    ["item", "30402:<merchant-pubkey>:keyboard-mx-blue-01", "1"],
    ["shipping", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

## なぜ重要か

NIP-99単体では、listingそのもの、すなわち署名済みでaddressableなclassified adだけを標準化します。Gamma Markets以前は、NIP-99上で実際のe-commerceを構築するclientはそれぞれ、配送、checkout、レビューのための独自のprivateな取り決めを発明しており、それは2つのNIP-99準拠のclientが、それぞれ正しくlistingを描画できても、両者間でorderを完了させる共有の方法を持たないことを意味しました。Gamma Marketsは、NIP-99のlistingフォーマットそのものに触れずにその穴を埋めるため、既存のNIP-99 listingは変更なしで有効なままです。

## 実装

- [Shopstr](https://github.com/shopstr-eng/shopstr) - Nostrマーケットプレイス。仕様を執筆した4つのプロジェクトの1つ
- [Conduit Mono](https://github.com/Conduit-BTC/conduit-mono) - マーケットプレイスプロトコル。同じ設計領域で独自のorder-stateとcheckout flowを構築中

---

**Primary sources:**
- [Gamma Markets spec repository](https://github.com/GammaMarkets/market-spec)
- [NIP-99 e-commerce use case extension, PR #1784](https://github.com/nostr-protocol/nips/pull/1784) - merged link from the canonical NIP-99 document to the Gamma Markets spec

**Mentioned in:**
- [Newsletter #31: NIP Deep Dive: NIP-99 and the Gamma Markets commerce extension](/ja/newsletters/2026-07-15-newsletter/#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension)

**See also:**
- [NIP-99: Classified Listings](/ja/topics/nip-99/)
- [NIP-15: Nostr Marketplace](/ja/topics/nip-15/)
- [NIP-17: Private Direct Messages](/ja/topics/nip-17/)
