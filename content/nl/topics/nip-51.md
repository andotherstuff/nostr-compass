---
title: "NIP-51: Lijsten"
date: 2025-12-17
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Sociaal
---

NIP-51 definieert lijst-events voor het organiseren van gebruikers, events, relays, hashtags en andere verwijzingen. Het is het belangrijkste protocol voor bookmarks, mute-lijsten, follow sets, relay sets en verschillende andere door gebruikers samengestelde collecties.

## Standaardlijsten en sets

- **Standaardlijsten** gebruiken replaceable event kinds zoals kind `10000` mute-lijsten, kind `10003` bookmarks en kind `10007` search relays.
- **Sets** gebruiken addressable kinds met `d` tags, zoals kind `30000` follow sets, kind `30003` bookmark sets en kind `30030` emoji sets.

Dat onderscheid is van belang voor clientgedrag. Standaardlijsten impliceren een canonieke lijst per gebruiker en kind. Sets impliceren meerdere benoemde collecties, dus clients moeten de `d` tag van elke lijst behouden.

## Structuur

Lijsten gebruiken tags om naar content te verwijzen:

- `p` tags voor pubkeys
- `e` tags voor events
- `a` tags voor addressable events
- `t` tags voor hashtags
- `word` tags voor gemute woorden
- `relay` tags voor relay-URL's in relaygerichte lijst-kinds

Sommige lijst-kinds hebben beperktere toegestane tagvormen dan andere. Relaygerichte lijsten gebruiken bijvoorbeeld `relay` tags, terwijl bookmarks naar notes of addressable events horen te verwijzen. Clients die elke NIP-51-lijst behandelen als willekeurige vrije tags verliezen interoperabiliteit.

## Openbaar versus privé

Lijsten kunnen openbare tags en privé-items hebben. Privé-items worden geserialiseerd als een JSON-array die de `tags`-structuur weerspiegelt, versleuteld, en opgeslagen in de event-`content`. De huidige specificatie gebruikt NIP-44 voor dit model van zelfversleuteling, met NIP-04 alleen als legacy compatibility.

Die scheiding laat gebruikers een zichtbare lijstschil publiceren terwijl sommige items verborgen blijven. Een bookmark-lijst kan openbaar blijven terwijl privénotities of privé-bookmarks in versleutelde content blijven staan.

## Nuttige kinds

- **Kind 10000**: mute-lijst voor pubkeys, threads, hashtags en gemute woorden
- **Kind 10003**: bookmarks voor notes en addressable content
- **Kind 10007**: preferred search relays
- **Kind 30002**: relay sets voor benoemde relaygroepen
- **Kind 30006**: picture curation sets
- **Kind 39089**: starter packs voor deelbare follow bundles

Recente wijzigingen in de specificatie verplaatsten hashtags uit generieke bookmarks naar interest sets, en voegden kind `30006` toe voor picture curation. Beide wijzigingen verminderen ambiguïteit in hoe clients lijstinhoud interpreteren.

---

**Primaire bronnen:**
- [NIP-51 Specificatie](https://github.com/nostr-protocol/nips/blob/master/51.md)

**Vermeld in:**
- [Nieuwsbrief #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Nieuwsbrief #2: NIP Updates](/en/newsletters/2025-12-24-newsletter/#nip-updates)
- [Nieuwsbrief #4: NIP Deep Dive](/en/newsletters/2026-01-13-newsletter/#nip-deep-dive-nip-51-and-nip-65)
- [Nieuwsbrief #8: njump voegt NIP-51-ondersteuning toe](/en/newsletters/2026-02-04-newsletter/#njump)

**Zie ook:**
- [NIP-02: Follow List](/nl/topics/nip-02/)
