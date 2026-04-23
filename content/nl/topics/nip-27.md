---
title: "NIP-27 (Tekstnotitiereferenties)"
date: 2026-02-04
translationDate: 2026-03-07
translationOf: /en/topics/nip-27.md
draft: false
categories:
  - NIP
  - Social
---

NIP-27 specificeert hoe referenties naar Nostr-entiteiten worden ingebed in de inhoud van tekstnotities. Referenties gebruiken het `nostr:` URI-schema, gevolgd door een bech32-gecodeerde identifier (`npub`, `note`, `nevent`, `nprofile`, `naddr`).

## Hoe het werkt

Bij het opstellen van een notitie die een andere gebruiker noemt of naar een ander event verwijst, wordt de referentie direct in de inhoud opgenomen:

```
Check out this post by nostr:npub1... about nostr:note1...
```

Clients parseren deze referenties en renderen ze passend, meestal als klikbare links of inline profielkaarten. De verwezen entiteiten kunnen ook worden gespiegeld naar event tags voor indexering of notificaties, maar de specificatie laat dat optioneel.

De NIP behandelt ook hashtag-parsing. Tags met een `#`-prefix worden geëxtraheerd en toegevoegd aan de `t` tags van het event, zodat ze doorzoekbaar blijven.

## Referentietypen

- `nostr:npub1...` - Referentie naar een gebruikersprofiel
- `nostr:note1...` - Referentie naar een specifiek note event
- `nostr:nevent1...` - Referentie naar een event met relay hints
- `nostr:nprofile1...` - Referentie naar een profiel met relay hints
- `nostr:naddr1...` - Referentie naar een addressable event

## Waarom het belangrijk is

NIP-27 scheidt wat mensen lezen van wat clients opslaan. Een gebruiker kan `@name` typen in een rich composer, terwijl het gepubliceerde event nog steeds een stabiele `nostr:nprofile...`-referentie in `content` kan bevatten. Dat maakt de referentie overdraagbaar tussen clients zonder afhankelijk te zijn van de mention-syntaxis van een enkele app.

Een tweede praktisch voordeel is veerkracht. Een ruwe `nostr:nevent...` of `nostr:naddr...` die in tekst is ingebed, bevat nog steeds genoeg informatie voor een andere client om het doel te reconstrueren, zelfs als die de oorspronkelijke lokale rendering nooit heeft gezien.

## Interop-opmerkingen

- Gebruik de [NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md)-vorm in de inhoud zelf: `nostr:<bech32-id>`
- Voeg alleen `p` of `q` tags toe wanneer je client mention-notificaties of sterkere event-indexering wil
- Ga er niet van uit dat elke inline referentie een reply-relatie moet worden. De specificatie laat die keuze aan de client

---

**Primairbronnen:**

- [NIP-27 Specification](https://github.com/nostr-protocol/nips/blob/master/27.md)
- [NIP-19 (Bech32-Encoded Entities)](/nl/topics/nip-19/) - Definieert de coderingsformaten die in referenties worden gebruikt

**Vermeld in:**

- [Newsletter #8 (2026-02-04)](/en/newsletters/2026-02-04-newsletter/) - nostr-tools-fix voor hashtag-parsing na nieuwe regels

**Zie ook:**
- [NIP-18: Reposts](/nl/topics/nip-18/)
- [NIP-19: Bech32-Encoded Entities](/nl/topics/nip-19/)
