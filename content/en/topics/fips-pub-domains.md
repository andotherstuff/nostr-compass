---
title: "FIPS Public Domains"
date: 2026-09-30
draft: false
categories:
  - Protocol
  - Networking
  - Identity
---

fips-pub-domains is an early implementation for resolving familiar Internet domain names to [FIPS](/en/topics/fips/) mesh services. It publishes signed Nostr claims, but a signature proves only who made a claim. A client must also check DNS or DNSSEC evidence, a trusted witness, or a previously pinned binding before treating the claimant as the domain owner.

## Verification and offline use

The [first release](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.1.0) added the claim, resolver daemon, and Android integration. [Version 0.2.0](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.0) can attach a DNSSEC proof to a claim, allowing a client that sees only a mesh relay to verify a previously unseen signed domain against the DNS root keys. It also supports more than one verified server for a domain. [Version 0.2.1](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.1) fixed the packaged server unit and changed it to run without root; existing installations need the replacement unit.

The project's [test notes](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md) describe two-node and mesh-only relay cases. They are maintainer-reported tests, not evidence of a wider deployment. Its [NIP-DB proposal](https://github.com/nostr-protocol/nips/pull/2487) is open, and its draft event-kind numbers are placeholders rather than assigned Nostr kinds.

---

**Primary sources:**
- [Repository and README](https://github.com/fr34aky/fips-pub-domains)
- [Releases 0.1.0–0.2.1](https://github.com/fr34aky/fips-pub-domains/releases)
- [Proposed NIP-DB](https://github.com/nostr-protocol/nips/pull/2487)
- [Testing notes](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)

**Mentioned in:**
- [Newsletter #42: fips-pub-domains](/en/newsletters/2026-09-30-newsletter/#fips-pub-domains-tests-signed-public-names-for-a-mesh)

**See also:**
- [FIPS](/en/topics/fips/)
