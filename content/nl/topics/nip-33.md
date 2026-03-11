---
title: "NIP-33: Geparametriseerde vervangbare events (adresseerbare events)"
date: 2026-03-11
translationOf: /en/topics/nip-33.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-33 definieerde oorspronkelijk geparametriseerde vervangbare events, een klasse events waarbij relays slechts een event per tuple `(pubkey, kind, d-tag)` bewaren. Het concept is sindsdien hernoemd naar "adresseerbare events" en opgenomen in [NIP-01](/nl/topics/nip-01/). Het NIP-33-document verwijst nu door naar NIP-01, maar blijft een gangbare referentie in codebases en documentatie.

## Hoe het werkt

Een adresseerbaar event gebruikt een kind in het bereik `30000-39999`. Elk event bevat een `d` tag waarvan de waarde, samen met de pubkey van de auteur en het kind-nummer, een uniek adres vormt. Wanneer een relay een nieuw event ontvangt dat overeenkomt met een bestaande tuple `(pubkey, kind, d-tag)`, vervangt het het oudere event door het nieuwere event op basis van `created_at`. Daardoor zijn adresseerbare events bruikbaar voor wijzigbare status: profielen, instellingen, appconfiguraties, rubrieksadvertenties en vergelijkbare structuren waarbij alleen de laatste versie telt.

Clients verwijzen naar adresseerbare events met `a` tags in het formaat `<kind>:<pubkey>:<d-tag>`, optioneel gevolgd door een relay hint.

## Veelvoorkomende toepassingen

- Kind `30023` long-form artikelen
- Kind `30078` app-specifieke data (gebruikt door NIP-78)
- Kind `31923` kalendergebeurtenissen (NIP-52)
- Kind `31990` handleraanbevelingen (NIP-89)
- Kind `30009` badgedefinities (NIP-58)
- Kind `31991` agent-runconfiguraties (Notedeck Agentium)

## Relatie met NIP-01

NIP-33 werd in NIP-01 opgenomen als onderdeel van een consolidatie. De NIP-01-specificatie definieert nu drie bewaarcategorieen voor events: reguliere events (blijven ongewijzigd), vervangbare events (een per `(pubkey, kind)`) en adresseerbare events (een per `(pubkey, kind, d-tag)`). NIP-33 blijft een geldige korte aanduiding voor het concept van adresseerbare events.

---

**Primaire bronnen:**
- [NIP-33 (doorverwijzing)](https://github.com/nostr-protocol/nips/blob/master/33.md)
- [NIP-01-specificatie](https://github.com/nostr-protocol/nips/blob/master/01.md) - sectie over adresseerbare events

**Vermeld in:**
- [Nieuwsbrief #13: Notedeck](/nl/newsletters/2026-03-11-newsletter/#notedeck-adds-nip-11-relay-limits-and-agentium-features)

**Zie ook:**
- [NIP-01: Basisprotocol](/nl/topics/nip-01/)
