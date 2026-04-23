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

NIP-52 definiert Calendar Events, Kalender und RSVPs auf Nostr. Es gibt Clients einen Standardweg, zeitbasierte oder datumsbasierte Events zu veröffentlichen, ohne für jede App ein eigenes Event-Modell zu erfinden.

## Event Kinds

### Kind 31922: Date-Based Calendar Event

Verwende kind `31922` für ganztägige oder mehrtägige Events, bei denen die genaue Uhrzeit keine Rolle spielt.

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

### Kind 31923: Time-Based Calendar Event

Verwende kind `31923` für Events mit präzisen Start- und Endzeiten.

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

Zeitbasierte Events brauchen außerdem ein oder mehrere `D`-Tags, die jeweils den Unix-Timestamp auf Tagesebene für die Tage enthalten, über die sich das Event erstreckt. Dieses Tag existiert, damit Relays und Clients nach Tagen indexieren können, ohne jeden vollständigen Timestamp zu parsen.

## Calendar and RSVP Support

Kind `31924` ist ein Kalender, also eine addressable Liste von Calendar Events. Kind `31925` ist ein RSVP, das mit einem `a`-Tag auf ein bestimmtes Calendar Event verweist und optional mit einem `e`-Tag auf eine konkrete Revision.

Kind-`31925`-Events erlauben Nutzern Antworten mit:

- `accepted` - wird teilnehmen
- `declined` - wird nicht teilnehmen
- `tentative` - nimmt vielleicht teil

RSVPs können außerdem `fb`-Werte von `free` oder `busy` enthalten. Das liefert zusätzlichen Planungskontext über den reinen Teilnahmestatus hinaus.

## Implementierungshinweise

- **Addressable**: Events und Kalender können aktualisiert werden, ohne Duplikate zu erzeugen
- **Timezone support**: Zeitbasierte Events können IANA-Zeitzonenbezeichner nutzen
- **Location data**: Tags können menschenlesbare Orte, Links und Geohashes enthalten
- **Collaborative requests**: Event-Autoren können um Aufnahme in den Kalender anderer bitten, indem sie ihn taggen

Wiederkehrende Events sind bewusst nicht Teil des Scopes. Die Spezifikation überlässt Recurrence Rules den Clients. Das hält die Indexierung auf Relay-Seite einfach und vermeidet die üblichen Kalender-Randfälle rund um Sommerzeitwechsel und Ausnahmen.

## Warum das wichtig ist

NIP-52 beschreibt mehr als nur ein Treffen. Es trennt Event-Definition, Kalender-Mitgliedschaft und Teilnehmerantworten in unterschiedliche Event-Kinds. So kann eine App ein Event veröffentlichen, eine andere Kalender aggregieren und eine dritte den RSVP-Status verwalten, ohne dass alle drei dasselbe Backend teilen müssen.

---

**Primärquellen:**
- [NIP-52 Specification](https://github.com/nostr-protocol/nips/blob/master/52.md)
- [PR #1752: Day-Granularity Timestamp Tag](https://github.com/nostr-protocol/nips/pull/1752)

**Erwähnt in:**
- [Newsletter #7: Notedeck Calendar App Draft](/de/newsletters/2026-01-28-newsletter/)
- [Newsletter #10: NIP Updates](/de/newsletters/2026-02-18-newsletter/)
- [Newsletter #10: NIP Deep Dive](/de/newsletters/2026-02-18-newsletter/)
- [Newsletter #13: Calendar by Form* v0.2.0](/en/newsletters/2026-03-11-newsletter/)

**Siehe auch:**
- [NIP-22: Comment](/de/topics/nip-22/)
- [NIP-51: Lists](/de/topics/nip-51/)
