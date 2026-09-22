## Protocol and Spec Work

### NIP-02 clarifies petnames in follow lists

[NIP-02 (Follow List)](/en/topics/nip-02/) standardizes the kind `3` event that records whom an account follows and can attach a local petname to each followed key. The [merged petname clarification](https://github.com/nostr-protocol/nips/pull/2472) allows display-safe characters while preserving the field as a user's local label, not a globally verified name.

### NIP-AC proposes relay-bootstrapped WebRTC signaling

[NIP-AC](https://github.com/nostr-protocol/nips/pull/2461) is an open proposal for using signed Nostr events to discover peers and exchange WebRTC offers, answers, and ICE candidates before traffic moves to a direct connection. NIP-59 standardizes gift wrapping that hides an event's sender and metadata inside encrypted envelopes. The proposal covered last week has since shipped a revised draft that keeps relays out of the established data path, uses ordinary `p` and `e` tags for recipients and session correlation, and recommends that gift-wrapping scheme when signaling metadata needs concealment.

### NIP-86 proposes clear and list methods for relay management

[NIP-86 (Relay Management API)](/en/topics/nip-86/) standardizes authenticated administrative calls for banning, allowing, inspecting, and configuring a relay. [PR #2477](https://github.com/nostr-protocol/nips/pull/2477) proposes methods for clearing pubkeys or events from both allow and ban lists and for listing roles, allowed events, and disallowed kinds, including behavior already present in the khatru relay framework and the go-nostr library.

### NIP-69 proposes a stable creation time for trading orders

[NIP-69 (Peer-to-Peer Trading)](/en/topics/nip-69/) standardizes addressable order events that let multiple trading applications share buy and sell liquidity. [PR #2476](https://github.com/nostr-protocol/nips/pull/2476) proposes an optional creation-time tag that stays fixed across status updates, so a returned or republished order does not look newly created merely because its event timestamp changed.

### NIP-A3 proposes proof of payment-address ownership

[NIP-A3 (Payment Targets)](/en/topics/nip-a3/) lets an account publish portable payment addresses for multiple networks in one replaceable event. [PR #2475](https://github.com/nostr-protocol/nips/pull/2475) proposes an optional signature made by the payment address's own key, giving compatible address types a proof that binds the destination to the Nostr author while treating missing proofs as neutral.

### BUD-16 proposes deterministic directory manifests

[BUD-16](https://github.com/hzrd149/blossom/pull/105) is an open Blossom proposal for grouping content-addressed blobs into named directory trees with reproducible manifest hashes. The draft defines deterministic MessagePack encoding, named links, metadata, optional encryption keys, and `.bdir` path resolution while leaving servers to store ordinary blobs.

### Marmot adds encrypted group polls

[Marmot Protocol](/en/topics/marmot/) defines interoperable application events inside MLS-encrypted groups carried over Nostr. NIP-88 defines poll questions and signed response events. [Merged MIP work](https://github.com/marmot-protocol/marmot/pull/425) recognizes those polls inside a group while keeping relay selection bound to authenticated group routing and explicitly stating that they are not anonymous or election-grade.

### Marmot merges group reports and admin deletion

[Marmot group moderation](https://github.com/marmot-protocol/marmot/pull/423) defines encrypted report, dismissal, and administrator-deletion events that converge under the group's authenticated state. The proposal covered last week has now merged, fixing a status transition that lets implementations align report review and message removal against the accepted specification.

### NWC-13 proposes connection budget queries

[Nostr Wallet Connect](/en/topics/nip-47/) lets an application request narrowly scoped wallet operations through encrypted Nostr events. [NWC-13](https://github.com/nostr-wallet-connect/nwc/pull/7) proposes a separate `get_budget` permission and response so an application can inspect used, total, and renewal allowance without receiving permission to read the wallet's balance.

writer_model: preferred=gemini-3.1-pro, actual=openai-codex/gpt-5.6-sol, receipt=data/newsletter_workspace/writer_receipt_2026-09-16.json

GATE: PENDING REVIEW
