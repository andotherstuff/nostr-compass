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

The authentication flow begins when a relay sends an `AUTH` message to the client. This message contains a challenge string that the client must sign. The client creates a kind 22242 authentication event containing the challenge and signs it with their private key. The relay verifies the signature and challenge, then grants access.

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

The challenge prevents replay attacks. The relay URL in the tags prevents the same signed event from being reused across different relays.

## Protocol Notes

Authentication is connection-scoped. A challenge stays valid for the duration of the connection, or until the relay sends a new one. The signed event is ephemeral and must not be broadcast as a normal event.

The spec also defines machine-readable error prefixes. `auth-required:` means the client has not authenticated yet. `restricted:` means it did authenticate, but that pubkey still lacks permission for the requested action.

## Use Cases

Paid relays use NIP-42 to verify subscribers before granting access. Private relays use it to limit reads or writes to approved pubkeys. It also improves rate limiting because relays can track behavior per authenticated key instead of per IP address.

Combined with [NIP-11](/en/topics/nip-11/) metadata, clients can discover whether a relay supports NIP-42 before attempting protected queries. In practice, support is still uneven, so clients need a fallback path when a relay advertises NIP-42 but handles protected events incorrectly.

---

**Primary sources:**
- [NIP-42 Specification](https://github.com/nostr-protocol/nips/blob/master/42.md) - Authentication of clients to relays

**Mentioned in:**
- [Newsletter #6: Relay Information Documents](/en/newsletters/2026-01-21-newsletter/#relay-information-documents-get-formalized)
- [Newsletter #9: Marmot Relay Status Testing](/en/newsletters/2026-02-11-newsletter/#nip-70-relay-support-critical-for-encrypted-messaging-security)
- [Newsletter #10: Nostr MCP Server](/en/newsletters/2026-02-18-newsletter/#nostr-mcp-server)

**See also:**
- [NIP-11: Relay Information Document](/en/topics/nip-11/)
- [NIP-50: Search Capability](/en/topics/nip-50/)
