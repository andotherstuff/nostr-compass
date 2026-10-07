## Top Stories

### Ants

Ants, a Nostr search client, now supports nested AND/OR searches across its [native Android release](https://github.com/dergigi/ants-android/releases/tag/v0.34.0) and [released web query compiler](https://github.com/dergigi/ants/pull/313), keeping author, event-type and date constraints tied to each branch. Android also filters result language locally. Results remain limited by selected relays, event caps and deadlines; text matching depends on relay support for [NIP-50, relay-side search](/en/topics/nip-50/).

The web app's [v0.6.0](https://github.com/dergigi/ants/releases/tag/v0.6.0) adds zap, nutzap and public mute-list cards; displayed amounts come from published invoices or proofs and do not establish settlement. Later [follow, pin and bookmark cards](https://github.com/dergigi/ants/commit/a81a1e2c628cc5aca5c5f2064652ba3bce1b7d30) read public entries while leaving encrypted private contents undisplayed.

Later Android [0.35.0](https://github.com/dergigi/ants-android/releases/tag/v0.35.0) loads zap and nutzap targets inline, including addressable notes, and adds profile-scoped media filters. [0.36.0](https://github.com/dergigi/ants-android/releases/tag/v0.36.0) shares submitted searches as ants.sh links. These links expose query text and omit local language-filter settings; results still depend on the receiving client and its relays.

### Myco

Myco, a host for small Nostr apps, [ships permission-gated uploads](https://github.com/Origami74/myco/pull/125) in [v0.10.0](https://github.com/Origami74/myco/releases/tag/v0.10.0). The shell selects [Blossom file servers](/en/topics/blossom/) and signs upload authorization without exposing the user's key to apps, returning confirmed file URLs and hashes. Uploads are capped at 16 MiB; consent comes from installation approval, with no per-upload preview or EXIF stripping.

### Marmot MDK

Marmot MDK, an encrypted messaging toolkit, [releases v0.12.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.12.0) with broader account-import discovery, separate inbox defaults and source-epoch attachment keys with bounded recovery, supported by its [implementation changes](https://github.com/marmot-protocol/mdk/pull/2138) and [companion release work](https://github.com/marmot-protocol/mdk/pull/2141). Later [merged queued-send preservation](https://github.com/marmot-protocol/mdk/pull/2172) keeps sibling failures from stopping eligible sends, but is outside that release. History beyond five epochs can remain undecryptable.

Later master work adds [beta per-account C sessions](https://github.com/marmot-protocol/mdk/pull/2154) using [NIP-46 remote signing](/en/topics/nip-46/) for remote-signer login and restore, and [backports the KEM dependency fix to 0.0.10](https://github.com/marmot-protocol/mdk/pull/2208) while retaining HPKE 0.7 compatibility. Hosts must encrypt exported signer credentials. These changes are outside v0.12.0.

Agent integrations add a [Goose terminal harness](https://github.com/marmot-protocol/mdk/pull/2199) and [admin-gated group-profile tools](https://github.com/marmot-protocol/mdk/pull/2115); [opaque draft-revision markers](https://github.com/marmot-protocol/mdk/pull/2132) help hosts distinguish newer edits during send handoff. Goose attachments and autonomous mode remain unsupported, and real-binary interoperability is unverified. Draft markers require host adoption and matching bindings; they do not authorize deletion.

### Iris Chat

Iris Chat, an encrypted messaging app, [adds message edits, edit history and deletion controls](https://github.com/irislib/iris-chat-rs/releases/tag/v2026.10.5.1). Its [author-authenticated mutation handling](https://github.com/irislib/iris-chat-rs/blob/90af94addbbaa8b9f34024f74def3b297499586f/core/src/core/message_mutations.rs) preserves deletion tombstones through replay and applies edits only after encrypted enqueue succeeds. Editing is limited to delivered, unexpired outgoing text without attachments; delete-for-everyone requests removal by compatible clients and cannot prove recipients erased their copies.

Later [device-link updates](https://github.com/irislib/iris-chat-rs/releases/tag/v2026.10.6.1) start chosen history transfer after verified local approval and preserve routed transfers when a direct link disappears. Sign-in codes remain usable until cancellation; completion waits for observed authorization. [Older-account recovery](https://github.com/irislib/iris-chat-rs/releases/tag/v2026.10.7) repairs equivalent signed device lists while stripping retired encrypted labels; conflicting authorization still fails.

writer_model: actual=openai-codex/gpt-6.1-sol, receipt=/opt/data/task-artifacts/compass-direct-2026-10-07/writer-top_stories/receipt.json; final root edits verified in assembled draft 4f46a95e8d1bad2c63d2e7b67b35c387bded0c07ac10b97c6ca12298922f354b

GATE: PENDING REVIEW
