---
title: "FIPS"
date: 2026-02-25
draft: false
categories:
  - Protocol
  - Networking
  - Infrastructure
---

FIPS (Free Internetworking Peering System) is a self-organizing mesh network protocol that uses Nostr keypairs (secp256k1) as node identities.

## How It Works

FIPS enables infrastructure-independent networking where nodes discover each other automatically without central servers or certificate authorities. The protocol uses a spanning tree for coordinate-based routing while bloom filters propagate reachability information, letting nodes make forwarding decisions with only local knowledge.

Two encryption layers protect traffic. Link-layer encryption (Noise IK pattern) secures hop-by-hop communication between neighbors. Session-layer encryption (Noise XK pattern) provides end-to-end protection against intermediate routers.

## Key Features

- Nostr keypairs as node identities
- Transport agnostic (UDP, Ethernet, Bluetooth, LoRa radio)
- Dual-layer Noise protocol encryption
- Greedy embedding spanning tree routing
- Bloom filter reachability propagation

---

**Primary sources:**
- [FIPS Repository](https://github.com/jmcorgan/fips)
- [Design Documentation](https://github.com/jmcorgan/fips/blob/master/docs/design/fips-intro.md)

**Mentioned in:**
- [Newsletter #11: FIPS News](/en/newsletters/2026-02-25-newsletter/#fips-nostr-native-mesh-networking)

**See also:**
- [Marmot Protocol](/en/topics/marmot/)
