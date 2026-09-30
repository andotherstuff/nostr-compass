# Tagged-release triage — 2026-09-30

Collector: `data/project_updates/updates_2026-09-21_2026-09-29.json`; generated `2026-09-29T14:10:15.190437+00:00`; SHA-256 `97fad295ac0387e8c8ddc4560aeb5846e1ef3a618caaa5456f0f4b11ddb9ad86`.
Previous published issue: [Compass 41](/en/newsletters/2026-09-23-newsletter/).
Walked 48 projects and 127 tagged releases. This artifact records draft inclusion, not final assembly or publication.

## Assembly instructions

- Move MDK 0.11.0 and fips-pub-domains to Top Stories if selected there; delete their duplicate paragraphs from Tagged Releases. Their draft paragraphs are supplied for reuse.
- Keep each monorepo or multi-tag sequence as one story. Do not reintroduce issue 41 URLs as current releases.
- The fips-pub-domains claim and zone kinds are project placeholders, not assigned NIPs. The Elisym store-authorization kind is provisional.
- Mostro Core 0.16.0 is tagged; the coordinator v0.19.0 transport removal is merged development, not a tagged daemon release in this collector.

## Project collector: exact tag disposition

### 0ceanSlim/grain

The only tag is the rc4 release covered in issue 41.

- [v0.8.0-rc4](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc4) — SKIP: cited in issue 41.

### 77elements/noornote

The new 1.8 tags emphasize navigation and visual treatment; the 1.7 booking release was covered in issue 41.

- [v1.8.1](https://github.com/77elements/noornote/releases/tag/v1.8.1) — SKIP or HOLD per project reason.
- [v1.8.0](https://github.com/77elements/noornote/releases/tag/v1.8.0) — SKIP or HOLD per project reason.
- [v1.7.0](https://github.com/77elements/noornote/releases/tag/v1.7.0) — SKIP: cited in issue 41.

### BitcreditProtocol/Bitcredit-Core

The new tag is an automated precompiled-binary bundle without a new relay behavior; 0.5.16 was covered.

- [Precompiled binaries 4310b775](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/precompiled_4310b77585bc2c7be0da0d16aafc54fb) — SKIP or HOLD per project reason.
- [v0.5.16](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.16) — SKIP: cited in issue 41.

### Cameri/nostream

New adaptive relay event PoW and operator telemetry; selected.

- [v3.1.0](https://github.com/cameri/nostream/releases/tag/v3.1.0) — INCLUDE in draft.

### DanConwayDev/ngit-cli

Proposal-base correction is useful Nostr Git tooling maintenance, but too narrow for a full release paragraph.

- [v3.0.3](https://github.com/DanConwayDev/ngit-cli/releases/tag/v3.0.3) — SKIP or HOLD per project reason.

### DavidGershony/openChat

Group history cutoff and duplicate invite fixes affect relay delivery; 0.7.4 and 0.7.5 selected.

- [v0.7.5](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.5) — INCLUDE in draft.
- [v0.7.4](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.4) — INCLUDE in draft.
- [v0.7.3](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.3) — SKIP as a separate tag: no distinct paragraph; see project reason.
- [v0.7.2](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.2) — SKIP: cited in issue 41.
- [v0.7.1](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.1) — SKIP as a separate tag: no distinct paragraph; see project reason.
- [v0.7.0](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.0) — SKIP: cited in issue 41.

### DestBro/mafrend-zapstore

Private-group compatibility shift to current Marmot; selected with alpha caveat.

- [Mafrend 1.3.0-alpha - Profiles, Updated Map Engine, and Adopted the new Marmot spec](https://github.com/DestBro/mafrend-zapstore/releases/tag/v1.3.0-alpha) — INCLUDE in draft.

### HiveTalk/swarm

The release only adds architecture documentation.

- [v0.1.2 add architecture map](https://github.com/HiveTalk/swarm/releases/tag/v0.1.2) — SKIP or HOLD per project reason.

### MostroP2P/mostro-cli

Two-sided chat transcript display is narrow after issue 41 covered the v0.16.2 transport migration.

- [Release v0.16.3](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.16.3) — SKIP or HOLD per project reason.

### MostroP2P/mostro-core

Breaking removal of protocol-v1 gift-wrap transport from the published library; selected.

- [Release v0.16.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.16.0) — INCLUDE in draft.
- [Release v0.15.1](https://github.com/MostroP2P/mostro-core/releases/tag/v0.15.1) — INCLUDE in draft.

### Origami74/myco

New account, signer, app-store and relay-discovery behavior; selected.

- [Myco v0.8.1](https://github.com/Origami74/myco/releases/tag/v0.8.1) — INCLUDE in draft.
- [Myco v0.8.0](https://github.com/Origami74/myco/releases/tag/v0.8.0) — INCLUDE in draft.

### ZeusLN/zeus

Mostly Lightning, swaps, and wallet maintenance; NWC secret display/validation is a possible short item but below this section’s depth threshold.

- [v13.2.2](https://github.com/ZeusLN/zeus/releases/tag/v13.2.2) — SKIP or HOLD per project reason.

### barrydeen/wisp

Version bump only; issue 41 covered the last substantive release. The NIP-22 reply fix [PR #667](https://github.com/barrydeen/wisp/pull/667) merged September 24, after the September 21 tag, so it belongs in development coverage and cannot be attributed to 1.2.5.

- [v1.2.5](https://github.com/barrydeen/wisp/releases/tag/v1.2.5) — SKIP or HOLD per project reason.

### bit-blik/bitblik

The new tags fix battery use and offer loading; issue 41 covered the dispute feature in 0.11.0.

- [Release v0.11.2](https://github.com/bit-blik/bitblik/releases/tag/v0.11.2) — SKIP or HOLD per project reason.
- [Release v0.11.1](https://github.com/bit-blik/bitblik/releases/tag/v0.11.1) — SKIP or HOLD per project reason.
- [Release v0.11.0](https://github.com/bit-blik/bitblik/releases/tag/v0.11.0) — SKIP: cited in issue 41.

### block-core/angor

Main release is Bitcoin funding and wallet fixes; Nostr subscription timeout cleanup alone is below the slot threshold.

- [Angor 0.2.36](https://github.com/block-core/angor/releases/tag/v0.2.36) — SKIP or HOLD per project reason.

### block/buzz

Version tags bundle much maintenance; specific merged Nostr protocol changes are more accurately covered in the development section.

- [Buzz Desktop v0.5.25](https://github.com/block/buzz/releases/tag/desktop-v0.5.25) — SKIP or HOLD per project reason.
- [Buzz Desktop v0.5.24](https://github.com/block/buzz/releases/tag/desktop-v0.5.24) — SKIP or HOLD per project reason.

### daywalker90/cln-nip47

Dependency refresh only, no distinct Nostr Wallet Connect behavior.

- [v0.2.1](https://github.com/daywalker90/cln-nip47/releases/tag/v0.2.1) — SKIP or HOLD per project reason.

### divinevideo/divine-mobile

Release notes are broad; exact merged encrypted-video and relay-recovery PRs belong in the development section.

- [1.0.23](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.23) — SKIP or HOLD per project reason.

### elisymlabs/elisym

Collapse eleven monorepo package tags into one developing Nostr commerce story; no claim that complete checkout is deployed.

- [@elisym/pay-core@0.1.2](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/pay-core%400.1.2) — SKIP as a separate tag: no distinct paragraph; see project reason.
- [@elisym/pay-core@0.1.1](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/pay-core%400.1.1) — INCLUDE in draft.
- [@elisym/commerce@0.2.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.2.0) — INCLUDE in draft.
- [@elisym/sdk@0.40.1](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/sdk%400.40.1) — SKIP as a separate tag: no distinct paragraph; see project reason.
- [@elisym/sdk@0.40.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/sdk%400.40.0) — SKIP as a separate tag: no distinct paragraph; see project reason.
- [@elisym/mcp@0.30.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/mcp%400.30.0) — SKIP as a separate tag: no distinct paragraph; see project reason.
- [@elisym/cli@0.33.2](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/cli%400.33.2) — SKIP as a separate tag: no distinct paragraph; see project reason.
- [@elisym/sdk@0.39.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/sdk%400.39.0) — SKIP as a separate tag: no distinct paragraph; see project reason.
- [@elisym/sdk@0.38.1](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/sdk%400.38.1) — SKIP as a separate tag: no distinct paragraph; see project reason.
- [@elisym/mcp@0.29.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/mcp%400.29.0) — SKIP as a separate tag: no distinct paragraph; see project reason.
- [@elisym/cli@0.33.1](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/cli%400.33.1) — SKIP as a separate tag: no distinct paragraph; see project reason.

### forgesworn/bray

Payment caps, human confirmation, isolated Nostr Wallet Connect grants, and local payment-rail matching make one substantive developer-tool release story; selected.

- [v3.5.2](https://github.com/forgesworn/bray/releases/tag/v3.5.2) — INCLUDE in draft.
- [v3.5.1](https://github.com/forgesworn/bray/releases/tag/v3.5.1) — SKIP or HOLD per project reason.
- [v3.5.0](https://github.com/forgesworn/bray/releases/tag/v3.5.0) — INCLUDE in draft.

### forgesworn/cambium

Relay-backed phone-unlock enrollment uses private Nostr events, relay selection, and delayed new-relay connections; selected as one signer-security story with hardware-version caveats.

- [Cambium 0.7.1](https://github.com/forgesworn/cambium/releases/tag/v0.7.1) — INCLUDE in draft as patch context.
- [Cambium 0.7.0](https://github.com/forgesworn/cambium/releases/tag/v0.7.0) — INCLUDE in draft.
- [Cambium 0.6.0](https://github.com/forgesworn/cambium/releases/tag/v0.6.0) — INCLUDE in draft.
- [Cambium 0.5.0](https://github.com/forgesworn/cambium/releases/tag/v0.5.0) — SKIP or HOLD per project reason.

### forgesworn/toll-booth

Payment-service hardening without an independently explained new relay behavior.

- [v6.2.6](https://github.com/forgesworn/toll-booth/releases/tag/v6.2.6) — SKIP or HOLD per project reason.
- [v6.2.5](https://github.com/forgesworn/toll-booth/releases/tag/v6.2.5) — SKIP or HOLD per project reason.
- [v6.2.4](https://github.com/forgesworn/toll-booth/releases/tag/v6.2.4) — SKIP or HOLD per project reason.

### fr34aky/fips-pub-domains

User-submitted new signed Nostr claim and DNS verification project; selected, with draft-kind and test-scope caveats.

- [fips-pub-domains 0.2.1](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.1) — INCLUDE in draft.
- [fips-pub-domains 0.2.0](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.0) — INCLUDE in draft.
- [fips-pub-domains 0.1.0](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.1.0) — INCLUDE in draft.

### fr34aky/fips2go

0.8.0 mesh-name synchronization runs over FIPS/fips-ui and lacks a distinct Nostr-relay change; 0.7.0 was covered in issue 41.

- [v0.8.0](https://github.com/fr34aky/fips2go/releases/tag/v0.8.0) — SKIP or HOLD per project reason.
- [v0.7.0](https://github.com/fr34aky/fips2go/releases/tag/v0.7.0) — SKIP: cited in issue 41.
- [v0.6.1](https://github.com/fr34aky/fips2go/releases/tag/v0.6.1) — SKIP: cited in issue 41.

### git.nostrdev.com/stuff/NostrAppShell

Duplicate tracking row for the canonical pakstr tags; count once under pakstr.

- [v0.25.4](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.25.4) — SKIP: duplicate pakstr tracker.
- [v0.25.3](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.25.3) — SKIP: duplicate pakstr tracker.
- [v0.25.2](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.25.2) — SKIP: duplicate pakstr tracker.
- [v0.25.1](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.25.1) — SKIP: duplicate pakstr tracker.
- [v0.25.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.25.0) — SKIP: duplicate pakstr tracker.

### git.nostrdev.com/stuff/pakstr

0.25.x tags are mostly icon, proxy and CI updates; the relay-error npub change is narrow after issue 41 covered the signer milestone.

- [v0.25.4](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.25.4) — SKIP or HOLD per project reason.
- [v0.25.3](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.25.3) — SKIP or HOLD per project reason.
- [v0.25.2](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.25.2) — SKIP or HOLD per project reason.
- [v0.25.1](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.25.1) — SKIP or HOLD per project reason.
- [v0.25.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.25.0) — SKIP or HOLD per project reason.

### git.vanderwarker.family/wellbeing/cellibacy-android

Automated release note gives no verifiable Nostr behavior.

- [v2.0.8](https://git.vanderwarker.family/wellbeing/cellibacy-android/releases/tag/v2.0.8) — SKIP or HOLD per project reason.

### git.vanderwarker.family/wellbeing/holyfit-android

Automated release note gives no verifiable Nostr behavior.

- [v2.0.8](https://git.vanderwarker.family/wellbeing/holyfit-android/releases/tag/v2.0.8) — SKIP or HOLD per project reason.

### git.vanderwarker.family/wellbeing/nunlock-android

Automated release note gives no verifiable Nostr behavior.

- [v2.0.7](https://git.vanderwarker.family/wellbeing/nunlock-android/releases/tag/v2.0.7) — SKIP or HOLD per project reason.

### git.vanderwarker.family/wellbeing/saintstream-android

Automated release note gives no verifiable Nostr behavior.

- [v2.0.9](https://git.vanderwarker.family/wellbeing/saintstream-android/releases/tag/v2.0.9) — SKIP or HOLD per project reason.

### git.vanderwarker.family/wellbeing/sistercharge-android

Automated release note gives no verifiable Nostr behavior.

- [v2.0.8](https://git.vanderwarker.family/wellbeing/sistercharge-android/releases/tag/v2.0.8) — SKIP or HOLD per project reason.

### greenart7c3/Morganite

The .onion Blossom release was covered in issue 41.

- [Morganite v0.0.5](https://github.com/greenart7c3/Morganite/releases/tag/v0.0.5) — SKIP: cited in issue 41.

### greenart7c3/amber

New nostrconnect parser fix restores padded remote-signer secrets; selected. 6.6.5 was covered.

- [Release v6.6.6](https://github.com/greenart7c3/Amber/releases/tag/v6.6.6) — INCLUDE in draft.
- [Release v6.6.5](https://github.com/greenart7c3/Amber/releases/tag/v6.6.5) — SKIP: cited in issue 41.

### hedwig-corp/bitchat-to-sonar

Encrypted-chat and excessive relay-publish hotfixes; selected, keeping Cashu pivot outside the Nostr story.

- [Sonar v0.1-alpha.15.1](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.15.1) — INCLUDE in draft.
- [Sonar v0.1-alpha.15](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.15) — INCLUDE in draft.

### irislib/nostr-double-ratchet

Removed-member sender-key rotation and encrypted invite-device approval; selected.

- [TypeScript 0.0.172](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.172) — INCLUDE in draft.
- [TypeScript 0.0.171: group membership key rotation](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.171) — INCLUDE in draft.

### jesuspirate/chama

Phone alerts and trade-history fixes are useful to Chama users, but too product-specific for the release slot.

- [v6.4.13](https://github.com/jesuspirate/chama/releases/tag/v6.4.13) — SKIP or HOLD per project reason.
- [v6.4.12](https://github.com/jesuspirate/chama/releases/tag/v6.4.12) — SKIP or HOLD per project reason.
- [v6.4.11](https://github.com/jesuspirate/chama/releases/tag/v6.4.11) — SKIP or HOLD per project reason.
- [v6.4.10](https://github.com/jesuspirate/chama/releases/tag/v6.4.10) — SKIP or HOLD per project reason.
- [v6.4.9](https://github.com/jesuspirate/chama/releases/tag/v6.4.9) — SKIP or HOLD per project reason.
- [v6.4.8](https://github.com/jesuspirate/chama/releases/tag/v6.4.8) — SKIP or HOLD per project reason.
- [v6.4.7](https://github.com/jesuspirate/chama/releases/tag/v6.4.7) — SKIP or HOLD per project reason.

### jmcorgan/fips

Nostr NAT-traversal privacy fix and relay TLS security update; selected.

- [FIPS v0.5.2](https://github.com/jmcorgan/fips/releases/tag/v0.5.2) — INCLUDE in draft.

### marmot-protocol/mdk

One 0.11.0 source cohort with account-history recovery, delivery and bindings changes; selected. Older tags were covered.

- [v0.11.0 - MDK](https://github.com/marmot-protocol/mdk/releases/tag/v0.11.0) — INCLUDE in draft.
- [v0.11.0 - MarmotKit](https://github.com/marmot-protocol/mdk/releases/tag/marmotkit-v0.11.0) — SKIP as a separate tag: no distinct paragraph; see project reason.
- [v0.11.0 - Marmot C](https://github.com/marmot-protocol/mdk/releases/tag/marmotc-v0.11.0) — SKIP as a separate tag: no distinct paragraph; see project reason.
- [v0.11.0 - wn-agent](https://github.com/marmot-protocol/mdk/releases/tag/wn-agent-v0.11.0) — SKIP as a separate tag: no distinct paragraph; see project reason.
- [snapshot-03b1809e6387f2d95e566a6a2d2f1212bec4d41b - MarmotKit](https://github.com/marmot-protocol/mdk/releases/tag/marmotkit-snapshot-03b1809e6387f2d95e566a6a2d2f1212bec4d41b) — SKIP as a separate tag: no distinct paragraph; see project reason.
- [snapshot-228f4d94f906960ef58a5568b6e6012e83bf9420 - MarmotKit](https://github.com/marmot-protocol/mdk/releases/tag/marmotkit-snapshot-228f4d94f906960ef58a5568b6e6012e83bf9420) — SKIP as a separate tag: no distinct paragraph; see project reason.
- [snapshot-4df54f47b406b1c96f56f40211db979d64b44fff - MarmotKit](https://github.com/marmot-protocol/mdk/releases/tag/marmotkit-snapshot-4df54f47b406b1c96f56f40211db979d64b44fff) — SKIP as a separate tag: no distinct paragraph; see project reason.

### michaelneale/mesh-llm

Release focuses on agent runtime and CI, with no material Nostr relay surface in the tagged notes.

- [v0.77.0](https://github.com/Mesh-LLM/mesh-llm/releases/tag/v0.77.0) — SKIP or HOLD per project reason.

### mmalmi/fips-ts

The 0.0.43 runtime release was covered in issue 41.

- [Shared FIPS runtime 0.0.43](https://github.com/mmalmi/fips-ts/releases/tag/runtime-v0.0.43) — SKIP: cited in issue 41.

### mmalmi/nostr-vpn

Private-exit discovery in 4.1.16 may merit a brief item; the three tags mainly address VPN platform, wallet and upgrade reliability.

- [v4.1.17](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.1.17) — SKIP or HOLD per project reason.
- [v4.1.16](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.1.16) — SKIP or HOLD per project reason.
- [v4.1.15](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.1.15) — SKIP or HOLD per project reason.

### mouse484/astraea

Five dependency-only tags; no new user or relay behavior.

- [v5.35.179](https://github.com/mouse484/astraea/releases/tag/v5.35.179) — SKIP or HOLD per project reason.
- [v5.35.178](https://github.com/mouse484/astraea/releases/tag/v5.35.178) — SKIP or HOLD per project reason.
- [v5.35.177](https://github.com/mouse484/astraea/releases/tag/v5.35.177) — SKIP or HOLD per project reason.
- [v5.35.176](https://github.com/mouse484/astraea/releases/tag/v5.35.176) — SKIP or HOLD per project reason.
- [v5.35.175](https://github.com/mouse484/astraea/releases/tag/v5.35.175) — SKIP or HOLD per project reason.

### nostr-wot/nostr-wot-extension

0.8.4 mainly adds themes; 0.8.3 NWC connection work was covered in issue 41.

- [Nostr WoT 0.8.4 — Project themes and custom palettes](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.4) — SKIP or HOLD per project reason.
- [Nostr WoT 0.8.3 — NWC app connections](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.3) — SKIP: cited in issue 41.
- [Nostr WoT 0.8.2](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.2) — SKIP or HOLD per project reason.
- [Nostr WoT 0.8.1](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.1) — SKIP or HOLD per project reason.

### penpenpng/rx-nostr

Small default-relay tag parsing fix; useful library maintenance but below a full section slot.

- [rx-nostr@3.7.7](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.7) — SKIP or HOLD per project reason.

### r0d8lsh0p/shosho-releases

NWC and zap features are real, but the release centers on Bitcoin wallet and marketplace flows; hold for higher-confidence Nostr-specific follow-up.

- [v1.2.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.2.0) — SKIP or HOLD per project reason.

### relaystr/ndk

New Blossom identity policy and remote-signer ACK behavior; selected prerelease series.

- [Release v0.10.0-dev.9](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.9) — INCLUDE in draft.
- [Release v0.10.0-dev.8](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.8) — INCLUDE in draft.
- [Release v0.10.0-dev.7](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.7) — INCLUDE in draft.
- [Release v0.10.0-dev.6](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.6) — SKIP as a separate tag: no distinct paragraph; see project reason.

### tcheeric/nostr-java

New Blossom MCP tools and tag preservation are real but narrow relative to selected developer-tool releases.

- [v2.4.1](https://github.com/tcheeric/nostr-java/releases/tag/v2.4.1) — SKIP or HOLD per project reason.
- [v2.4.0](https://github.com/tcheeric/nostr-java/releases/tag/v2.4.0) — SKIP or HOLD per project reason.

### zeSchlausKwab/napplet-soy

Backend publishing and signer approval repair; selected as one grouped sequence. Issue 41 already covered shared creations in 0.20.0 and the 0.18.2 launch.

- [napplet soyLI 0.23.4](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.23.4) — INCLUDE in draft.
- [napplet soyLI 0.23.2](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.23.2) — INCLUDE in draft.
- [napplet soyLI 0.23.1](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.23.1) — INCLUDE in draft.
- [napplet soyLI 0.23.0](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.23.0) — SKIP as a separate tag: no distinct paragraph; see project reason.
- [napplet soyLI 0.22.0](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.22.0) — SKIP as a separate tag: no distinct paragraph; see project reason.
- [napplet soyLI 0.21.0](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.21.0) — SKIP as a separate tag: no distinct paragraph; see project reason.
- [napplet soyLI 0.20.0](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.20.0) — SKIP: cited in issue 41.
- [napplet soyLI 0.19.0](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.19.0) — SKIP as a separate tag: no distinct paragraph; see project reason.
- [napplet soyLI 0.18.2](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.18.2) — SKIP: cited in issue 41.
- [napplet soyLI 0.18.1](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.18.1) — SKIP as a separate tag: no distinct paragraph; see project reason.

## Signed Zapstore releases absent from the project collector

Source: `data/zapstore_releases/zapstore_2026-09-29.json`. Its entries carry developer-signed release event IDs; the links below target the exact primary announcement or matching forge release. These are separate from the 48-project GitHub collector count.

- **INCLUDE:** [Flotilla 1.11.2](https://github.com/coracle-social/flotilla/releases/tag/1.11.2), exact signed event [fc30a99d](https://primal.net/e/fc30a99d4badeb884dcd3ea029b0e9f95cd07de3f6c4baab09841d68251ecb35). Fixes remote-signer startup stalls and feed gaps caused by slower relays.
- **INCLUDE:** [Ditto 2.42.3](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.42.3), exact signed event [847d9743](https://primal.net/e/847d9743d3ee4284b2d8153f73af300dfad18d56b3ea01218ff4f238796286fd). Shows which relays hold a post, avoids publishing to a previous account's relays, and closes muted-push and local-network URL paths.
- **INCLUDE:** [Iris Chat 2026.9.24.4](https://github.com/irislib/iris-chat-rs/releases/tag/v2026.9.24.4), exact signed event [d4c452fd](https://primal.net/e/d4c452fddc5ad7338ec22b364f511249ac7b0131ba50fdb486b54d3835823192). Adds compatible encrypted-chat calls and separate-signer login; later patches grouped, not separate stories.
- **INCLUDE:** [LibreNostr 0.6.0](https://github.com/Lwb89dev/librenostr/releases/tag/v0.6.0), [0.6.2](https://github.com/Lwb89dev/librenostr/releases/tag/v0.6.2), and [0.7.0](https://github.com/Lwb89dev/librenostr/releases/tag/v0.7.0). Routes relay and media traffic through a built-in, fail-closed Tor option; adds a local trust filter and bounds slow relay reads. Group the three releases as one client story.
- **INCLUDE:** [Newlay 0.3.45](https://primal.net/e/b8380ae1bf30492129727ec59e27e2ae8a4cf9ad08e7361826a9ba8be88a227a). Streams large relay results with backpressure and updates the bundled Cordn delivery coordinator; its signed notes aggregate changes since store version 0.3.39.
- **INCLUDE:** [ngit-grasp 3.0.5](https://primal.net/e/6ff00b9230e4523e6f14aaf6e5088f91e5696be38b9304a4e1cef384e3318d41). Keeps live relay sync independent of history reconciliation and fixes Git push races and stalled uploads.
- **INCLUDE:** [Armada 0.63.0](https://primal.net/e/34021b55504d74c5d04f55dbfea87f31168a7c4582f35113d7ec063894d19e56). Adds closed-app browser push across extension and remote-signer logins; issue 41 covered 0.61.0, a different media-privacy release.
