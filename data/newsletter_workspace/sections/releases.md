## Releases

### Mostro Core 0.14.2 changes the encrypted chat envelope

[Mostro Core](https://github.com/MostroP2P/mostro-core) is the Rust library of shared types and peer-to-peer functions used by the Mostro exchange daemon and its clients. [Version 0.14.2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.2) replaces gift-wrapped chat messages with kind 14 envelopes that use separate conversation-encryption and signing keys derived from the peers' shared secret. The new reader validates the author, signature, recipient, timestamp, and content size, while legacy gift-wrap helpers remain available so clients can read both formats during migration.

### LaWallet NWC 2.3.0 adds Nostr notifications and zap receipts

[LaWallet NWC](https://github.com/lawalletio/lawallet-nwc) is an open-source Lightning Address platform that connects wallets through [Nostr Wallet Connect](/en/topics/nip-47/). [Version 2.3.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.3.0) lets each wallet send received and forwarded notifications as configurable Nostr events, including a recipient `p` tag, selected relays, templated content, and optional [NIP-44](/en/topics/nip-44/) encryption; retries reuse the same signed event ID. It also accepts zap requests and publishes signed [NIP-57](/en/topics/nip-57/) kind 9735 receipts after settlement, while a new address capability view shows whether the resolved address supports NIP-05, NIP-57, and related Lightning Address protocols.

### nostr-double-ratchet TypeScript 0.0.166 binds public invites to session keys

[nostr-double-ratchet](https://github.com/irislib/nostr-double-ratchet) provides TypeScript and Rust primitives for end-to-end encrypted direct and group messaging over Nostr relays. [TypeScript 0.0.166](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.166) requires an invite response to prove ownership of its session key, preventing a reusable public invite from binding one Nostr identity to another party's session. The release also rejects malformed rumor fields and tightens payload validation; existing sessions continue to work, but an updated inviter rejects proofless responses from older invitees.

### cln-nip47 0.2.0 expands and isolates NWC requests

[cln-nip47](https://github.com/daywalker90/cln-nip47) is a Core Lightning plugin that exposes a node to wallets through [Nostr Wallet Connect](/en/topics/nip-47/). [Version 0.2.0](https://github.com/daywalker90/cln-nip47/releases/tag/v0.2.0) adds NWC methods to create, cancel, and settle hold invoices plus a `hold_invoice_accepted` notification, and it advertises the method set that the connected node actually supports. Transaction-list responses now stop at 500 entries and about 128 kB, request events are deduplicated by event ID, and one client's failed notification no longer prevents delivery to other clients. The release also removes the two multi-payment methods that are no longer part of the NWC specification.

### ClipRelay 0.1.3 restores relay and signer connections after idle periods

[ClipRelay](https://github.com/tajava2006/cliprelay) synchronizes a user's clipboard between devices through Nostr relays, encrypting the content to the same identity with [NIP-44](/en/topics/nip-44/). The matching [desktop](https://github.com/tajava2006/cliprelay/releases/tag/desktop/v0.1.3) and [Android](https://github.com/tajava2006/cliprelay/releases/tag/android/v0.1.3) 0.1.3 releases add a text box for sending typed text directly to another device's clipboard. They also test liveness with real relay round trips after idle periods, escalating from resubscription to socket replacement and a rebuilt connection pool, while stalled [NIP-46](/en/topics/nip-46/) signer calls now time out and rebuild automatically.

### NoorNote 1.3.2 moves article discovery into the social graph

[NoorNote](https://github.com/77elements/noornote) is a Nostr client for social posts, encrypted messages, long-form articles, and other event types across web, desktop, and Android. [Version 1.3.2](https://github.com/77elements/noornote/releases/tag/v1.3.2) replaces its flat global article feed with discovery drawn from first-, second-, and third-degree contacts, giving readers an article timeline rooted in their follow graph. It also collapses bursts of replayed direct messages from unknown senders into one rolling notification instead of producing a stack of toasts as relay history arrives.

### Bray 2.4.0 adds a compact remote-signing dialect

[Bray](https://github.com/forgesworn/bray) is a Nostr MCP server that gives software agents and people tools for relay access, identity, publishing, and remote signing. [Version 2.4.0](https://github.com/forgesworn/bray/releases/tag/v2.4.0) accepts a signing request whose event is an object as well as the stringified form used by [NIP-46](/en/topics/nip-46/), and adds `sign_event_compact`, which returns only the event ID, signature, public key, and timestamp. That smaller request and response format reduces memory use for constrained hardware signers, while the standard `sign_event` flow remains unchanged and both dialects produce a signature over the received event's ID.

GATE: PASS: seven approved tagged releases are present; all release links, complete primary notes, tag comparisons, and linked PR claims were verified, and every paragraph is limited to Nostr-facing behavior.
