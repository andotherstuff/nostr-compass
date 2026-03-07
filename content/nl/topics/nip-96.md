---
title: "NIP-96: HTTP-bestandsopslag"
date: 2026-02-11
translationOf: /en/topics/nip-96.md
translationDate: 2026-03-07
draft: false
categories:
  - NIPs
  - Media
---

NIP-96 definieert hoe Nostr-clients bestanden uploaden, downloaden en beheren op HTTP-mediaservers. De specificatie is nu gemarkeerd als "unrecommended" ten gunste van Blossom, maar blijft relevant omdat bestaande servers en clients deze tijdens de overgang nog steeds ondersteunen.

## Hoe het werkt

Een client ontdekt de mogelijkheden van een bestandsserver door `/.well-known/nostr/nip96.json` op te halen. Dat document vermeldt de upload-API-URL, optionele download-URL, ondersteunde contenttypes, groottelimieten en of de server mediatransformaties of delegated hosting ondersteunt.

Voor uploads stuurt de client een `multipart/form-data` POST naar de API-URL met een [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md)-autorisatieheader. De server antwoordt met een metadata-object in NIP-94-vorm dat de bestands-URL bevat plus tags zoals `ox` voor de oorspronkelijke hash en, indien van toepassing, `x` voor het getransformeerde bestand dat daadwerkelijk wordt geserveerd.

Downloads gebruiken `GET <api_url>/<sha256-hash>` met optionele queryparameters zoals afbeeldingsbreedte. Verwijderen gebruikt `DELETE` met NIP-98-auth. Gebruikers publiceren kind `10096` events om hun voorkeurs-uploadservers aan te geven.

## Details van het datamodel

Een nuttig detail is dat NIP-96 bestanden identificeert met de oorspronkelijke bestandshash, zelfs wanneer de server de upload transformeert. Daardoor kan een client de asset verwijderen of opnieuw downloaden met dezelfde stabiele identifier, terwijl die nog steeds servergegenereerde thumbnails of opnieuw gecomprimeerde varianten krijgt wanneer die beschikbaar zijn.

Het well-known-document ondersteunt ook `delegated_to_url`, waarmee een relay clients naar een aparte HTTP-opslagserver kan verwijzen. Daardoor hoefde relaysoftware niet zelf de volledige media-API te implementeren.

## Waarom het is afgekeurd

NIP-96 koppelde bestands-URL's aan specifieke servers. Als een server uitviel, verloor elke Nostr-notitie die naar die server-URL's verwees zijn media. Blossom draait dit om door de SHA-256-hash van de bestandsinhoud de canonieke identifier te maken. Elke Blossom-server die hetzelfde bestand host, serveert het op hetzelfde hashpad, waardoor content standaard overdraagbaar is tussen servers.

Blossom vereenvoudigt de API ook: gewone PUT voor uploads, GET voor downloads en ondertekende Nostr-events, geen HTTP-headers, voor autorisatie. De afkeuring gebeurde in september 2025 via [PR #2047](https://github.com/nostr-protocol/nips/pull/2047).

## Interop-opmerkingen

Servers zoals nostr.build en void.cat ondersteunden NIP-96 en hebben Blossom-endpoints toegevoegd of zijn daarnaar gemigreerd. Clients zitten in verschillende fasen: Angor v0.2.5 voegde NIP-96-serverconfiguratie toe, terwijl ZSP v0.3.1 uitsluitend naar Blossom-servers uploadt. Die co-existentie blijft bestaan totdat de resterende NIP-96-implementaties hun migratie hebben afgerond.

Kind 10096 server preference events blijven bruikbaar voor selectie van Blossom-servers. NIP-94-bestandsmetadata (kind 1063 events) beschrijft bestandseigenschappen ongeacht welk uploadprotocol ze heeft gemaakt.

---

**Primaire bronnen:**
- [NIP-96: HTTP File Storage](https://github.com/nostr-protocol/nips/blob/master/96.md)
- [PR #2047: Mark NIP-96 as Unrecommended](https://github.com/nostr-protocol/nips/pull/2047)

**Vermeld in:**
- [Newsletter #9: NIP Deep Dive](/en/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-96-http-file-storage-and-the-transition-to-blossom)

**Zie ook:**
- [Blossom Protocol](/nl/topics/blossom/)
- [NIP-94: Bestandsmetadata](/nl/topics/nip-94/)
