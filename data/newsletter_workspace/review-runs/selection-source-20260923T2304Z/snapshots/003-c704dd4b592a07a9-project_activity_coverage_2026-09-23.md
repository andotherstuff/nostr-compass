# Wednesday project-activity triage — Compass #41

The finalized Wednesday project artifact is `data/project_updates/updates_2026-09-14_2026-09-23.json`. These are all 38 projects with at least five merged PRs in the frozen window. Activity count triggers inspection, not automatic coverage. The prior project audit's eight selections were checked against the late PR delta.

## GREEN — eight selected project-activity items

- `divinevideo/divine-mobile` (182): [relay reconnection](https://github.com/divinevideo/divine-mobile/pull/9246) restores passive subscriptions.
- `SnowCait/nostter` (125): [session-owned remote signing](https://github.com/SnowCait/nostter/pull/2518) fixes signer lifecycle.
- `Conduit-BTC/conduit-mono` (77): [Blossom product images](https://github.com/Conduit-BTC/conduit-mono/pull/503) add signed marketplace media.
- `block/buzz` (56): [relay moderation routes](https://github.com/block/buzz/pull/7302) gain signed authorization and an audit trail.
- `zapcooking/frontend` (16): [NIP-92 descriptions](https://github.com/zapcooking/frontend/pull/746) improve image interoperability.
- `contextvm/ts-sdk` (10): [first relay acknowledgement](https://github.com/ContextVM/sdk/pull/100) shortens Nostr publish waits.
- `Cameri/nostream` (9): [signed NIP-66 health](https://github.com/cameri/nostream/pull/741) enables relay monitoring.
- `MostroP2P/mostro` (9): [stable order creation](https://github.com/MostroP2P/mostro/pull/971) implements the current NIP-69 proposal.

## FOLD — eleven projects already covered by their release candidate

- `marmot-protocol/mdk` (132): [0.10.4](https://github.com/marmot-protocol/mdk/releases/tag/v0.10.4); later account-recovery work is not claimed as released.
- `vitorpamplona/amethyst` (38): [1.16.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.16.0); later Marmot fixes are not attributed to it.
- `fr34aky/fips2go` (19): [0.6.0](https://github.com/fr34aky/fips2go/releases/tag/v0.6.0); later IPv6 bootstrap is separate.
- `lawalletio/lawallet-nwc` (17): [2.7.1](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.7.1); no second independent milestone.
- `MostroP2P/mostro-cli` (9): [0.16.2](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.16.2); same client transport series.
- `bit-blik/bitblik` (9): [0.11.0](https://github.com/bit-blik/bitblik/releases/tag/v0.11.0); dispute/NIP-82 changes.
- `relaystr/ndk` (9): [dev.5](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.5); later fixes are not attributed to it.
- `nostr-wot/nostr-wot-extension` (7): [0.8.3](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.3); scoped NWC connections.
- `BitcreditProtocol/Bitcredit-Core` (6): [0.5.16](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.16); Nostr chain resend/resync.
- `git.nostrdev.com/stuff/NostrAppShell` (6): alias of the pakstr package series, not a second implementation.
- `git.nostrdev.com/stuff/pakstr` (6): [0.21.0–0.24.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.24.0); signer/runtime changes.

## SKIP — nineteen projects without a distinct qualifying Nostr milestone

- `michaelneale/mesh-llm` (117): payment and host-runtime work without a verified Nostr product delta.
- `breez/glow-web` (56): payment UI and recovery, not a Nostr-facing milestone.
- `elisymlabs/elisym` (33): EVM payment rail and agent infrastructure do not establish a distinct Nostr change.
- `ZeusLN/zeus` (31): wallet and payment UI fixes without a Nostr-specific outcome.
- `cashubtc/cdk` (28): Cashu melt recovery without a Nostr interface change.
- `cashubtc/nutshell` (18): mint redemption and routing, not a new Nostr surface.
- `ChadFarrow/stablekraft-app` (14): general bandwidth work below the editorial threshold.
- `lnbits/lnbits` (12): general Lightning fee settlement.
- `block-core/angor` (11): [relay subscription cleanup](https://github.com/block-core/angor/pull/968) is a bounded reliability fix, not a standalone milestone.
- `arkin0x/cyberspace` (10): site polish lacks a new Nostr capability.
- `Lokuyow/ehagaki` (8): Web Component reconnect fix below the significance threshold.
- `getAlby/hub` (8): swap infrastructure, not a discrete Nostr change.
- `routstr/routstrd` (8): routing-service maintenance without a new user-facing Nostr behavior.
- `shocknet/Lightning.Pub` (8): admin-list metadata is below the significance threshold.
- `TsukemonoGit/lumilumi` (7): no verified launch or protocol milestone.
- `jesuspirate/chama` (7): rapid releases and site polish lack one source-supported feature milestone.
- `andotherstuff/pensieve` (6): [negentropy upload PR #46](https://github.com/andotherstuff/pensieve/pull/46) explicitly says runtime remains disabled, with no listener, worker, deployment, SDK or migration.
- `dergigi/ants` (6): library iteration without demonstrated downstream adoption.
- `DhananjayPurohit/paygress` (5): no verified Nostr-facing feature above the common threshold.

GATE: PASS (38/38 high-activity projects dispositioned; eight selected, eleven folded, nineteen skipped)
