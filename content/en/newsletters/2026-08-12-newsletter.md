---
title: "Nostr Compass #35"
date: 2026-08-12
publishDate: 2026-08-12
draft: false
type: newsletters
description: "Post-quantum identity tools, stronger encrypted messaging and signing, portable community settings, and protocol work across NIPs and Concord."
---

Welcome back to [Nostr Compass](https://nostrcompass.org), your weekly guide to Nostr.

**This week:** [nostr-wot-extension](https://github.com/nostr-wot/nostr-wot-extension) adds post-quantum keys and opt-in protected messages beside existing Nostr identities. [Divine](https://github.com/divinevideo/divine-mobile) tightens account isolation, private-message validation, and publish confirmation; [MDK](https://github.com/marmot-protocol/mdk) strengthens encrypted-group convergence and recovery; and [Amber](https://github.com/greenart7c3/Amber) makes grouped signing decisions explicit. Releases improve wallet connections, encrypted chat, social discovery, device sync, and remote signing, while protocol work covers identity and encrypted communities. The deep dives explain authenticated deletion requests and decentralized reporting.

## Top Stories

### nostr-wot-extension 0.4.0 adds post-quantum keys beside a Nostr identity

[nostr-wot-extension 0.4.0](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.4.0) is a browser extension for managing Nostr identities and signing. Accounts created from a 24-word seed can now derive ML-KEM-1024 encryption and ML-DSA-87 signing keys alongside their existing Nostr key. A one-click flow publishes a kind `10203` attestation that binds the Nostr public key to both post-quantum public keys and includes an ML-DSA proof of possession. Accounts imported from a 12-word mnemonic, bare `nsec`, remote signer, or read-only key cannot use the derivation flow, and the extension explains that limitation in the account view.

The release also adds opt-in post-quantum direct messages. It combines the ML-KEM shared secret with the existing [NIP-44 encrypted-message conversation key](https://github.com/nostr-protocol/nips/blob/master/44.md) through HKDF, then keeps the normal NIP-59 metadata-hiding gift-wrap layers for relay delivery. Encryption never silently falls back after a recipient opts in, while decryption selects the appropriate path automatically. This protects the new message path against later recovery of a present-day Nostr private key, but it does not replace secp256k1 event signatures; the release explicitly leaves that larger migration for future coordination with relays and clients.

### Divine Mobile 1.0.19 tightens accounts, private messages, and publishing

[Divine Mobile 1.0.19](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.19) is a mobile short-video client that publishes and retrieves videos through Nostr. Its account switcher now builds each signed-in identity around an account-scoped container, and a publishing fix prevents a video from being sent under the wrong account. Relay publication paths now wait for an `OK` response with explicit success semantics, while a relay `CLOSED` frame can terminate its own pending query instead of leaving the request hanging.

[Private-message handling](https://github.com/divinevideo/divine-mobile/pull/6368) rejects unauthenticated rumor fields and unsigned seals, restores four missing-message cases, and routes group conversations from fully followed participants into the inbox. The release also preserves the tags on addressable video events when lists are updated and consumes observed deletion requests so removed videos disappear from local state. Those changes follow the per-relay query timeout work covered last week, but move the focus from retrieval isolation to identity boundaries, message validation, and publish confirmation.

### MDK 0.9.11 hardens Marmot group convergence and recovery

[MDK 0.9.11](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.11) is a Rust development kit for Marmot, an encrypted group-messaging protocol carried over Nostr. The release builds a larger convergence and recovery system around the group state machine: stale convergence passes reopen at the current group tip, inbound capability projections commit atomically, deferred messages receive bounded lifetimes across restarts, and commit-addressed checkpoints help recover an identity's own commit forks. Non-stable sends can be queued and recovered, while an epoch-stall path escalates to backfill and sent messages survive convergence work.

[Storage and host integrations](https://github.com/marmot-protocol/mdk/pull/1201) receive a parallel hardening pass. MDK securely deletes pruned SQLite projections, zeroizes imported private keys, NIP-49 encrypted-key export intermediates, and OpenMLS serialization buffers, and redacts group image keys from debug output. Account import can resume after interruption, iOS and Android private-storage paths are repaired, and hosts can explicitly close storage before suspension. New lightweight roster and local-membership projections reduce what applications must read, while the Hermes connector can deliver several agent-generated images as one Marmot album.

### Nostria 4.1.67 expands encrypted-community administration

[Nostria 4.1.67](https://github.com/nostria-app/nostria/releases/tag/v4.1.67) is a web and desktop social client for Nostr. It builds on the experimental NIP-29 relay-managed groups and Concord encrypted communities introduced in 4.1.53, adding community dissolution, icon and banner administration, encrypted photo uploads with compressed previews, a full reaction picker, and a dual-pane layout that keeps a community open while the user reads notes or articles. The release also adds threaded messaging and a combined hub for public, group, and private chats.

### Amber 6.4.0 makes every grouped signing decision explicit

[Amber 6.4.0](https://github.com/greenart7c3/Amber/releases/tag/v6.4.0) is an Android signer that keeps Nostr private keys separate from the applications requesting signatures. Its redesigned multi-request screen provides Approve and Deny controls for each request and each group, replacing the previous selection-and-confirm flow. Denied requests sent through Amber's relay-mediated bunker interface now receive proper error responses, so the requesting client can distinguish rejection from a stalled signer.

[Amber's tagged source](https://github.com/greenart7c3/Amber/tree/v6.4.0) also adds localized, human-readable labels for 113 more event kinds across every shipped locale. The additions include Concord group events, NIP-51 Git repository bookmarks, and NIP-53 room-presence events, giving users more context about unfamiliar data before they approve a signature. A concurrent-map guard also fixes a relay-subscription crash that could produce a `NegativeArraySizeException`.

### Safebox Acorn separates a portable recovery component from the web app

[Safebox Acorn](https://github.com/trbouma/safebox-acorn) is a standalone Python component and command-line interface for safeguarding user-controlled keys, funds, and records with Nostr-backed state. Extracting Acorn from the broader Safebox web application lets another Python project install the runtime and use its key, Nostr profile, relay, record, Cashu, Lightning, and cryptographic helpers without taking on the web interface. Its current record-protection primitives can generate a fresh 256-bit key, derive one from separately supplied entropy, and encode the exact key as a checksummed 24-word recovery phrase.

The project's [recovery and continuity guide](https://trbouma.github.io/safebox-acorn/recovery-and-continuity/) frames Acorn as the replaceable protocol component inside a household or community Safebox. The design keeps encrypted state available through a local relay and independent replicas so recovery does not depend on one appliance, application, relay, mint, or service provider. The documentation is careful about the present boundary: protected-record encryption remains under design, so applications should not make records depend on the new record-protection key until that profile has been implemented and reviewed.


## Tagged Releases

### Mostro Core 0.14.2 changes the encrypted chat envelope

[Mostro Core](https://github.com/MostroP2P/mostro-core) is the Rust library of shared types and peer-to-peer functions used by the Mostro exchange daemon and its clients. [Version 0.14.2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.2) replaces gift-wrapped chat messages with kind 14 envelopes that use separate conversation-encryption and signing keys derived from the peers' shared secret. The new reader validates the author, signature, recipient, timestamp, and content size, while legacy gift-wrap helpers remain available so clients can read both formats during migration.

### Mostro 0.18.1 starts a Cashu escrow path and hardens the daemon

[Mostro](https://github.com/MostroP2P/mostro) is a peer-to-peer Lightning exchange daemon that coordinates orders through Nostr. [Version 0.18.1](https://github.com/MostroP2P/mostro/releases/tag/v0.18.1) lays the foundation for a Cashu escrow backend, including configuration, database helpers, mint integration, startup wiring, and the first lock action. It can also use prices announced by a trusted node over Nostr and advertises proof-of-work requirements for first contact in its replaceable info event. The release updates its Nostr dependency for a NIP-44 denial-of-service fix, removes private keys from restore-session logs, rejects unauthorized cooperative-cancel messages, hardens LNURL fetches against server-side request forgery and hangs, validates payout invoices, and restores hold-invoice subscriptions after a restart.

### LaWallet NWC 2.3.0 adds Nostr notifications and zap receipts

[LaWallet NWC](https://github.com/lawalletio/lawallet-nwc) is an open-source Lightning Address platform that connects wallets through [Nostr Wallet Connect](/en/topics/nip-47/). [Version 2.3.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.3.0) lets each wallet send received and forwarded notifications as configurable Nostr events, including a recipient `p` tag, selected relays, templated content, and optional [NIP-44](/en/topics/nip-44/) encryption; retries reuse the same signed event ID. It also accepts zap requests and publishes signed [NIP-57](/en/topics/nip-57/) kind 9735 receipts after settlement, while a new address capability view shows whether the resolved address supports NIP-05, NIP-57, and related Lightning Address protocols.

### nostr-double-ratchet TypeScript 0.0.166 binds public invites to session keys

[nostr-double-ratchet](https://github.com/irislib/nostr-double-ratchet) provides TypeScript and Rust primitives for end-to-end encrypted direct and group messaging over Nostr relays. [TypeScript 0.0.166](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.166) requires an invite response to prove ownership of its session key, preventing a reusable public invite from binding one Nostr identity to another party's session. The release also rejects malformed rumor fields and tightens payload validation; existing sessions continue to work, but an updated inviter rejects proofless responses from older invitees.

### cln-nip47 0.2.0 expands and isolates NWC requests

[cln-nip47](https://github.com/daywalker90/cln-nip47) is a Core Lightning plugin that exposes a node to wallets through [Nostr Wallet Connect](/en/topics/nip-47/). [Version 0.2.0](https://github.com/daywalker90/cln-nip47/releases/tag/v0.2.0) adds NWC methods to create, cancel, and settle hold invoices plus a `hold_invoice_accepted` notification, and it advertises the method set that the connected node actually supports. Transaction-list responses now stop at 500 entries and about 128 kB, request events are deduplicated by event ID, and one client's failed notification no longer prevents delivery to other clients. The release also removes the two multi-payment methods that are no longer part of the NWC specification.

### ClipRelay 0.1.3 restores relay and signer connections after idle periods

[ClipRelay](https://github.com/tajava2006/cliprelay) synchronizes a user's clipboard between devices through Nostr relays, encrypting the content to the same identity with [NIP-44](/en/topics/nip-44/). The matching [desktop](https://github.com/tajava2006/cliprelay/releases/tag/desktop/v0.1.3) and [Android](https://github.com/tajava2006/cliprelay/releases/tag/android/v0.1.3) 0.1.3 releases add a text box for sending typed text directly to another device's clipboard. They also test liveness with real relay round trips after idle periods, escalating from resubscription to socket replacement and a rebuilt connection pool, while stalled [NIP-46](/en/topics/nip-46/) signer calls now time out and rebuild automatically.

### NoorNote 1.3.2 moves article discovery into the social graph

[NoorNote](https://github.com/77elements/noornote) is a Nostr client for social posts, encrypted messages, long-form articles, and other event types across web, desktop, and Android. [Version 1.3.2](https://github.com/77elements/noornote/releases/tag/v1.3.2) replaces its flat global article feed with discovery drawn from first-, second-, and third-degree contacts, giving readers an article timeline rooted in their follow graph. It also collapses bursts of replayed direct messages from unknown senders into one rolling notification instead of producing a stack of toasts as relay history arrives.

### Bray 2.4.0 adds a compact remote-signing dialect

[Bray](https://github.com/forgesworn/bray) is a Nostr MCP server that gives software agents and people tools for relay access, identity, publishing, and remote signing. [Version 2.4.0](https://github.com/forgesworn/bray/releases/tag/v2.4.0) accepts a signing request whose event is an object as well as the stringified form used by [NIP-46](/en/topics/nip-46/), and adds `sign_event_compact`, which returns only the event ID, signature, public key, and timestamp. That smaller request and response format reduces memory use for constrained hardware signers, while the standard `sign_event` flow remains unchanged and both dialects produce a signature over the received event's ID.


## Newly Discovered

### Pact brings mutually consented agent bonds to Nostr

[Pact](https://github.com/bobodread876/pact), newly discovered this week, is an early-stage relationship layer for software agents built on MATE.md and a draft NIP-BD transport. Its signed, mutually consented bonds are held by the agents' own keys and can be published over Nostr, while private bonds use [NIP-59](/en/topics/nip-59/) gift wrapping. The monorepo includes an MCP server, TypeScript SDK, command-line client, self-hostable daemon, and web interface. Its latest repository activity predates this issue's weekly window, so this is a discovery note rather than a claim of a new release.


## In Development

### nostrord keeps group muting synchronized between devices

[nostrord](https://github.com/nostrord/nostrord) is a cross-platform client for relay-managed communities. [PR #250](https://github.com/nostrord/nostrord/pull/250) stores each account's per-group mute choices in a self-encrypted [NIP-78](/en/topics/nip-78/) (application-specific data) kind `30078` event, so a setting made on one device can follow the user to another without revealing the group list to the relay. The replaceable record uses newest-event ordering, listens for live changes, and rolls the interface back when signing or publication fails instead of leaving local state out of sync. Muted groups also stop contributing visible unread totals while retaining their unread position for the next visit.

### Amethyst completes Concord's invite lifecycle

[Amethyst](https://github.com/vitorpamplona/amethyst) is an Android Nostr client whose encrypted-community support implements the Concord protocol. [PR #3888](https://github.com/vitorpamplona/amethyst/pull/3888) lets invite links survive a community refounding by reissuing their bundles at the same addressable coordinates, while a ban check prevents a removed member from using that recovery path. It also implements the encrypted CORD-05 invite list on both the app and `amy` command-line client, adds per-link revocation tombstones, and requires relay confirmation before deleting the only stored signing key that can retire a link. The same work gives `amy` the control-key delivery, refounding, rekeying, and stranded-member recovery paths needed to follow later community epochs.

### Buzz carries each community's appearance across desktop and mobile

[Buzz](https://github.com/block/buzz) is a Nostr-based community workspace with desktop and mobile clients. Merged desktop [PR #3653](https://github.com/block/buzz/pull/3653) and mobile [PR #3767](https://github.com/block/buzz/pull/3767) store each community's theme, accent, and system-mode choice as an encrypted NIP-78 record on that community's relay. Both clients share the same versioned payload and keep identity-scoped local caches, so changing communities or accounts cannot apply the wrong appearance while the relay is unavailable. Replacement ordering, guarded writes, and resubscription after a closed connection let the two clients converge again after reconnecting.

[Buzz Desktop 0.5.10](https://github.com/block/buzz/releases/tag/desktop-v0.5.10) followed before the issue cutoff with a performance and reliability pass. It removes regressions introduced after 0.5.9, accelerates channel loading, bounds initial timeline retention, coalesces read-state persistence, preserves fresh channel timelines, and stops the relay ingest worker from crashing on reactions to project events. It also adds sending a thread message to a channel and narrows desktop search to the intended scope.


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

## NIP Deep Dive

### Event Deletion Requests (NIP-09)

[NIP-09](/en/topics/nip-09/), defined by the [primary specification](https://github.com/nostr-protocol/nips/blob/master/09.md), gives an event author a signed way to ask relays and clients to stop serving one or more of that author's events. It does not erase every copy. It carries the author's intent through the same relay network that distributed the original event.

The request is an ordinary signed kind `5` event. Its tags contain one or more `e` references to specific event IDs or `a` references to addressable-event coordinates, and the [NIP-09 tag rules](https://github.com/nostr-protocol/nips/blob/master/09.md#event-deletion-request) say it should include a `k` tag for each referenced event kind. The optional `content` can explain the reason. For an `a` reference, a relay should remove every version at that coordinate whose timestamp is no later than the request's `created_at`, which prevents an old deletion request from suppressing a later replacement.

[Authorship is the security boundary](https://github.com/nostr-protocol/nips/blob/master/09.md#relay-behavior). A relay should stop publishing a referenced event only when its `pubkey` matches the deletion request's `pubkey`, and a client must perform that check before hiding an event. A relay may not possess the referenced event and therefore may be unable to validate the relationship when accepting the request, so clients cannot treat relay acceptance as proof that the deletion was authorized. The specification also asks relays to retain the kind `5` request because another client may already hold the original event and encounter the request later.

Here is a [signed kind `5` event](https://primal.net/e/6f39fd3d0d593d97dd093f21fabe8f78895579d6979a6ecf14e169bd85bb0943):

```json
{
  "id": "6f39fd3d0d593d97dd093f21fabe8f78895579d6979a6ecf14e169bd85bb0943",
  "pubkey": "5877220aaae6e54a6f974602d5995c0fe24a3ea7ddabd8644bec795b9da00743",
  "created_at": 1786465675,
  "kind": 5,
  "tags": [
    ["e", "f3d47f8b813928c5baf7ac993846be0220dc37a2e7c7b128fb49a4b92711f131"],
    ["k", "30091"],
    ["a", "30091:5877220aaae6e54a6f974602d5995c0fe24a3ea7ddabd8644bec795b9da00743:survey:0ad5cebc-608b-47d7-97fd-9e6c47787199"],
    ["t", "nostr-survey"]
  ],
  "content": "Public survey summary deleted during privacy refresh",
  "sig": "846be83b038dc5f91af0c9d03a4ac81aff9bc4cfde7d85c849fa2fdae890f75cc444a4072f45aa18883b0b3871e15381b220182d6e366892f0c9c6f9c0557244"
}
```

Deletion remains a cooperative policy, not revocation of a signed object. A relay, cache, screenshot, or offline client can preserve the original bytes, and deleting the kind `5` request itself does not undo it. Clients may hide the target, mark it as disowned, or display the request reason, but should tell users that universal deletion cannot be guaranteed. This differs from [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md), where an `expiration` tag asks relays to stop storing an event after a time chosen when the event is published. NIP-09 handles a later author decision and can point to already-distributed events.

Current implementations apply that policy at different layers. [Divine PR #6623](https://github.com/divinevideo/divine-mobile/pull/6623) removes deleted videos from the client's event store, [strfry PR #251](https://github.com/hoytech/strfry/pull/251) extends valid deletion requests to gift-wrap recipients, and [Amethyst](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md) declares NIP-09 support in its client. [nostrord's group client](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/network/NostrGroupClient.kt) supplies another current implementation path.

### Reporting (NIP-56)

[NIP-56](/en/topics/nip-56/), defined by the [primary specification](https://github.com/nostr-protocol/nips/blob/master/56.md), standardizes a signed report about an account, event, or referenced blob. It separates the report signal from the moderation decision, allowing each client or relay to choose which reporters it trusts and what response fits its policy.

A report uses kind `1984` and must identify the reported account in a `p` tag. Reporting a note also requires an `e` tag for the event ID. The third value of the tag carries one of the specified categories: `nudity`, `malware`, `profanity`, `illegal`, `spam`, `impersonation`, or `other`. A report about a blob can use its hash in an `x` tag, an `e` tag for the event that referenced the blob, and an optional `server` tag for a location. Optional `L` and `l` tags from [NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md) can add a namespaced label when the fixed category list is not precise enough.

[The event proves only that one key made an allegation](https://github.com/nostr-protocol/nips/blob/master/56.md#reporting). The reported content does not become false, illegal, or removable merely because a valid kind `1984` exists, and an open relay cannot safely count anonymous reports as votes. The specification advises against automatic relay moderation because reports are easy to game, while allowing relay administrators to act on reports from moderators they already trust. A client can instead weight reports through a user's social graph, for example by blurring content after several trusted contacts flag the same account.

Here is a [signed kind `1984` event](https://primal.net/e/17301ea66066d34af9ba0b6957ed9d9d8854b9436939e682e21e7a5a8768e4b2):

```json
{
  "id": "17301ea66066d34af9ba0b6957ed9d9d8854b9436939e682e21e7a5a8768e4b2",
  "pubkey": "1ff02fb5cdc633c1be55368ab655490ec25d2f5dc2e364d4703bc3196d99eab1",
  "created_at": 1786465319,
  "kind": 1984,
  "tags": [
    ["p", "3a72b02cc05ee07310dc580874b6a9ca8271c6518b90655bd2e98003c9601e68", "impersonation"]
  ],
  "content": "",
  "sig": "6362e415410feb19e0505654a4660e8456b6b2aec5ae39173a0429a6a8e5fa1381c9488198ca2982db43ee8198af056f2a25537705c763784062056d0ab2eb1a"
}
```

[NIP-56 and NIP-09 solve different problems](https://github.com/nostr-protocol/nips/tree/master). A kind `1984` report can target somebody else's account or event, but confers no deletion authority. A kind `5` request expresses the original author's intent and is valid only against that author's own events. Neither guarantees removal: NIP-56 deliberately delegates action to local moderation policy, while NIP-09 depends on relays and clients honoring an authenticated request.

Implementations expose those choices in different products. [Divine PR #6591](https://github.com/divinevideo/divine-mobile/pull/6591) corrects report delivery in a short-video client, [Conduit PR #250](https://github.com/Conduit-BTC/conduit-mono/pull/250) reads reports as bounded context for marketplace participants, and [nostrord's NIP-56 module](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/nostr/Nip56.kt) publishes and processes report events. [Amethyst](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md#nip-support) also lists current NIP-56 support.


---

Send a NIP-17 DM to share a project or news item through the [Nostr Compass project](https://github.com/andotherstuff/nostr-compass).
