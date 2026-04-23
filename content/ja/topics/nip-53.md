---
title: "NIP-53: Live Activities"
date: 2026-04-15
translationOf: /en/topics/nip-53.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Live Streaming
---

NIP-53は、Nostr上でライブ配信metadataを公開するための標準イベント形式を定義します。配信はkind `30311`のaddressable eventとして告知されるため、clientはそれを発見し、現在の状態を表示し、chatをその配信文脈へ結び付けられます。

## 仕組み

各配信は、安定した識別子として`d`タグを持つkind `30311`イベントを使います。イベントには通常、titleとsummaryのテキスト、再生URLを示す`streaming`タグ、`status`タグ（`planned`、`live`、`ended`）が含まれます。これはaddressable eventなので、同じ`d`値に対する更新は過去metadataを置き換え、無制限にイベントが積み上がることはありません。

イベントにはtopic tags（`t`）、参加者参照（`p`）、任意の参加者数フィールドも含められます。ライブchatは、その配信を`a`タグで参照するkind `1311`イベントで運ばれ、chat messageが1つのlive activity recordへ結び付いたままになります。

## Implementations

- [Shosho](https://github.com/r0d8lsh0p/shosho-releases)は、Nostrネイティブなライブ配信のまわりでlive stream metadataとchatを公開しています。
- [Zap.stream](https://zap.stream/)は、配信の発見とインタラクションにNostr eventsを使っています。
- [WaveFunc](https://github.com/zeSchlausKwab/wavefunc)は、internet radioの文脈でkind `1311`のlive chat eventsを使っています。
- [Amethyst](https://github.com/vitorpamplona/amethyst)は、[PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469)で[NIP-75](/ja/topics/nip-75/)のzap goalsをLive Activities画面へ統合しました。各ライブ配信にfundraising goal header、progress bar、ワンタップのzapボタン、配信のkind `30311`イベントに結び付いたkind `9735` zap receiptsから計算されるtop-zappers leaderboardが表示されます。続く[PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491)はNIP-53 proof of agreementとevent buildersを追加し、[PR #2486](https://github.com/vitorpamplona/amethyst/pull/2486)はfilteringとdiscoveryを備えた専用のLive Streams feed画面を出荷しました。
- [NoorNote v0.8.4](https://github.com/77elements/noornote/releases/tag/v0.8.4)は、ライブ配信カードからのワンタップzapを追加し、送られたsatsがNIP-53経由で配信のchat overlayへ表示されます。

---

**Primary sources:**
- [NIP-53 Specification](https://github.com/nostr-protocol/nips/blob/master/53.md)
- [Amethyst PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) - Live stream goal header and top-zappers leaderboard
- [Amethyst PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491) - NIP-53 proof of agreement and event builders

**Mentioned in:**
- [Newsletter #18: WaveFunc launch](/en/newsletters/2026-04-15-newsletter/)
- [Newsletter #19: Amethyst live stream zap goals](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: NoorNote v0.8.4](/en/newsletters/2026-04-22-newsletter/)

**See also:**
- [NIP-29: Relay-based Groups](/ja/topics/nip-29/)
- [NIP-75: Zap Goals](/ja/topics/nip-75/)
- [NIP-57: Zaps](/ja/topics/nip-57/)
- [NIP-C7: Chat Messages](/ja/topics/nip-c7/)
