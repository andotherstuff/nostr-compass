## Newly tracked and discovered

### OpenDiscord v1.0.1 launches as a Discord-style client on Nostr

[OpenDiscord](https://github.com/sofia-gros/open-discord) is a Discord-style server-and-channel client built on Nostr with role-based permissions and WebRTC/SFU voice lobbies. [v1.0.1](https://github.com/sofia-gros/open-discord/releases/tag/v1.0.1) is the project's first tagged installer release.

### Auditable Voting v0.1.140 aligns organiser, voter, and audit-proxy roles

[Auditable Voting](https://github.com/tidley/auditable-voting) is a client-only Nostr voting shell. [v0.1.140](https://github.com/tidley/auditable-voting/releases/tag/v0.1.140) aligns the organiser, voter, and audit-proxy roles with the exact organiser-signed public questionnaire-definition event, closing a gap where an audit proxy could act on stale generated accounts or state persisted from a different worker or organiser.

### Cambium v0.3.2 pairs with Heartwood as a keyless NIP-55 signer

[Cambium](https://github.com/forgesworn/cambium) is this issue's Discovery pick: an Android [NIP-55](/en/topics/nip-55/) signer that holds no private key material of its own, proxying every signing request over [NIP-46](/en/topics/nip-46/) to a companion Heartwood hardware signer. The project shares the `forgesworn` GitHub org with tracked project Bray, and Heartwood itself was covered in #30 shipping the relay-to-serial signing bridge that Cambium's Android side now talks to. [v0.3.2](https://github.com/forgesworn/cambium) polishes the approval sheet to warn live when the selected identity differs from the app's existing binding and moves activity-log writes to a single non-blocking queue.

### Also launching this week: echoes, Dispatch, and Linky

Three more launches are worth a mention this week. [echoes](https://github.com/Lwb89dev/echoes) is an offline-first, end-to-end encrypted notes app that syncs privately over Nostr. [Dispatch](https://github.com/freecritter/dispatch) is a local-first travel organizer where every save is [NIP-44](/en/topics/nip-44/)-encrypted and backed up over Nostr under a dedicated, unlinkable key, and its [v0.3.0](https://github.com/freecritter/dispatch) release adds Amber [NIP-55](/en/topics/nip-55/) login so the app never touches the user's private key directly. [Linky](https://github.com/hynek-jina/linky) combines Nostr contacts and DMs with Lightning and Cashu payments in a single progressive web app.

GATE: PASS
