---
title: "BUD-10: Blossom URI-schema"
date: 2025-12-17
translationDate: 2026-03-07
translationOf: /en/topics/bud-10.md
draft: false
categories:
  - Media
  - Protocol
---

BUD-10 definieert het `blossom:` URI-schema, een draagbare blobverwijzing die serverhints, auteurshints en de verwachte grootte naast de bestands-hash kan meenemen.

## URI-formaat

```
blossom:<sha256>.<ext>?xs=<server>&as=<pubkey>&sz=<bytes>
```

De specificatie vereist een 64 tekens lange SHA-256-hash in kleine letters en een bestandsextensie. Als de extensie onbekend is, moeten clients terugvallen op `.bin`.

## Hoe resolutie werkt

Clients moeten een `blossom:` URI stapsgewijs oplossen:

1. Probeer eventuele `xs` serverhints in de volgorde waarin ze verschijnen
2. Als `as` auteurspubkeys aanwezig zijn, haal dan van elke auteur de serverlijst uit [BUD-03](/nl/topics/bud-03/) op en probeer die servers
3. Val zo nodig terug op bekende servers of lokale cache

Die volgorde is nuttig omdat een verzender daarmee directe hints kan meesturen voor snelle retrieval, terwijl ontvangers nog steeds een herstelpad hebben als die hints verouderen.

## Waarom dit belangrijk is

`blossom:` URI's werken meer als magnet links dan als gewone media-URL's. Ze beschrijven welke blob moet worden opgehaald en geven aanwijzingen over waar die te vinden is, in plaats van ervan uit te gaan dat een host voor altijd beschikbaar blijft.

Het optionele veld `sz` voegt naast de hash een concrete integriteitscontrole toe. Clients kunnen de verwachte grootte voor of na het downloaden verifiëren, wat helpt om onvolledige overdrachten te detecteren en de UX voor grote mediabestanden verbetert.

---

**Primaire bronnen:**
- [BUD-10 specificatie](https://github.com/hzrd149/blossom/blob/master/buds/10.md)
- [Blossom repository](https://github.com/hzrd149/blossom)

**Vermeld in:**
- [Nieuwsbrief #1: Nieuws](/en/newsletters/2025-12-17-newsletter/#news)

**Zie ook:**
- [Blossom Protocol](/nl/topics/blossom/)
- [BUD-03: Gebruikersserverlijst](/nl/topics/bud-03/)
