---
title: "NIP-52: Calendar Events"
date: 2026-01-28
draft: false
categories:
  - NIP
  - Calendar
  - Events
---

NIP-52 defines calendar events, calendars, and RSVPs on Nostr. It gives clients a standard way to publish time-based or date-based events without inventing a custom event model for every app.

## Event Kinds

### Kind 31922: Date-Based Calendar Event

Use kind `31922` for all-day or multi-day events where clock time does not matter.

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

Use kind `31923` for events with precise start and end times.

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

Time-based events also require one or more `D` tags, each containing the day-granularity Unix timestamp for the days the event spans. That tag exists so relays and clients can index by day without parsing every full timestamp.

## Calendar and RSVP Support

Kind `31924` is a calendar, an addressable list of calendar events. Kind `31925` is an RSVP that points back to a specific calendar event with an `a` tag and optionally to a specific revision with an `e` tag.

Kind `31925` events allow users to respond with:

- `accepted` - Will attend
- `declined` - Will not attend
- `tentative` - May attend

RSVPs can also include `fb` values of `free` or `busy`, which adds scheduling context beyond attendance status.

## Implementation Notes

- **Addressable**: Events and calendars can be updated without creating duplicates
- **Timezone support**: Time-based events can use IANA timezone identifiers
- **Location data**: Tags can include human-readable locations, links, and geohashes
- **Collaborative requests**: Event authors can request inclusion in someone else's calendar by tagging it

Recurring events are intentionally out of scope. The spec pushes recurrence rules to clients, which keeps relay-side indexing simple and avoids the usual calendar edge cases around daylight saving changes and exceptions.

## Why It Matters

NIP-52 does more than describe a meeting. It separates event definition, calendar membership, and attendee responses into different event kinds. That makes it possible for one app to publish an event, another to aggregate calendars, and a third to manage RSVP state without all three sharing the same backend.

---

**Primary sources:**
- [NIP-52 Specification](https://github.com/nostr-protocol/nips/blob/master/52.md)
- [PR #1752: Day-Granularity Timestamp Tag](https://github.com/nostr-protocol/nips/pull/1752)

**Mentioned in:**
- [Newsletter #7: Notedeck Calendar App Draft](/en/newsletters/2026-01-28-newsletter/#notedeck-progress-calendar-app-and-ux-polish)
- [Newsletter #10: NIP Updates](/en/newsletters/2026-02-18-newsletter/#nip-updates)
- [Newsletter #10: NIP Deep Dive](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-52-calendar-events)
- [Newsletter #13: Calendar by Form* v0.2.0](/en/newsletters/2026-03-11-newsletter/#calendar-by-form-v020)

**See also:**
- [NIP-22: Comment](/en/topics/nip-22/)
- [NIP-51: Lists](/en/topics/nip-51/)
