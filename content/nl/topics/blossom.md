---
title: "Blossom-protocol"
date: 2025-12-17
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---

Blossom is een media-hostingprotocol voor Nostr dat blobs opslaat op gewone HTTP-servers en ze adresseert met een SHA-256-hash in plaats van door de server toegekende ID's.

## Hoe Het Werkt

Blossom-servers bieden een kleine HTTP-interface voor blob retrieval, upload en beheer. De canonieke identifier is de bestandshash, dus dezelfde blob houdt hetzelfde adres op elke compatibele server.

- `GET /<sha256>` haalt een blob op via hash
- `PUT /upload` uploadt een blob
- kind `24242` Nostr-events autoriseren uploads en beheeracties
- kind `10063` events, gedefinieerd in [BUD-03](/nl/topics/bud-03/), laten gebruikers hun voorkeursservers publiceren

Omdat de hash de identifier is, kunnen clients de integriteit lokaal verifiëren na het downloaden en een andere server proberen zonder de onderliggende verwijzing te veranderen.

## Waarom Het Belangrijk Is

Blossom scheidt blobopslag van sociale events. Een note of profiel kan naar media verwijzen zonder die media te koppelen aan het URL-ontwerp van een enkele host.

Dat verandert ook de afhandeling van storingen. Als een server verdwijnt, kunnen clients dezelfde hash ophalen vanaf een mirror, een cache of een server die is ontdekt via de [BUD-03](/nl/topics/bud-03/)-lijst van de auteur. Dat is een praktisch voordeel ten opzichte van mediasystemen waar de oorspronkelijke host-URL de enige locator is.

## Interop-opmerkingen

Blossom is modulair. Het kernverhaal voor retrieval en upload staat in BUD-01 en BUD-02, terwijl mirroring, media optimization, autorisatie en URI sharing in afzonderlijke BUDs zijn opgesplitst.

Die opsplitsing laat clients het minimum implementeren dat nodig is voor basisinteroperabiliteit, en daarna optionele onderdelen toevoegen zoals [BUD-10](/nl/topics/bud-10/) URI hints of lokale caching naarmate support rijper wordt.

---

**Primaire bronnen:**
- [Blossom-repository](https://github.com/hzrd149/blossom)
- [BUD-01: Serververeisten en blob retrieval](https://github.com/hzrd149/blossom/blob/master/buds/01.md)
- [BUD-02: Blob upload en beheer](https://github.com/hzrd149/blossom/blob/master/buds/02.md)
- [Handleiding voor Local Blossom Cache](https://github.com/hzrd149/blossom/blob/master/implementations/local-blossom-cache.md)

**Vermeld in:**
- [Nieuwsbrief #1: Nieuws](/en/newsletters/2025-12-17-newsletter/#news)
- [Nieuwsbrief #2: Opvallende code- en documentatiewijzigingen](/en/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes)
- [Nieuwsbrief #10: Blossom local cache-laag verschijnt](/en/newsletters/2026-02-18-newsletter/#blossom-local-cache-layer-emerges)

**Zie ook:**
- [BUD-03: Gebruikersserverlijst](/nl/topics/bud-03/)
- [BUD-10: Blossom-URI-schema](/nl/topics/bud-10/)
