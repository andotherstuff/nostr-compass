---
title: "NIP-78: App-Specific Data"
date: 2026-05-14
draft: false
categories:
  - NIPs
  - Data Storage
---

NIP-78 defines a standard event kind for applications to store arbitrary data on behalf of a user using Nostr events, enabling cross-device state sync without a centralized server.

## How It Works

The core event kind is 30078, a parameterized replaceable event. The `d` tag is an application-defined identifier string that scopes the storage slot to a specific application and purpose.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1747180800,
  "kind": 30078,
  "tags": [
    ["d", "myapp-settings"]
  ],
  "content": "{\"theme\":\"dark\",\"fontSize\":14}",
  "sig": "<128-char hex>"
}
```

An application publishes a 30078 event with a unique `d` tag (for example `tamagostrich-pet-state` or `amethyst-settings`) and whatever JSON or text content it needs to persist. Because 30078 is replaceable and scoped by `d` tag, updating stored state means publishing a new event with the same `d` tag — the relay retains only the latest version.

## Cross-Device Sync

Any client that knows a user's public key and the application's `d` tag can fetch the current state from the user's relay set and reconstruct it on any device. The user owns the data because it lives in events signed by their keypair, stored on relays from their [NIP-65](/en/topics/nip-65/) relay list.

## Private vs Public Data

For private application data, the content field can be encrypted using [NIP-44](/en/topics/nip-44/) before publishing, so the relay stores ciphertext only the key holder can decrypt. Public application data can be stored unencrypted so other clients can read and display it.

## Content Format

NIP-78 deliberately leaves the content format open — applications choose their own schema. The common convention is to prefix `d` tags with the application name to prevent collision across apps using the same relay.

## Implementations

- [Tamagostrich](https://github.com/Negr087/tamagostrich) — pet state sync across devices via `tamagostrich-pet-state` kind:30078 events
- [Wisp](https://github.com/barrydeen/wisp-android) — kind:30078 wallet backup and cross-device security settings sync; outbox subscriptions merged into a single REQ using NIP-78 author filter
- [NosPress](https://github.com/nostrapps/nospress) — CMS orchestration state stored in NIP-78 events
- Several Nostr client settings sync implementations (Amethyst, others)

---

**Primary sources:**
- [NIP-78 Specification](https://github.com/nostr-protocol/nips/blob/master/78.md)
- [Tamagostrich](https://github.com/Negr087/tamagostrich) — production implementation

**Mentioned in:**
- [Newsletter #22: NIP-78 Deep Dive](/en/newsletters/2026-05-14-newsletter/#nip-deep-dive-nip-78-app-specific-data)
- [Newsletter #22: Tamagostrich](/en/newsletters/2026-05-14-newsletter/#tamagostrich-launches-a-decentralized-nip-78-tamagotchi-with-sats-rewards)

**See also:**
- [NIP-51: Lists](/en/topics/nip-51/)
- [NIP-44: Versioned Encryption](/en/topics/nip-44/)
- [NIP-65: Relay List Metadata](/en/topics/nip-65/)
