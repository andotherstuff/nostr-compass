---
title: "NIP-91: AND-operator voor filters"
date: 2026-03-04
translationOf: /en/topics/nip-91.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - Protocol
---

NIP-91 voegt AND-filtersemantiek toe voor tag-arrays in Nostr-relay subscriptions. De specificatie werd op 2026-03-03 gemerged nadat implementaties in meerdere relays waren verschenen.

## Het probleem

Het filtersysteem van Nostr ([NIP-01](/nl/topics/nip-01/)) combineert meerdere waarden binnen een enkele tag-filter met OR-logica. Als een client twee `p` tag-waarden in een filter opgeeft, retourneert de relay events die overeenkomen met een van beide pubkeys. Er was geen manier om events op te vragen die beide pubkeys tegelijk refereren.

Daardoor moesten clients te veel events van relays ophalen en lokaal filteren, wat het bandbreedtegebruik en de verwerkingstijd verhoogde.

## Hoe het werkt

NIP-91 introduceert AND-semantiek voor tag-arrays. Wanneer een client events nodig heeft die overeenkomen met alle opgegeven tag-waarden, kan die kiezen voor intersection matching in plaats van het standaard union-gedrag.

Dat is relevant voor queries zoals "events die beide deelnemers in een gesprek taggen" of "events die twee vereiste labels tegelijk dragen." Voor deze wijziging konden relays alleen de bredere superset teruggeven en de precieze intersection aan de client overlaten.

## Waarom het belangrijk is

AND-filters maken relay-side indexes nuttiger. Clients kunnen een relay om een kleinere, al relevante resultatenset vragen, wat bandbreedte en lokale nabewerking vermindert. De winst is het duidelijkst op mobiele clients en bij queries over grote datasets met veel tags.

## Interop-opmerkingen

Op het moment van de merge bestonden werkende implementaties in nostr-rs-relay, satellite-node, worker-relay en applesauce. Het voorstel had eerder nummer NIP-119 voordat het werd hernummerd.

Clients moeten nog steeds rekening houden met gemengde ondersteuning terwijl relay-adoptie bijtrekt. Een praktische fallback is om het oude client-side intersection-pad te behouden voor relays die de nieuwe semantiek nog niet hebben geïmplementeerd.

---

**Primaire bronnen:**
- [PR #1365](https://github.com/nostr-protocol/nips/pull/1365)

**Vermeld in:**
- [Nieuwsbrief #12: NIP-updates](/nl/newsletters/2026-03-04-newsletter/#nip-updates)

**Zie ook:**
- [NIP-01: Basisprotocol](/nl/topics/nip-01/)
