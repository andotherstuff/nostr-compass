---
title: "NIP-18: Reposts"
date: 2025-12-17
translationDate: 2026-03-07
draft: false
categories:
  - Sociaal
  - Protocol
---

NIP-18 definieert hoe events gerepost kunnen worden, vergelijkbaar met retweets op andere platforms.

## Hoe het werkt

Een repost is een kind 6 event (voor kind 1-notities) of kind 16 (generieke repost) dat het volgende bevat:
- een `e` tag die verwijst naar het gereposte event
- een `p` tag die verwijst naar de oorspronkelijke auteur
- optioneel het volledige oorspronkelijke event in het veld `content`

Kind 6 is specifiek voor tekstnotities. Kind 16 bestaat zodat clients ook andere eventtypen kunnen reposten zonder te doen alsof alles een kind 1-notitie is.

## Interop-opmerkingen

De ondersteuning voor het reposten van vervangbare events is verbeterd met `a` tag-ondersteuning. Daardoor kunnen reposts van adresseerbare events (kinds 30000-39999) ernaar verwijzen via hun adres in plaats van via een specifieke event-ID.

Dat onderscheid is belangrijk omdat adresseerbare events in de loop van de tijd kunnen worden bijgewerkt. Reposten via een `a`-coordinat laat clients verwijzen naar de huidige versie van een adresseerbaar event, terwijl reposten via event-ID een specifiek historisch exemplaar vastzet.

## Waarom het belangrijk is

Reposts zijn meer dan een share-knop in de UI. Ze maken deel uit van hoe content zich door sociale grafen verplaatst, hoe clients betrokkenheid tellen en hoe relay hint-data zich door het netwerk verspreidt. Als een client repost-tags verkeerd verwerkt, kunnen thread-reconstructie en event-opvraging op subtiele manieren stukgaan.

---

**Primaire bronnen:**
- [NIP-18-specificatie](https://github.com/nostr-protocol/nips/blob/master/18.md)
- [PR #2132](https://github.com/nostr-protocol/nips/pull/2132) - `a` tag-ondersteuning voor generieke reposts

**Vermeld in:**
- [Nieuwsbrief #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Nieuwsbrief #8: Nieuws](/en/newsletters/2026-02-04-newsletter/#news)

**Zie ook:**
- [NIP-01: Basic Protocol](/nl/topics/nip-01/)
- [NIP-10: Text Note Threading](/nl/topics/nip-10/)
