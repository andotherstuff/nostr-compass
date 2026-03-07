---
title: "NIP-56: Rapportage"
date: 2026-02-18
translationOf: /en/topics/nip-56.md
translationDate: 2026-03-07
draft: false
categories:
  - Moderation
  - Protocol
---

NIP-56 definieert kind `1984` report-events. Daarmee kunnen gebruikers en apps moderatiesignalen publiceren over accounts, notities en blobs, zonder dat daar een enkele gedeelde moderatieautoriteit voor nodig is.

## Hoe het werkt

Een report moet een `p`-tag bevatten voor de gerapporteerde pubkey. Als het report over een specifiek event gaat, moet het ook een `e`-tag voor dat event bevatten. Het reporttype staat als derde waarde in de relevante `p`-, `e`- of `x`-tag.

## Rapportcategorieen

- **nudity**: inhoud voor volwassenen
- **malware**: virussen, trojans, ransomware en vergelijkbare payloads
- **profanity**: beledigend taalgebruik en haatzaaien
- **illegal**: inhoud die mogelijk wetten schendt
- **spam**: ongewenste herhaalde berichten
- **impersonation**: frauduleuze identiteitsclaims
- **other**: overtredingen die niet in de bovenstaande categorieen passen

Blob-reports gebruiken `x`-tags met de blobhash en kunnen een `server`-tag bevatten die naar het hostingendpoint wijst. Daardoor is NIP-56 bruikbaar voor mediamoderatie, niet alleen voor notities en profielen.

## Beveiligings- en vertrouwensmodel

Reports zijn signalen, geen vonnissen. Clients kunnen ze wegen op basis van sociaal vertrouwen, moderatielijsten of expliciete moderatorrollen. Relays kunnen ze ook lezen, maar de specificatie waarschuwt tegen volledig automatische moderatie omdat reports makkelijk te manipuleren zijn.

Aanvullende classificatie kan worden toegevoegd met NIP-32 `l`- en `L`-tags, wat nuttig is wanneer een client een fijnmaziger moderatievocabulaire wil dan de zeven basisrapporttypes.

---

**Primaire bronnen:**
- [NIP-56-specificatie](https://github.com/nostr-protocol/nips/blob/master/56.md)

**Vermeld in:**
- [Nieuwsbrief #10: Projectupdates](/en/newsletters/2026-02-18-newsletter/#notedeck-android-app-store-prep)

**Zie ook:**
- [NIP-22: Commentaar](/nl/topics/nip-22/)
