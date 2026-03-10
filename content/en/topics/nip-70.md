---
title: "NIP-70: Protected Events"
date: 2026-03-11
draft: false
categories:
  - NIPs
  - Relay
  - Access Control
---

NIP-70 defines a way for authors to mark an event as protected with the simple tag `[["-"]]`. A protected event can be accepted only when a relay chooses to support that behavior and verifies that the authenticated publisher is the same pubkey as the event author.

## How It Works

The core rule is short. If an event contains the `[["-"]]` tag, a relay should reject it by default. A relay that wants to support protected events must first run the [NIP-42](/en/topics/nip-42/) `AUTH` flow and confirm that the client who authenticated is publishing their own event.

That makes NIP-70 a publish-authority rule, not an encryption rule. The content can still be readable. What changes is who gets to place that event on a relay that honors the tag. This lets relays support semi-closed feeds and other contexts where authors want a relay to refuse third-party republication.

```json
{
  "id": "cb8feca582979d91fe90455867b34dbf4d65e4b86e86b3c68c368ca9f9eef6f2",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1707409439,
  "kind": 1,
  "tags": [
    ["-"]
  ],
  "content": "hello members of the secret group",
  "sig": "fa163f5cfb75d77d9b6269011872ee22b34fb48d23251e9879bb1e4ccbdd8aaaf4b6dc5f5084a65ef42c52fbcde8f3178bac3ba207de827ec513a6aa39fa684c"
}
```

## AUTH Flow Implications

Protected events are useful only when relays actually enforce author identity at publish time. That is why NIP-70 depends so directly on [NIP-42](/en/topics/nip-42/). A relay that accepts `[["-"]]` events without a matching auth check is treating the tag as decoration, not policy.

## Relay Behavior and Limits

NIP-70 does not promise that content will stay contained forever. Any recipient can still copy what they see and publish a new event elsewhere. The spec only gives relays a standard way to respect the author's intent and reject direct republication of protected events.

That is why follow-up work matters. [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) extends the rule to reposts that embed protected events, closing an easy bypass where the original event stayed protected but the wrapper event did not.

## Implementations

- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - Added NIP-42 auth support for protected events
- [strfry PR #176](https://github.com/hoytech/strfry/pull/176) - Rejects reposts that embed protected events
- [SNSTR v0.3.3](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.3) - Adds helper support tied to protected-event handling

---

**Primary sources:**
- [NIP-70 Specification](https://github.com/nostr-protocol/nips/blob/master/70.md)
- [PR #1030](https://github.com/nostr-protocol/nips/pull/1030) - Added NIP-70 to the NIPs repository
- [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) - Reject reposts that embed protected events
- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - Relay implementation for NIP-42 auth and protected events

**Mentioned in:**
- [Newsletter #13: NIP Updates](/en/newsletters/2026-03-11-newsletter/#nip-updates)
- [Newsletter #13: NIP Deep Dive](/en/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-70-protected-events)

**See also:**
- [NIP-42: Client Authentication](/en/topics/nip-42/)
- [NIP-11: Relay Information Document](/en/topics/nip-11/)
