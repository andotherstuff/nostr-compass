---
title: "Cyberspace Protocol"
date: 2026-11-04
draft: false
categories:
  - Protocol
---

Cyberspace is a Nostr protocol for a shared 3D space, specified in the [arkin0x/cyberspace repository](https://github.com/arkin0x/cyberspace) and associated with the ONOSENDAI client. Signed Nostr events place objects in the space and record avatar movement as a chain of hops, each carrying a proof that verifiers check.

## Objects and doors

The [carried-object merge](https://github.com/arkin0x/cyberspace/commit/9210d6dff16637079c8339a9c957c60cbd3a744e) makes objects carried by an SNO object part of the parent payload. A root table resolves `a`-address placements before any relay fetch, with each entry keyed under the carrier author's key, so the root copy takes precedence over a fetched reference. A present but invalid entry yields a placeholder and does not trigger a fetch. Carried objects are sealed inside the bag, and re-publishing an object from a bag omits its table unless the user chooses otherwise.

The [doors and chest looks merge](https://github.com/arkin0x/cyberspace/commit/bd9125eea93274ee589657f0bd23203916ead40f) adds kind `3341` doors. Each door identifies one room at a specific height, and the room key derives from the location key plus a door secret. The room bag is sealed, and multiple or nested doors are supported. Rotating a lock SHOULD rotate the secret and reseal the room. A chest uses the first look tag that is well formed for its closed or open shape, and a failing payload means no look. Door test vectors await a first implementation.

Both changes were open proposals in October and are now normative specification text.

## Movement proofs

The [sampled residue revision](https://github.com/arkin0x/cyberspace/commit/8b45430af330f6e93ee763716d33868706cc2879) changes the hop proof commitment to Merkle-sealed modular residues with 16 sampled openings. A verifier checks word-sized residues without rebuilding the large roots. Trees and location keys are unchanged, and the new `proof`, `mn`, and `mp` tags are mandatory.

The only exemption is an [exact-ID list of legacy hops](https://github.com/arkin0x/cyberspace/commit/957021e2138b1477d2255e2678f0de889eb5fcd6) holding 2658 version 1 hop IDs that passed the project's published audit, with 8 failing hops omitted. There is no date-based grace period. That audit's census read one relay and missed a feeds relay, so the list does not prove complete historical coverage.

[Normative signed chain vectors](https://github.com/arkin0x/cyberspace/commit/3ffa27552a6f65e75f235a6bea93930333b065b1) lock the verdict, position, and failure point for 158 synthetic movement chains, 140 ported and 18 new. Separate [non-normative golden hop-proof vectors](https://github.com/arkin0x/cyberspace/commit/06c287332651f99b75e609b7b098e165993750fd) cover 7 prover hops and 26 verifier cases so ports in other languages can compare exact encodings. Where they differ, the spec text wins.

These merges change the specification. They do not show which clients verify the new proofs or render doors, and they carry no hardware performance claim.

---

**Primary sources:**
- [Cyberspace specification repository](https://github.com/arkin0x/cyberspace)
- [Carried SNO objects in the parent payload](https://github.com/arkin0x/cyberspace/commit/9210d6dff16637079c8339a9c957c60cbd3a744e)
- [Doors and chest looks](https://github.com/arkin0x/cyberspace/commit/bd9125eea93274ee589657f0bd23203916ead40f)
- [Sampled residue hop proofs](https://github.com/arkin0x/cyberspace/commit/8b45430af330f6e93ee763716d33868706cc2879)
- [Audited legacy hop ID list](https://github.com/arkin0x/cyberspace/commit/957021e2138b1477d2255e2678f0de889eb5fcd6)
- [Normative signed chain vectors](https://github.com/arkin0x/cyberspace/commit/3ffa27552a6f65e75f235a6bea93930333b065b1)
- [Portable hop-proof golden vectors](https://github.com/arkin0x/cyberspace/commit/06c287332651f99b75e609b7b098e165993750fd)

**Mentioned in:**
- [Newsletter #46](/en/newsletters/2026-10-28-newsletter/)
