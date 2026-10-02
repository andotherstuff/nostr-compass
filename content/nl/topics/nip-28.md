---
title: "NIP-28: Openbare chat"
date: 2026-09-30
translationOf: /en/topics/nip-28.md
translationDate: 2026-10-02
draft: false
categories:
  - NIPs
  - Social
---

NIP-28 beschrijft openbare chatkanalen, kanaalberichten en moderatie aan de clientzijde als Nostr-events. De huidige specificatie is gemarkeerd als **draft** en **unrecommended** en verwijst implementeerders naar NIP-29 voor de huidige groepen op basis van relays.

## Eventmodel {#event-model}

Kind `40` maakt een kanaal aan; kind `41` werkt de metadata ervan bij; kind `42` bevat een bericht. Met kinds `43` en `44` kan een gebruiker in zijn client een bericht verbergen of een andere gebruiker dempen. Berichttags verwijzen naar het event waarmee het kanaal is aangemaakt en kunnen het bericht aanduiden waarop wordt gereageerd. Relays hoeven die keuzes voor verbergen en dempen aan de clientzijde niet af te dwingen.

De [specificatiewijziging van september 2022](https://github.com/nostr-protocol/nips/commit/3423a6dfb) maakte van een openbare chatruimte een gedeeld onderwerp van het protocol. Die historische rol blijft nuttig om te begrijpen, ook al raadt de [huidige specificatie](https://github.com/nostr-protocol/nips/blob/master/28.md) een andere route aan voor nieuwe implementaties.

---

**Primaire bronnen:**
- [NIP-28-specificatie en huidige status](https://github.com/nostr-protocol/nips/blob/master/28.md)
- [Wijziging voor openbare chat uit september 2022](https://github.com/nostr-protocol/nips/commit/3423a6dfb)

**Genoemd in:**
- [Nieuwsbrief #42: september 2022](/nl/newsletters/2026-09-30-newsletter/#september-2022-chat-and-delegated-actions-enter-the-specifications)

**Zie ook:**
- [NIP-29: Groepen op basis van relays](/nl/topics/nip-29/)
