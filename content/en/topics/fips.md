---
title: "FIPS"
date: 2026-02-25
draft: false
categories:
  - Protocol
  - Networking
  - Infrastructure
---

FIPS (Free Internetworking Peering System) is a self-organizing mesh networking protocol that uses Nostr-style secp256k1 keypairs as node identities.

## How It Works

FIPS aims to make peer networking work without central servers or certificate authorities. Nodes discover neighbors, build routing state, and forward packets using only local knowledge.

The design combines a spanning tree with bloom filter reachability data. Each node gets coordinates relative to the tree, then routes greedily toward the destination. If greedy routing fails, the tree still provides a fallback path.

Two encryption layers protect traffic. Link-layer encryption (Noise IK pattern) secures hop-by-hop communication between neighbors. Session-layer encryption (Noise XK pattern) provides end-to-end protection against intermediate routers.

## Why It Matters

FIPS reuses the same key model Nostr developers already understand, but applies it to packet routing instead of social events. That gives it a simple identity story: the network identity is the cryptographic key, not an IP allocation or certificate chain.

The transport-agnostic design is also important. The same routing and identity model can, in principle, run over UDP, Ethernet, Bluetooth, or LoRa, which makes FIPS interesting for hostile or unreliable network environments.

## Implementation Status

As covered in Compass, the current Rust implementation already includes working UDP transport and bloom-filter-based discovery. Relay-based bootstrapping is still future work, so today the protocol is more a networking substrate than a finished Nostr relay replacement.

---

**Primary sources:**
- [FIPS Repository](https://github.com/jmcorgan/fips)
- [Design Documentation](https://github.com/jmcorgan/fips/blob/master/docs/design/fips-intro.md)

**Mentioned in:**
- [Newsletter #11: FIPS News](/en/newsletters/2026-02-25-newsletter/#fips-nostr-native-mesh-networking)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**See also:**
- [Marmot Protocol](/en/topics/marmot/)
