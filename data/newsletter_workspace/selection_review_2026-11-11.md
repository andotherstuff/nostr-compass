# Selection review — Newsletter #48 (2026-11-11)

Every editorial candidate, its disposition and primary sources. Generated from the triage record and the draft.

## top-stories:marmot-projects-at-bitcoin-seoul
- INCLUDE: Marmot projects at bitcoin++ Seoul
- Reason: Top Stories: bitcoin++ Seoul, a privacy-themed Bitcoin developer conference held 5 and 6 November, ran a hackathon whose gallery lists 20 projects, several of them built on Marmot encrypted groups.
- https://btcpp.dev/seoul
- https://btcpp.dev/seoul/hackathon
- https://github.com/rademenezbtc/blackice
- https://github.com/samthomson/mdk-squared
- https://github.com/dongguri-jun/ilchon
- https://github.com/ye0man/kimchi
- https://github.com/shroominic/satsroadmarket
- https://github.com/murdawkmedia/quiet-ledger
- https://github.com/CypherCommons/shroud/pull/233
- https://github.com/kkdao/kiss-bdk
- https://github.com/marmot-protocol/awesome-marmot/compare/57d5bb868aa7...e0a960475372

## tagged-releases:nostur
- INCLUDE: Nostur
- Reason: Tagged Releases: Nostur, an iOS and macOS client, adds polls in 1.35.0.
- https://github.com/nostur-com/nostur-ios-public/releases/tag/1.35.0

## tagged-releases:monostr
- INCLUDE: Monostr
- Reason: Tagged Releases: Monostr, a Nostr client built around Monero tips, builds in Tor in v0.34.0.
- https://github.com/schmidt1024/monostr/releases/tag/v0.34.0

## tagged-releases:chama
- INCLUDE: Chama
- Reason: Tagged Releases: Chama, a peer-to-peer bitcoin trading app with ecash escrow, closes the final open item from its security audit in v6.4.34.
- https://github.com/jesuspirate/chama/releases/tag/v6.4.34
- https://github.com/jesuspirate/chama/pull/116

## tagged-releases:zapstore
- INCLUDE: Zapstore
- Reason: Tagged Releases: Zapstore, the Nostr-based Android app store, shipped 2.0.2 through 2.0.4 in three days.
- https://github.com/zapstore/zapstore/releases/tag/2.0.2
- https://github.com/zapstore/zapstore/releases/tag/2.0.4

## tagged-releases:manent
- INCLUDE: Manent
- Reason: Tagged Releases: Manent, a private notes app that stores encrypted notes on Nostr relays, released v3.1.0.
- https://github.com/dtonon/manent/releases/tag/v3.1.0

## tagged-releases:streets
- INCLUDE: Streets
- Reason: Tagged Releases: Streets, a Japanese web client, separates relay budgets in v1.24.0.
- https://github.com/eyemono-moe/streets/releases/tag/v1.24.0

## tagged-releases:noornote
- INCLUDE: NoorNote
- Reason: Tagged Releases: NoorNote, a desktop Nostr client, checks Lightning invoices before paying a zap in v1.9.10.
- https://github.com/77elements/noornote/releases/tag/v1.9.10
- https://github.com/77elements/noornote/pull/8
- https://github.com/77elements/noornote/pull/7

## tagged-releases:infans
- INCLUDE: Infans
- Reason: Tagged Releases: Infans, an Android baby tracker that backs up and syncs between parents through encrypted Nostr events, fixes disappearing timers in v2.4.3.
- https://github.com/TurkeyNostr/infans/releases/tag/v2.4.3

## tagged-releases:amber
- INCLUDE: Amber
- Reason: Tagged Releases: Amber, an Android app that holds Nostr keys and signs for other apps, adds a local relay in v7.0.0-pre3, a pre-release.
- https://github.com/greenart7c3/Amber/releases/tag/v7.0.0-pre3

## tagged-releases:keep-android
- INCLUDE: Keep Android
- Reason: Tagged Releases: Keep Android, a FROST threshold signer, fixes several leaks in v1.4.0.
- https://github.com/privkeyio/keep-android/releases/tag/v1.4.0

## tagged-releases:nostr-social-graph
- INCLUDE: nostr-social-graph
- Reason: Tagged Releases: nostr-social-graph, a library that builds follow and mute graphs for Web of Trust scoring, changes its snapshot format in v4.0.0, after Newsletter #45 covered 3.0.0.
- https://github.com/mmalmi/nostr-social-graph/releases/tag/v4.0.0

## tagged-releases:mdk
- INCLUDE: MDK
- Reason: Tagged Releases: MDK, the SDK and runtime for Marmot encrypted groups, released v0.15.0 together with MarmotKit bindings for iOS, macOS and Android.
- https://github.com/marmot-protocol/mdk/releases/tag/v0.15.0
- https://github.com/marmot-protocol/mdk/releases/tag/marmotkit-v0.15.0
- https://github.com/marmot-protocol/mdk/blob/v0.15.0/docs/release/0.15.0.md

## tagged-releases:vector
- INCLUDE: Vector
- Reason: Tagged Releases: Vector, a private messenger built on Nostr, shipped v0.5.0 and v0.5.1.
- https://github.com/VectorPrivacy/Vector/releases/tag/v0.5.0
- https://github.com/VectorPrivacy/Vector/releases/tag/v0.5.1

## in-development:route96
- INCLUDE: Route96
- Reason: In Development: Route96, a media server for Blossom (hash-addressed media storage) and NIP-96 (HTTP file storage) uploads, merged security fixes on 8 November that are not yet in a tagged release.
- https://github.com/v0l/route96/pull/106
- https://github.com/v0l/route96/pull/109
- https://github.com/v0l/route96/pull/102

## new-projects:splitnut
- INCLUDE: SplitNut
- Reason: New Projects: SplitNut, from BlackIce's author, runs a stock Cashu mint whose signing keys are split two-of-three across guardians who coordinate in a Marmot group.
- https://github.com/rademenezbtc/splitnut

## new-projects:moranduba
- INCLUDE: Moranduba
- Reason: New Projects: Moranduba is a Flutter group chat with end-to-end encrypted video calls and screen sharing, built on Marmot.
- https://github.com/vzsoares/moranduba
- https://github.com/vzsoares/moranduba/releases

## protocol-and-spec-work:nip-01-relays-can-tell-clients-how-long-to-back-off
- INCLUDE: NIP-01 relays can tell clients how long to back off
- Reason: Protocol and Spec Work: A merged NIP-01 change adds an optional last parameter to the `OK` and `CLOSED` relay messages in NIP-01 (the base relay protocol).
- https://github.com/nostr-protocol/nips/pull/2498

## protocol-and-spec-work:nip-47-logout-method-proposed
- INCLUDE: NIP-47 logout method proposed
- Reason: Protocol and Spec Work: An open pull request adds a `logout` method to NIP-47, the Nostr Wallet Connect spec for controlling a wallet over Nostr.
- https://github.com/nostr-protocol/nips/pull/2537

## protocol-and-spec-work:logout-mirrored-in-the-nwc-specs-repository
- INCLUDE: Logout mirrored in the NWC specs repository
- Reason: Protocol and Spec Work: The same author opened a matching logout draft in the Nostr Wallet Connect specs.
- https://github.com/nostr-wallet-connect/nwc/pull/13

## protocol-and-spec-work:push-registration-for-wallet-notifications
- INCLUDE: Push registration for wallet notifications
- Reason: Protocol and Spec Work: A separate open NWC draft defines `register_push` and `unregister_push`, letting a client hand the wallet service a Web Push endpoint, which UnifiedPush distributors can also serve.
- https://github.com/nostr-wallet-connect/nwc/pull/15

## protocol-and-spec-work:concord-merges-roles-private-channels-and-voice
- INCLUDE: Concord merges Roles, private channels and voice
- Reason: Protocol and Spec Work: Concord is a protocol for encrypted Nostr communities.
- https://github.com/concord-protocol/concord/pull/25

## protocol-and-spec-work:concord-joins-authenticate-the-community-root
- INCLUDE: Concord joins authenticate the community root
- Reason: Protocol and Spec Work: A Concord proposal covered in the August 19 issue (Newsletter #36) has now merged.
- https://github.com/concord-protocol/concord/pull/23

## protocol-and-spec-work:marmot-moved-devices-keep-trusting-the-old-group-until-the-first-commi
- INCLUDE: Marmot: moved devices keep trusting the old group until the first Commit
- Reason: Protocol and Spec Work: Marmot, the end-to-end encrypted group messaging protocol built on MLS and Nostr, merged five device-group and departure changes between 4 and 9 November.
- https://github.com/marmot-protocol/marmot/pull/498

## protocol-and-spec-work:marmot-reset-a-local-device-group-without-losing-chats
- INCLUDE: Marmot: reset a local device group without losing chats
- Reason: Protocol and Spec Work: A device link can disappear from a device group's roster.
- https://github.com/marmot-protocol/marmot/pull/499

## protocol-and-spec-work:marmot-inactive-sibling-devices
- INCLUDE: Marmot: inactive sibling devices
- Reason: Protocol and Spec Work: After 30 days of caught-up inactivity, a device marks a sibling device `inactive`.
- https://github.com/marmot-protocol/marmot/pull/500

## protocol-and-spec-work:marmot-last-active-admin-cannot-leave
- INCLUDE: Marmot: last active admin cannot leave
- Reason: Protocol and Spec Work: Under a departure rule, a leaving admin repeats its step-down while another admin remains.
- https://github.com/marmot-protocol/marmot/pull/501

## protocol-and-spec-work:marmot-admins-step-down-before-leaving
- INCLUDE: Marmot: admins step down before leaving
- Reason: Protocol and Spec Work: A refused or lost step-down could stall a leave.
- https://github.com/marmot-protocol/marmot/pull/502

## protocol-and-spec-work:marmot-drafts-one-shot-agent-decisions
- INCLUDE: Marmot drafts one-shot agent decisions
- Reason: Protocol and Spec Work: An open draft specifies one-shot agent decisions: a software agent in an encrypted group asks one question and gets one answer, as ordinary encrypted group messages.
- https://github.com/marmot-protocol/marmot/pull/503

## protocol-and-spec-work:nip-d9-proposes-events-that-resist-deletion
- INCLUDE: NIP-D9 proposes events that resist deletion
- Reason: Protocol and Spec Work: An open NIP-D9 proposal lets an author mark a regular event with a `no_delete` tag, exempting it from that author's own NIP-09 (deletion requests) and NIP-62 (request to vanish) requests, even if the request arrives first.
- https://github.com/nostr-protocol/nips/pull/2531

## deep-dive:nip-deep-dive-nip-88-polls
- INCLUDE: NIP Deep Dive: NIP-88 (Polls)
- Reason: NIP Deep Dive: NIP-88 (Polls): NIP-88: Polls lets anyone post a public poll that any client can count from events on ordinary relays, without a poll service.
- https://github.com/nostr-protocol/nips/blob/master/88.md
- https://github.com/nostr-protocol/nips/pull/1346
- https://github.com/nostr-protocol/nips/pull/1507
- https://github.com/vitorpamplona/amethyst
- https://github.com/barrydeen/wisp-ios/blob/914febaf597fc044a680ead632931009b21d641a/PollTallyRepository.swift#L268-L274
- https://github.com/vitorpamplona/amethyst/blob/4fb29192d502542f714e1526ac229378617922fe/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/model/nip88Polls/PollResponsesCache.kt#L169-L220
- https://github.com/vitorpamplona/amethyst/blob/4fb29192d502542f714e1526ac229378617922fe/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/model/nip88Polls/PollTallyPolicy.kt#L57-L63
- https://github.com/vitorpamplona/amethyst/blob/4fb29192d502542f714e1526ac229378617922fe/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/model/nip88Polls/PollTallyPolicy.kt#L77-L81
- https://github.com/hzrd149/nostrudel/blob/25cb0e27af39eed10245680a7c28c4f0b49eb731/src/helpers/nostr/polls.ts#L21-L37
- https://github.com/hzrd149/applesauce/blob/961979353a39dded606cd1a8eeedaf66c46b272c/packages/common/src/helpers/poll.ts#L86-L99
- https://github.com/coracle-social/welshman/blob/aa655bd6aae025bcc082af08c65c76cbc80a6432/packages/domain/src/kinds/Poll.ts#L51-L79
- https://github.com/coracle-social/coracle/blob/81581be7d1dec59e274dea2d65096ad5774c7eab/src/app/shared/NoteContentKind1068.svelte#L26-L31
- https://github.com/barrydeen/wisp-ios/blob/914febaf597fc044a680ead632931009b21d641a/PollTallyRepository.swift#L206-L232
- https://github.com/nostur-com/nostur-ios-public/releases/tag/1.35.0

## skip:kryfo-gnosiworks-kryfo-v0-6-0
- SKIP: Kryfo (gnosiworks/kryfo) v0.6.0
- Reason: Skipped in triage: notes state no Nostr surface.
- https://github.com/gnosiworks/kryfo

## skip:better-auth-nostr-leon-wbr-better-auth-nostr-v0-6-0
- SKIP: better-auth-nostr (leon-wbr/better-auth-nostr) v0.6.0
- Reason: Skipped in triage: login nonce storage fix only; narrow.
- https://github.com/leon-wbr/better-auth-nostr

## skip:cosign-sybenx-cosign-v0-12-10
- SKIP: Cosign (sybenx/cosign) v0.12.10
- Reason: Skipped in triage: ping cadence/infra.
- https://github.com/sybenx/cosign

## skip:herdr-white-noise-remote-tidley-codr-v0-11-1
- SKIP: HERDR White Noise Remote (tidley/codr) v0.11.1
- Reason: Skipped in triage: plugin UX only.
- https://github.com/tidley/codr

## skip:mostro-cli-mostrop2p-mostro-cli-v0-17-0-v0-17-1
- SKIP: mostro-cli (MostroP2P/mostro-cli) v0.17.0/v0.17.1
- Reason: Skipped in triage: commit-log CLI rewrite, no protocol change stated; no Mostro entry this week.
- https://github.com/MostroP2P/mostro-cli

## skip:routstrd-routstr-routstrd-v0-5-0
- SKIP: Routstrd (routstr/routstrd) v0.5.0
- Reason: Skipped in triage: AI proxy fixes, no Nostr surface.
- https://github.com/routstr/routstrd

## skip:swift-nostr-client-yysskk-swift-nostr-client-0-10-0
- SKIP: swift-nostr-client (yysskk/swift-nostr-client) 0.10.0
- Reason: Skipped in triage: API rename/consistency churn.
- https://github.com/yysskk/swift-nostr-client

## skip:algia-mattn-algia-v0-0-138
- SKIP: algia (mattn/algia) v0.0.138
- Reason: Skipped in triage: release tooling.
- https://github.com/mattn/algia

## skip:citrine-greenart7c3-citrine-v3-2-2
- SKIP: Citrine (greenart7c3/Citrine) v3.2.2
- Reason: Skipped in triage: reliability fixes (import speed, redial); below bar this week.
- https://github.com/greenart7c3/Citrine

## skip:fips-ts-mmalmi-fips-ts-runtime-v0-0-58-0-0-61
- SKIP: fips-ts (mmalmi/fips-ts) runtime-v0.0.58–0.0.61
- Reason: Skipped in triage: transport internals.
- https://github.com/mmalmi/fips-ts

## skip:haps-mmalmi-haps-v0-1-26-27
- SKIP: Haps (mmalmi/haps) v0.1.26/27
- Reason: Skipped in triage: packaging.
- https://github.com/mmalmi/haps

## skip:hashtree-mmalmi-hashtree-runtime-releases
- SKIP: Hashtree (mmalmi/hashtree) runtime releases
- Reason: Skipped in triage: relay default change only.
- https://github.com/mmalmi/hashtree

## skip:kithmoot-forgesworn-kithmoot-v0-1-126-0-1-139
- SKIP: Kithmoot (forgesworn/kithmoot) v0.1.126–0.1.139
- Reason: Skipped in triage: version cadence; private-node migration not documented in protocol terms.
- https://github.com/forgesworn/kithmoot

## skip:linky-linky-fit-linky-v26-11-1-2
- SKIP: Linky (linky-fit/linky) v26.11.1/2
- Reason: Skipped in triage: UI/listings.
- https://github.com/linky-fit/linky

## skip:magnetar-awake-devel-magnetar-v0-3-2-probepex1
- SKIP: Magnetar (awake-devel/magnetar) v0.3.2-probepex1
- Reason: Skipped in triage: BitTorrent PEX, no Nostr surface.
- https://github.com/awake-devel/magnetar

## skip:marble-sybenx-marble-v0-12-24-0-12-29
- SKIP: Marble (sybenx/marble) v0.12.24–0.12.29
- Reason: Skipped in triage: sync safety/UI patches, below bar.
- https://github.com/sybenx/marble

## skip:napplets-web-packages-napplet-web
- SKIP: Napplets - Web Packages (napplet/web)
- Reason: Skipped in triage: NAP-NAVIGATION draft support in packages; draft-only, no spec change in window.
- https://github.com/napplet/web

## skip:nostr-wot-extension-nostr-wot-nostr-wot-extension-v0-8-23
- SKIP: nostr-wot-extension (nostr-wot/nostr-wot-extension) v0.8.23
- Reason: Skipped in triage: unlock fix, not Nostr.
- https://github.com/nostr-wot/nostr-wot-extension

## skip:nostrappshell-git-nostrdev-com-stuff-nostrappshell-and-pakstr-git-nost
- SKIP: NostrAppShell (git.nostrdev.com/stuff/NostrAppShell) and pakstr (git.nostrdev.com/stuff/pakstr) v1.0.0–1.1.0
- Reason: Skipped in triage: Android bridge refactor and Amber request serialization; early-stage scaffold, same notes duplicated.
- https://git.nostrdev.com/stuff/NostrAppShell
- https://git.nostrdev.com/stuff/pakstr

## skip:nostream-cameri-nostream-3-13-0-3-15-1
- SKIP: nostream (Cameri/nostream) 3.13.0–3.15.1
- Reason: Skipped in triage: operator rate limits/metrics and web headers.
- https://github.com/Cameri/nostream

## skip:nostrube-flox1an-nostube-v0-2-54-0-2-73
- SKIP: Nostrube (flox1an/nostube) v0.2.54–0.2.73
- Reason: Skipped in triage: installers only.
- https://github.com/flox1an/nostube

## skip:xmradar-kyc-rip-xmradar-v0-6-11-0-6-16
- SKIP: XMRadar (KYC-rip/xmradar) v0.6.11–0.6.16
- Reason: Skipped in triage: mostly non-Nostr; inbox relay item too thin.
- https://github.com/KYC-rip/xmradar

## skip:alby-hub-getalby-hub-v1-24-6
- SKIP: Alby Hub (getAlby/hub) v1.24.6
- Reason: Skipped in triage: Lightning/UX.
- https://github.com/getAlby/hub

## skip:bitcoin-safe-andreasgriffin-bitcoin-safe-2-3-0
- SKIP: Bitcoin-Safe (andreasgriffin/bitcoin-safe) 2.3.0
- Reason: Skipped in triage: Bitcoin-only.
- https://github.com/andreasgriffin/bitcoin-safe

## skip:divine-divinevideo-divine-mobile-1-0-28
- SKIP: diVine (divinevideo/divine-mobile) 1.0.28
- Reason: Skipped in triage: polls/DM fixes without stated kinds; consumer UI.
- https://github.com/divinevideo/divine-mobile

## skip:lawallet-android-lawalletio-android-wallet-v1-3-1-1-3-2
- SKIP: LaWallet Android (lawalletio/android-wallet) v1.3.1/1.3.2
- Reason: Skipped in triage: NFC/Lightning.
- https://github.com/lawalletio/android-wallet

## skip:napplet-soy-zeschlauskwab-napplet-soy-soyli-v0-32-0-0-32-1
- SKIP: napplet.soy (zeSchlausKwab/napplet-soy) soyli-v0.32.0/0.32.1
- Reason: Skipped in triage: narrow hello-port binding fix.
- https://github.com/zeSchlausKwab/napplet-soy

## skip:sidecar-dmnyc-sidecar-v1-17-0
- SKIP: Sidecar (dmnyc/sidecar) v1.17.0
- Reason: Skipped in triage: translations.
- https://github.com/dmnyc/sidecar

## skip:nostr-army-knife-nak-fiatjaf-nak-v0-22-3
- SKIP: Nostr Army Knife (nak) (fiatjaf/nak) v0.22.3
- Reason: Skipped in triage: empty notes.
- https://github.com/fiatjaf/nak

## skip:iris-kit-mmalmi-iris-kit-runtime-v0-2-8
- SKIP: iris-kit (mmalmi/iris-kit) runtime-v0.2.8
- Reason: Skipped in triage: relay default.
- https://github.com/mmalmi/iris-kit

## skip:lumen-nogringo-lumen-v0-3-0
- SKIP: Lumen (nogringo/lumen) v0.3.0
- Reason: Skipped in triage: bare changelog.
- https://github.com/nogringo/lumen

## skip:nostr-pubsub-mmalmi-nostr-pubsub-ts-v0-5-25
- SKIP: nostr-pubsub (mmalmi/nostr-pubsub) ts-v0.5.25
- Reason: Skipped in triage: receipt fix.
- https://github.com/mmalmi/nostr-pubsub

## skip:nail-formstr-hq-nail-v0-4-1
- SKIP: Nail (formstr-hq/nail) v0.4.1
- Reason: Skipped in triage: bare compare link.
- https://github.com/formstr-hq/nail

## skip:pollerama-2-3-2
- SKIP: Pollerama 2.3.2
- Reason: Skipped in triage: no notes; Zapstore-only patch.
- https://zapstore.dev/apps

## skip:nymchat-3-75-545-nym
- SKIP: Nymchat 3.75.545 (NYM)
- Reason: Skipped in triage: version cadence.
- https://zapstore.dev/apps

## skip:imwald-android-0-5-22
- SKIP: Imwald Android 0.5.22
- Reason: Skipped in triage: no notes.
- https://zapstore.dev/apps

## skip:deepmarks-2-2-21
- SKIP: Deepmarks 2.2.21
- Reason: Skipped in triage: no notes.
- https://zapstore.dev/apps

## skip:flotilla-1-15-1
- SKIP: Flotilla 1.15.1
- Reason: Skipped in triage: patch, no notes.
- https://zapstore.dev/apps

## skip:trikey-foss-0-1-26-alpha
- SKIP: Trikey FOSS 0.1.26-alpha
- Reason: Skipped in triage: NEW-APP, Nostr surface unverified.
- https://zapstore.dev/apps

## skip:malachite-0-1-1
- SKIP: Malachite 0.1.1
- Reason: Skipped in triage: NEW-APP, Nostr surface unverified this run.
- https://zapstore.dev/apps

## skip:dark-wisp-enhanced-1-0-5
- SKIP: Dark Wisp Enhanced 1.0.5
- Reason: Skipped in triage: NEW-APP, unverified.
- https://zapstore.dev/apps

## skip:coinos-v3-1-14
- SKIP: coinos v3 1.14
- Reason: Skipped in triage: NEW-APP, Lightning wallet; unverified Nostr surface.
- https://zapstore.dev/apps

## skip:symudol-1-0-1
- SKIP: Symudol 1.0.1
- Reason: Skipped in triage: NEW-APP, unverified.
- https://zapstore.dev/apps

## skip:outlink-1-1-13
- SKIP: Outlink 1.1.13
- Reason: Skipped in triage: NEW-APP, unverified.
- https://zapstore.dev/apps

## skip:tendrl-0-19-0
- SKIP: tendrl 0.19.0
- Reason: Skipped in triage: NEW-APP, unverified.
- https://zapstore.dev/apps

## skip:nip-34-1-patch-on-gitworkshop-dev-1-issue-on-whitenoise-linux
- SKIP: NIP-34: 1 patch on gitworkshop.dev, 1 issue on Whitenoise Linux
- Reason: Skipped in triage: routine single items.
- https://zapstore.dev/apps

## Publication-day release refresh (2026-11-11)

Bounded GraphQL check of 764 tracked repositories for releases published after the 2026-11-10T15:05:00Z pass cutoff (18 repository lookups failed and stay UNKNOWN).

- Include: LNbits v1.7.0 / v1.7.1 — https://github.com/lnbits/lnbits/releases/tag/v1.7.0 , https://github.com/lnbits/lnbits/releases/tag/v1.7.1 , https://news.lnbits.com/news/lnbits-1-7-0-security-update (critical security release; operators must upgrade and rotate keys; ships NIP-17 notifications covered in #46).
- Extend existing item: nostr-social-graph v4.1.0 — https://github.com/mmalmi/nostr-social-graph/releases/tag/v4.1.0
- Skip as routine version bumps without material Nostr change notes (e.g. https://github.com/forgesworn/kithmoot/releases/tag/v0.1.143): nomisma v0.1.5/v0.1.6, kithmoot v0.1.141–143, linky v26.11.3, nostrmarket v1.2.1, mattn/nostr-relay v0.0.269/270, Haven-App v0.1.13, mesh-llm v0.79.0, hashtree-ts-runtime 0.5.42–44, iris-kit runtime 0.2.9/0.2.10, nostr-pubsub ts 0.5.27/0.5.28 and reconcile 0.1.2, napplet web packages, routstrd v0.5.1, monostr v0.35.1/v0.35.2 (Monostr already covered), napplet-soy soyli-v0.33.0.
