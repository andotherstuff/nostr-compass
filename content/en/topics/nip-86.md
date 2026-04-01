---
title: "NIP-86: Relay Management API"
date: 2026-04-01
draft: false
categories:
  - Relays
  - Protocol
---

NIP-86 defines a JSON-RPC interface for relay management, letting authorized clients send administrative commands to relays over a standardized API. Relay operators can ban or allow pubkeys, manage access lists, and query relay state without relay-specific tooling.

## How It Works

The management API uses JSON-RPC-like requests over HTTP on the same URI as the relay websocket endpoint. Requests use the `application/nostr+json+rpc` content type and authenticate with a [NIP-98](/en/topics/nip-98/) (HTTP Auth) signed event in the `Authorization` header. The relay verifies the requesting pubkey against its admin list before executing commands.

Available methods include banning and allowing pubkeys, listing banned users, and querying relay configuration. The standardized interface means a single client implementation can manage any NIP-86-compatible relay.

## Implementations

- [Amethyst](https://github.com/vitorpamplona/amethyst) - Android client with NIP-86 relay management UI (v1.07.0+)

---

**Primary sources:**
- [NIP-86 Specification](https://github.com/nostr-protocol/nips/blob/master/86.md)
- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - Client-side NIP-86 support
- [PR #2039](https://github.com/vitorpamplona/amethyst/pull/2039) - Relay management user search dialog

**Mentioned in:**
- [Newsletter #16: Amethyst ships relay management](/en/newsletters/2026-04-01-newsletter/#amethyst-ships-pinned-notes-relay-management-and-request-to-vanish)

**See also:**
- [NIP-11: Relay Information Document](/en/topics/nip-11/)
- [NIP-98: HTTP Auth](/en/topics/nip-98/)
- [NIP-42: Authentication of Clients to Relays](/en/topics/nip-42/)
