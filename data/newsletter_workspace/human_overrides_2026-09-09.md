# Human overrides — 2026-09-09

## Mandatory include: ngit v3 / GitWorkshop v4 coordinated launch

The owner instructed that the 2026-09-09 issue include the launch at https://ngit.dev/v3.

Place it as the lead story and cover only primary-source-verified claims: ngit v3, ngit-grasp v3, GitWorkshop v4, the first ngit-ci 0.1 release, self-hosted CI coordinated through signed Nostr events, GRASP-08 private repositories, signed forge-free releases and assets over Nostr and Blossom, maintainer-authority changes, and the unified ngit.dev documentation site. Preserve the continuity distinction from ngit v2.6.3 coverage on 2026-07-15 and GitWorkshop coverage on 2026-07-29.

Primary sources:

- https://ngit.dev/v3
- https://ngit.dev/ngit.git
- https://ngit.dev/ngit-grasp.git
- https://ngit.dev/ngit-ci.git
- https://ngit.dev/gitworkshop.git

## Mandatory include: fips2go

The owner instructed that the 2026-09-09 issue include https://zapstore.dev/apps/naddr1qqgx7un89enxjurn9eskuerjda5kgqgcwaehxw309aex2mrp0yh85ctswd6x7un99ejx2aszyqs9vy2xh4p6zygk35qepsja6w7mnl4j3nnyvjgyg079gxnm83e0yqcyqqq8uzclek0pe.

Include fips2go in News as a newly tracked Android app. Its signed Zapstore listing and repository describe an embedded FIPS mesh node whose secp256k1 identity is rendered as an `npub`, with diagnostics that resolve or ping nodes by `npub`. The per-app VPN lets selected Nostr clients reach relays or services on `.fips` names while retaining ordinary internet access; it also provides a default-deny inbound firewall, Android Keystore identity backup, local peer discovery, and diagnostics. The current release is v0.3.4. Update the existing FIPS topic page and add the repository to project tracking. Do not defer it.

GATE: PASS (both owner instructions preserved; ngit launch sources and the relay-backed fips2go listing plus repository were verified)
