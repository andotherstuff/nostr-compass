---
title: "NIP-52: Kalenderereignisse"
date: 2026-01-28
translationOf: /en/topics/nip-52.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Calendar
  - Events
---

NIP-52 definiert Event-Arten für Kalenderfunktionalität auf Nostr und ermöglicht Terminplanung, RSVPs und Ereigniskoordination.

## Event-Arten

### Kind 31922: Datumsbasiertes Kalenderereignis
Für Ereignisse, die einen oder mehrere Tage ohne spezifische Zeiten umfassen:

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

### Kind 31923: Zeitbasiertes Kalenderereignis
Für Ereignisse mit spezifischen Start- und Endzeiten:

```json
{
  "kind": 31923,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Wöchentlicher Call"],
    ["start", "1706900400"],
    ["end", "1706904000"],
    ["start_tzid", "America/New_York"]
  ]
}
```

## RSVP-Unterstützung

Kind 31925 Events ermöglichen Benutzern, auf Kalenderereignisse zu antworten:

- `accepted` - Wird teilnehmen
- `declined` - Wird nicht teilnehmen
- `tentative` - Nimmt möglicherweise teil

## Funktionen

- **Adressierbar**: Events können ohne Duplikate aktualisiert werden
- **Zeitzonen-Unterstützung**: Ordnungsgemäße Handhabung von Zeitzonen über IANA-Identifikatoren
- **Ort**: Physische oder virtuelle Treffpunkte
- **Wiederholung**: Unterstützung für wiederkehrende Ereignisse (vorgeschlagene Erweiterung)

## Verwandt

- [NIP-22](/de/topics/nip-22/) - Kommentare (für Kalenderereignis-Diskussionen)
- [NIP-51](/de/topics/nip-51/) - Listen (für Kalendersammlungen)
