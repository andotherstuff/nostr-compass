---
title: "NIP-38: ユーザーステータス"
date: 2026-08-26
translationOf: /en/topics/nip-38.md
translationDate: 2026-08-26
draft: false
description: "一般ステータスと音楽ステータスのカテゴリを含む、短命のユーザーステータスイベントを定義します。"
---

NIP-38は短いユーザーステータスのためにkind 30315のaddressableイベントを定義します。`d` tagは`general`や`music`のようなステータスのカテゴリを示し、任意の`r`および`p` tagはURLへのリンクやアーティストの指定に使えます。クライアントはイベントの`expiration` tagを使って古いステータスの表示をやめられます。

## 仕組み

ユーザーはステータスの本文を`content`に入れたkind 30315イベントを公開します。イベントはpubkey、kind、`d` tagでaddressableなので、同じカテゴリのより新しいイベントが古いものを置き換えます。contentフィールドが空であれば、そのステータスは消去されます。

---

**主要ソース:**

- [NIP-38仕様](https://github.com/nostr-protocol/nips/blob/master/38.md) - ユーザーステータス

**言及箇所:**

- [ニュースレター #37: NoorNote v1.3.6: プロフィールステータスとclassified listing](/ja/newsletters/2026-08-26-newsletter/#noornote-v136-プロフィールステータスとclassified-listing)
