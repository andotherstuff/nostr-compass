# Selection coverage audit — 2026-09-09

This audit supersedes the coverage claims in `triage_2026-09-09.md` and `selection_review_2026-09-09.md`. Those artifacts reviewed release-bearing projects and top-level source events, but they did not reconcile every active repository or every project named inside an aggregate recap event. The newsletter must not advance from this audit alone; prose, links, continuity, event examples, and exact-head publication checks still require fresh review.

## Source boundary

- Window: `[2026-08-31T00:00:00Z, 2026-09-09T00:00:00Z)` unless an in-window, signed launch announcement establishes the first public launch of a project built immediately before the boundary.
- Local GitHub mirror first read: generated `2026-09-09T11:38:09Z`, last synchronized `2026-09-09T11:36:37Z`, covering 19 mirrored repositories and 17,083 issue or pull-request threads. This is bounded-staleness discovery evidence only. Every selected GitHub release, pull request, commit, repository state, and current head was reread through the authenticated live API with caching disabled.
- Project collector: 719 repositories fetched; 166 active; 138 releases; 948 merged pull requests; 3,111 commits. The active set contains 51 release-bearing projects and 115 projects without an in-window release.
- Nostr Recap: 18 signed events. Project roundups were expanded into their individual named projects and source URLs before selection.
- App discovery: 404 candidates. Four source-level MAYBE rows were individually inspected. One was promoted after its handler led to a working service and a new in-window public repository; three failed the source eligibility gate, as did the other 400. The GitHub search sub-source was partial at 500 of 609 results and some owner lookups failed, so it cannot prove ecosystem completeness and supplies no negative claim beyond the candidates it returned.
- Zapstore: 1,117 self-signed release events; 339 Nostr-relevant releases across 59 applications. These supplement primary repositories and do not override a repository release or commit.
- Triage after live follow-up: 503 rows: 21 GREEN, 33 MAYBE, and 449 SKIP.

## App-discovery MAYBE follow-up

- `Appointment Tool` — INCLUDE, 9/10. The [signed handler event](https://njump.me/6fead386f0f401c2d8641ef842ccc2ade5abb4e45d61bfd7f3872b43db04cdac) resolves to a working NIP-52 scheduling service. Its [public repository](https://github.com/delirehberi/cal.emre.xyz) was created inside the window and exposes the event construction, relay discovery, overlap checks, signing paths, tests, and deployment code. It is included as cal.emre.xyz.
- `BlindOracle` — SKIP_GATE. The live page is an agent counterparty-risk service and provides no release or inspectable NIP-58 implementation supporting the handler's broader Nostr claim.
- `ox402-utils` — SKIP_GATE. The handler describes paid web utilities, supports only kind `1`, names no repository, and its advertised endpoint did not answer the bounded live check. It establishes no distinct Nostr application behavior.
- `zap.stream (CA)` — SKIP_GATE. The record points to an alternate API endpoint rather than a released application; the advertised URL returned 404 and provides no repository or in-window implementation delta.

## Editorial filter

The first stage is a hard eligibility gate. A candidate needs a stable source ID, exact-window or verified launch evidence, a concrete Nostr surface, a primary source that supports the claimed behavior, and a distinct delta from recent Compass coverage. Missing evidence, an opaque merge, dependency or translation churn, packaging alone, a generic self-description, or work outside Nostr fails here.

Candidates that pass the hard gate receive zero to two points on each of five axes: Nostr or protocol consequence, user or operator consequence, novelty against recent issues, evidence and delivery maturity, and explanatory value. Publication requires at least eight of ten with no zero axis. Section size is an output of that threshold. A fixed slot budget cannot remove a qualifying item. A selected item may be folded into a related project section, but its candidate ID and primary source remain in this ledger.

## Original GREEN reconciliation

Eighteen of the original twenty GREEN candidates are present in the revised draft: nsite-clay, Wingman App, ngit/GitWorkshop, fips2go, FIPS, Chama, NoorNote, Mostro Mobile, nostr-java, Sister Charge, nostr-relay, Primal Android, nostr-social-graph, ZapStore, Jumble, Mafrend, NIP-78 pull request 2458, and NIP-01 pull request 2460. NIPs pull requests 2454 and 2371 are explicit continuity downgrades because those exact merged sources were already covered in Newsletter 38. No original GREEN candidate is unexplained.

The release re-audit reversed generic cadence or maintenance skips when the primary source described material behavior. The revised draft now includes Vector 0.4.4, Amber 6.6.1, GRAIN 0.8.0-rc2, Nostr-Doc 0.9.8, nostr-double-ratchet 0.0.170, Buzz 0.5.23, Cellibacy 2.0.7, Holy Fit 2.0.6, Nunlock 2.0.6, nostr-vpn 4.1.9, mostro-cli 0.16.1, mostro-core 0.14.6, Shosho 1.1.0, pakstr 0.19.0, Wisp 1.2.2, Sidecar 1.12.0, and YakiHonne Mobile 2.0.7. Meiso, nostr-components, and Infans were removed from the draft after scoring below eight: their in-window changes were narrower than the retained set or were groundwork without the runtime behavior wired.

The source identity error that assigned pakstr release URLs to `NostrAppShell` is rejected. The current item is pakstr, and continuity records that pakstr appeared in Newsletters 38 and 39 source material before this release. nostr-java 2.3.1 is a new MCP-server delta, not a first project release; version 2.0.8 appeared in Newsletter 37.

## Aggregate recap reconciliation

- Release roundup `5b7934…` expands to sixteen projects. Included: ZapStore, Amber, Jumble, Primal Android, Shosho as Livelier client evidence, YakiHonne Mobile, Mostro Mobile, Vector, Wisp, NoorNote, and Sidecar. Skipped: Earthly 0.1.8, whose only release delta is visual AI feedback; Nostrord 2.10.1, whose delta is AppImage and CI packaging; Dark Wisp 1.2.3, whose delta is branding and dependency maintenance; Workstr Web 2.4.0, whose large delta is primarily fitness-interface design without a distinct Nostr behavior; and Roadstr 0.5.2, a necessary map-renderer hotfix without a distinct Nostr behavior.
- Developer roundup `32a939…` expands to five projects. Included: nostr-java, Dart NDK, mostro-cli, and mostro-core as context for the maintenance state. Skipped: rx-nostr 3.7.6, a single publish-state cleanup below the impact threshold.
- Individual release events `015742…`, `87349…`, and `241f59…` yield Mostro, Buzz, and nostr-vpn, all included. Routstr Core 0.4.6-beta is skipped because its cited pre-release is payment-proxy work without a comparably direct Nostr protocol delta.
- Launch roundup `cb95e6…` names Livelier and Communitator; both in-window signed launches are included and were verified against their repositories. Its remaining twelve release links predate the reporting boundary and are excluded from this issue.
- Developer launch roundup `17ecd3…` names pakstr, Dart Nostr 11.0.0, Dart NDK 0.9.1, and snow-actions/nostr 2.0.0. pakstr is included from its in-window launch and 0.19.0 delta; Dart NDK is included from newer 0.9.2 and 0.9.3 releases. Dart Nostr 11.0.0 and snow-actions/nostr 2.0.0 were published before the reporting boundary.
- The remaining recap events contain meetups, press links, community posts, bounties, or direct Nostr references. They remain available to the news review but do not establish untracked project progress by themselves.

## All 59 Zapstore application rollups

The earlier source-health paragraph counted applications without deciding each
one. This pass expands the 59 application rollups and reads the latest signed
release record for each. `INCLUDE` and `FOLD` clear the common 8/10, no-zero
threshold; `SKIP_SCORE` survives the hard gate but falls below eight;
`SKIP_GATE` lacks a direct in-window Nostr delta or adequate primary evidence.

### INCLUDE or FOLD — 28

- `app.chama.market` — FOLD, 9/10: Chama's reconnect and wallet-state work is in its tagged section.
- `com.noornote.app` — FOLD, 9/10: NoorNote's unread bookmarks and encrypted synchronization are in its tagged section.
- `com.wingmanbefree.wingman_app` — FOLD, 10/10: Wingman is a top story with the current embedded-FIPS and application-shell evidence.
- `com.scuba323.holyfit` — FOLD, 8/10: the signer repair is in the wellbeing applications section.
- `com.wisp.app` — FOLD, 8/10: Wisp 1.2.2 is included; 1.2.3 is explicitly treated as maintenance.
- `network.mostro.app` — FOLD, 8/10: the mobile range-order state and Mostro concurrency work share one sourced section.
- `com.greenart7c3.nostrsigner` — FOLD, 9/10: Amber's request correlation and permission parsing are included.
- `com.mafrend.application` — FOLD, 10/10: Mafrend's Marmot groups and separate maps are a top story.
- `com.nym.bar` — INCLUDE, 9/10: Nymchat's cross-conversation threads and bot context are included from the signed release.
- `com.scuba323.cellibacy` — FOLD, 8/10: the background NIP-55 path is in the wellbeing applications section.
- `com.scuba323.sistercharge` — FOLD, 8/10: the background NIP-55 path is in the wellbeing applications section.
- `com.shosho.app` — FOLD, 8/10: Shosho's Livelier integration is evidence in the Livelier top story.
- `io.vectorapp` — FOLD, 10/10: the Concord recovery and key-rotation release is a top story.
- `net.primal.android` — FOLD, 9/10: signer and wallet requester authentication are included.
- `com.librenostr.android` — INCLUDE, 10/10: fail-closed Tor routing and the two follow-up repairs are included.
- `org.skatespots.app` — INCLUDE, 10/10: the on-device Citrine relay and payment-proof checks are included.
- `pub.ditto.app` — FOLD, 9/10: Blossom mirror and fallback behavior is included under Ditto's current work.
- `org.getwhistle.whistle` — INCLUDE, 10/10: lifecycle and stale-socket recovery are included.
- `space.einundzwanzig.mobile` — INCLUDE, 10/10: NIP-17 direct messages and their explicit legacy boundary are included.
- `app.unstablekraft` — INCLUDE, 9/10: live programs, shared playlists, and private-feed boundaries are included.
- `ngit` — FOLD, 10/10: the coordinated v3 release is the lead story.
- `com.example.epochs` — INCLUDE, 8/10: Astraea's first stable cross-platform encrypted-calendar contract is included.
- `com.formstr.pollerama` — FOLD, 9/10: Pollerama's NIP-A3 payment targets are included with the other implementations.
- `com.relaygazette.relay_gazette` — INCLUDE, 8/10: the first signed finite-edition Nostr newspaper is included.
- `com.scuba323.nunlock` — FOLD, 8/10: the background NIP-55 path is in the wellbeing applications section.
- `com.voca.app` — INCLUDE, 8/10: Voca's separation of required event verification from optional profile lookup is included.
- `cooking.zap.app` — FOLD, 9/10: the stronger current project evidence is Zap Cooking's merged NIP-27 implementation; the app release alone is below threshold.
- `tools.relay.relaytools` — INCLUDE, 9/10: copyable NIP-19 forms and bounded NIP-65 relay hints are included.

### SKIP_SCORE — 10

- `org.dergigi.boris` — 7/10: local-first search, relative links, and a zap spinner are useful but narrow interface repairs.
- `buzz.armada.app` — 7/10: desktop notification and read-state repair is real, while the stronger Armada interoperability evidence stays in Plektos's section.
- `fit.linky.app` — 6/10: automatic collection from an additional npub-based Cashu address is primarily payment behavior.
- `ai.alohak.kai` — 7/10: malformed pairing-identity rejection is a bounded security fix without a larger Nostr behavior change.
- `ai.hermex.vm` — 6/10: first-run relay editing and disconnected list replacement are narrow recovery controls.
- `com.echoes.echoes` — 7/10: the 1.0 milestone is mainly interface work and restates an already-settled encrypted-sync contract.
- `com.boostmebuddy` — 7/10: the first Android package wraps an existing web application and does not add a distinct protocol behavior.
- `space.einundzwanzig.meetup` — 6/10: organizer recognition repairs badge attribution through a portal lookup, not Nostr event behavior.
- `to.iris.chat` — 6/10: one shared-file retrieval reliability fix is too narrow for a separate item.
- `com.turkbot.babytracker` — 7/10: timer and WebSocket recovery are useful but below the retained application's impact threshold.
### SKIP_GATE — 21

- `eu.imwald.android` — “updated to match the ratings spec” names no behavior or primary specification delta.
- `app.zeusln.zeus` — the release notes are Lightning and wallet maintenance without a current Nostr change.
- `com.scuba323.saintstream` — no release notes establish an in-window behavior.
- `org.nostr.nostrord` — AppImage and CI packaging only.
- `place.poster.app` — high-cadence internal Jellyfin decoding work with no current Nostr delta.
- `app.roadstr` — map symbols and route-search fixes without a current Nostr delta.
- `io.coinos.app` — the signed package row provides no release notes for the in-window version.
- `com.receiptscanner.app` — the application is offline receipt tooling and “Nostr-friendly” does not establish a Nostr surface.
- `eu.decentnewsroom.bookshelf` — a changelog link without a described delta is insufficient evidence.
- `com.athena.reader` — Android file-picker repair does not change the reader's Nostr behavior.
- `com.darkwisp.app` — branding, dependency, target-SDK, and version maintenance only.
- `com.denimroad.ironsignr` — no release notes establish an in-window signer delta.
- `org.comunes.tane` — no release notes establish an in-window Nostr delta.
- `app.donkeyride.driver` — the underlying repository release is before the reporting boundary.
- `city.earthly` — image, AI, and map-review changes without a current Nostr delta.
- `com.aesirdev.amberup` — an unofficial fork mirrors upstream Amber behavior already covered from the canonical project.
- `com.scuba323.thehabit` — no release notes establish an in-window behavior.
- `dev.echoes.checkmarks` — a stable-version visual and task-interface release without a new Nostr behavior.
- `io.nostrlabs.zap_stream_flutter` — no release notes establish an in-window behavior.
- `social.cloudfodder.zzub` — no release notes establish a delta for this community fork.
- `to.iris.drive` — no release notes establish an in-window behavior.

## All 115 active projects without a release

Every repository below appears exactly once. `INCLUDE` means the current draft contains the project or exact-source context. `SKIP_SCORE` means a concrete Nostr delta survived the hard gate but scored below eight because it was narrow, repetitive, immature, weakly evidenced, or recently saturated. `SKIP_GATE` means it did not establish a concrete, merged, in-window Nostr delta suitable for this newsletter.

### INCLUDE — 19

- `Conduit-BTC/conduit-mono`
- `DocNR/clave`
- `OtherStuffAI/wm-app`
- `arbadacarbaYK/gittr`
- `derekross/plektos`
- `formstr-hq/nostr-polls`
- `jooray/nsite-clay`
- `marmot-protocol/marmot` — selected through the exact open proposal source
- `mattn/cagliostr`
- `mmalmi/nostr-notification-server`
- `nbd-wtf/nostr-tools` — exact failed-socket repair used in Sidecar context
- `nostr-protocol/nips` — selected through individual merged and open specification sources
- `purrgrammer/grimoire`
- `sanah9/noscall`
- `soapbox-pub/ditto`
- `trbouma/safebox-acorn`
- `vitorpamplona/amethyst`
- `zapcooking/frontend`
- `zapstore/server` — included in the ZapStore certificate-rotation section

### SKIP_SCORE — 37

- `Cameri/nostream` — NIP-43 invite issuance is useful but narrower than the retained relay changes.
- `ChadFarrow/stablekraft-app` — substantial feed and local-data repair, with an indirect Nostr surface and limited current evidence.
- `ClarkQAQ/nostr` — tolerant parsing and envelope fixes are small library changes.
- `DavidGershony/dotnet-mls` — strong MLS correctness work without a verified Nostr or Marmot integration in this source pass.
- `Lokuyow/ehagaki` — one NIP-46 multi-relay latency repair.
- `PrimalHQ/primal-ios-app` — simple-link handling is a narrow follow-up beside the selected Primal Android security release.
- `SnowCait/nostter` — relay parsing refactor and responsive labels, with no comparably large delivered feature.
- `SnowCait/snowflare` — invalid-event response and KV work are narrower than the selected relay conformance series.
- `TsukemonoGit/lumilumi` — one feed setting and dependency maintenance.
- `akiomik/nostui` — relay-acknowledged publish status is correct but one narrow client fix.
- `arbadacarbaYK/gitnostr` — dependency-security pins and comparison documentation only.
- `arbadacarbaYK/gittr-helper-tools` — documentation snippet only; the associated Gittr implementation is included.
- `arkin0x/cyberspace` — event-kind and game-mechanic documents without a verified shipping surface.
- `bit-blik/bitblik` — verifier and dispute-message changes have limited user-facing evidence.
- `block-core/angor` — relay EOSE recovery fixes one loading failure in a recently covered project class.
- `coracle-social/coracle` — a comment-tag fix plus deployment work.
- `coracle-social/paravel` — slash commands and NIP-22 fixes are commit-only and lack a bounded release or review source.
- `damus-io/damus` — one NWC key-derivation versioning change after frequent recent coverage.
- `damus-io/nostrdb` — re-ingest and pruning lifecycle fixes are valuable but narrow internal storage work.
- `damus-io/nostrdb-rs` — crate separation and subscription cleanup remain library-internal.
- `damus-io/notedeck` — active agent-session and encrypted-board development lacks a release boundary and is spread across many internal commits.
- `divinevideo/divine-mobile` — high-volume reliability work repeats the direct-message and signer themes covered in each of the last three issues.
- `dmnyc/ghostr` — draft interoperability and history repair are modest beside the selected Sidecar release.
- `fiatjaf/nak` — EOSE rendering and git path resolution are useful command-line fixes below the impact threshold.
- `getAlby/hub` — NWC extension metadata and migration/shutdown fixes are incremental after recent wallet coverage.
- `getAlby/lightning-browser-extension` — one requesting-site confirmation fix on a Lightning-auth path.
- `higedamc/meiso` — secure-storage work is explicitly not wired at runtime; the Amber comment path alone scores below eight.
- `lawalletio/lawallet-nwc` — failed-relay caching and pasted-key cleanup are narrow fixes.
- `lontivero/Nostra` — COUNT, filter-limit, and mailbox fixes overlap the better-evidenced cagliostr and nostr-relay sections.
- `nostur-com/nostur-ios-public` — media teardown and thread-safety fixes are narrow and the project was present in the recap history immediately before the window.
- `rust-nostr/nostr` — local-relay filter-limit refactor without a separately observable behavior change.
- `saiy2k/nostr-components` — extension zap/YouTube support and a directory page score below the revised impact threshold.
- `shocknet/Lightning.Pub` — authorization work is not described by a reviewable merged source in the collected record.
- `swentel/nostr-php` — integer decoding and default-relay maintenance are narrow library fixes.
- `theborakompanioni/nostr-spring-boot-starter` — dependency and build-system maintenance.
- `tidley/auditable-voting` — delivery and input hardening remain an early application milestone with limited ecosystem evidence.
- `v0l/route96` — one administrator ban-by-pubkey control.

### SKIP_GATE — 59

These candidates had no merged or released in-window behavior, an opaque change, routine dependency/build/documentation/automation work, or no sufficiently direct Nostr consequence:

- `0xchat-app/0xchat-app-main`
- `BitcreditProtocol/Bitcredit-Core`
- `BitcreditProtocol/bcr-relay`
- `DaBena/Brezn`
- `MostroP2P/mostro-skill`
- `Origami74/myco`
- `Routstr/routstrd-auth`
- `Spl0itable/NYM`
- `akiomik/nosvelte`
- `andotherstuff/pensieve`
- `andreasgriffin/bitcoin-safe`
- `breez/glow-web`
- `camelus-hq/camelus`
- `carlitoplatanito/disgus`
- `cashubtc/cashu.me`
- `cashubtc/npubcash-server`
- `cashubtc/nutshell`
- `coinos/coinos-ui`
- `contextvm/ts-sdk`
- `delirehberi/hugo2nostr`
- `delirehberi/nostr-ro-client`
- `delirehberi/nostr.hs`
- `dergigi/ants`
- `dergigi/boris`
- `diegogurpegui/nos2x-fox`
- `dsbaars/bunker46-extension`
- `dtonon/fevela`
- `forgesworn/bark`
- `forgesworn/cambium`
- `formstr-hq/formstr-drive`
- `getAlby/js-sdk`
- `geyserfund/geyser-app`
- `git.reya.su/reya/coop-mobile`
- `hedwig-corp/bitchat-to-sonar`
- `hoytech/strfry`
- `irislib/iris-stack`
- `jooray/nalgorithm`
- `kehto/web`
- `koteitan/nostr-post-checker`
- `minibits-cash/minibits_wallet`
- `napplet/web`
- `nostr-net/vanity-key`
- `nostrbuild/nostr.build`
- `paulmillr/nip44`
- `permissionlesstech/bitchat`
- `permissionlesstech/georelays`
- `relaytools/relaycreator`
- `routstr/routstrd`
- `sebastix/nuxstr`
- `shocknet/wallet2`
- `shopstr-eng/milk-market`
- `shopstr-eng/shopstr`
- `snarfed/granary`
- `soapbox-pub/nostrify`
- `spacecowboy/Feeder`
- `tajava2006/cliprelay`
- `tidley/nostr-codex-phone`
- `vicariousdrama/cornychat`
- `whisperbit-labs/zemzeme-android`

## Current result

The revised draft accounts for every GREEN row, every project named in the release and launch recap roundups, all 51 release-bearing tracked projects through the original project table plus the reversals above, all 115 active non-release projects through the explicit dispositions in this file, all 59 Zapstore application rollups, and all 404 app-discovery candidates. The partial app-discovery source is labeled partial, so this audit claims full treatment of the returned set rather than completeness beyond it. Coverage is reconciled; final editorial and publication review remain pending.

COVERAGE STATUS: PASS
