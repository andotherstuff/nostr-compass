## Unreleased Changes

### NMP ties relay admission to declarations and broadens group queries

NMP [PR #1254](https://github.com/pablof7z/nmp/pull/1254) makes relay admission follow the owner of the declaration that authorizes it, keeping the permission decision attached to signed Nostr state. [PR #1255](https://github.com/pablof7z/nmp/pull/1255) generalizes [NIP-29](/en/topics/nip-29/) group queries instead of assuming one narrow lookup shape. Both changes are merged but have not yet appeared in a tagged release.

### Mosaico derives managed-group identity from relay records

Mosaico [PR #758](https://github.com/pablof7z/mosaico/pull/758) derives a managed group's identity from the relay that hosts its authoritative records. [PR #757](https://github.com/pablof7z/mosaico/pull/757) observes the group's published record when resolving administration state. This keeps two similarly named groups on different relays distinct and gives clients a relay-backed source for their management metadata.

### Divine isolates slow relays during multi-relay queries

Divine [PR #6673](https://github.com/divinevideo/divine-mobile/pull/6673) gives each relay query its own timeout instead of letting one stalled connection consume the timeout budget for an entire request. Results from responsive relays can therefore arrive while the slow endpoint is abandoned independently. The change improves retrieval without treating one relay as authoritative for the combined result.

### rust-nostr hardens encryption, hashes, and reconciliation

rust-nostr [PR #1421](https://github.com/rust-nostr/nostr/pull/1421) reduces allocation in its [NIP-44](/en/topics/nip-44/) encryption path, while [PR #1423](https://github.com/rust-nostr/nostr/pull/1423) introduces typed hashes that make incompatible digest values harder to mix accidentally. [Commit 21e31c2](https://github.com/rust-nostr/nostr/commit/21e31c28da3dfadedb5fa6e58c712647f16e5f69) prevents a malformed [NIP-77](/en/topics/nip-77/) Negentropy message from disconnecting the local relay. The merged work tightens both encrypted payload handling and set-reconciliation failure behavior before the next release.

### Zeus serializes NWC payments before charging spending budgets

Zeus [PR #4305](https://github.com/ZeusLN/zeus/pull/4305) counts pending payments against a [NIP-47](/en/topics/nip-47/) Nostr Wallet Connect budget instead of waiting for settlement. [PR #4303](https://github.com/ZeusLN/zeus/pull/4303) serializes payment handling so concurrent requests cannot race through the same authorization limit. The merged pair closes a budget-enforcement gap on the wallet's Nostr control surface.

### Nostr Components shares one relay connection attempt

Nostr Components [PR #105](https://github.com/saiy2k/nostr-components/pull/105) lets components mounted at the same time share an in-flight relay connection attempt. Each consumer still receives the resulting connection, but concurrent mounts no longer open duplicate sockets while the first handshake is pending. The change reduces avoidable relay load in applications assembled from several independent components.

GATE: PASS
