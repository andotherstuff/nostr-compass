---
title: "NIP-35: トレント"
date: 2026-10-21
translationOf: /en/topics/nip-35.md
translationDate: 2026-10-28
draft: false
categories: ["NIPs"]
---

NIP-35 は、トレントのインデックス event を扱う、ドラフトかつオプションの NIP です。kind 2003 の event は、BitTorrent v1 の infohash を `x` tag に入れてファイルパスとともに運び、トラッカーを指定することもできます。これらの event が保持するのはインデックスのメタデータであり、ファイルの中身はピアが BitTorrent 経由で取得します。トレントへのコメントには kind 2004 を使い、NIP-10 のスレッド形式に従います。

この番号には、以前の経緯があります。2024 年の番号変更でその提案が NIP-37 に移されるまで、NIP-35 は Draft Wraps に割り当てられていました。そのため、変更前の NIP-35 への言及は Draft Wraps を指している可能性があります。現在、この番号は Torrents（トレント）のものです。

[現在の NIP-35 テキスト](https://github.com/nostr-protocol/nips/blob/master/35.md)は event の形式を定義しています。以前の割り当ては、[番号変更のコミット](https://github.com/nostr-protocol/nips/commit/48674e563865b1cb7bb3c5c7869d20055446f408)に記録されています。

## 一次資料

- [NIP-35: トレント](https://github.com/nostr-protocol/nips/blob/master/35.md)
- [nostr-protocol/nips のコミット 48674e5 (2024 年の番号変更)](https://github.com/nostr-protocol/nips/commit/48674e563865b1cb7bb3c5c7869d20055446f408)

## 言及箇所
- [ニュースレター #46: Magnetar](/ja/newsletters/2026-10-28-newsletter/#magnetar)

- [ニュースレター 45](/en/newsletters/2026-10-21-newsletter/#short-history)
