---
title: "NIP-52: Calendar Events"
date: 2026-01-28
translationOf: /en/topics/nip-52.md
translationDate: 2026-04-22
draft: false
categories:
  - NIP
  - Calendar
  - Events
---

NIP-52 definieert kalenderevenementen, kalenders en RSVP's op Nostr. Het geeft clients een standaardmanier om tijdgebonden of datumgebonden evenementen te publiceren zonder voor elke app een eigen eventmodel te verzinnen.

## Event Kinds

### Kind 31922: Datumgebaseerd kalenderevenement

Gebruik kind `31922` voor eendaagse of meerdaagse evenementen waarbij kloktijd niet van belang is.

```json
{
  "kind": 31922,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Nostr Meetup"],
    ["start", "2026-02-15"],
    ["end", "2026-02-16"],
    ["location", "Austin, TX"]
  ]
}
```

### Kind 31923: Tijdgebaseerd kalenderevenement

Gebruik kind `31923` voor evenementen met exacte begin- en eindtijden.

```json
{
  "kind": 31923,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Weekly Call"],
    ["start", "1706900400"],
    ["end", "1706904000"],
    ["D", "19755"],
    ["start_tzid", "America/New_York"]
  ]
}
```

Tijdgebaseerde evenementen vereisen ook een of meer `D` tags, die elk de Unix timestamp op dagniveau bevatten voor de dagen die het evenement beslaat. Die tag bestaat zodat relays en clients per dag kunnen indexeren zonder elke volledige timestamp te hoeven parseren.

## Kalender- en RSVP-ondersteuning

Kind `31924` is een kalender, een adresseerbare lijst van kalenderevenementen. Kind `31925` is een RSVP die met een `a` tag terugwijst naar een specifiek kalenderevenement en optioneel met een `e` tag naar een specifieke revisie.

Kind `31925` events laten gebruikers reageren met:

- `accepted` - Zal aanwezig zijn
- `declined` - Zal niet aanwezig zijn
- `tentative` - Is mogelijk aanwezig

RSVP's kunnen ook `fb`-waarden van `free` of `busy` bevatten, wat planningscontext toevoegt naast aanwezigheidsstatus.

## Implementatienotities

- **Adresseerbaar**: Evenementen en kalenders kunnen worden bijgewerkt zonder duplicaten te maken
- **Tijdzone-ondersteuning**: Tijdgebaseerde evenementen kunnen IANA-tijdzone-identifiers gebruiken
- **Locatiegegevens**: Tags kunnen leesbare locaties, links en geohashes bevatten
- **Samenwerkingsverzoeken**: Auteurs van evenementen kunnen opname in iemands kalender aanvragen door die te taggen

Terugkerende evenementen vallen bewust buiten scope. De specificatie schuift herhalingsregels door naar clients, wat relay-side indexering eenvoudig houdt en de gebruikelijke kalenderproblemen rond zomertijdwisselingen en uitzonderingen vermijdt.

## Why It Matters

NIP-52 doet meer dan een bijeenkomst beschrijven. Het scheidt eventdefinitie, kalenderlidmaatschap en reacties van deelnemers in verschillende event kinds. Daardoor kan de ene app een evenement publiceren, een andere kalenders aggregeren en een derde RSVP-status beheren zonder dat alle drie dezelfde backend delen.

---

**Primaire bronnen:**
- [NIP-52 Specification](https://github.com/nostr-protocol/nips/blob/master/52.md)
- [PR #1752: Day-Granularity Timestamp Tag](https://github.com/nostr-protocol/nips/pull/1752)

**Vermeld in:**
- [Newsletter #7: Notedeck Calendar App Draft](/nl/newsletters/2026-01-28-newsletter/)
- [Newsletter #10: NIP Updates](/nl/newsletters/2026-02-18-newsletter/)
- [Newsletter #10: NIP Deep Dive](/nl/newsletters/2026-02-18-newsletter/)
- [Newsletter #13: Calendar by Form* v0.2.0](/en/newsletters/2026-03-11-newsletter/)

**Zie ook:**
- [NIP-22: Comment](/nl/topics/nip-22/)
- [NIP-51: Lists](/nl/topics/nip-51/)
