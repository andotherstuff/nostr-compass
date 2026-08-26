---
title: "NIP-25: Reacties"
date: 2026-07-29
translationOf: /en/topics/nip-25.md
translationDate: 2026-08-26
draft: false
categories:
  - Protocol
  - Social
---

NIP-25 definieert reacties als kind `7`-events. Het geeft clients een gedeelde eventvorm om een emoji of andere korte reactie te hangen aan een note, artikel, advertentie of ander gerefereerd event.

## Hoe het werkt

Een reactie-event draagt zijn reactietekst in `content` en refereert het doel via de `e`-tag van het doelevent. Wanneer het doel adresseerbaar is, bevat de reactie ook de `a`-tag ervan. Ze bevat verder `p`-tags voor de auteur van het gerefereerde event, waardoor relays en clients meldingen kunnen routeren zonder de ontvangers uit de eventcontent te moeten afleiden.

De standaardreactie is `+`, dus clients kunnen lege reactiecontent opvatten als een positief antwoord. Andere emoji zijn geldige reactiewaarden. De specificatie staat ook `-` toe voor een negatieve reactie, die de aanvulling van juli 2022 toevoegde na de oorspronkelijke introductie.

Clients zouden de doelreferentie en de auteurstags moeten bewaren bij het maken van een reactie. Een reactie is een gewoon ondertekend event, dus ze kan via normale relay-subscriptions reizen en worden weergegeven door elke client die kind `7` herkent.

## Implementaties

NIP-25 is breed geïmplementeerd door Nostr-clients en -bibliotheken als deel van gewone interactie met notes. Het eenvoudige model van kind en tags laat clients aantallen, individuele reacties en meldingen tonen zonder een apart transportprotocol.

---

**Primaire bronnen:**
- [NIP-25 Specification](https://github.com/nostr-protocol/nips/blob/master/25.md)
- [Introductiecommit](https://github.com/nostr-protocol/nips/commit/dcbd504639d20d1b0ae6bb837609710645781b88)
- [Aanvulling over downvotes](https://github.com/nostr-protocol/nips/commit/89bb08ba8683)

**Vermeld in:**
- [Newsletter #33: Zes jaar Nostr in juli](/nl/newsletters/2026-07-29-newsletter/#zes-jaar-nostr-in-juli)
- [Newsletter #37: Marmot](/nl/newsletters/2026-08-26-newsletter/#marmot)

**Zie ook:**
- [NIP-01: Basic Protocol](/nl/topics/nip-01/)
- [NIP-10: Text Note Threading](/nl/topics/nip-10/)
