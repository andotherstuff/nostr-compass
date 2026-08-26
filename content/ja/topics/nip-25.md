---
title: "NIP-25: リアクション"
date: 2026-07-29
translationOf: /en/topics/nip-25.md
translationDate: 2026-08-26
draft: false
categories:
  - Protocol
  - Social
---

NIP-25はリアクションをkind `7`イベントとして定義します。ノート、記事、classified listing、その他の参照されたイベントに絵文字や短いリアクションを付けるための共通のイベント形式をクライアントに与えます。

## 仕組み

リアクションイベントはリアクションのテキストを`content`に持ち、対象イベントの`e` tagで対象を参照します。対象がaddressableな場合、リアクションはその`a` tagも含みます。さらに参照先イベントの作成者への`p` tagも含むため、relayとクライアントはイベントの内容から受信者を推測せずに通知を配送できます。

既定のリアクションは`+`なので、クライアントは空のリアクションcontentを肯定的な反応として扱えます。他の絵文字も有効なリアクション値です。仕様は否定的なリアクションのための`-`も許しており、これは当初の導入後、2022年7月の追記で加えられました。

クライアントはリアクションを作成するとき、対象への参照と作成者のtagを保持すべきです。リアクションは通常の署名済みイベントなので、普通のrelay subscriptionを通って流れ、kind `7`を認識する任意のクライアントで描画できます。

## 実装

NIP-25は、ノートに対する通常の操作の一部としてNostrのクライアントとライブラリに広く実装されています。kindとtagという単純なモデルにより、クライアントは別のトランスポートprotocolなしに件数、個々のリアクション、通知を表示できます。

---

**主要ソース:**

- [NIP-25 Specification](https://github.com/nostr-protocol/nips/blob/master/25.md)
- [導入コミット](https://github.com/nostr-protocol/nips/commit/dcbd504639d20d1b0ae6bb837609710645781b88)
- [ダウンボートの追記](https://github.com/nostr-protocol/nips/commit/89bb08ba8683)

**言及箇所:**

- [ニュースレター #33: Nostr の 6 年間の 7 月](/ja/newsletters/2026-07-29-newsletter/#nostr-の-6-年間の-7-月)
- [ニュースレター #37: Marmot](/ja/newsletters/2026-08-26-newsletter/#marmot)

**関連項目:**
- [NIP-01: Basic Protocol](/ja/topics/nip-01/)
- [NIP-10: Text Note Threading](/ja/topics/nip-10/)
