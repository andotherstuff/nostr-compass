## NIP Updates and Protocol Spec Work

### Nostr event formats and discovery

[NIP PR #2430](https://github.com/nostr-protocol/nips/pull/2430) proposes sticker packs as addressable kind `30031` definitions and a user's installed packs as replaceable kind `10031`. Each sticker tag carries a shortcode, SHA-256 hash, and MIME type; the image remains on a [NIP-B7](https://github.com/nostr-protocol/nips/blob/master/B7.md) (Blossom blob storage) server. The open draft therefore standardizes pack identity and installation without placing image bytes in events.

[NIP PR #2429](https://github.com/nostr-protocol/nips/pull/2429) proposes kind `31436` addressable Gopher documents. Each event holds one UTF-8 text or menu node, and signed nodes under one pubkey form a gopherhole that any relay-backed RFC 1436 bridge can serve. The open proposal uses ordinary addressable-event storage rather than binding the publication to one Gopher hostname.

[NIP PR #2428](https://github.com/nostr-protocol/nips/pull/2428) proposes epoch-ticketed private groups. A group rotates membership credentials between epochs, and clients present the ticket for the current epoch to participate. The draft targets private chat without asking a relay to treat a permanent bearer token as lifetime membership.

[NIP PR #2424](https://github.com/nostr-protocol/nips/pull/2424) proposes replaceable kind `10045` key-set declarations. A key lists other keys controlled by the same person, but clients accept a link only when both keys name each other. That mutual rule prevents one signer from attaching an unrelated identity unilaterally and lets verified links form a mergeable identity set.

[NIP PR #2309](https://github.com/nostr-protocol/nips/pull/2309) proposes ephemeral kind `20411` private-location events. Public `p` tags identify recipients, while `content` maps each pubkey to its own [NIP-44](/en/topics/nip-44/) (versioned encrypted payload) ciphertext containing a geohash, timestamp, and optional accuracy. A `ttl` tag tells clients when to discard the update; recipient lists and timing remain visible to relays.

[NIP PR #2257](https://github.com/nostr-protocol/nips/pull/2257) adds self-described relay attributes to [NIP-11](/en/topics/nip-11/) (relay information documents) and [NIP-66](/en/topics/nip-66/) (relay discovery and monitoring). Operators publish structured capabilities and monitors repeat the observations, giving clients a discovery filter beyond names and free-form descriptions. The proposal remains open, so clients must treat attributes as claims rather than guarantees.

[NIP PR #2425](https://github.com/nostr-protocol/nips/pull/2425) merged a URI clarification into [NIP-B0](/en/topics/nip-b0/) (addressable web bookmarks). It distinguishes omitted HTTPS prefixes from explicit URI schemes when a bookmark stores its target in the `d` tag, preventing clients from reconstructing an ambiguous destination.

### Payments and wallet connections

[NIP PR #2421](https://github.com/nostr-protocol/nips/pull/2421) proposes BOLT12 offers alongside [NIP-57](/en/topics/nip-57/) (Lightning zap receipts). It binds the payer proof for a settled offer payment to a signed zap intent, allowing clients to verify and total payments without depending on the recipient's LNURL callback to publish a receipt.

[NIP PR #2419](https://github.com/nostr-protocol/nips/pull/2419) merged a smaller [NIP-47](/en/topics/nip-47/) (Nostr Wallet Connect) core. Connection URIs, encrypted relay transport, capability discovery, encryption negotiation, and common methods stay in the NIP; notifications, hold invoices, keysend, transaction history, metadata, and deep-link pairing move to a dedicated extension repository. Existing connections remain compatible while wallets can implement optional contracts independently.

[NWC PR #2](https://github.com/nostr-wallet-connect/nwc/pull/2) merged BIP-321 payment methods into that extension repository. BIP-321 provides a common Bitcoin payment URI that can carry different rails, so NWC callers can request or send a payment without adding a new core RPC for each underlying instruction type.

### Napplet host capabilities

[NAP PR #95](https://github.com/napplet/naps/pull/95) proposes catalog discovery for Nostr-distributed sandbox applications. A napplet asks its host which applications and capabilities are available, and the host returns policy-filtered metadata instead of exposing its full local environment. The contract supports launch decisions without granting execution authority during discovery.

[NAP PR #88](https://github.com/napplet/naps/pull/88) proposes a virtual filesystem owned by the host shell. Napplets operate on scoped handles rather than arbitrary paths, while the shell controls consent, quotas, persistence, revocation, and cleanup. This keeps host files and credentials outside an untrusted napplet's direct browser authority.

[NAP PR #94](https://github.com/napplet/naps/pull/94) proposes shell-mediated microphone capture. The host displays consent, owns stop and discard controls, enforces finite time and byte limits, and returns immutable `Blob` artifacts after deterministic stop, cancellation, device-loss, or revocation handling. Capture IDs are bound to the authenticated napplet endpoint generation so a sibling instance cannot inherit authority.

[NAP PR #33](https://github.com/napplet/naps/pull/33) proposes shell-mediated file and blob uploads. A napplet supplies bytes and intent; the host selects a NIP-96 or Blossom rail, signs authorization, reports progress, and returns URLs, hashes, MIME data, and ready-to-attach [NIP-94](/en/topics/nip-94/) (file metadata) tags. Storage credentials and HTTP authority never enter the napplet.

### Marmot encrypted groups

[Marmot PR #410](https://github.com/marmot-protocol/marmot/pull/410) merged convergence and deferred-input rules. Clients distinguish an object that lacks a current epoch dependency from stale or invalid input, keep it eligible for refetch after resource refusal, and retry when another commit changes the decryption context. A domain-separated state commitment gives conformance tests a shared convergence oracle without adding a production wire field.

### Concord community planes

[Concord PR #14](https://github.com/concord-protocol/concord/pull/14) merged CORD-08 disappearing messages. One community metadata value sets the lifetime; chat rumors and encrypted wraps carry a [NIP-40](/en/topics/nip-40/) (event expiration) tag, while deletion events and the kind `1740` timer notice are exempt. The signed timer travels with community state, though relay deletion remains a retention request rather than a cryptographic erasure guarantee.

[Concord PR #13](https://github.com/concord-protocol/concord/pull/13) merged rotation-proof pinning into CORD-04. Each channel has one replace-entire pin list on the control plane; entries carry the original signed seal plus per-message NIP-44 expansion keys, allowing a new member to verify the author and plaintext without receiving an old epoch key. Private lists can remain sealed to a channel epoch, caps bound list size, and author deletions remove pins without forking the control-plane chain.

GATE: PASS
