# Review: ClaimCheck — Newsletter #36 (2026-08-19)

Every tagged release included in the issue was audited against its complete primary release
notes, and every cited pull request was verified live through `gh pr view` for state, merge
time, and title. This file records the source checked and what the audit did with it.

## Release audits

| Release | Source read | Substantive changes represented | Omitted, with reason |
|---|---|---|---|
| Amber v6.5.0 | release notes plus the four GitHub security advisories | relay-auth confused deputy (GHSA-vx4h-56qj-wcp7, high), NIP-46 freshness and replay (GHSA-h9fv-9247-3582), secrets encrypted at rest (GHSA-5fjp-ghh8-wch8), and all eight items in the hardening batch (GHSA-8844-q5vh-9j8f) | translation string updates, CI test and linter fixes: routine churn |
| Amber v6.5.1 | release notes | Keystore-rotation re-encryption of NIP-46 secrets, permission-editor crash | none |
| Amber v6.5.2 | release notes | applications-screen decryption and Keystore handle caching, account cache warm-up, duplicate-row crash, relay status debounce | none |
| Cambium v0.3.5 | release notes | permission removal and Gradle distribution pinning are F-Droid review hygiene with no protocol effect; represented as context only | no separate paragraph, correctly |
| Cambium v0.3.6 | release notes | rust-nostr 0.44.2 to 0.44.8, `connect` secret echo accepted alongside `ack` | none |
| Cambium v0.4.0 | release notes | NIP-55 website signing through validated `nostrsigner:` callbacks, minimal-event shape fix, required native CI gate | none |
| Cambium v0.4.1/v0.4.2/v0.4.3 | release notes for all three | reserved queue slots, bounded queue, terminal overload result, idle session discard, shared AUTH signature, one challenge per identity, sixty-second cooldown, measured results | none |
| Citrine v3.1.0 | release notes | NIP-29 groups, NIP-86 API and settings screen, NIP-5A nsites plus browse list and relay defaults, rebroadcast tool, purge on ban, `REJECTED_KINDS`, list import, `permessage-deflate` removal, query hot path, Tor start/stop, log persistence | Gradle/Kotlin dependency updates and translation updates |
| Vector v0.4.2 | release notes including preview 2 through preview 6 blocks | moderation queueing and single key rotation, dead-invite handling, background-sync notifications, typing expiry, cross-client list review with Armada, mute from a community, pinned messages and chats, synced blocks/mutes/nicknames, Mini Apps from URLs, biometric unlock, self-updating sideloads | rich composer markdown detail, emoji fidelity, QR button width, menu polish, header truncation: presentation detail with no Nostr surface |
| Vector v0.4.3 | release notes | Tor bootstrap on Windows, phantom typing across clients, dissolved-community propagation | none |
| Sonar alpha 13.1/13.2/13.3 | release notes for all three | NIP-C7 replies, mentions, bounded BLE reassembly, mesh signing verification, FCM fallback, both chat-open crashes, iOS keyboard, scroll invalidation | backup data-plan cap and onboarding/banner fixes folded into one clause |
| Nostria v4.1.69/70/71 | release notes | NIP-45 COUNT, feed reaction/reply/zap loading, localization, podcast publishing, episode durations | none |
| MDK v0.9.12 | release notes and each linked pull request | fork-anchor fail-closed, atomic leave proposal, incident-replay format detection, retained-history cross-route recovery, cross-adapter convergence, isolated convergence campaigns, relay rejection diagnostics | OpenClaw Dependabot and messaging-host fixes, Nostr 0.44 patch bump, strict-oracle test coverage: internal tooling |
| MDK MarmotKit and wn-agent artifacts | three release pages | iOS XCFramework, macOS arm64 addition, Android ABI bindings, provenance manifests | installer command lists |
| Divine Mobile 1.0.20 | release notes | NIP-58 badge minting and award, badge explanation on tap, plus the client-work summary | none material |
| ClipRelay v0.1.4 and v0.2.0 | release notes for android and desktop | sensitive clipboard retention and marker propagation, connection log, liveness-probe round trip, WebView suspension, session relay pinning, nostrconnect QR login, bunker URL scanning, sixty-second timeout | build/version display line |
| Bark v1.3.8 and v1.3.9 | release notes | Heartwood probe restriction and standard `sign_event` fallback, Firefox for Android declaration, approval-tab fallback, viewport fix, the stated Chromium-on-Android limitation | six Dependabot action bumps and a store-submission command |
| Bray v3.0.0, Toll Booth v6.0.0/6.0.1/6.1.1/6.1.2 | release notes for all five | nwc-kit adoption as a breaking change, payer credential removal, reproducible-build attestation, the three patch fixes | tarball size lines |
| nwc-kit | repository metadata and release list | creation date, license, stated scope, version reached | none |
| NoorNote v1.3.4 and v1.3.5 | release notes | Armada/Concord invite joining and notifications, external quote-post hiding, profile resolution, Soft Mute, long-note expander, invite input layout | none |
| Mostro v0.18.2/0.18.4, mostro-core v0.14.3/0.14.4/0.14.5, mobile v1.3.1/v1.3.2 | release notes for all seven | kind 14 dispute-chat migration and primitives, durable cursors, rumor-id serialization, ratings average, nostr-sdk 0.45.1, Blossom server switch, range-order push tokens, the 0.18.3 do-not-use warning | GPG verification boilerplate repeated in every Mostro release body, Portuguese translation, Windows runner pin, invoice screen scrolling |
| NYM v3.73.520-524 | release notes for all five | encrypted group chat refinement, encrypted SQLite, CSP inline script, stale-message display, assistant model hotfixes | none |
| Morganite v0.0.4 | release notes | single-pass hash verification, incremental cache sizing, blocking calls moved to I/O threads, Tika reuse, log persistence | IDE deployment-target state and permission logging removal |

### Nail (added 2026-08-18)

Nail was verified from primary sources rather than from its README summary. The repository
metadata (MIT, TypeScript, created 2026-02-25) came from the GitHub API;
`client/src/lib/nostr/constants.ts` supplied every kind number cited (1301, 1059, 10050, 10002,
1985, 30078) and the 60,000-byte Blossom threshold; `client/src/lib/mail/receive.ts` supplied the
four-state sender-provenance model; the mailcow integration and LMTP/SMTP wiring came from the
README; and `https://mailstr.app/.well-known/nostr.json?name=_smtp` was fetched live and returns a
single `_smtp` record. [PR #7](https://github.com/formstr-hq/nail/pull/7) was confirmed MERGED at
2026-08-18T15:15:20Z across 22 files with the three changes named in the prose. No release exists,
and the section claims none.

## Pull request verification

All 41 cited pull requests were confirmed `MERGED` with matching titles through the GitHub API
on 2026-08-18: MDK #1329/#1360/#1140/#1350/#1372/#1357/#1361; Amethyst #3899/#3905/#3906/#3931/
#3937/#3911/#3932/#3909/#3939; nostrord #247/#261/#271/#274/#269/#272/#268; nostream #724/#733/
#689/#732/#680/#727; rust-nostr #1444/#1445/#1450/#1451; NDK #713/#712/#710; Nostter #2311/#2281/
#2298/#2303; Zap Cooking #622/#626/#627; mostro-core #164/#163/#162; and Nail #7. Zero fabricated numbers,
zero unmerged pull requests presented as merged.

Open proposals are stated as open: NIPs #2436, #2437, and #2438 are described as proposals,
Concord #22 and #23 as opened on 16 August, and NIP-4e as unmerged. Concord #18 and Marmot #416
are stated as merged with their merge dates, both confirmed.

## NIP number verification

Every NIP identifier cited was resolved against the live specification repository. NIP-05, 07,
10, 13, 17, 22, 27, 29, 42, 43, 44, 45, 46, 47, 51, 55, 58, 59, 5A, 66, 70, 73, 86, 98, and C7 all
resolve. **NIP-4e does not exist in `nostr-protocol/nips`** (`4E.md` and `4e.md` both return 404);
it lives only in open pull request #1647. The draft therefore describes it as an unmerged
proposal, gives it no topic-page link, and keeps it out of the NIP updates section because it
had no in-window change. NIP-9A is likewise described as proposed, since #2438 adds `9A.md` as a
new file.

## Event examples

Both JSON blocks are events recovered from `wss://nos.lol` and `wss://relay.primal.net` with
`nak req` on 2026-08-18, not constructed. `scripts/check_newsletter_event_examples.py` confirms
all seven NIP-01 fields, hex field lengths, entropy, and timestamp plausibility.

GATE: PASS (24 source audits recorded against complete primary notes with omissions justified; 41/41 cited pull requests verified MERGED with matching titles on 2026-08-18; 25 NIP identifiers resolved live and the one non-existent identifier, NIP-4e, explicitly framed as an unmerged proposal; both event examples relay-recovered)
