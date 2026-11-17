---
title: "Noise Protocol Framework"
date: 2026-11-18
draft: false
categories: ["NIPs"]
---

The Noise Protocol Framework (revision 34, 2018-07-11) builds cryptographic protocols from Diffie-Hellman handshake patterns. In its interactive XX pattern, both parties send their static keys and can authenticate each other. Applications choose the pattern and the cryptographic functions, and they are responsible for authenticating how keys bind to identities. Noise does not define Nostr relay routing or application permissions.

Open pull request [#2544](https://github.com/nostr-protocol/nips/pull/2544) proposes rebuilding NIP-BE, the Bluetooth Low Energy transport for Nostr, on Noise XX with a fresh static key for each handshake. Advertisements expose only the service, and comparing a six-digit pairing code is optional. A modified mutual NIP-42 exchange authenticates both sides. After that, NIP-01 and NIP-77 messages flow in both directions. Devices that have met before recognize each other through per-session tags, and no advertisement carries a permanent identity. Blob range requests may include optional Bao/BLAKE3 proofs. An optional L2CAP channel shares the Noise session and can fall back to GATT. Reaching backgrounded iOS devices depends on Android devices connecting to Apple overflow advertisements and discovering services. The pull request also proposes dropping NIP-BE's `unrecommended` label; that change is not approved. The author plans to use the design in next-dipity. Deployment, test results, benchmarks and an independent privacy audit are not established in the reviewed evidence.

**Primary sources:**
- [Noise Protocol Framework, revision 34](https://noiseprotocol.org/noise_rev34.html)
- [NIPs PR #2544: NIP-BE rewrite](https://github.com/nostr-protocol/nips/pull/2544)

**Mentioned in:**
- [Newsletter #49](/en/newsletters/2026-11-18-newsletter/#nostr-protocol-nips-2544)

**See also:**
- [NIP-BE: Bluetooth Low Energy](/en/topics/nip-be/)
- [NIP-42: Client authentication](/en/topics/nip-42/)
- [NIP-77: Negentropy syncing](/en/topics/nip-77/)
