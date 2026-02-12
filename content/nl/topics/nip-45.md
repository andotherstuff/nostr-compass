---
title: "NIP-45: Event Counting"
date: 2026-02-11
translationOf: /en/topics/nip-45.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-45 definieert hoe toepassingen relays vragen om events te tellen die overeenkomen met een filter, zonder de events zelf over te dragen. Toepassingen sturen COUNT-bericht met dezelfde filtersyntax als REQ, en relays antwoorden met een telling.

## Werking

De toepassing stuurt COUNT-verzoek met abonnements-ID en filter:

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

De relay antwoordt met de telling:

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

Zo wordt voorkomen dat honderden of duizenden events gedownload moeten worden om een getal te tonen.

## HyperLogLog Approximate Counting

Per februari 2026 ondersteunt NIP-45 HyperLogLog (HLL) approximate counting ([PR #1561](https://github.com/nostr-protocol/nips/pull/1561)). Relays kunnen 256-byte HLL-registerwaarden retourneren naast COUNT-responses:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<base64 encoded 256 bytes>"}]
```

HLL lost fundamenteel probleem op: het tellen van unieke events over meerdere relays. Meldt relay A 50 reacties en relay B 40, dan is de som niet 90 omdat veel events op beide relays bestaan. HLL-registers van meerdere relays zijn samen te voegen door de maximumwaarde op elke registerpositie te nemen, wat automatisch deduplicatie over het netwerk afhandelt.

Met 256 registers is de standaardfout ongeveer 5,2%. HyperLogLog++-correcties verbeteren de nauwkeurigheid voor kleine cardinaliteiten onder ~200 events. Zelfs twee reactie-events verbruiken meer bandbreedte dan de 256-byte HLL-payload, wat de aanpak efficient maakt voor iedere telling boven triviale aantallen.

De spec fixeert het registeraantal op 256 voor interoperabiliteit over relay-implementaties heen.

## Toepassingen

Sociale metrics (volger-tellingen, reactietellingen, repost-tellingen) vormen de primaire toepassing. Zonder HLL moeten toepassingen ofwel enkele "vertrouwde" relay bevragen voor tellingen (wat de gegevens centraliseert) of events van iedere relay downloaden om lokaal te dedupliceren (wat bandbreedte verspilt). HLL levert benaderende cross-relay tellingen met 256 bytes overhead per relay.

---

**Primaire bronnen:**
- [NIP-45: Event Counting](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561: HyperLogLog Relay Response](https://github.com/nostr-protocol/nips/pull/1561)

**Vermeld in:**
- [Nieuwsbrief #9: NIP Deep Dive](/nl/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-45-event-counting-en-hyperloglog)
- [Nieuwsbrief #9: NIP-Updates](/nl/newsletters/2026-02-11-newsletter/#nip-updates)

**Zie ook:**
- [NIP-11: Relay Information Document](/nl/topics/nip-11/)
