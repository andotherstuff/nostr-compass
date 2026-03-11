---
title: "NIP-33: Parameterized Replaceable Events (Addressable Events)"
date: 2026-03-11
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-33 originally defined parameterized replaceable events, a class of events where only one event per `(pubkey, kind, d-tag)` tuple is retained by relays. The concept has since been renamed to "addressable events" and folded into [NIP-01](/en/topics/nip-01/). The NIP-33 document now redirects to NIP-01 but remains a common reference in codebases and documentation.

## How It Works

An addressable event uses a kind in the range `30000-39999`. Each event carries a `d` tag whose value, together with the author's pubkey and the kind number, forms a unique address. When a relay receives a new event matching an existing `(pubkey, kind, d-tag)` tuple, it replaces the older event with the newer one (by `created_at`). This makes addressable events useful for mutable state: profiles, settings, app configurations, classified listings, and similar structures where only the latest version matters.

Clients reference addressable events with `a` tags in the format `<kind>:<pubkey>:<d-tag>`, optionally followed by a relay hint.

## Common Uses

- Kind `30023` long-form articles
- Kind `30078` app-specific data (used by NIP-78)
- Kind `31923` calendar events (NIP-52)
- Kind `31990` handler recommendations (NIP-89)
- Kind `30009` badge definitions (NIP-58)
- Kind `31991` agent run configurations (Notedeck Agentium)

## Relationship to NIP-01

NIP-33 was merged into NIP-01 as part of a consolidation effort. The NIP-01 spec now defines three event retention categories: regular events (kept as-is), replaceable events (one per `(pubkey, kind)`), and addressable events (one per `(pubkey, kind, d-tag)`). NIP-33 remains a valid shorthand for the addressable-event concept.

---

**Primary sources:**
- [NIP-33 (redirect)](https://github.com/nostr-protocol/nips/blob/master/33.md)
- [NIP-01 Specification](https://github.com/nostr-protocol/nips/blob/master/01.md) - Addressable events section

**Mentioned in:**
- [Newsletter #13: Notedeck](/en/newsletters/2026-03-11-newsletter/#notedeck-adds-nip-11-relay-limits-and-agentium-features)

**See also:**
- [NIP-01: Basic Protocol](/en/topics/nip-01/)
