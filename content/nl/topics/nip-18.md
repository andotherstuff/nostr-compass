---
title: "NIP-18: Reposts"
date: 2025-12-17
draft: false
categories:
  - Sociaal
  - Protocol
---

NIP-18 definieert hoe events gerepost kunnen worden, vergelijkbaar met retweets op andere platforms.

## Structuur

Een repost is een kind 6 event (voor kind 1 nota's) of kind 16 (generieke repost) die bevat:
- `e` tag die naar het gereposte event verwijst
- `p` tag die naar de originele auteur verwijst
- Optioneel het volledige originele event in het `content` veld

## Recente Wijzigingen

Verbeterde ondersteuning voor het reposten van vervangbare events met `a` tag ondersteuning. Dit maakt het mogelijk dat reposts van adresseerbare events (kinds 30000-39999) ernaar verwijzen via hun adres in plaats van een specifieke event-ID.

---

**Primaire bronnen:**
- [NIP-18 Specificatie](https://github.com/nostr-protocol/nips/blob/master/18.md)

**Vermeld in:**
- [Nieuwsbrief #1: NIP Updates](/nl/newsletters/2025-12-17-newsletter/#nip-updates)

**Zie ook:**
- [NIP-01: Basisprotocol](/nl/topics/nip-01/)
