---
title: "BUD-03: Gebruikersserverlijst"
date: 2025-12-17
translationDate: 2026-03-07
translationOf: /en/topics/bud-03.md
draft: false
categories:
  - Media
  - Protocol
---

BUD-03 definieert hoe een gebruiker hun voorkeurs-Blossom-servers publiceert, zodat clients weten waar ze blobs moeten uploaden en waar ze moeten zoeken wanneer een media-URL niet meer werkt.

## Hoe Het Werkt

Gebruikers publiceren een replaceable kind `10063` event met een of meer `server` tags. Elke tag bevat een volledige Blossom-server-URL.

Clients kunnen dan:
- blobs uploaden naar de voorkeursservers van de gebruiker
- waarschijnlijke bloblocaties ontdekken op basis van de pubkey van de auteur
- ophalen opnieuw proberen vanaf de vermelde servers wanneer een oudere URL niet meer werkt

## Details Die Nuttig Zijn Voor Lezers

De volgorde van `server` tags is belangrijk. De specificatie zegt dat gebruikers hun meest vertrouwde of betrouwbaarste servers eerst moeten vermelden, en clients moeten voor uploads in elk geval de eerste server proberen. Dat betekent dat BUD-03 niet alleen een directory is, maar ook een zwak voorkeurssignaal.

De richtlijn voor retrieval is ook praktisch: wanneer een client een blobhash uit een URL haalt, moet die de laatste 64-tekens lange hex-string in het pad gebruiken. Dit helpt clients blobs terug te vinden uit zowel standaard Blossom-URL's als niet-standaard CDN-achtige URL's die de hash nog steeds bevatten.

---

**Primaire bronnen:**
- [BUD-03-specificatie](https://github.com/hzrd149/blossom/blob/master/buds/03.md)
- [Blossom-repository](https://github.com/hzrd149/blossom)

**Vermeld in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)

**Zie ook:**
- [Blossom-protocol](/nl/topics/blossom/)
- [NIP-51: Lijsten](/nl/topics/nip-51/)
