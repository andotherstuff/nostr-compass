## Protocol and Spec Work

### NIP-A3 clarifies payment-type ambiguity

[NIP-A3 (Payment Targets)](/en/topics/nip-a3/) standardizes typed payment targets in `["payto", "<type>", "<address>"]` tags on kind `10133` events. The merged [payment-type clarification](https://github.com/nostr-protocol/nips/pull/2463) adds `bitcoincash` and `tron` to the documented type list and clarifies rendering: clients use a type-specific URI scheme when one exists, otherwise they fall back to `payto://<type>/<address>`.

### NIP-CD proposes addressable slash commands

The open [NIP-CD slash-command proposal](https://github.com/nostr-protocol/nips/pull/2462) defines addressable kind `31992` events whose `command`, `title`, `description`, `arg`, scope, and ignore tags advertise executable commands. Invocations begin at the first byte of an event's plaintext content, can target one executor by npub, and deliberately require no special client support. The draft also defines positional argument types and scope filters by event kind, relay, author, or tag; none of this is merged protocol behavior yet.

### NIP-90 proposes expiring DVM heartbeat events

[NIP-90 (Data Vending Machines)](/en/topics/nip-90/) defines job requests, results, and feedback for services that perform work over Nostr. An open [DVM heartbeat proposal](https://github.com/nostr-protocol/nips/pull/2465) adds optional kind `11998` events that should carry an `expiration` tag so clients can distinguish a live machine from a stale NIP-89 announcement. The heartbeat sits outside the NIP-90 job-kind range, lets relays discard expired or superseded heartbeats, and leaves existing DVM flows unchanged when a service does not emit it.

### NIP-73 proposes podcast-medium filters

[NIP-73 (External Content IDs)](/en/topics/nip-73/) standardizes `i` tags for external identifiers and `k` tags for their categories. The open draft [podcast-medium proposal](https://github.com/nostr-protocol/nips/pull/2468) adds optional `podcast:medium:music` and `podcast:medium:podcast` category tags so clients can filter notes by the medium declared in a podcast RSS feed. An absent category continues to imply a podcast feed, though clients should resolve the RSS source when they need to confirm its medium.

### NIP-F5 proposes permissioned FIPS transport for web apps

The open [NIP-F5 browser-transport proposal](https://github.com/nostr-protocol/nips/pull/2469) defines an optional `window.fipsTransport` API through which a Nostr web application can request user-approved HTTP or WebSocket access to a FIPS-addressed relay, Blossom server, Git service, or other private endpoint. The host binds each grant to the requesting web origin and target while keeping transport separate from Nostr signing, identity, and service authorization. The proposal also requires explicit consent and scoped permissions, but its address forms and browser contract remain draft behavior.

### Marmot clarifies KeyPackage relay discovery

[Marmot](/en/topics/marmot/) carries MLS group state over Nostr events. The open [KeyPackage relay-discovery clarification](https://github.com/marmot-protocol/marmot/pull/422) documents the current sequence: publish kind `10002` relay metadata, fetch the recipient's kind `30443` KeyPackage from write-capable or unmarked destinations, then use kind `10050` separately to find the recipient's Welcome inbox. It also states that read-only NIP-65 entries are not KeyPackage destinations and that the removed kind `10051` list is no longer a discovery step. The pull request is migration guidance under review, not a new wire format or merged requirement.

### Marmot proposes encrypted group reports and shared moderation

The open [Marmot moderation specification](https://github.com/marmot-protocol/marmot/pull/423) proposes unsigned inner events carried by the protocol's existing encrypted group transport. Kind `1984` would report a specific message revision, kind `1985` would let administrators dismiss referenced reports without removing the content, and kind `4891` would let an authenticated administrator remove a message and its revisions. The proposal also defines deduplication, shared review visibility, ordering, retention, and authority rules, while keeping author deletion on kind `5` and host-application interfaces outside the wire contract.

### NWC adds payment lookup and BOLT12 records

[Nostr Wallet Connect](/en/topics/nip-47/) lets applications control a wallet through encrypted requests and responses over Nostr. Covered previously as an open proposal, its payment-lookup work has now merged into the repository. The merged [`lookup_payment` and BOLT12 specification](https://github.com/nostr-wallet-connect/nwc/pull/5) defines payment lookup by transaction ID, invoice, payment hash, or payment-type-specific selectors, and adds draft, optional BOLT12 payment records and states. Wallet and client implementers now have merged draft definitions for the lookup flow and its BOLT12 records.

### NWC adds client-initiated connections

The merged [client-initiated connection flow](https://github.com/nostr-wallet-connect/nwc/pull/3) lets a client generate the connection secret, direct the user through HTTP confirmation or Nostr authorization, negotiate required and optional permissions, and receive the approved connection details. The change gives NWC clients and wallets a repository-hosted draft definition for creating a connection from the client side.

writer_model: preferred=gemini-3.1-pro, actual=openai-codex/gpt-5.6-sol, receipt=data/newsletter_workspace/writer_receipt_2026-09-16.json

GATE: PENDING REVIEW
