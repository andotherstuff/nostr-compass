---
title: "Trusted Relay Assertions"
date: 2026-01-21
draft: false
categories:
  - Protocol
  - Relays
---

Trusted Relay Assertions is a draft NIP proposal for standardizing relay trust scoring and reputation management. The specification introduces kind 30385 events where assertion providers publish trust scores computed from observed metrics, operator reputation, and user reports.

## How It Works

The proposal fills a gap in the relay ecosystem. While [NIP-11](/en/topics/nip-11/) defines what relays claim about themselves and [NIP-66](/en/topics/nip-66/) measures what we observe, Trusted Relay Assertions standardizes what we conclude about relay trustworthiness.

Assertion providers compute scores across three dimensions. Reliability measures availability, recovery speed, consistency, and latency. Quality evaluates policy documentation, TLS security, and operator accountability. Accessibility assesses access barriers, jurisdiction freedom, and surveillance risk. An overall trust score (0-100) combines these components with weights: 40% reliability, 35% quality, 25% accessibility.

Each assertion includes confidence levels (low, medium, high) based on observation counts. Operator verification uses multiple methods: cryptographic proof via signed NIP-11 documents, DNS TXT records, or .well-known files. The spec integrates Web of Trust through operator trust scores. Policy classification helps users find appropriate relays: open, moderated, curated, or specialized.

Users declare trusted assertion providers via kind 10385 events. Clients query multiple providers and compare scores. The proposal includes an appeals process where relay operators can dispute scores using [NIP-32](/en/topics/nip-32/) labeling events.

## Use Cases

For [NIP-46](/en/topics/nip-46/) remote signers, trust assertions help users evaluate unfamiliar relays embedded in connection URIs before accepting connections. Combined with [NIP-65](/en/topics/nip-65/) relay lists, clients can make informed relay selection decisions based on both user preferences and third-party trust evaluations.

The specification complements existing relay discovery mechanisms. [NIP-66](/en/topics/nip-66/) provides discovery (what exists), this proposal adds evaluation (what's good). Together they enable informed relay selection rather than relying on hardcoded defaults or word-of-mouth recommendations.

---

**Primary sources:**
- [Draft NIP Document](https://nostr.com/nevent1qqsqjymvcp6ch3ps3fqsxljf6j8u3adz64ucw8npnzuj3cn6dekn0gspz9mhxue69uhkummnw3ezumrpdejz7qg3waehxw309ahx7um5wgh8w6twv5hsyga3qg) - Kind 30817 event proposing the specification

**Mentioned in:**
- [Newsletter #6: News](/en/newsletters/2026-01-21-newsletter/#trusted-relay-assertions-a-new-approach-to-relay-trust)
- [Newsletter #6: NIP Updates](/en/newsletters/2026-01-21-newsletter/#nip-updates)

**See also:**
- [NIP-11: Relay Information Document](/en/topics/nip-11/)
- [NIP-66: Relay Discovery and Liveness Monitoring](/en/topics/nip-66/)
- [NIP-32: Labeling](/en/topics/nip-32/)
