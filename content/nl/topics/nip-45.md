---
title: "NIP-45: Event Counting"
date: 2026-02-11
translationOf: /en/topics/nip-45.md
translationDate: 2026-03-07
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-45 definieert hoe clients relays vragen om events te tellen die overeenkomen met een filter, zonder de overeenkomende events zelf over te dragen. Het hergebruikt de NIP-01-filtersyntax, zodat een client vaak een bestaande `REQ` kan omzetten in een `COUNT`-verzoek met dezelfde filters.

## Hoe het werkt

Een client stuurt een `COUNT`-verzoek met een subscription ID en filter:

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

De relay antwoordt met een telling:

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

Dit voorkomt dat honderden of duizenden events moeten worden gedownload alleen om een getal weer te geven. Als een client meerdere filters in een enkel `COUNT`-verzoek verstuurt, voegt de relay ze samen tot een enkel resultaat, net zoals meerdere `REQ`-filters met OR worden gecombineerd.

## HyperLogLog Approximate Counting

Sinds februari 2026 ondersteunt NIP-45 HyperLogLog (HLL) approximate counting ([PR #1561](https://github.com/nostr-protocol/nips/pull/1561)). Relays kunnen een resultaat als benaderend markeren, en voor cross-relay deduplicatie kunnen ze 256 HLL-registers teruggeven naast de telling:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<512-char hex string>"}]
```

HLL lost een fundamenteel probleem op: het tellen van unieke events over meerdere relays. Als relay A 50 reacties meldt en relay B 40, dan is het totaal niet 90 omdat veel events op beide relays bestaan. Clients voegen HLL-waarden samen door op elke registerpositie de maximumwaarde te nemen, wat een netwerkbrede schatting oplevert zonder de ruwe events te downloaden.

De spec legt het aantal registers vast op 256 voor interoperabiliteit. Dat houdt de payload klein en maakt relay-side caching praktisch omdat elke relay dezelfde registerindeling berekent voor dezelfde geschikte filter.

## Interop-opmerkingen

HLL is alleen gedefinieerd voor filters met een tag-attribuut, omdat de offset die wordt gebruikt om de registers op te bouwen wordt afgeleid van de eerste tagwaarde in het filter. De spec noemt ook een kleine set canonieke query's, waaronder reacties, reposts, quotes, replies, comments en follower counts. Dat zijn de tellingen die relays het makkelijkst kunnen voorberekenen of cachen.

## Waarom het belangrijk is

Follower counts, reaction counts en reply counts zijn de belangrijkste use cases. Zonder NIP-45 moeten clients ofwel de lokale weergave van een enkele relay vertrouwen, of alle overeenkomende events downloaden en ze lokaal dedupliceren. NIP-45 houdt het tellen binnen de relay, en HLL maakt multi-relay tellingen praktisch zonder een relay tot autoriteit te maken.

---

**Primaire bronnen:**
- [NIP-45: Event Counting](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561: HyperLogLog Relay Response](https://github.com/nostr-protocol/nips/pull/1561)

**Vermeld in:**
- [Nieuwsbrief #9: NIP Deep Dive](/en/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-45-event-counting-and-hyperloglog)
- [Nieuwsbrief #9: NIP Updates](/en/newsletters/2026-02-11-newsletter/#nip-updates)
- [Nieuwsbrief #12: Five Years of Nostr Februaries](/en/newsletters/2026-03-04-newsletter/)

**Zie ook:**
- [NIP-11: Relay Information Document](/nl/topics/nip-11/)
