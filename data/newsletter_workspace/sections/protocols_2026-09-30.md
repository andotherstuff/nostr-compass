## Protocol and Spec Work

### NIP-39 extends identity proofs to Bluesky and Discord

[NIP-39](/en/topics/nip-39/) lets a Nostr account point to proof that it controls an identity on another platform. A [change merged September 27](https://github.com/nostr-protocol/nips/pull/2486) gives new proofs one recommended sentence and tells verifiers to accept older proofs that contain the account's npub, even when their wording differs. It also documents Bluesky posts and Discord messages as proof locations. A Discord claim can only be checked by someone who can read the server where its message was posted.

### NIP-86 adds invite-code management for relay administrators

Compass described in the July 8 issue the [NIP-86 invitation proposal](https://github.com/nostr-protocol/nips/pull/2408) while it was open; it has now merged. [NIP-86](/en/topics/nip-86/) defines a standard relay-management API, and [NIP-43](/en/topics/nip-43/) defines how restricted relays announce membership and process admission requests. The September 24 merge adds `listclaims`, `createclaim`, and `deleteclaim` so an administrator can list, issue, and revoke invite codes accepted by a relay. That gives operators a management path for invitations that may grant a member a role after they join; it does not require every relay to support the methods.

A correction to last week's [NIP-86 coverage](/en/newsletters/2026-09-23-newsletter/#nip-86-adds-clear-and-list-methods-for-relay-management): the [merged specification](https://github.com/nostr-protocol/nips/blob/5b9920982ae1f4061328c1b09a90360da28d13c8/86.md) added `unallowevent`, `unbanevent`, `listallowedevents`, and `listdisallowedkinds`. The earlier item listed names from an outdated proposal description. The first two methods reverse an event-level allow or ban decision; the others inspect allowed events and disallowed kinds.

### NIP-51 moves favorite follow sets to an unused event kind

[NIP-51](/en/topics/nip-51/) defines public and private lists, including a list of a user's favorite follow sets. Compass described the [kind-collision proposal](https://github.com/nostr-protocol/nips/pull/2417) in the July 22 issue; it has now merged. The September 27 correction assigns that favorites list kind `10021` because the earlier number was already in use. Its `a` tags still point to kind `30000` follow sets. The change resolves a number collision in the specification; it does not create a new way to follow people.

### NIP-51 proposes hidden replies for each thread

An [open NIP-51 proposal](https://github.com/nostr-protocol/nips/pull/2489) would let a thread's author publish a public hidden-replies set that cooperating clients display behind a toggle. It uses one addressable kind-30027 event per thread, with the root ID as its `d` tag and `e` tags naming replies; only a set signed by the root's author applies. Listing the root asks clients to hide other authors' replies and stop offering a reply composer, while replies can still be published on relays. The per-thread format limits editing collisions to the same conversation. The author reports an implementation in Nostrich, but public-source inspection did not establish it; the proposal remains unmerged, with its set format still under discussion.


### NIP-DB proposes verified domain names for key-addressed services

The [open NIP-DB proposal](https://github.com/nostr-protocol/nips/pull/2487), submitted September 28, describes Nostr events that bind an ordinary Internet domain to the key serving it over a key-addressed network such as [FIPS](/en/topics/fips/), an encrypted mesh that addresses nodes by Nostr public key. A domain owner can establish the binding with a DNS TXT record or a DNSSEC proof carried with the claim; clients would pin a verified result for later offline use. The proposal explicitly bars resolution through an unverified claim, since anyone can claim someone else's domain in a Nostr event. [fips-pub-domains](https://github.com/fr34aky/fips-pub-domains) is the author's reference implementation, but the event-kind numbers and some overlay-specific wording are still under review. Its reported end-to-end tests are the author's evidence, not a claim that the proposal is an accepted NIP.

### A private-feed draft explores encrypted groups of recipients

A [new multi-recipient envelope proposal](https://github.com/nostr-protocol/nips/pull/2488), opened September 29, sketches private notes, replies, and connections whose intended recipients can find an event without exposing their ordinary public keys in its visible tags. It proposes opaque pairwise alias tags derived from shared secrets and provisional event kinds, including a way to wrap another Nostr event for hundreds of readers. That could give small private feeds a more direct retrieval path than sending a separate message to every member.

The [proposal's author](https://github.com/nostr-protocol/nips/pull/2488) explicitly calls this a work in progress. The draft has no demonstrated implementation or security review, and its kind assignments and byte-level signing rules remain open.

### A Blossom proposal lets other people announce mirrored media

An [open NIP proposal](https://github.com/nostr-protocol/nips/pull/2478) describes a way for someone who mirrors another author's Blossom blob to announce that copy through Nostr. A client could then look for the copy if the original server loses the blob. Discussion has also raised checking the mirror's current BUD-03 server list when an announced server hint has gone stale. This is a proposed discovery path, not a guarantee that clients or archival relays already provide fallback storage.

### Road-event reports seek a shared Nostr format

The [open Road Event Reports proposal](https://github.com/nostr-protocol/nips/pull/2479) describes reports and confirmations for potholes, closures, cameras, and other road conditions. It uses location tags and [NIP-40](/en/topics/nip-40/)'s expiration timestamp, which tells relays when to stop serving an event, so a report need not remain current indefinitely. The author based revisions on a sample of events recovered from public relays and on the existing [Roadstr clients](https://github.com/jooray/roadstr) for reporting road conditions, but the draft still leaves a compact-encoding question open, and the proposed NIP number has not been adopted.

### Marmot revisits multi-device coordination

[Marmot's multi-device redesign](https://github.com/marmot-protocol/marmot/pull/427) replaces an unimplemented External Commit draft with a non-normative walkthrough for early feedback. The new direction explores an existing device approving a new one, bringing it into conversations and later removing devices, while keeping open questions visible. IDs reserved by the removed draft are freed because no implementation adopted them. The ideas document allocates no new IDs or wire formats and is not an implemented multi-device feature.
