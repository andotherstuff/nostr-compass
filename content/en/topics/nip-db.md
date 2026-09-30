---
title: "Proposed NIP-DB: Domain Service Bindings"
date: 2026-09-30
draft: false
categories:
  - Proposals
  - Networking
  - Identity
---

NIP-DB is an **open proposal** for binding an ordinary Internet domain to a key-addressed service. Its event kinds and wording remain subject to review; this page does not present it as an accepted Nostr specification.

## Verification model

A serving key can publish a signed claim naming the domain and service. The proposal describes optional DNS or DNSSEC evidence, witness attestations, and a zone record for names under the domain. A signature proves which key published a claim but does not prove control of the domain. A client must verify the binding with DNS evidence, a trusted witness, or a previously pinned key before using it to resolve a name.

[fips-pub-domains](/en/topics/fips-pub-domains/) is the author's reference implementation for the FIPS mesh. Its documented two-node and mesh-only tests are maintainer-reported implementation evidence. They do not settle the proposal's open review or establish wider deployment.

---

**Primary sources:**
- [Open NIP-DB pull request](https://github.com/nostr-protocol/nips/pull/2487)
- [Author's draft and event-kind placeholders](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/nip.md)
- [Reference implementation and tests](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)

**Mentioned in:**
- [Newsletter #42: public domains](/en/newsletters/2026-09-30-newsletter/#fips-pub-domains-tests-signed-public-names-for-a-mesh)
- [Newsletter #42: proposed NIP-DB](/en/newsletters/2026-09-30-newsletter/#nip-db-proposes-verified-domain-names-for-key-addressed-services)
