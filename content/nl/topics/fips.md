---
title: "FIPS"
date: 2026-02-25
translationOf: /en/topics/fips.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Networking
  - Infrastructure
---

FIPS (Free Internetworking Peering System) is een zelforganiserend mesh-netwerkprotocol dat Nostr-achtige secp256k1-sleutelparen gebruikt als node-identiteiten.

## Hoe het werkt

FIPS wil peer-netwerken laten werken zonder centrale servers of certificaatautoriteiten. Nodes ontdekken buren, bouwen routingstatus op en sturen pakketten door met alleen lokale kennis.

Het ontwerp combineert een spanning tree met bloom filter-bereikbaarheidsdata. Elke node krijgt coordinaten relatief aan de tree en routeert daarna greedy richting de bestemming. Als greedy routing faalt, biedt de tree nog steeds een fallback-pad.

Twee encryptielagen beschermen het verkeer. Link-layer encryption (Noise IK pattern) beveiligt hop-by-hop-communicatie tussen buren. Session-layer encryption (Noise XK pattern) biedt end-to-end-bescherming tegen tussenliggende routers.

## Waarom het belangrijk is

FIPS hergebruikt hetzelfde sleutelmodel dat Nostr-ontwikkelaars al kennen, maar past het toe op pakketroutering in plaats van op sociale events. Dat geeft het een eenvoudig identiteitsmodel: de netwerkidentiteit is de cryptografische sleutel, niet een IP-toewijzing of certificaatketen.

Het transport-agnostische ontwerp is ook belangrijk. Hetzelfde routing- en identiteitsmodel kan in principe draaien over UDP, Ethernet, Bluetooth of LoRa, wat FIPS interessant maakt voor vijandige of onbetrouwbare netwerkomgevingen.

## Implementatiestatus

Zoals behandeld in Compass bevat de huidige Rust-implementatie al werkende UDP-transport en bloom-filter-gebaseerde discovery. Relay-gebaseerde bootstrapping is nog toekomstig werk, dus vandaag is het protocol eerder een netwerksubstraat dan een volwaardige vervanger voor Nostr relays.

---

**Primaire bronnen:**
- [FIPS-repository](https://github.com/jmcorgan/fips)
- [Ontwerpdocumentatie](https://github.com/jmcorgan/fips/blob/master/docs/design/fips-intro.md)

**Vermeld in:**
- [Newsletter #11: FIPS-nieuws](/en/newsletters/2026-02-25-newsletter/#fips-nostr-native-mesh-networking)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**Zie ook:**
- [Marmot Protocol](/nl/topics/marmot/)
