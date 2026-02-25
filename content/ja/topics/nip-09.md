---
title: "NIP-09"
date: 2026-02-25
translationOf: /en/topics/nip-09.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - Protocol
---

NIP-09はイベント削除を定義します。これはユーザーが以前に公開したイベントをrelayから削除するよう要求するメカニズムです。

## 仕組み

ユーザーは削除したいイベントIDを参照する`e`タグを含むkind 5イベントを公開します。NIP-09をサポートするrelayは参照されたイベントの配信を停止し、ストレージから削除することができます。

削除はリクエストであり、保証ではありません。relayは削除リクエストを無視することがあり、削除をサポートしないrelayにすでに伝播しているeventもあります。プライバシーに関わるコンテンツの削除にNIP-09を頼ることはお勧めしません。

## 主な機能

- kind 5削除リクエストイベント
- eタグによるIDでの削除イベントの参照
- 削除理由の任意フィールド
- relayの準拠は任意

---

**主要ソース：**
- [NIP-09仕様](https://github.com/nostr-protocol/nips/blob/master/09.md)

**掲載ニュースレター：**
- [ニュースレター#11：NIP-60ディープダイブ](/ja/newsletters/2026-02-25-newsletter/#nipディープダイブnip-60cashuウォレット)

**関連項目：**
- [NIP-60：Cashuウォレット](/ja/topics/nip-60/)
