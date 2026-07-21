# Selection Review — Newsletter #31 (2026-07-15)

Resumed run. Input: `triage_2026-07-15.md` (GATE: PASS, 41 GREEN / 20 MAYBE / 30 SKIP). Continuity baseline: #30 (2026-07-08). Not a month-end issue (next month-end is #33, around 2026-07-29 per rotation memory) — regular two-NIP deep dive applies.

## NIP Deep Dive selection

**NIP-15 (Nostr Marketplace)** and **NIP-99 (Classified Listings)** — neither appears in the rotation history (`~/.claude/projects/-home-vibe-compass/memory/MEMORY.md` covered-NIPs list runs through NIP-98, does not include NIP-15 or NIP-99). Both already have topic pages (`content/en/topics/nip-15.md`, `content/en/topics/nip-99.md`) that need a "Mentioned in" update rather than creation. Editorial hook: this week's Conduit-BTC marketplace work (guest checkout with ephemeral order keys, orders-inbox rebuild) is NIP-99-adjacent commerce protocol activity, giving the pairing a live news anchor — NIP-15's original all-in-one marketplace event shape versus NIP-99's decomposed classified-listing model is a natural "how Nostr commerce evolved" narrative.

## Section allocations

### Lead stories (5)
1. VectorPrivacy/Vector v0.4.0 — Tor integration, NIP-46 remote signers, multi-account switcher, custom emoji packs, and the notable move from Marmot to a custom "Concord Protocol" for group chat. Score 10/10 (protocol-level, high breadth, novel/contentious).
2. Sonar (hedwig-corp/bitchat-to-sonar) v0.1-alpha.7 / v0.1-alpha.6 — new-project spinoff of Bitchat, cited as the spec source for NIP PR #2410 (sticker packs), corroborated across GitHub + Zapstore. Score 9/10.
3. divinevideo/divine-mobile 1.0.16 — first tagged release since #30, major feature set (editor tools, feed tuning, at-rest encryption, ProofMode, 17-language localization). Score 9/10.
4. permissionlesstech/bitchat v1.7.0 — live push-to-talk voice for DMs and signed public-mesh push-to-talk, direct continuity from #30's v1.6.0 lead story. Score 9/10.
5. marmot-protocol/mdk v0.9.4 — continues the spec-adoption arc from #30; pairs editorially with the Vector item (one client deepens Marmot investment same week another leaves it for a fork). Score 8/10.

### Tagged releases (10)
0n4t3/n_cord V.1.1, cashubtc/cdk v0.17.3 (NIP-47/NWC across cdk+cdk-nwc+cdk-ffi, Gate C pass), git.reya.su/reya/coop-mobile v0.2.4, nogringo/nostr-mail-client v0.14.0, nostrord/nostrord v2.2.0, nostr-wot/nostr-wot-extension 0.3.86, privkeyio/keep-android v1.1.8, sanah9/noscall v0.6.0 (push-notification claim needs verification — do NOT cite "NIP-9A", confirmed non-existent via `gh api repos/nostr-protocol/nips/contents/9A.md` → 404; describe the feature without a NIP number), JeroenOnNostr/kubo kubo-v2026.07.05 (Recap-sourced, GitHub-API-verified, landed just outside prior fetch window), tidley/nostr-codex-phone v0.2.9.

### Newly tracked and discovered (6)
Already added to `projects.yml` via intake this week (not Discovery-slot candidates, just first coverage): sofia-gros/open-discord v1.0.1, tidley/auditable-voting v0.1.140.
Discovery slot (Change C, exactly one, projects.yml addition required): **Cambium v0.3.2** (forgesworn/cambium) — NIP-55 signer app holding no keys, proxies signing to a Heartwood hardware signer over NIP-46; same GitHub org as tracked project Bray and companion to Heartwood (#30 covered Heartwood's serial signing bridge as unreleased work). Strongest hub-link of the four zapstore-only candidates.
One-time mentions (not counted against Discovery slot): Lwb89dev/echoes v0.1.0, freecritter/dispatch v0.3.0, hynek-jina/linky v26.7.4.

### Unreleased changes / high-PR projects (7)
block/buzz (240 merged PRs, relay/kind-39002 hardening, continuity), vitorpamplona/amethyst (NIP-85 contact-card nicknaming, 54 PRs), zapcooking/frontend (Kitchen Phase 3 + NDK pool quorum fix, 43 PRs), kehto/web (outbox reliability fixes + NAP-SHELL alignment, 26 PRs; note napplet/web's 32-tag monorepo churn as supporting context, not a separate item), smolgrrr/Wired + smolgrrr/TAO (NIP-57 creator revenue sharing, combined entry per single-PR-list rule), Conduit-BTC/conduit-mono (marketplace ephemeral-order-keys + orders-inbox rebuild — ties to NIP Deep Dive), formstr-hq/nostr-docs (NIP-49-based signer adoption, multi-account + QR).

### Also shipped (grouped, low-signal but real; one paragraph, no individual headers)
DanConwayDev/ngit-cli v2.6.3 (friendlier `ngit init` flow), dtonon/manent v1.4.1 (Amber hex-pubkey login fix), 77elements/noornote v1.2.8 (notification fixes), forgesworn/bray v1.34.0 (client-name metadata on bunker connect), TsukemonoGit/lumilumi (NIP-65 relay-list offline caching), moogmodular/earthly (NIP-50 geo search), lnbits/lnbits (PR #3925, non-blocking `send_nostr_dm` fix inside an otherwise Lightning-only release).

### Protocol work and NIP updates
**Merged:** none this window (confirmed via `gh pr list --state merged --search "merged:>=2026-07-06"` returning empty, per triage).
**Open:**
- kind:10011 favorite follow sets ([PR #2413](https://github.com/nostr-protocol/nips/pull/2413))
- private encrypted drive proposal, extends NIP-4E ([PR #2412](https://github.com/nostr-protocol/nips/pull/2412))
- NIP-DA — Permissioned Private Data Sharing / Scoped Data Grants ([PR #2411](https://github.com/nostr-protocol/nips/pull/2411))
- sticker pack kinds 10031/30031 ([PR #2410](https://github.com/nostr-protocol/nips/pull/2410)) — hub link to Sonar
- [NIP-29](/en/topics/nip-29/) message pinning, kind:9010 + kind:39005 mirror ([PR #2379](https://github.com/nostr-protocol/nips/pull/2379)) — hub link to nostrord maintainer Anderson-Juhasc
- [NIP-66](/en/topics/nip-66/) relay discovery restructure, W/l tags ([PR #2241](https://github.com/nostr-protocol/nips/pull/2241))

## SKIP list (not included, with reasons)

- NIP-100 SNIN ([PR #2378](https://github.com/nostr-protocol/nips/pull/2378)) — MAYBE in triage, fresh/unverified contributor, large 8-kind proposal; holding for due-diligence read of the diff rather than citing untriaged claims in a resumed run without time to verify. Carry to next week's intake-followup.
- GitWorkshop v3.0.3 (Zapstore) — MAYBE, fetcher gap, needs direct verification against gitworkshop.dev/GitHub before use. Not verified this run.
- Sidecar v1.3.0, Routstr Core v0.4.4 — MAYBE, Recap-only sourcing, repo identity unresolved (Routstr Core naming overlaps 3 existing tracked entries). Hold for intake-followup.
- Iris Drive — MAYBE, thin (empty kind:30617 content, non-standard clone URL). Already added to projects.yml as `other`/low priority via intake; no newsletter mention this week.
- Bitcoin-Safe — added to projects.yml this week via intake, but this window's 15 merged PRs are unrelated wallet UI/packaging work; the NIP-17 label-sync/signer-chat features the user flagged already shipped in v2.0.0 (2026-06-29, before this window). No newsletter mention this week; PR #108 (community, unmerged) is now a redundant duplicate — informational only.
- jesuspirate/chama v5.1.0, Spl0itable/NYM v3.73.519 — MAYBE, localization-only releases, no protocol-level content.
- sandwichfarm/nostr-watch, PrimalHQ/primal-android-app, block-core/angor — MAYBE, below depth-minimum threshold this window (general hardening / cosmetic UI / modest single-bug fixes).
- napplet/web — MAYBE monorepo churn; folded into kehto/web as supporting context rather than a standalone item.
- All triage SKIP verdicts (30 items: AustinKelsay/snstr, DaBena/Brezn, diegogurpegui/nos2x-fox, lawalletio/lawallet-nwc, mattn/nostr-relay, michaelneale/mesh-llm, mmalmi/hashtree, mouse484/astraea, routstr/routstrd, shocknet/Lightning.Pub, CodyTseng/jumble, cashubtc/cashu.me, cashubtc/nutshell, shopstr-eng/shopstr, K.ai, gitworkshop.dev NIP-34 issues, Whitenoise Linux NIP-34 issues, IndieSats, PosterChan, bulk pubkey 78ce6faa..., ngit/Codeberg, nostr-rs-relay/Sourcehut, NIP-80, NIP-01 pagination, NIP-29 message pinning dup-check passed (new PR, kept above), kind 32267 software-apps PR, NIP-65 outbox-trust PR) — reasons already documented per-item in `triage_2026-07-15.md`, not repeated here.

## Redundancy check against #30 and coverage_history.json

Continuity notes already applied inline above per triage's per-item continuity flags. No item in this selection duplicates content already published in #30 (routstrd v0.3.7 and jumble v26.7.1 were excluded specifically because they are the same tagged versions #30 already covered).

## Auto-proceed note

Per user resume instruction ("resume from Selection onward through Writing and Review, and stop at the human-approval gate before Publish"), this selection proceeds to Writing without an intermediate pause. Final human review happens at the Stage 8 handoff gate before any publish action.

## Human editorial override — Bitcoin-Safe (added post-Selection)

Selection's original SKIP verdict above is correct as written (v2.0.0's Nostr feature set shipped 2026-06-29, before this window). The user reviewed that reasoning and asked to include it anyway, on a distinct and separately-verified news hook: Bitcoin-Safe shipped its first Flathub package this window (flathub/org.bitcoin_safe.BitcoinSafe repo activity 2026-07-03 to 2026-07-06; live on Flathub's stable branch as of 2026-07-07), which is new-this-week distribution activity even though the underlying Sync & Chat code is not. Verified before writing: NIP-17 usage for label sync and PSBT sharing (confirmed in andreasgriffin/bitcoin-nostr-chat README), the "Share via Chat & Sync" signing UI in the 2.0.0 release notes, and live Flathub listing (API query). No public source was found for a Marmot-migration roadmap item, so the newsletter item frames that as an open editorial question, not a confirmed claim. Added as a tagged-release item in `sections/tagged-releases.md` rather than a lead story, since the news value this week is the distribution milestone, not new code.

**Second manual fix (2026-07-14, post-Review-Swarm):** the resumed Stage 4-7 run (17:09-17:32 UTC) regenerated `sections/tagged-releases.md` from Selection's own approved list during Stage 5 Writing, which does not carry this override note, so the manually-added Bitcoin-Safe paragraph was silently dropped from that pass and never made it into the assembled draft or through the Review Swarm's link/prose/claim checks. Caught by direct diff of the draft against the section file after Review completed. Fixed by inserting the same, already-fact-checked paragraph directly into `content/en/newsletters/2026-07-15-newsletter.md` (Tagged releases section) post-hoc, and independently re-verified at that point: all 4 links return HTTP 200 (bitcoin-safe.org, Flathub listing, bitcoin-nostr-chat repo, 2.0.0 release tag), `nip-17` and `marmot` topic pages both exist, `hugo --buildFuture` builds clean with the addition, and the generated heading anchor (`#bitcoin-safe-reaches-flathub-spotlighting-its-nostr-sync--chat-plugin`, note double hyphen where "&" was stripped) was added as "Mentioned in" entries on both `content/en/topics/nip-17.md` and `content/en/topics/marmot.md`, matching the swarm's own TopicAudit convention. Not independently re-run through the automated ProseReview/ClaimCheck/LinkChecker swarm agents themselves, since the paragraph text is verbatim identical to what those checks would have seen had Writing not dropped it; spot-verification above covers the same ground manually.

**Process gap to fix before next resume-from-Selection scenario:** any post-Selection human override note in this file should be re-applied to the regenerated section file *after* Stage 5 Writing completes, not just written once before a Selection re-run, since Writing does not read this override section.

## Model comparison follow-up and final editorial pass (2026-07-14, post-publish-gate)

Two blind Opus subagent test outputs (`/tmp/compass_model_comparison/lead-stories_TEST-OPUS.md`, `nip-deep-dive_TEST-OPUS.md`) were diffed against the real Sonnet-written and Sonnet-verified draft to decide what, if anything, to merge in:

- **Lead stories:** kept the Sonnet version as-is. Opus's version had weaker sourcing (no PR-level citations for the Bitchat/MDK items the Sonnet draft cites directly, e.g. PRs #1401/#1403/#1406/#1415, #793/#812) and introduced uncited comparative/speculative framing ("largest new interaction surface... since last week," "open editorial question heading into the second half of 2026") that the style guide's "no significance inflation" and citation rules exclude. Nothing merged.
- **NIP Deep Dive:** kept the Sonnet version (JSON event examples, PR #174/#175 citations) as the base. Opus's version had no code examples and made one uncited/unverifiable claim ("Milk Market... builds on the classified-listing primitive" — no such Nostr project found via GitHub search, treated as a likely fabrication and discarded) but also surfaced one claim that checked out: Shopstr refactored NIP-17 gift-wrap logic ([PR #568](https://github.com/shopstr-eng/shopstr/pull/568), merged 2026-07-12) and hit 100% NIP-98 auth-parser test coverage ([PR #567](https://github.com/shopstr-eng/shopstr/pull/567), merged 2026-07-08) this window — both independently confirmed via `gh pr list --repo shopstr-eng/shopstr --state merged`. Merged this one verified fact into both `sections/nip-deep-dive.md` and the published draft as a new paragraph in "Why the split happened."

**Additional review pass for missed/boring items**, checking the full triage MAYBE list against the current draft: re-examined GitWorkshop v3.0.3, which triage flagged as a fetcher-gap MAYBE (Zapstore naddr listing didn't match the tracked GitHub repo). Verified directly against `DanConwayDev/gitworkshop` tag/commit history: real release, one substantive fix (`fix(explorer): resolve newly announced refs`, touching branches/tags/commits/code-browsing views) plus CI workflow-timing cleanup. Added as a one-paragraph tagged-release item (existing high-priority tracked project, closes the triage-flagged gap). NIP-100/SNIN and Routstr Core/Sidecar were re-considered and left as SKIP/MAYBE — both still rest on fresh/unverified sourcing (new GitHub contributor, Recap-only description) that a few minutes of due diligence couldn't responsibly resolve; no other pre-window "important item" was found beyond Bitcoin-Safe, already covered above. No item already in the draft was judged boring enough to cut; Selection's original SKIP list reasoning (documented per-item in `triage_2026-07-15.md`) held up on re-check.

All additions independently re-verified: GitHub PR/release links return HTTP 200, `hugo --buildFuture` builds clean (277 EN pages), and "Mentioned in" entries added to `content/en/topics/nip-98.md` and `content/en/topics/nip-34.md` matching TopicAudit convention.

GATE: PASS
