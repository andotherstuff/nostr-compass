## NIP Updates and Protocol Spec Work

### Nostr event formats and discovery

[NIP PR #2430](https://github.com/nostr-protocol/nips/pull/2430) proposes sticker packs as addressable kind `30031` definitions and a user's installed packs as replaceable kind `10031`. Each sticker tag carries a shortcode, SHA-256 hash, and MIME type; the image remains on a [NIP-B7](https://github.com/nostr-protocol/nips/blob/master/B7.md) (Blossom blob storage) server. The open draft therefore standardizes pack identity and installation without placing image bytes in events.

[NIP PR #2429](https://github.com/nostr-protocol/nips/pull/2429) proposes kind `31436` addressable Gopher documents. Each event holds one UTF-8 text or menu node, and signed nodes under one pubkey form a gopherhole that any relay-backed RFC 1436 bridge can serve. The open proposal uses ordinary addressable-event storage rather than binding the publication to one Gopher hostname.

[NIP PR #2428](https://github.com/nostr-protocol/nips/pull/2428) proposes epoch-ticketed private groups. A group rotates membership credentials between epochs, and clients present the ticket for the current epoch to participate. The draft targets private chat without asking a relay to treat a permanent bearer token as lifetime membership.

[NIP PR #2425](https://github.com/nostr-protocol/nips/pull/2425), covered as a proposal last week, has now merged a URI clarification into [NIP-B0](/en/topics/nip-b0/) (addressable web bookmarks). It distinguishes omitted HTTPS prefixes from explicit URI schemes when a bookmark stores its target in the `d` tag, preventing clients from reconstructing an ambiguous destination.

### Payments and wallet connections

[NIP PR #2419](https://github.com/nostr-protocol/nips/pull/2419), covered as a proposal in the July 22 issue, has now merged a smaller [NIP-47](/en/topics/nip-47/) (Nostr Wallet Connect) core. Connection URIs, encrypted relay transport, capability discovery, encryption negotiation, and common methods stay in the NIP; notifications, hold invoices, keysend, transaction history, metadata, and deep-link pairing move to a dedicated extension repository. Existing connections remain compatible while wallets can implement optional contracts independently.

[NWC PR #2](https://github.com/nostr-wallet-connect/nwc/pull/2), covered as a proposal last week, has now merged BIP-321 payment methods into that extension repository. BIP-321 provides a common Bitcoin payment URI that can carry different rails, so NWC callers can request or send a payment without adding a new core RPC for each underlying instruction type.

### Napplet host capabilities

[NAP PR #95](https://github.com/napplet/naps/pull/95) proposes catalog discovery for Nostr-distributed sandbox applications. A napplet asks its host which applications and capabilities are available, and the host returns policy-filtered metadata instead of exposing its full local environment. The contract supports launch decisions without granting execution authority during discovery.

[NAP PR #33](https://github.com/napplet/naps/pull/33) proposes shell-mediated file and blob uploads. A napplet supplies bytes and intent; the host selects a NIP-96 or Blossom rail, signs authorization, reports progress, and returns URLs, hashes, MIME data, and ready-to-attach [NIP-94](/en/topics/nip-94/) (file metadata) tags. Storage credentials and HTTP authority never enter the napplet.

### Marmot encrypted groups

[Marmot PR #410](https://github.com/marmot-protocol/marmot/pull/410) merged convergence and deferred-input rules. Clients distinguish an object that lacks a current epoch dependency from stale or invalid input, keep it eligible for refetch after resource refusal, and retry when another commit changes the decryption context. A domain-separated state commitment gives conformance tests a shared convergence oracle without adding a production wire field.

### Concord community planes

[Concord PR #14](https://github.com/concord-protocol/concord/pull/14) merged CORD-08 disappearing messages. One community metadata value sets the lifetime; chat rumors and encrypted wraps carry a [NIP-40](/en/topics/nip-40/) (event expiration) tag, while deletion events and the kind `1740` timer notice are exempt. The signed timer travels with community state, though relay deletion remains a retention request rather than a cryptographic erasure guarantee.

[Concord PR #13](https://github.com/concord-protocol/concord/pull/13) merged rotation-proof pinning into CORD-04. Each channel has one replace-entire pin list on the control plane; entries carry the original signed seal plus per-message NIP-44 expansion keys, allowing a new member to verify the author and plaintext without receiving an old epoch key. Private lists can remain sealed to a channel epoch, caps bound list size, and author deletions remove pins without forking the control-plane chain.

GATE: PASS
