---
title: "NIP-52: Kalenderevents"
date: 2026-01-28
translationOf: /en/topics/nip-52.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Calendar
  - Events
---

NIP-52 definieert event kinds voor kalenderfunctionaliteit op Nostr, wat planning, RSVP's en eventcoördinatie mogelijk maakt.

## Event Kinds

### Kind 31922: Datumgebaseerd Kalenderevent
Voor events die een of meerdere dagen beslaan zonder specifieke tijden:

```json
{
  "kind": 31922,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Nostr Meetup"],
    ["start", "2026-02-15"],
    ["end", "2026-02-15"],
    ["location", "Austin, TX"]
  ]
}
```

### Kind 31923: Tijdgebaseerd Kalenderevent
Voor events met specifieke start- en eindtijden:

```json
{
  "kind": 31923,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Wekelijkse Call"],
    ["start", "1706900400"],
    ["end", "1706904000"],
    ["start_tzid", "America/New_York"]
  ]
}
```

## RSVP-Ondersteuning

Kind 31925 events stellen gebruikers in staat om te reageren op kalenderevents:

- `accepted` - Zal deelnemen
- `declined` - Zal niet deelnemen
- `tentative` - Misschien deelnemen

## Kenmerken

- **Adresseerbaar**: Events kunnen worden bijgewerkt zonder duplicaten te creëren
- **Tijdzone-ondersteuning**: Correcte afhandeling van tijdzones via IANA-identifiers
- **Locatie**: Fysieke of virtuele vergaderlocaties
- **Herhaling**: Ondersteuning voor terugkerende events (voorgestelde uitbreiding)

## Gerelateerd

- [NIP-22](/nl/topics/nip-22/) - Reacties (voor kalenderevent-discussies)
- [NIP-51](/nl/topics/nip-51/) - Lijsten (voor kalenderverzamelingen)
