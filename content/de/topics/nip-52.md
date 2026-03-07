---
title: "NIP-52: Kalenderereignisse"
date: 2026-01-28
translationOf: /en/topics/nip-52.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Calendar
  - Events
---

NIP-52 definiert Kalenderereignisse, Kalender und RSVPs auf Nostr. Es gibt Clients einen Standardweg, zeitbasierte oder datumsbasierte Ereignisse zu veroffentlichen, ohne fur jede App ein eigenes Event-Modell zu erfinden.

## Event-Kinds

### Kind 31922: Datumsbasiertes Kalenderereignis

Verwende Kind `31922` fur ganztagige oder mehrtagige Ereignisse, bei denen die genaue Uhrzeit keine Rolle spielt.

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

### Kind 31923: Zeitbasiertes Kalenderereignis

Verwende Kind `31923` fur Ereignisse mit genauen Start- und Endzeiten.

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

Zeitbasierte Ereignisse brauchen auBerdem ein oder mehrere `D`-Tags, die jeweils den Unix-Timestamp auf Tagesebene fur die Tage enthalten, uber die sich das Ereignis erstreckt. Dieses Tag existiert, damit Relays und Clients nach Tagen indexieren konnen, ohne jeden vollstandigen Timestamp zu parsen.

## Kalender- und RSVP-Unterstutzung

Kind `31924` ist ein Kalender, also eine adressierbare Liste von Kalenderereignissen. Kind `31925` ist ein RSVP, das mit einem `a`-Tag auf ein bestimmtes Kalenderereignis verweist und optional mit einem `e`-Tag auf eine konkrete Revision.

Events vom Kind `31925` erlauben Nutzern Antworten mit:

- `accepted` - Wird teilnehmen
- `declined` - Wird nicht teilnehmen
- `tentative` - Nimmt vielleicht teil

RSVPs konnen auch `fb`-Werte von `free` oder `busy` enthalten. Das liefert zusatzlichen Planungs-Kontext uber den reinen Teilnahme-Status hinaus.

## Implementierungshinweise

- **Addressable**: Ereignisse und Kalender konnen aktualisiert werden, ohne Duplikate zu erzeugen
- **Timezone support**: Zeitbasierte Ereignisse konnen IANA-Zeitzonenbezeichner verwenden
- **Location data**: Tags konnen menschenlesbare Orte, Links und Geohashes enthalten
- **Collaborative requests**: Autoren konnen um Aufnahme in den Kalender anderer bitten, indem sie ihn taggen

Wiederkehrende Ereignisse sind bewusst nicht Teil des Scopes. Die Spezifikation uberlasst Wiederholungsregeln den Clients. Das halt die Indexierung auf Relay-Seite einfach und vermeidet die ublichen Kalender-Randfalle rund um Sommerzeit-Wechsel und Ausnahmen.

## Warum es wichtig ist

NIP-52 beschreibt mehr als nur ein Treffen. Es trennt Ereignisdefinition, Kalender-Mitgliedschaft und Teilnehmerantworten in unterschiedliche Event-Kinds. So kann eine App ein Ereignis veroffentlichen, eine andere Kalender aggregieren und eine dritte den RSVP-Status verwalten, ohne dass alle drei dasselbe Backend teilen mussen.

---

**Primarquellen:**
- [NIP-52 Specification](https://github.com/nostr-protocol/nips/blob/master/52.md)
- [PR #1752: Day-Granularity Timestamp Tag](https://github.com/nostr-protocol/nips/pull/1752)

**Erwahnt in:**
- [Newsletter #7: Notedeck Calendar App Draft](/en/newsletters/2026-01-28-newsletter/#notedeck-progress-calendar-app-and-ux-polish)
- [Newsletter #10: NIP Updates](/en/newsletters/2026-02-18-newsletter/#nip-updates)
- [Newsletter #10: NIP Deep Dive](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-52-calendar-events)

**Siehe auch:**
- [NIP-22: Comment](/de/topics/nip-22/)
- [NIP-51: Lists](/de/topics/nip-51/)
