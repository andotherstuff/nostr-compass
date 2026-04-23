---
title: "NIP-C7: Chat Messages"
date: 2026-04-15
translationOf: /en/topics/nip-c7.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Messaging
description: "NIP-C7 definiert kind 9 als dedizierten Event-Kind für Chatnachrichten in Nostr-Gruppen- und Channel-Kontexten."
---

NIP-C7 definiert kind `9` als Event-Kind für Chatnachrichten. Das Ziel ist, chat-orientierten Verkehr von allgemeinem Social-Feed-Verkehr zu trennen, damit Clients auf beide Kontexte unterschiedliche UX- und Moderationsregeln anwenden können.

## Funktionsweise

Ein kind-`9`-Event trägt den Nachrichteninhalt plus Tags, die den Chat-Kontext identifizieren. In [NIP-29](/de/topics/nip-29/) relay-basierten Gruppen enthält das Event ein `h`-Tag mit der Gruppen-ID. Reply-Threading nutzt `q`-Tags, die auf frühere Events verweisen.

NIP-C7 konzentriert sich darauf, wo diese Events gerendert werden sollen. Statt in globalen Notiz-Feeds wie kind-`1`-Textnotizen zu erscheinen, sind kind-`9`-Events für chat-orientierte Ansichten gedacht, in denen Gesprächszustand und Threading explizit sind.

## Implementierungen

- [Flotilla](https://gitea.coracle.social/coracle/flotilla) und [Coracle](https://github.com/coracle-social/coracle) nutzen kind `9` in Gruppenchat-Workflows.
- [Amethyst](https://github.com/vitorpamplona/amethyst) unterstützt kind `9` in seinem Messaging-Stack.
- [White Noise](https://github.com/marmot-protocol/whitenoise) nutzt NIP-C7-Reply-Threading mit `q`-Tags.

---

**Primärquellen:**
- [NIP-C7 Specification](https://github.com/nostr-protocol/nips/blob/master/C7.md)
- [PR #2310: Restrict kind 9 to chat views](https://github.com/nostr-protocol/nips/pull/2310)

**Erwähnt in:**
- [Newsletter #18: NIP Updates](/en/newsletters/2026-04-15-newsletter/)

**Siehe auch:**
- [NIP-29: Relay-based Groups](/de/topics/nip-29/)
- [NIP-17: Private Direct Messages](/de/topics/nip-17/)
