---
title: "NIP-65: Relay List Metadata"
date: 2026-01-13
draft: false
categories:
  - Protocol
  - Discovery
---

NIP-65 defines kind 10002 events that advertise which relays a user prefers for reading and writing. This metadata helps other users and clients locate your content across the distributed relay network, enabling the "outbox model" that distributes load and improves censorship resistance.

## Structure

A relay list is a replaceable event (kind 10002) containing `r` tags for each relay the user wants to advertise. The event replaces any previous relay list from the same pubkey.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 10002,
  "tags": [
    ["r", "wss://relay.damus.io", "read"],
    ["r", "wss://nos.lol"],
    ["r", "wss://relay.nostr.band", "write"]
  ],
  "content": "",
  "sig": "sig1234..."
}
```

Each `r` tag contains a relay WebSocket URL and an optional marker indicating how the user interacts with that relay. The `read` marker means the user consumes events from this relay, so others should publish there to reach the user. The `write` marker means the user publishes to this relay, so others should subscribe there to see the user's content. Omitting the marker indicates both read and write.

The `content` field is empty for relay list events.

## The Outbox Model

NIP-65 enables a decentralized content distribution pattern called the "outbox model." Rather than everyone publishing to and reading from the same central relays, users publish to their own preferred relays and clients dynamically discover where to find each user's content.

When Alice wants to find Bob's posts, her client first fetches Bob's kind 10002 event from any relay that has it. She then extracts the relays Bob marked for `write` since those are where he publishes. Her client subscribes to those relays for Bob's events. When Alice wants to send Bob a direct message, her client looks for his `read` relays instead and publishes the message there.

Clients following the outbox model maintain connections to relays listed in their followed users' NIP-65 events. As they discover new accounts, they dynamically connect to new relays. Relays that appear in multiple followed users' lists get prioritized since connecting to them serves more of the user's social graph.

This architecture improves censorship resistance because no single relay needs to store or serve everyone's content. If one relay goes offline or blocks a user, their content remains available on their other listed relays.

## Relationship to Relay Hints

NIP-65 complements the relay hints found throughout other NIPs. When you tag someone with `["p", "pubkey", "wss://hint.relay"]`, the hint tells clients where to look for that specific reference. NIP-65 provides the authoritative, user-controlled list of preferred relays, while hints offer shortcuts embedded in individual events for faster discovery.

## Best Practices

Keep your relay list current since stale entries pointing to defunct relays make you harder to find. Include at least two or three relays for redundancy so that if one relay goes offline, your content remains accessible through the others.

Avoid listing too many relays. When you list ten or fifteen relays, every client that wants to fetch your content must connect to all of them, slowing down their experience and increasing load across the network. A focused list of three to five well-chosen relays serves you better than an exhaustive list that burdens everyone who follows you.

Mix general-purpose relays with any specialized relays you use. For instance, you might list a popular general relay like `wss://relay.damus.io`, a relay focused on your geographic region, and a relay for a specific community you participate in.

---

**Primary sources:**
- [NIP-65 Specification](https://github.com/nostr-protocol/nips/blob/master/65.md)

**Mentioned in:**
- [Newsletter #5: NIP Deep Dive](/en/newsletters/2026-01-13-newsletter/#nip-65-relay-list-metadata)

**See also:**
- [NIP-11: Relay Information](/en/topics/nip-11/)
