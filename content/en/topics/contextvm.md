---
title: "ContextVM"
date: 2026-02-25
draft: false
categories:
  - Infrastructure
  - AI
  - Protocol
---

ContextVM is a protocol built on MCP (Model Context Protocol) that enables servers and clients to use Nostr as their transports, enabling them to communicate remotely and in a permissionless way, with no domains, no OAuth, nor port forwarding involved.

## How It Works

The ContextVM SDK provides TypeScript client and server transports for MCP over Nostr. Developers can expose MCP servers across the Nostr network and clients can connect to them. Relays act like a blind message bus, just routing encrypted events blindly. Clients without native Nostr support connect through a proxy layer. The library handles relay management and cryptographic signing for event authentication.

## Components

**SDK**: TypeScript library with client/server transports, proxy support, and gateway functionality for bridging local MCP servers to Nostr.

**CVMI**: Command-line interface for server discovery and method invocation.

**Relatr**: Trust scoring service calculating personalized scores from social graph distance and profile validation.

---

**Primary sources:**
- [ContextVM Website](https://contextvm.org)
- [ContextVM SDK](https://github.com/ContextVM/sdk)
- [CVMI CLI](https://github.com/ContextVM/cvmi)
- [Relatr](https://github.com/ContextVM/relatr)

**Mentioned in:**
- [Newsletter #11: ContextVM News](/en/newsletters/2026-02-25-newsletter/#contextvm-mcp-over-nostr)

**See also:**
- [NIP-90: Data Vending Machines](/en/topics/nip-90/)
