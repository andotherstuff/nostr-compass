---
title: "NIP-89: Recommended Application Handlers"
date: 2026-01-07
draft: false
categories:
  - Discovery
  - Clients
  - Protocol
---

NIP-89 defines how applications can announce their capabilities and how users can recommend apps that handle specific event kinds.

## Event Kinds

- **kind 31990** - Application handler (published by app developers)
- **kind 31989** - App recommendation (published by users)

## How It Works

1. **Applications** publish handler events describing which event kinds they support and how to open content
2. **Users** recommend apps they use for specific event kinds
3. **Clients** query recommendations to offer "open in..." functionality for unknown event types

## Application Handler

```json
{
  "id": "<event-id>",
  "pubkey": "<app-developer-pubkey>",
  "created_at": 1736200000,
  "kind": 31990,
  "tags": [
    ["d", "<app-identifier>"],
    ["k", "30023"],
    ["web", "https://app.example.com/a/<bech32>", "naddr"],
    ["ios", "appname://open/<bech32>"]
  ],
  "content": "{\"name\": \"My App\", \"picture\": \"...\"}",
  "sig": "<signature>"
}
```

The `k` tags specify supported event kinds. URL templates use `<bech32>` as a placeholder for NIP-19 encoded entities.

The same handler event can advertise several supported kinds if they share the same routing pattern. That keeps app discovery compact and avoids publishing one handler event per kind when the destination logic is identical.

## User Recommendation

```json
{
  "id": "<event-id>",
  "pubkey": "<user-pubkey>",
  "created_at": 1736200000,
  "kind": 31989,
  "tags": [
    ["d", "30023"],
    ["a", "31990:app-pubkey:identifier", "wss://relay", "web"]
  ],
  "content": "",
  "sig": "<signature>"
}
```

The `d` tag is the event kind being recommended. Multiple `a` tags can recommend different apps for different platforms.

## Client Tag

NIP-89 also defines an optional `client` tag that publishing apps can attach to ordinary events. It records the client name plus a pointer to the handler event, which lets other clients show where a note came from or look up richer application metadata.

This has privacy implications. The spec explicitly says clients should let users opt out, because publishing software identity on every event can reveal usage patterns people may not want to expose.

## Use Cases

- Discovering apps that can display longform articles (kind 30023)
- Finding clients that support specific event types
- Cross-client "open in..." functionality
- Detecting client capabilities for encryption support

## Trust and Safety Notes

NIP-89 improves interoperability, but it also creates a redirect surface. If a client queries arbitrary handler announcements from untrusted relays, it can end up sending users to malicious or misleading applications.

That is why the recommendation flow starts with people you follow. Socially filtered recommendations are not perfect, but they are safer than treating every published handler as equally trustworthy.

---

**Primary sources:**
- [NIP-89 Specification](https://github.com/nostr-protocol/nips/blob/master/89.md)

**Mentioned in:**
- [Newsletter #4: NIP Deep Dive](/en/newsletters/2026-01-07-newsletter/#nip-44-versioned-encryption)
- [Newsletter #12: Damus](/en/newsletters/2026-03-04-newsletter/#damus-nip-89-recommended-application-handlers)

**See also:**
- [NIP-19: Bech32-Encoded Entities](/en/topics/nip-19/)
