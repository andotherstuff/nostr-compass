---
title: "NIP-52: Calendar Events"
date: 2026-01-28
draft: false
categories:
  - NIP
  - Calendar
  - Events
---

NIP-52 defines event kinds for calendar functionality on Nostr, enabling scheduling, RSVPs, and event coordination.

## Event Kinds

### Kind 31922: Date-Based Calendar Event
For events spanning one or more days without specific times:

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

### Kind 31923: Time-Based Calendar Event
For events with specific start and end times:

```json
{
  "kind": 31923,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Weekly Call"],
    ["start", "1706900400"],
    ["end", "1706904000"],
    ["start_tzid", "America/New_York"]
  ]
}
```

## RSVP Support

Kind 31925 events allow users to respond to calendar events:

- `accepted` - Will attend
- `declined` - Will not attend
- `tentative` - May attend

## Features

- **Addressable**: Events can be updated without creating duplicates
- **Timezone Support**: Proper handling of time zones via IANA identifiers
- **Location**: Physical or virtual meeting locations
- **Recurrence**: Support for recurring events (proposed extension)

## Related

- [NIP-22](/en/topics/nip-22/) - Comments (for calendar event discussions)
- [NIP-51](/en/topics/nip-51/) - Lists (for calendar collections)
