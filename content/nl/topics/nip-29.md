---
title: "NIP-29: Relay-gebaseerde Groepen"
date: 2025-12-24
draft: false
categories:
  - Sociaal
  - Groepen
---

NIP-29 definieert relay-gebaseerde groepen, waarbij een relay groepslidmaatschap, permissies en berichtzichtbaarheid beheert.

## Groepstoegang Tags

- **private**: Alleen leden kunnen groepsberichten lezen
- **closed**: Join-verzoeken worden genegeerd (alleen op uitnodiging)
- **hidden**: Relay verbergt groepsmetadata voor niet-leden, waardoor de groep niet ontdekt kan worden
- **restricted**: Alleen leden kunnen berichten naar de groep schrijven

Deze tags kunnen worden gecombineerd. Een groep kan `restricted` zijn (schrijfbeperkt) maar niet `hidden` (nog steeds vindbaar). Het weglaten van een tag maakt het tegenovergestelde gedrag mogelijk: geen `private` betekent dat iedereen kan lezen, geen `closed` betekent dat join-verzoeken worden gehonoreerd.

## Hoe Het Werkt

De relay is de autoriteit voor groepsbewerkingen:
- Onderhoudt ledenlijst en rollen
- Handhaaft schrijfpermissies
- Controleert wat niet-leden kunnen zien

Clients sturen groepsberichten naar de relay, die lidmaatschap valideert voordat ze worden geaccepteerd.

## Privacyoverwegingen

- `hidden` groepen bieden de sterkste vindbaarheidsbeveiliging: ze verschijnen niet in zoekopdrachten of relay-lijsten
- `private` groepen verbergen berichtinhoud voor niet-leden
- `closed` groepen negeren simpelweg join-verzoeken; combineer met `private` of `hidden` voor sterkere toegangscontrole
- `restricted` controleert wie kan schrijven, onafhankelijk van leestoegang

---

**Primaire bronnen:**
- [NIP-29 Specificatie](https://github.com/nostr-protocol/nips/blob/master/29.md)

**Vermeld in:**
- [Nieuwsbrief #2: NIP Updates](/nl/newsletters/2025-12-24-newsletter/#nip-updates)
