# Compass #41 distinct final-cutoff source decisions

Frozen window: 2026-09-23T23:44:00Z..2026-09-24T00:41:00Z. This is a third, isolated source pass, not a replacement for the complete Wednesday pass or the finalized 20:31:30Z..23:44:00Z broad delta. The final source pass is still collecting; this memo remains pending until all ten families have exact results.

The final project-update artifact is `/opt/data/compass-worktrees/2026-09-23-final-cutoff/data/project_updates/updates_2026-09-23_2026-09-24.json`, SHA-256 `287b7f3d6fa7a708dd56141199cf4b8f044de991ea9050d64c7a8fd939f654c7`. It contains zero new tagged releases and six merged PRs across four projects. The decisions below are read from the captured primary PR bodies, not inferred from titles.

| Project | Primary merged PR | Decision | Source-grounded reason |
|---|---|---|---|
| nostter | [#2585 notification classification](https://github.com/SnowCait/nostter/pull/2585) | FOLD | Moves pure notification classification out of the global Author object; it supports the already covered account-capability migration without a new user-facing behavior. |
| nostter | [#2586 global Author store removal](https://github.com/SnowCait/nostter/pull/2586) | FOLD | Removes an unused global instance while preserving current runtime behavior and account-state publication; not a second client milestone. |
| nostter | [#2587 account event loading](https://github.com/SnowCait/nostter/pull/2587) | FOLD | Separates event loading from application state while explicitly preserving current runtime behavior; the migration issue remains open. |
| mesh-llm | [#2026 System One canary evidence](https://github.com/Mesh-LLM/mesh-llm/pull/2026) | SKIP | Repairs test/canary evidence handling in an AI-hosting workflow, with no demonstrated Nostr event, relay, or client change. |
| MDK | [#2005 directory relay separation](https://github.com/marmot-protocol/mdk/pull/2005) | SKIP | Separates public directory subscriptions from account transport as a preparatory library step; its body explicitly says account-context migration, bounded acquisition and recovery activation remain future work. |
| MDK | [#2007 parked-message replay](https://github.com/marmot-protocol/mdk/pull/2007) | INCLUDE | Removes repeated lineage scans and historical-state rewinds for unreadable parked rows after publish/join, with regression tests and a passing engine suite. The draft marks it merged library work after 0.10.4, not a released or measured client latency result. |

## Signed-store dispositions

The final Zapstore artifact is `/opt/data/compass-worktrees/2026-09-23-final-cutoff/data/zapstore_releases/zapstore_2026-09-24.json`, SHA-256 `a8f73cba1ed7b12191cb5a7544fe856611c366a632125816023f16b63b573902`. Its self-signature gate retains exactly two releases.

| App | Developer-signed primary event | Decision | Reason |
|---|---|---|---|
| Table Mesh 0.1.0 | [signed release](https://primal.net/e/c5c5ad0eba413e18c10e3cd2be607e550ac818a8abaf97ccbf8fa242fbaff15f) | INCLUDE | First Android release has a distinctive Nostr kind-7529/Blossom path for discovering and verifying optional game modules. Board-game sessions run locally over Bluetooth/Wi-Fi; signed notes ask for real multi-phone reports rather than claiming device validation. |
| PosterChan 1.0.2356 | [signed release](https://primal.net/e/35e74e8a6546c85a8ce540a845dc859010138ef03aec9572478bb4c5a111cfa2) | SKIP | The only release-note change imports linked Pleroma follows/bridge puppets; no new Nostr protocol or client milestone beyond the already skipped listing. |

The app-discovery artifact, `/opt/data/compass-worktrees/2026-09-23-final-cutoff/data/app_discovery/discovery_2026-09-24.json` (SHA-256 `c805a27eb789f616b94b9a3b0ff8ba52d65793742ebfaab2e851d7592395e713`), has three candidate-only leads. [BlindOracle's self-published NIP-89 handler](https://primal.net/e/945672d34c81ab31a21cb1146561315469740e4081239f16bde40ab0b98975e0) is SKIP pending repository/product verification, not evidence that its sweeping finance claims shipped. [monstr-chat](https://github.com/g4r7y/monstr-chat) is an older repository merely first seen now; SKIP as no independently verified in-window release. PosterChan's listing is FOLD into its explicit signed-release skip above.

The heartbeat artifact, `/opt/data/compass-worktrees/2026-09-23-final-cutoff/data/heartbeats/heartbeat_2026-09-23_2026-09-24.json` (SHA-256 `2e28307acee6b5913eb870acee1323ebf51ce87882fe114535cdf744dd7e5c11`), contains twelve OpenSats Nostr-fund events duplicating the nostter PRs above and six general-fund Bitcoin/BIP/Stratum events without a distinct Nostr story. The Sovereign Engineering archive has no tagged event in this window. No separate heartbeat story is selected.

Authenticated live GitHub readback: MDK #2007 is merged at 2026-09-23T23:59:48Z, merge commit `828bed64e2359aa174bdcbd7ddf8655d09b58516`, into `marmot-protocol/mdk` base `master`; the repository's current default branch is `master`. The draft cites the selected PR.

GATE: PENDING — the specs family hit GitHub's shared core API reserve and must be resumed after reset. The final manifest hash, spec decisions, final draft hash and independent exact-draft review remain required.
