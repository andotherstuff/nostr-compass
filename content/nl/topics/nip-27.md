---
title: "NIP-27 (Tekstnotitiereferenties)"
date: 2026-02-04
description: "NIP-27 definieert hoe profielen, notities en andere entiteiten gerefereerd worden binnen notitie-inhoud met het nostr: URI-schema."
---

NIP-27 specificeert hoe referenties naar Nostr-entiteiten worden ingebed in de inhoud van tekstnotities. Referenties gebruiken het `nostr:` URI-schema gevolgd door een bech32-gecodeerde identifier (npub, note, nevent, nprofile, naddr).

## Hoe Het Werkt

Bij het opstellen van een notitie die een andere gebruiker vermeldt of naar een ander event verwijst, wordt de referentie direct in de inhoud ingebed:

```
Bekijk deze post van nostr:npub1... over nostr:note1...
```

Clients parsen deze referenties en renderen ze gepast, meestal als klikbare links of inline profielkaarten. De gerefereerde entiteiten worden ook toegevoegd aan de tags van het event voor indexering en notificatiedoeleinden.

De NIP behandelt ook hashtag-parsing. Tags voorafgegaan door `#` worden ge-extract en toegevoegd aan de `t` tags van het event voor doorzoekbaarheid.

## Referentietypes

- `nostr:npub1...` - Referentie naar een gebruikersprofiel
- `nostr:note1...` - Referentie naar een specifiek notitie-event
- `nostr:nevent1...` - Referentie naar een event met relay hints
- `nostr:nprofile1...` - Referentie naar een profiel met relay hints
- `nostr:naddr1...` - Referentie naar een adresseerbaar event

## Implementaties

Alle grote Nostr clients implementeren NIP-27:
- Tekstparsers extraheren referenties tijdens het opstellen
- Renderers tonen referenties als interactieve elementen
- Notificatiesystemen gebruiken de bijbehorende tags

## Primaire Bronnen

- [NIP-27 Specificatie](https://github.com/nostr-protocol/nips/blob/master/27.md)
- [NIP-19 (Bech32 Gecodeerde Entiteiten)](/nl/topics/nip-19/) - Definieert de coderingsformaten gebruikt in referenties

## Vermeld In

- [Nieuwsbrief #8 (2026-02-04)](/nl/newsletters/2026-02-04-newsletter/) - nostr-tools fix voor hashtag-parsing na newlines
