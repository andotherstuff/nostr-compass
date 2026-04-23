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

NIP-53 definieert het standaard event-formaat voor live streaming-metadata op Nostr. Een stream wordt aangekondigd als een kind `30311` addressable event, zodat clients die kunnen ontdekken, de huidige status kunnen tonen en chat aan de streamcontext kunnen koppelen.

## Hoe Het Werkt

Elke stream gebruikt een kind `30311`-event met een `d`-tag als stabiele identifier. Het event bevat doorgaans title- en summary-tekst, een `streaming`-tag met de playback URL en een `status`-tag (`planned`, `live` of `ended`). Omdat dit een addressable event is, vervangen updates eerdere metadata voor dezelfde `d`-waarde in plaats van een onbegrensd eventspoor te creëren.

Het event kan topic-tags (`t`), participant-references (`p`) en optionele participant-count-velden bevatten. Live chat wordt gedragen door kind `1311`-events die met een `a`-tag naar de stream verwijzen, waardoor chatberichten gekoppeld blijven aan een specifiek live activity-record.

## Implementaties

- [Shosho](https://github.com/r0d8lsh0p/shosho-releases) publiceert live stream-metadata en chat rond Nostr-native live-uitzendingen.
- [Zap.stream](https://zap.stream/) gebruikt Nostr-events voor streamdiscovery en interactie.
- [WaveFunc](https://github.com/zeSchlausKwab/wavefunc) gebruikt kind `1311` live chat-events in zijn internetradiocontext.
- [Amethyst](https://github.com/vitorpamplona/amethyst) integreerde [NIP-75](/nl/topics/nip-75/) zap goals in het Live Activities-scherm via [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469): elke livestream krijgt een fundraising goal-header met een progress bar, een one-tap zap button en een top-zappers leaderboard berekend uit kind `9735` zap receipts die aan het kind `30311`-event van de stream zijn gekoppeld. De vervolg-PR's [PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491) en [PR #2486](https://github.com/vitorpamplona/amethyst/pull/2486) voegen NIP-53 proof-of-agreement, event builders en een dedicated Live Streams-feedscherm met filtering en discovery toe.
- [NoorNote v0.8.4](https://github.com/77elements/noornote/releases/tag/v0.8.4) voegt one-tap zapping toe vanaf live-stream cards waarbij de sats via NIP-53 in de chat-overlay van de stream verschijnen.

---

**Primaire bronnen:**
- [NIP-53 Specification](https://github.com/nostr-protocol/nips/blob/master/53.md)
- [Amethyst PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) - Live stream goal header and top-zappers leaderboard
- [Amethyst PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491) - NIP-53 proof of agreement and event builders

**Vermeld in:**
- [Newsletter #18: WaveFunc launch](/en/newsletters/2026-04-15-newsletter/)
- [Newsletter #19: Amethyst live stream zap goals](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: NoorNote v0.8.4](/en/newsletters/2026-04-22-newsletter/)

**Zie ook:**
- [NIP-29: Relay-based Groups](/nl/topics/nip-29/)
- [NIP-75: Zap Goals](/nl/topics/nip-75/)
- [NIP-57: Zaps](/nl/topics/nip-57/)
- [NIP-C7: Chat Messages](/nl/topics/nip-c7/)
