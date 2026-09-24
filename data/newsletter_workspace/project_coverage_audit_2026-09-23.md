# Compass #41 project-coverage audit

Window: 2026-09-14 00:00 UTC through 2026-09-22 13:24 UTC. This audit compares the fixed-window `project_updates` findings with the draft at PR #177 and the September 2, 9, and 16 newsletters. Counts of commits or PRs alone never qualify an item. The links below were read back live as merged to each project's default branch; each chosen change has a distinct Nostr-facing effect and was absent from those preceding issues.

## Added to In Development

| Project | Score | Direct evidence | Editorial reason |
|---|---:|---|---|
| nostream | 9 | [NIP-66 monitor events](https://github.com/cameri/nostream/pull/741), [trust-aware proof of work](https://github.com/cameri/nostream/pull/779) | A relay now publishes signed health observations and offers an opt-in trust-aware admission policy. |
| nostter | 8 | [session-owned remote signer](https://github.com/SnowCait/nostter/pull/2518), [share-menu images](https://github.com/SnowCait/nostter/pull/2510) | Signer teardown follows login state and images from the device share menu enter normal Nostr composition. |
| Zap Cooking | 10 | [NIP-92 image descriptions](https://github.com/zapcooking/frontend/pull/746), [search safety](https://github.com/zapcooking/frontend/pull/744) | Cross-client image accessibility and prevention of accidental secret-key relay search are both material. |
| Divine Mobile | 8 | [automatic relay reconnection](https://github.com/divinevideo/divine-mobile/pull/9246), [profile identity read](https://github.com/divinevideo/divine-mobile/pull/9293) | Passive subscriptions recover after disconnect and slower relays no longer hide linked identities. |
| Conduit | 9 | [Blossom product-image uploads](https://github.com/Conduit-BTC/conduit-mono/pull/503) | Merchants gain a signed, preference-respecting media workflow in the Nostr marketplace. |
| Buzz | 8 | [NIP-98 relay moderation routes](https://github.com/block/buzz/pull/7302) | Relay operators can inspect and reverse community restrictions with signed authorization and transactional audit records. |
| ContextVM SDK | 8 | [relay liveness and first acknowledgement](https://github.com/ContextVM/sdk/pull/100), [stream sequencing](https://github.com/ContextVM/sdk/pull/95) | Nostr transport clients no longer wait for every relay before publishing and client-started streams avoid duplicate sequence numbers. |
| Mostro | 8 | [stable order creation tag](https://github.com/MostroP2P/mostro/pull/971) | The implementation of the in-window NIP-69 proposal lets clients distinguish an order's opening time from its latest revision. |

## Kept out

- [Buzz remote signing](https://github.com/block/buzz/pull/7627) is substantial but merged into `buzz-unified-signing`, not `main`; its own PR says full CI and live acceptance remain outstanding. Do not present it as available product behavior.
- [Conduit relay-routing work](https://github.com/Conduit-BTC/conduit-mono/pull/511) is likewise stacked on a non-default branch. The main-branch Blossom upload is the verified current milestone.
- [Glow Web](https://github.com/breez/glow-web/pull/446), [LNBits](https://github.com/lnbits/lnbits/pull/4169), and [mesh-llm](https://github.com/michaelneale/mesh-llm/pull/1990) had considerable activity but no discrete Nostr-facing change that clears the relay test in this window.
- [Stablekraft Data Saver](https://github.com/ChadFarrow/stablekraft-app/pull/273) is useful general bandwidth work, but not a Nostr-specific milestone; its small [boost-text correction](https://github.com/ChadFarrow/stablekraft-app/pull/262) does not reach the common 8/10 bar alone.
- [Chama](https://github.com/jesuspirate/chama/pull/19), [ehagaki](https://github.com/Lokuyow/ehagaki), and [cyberspace](https://github.com/arkin0x/cyberspace/pull/25) had site polish or early documentation activity, not a reviewable new Nostr application capability at the threshold.
- [NIP-AC PR #2461](https://github.com/nostr-protocol/nips/pull/2461) was removed from the draft: the September 9 issue already explained that exact proposal and its in-window merge did not add a distinct protocol change.
- Version-only and maintenance-only releases remain excluded; in particular Wisp 1.2.5 and pakstr 0.24.0 are not treated as the substantive milestones behind their earlier releases.

The Stage 4 selection ledger in this branch remains provisional (`final: false`) and predates this audit. Stage 5 must incorporate these eight selected items and this NIP-AC exclusion into the canonical source-to-draft ledger, then bind the exact reviewed draft hash before publication. This audit is editorial evidence, not a publication receipt.
