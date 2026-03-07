---
title: "ContextVM"
date: 2026-02-25
draft: false
categories:
  - Infrastructure
  - AI
  - Protocol
---

ContextVM is a protocol and toolchain for transporting MCP (Model Context Protocol) traffic over Nostr. It lets MCP clients and servers find each other and exchange signed messages without depending on a central registry, domains, or OAuth.

## How It Works

The ContextVM SDK provides TypeScript client and server transports for MCP over Nostr. Existing MCP servers can stay on their normal transports while a gateway exposes them to Nostr, and clients without native Nostr support can connect through a proxy layer.

Relays act as a message bus. They route events, while signing and encryption give endpoints authentication and transport privacy.

## Components

**SDK**: TypeScript library with client/server transports, proxy support, and gateway functionality for bridging local MCP servers to Nostr.

**CVMI**: Command-line interface for server discovery and method invocation.

**Relatr**: Trust scoring service calculating personalized scores from social graph distance and profile validation.

## Why It Matters

ContextVM is a transport bridge, not a replacement for MCP itself. That matters because it lowers adoption cost: an existing MCP server can gain Nostr reachability without rewriting its tool schema or business logic.

Recent ContextVM work also pushed ephemeral delivery for gift-wrapped traffic. That is useful for tool calls and intermediate responses where durable relay storage is unnecessary and can create extra privacy exposure.

## Interop Notes

In February and March 2026, the project moved from implementation toward standardization. The team opened NIP proposals for MCP JSON-RPC over Nostr and for an ephemeral variant of gift wrap. Even if those proposals change, they show the protocol boundary more clearly: MCP stays the application layer, Nostr handles discovery and transport.

---

**Primary sources:**
- [ContextVM Website](https://contextvm.org)
- [ContextVM SDK](https://github.com/ContextVM/sdk)
- [CVMI CLI](https://github.com/ContextVM/cvmi)
- [Relatr](https://github.com/ContextVM/relatr)
- [NIP PR #2245: Ephemeral Gift Wrap](https://github.com/nostr-protocol/nips/pull/2245)
- [NIP PR #2246: MCP JSON-RPC over Nostr](https://github.com/nostr-protocol/nips/pull/2246)

**Mentioned in:**
- [Newsletter #11: ContextVM News](/en/newsletters/2026-02-25-newsletter/#contextvm-mcp-over-nostr)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**See also:**
- [NIP-90: Data Vending Machines](/en/topics/nip-90/)
