---
title: "NIP-73: Externe content-ID's"
date: 2026-02-04
translationOf: /en/topics/nip-73.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Discovery
  - Metadata
---

NIP-73 definieert een standaardmanier om binnen Nostr events naar externe content te verwijzen. Het gebruikt `i` tags voor de identifier zelf en `k` tags voor het type identifier, zodat clients discussie kunnen groeperen rond hetzelfde boek, dezelfde website, podcastaflevering, locatie, hashtag of blockchainobject.

## Hoe het werkt

Een event dat NIP-73 gebruikt bevat een `i` tag met een genormaliseerde externe identifier en een `k` tag die beschrijft om wat voor soort identifier het gaat. Clients kunnen daarna alle events opvragen die naar hetzelfde onderwerp verwijzen.

```json
{
  "tags": [
    ["i", "isbn:9780765382030"],
    ["k", "isbn"]
  ]
}
```

De specificatie beschrijft verschillende identifierfamilies, waaronder:

- genormaliseerde web-URL's zonder fragment
- ISBN's voor boeken
- ISAN's voor films
- geohashes en ISO 3166 land- of deelgebiedcodes
- podcast feed-, episode- en publisher-GUID's
- hashtags
- blockchain-transactie- en adresidentifiers

## Normalisatieregels

Het belangrijkste detail voor lezers in NIP-73 is normalisatie. Hetzelfde onderwerp moet naar een canonieke string verwijzen, anders splitsen clients de discussie op over meerdere identifiers die in de praktijk hetzelfde betekenen.

Voorbeelden uit de specificatie:

- geohashes gebruiken `geo:<value>` en moeten lowercase zijn
- land- en deelgebiedcodes gebruiken `iso3166:<code>` en moeten uppercase zijn
- ISBN's laten koppeltekens weg
- web-URL's verwijderen fragmenten
- blockchain-transactiehashes gebruiken lowercase hex

Dat lijkt klein, maar het bepaalt het verschil tussen een gedeeld gesprek en meerdere niet-compatibele indexen.

## Nuttige patronen

NIP-73 is een algemene referentielaag, geen contentformaat. Een long-form note kan naar een boek-ISBN verwijzen, een recensie kan naar een film-ISAN verwijzen, en een lokale post kan naar een geohash of landcode verwijzen zonder telkens een custom tag te moeten verzinnen.

De specificatie staat ook een optionele URL-hint toe als tweede waarde van een `i` tag. Dat geeft clients een fallback-link wanneer ze geen custom renderer hebben voor dat type identifier.

## Waarom het belangrijk is

Nostr heeft al sterke interne verwijzingen voor events en profielen. NIP-73 breidt dat idee uit naar zaken buiten Nostr. Zodra identifiers genormaliseerd zijn, kunnen opmerkingen, beoordelingen, highlights en trusted assertions allemaal aan hetzelfde externe onderwerp worden gekoppeld over verschillende clients heen.

Dit is ook waarom NIP-85 voortbouwt op NIP-73. Trusted Assertions kunnen niet alleen gebruikers en events beoordelen, maar ook NIP-73 identifiers zoals boeken, websites, hashtags en locaties.

---

**Primaire bronnen:**
- [NIP-73-specificatie](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - Voegt ISO 3166 land- en deelgebiedcodes toe

**Vermeld in:**
- [Nieuwsbrief #8: NIP Updates](/en/newsletters/2026-02-04-newsletter/#nip-updates)
- [Nieuwsbrief #10: NIP-85 Deep Dive](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)

**Zie ook:**
- [NIP-85: Trusted Assertions](/nl/topics/nip-85/)
