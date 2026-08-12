## Protocol and Spec Work

### NIPs

[NIPs PR #2435](https://github.com/nostr-protocol/nips/pull/2435) is an open amendment to NIP-34, which standardizes git repository collaboration through Nostr events. It adds an optional `b` tag to a pull-request event so the author can name a target branch other than the repository's default. The proposal matches support already implemented in ngit and GitWorkshop, but has not entered the specification.

[NIPs PR #2434](https://github.com/nostr-protocol/nips/pull/2434) is an open proposal for post-quantum identity keys. It derives post-quantum encryption and signing keys beside the existing secp256k1 key from a NIP-06 mnemonic key-derivation seed, then binds the public keys to the Nostr identity with a kind `10203` attestation. The draft limits its claim to protecting the confidentiality of earlier messages if secp256k1 is later broken; it does not replace today's event signatures.

[NIPs PR #2431](https://github.com/nostr-protocol/nips/pull/2431) is an open NIP-07 amendment for browser signers. A client could attach the public key it expects to signing or encryption requests, requiring the signer to use that account or reject the call. This would keep a page from silently continuing under a different identity after the user switches accounts in the signer.

[NIPs PR #1813](https://github.com/nostr-protocol/nips/pull/1813) remains an open double-ratchet proposal after substantive work during the window. It specifies forward-secret encrypted conversations whose keys advance with messages, with an implementation already available in the nostr-double-ratchet library and Iris. It is still a draft, not a merged NIP.

[NIPs PR #2433](https://github.com/nostr-protocol/nips/pull/2433) opened and closed without merging during the window. It proposed clarifying NIP-42 relay errors so `auth-required` would mean another authentication could change the result, while `restricted` would mean it could not. The distinction addressed connections authenticated for one key but still missing authorization for another; the closed status means the wording did not enter the specification.

[NIPs PR #2378](https://github.com/nostr-protocol/nips/pull/2378), which was covered previously while still proposed, has now closed without merging. Its proposed agent passports, discovery, task, marketplace, invoice, and connection events therefore remain outside the NIP set.

[NIPs commit 656cecc](https://github.com/nostr-protocol/nips/commit/656cecc7c0a815b6a2b218d3b5d6f078b3f4dbab) merged a documentation-only correction to NIP-29. It adds a `previous` tag to the group metadata example, showing how a replacement event can identify the event it supersedes. This clarifies an example and does not introduce a new protocol feature.

### Concord and CORDs

[CORD PR #18](https://github.com/concord-protocol/concord/pull/18) would shard encrypted Community Lists across kind `33302` events, remove the 50-membership limit, and prune retired entries to stay within relay limits. Two other open proposals add [private mention locators](https://github.com/concord-protocol/concord/pull/16) and a [pause signal](https://github.com/concord-protocol/concord/pull/17) that suspends chat without discarding messages.

[CORD-02 PR #15](https://github.com/concord-protocol/concord/pull/15) merged on August 6 and restricts writes to a community's control plane. Owners and staff hold a new `control_root` signing secret, while all members retain the derived public key and read key needed to verify and decrypt moderation state. The write key is a spam barrier, not a substitute for the inner actor signatures and roster checks that establish authority.

[CORD PR #12](https://github.com/concord-protocol/concord/pull/12), covered previously as an open draft, has now closed without merging. Its control-plane portion was superseded by the narrower merged CORD-02 amendment above, while restricted-write channels and the other draft material did not enter the specification.

GATE: PASS (final-delta claims, continuity, 73/73 live links, prose/style, topic-backlink, and production-build gates passed at 2026-08-12T15:45Z)
