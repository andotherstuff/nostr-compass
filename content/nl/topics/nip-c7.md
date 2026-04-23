---
title: "NIP-C7: Chat Messages"
date: 2026-04-15
translationOf: /en/topics/nip-c7.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Messaging
---

NIP-C7 definieert kind `9` als het event kind voor chat messages. Het doel is chatgericht verkeer te scheiden van algemeen sociaal feedverkeer, zodat clients andere UX- en moderatieregels op elke context kunnen toepassen.

## Hoe Het Werkt

Een kind `9`-event draagt berichtinhoud plus tags die de chatcontext identificeren. In [NIP-29](/nl/topics/nip-29/) relay-based groups bevat het event een `h`-tag met de group ID. Reply-threading gebruikt `q`-tags die naar eerdere events verwijzen.

NIP-C7 focust op waar deze events moeten worden gerenderd. In plaats van in globale note-feeds te verschijnen zoals kind `1` text notes, zijn kind `9`-events bedoeld voor chatgerichte weergaven waarin conversatiestatus en threading expliciet zijn.

## Implementaties

- [Flotilla](https://gitea.coracle.social/coracle/flotilla) en [Coracle](https://github.com/coracle-social/coracle) gebruiken kind `9` in group-chatworkflows.
- [Amethyst](https://github.com/vitorpamplona/amethyst) bevat kind `9`-ondersteuning in zijn messaging-stack.
- [White Noise](https://github.com/marmot-protocol/whitenoise) gebruikt NIP-C7 reply-threading met `q`-tags.

---

**Primaire bronnen:**
- [NIP-C7 Specification](https://github.com/nostr-protocol/nips/blob/master/C7.md)
- [PR #2310: Restrict kind 9 to chat views](https://github.com/nostr-protocol/nips/pull/2310)

**Vermeld in:**
- [Newsletter #18: NIP Updates](/en/newsletters/2026-04-15-newsletter/)

**Zie ook:**
- [NIP-29: Relay-based Groups](/nl/topics/nip-29/)
- [NIP-17: Private Direct Messages](/nl/topics/nip-17/)
