---
title: "NIP-35: Torrents"
date: 2026-10-21
translationOf: /en/topics/nip-35.md
translationDate: 2026-10-28
draft: false
categories: ["NIPs"]
---

NIP-35 is een optionele NIP in draftstatus voor torrent-indexevents. Een event van kind 2003 bevat een BitTorrent v1-infohash in een `x`-tag, samen met bestandspaden, en kan trackers noemen. De events bevatten indexmetadata; peers halen de bestandsinhoud op via BitTorrent. Reacties op een torrent gebruiken kind 2004 en volgen de threading van NIP-10.

Het nummer heeft een voorgeschiedenis. Draft Wraps had NIP-35 tot een hernummering in 2024 dat voorstel naar NIP-37 verplaatste. Een verwijzing naar NIP-35 van vóór die wijziging kan dus Draft Wraps bedoelen. Tegenwoordig hoort het nummer bij Torrents.

De [huidige NIP-35-tekst](https://github.com/nostr-protocol/nips/blob/master/35.md) definieert het eventformaat. In de [hernummeringscommit](https://github.com/nostr-protocol/nips/commit/48674e563865b1cb7bb3c5c7869d20055446f408) is de eerdere toewijzing vastgelegd.

## Primaire bronnen

- [NIP-35: Torrents](https://github.com/nostr-protocol/nips/blob/master/35.md)
- [nostr-protocol/nips-commit 48674e5 (hernummering in 2024)](https://github.com/nostr-protocol/nips/commit/48674e563865b1cb7bb3c5c7869d20055446f408)

## Genoemd in
- [Nieuwsbrief #46: Magnetar](/nl/newsletters/2026-10-28-newsletter/#magnetar)

- [Nieuwsbrief 45](/en/newsletters/2026-10-21-newsletter/#short-history)
