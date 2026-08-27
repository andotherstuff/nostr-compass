# Coverage review — Newsletter #37 (2026-08-26), retroactive

Prompted by the owner on 2026-08-27: a project may be omitted only when it was covered in the previous issue AND shipped nothing substantive. `scripts/check_triage_coverage.py` reported 22 high-signal releases in #37's window that no artifact named. Every one is decided below against the per-PR Nostr-surface gate in `CLAUDE.md`.

Nail v0.1.0 was added separately in [#155](https://github.com/andotherstuff/nostr-compass/pull/155).

## Written up

| Project | Release | Nostr surface |
|---|---|---|
| MDK | v0.9.14, v0.9.15 | KeyPackage selection for invites, epoch-gap recovery before publish gates, admin-policy depletion, directory relays split from operational relays, MarmotKit bindings |
| Zeus | v13.2.0 | Eight NIP-47 fixes: connection spending budgets, `pay_invoice` races, `sign_message` ordering, client-secret rotation on relay change |
| NYM | v3.73.525–v3.75.543 | Post-quantum encryption for PMs and group chats, message threads, Bluetooth mesh in browsers, Bitchat PM interop |
| diVine | 1.0.22 | Relay and NIP-46 signer connections outliving sign-out, subscription slot release, NIP-04 `created_at` bound, deleted list returning on sync |
| Chama | v6.0.1 | Escrow lock published on Nostr read funded while the ecash behind it had already unwound |
| ants | v0.4.6 | NIP-66 relay discovery feeding NIP-50 search-relay probes |
| nostr-dart | v11.0.0 | Major client-library release, integration-tested against live relays |
| myco | v0.6.0, v0.6.1 | Mesh wire-format change; user-run Nostr relay as storage |
| FIPS | v0.4.2 | Security work on a protocol using Nostr keypairs for node identity |
| Tollbooth DPYC | v0.3.0 | Relay set reordered from measured reachability; rendezvous pinning |
| Lightning.Pub | v0.0.39 | A Lightning call blocking the daemon's Nostr relay connection at startup |
| Keydex | v1.0.1-37 | Compatibility with some relay authentication implementations |
| nostr-vpn | v4.1.8 | Peer and paid-exit discovery via WebSocket bootstrap peers; private-mesh session recovery |

## Skipped, with reasons

| Project | Release | Reason |
|---|---|---|
| bray | v3.1.0–v3.3.0 | Website fonts, motion and sideways-scroll fixes. Generic UX polish; the MCP server's Nostr surface did not change. |
| Sonar | v0.1-alpha.14 | Mention-chip design, bubble send-time clipping, crash and scroll fixes. UX polish. |
| Buzz | desktop-v0.5.17–20 | Zero Nostr-surface lines across four changelogs. Agent mention authorization and addressing are app-level. |
| CDK | v0.18.0-rc.1 | Cashu-only prepared payment-request flow. Touches no Nostr event kind. |
| toll-booth | v6.2.0 | LUD-25 bearer notes in an HTTP header. Lightning-only. |
| BitBlik | v0.10.1 | New bank entry and a code-validity correction. No Nostr surface. |
| Nostr action | v1.9.0, v2.0.0 | Node 20 to 24 runtime migration and dependency bumps. Build tooling. |
| earthly | v0.1.6 | One change: chat and entity editing made explicit. Too thin for an entry. |
| Disgus | v0.1.0, v0.2.0 | No release notes; a bare compare link. A Nostr comment widget worth introducing properly once researched, not retrofitted into a published issue. |
| rssnotes | v0.1.4, v0.1.6 | No release notes on any tag. |
| Nostr Codex Phone | v0.3.46 | Release notes are a bare compare link. This is the single entry `suppression_allowed` marks defensible for this window. |
| mesh-llm | v0.76.0-rc4–rc7 | Release candidates whose changes are Skippy refactors, a pinned llama.cpp revision, IPC timeouts and crates.io publishing. The project uses Nostr for identity and config, but this RC line does not touch it. |
| astraea, fips-ts, nostr-pubsub, Napplets Web Packages | various | Documented changes only, with no Nostr surface in the window. |

## Data-quality finding

`NostrAppShell` (v0.13.0–v0.16.0) release notes resolve to `git.nostrdev.com/stuff/pakstr` compare URLs, so the tracker is reading pakstr's changelog under the NostrAppShell name. pakstr is already covered in #37 on its own. The repo mapping in `data/projects.yml` needs checking before either project is written up from this source again.

GATE: PASS (22 flagged releases each carry a written-up or skipped decision; 13 added to the issue; 15 skipped with a stated Nostr-surface reason; 1 tracker mapping defect recorded)
