---
title: "NIP-33: Parameterized Replaceable Events (Addressable Events)"
date: 2026-03-11
translationOf: /en/topics/nip-33.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-33 definieerde oorspronkelijk parameterized replaceable events, een klasse events waarbij slechts één event per `(pubkey, kind, d-tag)` tuple door relays wordt bewaard. Het concept is sindsdien hernoemd naar "addressable events" en opgenomen in [NIP-01](/nl/topics/nip-01/). Het NIP-33 document verwijst nu door naar NIP-01, maar blijft een veelgebruikte referentie in codebases en documentatie.

## Hoe Het Werkt

Een addressable event gebruikt een kind in het bereik `30000-39999`. Elk event draagt een `d` tag waarvan de waarde, samen met de pubkey van de auteur en het kindnummer, een uniek adres vormt. Wanneer een relay een nieuw event ontvangt dat overeenkomt met een bestaande `(pubkey, kind, d-tag)` tuple, vervangt het het oudere event door het nieuwere (op basis van `created_at`). Dit maakt addressable events nuttig voor veranderlijke status: profielen, instellingen, appconfiguraties, advertenties en vergelijkbare structuren waar alleen de laatste versie belangrijk is.

Clients refereren naar addressable events met `a` tags in het formaat `<kind>:<pubkey>:<d-tag>`, optioneel gevolgd door een relayhint.

## Veelvoorkomend Gebruik

- Kind `30023` long-form artikelen
- Kind `30078` app-specifieke data (gebruikt door NIP-78)
- Kind `31923` kalendergebeurtenissen (NIP-52)
- Kind `31990` handleraanbevelingen (NIP-89)
- Kind `30009` badgedefinities (NIP-58)
- Kind `31991` agent run-configuraties (Notedeck Agentium)

## Relatie met NIP-01

NIP-33 werd samengevoegd met NIP-01 als onderdeel van een consolidatie-inspanning. De NIP-01 specificatie definieert nu drie eventretentiecategorieën: reguliere events (ongewijzigd bewaard), replaceable events (één per `(pubkey, kind)`) en addressable events (één per `(pubkey, kind, d-tag)`). NIP-33 blijft een geldige afkorting voor het addressable-eventconcept.

---

**Primaire bronnen:**
- [NIP-33 (redirect)](https://github.com/nostr-protocol/nips/blob/master/33.md)
- [NIP-01 Specificatie](https://github.com/nostr-protocol/nips/blob/master/01.md) - Addressable events sectie

**Vermeld in:**
- [Newsletter #13: Notedeck](/en/newsletters/2026-03-11-newsletter/#notedeck-adds-nip-11-relay-limits-and-agentium-features)

**Zie ook:**
- [NIP-01: Basic Protocol](/nl/topics/nip-01/)
