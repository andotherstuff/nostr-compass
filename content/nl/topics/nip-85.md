---
title: "NIP-85"
date: 2026-02-18
translationOf: /en/topics/nip-85.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - Trust
  - Infrastructure
---

NIP-85 definieert Trusted Assertions, een systeem voor het delegeren van dure berekeningen aan vertrouwde serviceproviders die ondertekende resultaten publiceren als Nostr-events.

## Hoe Het Werkt

Web of Trust-scores, engagementmetrics en andere berekende waarden vereisen het crawlen van veel relays en het verwerken van grote eventvolumes. Dit werk is onpraktisch op mobiele apparaten. NIP-85 laat gespecialiseerde providers deze berekeningen uitvoeren en resultaten publiceren die clients kunnen opvragen.

Serviceproviders adverteren hun mogelijkheden via kind 30085-events. Clients ontdekken providers door deze aankondigingen op te vragen bij relays van pubkeys die de gebruiker al volgt of vertrouwt. Resultaten komen als kind 30382-events ondertekend door de provider.

## Kernfuncties

- Gedelegeerde berekening voor resource-intensieve metrics
- Providerontdekking via de sociale graaf
- Ondertekende assertions voor verifieerbare resultaten
- Client-side vertrouwensbeslissingen

---

**Primaire bronnen:**
- [NIP-85 Specificatie](https://github.com/nostr-protocol/nips/blob/master/85.md)

**Vermeld in:**
- [Newsletter #10: NIP-85 Deep Dive](/nl/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [Newsletter #11: NIP-85 Vindbaarheid Serviceproviders](/nl/newsletters/2026-02-25-newsletter/#nip-updates)

**Zie ook:**
- [Web of Trust](/nl/topics/web-of-trust/)
