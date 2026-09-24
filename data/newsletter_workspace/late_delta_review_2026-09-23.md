# Compass #41 late-delta source decisions

Window: 2026-09-23T20:31:30Z..2026-09-23T23:44:00Z. The earlier complete ten-family Wednesday pass remains the base selection manifest. This separate late pass is a real post-cutoff source check; it is not silently substituted for the full-pass ledger.

Project-update collector SHA-256: `b5ed87d73deb5e6da13f71e5c96e921cd33600555a1c142e1a078433d7206f0f`. Compact inventory: `late_delta_inventory_2026-09-23.json` (37 merged PRs, two project releases, eight signed app-release records, and one updated spec PR). The complete ten-family late pass is finalized: source-manifest SHA-256 `0e3efbdd32a42e9283e1d3e98a5cfe3b422f430572f19d4481c7cb9704c3bd95`.
Signed Zapstore artifact SHA-256: `840bf8a755e1840c90e7b18358e062eca0623717d1f6194e7d7c3dea7e43d729`.
Specification artifact SHA-256: `5ffadfb38153310bf2ca57f57e3b6feb55c2e9ac2bcf4b46a6d55defb676e27d`.

## New tagged releases

- [fips2go 0.6.1](https://github.com/fr34aky/fips2go/releases/tag/v0.6.1), published 20:34:57Z: IPv6-only-carrier bootstrap address selection fix; maintainer has not tested it on an actual DNS64 carrier. Fold into the existing fips2go Top Story.
- [fips2go 0.7.0](https://github.com/fr34aky/fips2go/releases/tag/v0.7.0), published 22:37:03Z: three default bootstrap peers and opt-in capped Nostr-discovered peers; public test-mesh stale-announcement caveat. Fold into the same Top Story.

- [Zzub 0.0.16](https://primal.net/e/d9ad994bfadc1152b4c77a4fd3eb6be1746eca9d2626008d341bf31d06988872), developer-signed at 21:10:28Z: restores announced projects, adds project-wide Tasks/Reviews tabs, mention selection, and board filters. Fold into the existing Zzub Tagged Release; the earlier 0.0.15 source remains distinct.
## NIP-34 discovery decisions

NIP-34 cutoff artifact SHA-256: `68c8479c91171d0c1713e7fe029cb9a9228aee73506e81e22607063fcf232620`; tracked repositories had no new patches or issues in this window. Four new announcements were checked:

- [gyoza-hanto](https://primal.net/e/aad13a158be702a1835b41ebb022a00c0a51c97851082caae7d22d7da85dea6e): SKIP. The signed announcement describes an Omarchy Nostr client, but there is no verified code release, usage, or material product launch yet.
- [omarchy-pock](https://primal.net/e/1a41e07d21d4f5556ee1a4f63b3a7287dd40aef1b64820f41129c8b8571f51f0): SKIP. A Touch Bar widget daemon announcement has no demonstrated Nostr application surface.
- [omarchy-btclock](https://primal.net/e/d2cd9dfde48986285945496708d804d2de059a4151b6efd819b4bf1d7758a98b): SKIP. A Bitcoin clock repository announcement has no demonstrated Nostr-facing product change.
- [omarchy-bitcoin-frontier-theme](https://primal.net/e/75d7771286ff9b2c6d542396d72cfbc3dbe90bf8bfcef526c2eb69a35ef9add7): SKIP. A visual theme repository announcement has no demonstrated Nostr-facing product change.

## App-discovery decisions

App-discovery cutoff artifact SHA-256: `3d574a0bd2bc7bcc5228f6bcb71eaf84b25aca31ce61e499fdd671c3e428000f`. All five are candidate-only leads, not evidence of a newly shipped app:

- [BlindOracle](https://primal.net/e/fa183fa9970986e8611aceb54ff73f5c6db74939f0ce7fbcec7985d0ff34efad): SKIP. The self-published NIP-89 handler advertises a financial suite, but no repository ownership, released product, or live user flow is verified.
- [node-dlc](https://github.com/AtomicFinance/node-dlc): SKIP. Sibling repository discovery provides no current Nostr-facing release or product milestone.
- [qrgo](https://github.com/block/qrgo): SKIP. QR capture for emulators is a general developer utility, not a Nostr-facing release.
- [taskledger](https://github.com/ledgerwerk/taskledger): SKIP. Coding-work state tooling has no demonstrated Nostr-facing change.
- [tollbooth-web](https://github.com/lonniev/tollbooth-web): SKIP. Sibling browser SDK has no independently verified Nostr-facing release in the cutoff window.

## Remaining signed store and specification records

The signed Zapstore cutoff contains eight release events. Zzub 0.0.16 is folded above. [fips2go 0.6.1](https://primal.net/e/13a4c43de32c03fbb18d888025cf9ef01bd4a98877e0dc6545fd14e5dec1d3c0) and [0.7.0](https://primal.net/e/55a1c289ea6c3b3b56d5eb692bceae4a87d3d789b68882f118b9f9bb59c59ab2) are the same two releases covered through their exact project tags, so both signed events FOLD into the Top Story.

- [FilePipe 3.11.0](https://primal.net/e/e66b7e455a82b4ef7ab063abde39abc542884f4e345956adea3bf7c233837111): SKIP. Offline build and layout repairs have no Nostr-facing behavior.
- [Fokus 1.9.4](https://primal.net/e/30ef95bc82ee88456b6981afb0f88f0133a9657ddf795689a588b695208193b5): SKIP. Launcher naming and activity-selection fixes have no Nostr-facing change.
- [Mood Cairns 1.2.0](https://primal.net/e/a4f16cec210713185fce21946b8ed1f2ddcae2ed10be19ee8d76b3cabe63b97e): SKIP. Mood tags and chart controls are not Nostr product changes.
- [Clench 0.3.33](https://primal.net/e/66953e5f9c2d0c1efaa0bd7ddcf81ca2175c8cc4def57977d193f68cb23dce5d): SKIP. The JNA crash repair on 16 KB-page Android devices is wallet runtime maintenance, not a Nostr change.
- [Atmo Engine 7.2.3](https://primal.net/e/3c5a481a26c404bf987029d01c710985dd817a9ddd0bf675f2bb247c0cf1f5f1): SKIP. Foldable-layout and clock-effect changes have no Nostr-facing behavior.

The only new specs-family activity is [open NIP-86 PR #2439](https://github.com/nostr-protocol/nips/pull/2439). Its September 23 update is [a comment](https://github.com/nostr-protocol/nips/pull/2439#issuecomment-5803154499) saying nostrfy will implement assign/unassign methods in a future v0.1.16. SKIP a separate story: the PR remains open, the spec did not merge, and that comment does not verify an implementation. This does not change the draft's distinct coverage of merged NIP-86 PR #2477.

NIP discussions, Nostr Recap and Shakespeare Apps returned verified empty activity; monthly-history is not applicable for this issue. The heartbeats collector found no new editorial milestone. NIP-34 records and app-discovery leads are dispositioned above.

## Merged-PR dispositions

| Project | Primary PR | Decision | Source-grounded reason |
|---|---|---|---|
| Amethyst | [#4189: fix: address the audit of the Render/Display split — desktop uses the shared dialogs, no blank group messages](https://github.com/vitorpamplona/amethyst/pull/4189) | FOLD: Amethyst MLS interop | MLS optional fields, supported extensions and desktop group rendering form one in-development update. |
| Amethyst | [#4185: refactor: Render/Display split, batches 1–3 — shared displays for AccountViewModel-bound composables](https://github.com/vitorpamplona/amethyst/pull/4185) | FOLD: Amethyst desktop group rendering | The internal Render/Display split shares account-independent UI across desktop and Android; #4189 audits and fixes its group-message regression. It is not a separate MLS feature. |
| Amethyst | [#4188: feat(marmot): optional leaf lifetime on createKeyPackage](https://github.com/vitorpamplona/amethyst/pull/4188) | FOLD: Amethyst MLS interop | MLS optional fields, supported extensions and desktop group rendering form one in-development update. |
| Amethyst | [#4187: feat(marmot): caller-chosen group_id and optional required_capabilities](https://github.com/vitorpamplona/amethyst/pull/4187) | FOLD: Amethyst MLS interop | MLS optional fields, supported extensions and desktop group rendering form one in-development update. |
| Amethyst | [#4184: feat(marmot): send and return authenticated_data on application messages](https://github.com/vitorpamplona/amethyst/pull/4184) | FOLD: Amethyst MLS interop | MLS optional fields, supported extensions and desktop group rendering form one in-development update. |
| Amethyst | [#4183: feat(marmot): Ed25519.keyPairFromSeed](https://github.com/vitorpamplona/amethyst/pull/4183) | FOLD: Amethyst MLS interop | MLS optional fields, supported extensions and desktop group rendering form one in-development update. |
| Amethyst | [#4182: fix(marmot): accept extensions every member supports in GCE proposals](https://github.com/vitorpamplona/amethyst/pull/4182) | FOLD: Amethyst MLS interop | MLS optional fields, supported extensions and desktop group rendering form one in-development update. |
| Amethyst | [#4186: Implement DECK-0003 (SNO) reader, rasterizer, and Cyberspace bag opening](https://github.com/vitorpamplona/amethyst/pull/4186) | INCLUDE: Amethyst DECK-0003 | The PR body confirms Nostr kinds 11333, 3330 and 33330, SNO parsing/rasterizing, region-bag opening, and reference conformance. Bag UI is not phone-verified. |
| Nostter | [#2584: Remove the Author followees compatibility projection](https://github.com/SnowCait/nostter/pull/2584) | FOLD: nostter signer capabilities | Signer/decrypter capability migration forms one user-facing safety update; projection removals are implementation support. |
| Nostter | [#2583: Migrate application callers to auth followees](https://github.com/SnowCait/nostter/pull/2583) | FOLD: nostter signer capabilities | Signer/decrypter capability migration forms one user-facing safety update; projection removals are implementation support. |
| Nostter | [#2582: Remove the Author pubkey compatibility projection](https://github.com/SnowCait/nostter/pull/2582) | FOLD: nostter signer capabilities | Signer/decrypter capability migration forms one user-facing safety update; projection removals are implementation support. |
| Nostter | [#2581: Migrate Svelte callers to auth pubkey](https://github.com/SnowCait/nostter/pull/2581) | FOLD: nostter signer capabilities | Signer/decrypter capability migration forms one user-facing safety update; projection removals are implementation support. |
| Nostter | [#2580: Migrate application callers to auth pubkey](https://github.com/SnowCait/nostter/pull/2580) | FOLD: nostter signer capabilities | Signer/decrypter capability migration forms one user-facing safety update; projection removals are implementation support. |
| Nostter | [#2579: Remove following pubkeys store projection](https://github.com/SnowCait/nostter/pull/2579) | FOLD: nostter signer capabilities | Signer/decrypter capability migration forms one user-facing safety update; projection removals are implementation support. |
| Nostter | [#2578: Remove unused rom projection](https://github.com/SnowCait/nostter/pull/2578) | FOLD: nostter signer capabilities | Signer/decrypter capability migration forms one user-facing safety update; projection removals are implementation support. |
| Nostter | [#2577: Remove npub-specific display restrictions](https://github.com/SnowCait/nostter/pull/2577) | FOLD: nostter signer capabilities | Signer/decrypter capability migration forms one user-facing safety update; projection removals are implementation support. |
| Nostter | [#2576: Gate remote signer settings on NIP-44 capability](https://github.com/SnowCait/nostter/pull/2576) | FOLD: nostter signer capabilities | Signer/decrypter capability migration forms one user-facing safety update; projection removals are implementation support. |
| Nostter | [#2575: Gate legacy bookmark actions on signer availability](https://github.com/SnowCait/nostter/pull/2575) | FOLD: nostter signer capabilities | Signer/decrypter capability migration forms one user-facing safety update; projection removals are implementation support. |
| Nostter | [#2574: Gate private bookmark reads on decryption capability](https://github.com/SnowCait/nostter/pull/2574) | FOLD: nostter signer capabilities | Signer/decrypter capability migration forms one user-facing safety update; projection removals are implementation support. |
| Nostter | [#2573: Use signer availability for remaining write actions](https://github.com/SnowCait/nostter/pull/2573) | FOLD: nostter signer capabilities | Signer/decrypter capability migration forms one user-facing safety update; projection removals are implementation support. |
| Nostter | [#2572: Separate profile actions by signing capability](https://github.com/SnowCait/nostter/pull/2572) | FOLD: nostter signer capabilities | Signer/decrypter capability migration forms one user-facing safety update; projection removals are implementation support. |
| Nostter | [#2571: Use signer availability for write controls](https://github.com/SnowCait/nostter/pull/2571) | FOLD: nostter signer capabilities | Signer/decrypter capability migration forms one user-facing safety update; projection removals are implementation support. |
| Nostter | [#2570: Use signer availability in the action menu](https://github.com/SnowCait/nostter/pull/2570) | FOLD: nostter signer capabilities | Signer/decrypter capability migration forms one user-facing safety update; projection removals are implementation support. |
| Buzz | [#7844: feat(agents): humanize uncurated Databricks model ids with a label grammar](https://github.com/block/buzz/pull/7844) | SKIP | Provider-model label grammar is not a Nostr-facing change. |
| diVine | [#9413: feat(supporters): show membership and optional profile badges](https://github.com/divinevideo/divine-mobile/pull/9413) | SKIP | Supporter badges require a companion endpoint whose deployment is unverified; no Nostr event/protocol behavior shown. |
| Mostro | [#976: docs: spec a quality bar for pull requests](https://github.com/MostroP2P/mostro/pull/976) | SKIP | PR quality documentation only; no shipped Nostr behavior. |
| Pensieve | [#50: Build bounded archive-confirmed reconciliation inventory](https://github.com/andotherstuff/pensieve/pull/50) | FOLD: Pensieve archive durability | Three library-only archive/reconciliation increments form one in-development update; no runtime deployment is claimed. |
| Pensieve | [#49: Seal the archive independently of optional Parquet publication](https://github.com/andotherstuff/pensieve/pull/49) | FOLD: Pensieve archive durability | Three library-only archive/reconciliation increments form one in-development update; no runtime deployment is claimed. |
| Pensieve | [#48: Connect isolated reconciliation receipts to durable archive completion](https://github.com/andotherstuff/pensieve/pull/48) | FOLD: Pensieve archive durability | Three library-only archive/reconciliation increments form one in-development update; no runtime deployment is claimed. |
| fips2go | [#52: Release 0.7.0](https://github.com/fr34aky/fips2go/pull/52) | FOLD: fips2go 0.7.0 | Merged implementation and release PRs are covered by the two new tagged releases, not separate stories. |
| fips2go | [#51: Discover peers via Nostr: a Settings toggle for fips's open policy, capped (fips pin → ae22165)](https://github.com/fr34aky/fips2go/pull/51) | FOLD: fips2go 0.7.0 | Merged implementation and release PRs are covered by the two new tagged releases, not separate stories. |
| fips2go | [#50: Three links into the mesh: fallback bootstrap peers, via_nostr on every peer](https://github.com/fr34aky/fips2go/pull/50) | FOLD: fips2go 0.7.0 | Merged implementation and release PRs are covered by the two new tagged releases, not separate stories. |
| fips2go | [#49: Release 0.6.1](https://github.com/fr34aky/fips2go/pull/49) | FOLD: fips2go 0.7.0 | Merged implementation and release PRs are covered by the two new tagged releases, not separate stories. |
| Angor | [#974: Add indexer retry/backoff + concurrency cap; ease SendFundsTest load](https://github.com/block-core/angor/pull/974) | SKIP | Bitcoin indexer error handling and test throttling have no demonstrated Nostr-facing effect. |
| Angor | [#973: Fix unguarded /outspends response parsing in MempoolSpaceIndexerApi](https://github.com/block-core/angor/pull/973) | SKIP | Bitcoin indexer error handling and test throttling have no demonstrated Nostr-facing effect. |
| Marmot Protocol (mdk) | [#2008: Add explicit fenced audit OTLP runtime attempt](https://github.com/marmot-protocol/mdk/pull/2008) | SKIP | Audit OTLP attempt is inactive by default with no production sender, native binding, or user-facing release. |
| Heterodyne | [#33: Add optional token custody checker and guidance](https://github.com/HeterodyneNetwork/HeterodyneProtocol/pull/33) | SKIP | Optional read-only FIDO custody checker does not change the live Nostr protocol or published vectors. |

The four in-development updates are Amethyst DECK-0003 objects/bag search, Amethyst MLS interoperability and desktop group rendering, nostter capability-gated signer/decryption actions, and Pensieve's bounded archive reconciliation. No tagged app release is claimed for these PRs. Pensieve's repair worker is not deployed; nostter's live web deployment was not independently verified.

GATE: PASS — all ten late source families finalized and their material candidate decisions recorded; final exact-draft selection, review, PR-head, deployment and broadcast gates remain separate.
