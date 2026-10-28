---
title: "NIP-03: event の OpenTimestamps アテステーション"
date: 2026-10-28
translationOf: /en/topics/nip-03.md
translationDate: 2026-10-28
draft: false
categories:
  - Protocol
---

NIP-03 は、Nostr の event に対する [OpenTimestamps](https://opentimestamps.org/) 証明を公開する方法を定めています。この証明は、その event が特定の Bitcoin ブロックの時点までに存在していたことを示す証拠です。

**警告:** 現在の仕様には `draft`、`optional`、`unrecommended` というラベルが付いています。そのヘッダーには、ある特定の攻撃に対して脆弱であり、更新が必要だと記されています。本文ではその攻撃について説明されていません。この形式は歴史的な参考資料として扱い、仕様が改訂されるまでは新たな取り組みに採用しないでください。

## 仕組み

証明は、独立した kind 1040 の event として公開されます。その `e` tag は対象 event の id を relay URL とともに示し、`k` tag は対象 event の kind を記録します。OpenTimestamps 証明は、対象 event の id そのものをダイジェストとして証明しなければなりません。id が改めてハッシュされることはありません。

`content` には、base64 でエンコードされた完全な `.ots` ファイルが格納され、少なくとも 1 つの Bitcoin アテステーションが含まれます。仕様が推奨するのは、アテステーションをちょうど 1 つにし、保留中のアテステーションを含めないことです。保留中のアテステーションは検証の助けにならず、バイト数を増やすだけだからです。

検証者は kind 1040 の event を取得し、そのコンテンツをデコードして、証明を Bitcoin と照合します。有効な証明は、アテステーションされたブロックの時点までに event id がコミットされていたことを示します。これにより、作成者自身の `created_at` の値に依存しない、event の作成時刻として考えうる最も遅い時点が定まります。ただし、event の内容が真実であることを示すものではありません。

## 経緯

[2023 年 10 月 11 日のコミット](https://github.com/nostr-protocol/nips/commit/09ffb951c69343312486aaff2726dca04bc42f6e)で、証明の置き場所が変わりました。それ以前、証明は event 自体に付加される `ots` フィールドでした。このコミット以降は、各証明が対象を指し示す独立した kind 1040 の event になっています。

## 一次資料

- [現在の NIP-03 仕様](https://github.com/nostr-protocol/nips/blob/master/03.md)
- [証明を kind 1040 の event に移した 2023 年 10 月 11 日のコミット](https://github.com/nostr-protocol/nips/commit/09ffb951c69343312486aaff2726dca04bc42f6e)

## ニュースレターでの言及

- [ニュースレター #46 (2026-10-28): 2023 年 10 月、event が証拠と作業依頼を運ぶように](/ja/newsletters/2026-10-28-newsletter/#october-2023-events-carry-evidence-and-requests-for-work)

## 関連項目

- [NIP-01: 基本プロトコル](/ja/topics/nip-01/)
