---
title: "NIP-53: Live Activities"
date: 2026-04-15
translationOf: /en/topics/nip-53.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Live Streaming
description: "NIP-53 definiert, wie Livestream-Metadaten auf Nostr mit kind-30311-Addressable-Events veröffentlicht werden."
---

NIP-53 definiert das Standard-Event-Format für Livestream-Metadaten auf Nostr. Ein Stream wird als kind-`30311`-Addressable-Event angekündigt, sodass Clients ihn entdecken, seinen aktuellen Status anzeigen und den Chat an den Stream-Kontext binden können.

## Funktionsweise

Jeder Stream nutzt ein kind-`30311`-Event mit einem `d`-Tag als stabiler Kennung. Das Event enthält typischerweise Titel- und Summary-Text, ein `streaming`-Tag mit der Playback-URL und ein `status`-Tag (`planned`, `live` oder `ended`). Weil dies ein addressable Event ist, ersetzen Updates frühere Metadaten mit demselben `d`-Wert, statt eine unbegrenzte Event-Spur zu erzeugen.

Das Event kann Themen-Tags (`t`), Teilnehmer-Referenzen (`p`) und optionale Felder zur Teilnehmerzahl enthalten. Live-Chat läuft über kind-`1311`-Events, die den Stream mit einem `a`-Tag referenzieren. So bleiben Chat-Nachrichten an genau einen Live-Activity-Datensatz gebunden.

## Implementierungen

- [Shosho](https://github.com/r0d8lsh0p/shosho-releases) veröffentlicht Livestream-Metadaten und Chat rund um Nostr-native Live-Broadcasts.
- [Zap.stream](https://zap.stream/) nutzt Nostr-Events für Stream-Discovery und Interaktion.
- [WaveFunc](https://github.com/zeSchlausKwab/wavefunc) nutzt kind-`1311`-Live-Chat-Events im Kontext seines Internetradios.
- [Amethyst](https://github.com/vitorpamplona/amethyst) integrierte [NIP-75](/de/topics/nip-75/) Zap Goals über [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) in den Live-Activities-Screen: Jeder Livestream erhält einen Fundraising-Header mit Fortschrittsbalken, One-Tap-Zap-Button und Top-Zappers-Leaderboard auf Basis von kind-`9735`-Zap-Receipts, die an das kind-`30311`-Event des Streams gebunden sind. Das Follow-up [PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491) fügt NIP-53-Proof-of-Agreement und Event-Builder hinzu, und [PR #2486](https://github.com/vitorpamplona/amethyst/pull/2486) liefert einen dedizierten Live-Streams-Feed mit Filterung und Discovery.
- [NoorNote v0.8.4](https://github.com/77elements/noornote/releases/tag/v0.8.4) fügt One-Tap-Zapping aus Livestream-Karten hinzu, wobei die sats im Chat-Overlay des Streams über NIP-53 erscheinen.

---

**Primärquellen:**
- [NIP-53 Specification](https://github.com/nostr-protocol/nips/blob/master/53.md)
- [Amethyst PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) - Live-Stream-Zielheader und Top-Zappers-Leaderboard
- [Amethyst PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491) - NIP-53 proof of agreement and event builders

**Erwähnt in:**
- [Newsletter #18: WaveFunc launch](/en/newsletters/2026-04-15-newsletter/)
- [Newsletter #19: Amethyst live stream zap goals](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: NoorNote v0.8.4](/en/newsletters/2026-04-22-newsletter/)

**Siehe auch:**
- [NIP-29: Relay-based Groups](/de/topics/nip-29/)
- [NIP-75: Zap Goals](/de/topics/nip-75/)
- [NIP-57: Zaps](/de/topics/nip-57/)
- [NIP-C7: Chat Messages](/de/topics/nip-c7/)
