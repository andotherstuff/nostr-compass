# Compass #41 exact project-activity audit

The frozen Wednesday project artifact is `data/project_updates/updates_2026-09-14_2026-09-23.json`, SHA-256 `b5a438b762f57bd0eb1d4549521b61f35afbaa6736f9207004796fa9c8fe3faf`.
All 80 projects and 1230 merged PR URLs were reconciled against the assembled draft.
A release-covered project is not automatically a second PR story; a skipped project has no cited Wednesday PR URL.
The machine-readable decisions include the full reviewed URL list, primary evidence, scores, hard gates, and live branch readbacks.

## Included primary PR work

- `0xchat-app/0xchat-app-main`: Four merged audit fixes close Cashu signing, gift-wrap authentication, trusted-config and WebView consent paths; no app release is claimed. https://github.com/0xchat-app/0xchat-app-main/pull/92
- `block/buzz`: Signed relay administration with transactional audit records is a distinct Nostr operator capability. https://github.com/block/buzz/pull/7302
- `Cameri/nostream`: Signed NIP-66 monitoring and opt-in trust-distance proof of work are distinct relay-operator capabilities. https://github.com/cameri/nostream/pull/741 https://github.com/cameri/nostream/pull/779
- `Conduit-BTC/conduit-mono`: Signed Blossom product-image uploads are a distinct Nostr marketplace capability. https://github.com/Conduit-BTC/conduit-mono/pull/503
- `contextvm/ts-sdk`: Positive relay acknowledgement and corrected stream sequencing change Nostr SDK transport behavior. https://github.com/ContextVM/sdk/pull/95 https://github.com/ContextVM/sdk/pull/100
- `diegogurpegui/nos2x-fox`: Merged fixes close web-page PIN extraction and stable extension identification while making NIP-07 injection deterministic; no store release is claimed. https://github.com/diegogurpegui/nos2x-fox/pull/69 https://github.com/diegogurpegui/nos2x-fox/pull/67
- `divinevideo/divine-mobile`: Passive relay reconnection and all-relay profile verification repair distinct Nostr client paths. https://github.com/divinevideo/divine-mobile/pull/9246 https://github.com/divinevideo/divine-mobile/pull/9293
- `marmot-protocol/marmot`: Merged encrypted group-poll and moderation specifications are directly covered in the protocol section. https://github.com/marmot-protocol/marmot/pull/423 https://github.com/marmot-protocol/marmot/pull/425
- `MostroP2P/mostro`: Stable order creation time is a distinct interoperable NIP-69 trading change. https://github.com/MostroP2P/mostro/pull/971
- `nostr-protocol/nips`: Merged NIP-02 and NIP-86 changes are directly covered as protocol milestones. https://github.com/nostr-protocol/nips/pull/2472 https://github.com/nostr-protocol/nips/pull/2477
- `SnowCait/nostter`: Session-owned NIP-46 signing and image-share composition change Nostr client behavior. https://github.com/SnowCait/nostter/pull/2510 https://github.com/SnowCait/nostter/pull/2518
- `zapcooking/frontend`: NIP-92 image descriptions and pre-relay secret-key search protection are distinct user-visible changes. https://github.com/zapcooking/frontend/pull/744 https://github.com/zapcooking/frontend/pull/746

## Folded or skipped PR work

- `abh3po/better-nips`: Adding one default relay is distribution configuration, not a distinct protocol or user workflow milestone. Primary readback: https://github.com/formstr-hq/better-nips/pull/3
- `andotherstuff/pensieve`: The Wednesday PRs leave archive runtime disabled; later separately reviewed archive work is covered without retroactively claiming deployment. Primary readback: https://github.com/andotherstuff/pensieve/pull/46
- `arkin0x/cyberspace`: Site presentation work has no distinct, source-verified Nostr capability beyond recent coverage. Primary readback: https://github.com/arkin0x/cyberspace/pull/34
- `barrydeen/wisp`: NIP-22 comments and wallet withdrawal are covered by the tagged Wisp release, not a second PR story. Primary readback: https://github.com/barrydeen/wisp/pull/660
- `bit-blik/bitblik`: Dispute and NIP-82 work is covered by the tagged BitBlik release rather than repeated as PR activity. Primary readback: https://github.com/bit-blik/bitblik/pull/23
- `BitcreditProtocol/Bitcredit-Core`: Bill-event resend and resync repairs are covered by the tagged Bitcredit release. Primary readback: https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1019
- `block-core/angor`: The relay cleanup is a bounded maintenance fix below a separate operator milestone. Primary readback: https://github.com/block-core/angor/pull/970
- `breez/glow-web`: Payment interface and recovery work does not establish a distinct Nostr-facing change. Primary readback: https://github.com/breez/glow-web/pull/474
- `cashubtc/cashu.me`: Duplicate Lightning payment-history repair has no distinct Nostr event or relay behavior. Primary readback: https://github.com/cashubtc/cashu.me/pull/612
- `cashubtc/cdk`: Cashu melt and mint recovery work does not create a distinct Nostr-facing milestone. Primary readback: https://github.com/cashubtc/cdk/pull/2566
- `cashubtc/nutshell`: Mint redemption and routing changes do not establish a Nostr protocol or client surface. Primary readback: https://github.com/cashubtc/nutshell/pull/1176
- `ChadFarrow/stablekraft-app`: General bandwidth iteration lacks a new source-verified Nostr capability. Primary readback: https://github.com/ChadFarrow/stablekraft-app/pull/270
- `coracle-social/coracle`: The NIP-70 compose toggle is merged, but relay acceptance was not verified and it remains below the independent product-milestone bar. Primary readback: https://github.com/coracle-social/coracle/pull/674
- `Cordn-msg/cordn`: This repository changed multi-device documentation; the separate tagged Cordn application release is covered. Primary readback: https://github.com/Cordn-msg/cordn/pull/6
- `damus-io/notedeck`: Headless and ingest hardening is an early internal step without a verified user-facing Nostr release. Primary readback: https://github.com/damus-io/notedeck/pull/1501
- `dergigi/ants`: Library iteration has no demonstrated downstream adoption or distinct product change. Primary readback: https://github.com/dergigi/ants/pull/311
- `dergigi/boris`: Linking an Android source repository is documentation, not a new capability. Primary readback: https://github.com/dergigi/boris/pull/78
- `DhananjayPurohit/paygress`: Payment application iteration has no verified Nostr-facing feature above the editorial threshold. Primary readback: https://github.com/DhananjayPurohit/Paygress/pull/88
- `elisymlabs/elisym`: EVM payment and agent infrastructure work does not establish a discrete Nostr capability. Primary readback: https://github.com/elisymlabs/elisym/pull/111
- `fiatjaf/relayer`: Storage notifier changes are a bounded internal scaling repair without a separately demonstrated operator outcome. Primary readback: https://github.com/fiatjaf/relayer/pull/168
- `forgesworn/bark`: Approval-timeout classification is general payment-tool maintenance rather than a new Nostr surface. Primary readback: https://github.com/forgesworn/bark/pull/41
- `forgesworn/bray`: Human confirmation and payment caps are important but belong to a payment tool, without a distinct Nostr change. Primary readback: https://github.com/forgesworn/bray/pull/115
- `forgesworn/toll-booth`: Credential and payment-bypass fixes concern generic payment middleware, without a demonstrated Nostr interface change. Primary readback: https://github.com/forgesworn/toll-booth/pull/99
- `formstr-hq/formstr-drive`: Media preview and outbox work is not yet a verified distinct Nostr release or complete capability. Primary readback: https://github.com/formstr-hq/formstr-drive/pull/63
- `formstr-hq/nostr-calendar`: Mail bridge invites and relay defaults do not establish a separate Nostr milestone beyond existing calendar coverage. Primary readback: https://github.com/formstr-hq/nostr-calendar/pull/215
- `formstr-hq/nostr-docs`: One default-relay configuration addition is not a distinct user or protocol milestone. Primary readback: https://github.com/formstr-hq/nostr-docs/pull/62
- `formstr-hq/nostr-forms`: Browser NIP-55 signer integration is merged, but its app deployment is unverified and it is not yet a separate release milestone. Primary readback: https://github.com/formstr-hq/nostr-forms/pull/507
- `formstr-hq/nostr-polls`: Browser NIP-55 signer integration mirrors the forms change, with no verified deployment or independent milestone. Primary readback: https://github.com/formstr-hq/nostr-polls/pull/247
- `fr34aky/fips2go`: Merged client work is covered through the verified 0.6.0 to 0.7.0 tagged releases rather than a duplicate PR story. Primary readback: https://github.com/fr34aky/fips2go/pull/46
- `getAlby/hub`: Swap infrastructure is not a discrete Nostr-facing milestone in this window. Primary readback: https://github.com/getAlby/hub/pull/2601
- `getAlby/lightning-browser-extension`: These PRs update build dependencies; the separate security release is covered by its tag. Primary readback: https://github.com/getAlby/lightning-browser-extension/pull/3629
- `git.nostrdev.com/stuff/NostrAppShell`: This is an alias of the pakstr package sequence already covered through exact release tags. Primary readback: https://git.nostrdev.com/stuff/pakstr/pulls/91
- `git.nostrdev.com/stuff/pakstr`: Signer and runtime work is covered by the 0.22.0 to 0.24.0 release sequence, not duplicated here. Primary readback: https://git.nostrdev.com/stuff/pakstr/pulls/91
- `HeterodyneNetwork/HeterodyneProtocol`: The maintenance workflow phase does not demonstrate a live Nostr protocol change. Primary readback: https://github.com/HeterodyneNetwork/HeterodyneProtocol/pull/31
- `hroomnik007/MintRadar`: Current source and signed submission support the main MintRadar story; these UI and stats PRs are not a second independent milestone. Primary readback: https://github.com/hroomnik007/MintRadar/pull/95
- `jesuspirate/chama`: Site polish and rapid tags lack one source-supported Nostr feature milestone. Primary readback: https://github.com/jesuspirate/chama/pull/24
- `lawalletio/lawallet-nwc`: NWC receipt changes are covered by the 2.7.0 to 2.7.1 release story. Primary readback: https://github.com/lawalletio/lawallet-nwc/pull/299
- `lnbits/lnbits`: Lightning settlement work has no distinct Nostr surface in the reviewed PRs. Primary readback: https://github.com/lnbits/lnbits/pull/4193
- `Lokuyow/ehagaki`: Web-component reconnect repair is useful but below a standalone significance threshold. Primary readback: https://github.com/Lokuyow/ehagaki/pull/260
- `lontivero/Nostra`: A general test and bug-fix PR does not establish a specific Nostr user change. Primary readback: https://github.com/lontivero/Nostra/pull/64
- `marmot-protocol/mdk`: Durable sends and attachment work is covered by the tagged 0.10.4 release; later account recovery is not claimed as released. Primary readback: https://github.com/marmot-protocol/mdk/pull/1993
- `marmot-protocol/whitenoise`: A landing-page proposal changes repository documentation, not the shipped messenger. Primary readback: https://github.com/marmot-protocol/whitenoise/pull/703
- `mattn/cagliostr`: Redis inter-instance propagation is a bounded implementation step without a demonstrated new Nostr client capability. Primary readback: https://github.com/mattn/cagliostr/pull/31
- `mattn/nostr-relay`: Shared-database and Redis propagation are scaling steps without a verified release or operator migration. Primary readback: https://github.com/mattn/nostr-relay/pull/33
- `michaelneale/mesh-llm`: Payment and host runtime development does not yield a verified Nostr product delta. Primary readback: https://github.com/Mesh-LLM/mesh-llm/pull/1939
- `MostroP2P/mostro-cli`: Chat transport and cancellation are covered by the tagged Mostro CLI release. Primary readback: https://github.com/MostroP2P/mostro-cli/pull/199
- `MostroP2P/mostro-core`: Trade pubkey and dispute-model fields are supporting library changes without a distinct released client behavior. Primary readback: https://github.com/MostroP2P/mostro-core/pull/173
- `nbd-wtf/nostr-tools`: NIP-42 rejection and NIP-77 error propagation repair library edge cases but are below a separate product-milestone threshold. Primary readback: https://github.com/nbd-wtf/nostr-tools/pull/559
- `nogringo/nostr-mail-client`: Relay-list and delivery choice changes are covered by the tagged Nostr Mail Client release. Primary readback: https://github.com/nogringo/nostr-mail-client/pull/68
- `nostr-wot/nostr-wot-extension`: Scoped NWC work is covered by the tagged 0.8.0 to 0.8.3 release sequence. Primary readback: https://github.com/nostr-wot/nostr-wot-extension/pull/31
- `nostr-wot/nostr-wot-oracle`: Graph readiness and persistence are covered by the tagged 0.3.0 to 0.3.1 releases. Primary readback: https://github.com/nostr-wot/nostr-wot-oracle/pull/4
- `nostr-wot/nostr-wot-sdk`: Graph storage and crawling changes are covered by the tagged 1.0.2 and graph 0.3.0 releases. Primary readback: https://github.com/nostr-wot/nostr-wot-sdk/pull/11
- `Origami74/myco`: The 0.7.0 runtime release appeared in prior coverage; current PRs add no separate verified launch. Primary readback: https://github.com/Origami74/myco/pull/52
- `penpenpng/rx-nostr`: Filtering non-relay tags from defaults is a bounded library correction below a standalone milestone. Primary readback: https://github.com/penpenpng/rx-nostr/pull/199
- `permissionlesstech/bitchat`: Mesh privacy and sync bounds do not change a verified Nostr application surface. Primary readback: https://github.com/permissionlesstech/bitchat/pull/1719
- `privkeyio/keep-android`: Removing an obsolete Android SDK CI package is build maintenance, not a user-visible Nostr change. Primary readback: https://github.com/privkeyio/keep-android/pull/522
- `relaystr/ndk`: NIP-82 and authenticated delivery work is covered by the Dart NDK prerelease story. Primary readback: https://github.com/relaystr/ndk/pull/837
- `routstr/routstrd`: Routing-service maintenance has no new user-facing Nostr behavior in this window. Primary readback: https://github.com/Routstr/routstrd/pull/110
- `rust-nostr/nostr`: Local-relay connection limits and BIP321 helpers are library increments without demonstrated downstream adoption. Primary readback: https://github.com/nostrdevkit/nostr/pull/1465
- `shocknet/Lightning.Pub`: Admin metadata changes remain below the separate Nostr significance threshold. Primary readback: https://github.com/shocknet/Lightning.Pub/pull/1038
- `shocknet/wallet2`: Dashboard and overlay work has no specific source-verified Nostr milestone. Primary readback: https://github.com/shocknet/wallet2/pull/634
- `shopstr-eng/milk-market`: Domain migration is site operations rather than a new Nostr marketplace feature. Primary readback: https://github.com/shopstr-eng/self-sown/pull/35
- `shopstr-eng/shopstr`: Marketplace search relay refresh and payout work lack a distinct, tested Nostr milestone. Primary readback: https://github.com/shopstr-eng/shopstr/pull/634
- `spacecowboy/Feeder`: Per-feed filtering and display work are useful but not a distinct Nostr interoperability milestone. Primary readback: https://github.com/spacecowboy/Feeder/pull/1228
- `TsukemonoGit/lumilumi`: No verified launch or protocol milestone is supported by the reviewed activity. Primary readback: https://github.com/TsukemonoGit/lumilumi/pull/1108
- `vitorpamplona/amethyst`: Wednesday PRs are covered by the tagged 1.16.0 release; later MLS and DECK work is separately reviewed. Primary readback: https://github.com/vitorpamplona/amethyst/pull/4180
- `zeSchlausKwab/napplet-soy`: A macOS CI probe repair is build maintenance; CLI features are covered by exact tagged releases. Primary readback: https://github.com/zeSchlausKwab/napplet-soy/pull/1
- `ZeusLN/zeus`: Wallet and payment UI fixes have no distinct Nostr-specific outcome in this window. Primary readback: https://github.com/ZeusLN/zeus/pull/4651

GATE: PASS (80/80 projects; 1230 merged PR URLs dispositioned)
