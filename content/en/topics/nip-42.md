---
title: "NIP-42: Authentication of clients to relays"
date: 2026-01-21
draft: false
categories:
  - NIPs
  - Authentication
---

NIP-42 defines how clients authenticate to relays. Relays can require authentication to provide access control, prevent abuse, or implement paid relay services.

## How It Works

The authentication flow begins when a relay sends an AUTH message to the client. This message contains a challenge string that the client must sign. The client creates a kind 22242 authentication event containing the challenge and signs it with their private key. The relay verifies the signature and challenge, then grants access.

```json
{
  "kind": 22242,
  "tags": [
    ["relay", "wss://relay.example.com"],
    ["challenge", "random-challenge-string"]
  ],
  "content": "",
  "pubkey": "<client_pubkey>",
  "created_at": 1736784000,
  "sig": "<signature>"
}
```

The challenge prevents replay attacks: clients must sign fresh challenges for each authentication attempt. The relay URL in the tags ensures authentication tokens cannot be reused across different relays.

## Use Cases

Paid relays use NIP-42 to verify subscribers before granting access. After authenticating, relays can check payment status or subscription expiration. Private relays restrict access to approved pubkeys, creating closed communities or personal relay infrastructure.

Rate limiting becomes more effective with authentication. Relays can track request rates per authenticated pubkey rather than per IP address, preventing abuse while supporting legitimate users behind shared IPs. Spam prevention improves when relays require authentication for publishing events.

Some relays use NIP-42 for analytics, tracking which users access which content without requiring centralized accounts. Combined with [NIP-11](/en/topics/nip-11/) metadata, clients discover whether relays require authentication before attempting connections.

---

**Primary sources:**
- [NIP-42 Specification](https://github.com/nostr-protocol/nips/blob/master/42.md) - Authentication of clients to relays

**See also:**
- [NIP-11: Relay Information Document](/en/topics/nip-11/)
- [NIP-50: Search Capability](/en/topics/nip-50/)
