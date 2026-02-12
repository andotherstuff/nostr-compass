---
title: "NIP-96: HTTP-Bestandsopslag"
date: 2026-02-11
translationOf: /en/topics/nip-96.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Media
---

NIP-96 definieerde hoe Nostr-toepassingen bestanden uploaden, downloaden en beheren op HTTP-mediaservers. Nu gemarkeerd als "afgeraden" ten gunste van Blossom, blijft NIP-96 relevant terwijl projecten de overgang tussen de twee mediastandaarden doorlopen.

## Werking

Toepassingen ontdekken de mogelijkheden van bestandsserver door `/.well-known/nostr/nip96.json` op te halen, wat de API-URL, ondersteunde contenttypes, groottelimieten en beschikbare mediatransformaties retourneert.

Voor uploads stuurt de toepassing `multipart/form-data` POST naar de API-URL met NIP-98 autorisatieheader (ondertekend Nostr event dat de identiteit van de uploader bewijst). De server retourneert NIP-94 bestandsmetadatastructuur met de bestands-URL, SHA-256-hashes, MIME-type en afmetingen.

Downloads gebruiken GET-verzoeken naar `<api_url>/<sha256-hash>`, met optionele queryparameters voor serverside transformaties zoals beeldverkleining. Verwijdering gebruikt DELETE met NIP-98 auth. Met kind 10096 events geven mensen hun voorkeur-uploadservers aan.

## Reden voor Afkeuring

NIP-96 koppelde bestands-URL's aan specifieke servers. Viel een server uit, dan verloor elke Nostr-notitie die naar die server verwees zijn media. Blossom keert dat om door de SHA-256-hash van de bestandsinhoud tot canonieke identifier te maken. Elke Blossom-server die hetzelfde bestand host serveert het op hetzelfde hashpad, waardoor content standaard draagbaar is over servers.

Blossom vereenvoudigt ook de API: plain PUT voor uploads, GET voor downloads en ondertekende Nostr events (geen HTTP-headers) voor autorisatie. De afkeuring vond plaats in september 2025 met [PR #2047](https://github.com/nostr-protocol/nips/pull/2047).

## De Transitie

Servers als nostr.build en void.cat ondersteunden NIP-96 en hebben Blossom-endpoints toegevoegd of zijn ernaar gemigreerd. Toepassingen bevinden zich in verschillende stadia: Angor v0.2.5 voegde NIP-96-serverconfiguratie toe, terwijl ZSP v0.3.1 exclusief naar Blossom-servers uploadt. De co-existentie zal voortduren totdat overgebleven NIP-96-implementaties hun migratie voltooien.

Kind 10096 servervoorkeur-events blijven nuttig voor Blossom-serverselectie. NIP-94 bestandsmetadata (kind 1063 events) beschrijft bestandseigenschappen ongeacht welk uploadprotocol ze heeft aangemaakt.

---

**Primaire bronnen:**
- [NIP-96: HTTP File Storage](https://github.com/nostr-protocol/nips/blob/master/96.md)
- [PR #2047: Mark NIP-96 as Unrecommended](https://github.com/nostr-protocol/nips/pull/2047)

**Vermeld in:**
- [Nieuwsbrief #9: NIP Deep Dive](/nl/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-96-http-bestandsopslag-en-de-transitie-naar-blossom)

**Zie ook:**
- [Blossom Protocol](/nl/topics/blossom/)
- [NIP-94: Bestandsmetadata](/nl/topics/nip-94/)
