---
title: "NIP-03: OpenTimestamps-attestaties voor events"
date: 2026-10-28
translationOf: /en/topics/nip-03.md
translationDate: 2026-10-28
draft: false
categories:
  - Protocol
---

NIP-03 beschrijft hoe je een [OpenTimestamps](https://opentimestamps.org/)-bewijs voor een Nostr-event publiceert. Het bewijs toont aan dat het event al bestond op het moment van een bepaald Bitcoin-blok.

**Waarschuwing:** de huidige specificatie heeft de labels `draft`, `optional` en `unrecommended`. Volgens de header is ze kwetsbaar voor één specifieke aanval en heeft ze een update nodig. Welke aanval dat is, beschrijft de tekst niet. Beschouw het formaat als historische referentie en gebruik het niet voor nieuw werk totdat de specificatie is herzien.

## Hoe het werkt

Een bewijs wordt gepubliceerd als afzonderlijk event van kind 1040. De `e`-tag noemt de id van het doelevent, samen met een relay-URL, en de `k`-tag legt de kind van het doelevent vast. Het OpenTimestamps-bewijs moet de id van het doelevent zelf als digest bewijzen. Die id wordt niet opnieuw gehasht.

In `content` staat het volledige `.ots`-bestand, base64-gecodeerd, met minstens één Bitcoin-attestatie. De specificatie raadt precies één attestatie aan en geen pending attestaties, omdat die bytes toevoegen zonder de verificatie te helpen.

Een verifier haalt het kind 1040-event op, decodeert de inhoud en controleert het bewijs tegen Bitcoin. Uit een geldig bewijs blijkt dat de event-id uiterlijk in het geattesteerde blok was vastgelegd. Zo ontstaat een uiterste mogelijke aanmaaktijd voor het event die niet afhangt van de eigen `created_at`-waarde van de auteur. Dat de inhoud van het event waar is, toont het niet aan.

## Geschiedenis

Een [commit van 11 oktober 2023](https://github.com/nostr-protocol/nips/commit/09ffb951c69343312486aaff2726dca04bc42f6e) veranderde waar bewijzen worden ondergebracht. Daarvoor was een bewijs een `ots`-veld dat aan het event zelf was gekoppeld. Sindsdien is elk bewijs een afzonderlijk kind 1040-event dat naar zijn doel verwijst.

## Primaire bronnen

- [Huidige NIP-03-specificatie](https://github.com/nostr-protocol/nips/blob/master/03.md)
- [Commit van 11 oktober 2023 die bewijzen naar kind 1040-events verplaatst](https://github.com/nostr-protocol/nips/commit/09ffb951c69343312486aaff2726dca04bc42f6e)

## Genoemd in nieuwsbrieven

- [Nieuwsbrief #46 (2026-10-28): oktober 2023, events dragen bewijs en verzoeken om werk](/nl/newsletters/2026-10-28-newsletter/#october-2023-events-carry-evidence-and-requests-for-work)

## Zie ook

- [NIP-01: Basisprotocol](/nl/topics/nip-01/)
