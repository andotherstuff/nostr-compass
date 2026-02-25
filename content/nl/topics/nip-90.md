---
title: "NIP-90"
date: 2026-02-25
translationOf: /en/topics/nip-90.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - DVM
---

NIP-90 definieert Data Vending Machines (DVM's), een marktplaatsprotocol voor het aanvragen en betalen van rekenwerk op Nostr.

## Hoe Het Werkt

Clients publiceren jobaanvraag-events (kinds 5000-5999) die het benodigde werk specificeren. Serviceproviders monitoren op aanvragen die passen bij hun mogelijkheden en publiceren resultaten na het voltooien van de berekening. Betaling verloopt via Lightning of andere mechanismen die in de jobflow worden onderhandeld.

Job-kinds definieren verschillende berekeningstypen: tekstgeneratie, beeldgeneratie, vertaling, inhoudsontdekking, en meer. Elke kind specificeert het verwachte invoer-/uitvoerformaat.

## Kernfuncties

- Gedecentraliseerde rekenmarktplaats
- Op kind gebaseerd jobtypesysteem
- Providerconcurrentie op prijs en kwaliteit
- Uitbreidbaar voor nieuwe berekeningstypen

---

**Primaire bronnen:**
- [NIP-90 Specificatie](https://github.com/nostr-protocol/nips/blob/master/90.md)

**Vermeld in:**
- [Newsletter #11: NIP-AC DVM Agent Coordination](/nl/newsletters/2026-02-25-newsletter/#nip-updates)

**Zie ook:**
- [NIP-85: Trusted Assertions](/nl/topics/nip-85/)
