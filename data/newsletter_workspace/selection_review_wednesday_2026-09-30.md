# Wednesday selection reconciliation — 2026-09-30

This report preserves the original Tuesday ledger/review. It binds the Wednesday full-pass manifest, all new merged-PR and release decisions, explicit series folds, signed Zapstore delta decisions and the current draft. The finalized ten-family source pass and final article are bound below. This report records selection coverage; publication has separate gates.

## Input bindings
- Source manifest: `/opt/data/compass-worktrees/2026-09-30/data/source_runs/source_run_2026-09-30_urgent-full-20260930-1511.json` at `bf7a10a48ea3c061339262dfc7805643f6342acd5e5e7735d46cd8859369f4da`.
- Draft: `/opt/data/compass-worktrees/2026-09-30/content/en/newsletters/2026-09-30-newsletter.md` at `18f3f80a31b011737722c1715490836a88141e7cf19ad1a9ddec7f3253a751ec`.
- Project source: `/opt/data/compass-worktrees/2026-09-30/data/project_updates/updates_2026-09-21_2026-09-30.json` at `e330807c75637311c2b63c6d4542d157b796be88976238718c2911711e1faef1`.
- PR delta: `/opt/data/tmp/compass_pr_delta_decisions_20260930.json` at `b2766c120fb365925995efffe209c6b158265c4885fe786aaab3eb1dcee853f3`.
- Release delta: `/opt/data/tmp/compass_release_delta_decisions_20260930.json` at `ca74e93c542858d55ab10d4a3492f05a5739d79c00e0155b7a16484ccc1454f4`.

## Exact source decisions and folds

### Nostter PR 2628 — SKIP

CSS placement/reset refactor explicitly without intended behavior change

Primary: https://github.com/SnowCait/nostter/pull/2628

### Nostter PR 2626 — SKIP

Server diagnostics only, no changed Nostr behavior

Primary: https://github.com/SnowCait/nostter/pull/2626

### Nostter PR 2625 — SKIP

Stylesheet diagnostic telemetry only

Primary: https://github.com/SnowCait/nostter/pull/2625

### Nostter PR 2624 — SKIP

Temporary CSS diagnostics explicitly do not fix cause

Primary: https://github.com/SnowCait/nostter/pull/2624

### Amethyst PR 4282 — FOLD

Material merged-source Nostr progress: Add Buzz protocol event types and NIP-MP conformance fixtures. Fold into sourced Amethyst addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/vitorpamplona/amethyst/pull/4282
Cited story evidence: https://github.com/vitorpamplona/amethyst/pull/4282

### Amethyst PR 4284 — FOLD

Material merged-source Nostr progress: feat: display Ultra HDR photos in HDR. Fold into sourced Amethyst addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/vitorpamplona/amethyst/pull/4284
Cited story evidence: https://github.com/vitorpamplona/amethyst/pull/4284

### Amethyst PR 4277 — FOLD

Material merged-source Nostr progress: feat(concord): private channels, Kick, audit fixes and the remaining CORD features. Fold into sourced Amethyst addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/vitorpamplona/amethyst/pull/4277
Cited story evidence: https://github.com/vitorpamplona/amethyst/pull/4277

### Amethyst PR 4280 — SKIP

Image transition clipping polish below substantive workflow threshold

Primary: https://github.com/vitorpamplona/amethyst/pull/4280

### Amethyst PR 4281 — SKIP

Test/CI/internal cleanup only; no new Nostr runtime, user workflow or independently reviewable protocol milestone.

Primary: https://github.com/vitorpamplona/amethyst/pull/4281

### Amethyst PR 4278 — FOLD

Material merged-source Nostr progress: refactor: one-UI step 6 waves 3–7 — upload port, 140 shared screens, audit fixes. Fold into sourced Amethyst addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/vitorpamplona/amethyst/pull/4278
Cited story evidence: https://github.com/vitorpamplona/amethyst/pull/4278

### Amethyst PR 4272 — FOLD

Material merged-source Nostr progress: feat(mls): open late application messages from retained former epochs. Fold into sourced Amethyst addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/vitorpamplona/amethyst/pull/4272
Cited story evidence: https://github.com/vitorpamplona/amethyst/pull/4272

### Amethyst PR 4275 — FOLD

Material merged-source Nostr progress: feat(mls): derive secret-tree leaves from the unexpanded node secrets. Fold into sourced Amethyst addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/vitorpamplona/amethyst/pull/4275
Cited story evidence: https://github.com/vitorpamplona/amethyst/pull/4275

### Amethyst PR 4271 — FOLD

Material merged-source Nostr progress: feat(mls): keep skipped-generation secrets across a restore. Fold into sourced Amethyst addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/vitorpamplona/amethyst/pull/4271
Cited story evidence: https://github.com/vitorpamplona/amethyst/pull/4271

### Amethyst PR 4270 — FOLD

Material merged-source Nostr progress: fix(mls): name the sender when a ratchet generation is reused. Fold into sourced Amethyst addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/vitorpamplona/amethyst/pull/4270
Cited story evidence: https://github.com/vitorpamplona/amethyst/pull/4270

### Amethyst PR 4274 — SKIP

Build repair without shipped release or new Nostr functionality

Primary: https://github.com/vitorpamplona/amethyst/pull/4274

### Amethyst PR 4265 — FOLD

Material merged-source Nostr progress: fix(concord): cross-client interop with Armada and Accordion. Fold into sourced Amethyst addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/vitorpamplona/amethyst/pull/4265
Cited story evidence: https://github.com/vitorpamplona/amethyst/pull/4265

### Amethyst PR 4264 — FOLD

Material merged-source Nostr progress: feat(concord): pins, disappearing messages, Invite Registry and Direct Invites. Fold into sourced Amethyst addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/vitorpamplona/amethyst/pull/4264
Cited story evidence: https://github.com/vitorpamplona/amethyst/pull/4264

### Amethyst PR 4267 — FOLD

Material merged-source Nostr progress: fix(quartz): correct tag readers found by the graph link review; remove ForkTag. Fold into sourced Amethyst addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/vitorpamplona/amethyst/pull/4267
Cited story evidence: https://github.com/vitorpamplona/amethyst/pull/4267

### Amethyst PR 4266 — FOLD

Material merged-source Nostr progress: Add NIP-71 video view events and push notification support. Fold into sourced Amethyst addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/vitorpamplona/amethyst/pull/4266
Cited story evidence: https://github.com/vitorpamplona/amethyst/pull/4266

### Amethyst PR 4262 — FOLD

Material merged-source Nostr progress: Implement CORD spec conformance: fragments, pins, rekey, dissolution. Fold into sourced Amethyst addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/vitorpamplona/amethyst/pull/4262
Cited story evidence: https://github.com/vitorpamplona/amethyst/pull/4262

### diVine PR 9702 — SKIP

Test/CI/internal cleanup only; no new Nostr runtime, user workflow or independently reviewable protocol milestone.

Primary: https://github.com/divinevideo/divine-mobile/pull/9702

### diVine PR 9703 — FOLD

Material merged-source Nostr progress: fix(video-editor): keep text in place on square exports with a smaller clip. Fold into sourced diVine addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/divinevideo/divine-mobile/pull/9703
Cited story evidence: https://github.com/divinevideo/divine-mobile/pull/9703

### diVine PR 9662 — SKIP

Test/CI/internal cleanup only; no new Nostr runtime, user workflow or independently reviewable protocol milestone.

Primary: https://github.com/divinevideo/divine-mobile/pull/9662

### diVine PR 9598 — FOLD

Material merged-source Nostr progress: feat(video-recorder): add a chroma key camera mode that shows the swapped background while recording. Fold into sourced diVine addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/divinevideo/divine-mobile/pull/9598
Cited story evidence: https://github.com/divinevideo/divine-mobile/pull/9598

### diVine PR 9701 — FOLD

Material merged-source Nostr progress: feat(video-editor): rename green screen to Color mask and let it key a plain white wall. Fold into sourced diVine addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/divinevideo/divine-mobile/pull/9701
Cited story evidence: https://github.com/divinevideo/divine-mobile/pull/9701

### diVine PR 9682 — SKIP

Test/CI/internal cleanup only; no new Nostr runtime, user workflow or independently reviewable protocol milestone.

Primary: https://github.com/divinevideo/divine-mobile/pull/9682

### diVine PR 9698 — FOLD

Material merged-source Nostr progress: fix(recorder): keep stills shot after leaving the stop-motion editor in the same clip. Fold into sourced diVine addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/divinevideo/divine-mobile/pull/9698
Cited story evidence: https://github.com/divinevideo/divine-mobile/pull/9698

### diVine PR 9694 — FOLD

Material merged-source Nostr progress: fix(video-editor): stop text moving down in square videos that mix clip resolutions. Fold into sourced diVine addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/divinevideo/divine-mobile/pull/9694
Cited story evidence: https://github.com/divinevideo/divine-mobile/pull/9694

### diVine PR 9652 — FOLD

Material merged-source Nostr progress: feat(video-editor): highlight each caption word as it is spoken. Fold into sourced diVine addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/divinevideo/divine-mobile/pull/9652
Cited story evidence: https://github.com/divinevideo/divine-mobile/pull/9652

### diVine PR 9672 — SKIP

Test/CI/internal cleanup only; no new Nostr runtime, user workflow or independently reviewable protocol milestone.

Primary: https://github.com/divinevideo/divine-mobile/pull/9672

### diVine PR 9680 — FOLD

Material merged-source Nostr progress: fix(providers): reload account-scoped preference services instead of rebuilding them. Fold into sourced diVine addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/divinevideo/divine-mobile/pull/9680
Cited story evidence: https://github.com/divinevideo/divine-mobile/pull/9680

### diVine PR 9674 — SKIP

Test/CI/internal cleanup only; no new Nostr runtime, user workflow or independently reviewable protocol milestone.

Primary: https://github.com/divinevideo/divine-mobile/pull/9674

### diVine PR 9679 — SKIP

Test/CI/internal cleanup only; no new Nostr runtime, user workflow or independently reviewable protocol milestone.

Primary: https://github.com/divinevideo/divine-mobile/pull/9679

### diVine PR 9677 — FOLD

Material merged-source Nostr progress: fix(comments): stop deleted comments from reappearing. Fold into sourced diVine addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/divinevideo/divine-mobile/pull/9677
Cited story evidence: https://github.com/divinevideo/divine-mobile/pull/9677

### diVine PR 9676 — SKIP

Test/CI/internal cleanup only; no new Nostr runtime, user workflow or independently reviewable protocol milestone.

Primary: https://github.com/divinevideo/divine-mobile/pull/9676

### diVine PR 9675 — SKIP

Test/CI/internal cleanup only; no new Nostr runtime, user workflow or independently reviewable protocol milestone.

Primary: https://github.com/divinevideo/divine-mobile/pull/9675

### diVine PR 9673 — SKIP

Test/CI/internal cleanup only; no new Nostr runtime, user workflow or independently reviewable protocol milestone.

Primary: https://github.com/divinevideo/divine-mobile/pull/9673

### diVine PR 9671 — SKIP

iOS compiler workaround without proven new shipped release

Primary: https://github.com/divinevideo/divine-mobile/pull/9671

### diVine PR 9669 — SKIP

Supporter marketing copy with no material Nostr surface

Primary: https://github.com/divinevideo/divine-mobile/pull/9669

### diVine PR 9647 — SKIP

Store supporter purchase handling with no direct Nostr integration change

Primary: https://github.com/divinevideo/divine-mobile/pull/9647

### diVine PR 9645 — FOLD

Material merged-source Nostr progress: feat(video-editor): put a detached clip back into the timeline. Fold into sourced diVine addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/divinevideo/divine-mobile/pull/9645
Cited story evidence: https://github.com/divinevideo/divine-mobile/pull/9645

### diVine PR 9664 — FOLD

Material merged-source Nostr progress: fix(video-player): stop imported HLS videos from crashing the Android feed. Fold into sourced diVine addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/divinevideo/divine-mobile/pull/9664
Cited story evidence: https://github.com/divinevideo/divine-mobile/pull/9664

### diVine PR 9640 — SKIP

Test/CI/internal cleanup only; no new Nostr runtime, user workflow or independently reviewable protocol milestone.

Primary: https://github.com/divinevideo/divine-mobile/pull/9640

### diVine PR 9639 — SKIP

Test/CI/internal cleanup only; no new Nostr runtime, user workflow or independently reviewable protocol milestone.

Primary: https://github.com/divinevideo/divine-mobile/pull/9639

### diVine PR 9654 — FOLD

Material merged-source Nostr progress: feat(video-editor): add 49 text fonts and group the font picker by style. Fold into sourced diVine addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/divinevideo/divine-mobile/pull/9654
Cited story evidence: https://github.com/divinevideo/divine-mobile/pull/9654

### diVine PR 9601 — FOLD

Material merged-source Nostr progress: feat(video-editor): pick common clip speeds with one tap. Fold into sourced diVine addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/divinevideo/divine-mobile/pull/9601
Cited story evidence: https://github.com/divinevideo/divine-mobile/pull/9601

### diVine PR 9658 — SKIP

Test/CI/internal cleanup only; no new Nostr runtime, user workflow or independently reviewable protocol milestone.

Primary: https://github.com/divinevideo/divine-mobile/pull/9658

### diVine PR 9661 — SKIP

Diagnostic logging of existing sign-in/upload behavior

Primary: https://github.com/divinevideo/divine-mobile/pull/9661

### diVine PR 9603 — FOLD

Material merged-source Nostr progress: fix(dm): stop trusting retired moderation keys for minors, labels and reports. Fold into sourced diVine addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/divinevideo/divine-mobile/pull/9603
Cited story evidence: https://github.com/divinevideo/divine-mobile/pull/9603

### diVine PR 9644 — SKIP

Navigation analytics scheduling only

Primary: https://github.com/divinevideo/divine-mobile/pull/9644

### Buzz PR 7969 — FOLD

Material merged-source Nostr progress: feat(buzz-relay): idempotent owner community deletion with quota reservation. Fold into sourced Buzz addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/block/buzz/pull/7969
Cited story evidence: https://github.com/block/buzz/pull/7969

### Buzz PR 7896 — FOLD

Material merged-source Nostr progress: feat(mobile): show contextual names in lists, Search and Pulse. Fold into sourced Buzz addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/block/buzz/pull/7896
Cited story evidence: https://github.com/block/buzz/pull/7896

### Buzz PR 5997 — SKIP

AI harness executable discovery, no Nostr surface

Primary: https://github.com/block/buzz/pull/5997

### Buzz PR 7981 — SKIP

Test/CI/internal cleanup only; no new Nostr runtime, user workflow or independently reviewable protocol milestone.

Primary: https://github.com/block/buzz/pull/7981

### Buzz PR 7980 — SKIP

Release bookkeeping: substantive release research belongs to root release triage

Primary: https://github.com/block/buzz/pull/7980

### Buzz PR 4846 — SKIP

Third-party AI guide link repair, no Nostr surface

Primary: https://github.com/block/buzz/pull/4846

### Buzz PR 6515 — FOLD

Material merged-source Nostr progress: fix(db): audit partition catalog before creation. Fold into sourced Buzz addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/block/buzz/pull/6515
Cited story evidence: https://github.com/block/buzz/pull/6515

### Buzz PR 7895 — FOLD

Material merged-source Nostr progress: feat(mobile): show contextual names in channel conversations. Fold into sourced Buzz addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/block/buzz/pull/7895
Cited story evidence: https://github.com/block/buzz/pull/7895

### Buzz PR 7224 — FOLD

Material merged-source Nostr progress: feat(buzz-relay): NIP-FI stateless enforcement (S3) — upgrade gate, NIP-42 pairing, session lifetime, JWKS warm. Fold into sourced Buzz addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/block/buzz/pull/7224
Cited story evidence: https://github.com/block/buzz/pull/7224

### Buzz PR 2255 — SKIP

Download-page navigation polish below materiality threshold

Primary: https://github.com/block/buzz/pull/2255

### Buzz PR 4486 — SKIP

Specification comparison-operator formatting only; vectors/wire unchanged

Primary: https://github.com/block/buzz/pull/4486

### Buzz PR 7809 — SKIP

Early push suppression design with wire/synchronization unresolved; insufficient mature milestone

Primary: https://github.com/block/buzz/pull/7809

### Buzz PR 7894 — FOLD

Material merged-source Nostr progress: feat(mobile): add the contextual identity-name resolver. Fold into sourced Buzz addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/block/buzz/pull/7894
Cited story evidence: https://github.com/block/buzz/pull/7894

### Buzz PR 7830 — FOLD

Material merged-source Nostr progress: Automate owner deletion preparation. Fold into sourced Buzz addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/block/buzz/pull/7830
Cited story evidence: https://github.com/block/buzz/pull/7830

### Mostro Mobile PR 733 — SKIP

Fiat payment-method list only, no Nostr transport delta

Primary: https://github.com/MostroP2P/mobile/pull/733

### Mostro PR 923 — FOLD

Material merged-source Nostr progress: fix(dispute): make the dispute writes atomic (#921). Fold into sourced Mostro addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/MostroP2P/mostro/pull/923
Cited story evidence: https://github.com/MostroP2P/mostro/pull/923

### Mostro PR 1008 — SKIP

Test/CI/internal cleanup only; no new Nostr runtime, user workflow or independently reviewable protocol milestone.

Primary: https://github.com/MostroP2P/mostro/pull/1008

### Mostro PR 945 — FOLD

Material merged-source Nostr progress: fix: notify solver when dispute closes after user resolution. Fold into sourced Mostro addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/MostroP2P/mostro/pull/945
Cited story evidence: https://github.com/MostroP2P/mostro/pull/945

### Mostro PR 1006 — FOLD

Material merged-source Nostr progress: fix: recognize trade keys when create/take is accepted. Fold into sourced Mostro addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/MostroP2P/mostro/pull/1006
Cited story evidence: https://github.com/MostroP2P/mostro/pull/1006

### Conduit PR 591 — SKIP

Preview hosting rename/dependency patch, no distinct Nostr functionality

Primary: https://github.com/Conduit-BTC/conduit-mono/pull/591

### Conduit PR 575 — FOLD

Material merged-source Nostr progress: fix(market): use plain NIP-50 for ranked product search. Fold into sourced Conduit addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/Conduit-BTC/conduit-mono/pull/575
Cited story evidence: https://github.com/Conduit-BTC/conduit-mono/pull/575

### ZapTracker PR 133 — FOLD

Material merged-source Nostr progress: Replace Lightning Network stats with Nostr network stats. Fold into sourced ZapTracker addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/pratik227/zap_dashboard/pull/133
Cited story evidence: https://github.com/pratik227/zap_dashboard/pull/133

### ZapTracker PR 135 — FOLD

Material merged-source Nostr progress: Add Nostr quote engagement metrics. Fold into sourced ZapTracker addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/pratik227/zap_dashboard/pull/135
Cited story evidence: https://github.com/pratik227/zap_dashboard/pull/135

### ZapTracker PR 138 — SKIP

Test/CI/internal cleanup only; no new Nostr runtime, user workflow or independently reviewable protocol milestone.

Primary: https://github.com/pratik227/zap_dashboard/pull/138

### ZapTracker PR 137 — SKIP

Blank primary PR body; exact files read yielded no output under quota guard, no verified material claim

Primary: https://github.com/pratik227/zap_dashboard/pull/137

### ZapTracker PR 136 — SKIP

Blank primary PR body; exact files read yielded no output under quota guard, no verified material claim

Primary: https://github.com/pratik227/zap_dashboard/pull/136

### ZapTracker PR 129 — SKIP

Blank primary PR body; exact files read yielded no output under quota guard, no verified material claim

Primary: https://github.com/pratik227/zap_dashboard/pull/129

### earthly PR 30 — FOLD

Material merged-source Nostr progress: Fix Android SDK setup and prepare release 0.1.12. Fold into sourced earthly addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/zeSchlausKwab/earthly/pull/30
Cited story evidence: https://github.com/zeSchlausKwab/earthly/pull/30

### earthly PR 29 — FOLD

Material merged-source Nostr progress: Release 0.1.11: GMapper configurations and chat improvements. Fold into sourced earthly addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/zeSchlausKwab/earthly/pull/29
Cited story evidence: https://github.com/zeSchlausKwab/earthly/pull/29

### @elisym/cli PR 137 — FOLD

Material merged-source Nostr progress: Commerce: Tempo payments in the checkout and the merchant node (P3). Fold into sourced @elisym/cli addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/elisymlabs/elisym/pull/137
Cited story evidence: https://github.com/elisymlabs/elisym/pull/137

### @elisym/cli PR 136 — FOLD

Material merged-source Nostr progress: MCP: buy_product and get_order for commerce products (P5a). Fold into sourced @elisym/cli addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/elisymlabs/elisym/pull/136
Cited story evidence: https://github.com/elisymlabs/elisym/pull/136

### @elisym/cli PR 138 — SKIP

Release packaging only; author explicitly states merge publishes nothing

Primary: https://github.com/elisymlabs/elisym/pull/138

### @elisym/cli PR 134 — SKIP

Documentation for implementation already included; no separate runtime milestone

Primary: https://github.com/elisymlabs/elisym/pull/134

### @elisym/cli PR 135 — SKIP

Documentation deploy cache only

Primary: https://github.com/elisymlabs/elisym/pull/135

### nostream PR 788 — FOLD

Material merged-source Nostr progress: feat(nip56): hide events matching an actionable report. Fold into sourced nostream addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/cameri/nostream/pull/788
Cited story evidence: https://github.com/cameri/nostream/pull/788

### nostr-tools PR 564 — SKIP

Documents existing verification cache semantics; no new validation behavior or fix

Primary: https://github.com/nbd-wtf/nostr-tools/pull/564

### Dart NDK PR 852 — FOLD

Material merged-source Nostr progress: feat: send NIP-46 client metadata and requested perms on bunker connect. Fold into sourced Dart NDK addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/relaystr/ndk/pull/852
Cited story evidence: https://github.com/relaystr/ndk/pull/852

### Dart NDK PR 863 — SKIP

File-picker dependency compatibility only

Primary: https://github.com/relaystr/ndk/pull/863

### Dart NDK PR 860 — FOLD

Material merged-source Nostr progress: fix: send private NIP-01 compliant request ids. Fold into sourced Dart NDK addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/relaystr/ndk/pull/860
Cited story evidence: https://github.com/relaystr/ndk/pull/860

### rust-nostr PR 1478 — FOLD

Material merged-source Nostr progress: sdk: require correlated COUNT results and preserve waiter receive errors. Fold into sourced rust-nostr addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/nostrdevkit/nostr/pull/1478
Cited story evidence: https://github.com/nostrdevkit/nostr/pull/1478

### Zeus PR 4423 — SKIP

Lightning node refetch only, no direct Nostr surface

Primary: https://github.com/ZeusLN/zeus/pull/4423

### Zeus PR 4788 — SKIP

Wallet settings data repair only, no direct Nostr surface

Primary: https://github.com/ZeusLN/zeus/pull/4788

### MintRadar PR 107 — SKIP

Test/CI/internal cleanup only; no new Nostr runtime, user workflow or independently reviewable protocol milestone.

Primary: https://github.com/hroomnik007/MintRadar/pull/107

### MintRadar PR 106 — SKIP

Cashu mint fees only, no direct Nostr integration change

Primary: https://github.com/hroomnik007/MintRadar/pull/106

### MintRadar PR 105 — SKIP

Cashu token inspector layout only

Primary: https://github.com/hroomnik007/MintRadar/pull/105

### MintRadar PR 104 — SKIP

Cashu mint wizard layout only

Primary: https://github.com/hroomnik007/MintRadar/pull/104

### lawalletio/lawallet-nwc PR 322 — SKIP

Card-wallet REST rebinding, no new NWC integration behavior

Primary: https://github.com/lawalletio/lawallet-nwc/pull/322

### lawalletio/lawallet-nwc PR 316 — FOLD

Material merged-source Nostr progress: feat(cards): LUD-19 payLink for BoltCard top-up. Fold into sourced lawalletio/lawallet-nwc addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/lawalletio/lawallet-nwc/pull/316
Cited story evidence: https://github.com/lawalletio/lawallet-nwc/pull/316

### lawalletio/lawallet-nwc PR 319 — FOLD

Material merged-source Nostr progress: feat: BoltCard payLink and payer notes on send. Fold into sourced lawalletio/lawallet-nwc addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/lawalletio/lawallet-nwc/pull/319
Cited story evidence: https://github.com/lawalletio/lawallet-nwc/pull/319

### Angor PR 978 — SKIP

Bitcoin indexer/testing documentation; hosting a relay does not establish Nostr runtime progress

Primary: https://github.com/block-core/angor/pull/978

### Routstrd PR 113 — SKIP

Cashu mint selection only, no direct Nostr behavior

Primary: https://github.com/Routstr/routstrd/pull/113

### castr.me PR 26 — SKIP

Hosting runtime upgrade only

Primary: https://github.com/dergigi/castr.me/pull/26

### Zap Cooking PR 766 — SKIP

Single-account temporary spam denylist, explicitly not broader moderation capability

Primary: https://github.com/zapcooking/frontend/pull/766

### Zap Cooking PR 765 — SKIP

Removal of one dead relay below substantive new-change threshold

Primary: https://github.com/zapcooking/frontend/pull/765

### Zap Cooking PR 764 — FOLD

Material merged-source Nostr progress: fix(mute): ProfileSheet mute keeps every existing mute-list entry. Fold into sourced Zap Cooking addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/zapcooking/frontend/pull/764
Cited story evidence: https://github.com/zapcooking/frontend/pull/764

### Zap Cooking PR 763 — FOLD

Material merged-source Nostr progress: fix(nip05): require NIP-98 signer to match the claimed pubkey. Fold into sourced Zap Cooking addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/zapcooking/frontend/pull/763
Cited story evidence: https://github.com/zapcooking/frontend/pull/763

### mesh-llm PR 2121 — SKIP

LLM wallet build defaults, no direct Nostr surface

Primary: https://github.com/Mesh-LLM/mesh-llm/pull/2121

### mesh-llm PR 2117 — SKIP

Non-Nostr mesh frame authentication

Primary: https://github.com/Mesh-LLM/mesh-llm/pull/2117

### mesh-llm PR 2118 — SKIP

Test/CI/internal cleanup only; no new Nostr runtime, user workflow or independently reviewable protocol milestone.

Primary: https://github.com/Mesh-LLM/mesh-llm/pull/2118

### mesh-llm PR 2113 — SKIP

LLM performance controls, no Nostr surface

Primary: https://github.com/Mesh-LLM/mesh-llm/pull/2113

### mesh-llm PR 2111 — SKIP

LLM wallet/payment profile restart behavior, no Nostr surface

Primary: https://github.com/Mesh-LLM/mesh-llm/pull/2111

### mesh-llm PR 2120 — SKIP

LLM model setup docs, no Nostr surface

Primary: https://github.com/Mesh-LLM/mesh-llm/pull/2120

### mesh-llm PR 2102 — SKIP

LLM analytics instrumentation, no Nostr surface

Primary: https://github.com/Mesh-LLM/mesh-llm/pull/2102

### mesh-llm PR 2114 — SKIP

LLM engine guide, no Nostr surface

Primary: https://github.com/Mesh-LLM/mesh-llm/pull/2114

### Marmot Protocol PR 427 — FOLD

Material merged-source Nostr progress: Replace multi-device draft with an ideas-surface walkthrough. Fold into sourced Marmot Protocol addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/marmot-protocol/marmot/pull/427
Cited story evidence: https://github.com/marmot-protocol/marmot/pull/427

### Marmot Protocol (mdk) PR 2101 — SKIP

APFS test fixture only; production attachment validation unchanged

Primary: https://github.com/marmot-protocol/mdk/pull/2101

### Marmot Protocol (mdk) PR 2105 — FOLD

Material merged-source Nostr progress: Add NIP-30 tagged sends and window emoji tags. Fold into sourced Marmot Protocol (mdk) addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/marmot-protocol/mdk/pull/2105
Cited story evidence: https://github.com/marmot-protocol/mdk/pull/2105

### Marmot Protocol (mdk) PR 1929 — FOLD

Material merged-source Nostr progress: Expose optional group app components. Fold into sourced Marmot Protocol (mdk) addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/marmot-protocol/mdk/pull/1929
Cited story evidence: https://github.com/marmot-protocol/mdk/pull/1929

### Marmot Protocol (mdk) PR 1969 — FOLD

Material merged-source Nostr progress: Merge the published kind:0 profile in account_publish_profile instead of replacing it. Fold into sourced Marmot Protocol (mdk) addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/marmot-protocol/mdk/pull/1969
Cited story evidence: https://github.com/marmot-protocol/mdk/pull/1969

### Marmot Protocol (mdk) PR 2097 — FOLD

Material merged-source Nostr progress: Align encrypted-media read timeout with resumable body idle policy. Fold into sourced Marmot Protocol (mdk) addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/marmot-protocol/mdk/pull/2097
Cited story evidence: https://github.com/marmot-protocol/mdk/pull/2097

### Marmot Protocol (mdk) PR 2098 — FOLD

Material merged-source Nostr progress: Report the startup stage an account worker was blocked in when its ready-wait expires. Fold into sourced Marmot Protocol (mdk) addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/marmot-protocol/mdk/pull/2098
Cited story evidence: https://github.com/marmot-protocol/mdk/pull/2098

### Marmot Protocol (mdk) PR 2096 — FOLD

Material merged-source Nostr progress: Expose admin group profile updates to agent connector. Fold into sourced Marmot Protocol (mdk) addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/marmot-protocol/mdk/pull/2096
Cited story evidence: https://github.com/marmot-protocol/mdk/pull/2096

### Marmot Protocol (mdk) PR 2095 — FOLD

Material merged-source Nostr progress: Remove the unreachable commit-merge arm from direct ingest. Fold into sourced Marmot Protocol (mdk) addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/marmot-protocol/mdk/pull/2095
Cited story evidence: https://github.com/marmot-protocol/mdk/pull/2095

### Marmot Protocol (mdk) PR 2094 — FOLD

Material merged-source Nostr progress: Expose per-voter poll selections through the bindings. Fold into sourced Marmot Protocol (mdk) addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/marmot-protocol/mdk/pull/2094
Cited story evidence: https://github.com/marmot-protocol/mdk/pull/2094

### Marmot Protocol (mdk) PR 2093 — FOLD

Material merged-source Nostr progress: Stop discarding pending messages when convergence selects no branch. Fold into sourced Marmot Protocol (mdk) addendum, retaining implementation/test/deployment limitations.

Primary: https://github.com/marmot-protocol/mdk/pull/2093
Cited story evidence: https://github.com/marmot-protocol/mdk/pull/2093

### mouse484/astraea v5.35.180 — SKIP

Dependency-only TanStack query update; no changed Nostr feature or protocol behavior.

Primary: https://github.com/mouse484/astraea/releases/tag/v5.35.180

### nostr-wot/nostr-wot-extension v0.8.7 — FOLD

Exact-destination authentication grants and complete approved-event verification; internal wallet proof restrictions, payment preimage checks and local timed private-message previews.

Primary: https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.7, https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.7
Cited story evidence: https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.7

### 0xchat-app/0xchat-app-main v1.5.6-release — FOLD

Previously covered source security fixes now ship in1.5.6; additional Tor proxy/log privacy, relay recovery, account/signer retention and send failure fixes establish a distinct continuity delta.

Primary: https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.6-release, https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.6-release
Cited story evidence: https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.6-release

### nogringo/nostr-mail-client v0.17.0 — FOLD

New hidden mailbox-state/deletion synchronization, large-message Bcc protection, recipient read-relay delivery, folders/labels and composition changes; distinct from prior0.16.0.

Primary: https://github.com/nogringo/nostr-mail-client/releases/tag/v0.17.0, https://github.com/nogringo/nostr-mail-client/releases/tag/v0.17.0
Cited story evidence: https://github.com/nogringo/nostr-mail-client/releases/tag/v0.17.0

### DavidGershony/openChat v0.7.8 — FOLD

Fold into existing Scramble section: manual all-address group-history recovery, native member administration and held-message drain fix; never imply decryption of pre-join MLSepochs.

Primary: https://github.com/DavidGershony/Scramble/releases/tag/v0.7.8, https://github.com/DavidGershony/Scramble/releases/tag/v0.7.8
Cited story evidence: https://github.com/DavidGershony/Scramble/releases/tag/v0.7.8

### DavidGershony/openChat v0.7.7 — FOLD

Fold into existing Scramble section: manual all-address group-history recovery, native member administration and held-message drain fix; never imply decryption of pre-join MLSepochs.

Primary: https://github.com/DavidGershony/Scramble/releases/tag/v0.7.7, https://github.com/DavidGershony/Scramble/releases/tag/v0.7.7
Cited story evidence: https://github.com/DavidGershony/Scramble/releases/tag/v0.7.7

### DavidGershony/openChat v0.7.6 — FOLD

Fold into existing Scramble section: manual all-address group-history recovery, native member administration and held-message drain fix; never imply decryption of pre-join MLSepochs.

Primary: https://github.com/DavidGershony/Scramble/releases/tag/v0.7.6, https://github.com/DavidGershony/Scramble/releases/tag/v0.7.6
Cited story evidence: https://github.com/DavidGershony/Scramble/releases/tag/v0.7.6

### block/buzz desktop-v0.5.26 — FOLD

Tagged desktop/shared release ships previously described source changes, adds relay admin console and cross-device sidebar synchronization; repository/mobile notes retain separate source-level status.

Primary: https://github.com/block/buzz/releases/tag/desktop-v0.5.26, https://github.com/block/buzz/releases/tag/desktop-v0.5.26
Cited story evidence: https://github.com/block/buzz/releases/tag/desktop-v0.5.26

### MostroP2P/mostro v0.19.0 — FOLD

v0.19.0 now publishes daemon transport removal already in existing development section; replace obsolete source-only status, include published_at tags, restoration and first-relay acceptance.

Primary: https://github.com/MostroP2P/mostro/releases/tag/v0.19.0, https://github.com/MostroP2P/mostro/releases/tag/v0.19.0
Cited story evidence: https://github.com/MostroP2P/mostro/releases/tag/v0.19.0

### jesuspirate/chama v6.4.16 — FOLD

Group6.4.14–6.4.16: signed cancellation propagates listing removal, recipient opaque wake tags and per-trade replay repair alerts, signed event chronology makes client trade state converge.

Primary: https://github.com/jesuspirate/chama/releases/tag/v6.4.16, https://github.com/jesuspirate/chama/releases/tag/v6.4.16
Cited story evidence: https://github.com/jesuspirate/chama/releases/tag/v6.4.16

### jesuspirate/chama v6.4.15 — FOLD

Group6.4.14–6.4.16: signed cancellation propagates listing removal, recipient opaque wake tags and per-trade replay repair alerts, signed event chronology makes client trade state converge. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/jesuspirate/chama/releases/tag/v6.4.15, https://github.com/jesuspirate/chama/releases/tag/v6.4.16
Cited story evidence: https://github.com/jesuspirate/chama/releases/tag/v6.4.16

### jesuspirate/chama v6.4.14 — FOLD

Group6.4.14–6.4.16: signed cancellation propagates listing removal, recipient opaque wake tags and per-trade replay repair alerts, signed event chronology makes client trade state converge. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/jesuspirate/chama/releases/tag/v6.4.14, https://github.com/jesuspirate/chama/releases/tag/v6.4.16
Cited story evidence: https://github.com/jesuspirate/chama/releases/tag/v6.4.16

### moogmodular/earthly v0.1.12 — FOLD

Earthly is aNostr collaborative mapper (exact-tag README verified); v0.1.12 adds reusable public/private configurations, Maplet discovery and encrypted connection sharing. Canonical repository redirected tozeSchlausKwab/earthly.

Primary: https://github.com/zeSchlausKwab/earthly/releases/tag/v0.1.12, https://github.com/zeSchlausKwab/earthly/releases/tag/v0.1.12
Cited story evidence: https://github.com/zeSchlausKwab/earthly/releases/tag/v0.1.12

### elisymlabs/elisym @elisym/sdk@0.41.0 — FOLD

Group shared monorepo tags into existing commerce story; self-hosted merchant-node distribution and MCPbuy_product/get_order add concrete Nostr-commerce surfaces. Do not assign all shared release-body features independently to every package. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/elisymlabs/elisym/releases/tag/%40elisym/sdk%400.41.0, https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.2.0
Cited story evidence: https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.2.0

### elisymlabs/elisym @elisym/pay-core@0.1.3 — FOLD

Fold Tempo payment integration into existing commerce story; payment-rail delta alone is not independent Nostr news. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/elisymlabs/elisym/releases/tag/%40elisym/pay-core%400.1.3, https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.2.0
Cited story evidence: https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.2.0

### elisymlabs/elisym @elisym/merchant-node@0.2.0 — FOLD

Fold Tempo payment integration into existing commerce story; payment-rail delta alone is not independent Nostr news. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/elisymlabs/elisym/releases/tag/%40elisym/merchant-node%400.2.0, https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.2.0
Cited story evidence: https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.2.0

### elisymlabs/elisym @elisym/merchant-node@0.1.0 — FOLD

Group shared monorepo tags into existing commerce story; self-hosted merchant-node distribution and MCPbuy_product/get_order add concrete Nostr-commerce surfaces. Do not assign all shared release-body features independently to every package. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/elisymlabs/elisym/releases/tag/%40elisym/merchant-node%400.1.0, https://github.com/elisymlabs/elisym/releases/tag/%40elisym%2Fmerchant-node%400.1.0
Cited story evidence: https://github.com/elisymlabs/elisym/releases/tag/%40elisym%2Fmerchant-node%400.1.0

### elisymlabs/elisym @elisym/mcp@0.31.1 — FOLD

Fold Tempo payment integration into existing commerce story; payment-rail delta alone is not independent Nostr news. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/elisymlabs/elisym/releases/tag/%40elisym/mcp%400.31.1, https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.2.0
Cited story evidence: https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.2.0

### elisymlabs/elisym @elisym/mcp@0.31.0 — FOLD

Group shared monorepo tags into existing commerce story; self-hosted merchant-node distribution and MCPbuy_product/get_order add concrete Nostr-commerce surfaces. Do not assign all shared release-body features independently to every package. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/elisymlabs/elisym/releases/tag/%40elisym/mcp%400.31.0, https://github.com/elisymlabs/elisym/releases/tag/%40elisym%2Fmcp%400.31.0
Cited story evidence: https://github.com/elisymlabs/elisym/releases/tag/%40elisym%2Fmcp%400.31.0

### elisymlabs/elisym @elisym/commerce@0.4.0 — FOLD

Fold Tempo payment integration into existing commerce story; payment-rail delta alone is not independent Nostr news. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.4.0, https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.2.0
Cited story evidence: https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.2.0

### elisymlabs/elisym @elisym/commerce@0.3.0 — FOLD

Group shared monorepo tags into existing commerce story; self-hosted merchant-node distribution and MCPbuy_product/get_order add concrete Nostr-commerce surfaces. Do not assign all shared release-body features independently to every package. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.3.0, https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.2.0
Cited story evidence: https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.2.0

### elisymlabs/elisym @elisym/cli@0.33.3 — FOLD

Group shared monorepo tags into existing commerce story; self-hosted merchant-node distribution and MCPbuy_product/get_order add concrete Nostr-commerce surfaces. Do not assign all shared release-body features independently to every package. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/elisymlabs/elisym/releases/tag/%40elisym/cli%400.33.3, https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.2.0
Cited story evidence: https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.2.0

### irislib/nostr-double-ratchet nostr-double-ratchet-ts-v0.0.175 — FOLD

Extend existing ratchet story through.175: durable handoffs saved before publishing, local group publication scope for removal-aware retry cancellation and device-label retention; unchanged signed wire format.

Primary: https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.175, https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.175
Cited story evidence: https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.175

### irislib/nostr-double-ratchet nostr-double-ratchet-ts-v0.0.174 — FOLD

Extend existing ratchet story through.175: durable handoffs saved before publishing, local group publication scope for removal-aware retry cancellation and device-label retention; unchanged signed wire format. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.174, https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.171
Cited story evidence: https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.171

### irislib/nostr-double-ratchet nostr-double-ratchet-ts-v0.0.173 — FOLD

Extend existing ratchet story through.175: durable handoffs saved before publishing, local group publication scope for removal-aware retry cancellation and device-label retention; unchanged signed wire format.

Primary: https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.173, https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.173
Cited story evidence: https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.173

### mmalmi/nostr-pubsub nostr-pubsub-ts-v0.5.9 — FOLD

Group0.5.7–.13: persistent event/outbox runtime, bounded exact relay/peer batching, source-bound evidence and durable admission before complete-history status. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.9, https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.13
Cited story evidence: https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.13

### mmalmi/nostr-pubsub nostr-pubsub-ts-v0.5.8 — FOLD

Group0.5.7–.13: persistent event/outbox runtime, bounded exact relay/peer batching, source-bound evidence and durable admission before complete-history status. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.8, https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.13
Cited story evidence: https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.13

### mmalmi/nostr-pubsub nostr-pubsub-ts-v0.5.7 — FOLD

Group0.5.7–.13: persistent event/outbox runtime, bounded exact relay/peer batching, source-bound evidence and durable admission before complete-history status. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.7, https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.13
Cited story evidence: https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.13

### mmalmi/nostr-pubsub nostr-pubsub-ts-v0.5.13 — FOLD

Group0.5.7–.13: persistent event/outbox runtime, bounded exact relay/peer batching, source-bound evidence and durable admission before complete-history status.

Primary: https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.13, https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.13
Cited story evidence: https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.13

### mmalmi/nostr-pubsub nostr-pubsub-ts-v0.5.12 — FOLD

Group0.5.7–.13: persistent event/outbox runtime, bounded exact relay/peer batching, source-bound evidence and durable admission before complete-history status. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.12, https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.13
Cited story evidence: https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.13

### mmalmi/nostr-pubsub nostr-pubsub-ts-v0.5.11 — FOLD

Group0.5.7–.13: persistent event/outbox runtime, bounded exact relay/peer batching, source-bound evidence and durable admission before complete-history status. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.11, https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.13
Cited story evidence: https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.13

### mmalmi/nostr-pubsub nostr-pubsub-ts-v0.5.10 — FOLD

Group0.5.7–.13: persistent event/outbox runtime, bounded exact relay/peer batching, source-bound evidence and durable admission before complete-history status. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.10, https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.13
Cited story evidence: https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.13

### mmalmi/fips-ts runtime-v0.0.45 — FOLD

Fold capacity-aware signaling routes and bounded setup recovery into shared event/file runtime story; retain native-peer upgrade requirement, no standalone package churn entry.

Primary: https://github.com/mmalmi/fips-ts/releases/tag/runtime-v0.0.45, https://github.com/mmalmi/fips-ts/releases/tag/runtime-v0.0.45
Cited story evidence: https://github.com/mmalmi/fips-ts/releases/tag/runtime-v0.0.45

### mmalmi/fips-ts runtime-v0.0.44 — FOLD

Fold capacity-aware signaling routes and bounded setup recovery into shared event/file runtime story; retain native-peer upgrade requirement, no standalone package churn entry. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/mmalmi/fips-ts/releases/tag/runtime-v0.0.44, https://github.com/mmalmi/fips-ts/releases/tag/runtime-v0.0.45
Cited story evidence: https://github.com/mmalmi/fips-ts/releases/tag/runtime-v0.0.45

### mmalmi/hashtree hashtree-ts-runtime-v0.5.9 — FOLD

Fold0.5.8–.13 shared event worker/index/outbox and compatible FIPSadapter adoption into runtime story; adapter-only releases are dependency consumption of already described behavior. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.9, https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.13
Cited story evidence: https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.13

### mmalmi/hashtree hashtree-ts-runtime-v0.5.8 — FOLD

Fold0.5.8–.13 shared event worker/index/outbox and compatible FIPSadapter adoption into runtime story; adapter-only releases are dependency consumption of already described behavior. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.8, https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.13
Cited story evidence: https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.13

### mmalmi/hashtree hashtree-ts-runtime-v0.5.13 — FOLD

Fold0.5.8–.13 shared event worker/index/outbox and compatible FIPSadapter adoption into runtime story; adapter-only releases are dependency consumption of already described behavior.

Primary: https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.13, https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.13
Cited story evidence: https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.13

### mmalmi/hashtree hashtree-ts-runtime-v0.5.12 — FOLD

Fold0.5.8–.13 shared event worker/index/outbox and compatible FIPSadapter adoption into runtime story; adapter-only releases are dependency consumption of already described behavior. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.12, https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.13
Cited story evidence: https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.13

### mmalmi/hashtree hashtree-ts-runtime-v0.5.11 — FOLD

Fold0.5.8–.13 shared event worker/index/outbox and compatible FIPSadapter adoption into runtime story; adapter-only releases are dependency consumption of already described behavior. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.11, https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.13
Cited story evidence: https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.13

### mmalmi/hashtree hashtree-ts-runtime-v0.5.10 — FOLD

Fold0.5.8–.13 shared event worker/index/outbox and compatible FIPSadapter adoption into runtime story; adapter-only releases are dependency consumption of already described behavior. Explicitly folded into the same project release-series story using its cited representative tag; series component release notes were reviewed in full by release triage.

Primary: https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.10, https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.13
Cited story evidence: https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.13

### mmalmi/iris-kit runtime-v0.2.6 — FOLD

Fold transport-neutral NIP46signer and persistent app client, then immediate exact-ID cached retrieval into runtime story; prefix/replaceable queries retain history-completion requirement.

Primary: https://github.com/mmalmi/iris-kit/releases/tag/runtime-v0.2.6, https://github.com/mmalmi/iris-kit/releases/tag/runtime-v0.2.6
Cited story evidence: https://github.com/mmalmi/iris-kit/releases/tag/runtime-v0.2.6

### mmalmi/iris-kit runtime-v0.2.5 — FOLD

Fold transport-neutral NIP46signer and persistent app client, then immediate exact-ID cached retrieval into runtime story; prefix/replaceable queries retain history-completion requirement.

Primary: https://github.com/mmalmi/iris-kit/releases/tag/runtime-v0.2.5, https://github.com/mmalmi/iris-kit/releases/tag/runtime-v0.2.5
Cited story evidence: https://github.com/mmalmi/iris-kit/releases/tag/runtime-v0.2.5

### NostrBox Locate 0.3.1 — SKIP

No substantive release notes or verifiable distinct Nostr progress; version/listing metadata alone below eligibility gate.

Primary: https://primal.net/e/e88ac513a40b7656460a71c3c57de359c9212edaef9b75db427a3e0554084da5

### Iris Chat 2026.9.30.2 — FOLD

Distinct user/protocol changes recorded in signed notes; folded into project story.

Primary: https://primal.net/e/89ec93e25caf31831714e807c927b6d50d3d5fc38044df845163ff656db3f711, https://primal.net/e/89ec93e25caf31831714e807c927b6d50d3d5fc38044df845163ff656db3f711
Cited story evidence: https://primal.net/e/89ec93e25caf31831714e807c927b6d50d3d5fc38044df845163ff656db3f711

### Noteds 0.1.2 — SKIP

No substantive release notes or verifiable distinct Nostr progress; version/listing metadata alone below eligibility gate.

Primary: https://primal.net/e/c07170dfa8bb4cf4ab1f61736a5c136db58da0fbe32c853b4b36c65ccc7bb479

### Noteds 0.1.1 — SKIP

No substantive release notes or verifiable distinct Nostr progress; version/listing metadata alone below eligibility gate.

Primary: https://primal.net/e/1cda0d82ac26b1a8b3d18c88babc9a87bb5ce4573de13eea5468d192dec60660

### Armada 0.63.2 — FOLD

Distinct user/protocol changes recorded in signed notes; folded into project story.

Primary: https://primal.net/e/ad0f6ad1a7730a400e8257c494c53ef14597c55a24e01b05dd2b2301c7d3aa36, https://primal.net/e/ad0f6ad1a7730a400e8257c494c53ef14597c55a24e01b05dd2b2301c7d3aa36
Cited story evidence: https://primal.net/e/ad0f6ad1a7730a400e8257c494c53ef14597c55a24e01b05dd2b2301c7d3aa36

### Iris Chat 2026.9.30.1 — FOLD

Distinct user/protocol changes recorded in signed notes; folded into project story.

Primary: https://primal.net/e/17fd3f325dda1feb0c1e51c6e1af0f7b3efe42ecff75e9527ac435cdc6a30c7a, https://primal.net/e/17fd3f325dda1feb0c1e51c6e1af0f7b3efe42ecff75e9527ac435cdc6a30c7a
Cited story evidence: https://primal.net/e/17fd3f325dda1feb0c1e51c6e1af0f7b3efe42ecff75e9527ac435cdc6a30c7a

### Noteds 0.1.0 — SKIP

No substantive release notes or verifiable distinct Nostr progress; version/listing metadata alone below eligibility gate.

Primary: https://primal.net/e/7c55818f9d1fb6d08f9d1031c9a5118eeebf4a4381a6c74ca2a7caa35b510923

### Noteds 0.0.1 — SKIP

No substantive release notes or verifiable distinct Nostr progress; version/listing metadata alone below eligibility gate.

Primary: https://primal.net/e/40d7cdbdc42847441aab387c22b96d84e14f5dfdebfe64cedce690920ac7e387

### White Noise: Secure Chat 2026.9.30 — FOLD

Distinct user/protocol changes recorded in signed notes; folded into project story. Explicitly folded into the cited same-app release-series story; signed source notes remain preserved.

Primary: https://primal.net/e/ac9a14c2dcbfa5d14bf554574df3616ea8fa340d7e89b7a771360a9cc019b952, https://github.com/marmot-protocol/whitenoise-android/releases/tag/android-v2026.9.30
Cited story evidence: https://github.com/marmot-protocol/whitenoise-android/releases/tag/android-v2026.9.30

### Trails Coffee 3.5.24 — SKIP

No substantive release notes or verifiable distinct Nostr progress; version/listing metadata alone below eligibility gate.

Primary: https://primal.net/e/6b3c8d03366337806032556bb7b84f4803f5a149769a26fefb24843fae1b4bb9

### PosterChan 1.0.2409 — SKIP

No substantive release notes or verifiable distinct Nostr progress; version/listing metadata alone below eligibility gate.

Primary: https://primal.net/e/0af1d509e7a18b4754724e10a08308fbb57362266695c9aceaf5889463272cb1

### Chama 6.4.16 — FOLD

Distinct user/protocol changes recorded in signed notes; folded into project story. Explicitly folded into the cited same-app release-series story; signed source notes remain preserved.

Primary: https://primal.net/e/f9da81a6b1a8e585896796079a1f3303a68727015f32d8823b6edc2e52811278, https://github.com/jesuspirate/chama/releases/tag/v6.4.16
Cited story evidence: https://github.com/jesuspirate/chama/releases/tag/v6.4.16

### PosterChan 1.0.2408 — SKIP

No substantive release notes or verifiable distinct Nostr progress; version/listing metadata alone below eligibility gate.

Primary: https://primal.net/e/91e5a0c2bbea1a4520aa34228745d5fda814de6e387080ef6a3af0e6e8604bbb

### Mangatsu 0.1.11 — SKIP

No substantive release notes or verifiable distinct Nostr progress; version/listing metadata alone below eligibility gate.

Primary: https://primal.net/e/c6de61676b38d537d603047f904b1d1adc93c32c71248413062aa0f220d82021

### PosterChan 1.0.2407 — SKIP

No substantive release notes or verifiable distinct Nostr progress; version/listing metadata alone below eligibility gate.

Primary: https://primal.net/e/d6a8af25c96cb7b53f65cb827521650f0a9fe4fe8a373e07665905d25cd4da73

### Mangatsu 0.1.10 — SKIP

No substantive release notes or verifiable distinct Nostr progress; version/listing metadata alone below eligibility gate.

Primary: https://primal.net/e/d0a7ec78fcd8e3829a8495d1cf85d51bd016d7af6ff9fea56fcb014f24726b1e

### Nostr Compass 1.1.2 — FOLD

Distinct user/protocol changes recorded in signed notes; folded into project story. Explicitly folded into the cited same-app release-series story; signed source notes remain preserved.

Primary: https://primal.net/e/003c18f2ea16b8e22178fd9c6d7133871a5dcf4522c1e38e7c1df84462571ec7, https://gitworkshop.dev/npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923/relay.ngit.dev/nostr-compass-android
Cited story evidence: https://gitworkshop.dev/npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923/relay.ngit.dev/nostr-compass-android

### Mangatsu 0.1.9 — SKIP

No substantive release notes or verifiable distinct Nostr progress; version/listing metadata alone below eligibility gate.

Primary: https://primal.net/e/4c8ad49afdbc4db9e1b6f49e608aa2b35382436f6f806cdca9e0ac43fb0a75f4

### Mangatsu 0.1.8 — SKIP

No substantive release notes or verifiable distinct Nostr progress; version/listing metadata alone below eligibility gate.

Primary: https://primal.net/e/abb65fb54b1d504ac11dce67776cc024fe29f9a96ac89aa7bae7fad116a435e0

### Mangatsu 0.1.7 — SKIP

No substantive release notes or verifiable distinct Nostr progress; version/listing metadata alone below eligibility gate.

Primary: https://primal.net/e/44eeca2efe5c5a37f8d588e1446f0dbbdd5451e0c4db54467d263f936fbecd4a

### Mangatsu 0.1.6 — SKIP

No substantive release notes or verifiable distinct Nostr progress; version/listing metadata alone below eligibility gate.

Primary: https://primal.net/e/e01e7aa8f611d790b7c29329054e51e02f8a2d53e99bdbbf91df4f5e36226119

### Chama 6.4.15 — FOLD

Distinct user/protocol changes recorded in signed notes; folded into project story. Explicitly folded into the cited same-app release-series story; signed source notes remain preserved.

Primary: https://primal.net/e/d20bb056a9f260e512a77a0477b2fcc452080eec2084763f130cecf055800a59, https://github.com/jesuspirate/chama/releases/tag/v6.4.16
Cited story evidence: https://github.com/jesuspirate/chama/releases/tag/v6.4.16

### Mangatsu 0.1.5 — SKIP

No substantive release notes or verifiable distinct Nostr progress; version/listing metadata alone below eligibility gate.

Primary: https://primal.net/e/a982d80d82a16ddb29f37e4142b024f60c2abdd8e1acf3ed47b1519e59241210

### Armada 0.63.1 — FOLD

Distinct user/protocol changes recorded in signed notes; folded into project story.

Primary: https://primal.net/e/af3ff711c1c1daa4d6a621dc5add0615fc5d37fbb1de31395cb79dcdf820aaf1, https://primal.net/e/af3ff711c1c1daa4d6a621dc5add0615fc5d37fbb1de31395cb79dcdf820aaf1
Cited story evidence: https://primal.net/e/af3ff711c1c1daa4d6a621dc5add0615fc5d37fbb1de31395cb79dcdf820aaf1

### Nymbot - Private AI Assistant 1.0.7 — FOLD

Distinct user/protocol changes recorded in signed notes; folded into project story.

Primary: https://primal.net/e/affd11e97fb3438965780aa01732e8d0e0f9b2162b87ab0f3019dff93449673e, https://primal.net/e/affd11e97fb3438965780aa01732e8d0e0f9b2162b87ab0f3019dff93449673e
Cited story evidence: https://primal.net/e/affd11e97fb3438965780aa01732e8d0e0f9b2162b87ab0f3019dff93449673e

### Nostr Compass 1.1.1 — FOLD

Distinct user/protocol changes recorded in signed notes; folded into project story. Explicitly folded into the cited same-app release-series story; signed source notes remain preserved.

Primary: https://primal.net/e/824285261139e95ece800828a1af8ac43ec478a3569ef4a1770ecb41a440fb6b, https://gitworkshop.dev/npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923/relay.ngit.dev/nostr-compass-android
Cited story evidence: https://gitworkshop.dev/npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923/relay.ngit.dev/nostr-compass-android

### Nostr Compass 1.1.0 — FOLD

Distinct user/protocol changes recorded in signed notes; folded into project story. Explicitly folded into the cited same-app release-series story; signed source notes remain preserved.

Primary: https://primal.net/e/66579d6983ec7b628dec1e2dfe3c1a98203fb12b1cf3648d3f38612b06c5d7f4, https://gitworkshop.dev/npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923/relay.ngit.dev/nostr-compass-android
Cited story evidence: https://gitworkshop.dev/npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923/relay.ngit.dev/nostr-compass-android

### PosterChan 1.0.2406 — SKIP

No substantive release notes or verifiable distinct Nostr progress; version/listing metadata alone below eligibility gate.

Primary: https://primal.net/e/aa98c97110fbfdaec216a852b1e264ca2d7a56eaa937cfc1cc833f6c239fe580

### Chama 6.4.14 — FOLD

Distinct user/protocol changes recorded in signed notes; folded into project story. Explicitly folded into the cited same-app release-series story; signed source notes remain preserved.

Primary: https://primal.net/e/49326ac5822d3ca689093b60e349c3575a8ac7d05b8e6dce19988750afa495fd, https://github.com/jesuspirate/chama/releases/tag/v6.4.16
Cited story evidence: https://github.com/jesuspirate/chama/releases/tag/v6.4.16

### PosterChan 1.0.2405 — SKIP

No substantive release notes or verifiable distinct Nostr progress; version/listing metadata alone below eligibility gate.

Primary: https://primal.net/e/50602a0fb188b43020aacf7de20e9afc1a33723cb1b666717f8710a963b0c616

### Nostr Compass 1.0.0 — FOLD

Distinct user/protocol changes recorded in signed notes; folded into project story. Explicitly folded into the cited same-app release-series story; signed source notes remain preserved.

Primary: https://primal.net/e/8282c64231f2316c92098b40188cccd80e614609abe5a0f6f28fbc4c8452afc6, https://gitworkshop.dev/npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923/relay.ngit.dev/nostr-compass-android
Cited story evidence: https://gitworkshop.dev/npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923/relay.ngit.dev/nostr-compass-android

### LibreNostr 1.0.1 — FOLD

Distinct user/protocol changes recorded in signed notes; folded into project story.

Primary: https://primal.net/e/630becb73dbe7ba7c76a2d1970f1d7262a5afc33b02fc8002bef611cf638deab, https://primal.net/e/630becb73dbe7ba7c76a2d1970f1d7262a5afc33b02fc8002bef611cf638deab
Cited story evidence: https://primal.net/e/630becb73dbe7ba7c76a2d1970f1d7262a5afc33b02fc8002bef611cf638deab

### LibreNostr 1.0.0 — FOLD

Distinct user/protocol changes recorded in signed notes; folded into project story.

Primary: https://primal.net/e/4eeba660b6b789288954290497de89fe3222bfc955214647ead5d63e6031d927, https://primal.net/e/4eeba660b6b789288954290497de89fe3222bfc955214647ead5d63e6031d927
Cited story evidence: https://primal.net/e/4eeba660b6b789288954290497de89fe3222bfc955214647ead5d63e6031d927

### Cordn 0.5.1 — FOLD

Distinct user/protocol changes recorded in signed notes; folded into project story.

Primary: https://primal.net/e/23f7498e2e405e05c4d3075ccc522c753d80f37b954a81ff8ecb3268f2dc7dc6, https://primal.net/e/23f7498e2e405e05c4d3075ccc522c753d80f37b954a81ff8ecb3268f2dc7dc6
Cited story evidence: https://primal.net/e/23f7498e2e405e05c4d3075ccc522c753d80f37b954a81ff8ecb3268f2dc7dc6

### Nmail 0.17.0 — FOLD

Distinct user/protocol changes recorded in signed notes; folded into project story. Explicitly folded into the cited same-app release-series story; signed source notes remain preserved.

Primary: https://primal.net/e/ad512edf894395fe5124de9299e087f99e8c33d3f03d312c5e370aee89e92c01, https://github.com/nogringo/nostr-mail-client/releases/tag/v0.17.0
Cited story evidence: https://github.com/nogringo/nostr-mail-client/releases/tag/v0.17.0

### Nmail 0.17.0 — FOLD

Distinct user/protocol changes recorded in signed notes; folded into project story. Explicitly folded into the cited same-app release-series story; signed source notes remain preserved.

Primary: https://primal.net/e/500a8c46443ea07d9bc582d17fabece26e7303df4d100505394adff8021ea1fb, https://github.com/nogringo/nostr-mail-client/releases/tag/v0.17.0
Cited story evidence: https://github.com/nogringo/nostr-mail-client/releases/tag/v0.17.0

## Remaining gates

Missing manifest families: none.


## Deterministic final validation

The maintained selection coverage checker returned no errors for the current manifest, draft, 498 candidates, source provenance, project activity decisions and selected citations. The three new specification candidates have explicit dispositions: two skipped and the reviewable hidden-replies proposal included with its primary citation.

GATE: PASS — actual deterministic selection coverage validation.
