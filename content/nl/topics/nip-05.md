---
title: "NIP-05: Domeinverificatie"
date: 2026-02-04
translationDate: 2026-03-07
translationOf: /en/topics/nip-05.md
draft: false
categories:
  - Identity
  - Discovery
---

NIP-05 koppelt Nostr public keys aan menselijk leesbare internet-identifiers zoals `user@example.com`. Het geeft gebruikers een door DNS ondersteunde identiteitsaanduiding die clients via HTTPS kunnen verifiëren.

## Hoe het werkt

Een gebruiker claimt een identifier door een `nip05`-veld toe te voegen aan zijn profielmetadata. De identifier volgt het formaat `name@domain`. Clients verifiëren de claim door `https://domain/.well-known/nostr.json` op te halen en te controleren of de naam overeenkomt met de pubkey van de gebruiker.

Het JSON-bestand op het well-known-pad bevat een `names`-object dat lokale namen koppelt aan hex pubkeys:

```json
{
  "names": {
    "alice": "abc123...",
    "bob": "def456..."
  }
}
```

Wanneer verificatie slaagt, kunnen clients de identifier tonen in plaats van of naast de npub. Sommige clients tonen een verificatie-indicator, terwijl andere de identifier als platte tekst tonen en de vertrouwensbeslissing aan de lezer overlaten.

## Vertrouwensmodel

NIP-05 is geen wereldwijd username-register. Het bewijst controle over een domeinnaam en een webserverpad, niet de juridische identiteit of langdurige continuïteit van een account. Als een domeineigenaar de koppeling later wijzigt, verifiëren clients de nieuwe koppeling tenzij ze eerdere status bewaren.

Dat maakt NIP-05 nuttig voor vindbaarheid en reputatie, maar zwakker dan gebruikers vaak aannemen. Een goede client zou het moeten behandelen als geverifieerde domeincontrole, niet als bewijs dat een persoon of organisatie werkelijk is wie die beweert te zijn.

## Relay hints

Het `nostr.json`-bestand kan optioneel een `relays`-object bevatten dat pubkeys koppelt aan arrays met relay-URL's. Dit helpt clients te ontdekken waar ze events van een bepaalde gebruiker kunnen vinden.

## Interop-opmerkingen

De lowercase-vereiste is belangrijker dan ze lijkt. Namen of pubkeys met gemengde hoofdletters en kleine letters kunnen in de ene implementatie werken en in de andere falen, dus clients moeten uitgaan van lowercase-namen en lowercase hex keys in `nostr.json`.

Een ander praktisch detail is de speciale naam `_`, waarmee een domein de kale identifier-vorm zoals `_@example.com` of alleen `example.com` kan koppelen in clients die dat ondersteunen. Niet elke client behandelt die vorm op dezelfde manier, dus gebruikers krijgen nog steeds de meest consistente resultaten met expliciete `name@domain`-identifiers.

## Implementatiestatus

De meeste grote clients ondersteunen NIP-05-verificatie:
- Damus, Amethyst en Primal tonen geverifieerde identifiers
- Veel relay-services bieden NIP-05-identifiers als feature
- Er bestaan veel gratis en betaalde NIP-05-providers

---

**Primaire bronnen:**
- [NIP-05 Specification](https://github.com/nostr-protocol/nips/blob/master/05.md)
- [PR #2208](https://github.com/nostr-protocol/nips/pull/2208) - lowercase-vereiste voor namen en hex keys

**Vermeld in:**
- [Newsletter #8: NIP Updates](/en/newsletters/2026-02-04-newsletter/#nip-updates)

**Zie ook:**
- [NIP-01: Basic Protocol](/nl/topics/nip-01/)
- [NIP-65: Relay List Metadata](/nl/topics/nip-65/)
