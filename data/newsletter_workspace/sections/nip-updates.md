## Protocol and Spec Work

### NIPs: NIP-34 hosting boundary, group migration, and three live drafts

Two specification changes merged this week. [NIP-34 commit 6d2979b](https://github.com/nostr-protocol/nips/commit/6d2979b3f503a8539c983efbcdcf901bbcf9ed23) removes GRASP hosting instructions from the `kind:1618` pull-request description, leaving hosting and fallback behavior outside the event contract. [NIP-29 commit db5fe3d](https://github.com/nostr-protocol/nips/commit/db5fe3de8c5d1443b634c9bbf66ecb004f337057) defines how relay-group metadata migrates to another relay and how clients distinguish a valid move from a fork that continues independently.

[PR #2424](https://github.com/nostr-protocol/nips/pull/2424) proposes mutual `kind:10045` key-set declarations, so one identity cannot attach another key without a reciprocal event. [PR #2421](https://github.com/nostr-protocol/nips/pull/2421) proposes BOLT12 zap intents and payer proofs that clients can validate against the target, amount, offer, and settled payment without depending on a recipient-operated receipt server.

[PR #2425](https://github.com/nostr-protocol/nips/pull/2425) would let NIP-B0 bookmarks retain non-HTTP schemes such as `nostr:` alongside web URLs. That keeps native Nostr identifiers, payment requests, and other application schemes intact inside the same private or public bookmark lists that already carry web addresses.

### Mill implements a draft for cloud-account key backup

Mill [announced](https://primal.net/e/6362d9b00662fa64200530f8a29ae547521bac0a1e3c9379ef9086eac7d2030b) an implemented [cloud-account key-backup draft](https://github.com/0ceanSlim/nostr-mill/blob/main/docs/nip-cloud-key-backup.md) that combines a Google OIDC account identifier with a high-entropy passphrase to derive a disposable backup key. Its [reference implementation](https://github.com/0ceanSlim/nostr-mill/blob/main/src/nipbackup.js) encrypts the user's real key as a [NIP-49 (Private Key Encryption)](/en/topics/nip-49/) `ncryptsec`, then stores it in a provisional parameterized-replaceable kind `30049` event on configured relays. The project [merged the flow to main](https://github.com/0ceanSlim/nostr-mill/commit/eeb4b9114d02114b703a6823ad36ca8063b224da), but no post-v1.0.0 release includes it and the feature stays disabled unless an operator supplies dedicated `backupRelays`. The draft pins a versioned relay set whose concrete purpose-run endpoints remain provisional and warns that published ciphertext remains available for offline passphrase guessing. The design depends on a high-entropy passphrase, and readers should treat it as an implemented experiment.

### BUDs: Blossom servers may identify unknown uploads from their bytes

[BUD-02 PR #110](https://github.com/hzrd149/blossom/pull/110) now recommends server-side MIME detection when an uploader omits `Content-Type` or sends `application/octet-stream`. A Blossom server would inspect the first bytes with a maintained file-type library, preserve a specific client-supplied type, and fall back to the generic binary type when detection fails. That keeps images, audio, video, and agent-produced files renderable without making byte sniffing mandatory for every upload.

### NAPs: conventions replace numbered tracks as capture and filesystem contracts develop

[PR #87](https://github.com/napplet/naps/pull/87) removes the numbered cross-napplet protocol track and keeps runtime capabilities under named contracts while application messages converge on `napplet:<archetype>/<intent>` convention URIs. The merged [topic-identity change](https://github.com/napplet/naps/pull/89) separates a stable, queryless convention path from per-message payload data, and [PR #90](https://github.com/napplet/naps/pull/90) applies that transposition rule to discovery and handler metadata.

Two NAP drafts extend the trusted shell boundary. [NAP-CAPTURE PR #94](https://github.com/napplet/naps/pull/94) keeps microphone consent, platform permission, limits, retention, and teardown in the runtime while returning a bounded media artifact to a sandboxed napplet. [NAP-FS PR #88](https://github.com/napplet/naps/pull/88) is the parallel virtual-filesystem proposal, with policy-bound handles instead of unrestricted host paths.

### Marmot: the specification defines a terminal group state

[Marmot PR #409](https://github.com/marmot-protocol/marmot/pull/409) adds an authenticated, irreversible `Disbanded` state because MLS itself has no group-deletion operation. An authorized admin commit moves a group out of `Active`, blocks old branches, messages, and Welcomes from reviving it, and gives existing groups an explicit compatibility path before they can disband. The preceding [specification issue sweep](https://github.com/marmot-protocol/marmot/pull/408) also reconciled group-state authority, convergence, key packages, acknowledgements, media rules, registry language, and 200 tracked specification issues.

### Gamma Markets: no public specification changes landed

The [Gamma Markets specification repository](https://github.com/GammaMarkets/market-spec) recorded no public commits or pull-request activity from July 21 through July 28. Its published order, settlement, and market-data documents remain the current baseline; this no-change entry keeps Gamma visible in the weekly specification sweep.

### Concord: read and write capabilities may split inside one plane

[Concord PR #12](https://github.com/concord-protocol/concord/pull/12) remains an open draft for planes whose readers should not all be writers. It moves the Control Plane toward separate read and write stream capabilities and sketches restricted-write channels, invites, and rekey scopes. The write key is a spam gate in the draft, while signed inner actors and roster checks continue to carry authority.

### NWC: one wallet method can choose between BOLT11 and BOLT12

[NWC PR #2](https://github.com/nostr-wallet-connect/nwc/pull/2) proposes optional `pay` and `receive` methods for BIP-321 payment URIs. A wallet service can advertise support, choose one compatible BOLT11 invoice or BOLT12 offer from a URI, reject a mismatched Bitcoin network before payment, and report which instruction type it used. The proposal stays outside the NWC core so wallets without BIP-321 or BOLT12 support do not have to implement it.

GATE: PASS (prepublish refresh: five review gates PASS at 2026-07-29T14:00:03Z; 113/113 external URLs 200, claims/style/topics/continuity verified)
