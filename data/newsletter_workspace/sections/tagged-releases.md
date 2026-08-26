## Releases

### Nostr Java v2.0.8: subscription isolation and portable NIP-44

A gift-wrap query against a relay holding five events was returning zero, two, or six events at random, because [Nostr Java](https://github.com/tcheeric/nostr-java), a Java library for talking to relays and encrypting Nostr payloads, delivered every inbound frame to every listener on the connection. [Version 2.0.8](https://github.com/tcheeric/nostr-java/releases/tag/v2.0.8) routes `EVENT`, `EOSE`, and `CLOSED` to the subscription those frames name, so one query's end-of-stored-events signal can no longer close another. Connection-scoped frames such as `NOTICE`, `OK`, and `AUTH` still reach every listener.

[NIP-44](/en/topics/nip-44/) (payload encryption) in the same [release](https://github.com/tcheeric/nostr-java/releases/tag/v2.0.8) no longer needs a JCE provider registered in the process. Encryption used to work only after a key had been generated in that JVM, which registered BouncyCastle as a side effect, and it failed on Android, where adding a provider named "BC" is a no-op. Both cipher paths now use BouncyCastle's lightweight ChaCha20 engine, and key generation no longer mutates process-wide JCE state. Callers that relied on the library to register the provider must register it themselves. The [NIP-44 JCE-provider dependence](https://github.com/tcheeric/nostr-java/issues/537) is the issue this closes.

### NoorNote v1.3.6: profile statuses and classified listings

[NoorNote](https://github.com/77elements/noornote) is a Nostr client for desktop, web, and Android. A week after [1.3.4 added encrypted community joins](/en/newsletters/2026-08-19-newsletter/#noornote-134-joining-encrypted-communities-from-an-invite-link), [version 1.3.6](https://github.com/77elements/noornote/releases/tag/v1.3.6) shows [NIP-38](/en/topics/nip-38/) (user statuses) under a profile's [NIP-05](/en/topics/nip-05/) (domain-verified) name: the optionally expiring kind `30315` addressable events that carry a one-line general or music status. Clicking that line sets the viewer's own status.

[Classified listings](https://github.com/77elements/noornote/releases/tag/v1.3.6) from [NIP-99](/en/topics/nip-99/) (kind `30402` marketplace offers) now render throughout the app, so the marketplace addon is needed only to buy and sell. Private petname notes on profiles also show in warning orange, with a filled note icon and an orange avatar ring.

### nostrord v2.9.0: relay-scoped group state and media

Leaving a [NIP-29](/en/topics/nip-29/) (relay-managed groups) group on one host used to suppress the same group id on every other relay, because [nostrord](https://github.com/nostrord/nostrord), a cross-platform client for relay-hosted communities, keyed its leave and delete markers by bare id. [Leave and delete markers scoped per relay](https://github.com/nostrord/nostrord/pull/253) keep those suppressions on the host that produced them, so a group that shares an id across two relays is no longer left or dropped as a pair. A join that the relay rejects as already a member now counts as success and clears the local marker, which had been an absorbing state: the self-heal cleared one slot while cold start restored the other.

[Version 2.9.0](https://github.com/nostrord/nostrord/releases/tag/v2.9.0) also renders [markdown image embeds](https://github.com/nostrord/nostrord/pull/254) that other clients write as `![alt](url)`, instead of showing the markdown punctuation around an already-detected URL. Direct messages pick up [NIP-17](/en/topics/nip-17/) (gift-wrapped private DMs) [kind `15` file rumors](https://github.com/nostrord/nostrord/pull/275), so an encrypted attachment sent from Jumble is downloaded, decrypted, and shown, and outbound attachments are encrypted before upload. This tag now ships the [NIP-4e encryption-key work covered last week](/en/newsletters/2026-08-19-newsletter/#nostrord-implements-an-unmerged-encryption-key-proposal). The proposal remains unmerged, and nostrord says its implementation follows deployed Jumble behavior where that behavior differs from the draft.

GATE: PENDING REVIEW
