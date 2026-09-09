## Tagged Releases

### Vector 0.4.4 makes encrypted-community recovery safer

[Vector 0.4.4](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4) shipped August 31 with community recovery, key-rotation, moderation, and reply-routing fixes. Refounding closes a raided community to the invitation path used by attackers; replacement membership supersedes stale local state; and one unreachable member no longer freezes the roster. Empty rotations are rejected, promotions preserve online members, and operations refuse to run when required members cannot be reached.

The [release](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4) also persists moderator deletions and bans, re-encrypts the guest book after a password change, binds notification replies to their conversation after restart, and uses only verified multiplayer paths. These are recovery controls, not revocation of keys already obtained.

### Primal Android 3.5.27 checks signer and wallet identity

[Primal Android 3.5.27](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.27) shipped September 3 after [the signer identity check](https://github.com/PrimalHQ/primal-android-app/pull/1108) and [wallet-request authentication](https://github.com/PrimalHQ/primal-android-app/pull/1105) merged August 31. Local signing rejects a request whose identity does not match the held account, and incoming [NIP-47](/en/topics/nip-47/) requests are authenticated before processing. Zap-poll routing also sends votes to the poll author when the poll appears in a reply.

### GRAIN 0.8.0-rc2 closes an acknowledged-but-not-stored path

[GRAIN 0.8.0-rc2](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc2) shipped September 7 after a storage failure allowed `OK` before its asynchronous LMDB database writer noticed full storage capacity. The relay now warns at 80 and 95 percent, refuses new events at 97 percent while leaving deletion room, and reports post-acceptance writer failures. Retention walks oldest-first, teardown handles late messages, and invalid filters no longer discard valid siblings.

The [release](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc2) also corroborates kind `10166` monitor announcements and kind `30166` relay reports, evicts stale reports, keeps configured relays as fallback, and reports live limits and authentication in [NIP-11](/en/topics/nip-11/) instead of static zeros.

### LibreNostr 0.5.0–0.5.2 makes Tor routing fail closed

[LibreNostr 0.5.0](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) shipped September 7 with an Orbot mode routing relays, zaps, uploads, media, playback, and previews through one SOCKS port, plus a repair for a zap-sheet crash. If Orbot or the proxy is unavailable, connections stop instead of leaking onto a direct route. [Version 0.5.1](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.1) stops slow [NIP-50](/en/topics/nip-50/) searches delaying local results; [0.5.2](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.2) replaces recursive thread layout and repairs thread ordering.

The [fail-closed behavior](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) applies to every network surface listed by the release, and a restart is required because those clients are long lived. The patch releases preserve that choice while limiting unrelated search, stack-depth, and layout failures.

### SkateSpots adds an on-device relay path

The signed [September 8 Zapstore release](https://zapstore.dev/apps/org.skatespots.app) adds an optional Citrine relay to SkateSpots. Spots, crews, messages, and map data can load locally; posts queue offline; and the phone keeps a local copy. Existing stash and message content stays end-to-end encrypted. Payment checks require invoice amounts and provider-issued zap receipts before granting access or counting contributions.

The [local relay](https://zapstore.dev/apps/org.skatespots.app) is a storage and continuity option, not a replacement for every remote relay. It lets a skater keep working through a disconnected stretch and then reconcile signed activity later, while the payment changes stop a self-authored receipt from becoming proof of settlement.

### Whistle 1.8.15 repairs encrypted-group lifecycle recovery

[Whistle 1.8.15](https://github.com/sjmcnamara/whistle/releases/tag/v1.8.15) shipped September 3 after an Android lifecycle repair stopped route-level state holders from destroying application-wide relay subscriptions and location updates. Its release notes also describe refreshed connection state after lock or doze and a recovered 501-event backlog in the observed case.

The [bug](https://github.com/sjmcnamara/whistle/releases/tag/v1.8.15) tied ownership of a long-lived service to a short-lived screen. Keeping the activity-scoped instance alive and checking the socket before a one-shot read makes ordinary Android navigation and background suspension less likely to look like an empty group.

### TWENTY ONE Companion 1.12.0 separates encrypted DMs from legacy chat

[TWENTY ONE Companion 1.12.0](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.12.0) shipped September 5 with [NIP-17](/en/topics/nip-17/) gift-wrapped DMs. The encrypted inbox is separate from older space chat, which remains distinct because those messages were never encrypted and cannot be migrated. PDFs and videos are supported subject to relay policy, and personal hides sync without becoming moderator bans.

The [visible separation](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.12.0) is part of the security model. Calling the old history a secure inbox would misrepresent its provenance, while silently migrating it would suggest encryption that did not exist when it was written.

### ZapStore 1.1.2 validates event ids and certificate rotation

[ZapStore 1.1.2](https://github.com/zapstore/zapstore/releases/tag/1.1.2) shipped September 4 with NIP-01 event-id validation: the client recomputes an incoming event's id and rejects mismatches before using it. The release also identifies packages installed outside ZapStore. On the server, [certificate-hash retention](https://github.com/zapstore/relay/pull/8) preserves repeated `apk_certificate_hash` tags so Android signing-key rotation can retain an approved lineage.

The [event-id check](https://github.com/zapstore/zapstore/releases/tag/1.1.2) prevents a relay or cache from changing tags or content while keeping the old id. The installer-source indicator supplies separate provenance when an Android package with the same application id came from another channel.

### Amber 6.6.1 keeps signer responses attributable

[Amber 6.6.1](https://github.com/greenart7c3/Amber/releases/tag/v6.6.1) shipped September 4 after permission parsing was fixed to tolerate a missing optional `kind`, and rejected signing requests began returning their original request id. Calling applications can match a rejection to the submitted operation. The release also updates remote-signer defaults and adds an indexer relay.

Together these [fixes](https://github.com/greenart7c3/Amber/releases/tag/v6.6.1) preserve attribution in both directions: a permission record remains usable when an optional field is absent, and a refusal remains tied to the request that caused it. The relay-default changes affect discovery, but they do not replace the signer's local authorization decision.

writer_model: claude-opus-5 (bounded first-party fallback candidate; wrapper run `7dee2ec3-0440-4980-a0a5-9dd9ce854a4c`)

GATE: PENDING REVIEW
