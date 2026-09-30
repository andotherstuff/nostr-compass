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

The Rust implementation includes UDP transport and bloom-filter-based discovery. [fips2go 0.7.0](https://github.com/fr34aky/fips2go/releases/tag/v0.7.0) added optional Nostr-announced peer discovery and fallback bootstrap peers. [fips-pub-domains](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.1) is testing Nostr-signed public-domain claims, DNSSEC proofs, and mesh-only lookups. These are application and naming integrations; they do not make FIPS a Nostr relay replacement.

---

**Primary sources:**
- [FIPS Repository](https://github.com/jmcorgan/fips)
- [Design Documentation](https://github.com/jmcorgan/fips/blob/master/docs/design/fips-intro.md)
- [fips2go 0.7.0 release](https://github.com/fr34aky/fips2go/releases/tag/v0.7.0)
- [fips-pub-domains 0.2.1 release](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.1)

**Mentioned in:**
- [Newsletter #11: FIPS News](/en/newsletters/2026-02-25-newsletter/#fips-nostr-native-mesh-networking)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)
- [Newsletter #32: News](/en/newsletters/2026-07-22-newsletter/#the-iris-projects-ship-a-pubsub-library-a-browser-fips-runtime-and-a-social-graph-20-in-one-week)
- [Newsletter #41: FIPS mesh updates](/en/newsletters/2026-09-23-newsletter/#fips2go-070-keeps-the-mesh-connected-through-bootstrap-failures)
- [Newsletter #42: public-domain bindings](/en/newsletters/2026-09-30-newsletter/#fips-pub-domains-tests-signed-public-names-for-a-mesh)

**See also:**
- [Marmot Protocol](/en/topics/marmot/)
