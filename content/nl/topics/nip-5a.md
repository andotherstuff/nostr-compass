---
title: "NIP-5A: Static Websites"
date: 2026-04-01
translationOf: /en/topics/nip-5a.md
translationDate: 2026-04-01
draft: false
categories:
  - Protocol
  - Hosting
---

NIP-5A definieert hoe statische websites onder Nostr-sleutelparen gehost kunnen worden. Site-auteurs publiceren ondertekende manifestevents die URL-paden koppelen aan SHA256-inhoudshashes, en hostservers resolven die manifesten om de bestanden van de site te serveren vanuit Blossom-opslag.

## Hoe Het Werkt

De specificatie gebruikt twee event kinds. Kind `15128` is een rootsitemanifest, één per pubkey, dat dient als de standaardwebsite voor die sleutel. Kind `35128` is een benoemd sitemanifest, geïdentificeerd door een `d` tag, dat functioneert als een subdomein. Elk manifest bevat `path` tags die absolute URL-paden koppelen aan SHA256-hashes van de bestanden die geserveerd moeten worden.

```json
{
  "id": "5324d695ed7abf7cdd2a48deb881c93b7f4e43de702989bbfb55a1b97b35a3de",
  "pubkey": "266815e0c9210dfa324c6cba3573b14bee49da4209a9456f9484e5106cd408a5",
  "created_at": 1743465600,
  "kind": 15128,
  "tags": [
    ["path", "/index.html", "186ea5fd14e88fd1ac49351759e7ab906fa94892002b60bf7f5a428f28ca1c99"],
    ["path", "/about.html", "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"],
    ["server", "https://blossom.primal.net"],
    ["title", "My Nostr Site"],
    ["source", "https://github.com/lez/nsite"]
  ],
  "content": "",
  "sig": "f4e4a9e785f70e9fcaa855d769438fea10781e84cd889e3fcb823774f83d094cf2c05d5a3ac4aebc1227a4ebc3d56867286c15a6df92d55045658bb428fd5fb5"
}
```

Een hostserver ontvangt een HTTP-verzoek, extraheert de pubkey van de auteur uit het subdomein, haalt het sitemanifest op uit de relaylijst van de auteur, resolveert het gevraagde pad naar een inhoudshash, en downloadt de overeenkomende blob van de Blossom-server(s) vermeld in `server` tags.

## URL-resolutie

Rootsites gebruiken de npub als subdomein. Benoemde sites gebruiken een 50-karakter base36-codering van de rauwe pubkey gevolgd door de `d` tagwaarde, allemaal in één DNS-label. Omdat DNS-labels beperkt zijn tot 63 karakters en de base36-pubkey altijd 50 gebruikt, zijn benoemde site-identifiers beperkt tot 13 karakters.

## Implementaties

- [nsite](https://github.com/lez/nsite) - Hostserver die NIP-5A manifesten resolveert en bestanden serveert
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - UI voor het bouwen en publiceren van sitemanifesten

---

**Primaire bronnen:**
- [NIP-5A Specificatie](https://github.com/nostr-protocol/nips/blob/master/5A.md)
- [PR #1538](https://github.com/nostr-protocol/nips/pull/1538) - Oorspronkelijk voorstel en merge
- [nsite](https://github.com/lez/nsite) - Referentie-hostimplementatie
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - Publicatie- en beheer-UI

**Vermeld in:**
- [Newsletter #16: NIP-5A merges](/nl/newsletters/2026-04-01-newsletter/#nip-5a-merges-bringing-static-websites-to-nostr)
- [Newsletter #16: NIP Deep Dive](/nl/newsletters/2026-04-01-newsletter/#nip-deep-dive-nip-5a-static-websites)

**Zie ook:**
- [Blossom](/nl/topics/blossom/)
- [NIP-65: Relay List Metadata](/nl/topics/nip-65/)
- [NIP-96: HTTP File Storage](/nl/topics/nip-96/)
