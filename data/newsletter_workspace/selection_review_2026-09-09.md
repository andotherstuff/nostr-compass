# Final Selection Review — 2026-09-09

Newsletter: Nostr Compass #39

Reporting window: 2026-08-31T00:00:00Z through 2026-09-09T00:00:00Z
Owner direction: shorten the issue, remove low-value projects, and retain only projects with real progress in the reporting window.

## Evidence boundary

The local GitHub mirror was current through 2026-09-09T15:48:43Z when used for bounded discovery. Every retained GitHub release, pull request, or commit below was then read from the authenticated GitHub API with caching disabled at 2026-09-09T16:30Z–16:36Z. Nostr-native releases were recovered by exact event id with signature verification enabled. The ngit launch page reported a last update of 2026-09-08T23:58:16Z.

The prior 8/10 common threshold produced an issue with too many narrow fixes. This final pass raises the editorial bar: an item needs a dated, primary-source-backed change in the window and enough novelty or reader consequence to justify space in a weekly digest. Release cadence, packaging, metadata, dependency churn, vague activity, and minor interface polish do not qualify.

## Final selection

### Top Stories

| Project | In-window progress | Decision |
|---|---|---|
| ngit / GitWorkshop | The coordinated v3/v4 launch page was updated [2026-09-08](https://ngit.dev/v3), shipping ngit-ci 0.1, private repositories, signed releases, and the new documentation site. | KEEP, lead |
| nsite-clay | Commits from [August 31](https://github.com/jooray/nsite-clay/commit/064a0c5350f1e2b107f7d8f1de00ad75ef2e69d8) through [September 2](https://github.com/jooray/nsite-clay/commit/8f9d7d140dd3cd3e1db8726781fcd852041713f7) made browser publishing recoverable, reduced signer prompts, and improved editing controls. | KEEP |
| Wingman App | Commits from [September 2](https://github.com/OtherStuffAI/wm-app/commit/b0c9c03d317573adeafa92b1a56d696ad399e3ec) through [September 8](https://github.com/OtherStuffAI/wm-app/commit/60456ec0a8b4ed26ecde53812a61f95dc0bd22ac) added file pickers, profile publication, safe signer/session restore, and tested mobile builds. | KEEP |
| Shosho / Livelier | [Shosho 1.1.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.1.0) shipped Livelier bridge support September 1; the bridge added explicit source attribution on [August 31](https://github.com/r0d8lsh0p/livelier/commit/7d8abb875770289502b55c3d947987db08e206dc). | KEEP |
| Communitator | The August 31 launch series implemented [canonical templates](https://github.com/dyne/communitator/commit/520edd33a253ca3249993172fd1003c80bfd9b7c), [bounded signing and publication](https://github.com/dyne/communitator/commit/2bd04c8fab292e73fe9a4ada250c64358aee8501), and the reviewed consent surface. | KEEP |
| cal.emre.xyz | The public repository was created in an [initial September 2 commit](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743), followed by a signed September 3 handler announcement for the live NIP-52 service. | KEEP |
| Plektos | Private events merged [September 2](https://github.com/derekross/plektos/pull/12), with lifecycle and parser-security repairs merged [September 6](https://github.com/derekross/plektos/pull/14) and [September 6](https://github.com/derekross/plektos/pull/16). | KEEP |

### Tagged Releases

| Project | In-window progress | Decision |
|---|---|---|
| Vector | [0.4.4](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4) shipped August 31 with community recovery, key-rotation, moderation, and reply-routing fixes. | KEEP |
| Primal Android | [3.5.27](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.27) shipped September 3 after signer-identity and NWC-authentication changes merged August 31. | KEEP |
| GRAIN | [0.8.0-rc2](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc2) shipped September 7 with storage-pressure refusal, retention, teardown, and relay-discovery repairs. | KEEP |
| LibreNostr | [0.5.0–0.5.2](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) shipped September 7–8 with fail-closed Tor routing and follow-up search and thread repairs. | KEEP |
| SkateSpots | Signed release event `a13b8049…`, recovered with signature verification from the Zapstore source data and represented by the [app's Zapstore page](https://zapstore.dev/apps/org.skatespots.app), was published September 8 with an on-device relay path and stricter payment proof. | KEEP |
| Whistle | [1.8.15](https://github.com/sjmcnamara/whistle/releases/tag/v1.8.15) shipped September 3 with lifecycle and stale-socket recovery for encrypted groups. | KEEP |
| TWENTY ONE Companion | [1.12.0](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.12.0) shipped September 5 with NIP-17 direct messages and a clear legacy-chat boundary. | KEEP |
| ZapStore | [1.1.2](https://github.com/zapstore/zapstore/releases/tag/1.1.2) shipped September 4 with event-id validation; certificate-rotation support [merged the same day](https://github.com/zapstore/relay/pull/8). | KEEP |
| Amber | [6.6.1](https://github.com/greenart7c3/Amber/releases/tag/v6.6.1) shipped September 4 with permission parsing and attributable rejection responses. | KEEP |

### In Development

| Project | In-window progress | Decision |
|---|---|---|
| Zap Cooking | NIP-27 rendering [merged September 4](https://github.com/zapcooking/frontend/pull/665), followed by relay-read, NIP-50, and NWC repairs on September 6. | KEEP |
| Conduit | Blossom preferences and protected-inbox changes merged [September 2](https://github.com/Conduit-BTC/conduit-mono/pull/374), and signed relay preference reconciliation [merged September 7](https://github.com/Conduit-BTC/conduit-mono/pull/397). | KEEP |
| Amethyst, Grimoire, and Pollerama | NIP-A3 payment-target implementations landed in [Amethyst](https://github.com/vitorpamplona/amethyst/pull/4041), [Grimoire](https://github.com/purrgrammer/grimoire/commit/54052506f7a0da06dfc4cf7e969331ee61be7851), and [Pollerama](https://github.com/formstr-hq/nostr-polls/commit/5a015f1d17abecd036f3e10c88d493d23928fa98) from September 1–3. | KEEP as one ecosystem item |
| Ditto | Live-stream embeds landed [September 4](https://github.com/soapbox-pub/ditto/commit/e2a29004a65122470179c83d6ded8336a5c10dfa), followed by broad Blossom fallback and mirroring on [September 6](https://github.com/soapbox-pub/ditto/commit/1e35a0705c28f706eb40d1f99aedef3105cf6f07). | KEEP |

### Protocol Work

| Change | In-window progress | Decision |
|---|---|---|
| NIP-01 `limit: 0` | The clarification [merged September 4](https://github.com/nostr-protocol/nips/pull/2460). | KEEP |
| NIP-78 authenticated app data | The requirement [merged September 3](https://github.com/nostr-protocol/nips/pull/2458). | KEEP |
| NIP-AC WebRTC signaling | The proposal [opened September 4](https://github.com/nostr-protocol/nips/pull/2461) and remains explicitly labeled open. | KEEP, concise |

The NIP-21/NIP-27 deep dive remains because it is the issue's explanatory feature, but it must be reduced to the URI/reference contract, one verified seven-field event, practical parsing and trust boundaries, and two implementation examples.

## Removed from the current draft

- **No qualifying progress inside the window:** fips2go. Its signed app listing and v0.3.4 release are dated August 30; the release explicitly says the only user-visible change is the name.
- **Metadata or packaging rather than meaningful Nostr progress:** Mafrend 1.2.0-alpha points to the same code as its August 6 tag and changed only its Zapstore listing inside the window; FIPS 0.5.1 was also packaging-only.
- **Real but too narrow, repetitive, or low-value for this issue:** nostr-relay, Jumble, Nymchat, Wisp, Sidecar, YakiHonne Mobile, NoorNote, Chama, nostr-java, Nostr-Doc, nostr-double-ratchet, Buzz, Mostro, the four wellbeing apps, pakstr, nostr-vpn, Dart NDK, Voca, Astraea, The Relay Gazette, UnstableKraft, Relay Tools, nostr-social-graph, better-auth-nostr, and NosCall's thin desktop-interface update.
- **Commit-only work displaced by stronger user-facing changes:** cagliostr, nostr-notification-server, Gittr, Safebox Acorn, and Clave.
- **Open or overly technical proposal material without enough weekly reader value:** NIP-CD, the NIP-44 checksum correction, NIP-F5, and the Marmot history-purge proposal.

All other fetched candidates retain their explicit disposition in `selection_coverage_audit_2026-09-09.md`; this review changes only what advances into the final issue.

GATE: PASS (20 retained project items and 3 protocol changes each have direct in-window evidence; 37 low-signal draft items removed or consolidated; final prose tightening complete)
