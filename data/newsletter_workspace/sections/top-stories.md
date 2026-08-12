## Top Stories

### nostr-wot-extension 0.4.0 adds post-quantum keys beside a Nostr identity

[nostr-wot-extension 0.4.0](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.4.0) is a browser extension for managing Nostr identities and signing. Accounts created from a 24-word seed can now derive ML-KEM-1024 encryption and ML-DSA-87 signing keys alongside their existing Nostr key. A one-click flow publishes a kind `10203` attestation that binds the Nostr public key to both post-quantum public keys and includes an ML-DSA proof of possession. Accounts imported from a 12-word mnemonic, bare `nsec`, remote signer, or read-only key cannot use the derivation flow, and the extension explains that limitation in the account view.

The release also adds opt-in post-quantum direct messages. It combines the ML-KEM shared secret with the existing NIP-44 encrypted-message conversation key through HKDF, then keeps the normal NIP-59 metadata-hiding gift-wrap layers for relay delivery. Encryption never silently falls back after a recipient opts in, while decryption selects the appropriate path automatically. This protects the new message path against later recovery of a present-day Nostr private key, but it does not replace secp256k1 event signatures; the release explicitly leaves that larger migration for future coordination with relays and clients.

### Divine Mobile 1.0.19 tightens accounts, private messages, and publishing

[Divine Mobile 1.0.19](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.19) is a mobile short-video client that publishes and retrieves videos through Nostr. Its account switcher now builds each signed-in identity around an account-scoped container, and a publishing fix prevents a video from being sent under the wrong account. Relay publication paths now wait for an `OK` response with explicit success semantics, while a relay `CLOSED` frame can terminate its own pending query instead of leaving the request hanging.

Private-message handling rejects unauthenticated rumor fields and unsigned seals, restores four missing-message cases, and routes group conversations from fully followed participants into the inbox. The release also preserves the tags on addressable video events when lists are updated and consumes observed deletion requests so removed videos disappear from local state. Those changes follow the per-relay query timeout work covered last week, but move the focus from retrieval isolation to identity boundaries, message validation, and publish confirmation.

### MDK 0.9.11 hardens Marmot group convergence and recovery

[MDK 0.9.11](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.11) is a Rust development kit for Marmot, an encrypted group-messaging protocol carried over Nostr. The release builds a larger convergence and recovery system around the group state machine: stale convergence passes reopen at the current group tip, inbound capability projections commit atomically, deferred messages receive bounded lifetimes across restarts, and commit-addressed checkpoints help recover an identity's own commit forks. Non-stable sends can be queued and recovered, while an epoch-stall path escalates to backfill and sent messages survive convergence work.

Storage and host integrations receive a parallel hardening pass. MDK securely deletes pruned SQLite projections, zeroizes imported private keys, NIP-49 encrypted-key export intermediates, and OpenMLS serialization buffers, and redacts group image keys from debug output. Account import can resume after interruption, iOS and Android private-storage paths are repaired, and hosts can explicitly close storage before suspension. New lightweight roster and local-membership projections reduce what applications must read, while the Hermes connector can deliver several agent-generated images as one Marmot album.

### Nostria 4.1.67 expands encrypted-community administration

[Nostria 4.1.67](https://github.com/nostria-app/nostria/releases/tag/v4.1.67) is a web and desktop social client for Nostr. It builds on the experimental NIP-29 relay-managed groups and Concord encrypted communities introduced in 4.1.53, adding community dissolution, icon and banner administration, encrypted photo uploads with compressed previews, a full reaction picker, and a dual-pane layout that keeps a community open while the user reads notes or articles. The release also adds threaded messaging and a combined hub for public, group, and private chats.

### Amber 6.4.0 makes every grouped signing decision explicit

[Amber 6.4.0](https://github.com/greenart7c3/Amber/releases/tag/v6.4.0) is an Android signer that keeps Nostr private keys separate from the applications requesting signatures. Its redesigned multi-request screen provides Approve and Deny controls for each request and each group, replacing the previous selection-and-confirm flow. Denied requests sent through Amber's relay-mediated bunker interface now receive proper error responses, so the requesting client can distinguish rejection from a stalled signer.

Amber also adds localized, human-readable labels for 113 more event kinds across every shipped locale. The additions include Concord group events, NIP-51 Git repository bookmarks, and NIP-53 room-presence events, giving users more context about unfamiliar data before they approve a signature. A concurrent-map guard also fixes a relay-subscription crash that could produce a `NegativeArraySizeException`.

### Safebox Acorn separates a portable recovery component from the web app

[Safebox Acorn](https://github.com/trbouma/safebox-acorn) is a standalone Python component and command-line interface for safeguarding user-controlled keys, funds, and records with Nostr-backed state. Extracting Acorn from the broader Safebox web application lets another Python project install the runtime and use its key, Nostr profile, relay, record, Cashu, Lightning, and cryptographic helpers without taking on the web interface. Its current record-protection primitives can generate a fresh 256-bit key, derive one from separately supplied entropy, and encode the exact key as a checksummed 24-word recovery phrase.

The project's [recovery and continuity guide](https://trbouma.github.io/safebox-acorn/recovery-and-continuity/) frames Acorn as the replaceable protocol component inside a household or community Safebox. The design keeps encrypted state available through a local relay and independent replicas so recovery does not depend on one appliance, application, relay, mint, or service provider. The documentation is careful about the present boundary: protected-record encryption remains under design, so applications should not make records depend on the new record-protection key until that profile has been implemented and reviewed.

GATE: PASS: six approved Top Stories included; all six first mentions define the project; five tagged releases, six canonical repositories, and the Safebox Digital Go-Bag guide were checked as primary sources; exact source links are direct; continuity, Nostr scope, no-em-dash, banned-phrase, and unsupported-claim self-checks passed.
