## NIP Deep Dive: NIP-42 and NIP-43


Running a relay that is not open to everyone used to mean inventing everything yourself. A paid or invite-only relay operator had to maintain a whitelist out of band, usually a text file of pubkeys collected over DMs, with no standard way to tell a connected client "prove who you are" and no standard way for a user to ask for admission or know whether they were a member. Every relay that wanted gated reads or gated writes built its own private mechanism, and clients could not interoperate with any of them. [NIP-42](/en/topics/nip-42/) standardizes the proof-of-identity half of that problem, and [NIP-43](/en/topics/nip-43/) standardizes the membership half. This week nostream, the TypeScript relay, merged the pair end to end: [PR #702](https://github.com/Cameri/nostream/pull/702) restricts reads of encrypted kinds to authenticated recipients, and [PR #676](https://github.com/Cameri/nostream/pull/676) adds join and leave request event strategies, both merged on July 20.

### NIP-42: Authentication of clients to relays

[NIP-42](/en/topics/nip-42/) answers one question: who is on this connection? A relay that wants to gate reads or writes sends an `AUTH` message carrying a challenge string, at connect time or on demand when a request needs authentication. The client replies with its own `AUTH` message containing a signed ephemeral event, kind 22242, and the relay answers with an `OK` message exactly as if the auth event were an ordinary write. The authenticated session then holds for the duration of the connection, and a client may authenticate several pubkeys on one connection with a sequence of `AUTH` messages, each of which the relay treats as authenticated.

The signed auth event looks like this:

```json
{
  "id": "4ef6f2c0b1a84c9a3d0f9c58e2a1b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0",
  "pubkey": "c308e1f882c1f1dff2a43d4294239ddeec04e575f2d1aad1fa21ea7684e61fb5",
  "created_at": 1753195800,
  "kind": 22242,
  "tags": [
    ["relay", "wss://relay.example.com/"],
    ["challenge", "challengestringhere"]
  ],
  "content": "",
  "sig": "8b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1"
}
```

The `pubkey` is the identity being proved, since the relay verifies the `sig` over the event `id` against it. The `kind` 22242 sits in the ephemeral range: the event is a connection-level credential, and relays must never store it or broadcast it to other clients. The `relay` tag binds the signature to one relay URL so a captured auth event cannot be replayed against a different relay, and the `challenge` tag binds it to the specific challenge string the relay issued on this connection, blocking replay of a captured auth on a later connection. The `created_at` must be close to the current time, within roughly a ten-minute window, so a stale auth event expires on its own. The `content` field is empty; nothing is being published.

The spec also defines two machine-readable prefixes that make gating visible to clients. A relay that rejects a subscription because the client has not authenticated yet answers with a `CLOSED` message starting with `auth-required:`, and a rejected write gets an `OK` with the same prefix. A client that authenticated but still lacks permission for the action gets `restricted:` instead. That distinction is what [nostream's PR #702](https://github.com/Cameri/nostream/pull/702) builds on: reads of encrypted kinds can now be closed with `auth-required:` until the requesting pubkey proves it is the recipient.

### NIP-43: Relay Access Metadata and Requests

[NIP-43](/en/topics/nip-43/) answers the follow-up question: now that the relay knows who you are, what are you allowed to do? Where NIP-42 is a handshake on a live connection, NIP-43 is a set of published events that describe membership state and let users ask to change it. On the relay side, a kind 13534 event, signed by the pubkey in the relay's [NIP-11](/en/topics/nip-11/) `self` field, lists one `member` tag per pubkey, with optional role arguments pointing at role definitions published as kind 33534. Kind 8000 announces a member being added and kind 8001 announces a removal, both signed by the same relay key with a `p` tag for the affected member. On the user side, kind 28934 is a join request carrying an invite code in a `claim` tag, kind 28935 is an ephemeral invite-code event the relay generates on the fly when a user requests a claim, and kind 28936 is a leave request.

A join request looks like this:

```json
{
  "id": "9f0e1d2c3b4a59687a6b5c4d3e2f1098a7b6c5d4e3f2019a8b7c6d5e4f3021a9b8",
  "pubkey": "ee1d336e13779e4d4c527b988429d96de16088f958cbf6c074676ac9cfd9c958",
  "created_at": 1753195900,
  "kind": 28934,
  "tags": [
    ["-"],
    ["claim", "invite-code-from-operator"]
  ],
  "content": "",
  "sig": "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2"
}
```

The `pubkey` is the user asking for admission, and kind 28934 marks the event as a join request. The `-` tag is the [NIP-70](/en/topics/nip-70/) protected-event marker, telling relays not to accept this event from anyone but its author. The `claim` tag carries the invite code the user obtained out of band, and `created_at` must be now, plus or minus a few minutes, so an old request cannot be replayed. The relay answers the claim with an `OK` message, reusing the NIP-42 `restricted:` prefix for failures such as an expired or invalid code, and should then update its kind 13534 list and may publish a kind 8000 add-member event. Membership is deliberately not derived from a single event: the spec says the relay-signed list should not be considered exhaustive or authoritative, and a client deciding whether someone is currently a member should consult both the relay's kind 13534 and the member's own events. Clients must only send join, invite, or leave requests to relays that advertise this NIP in the `supported_nips` section of their NIP-11 document, and [nostream's PR #676](https://github.com/Cameri/nostream/pull/676) is the relay-side machinery that turns those request kinds into actual membership changes.

### History

NIP-42 is the older of the two by a wide margin. It entered the NIPs repository on January 2, 2023, in [commit c80be21c](https://github.com/nostr-protocol/nips/commit/c80be21c), where fiatjaf drastically simplified an earlier relay-auth NIP drafted by semisol, collapsing a more complex challenge scheme into the single signed ephemeral event the spec still uses today. NIP-43 arrived much later, on October 30, 2025, when hodlbod's [PR #1079](https://github.com/nostr-protocol/nips/pull/1079) merged, adding relay access metadata and requests built directly on top of NIP-42's `restricted:` prefix. The two-and-a-half-year gap reflects how long the ecosystem ran paid and private relays on ad-hoc whitelists before the membership layer got a standard.

### Implementations

On the relay side, [nostream](https://github.com/Cameri/nostream) now ships both halves after this week's merges. [strfry](https://github.com/hoytech/strfry) implements NIP-42, validating kind 22242 auth events in its ingester and issuing challenges from its config. [nostr-rs-relay](https://github.com/scsibug/nostr-rs-relay) handles the AUTH handshake in its connection layer with tests covering the challenge and timestamp window. [khatru](https://github.com/fiatjaf/khatru), the Go relay framework, tracks the authenticated pubkey per connection so policies can gate reads and writes on it. On the client side, [Amethyst](https://github.com/vitorpamplona/amethyst) signs kind 22242 responses to relay challenges, including per-stream auth for its Concord encrypted communities. The two NIPs split access control along a clean line: NIP-42 is proof of identity, scoped to one connection, one challenge, and a few minutes of validity, and it says nothing about policy. NIP-43 is policy, expressed as ordinary relay events: who is a member, who was added or removed, and how a user requests those transitions. The gap implementers should keep in mind is that nothing yet standardizes finer-grained permissions beyond NIP-43's optional role metadata, so any relay doing more than a binary member/non-member split is designing that layer on its own.

---

That's it for this week. Building something or have news to share? Reach out via NIP-17 DM or find us on Nostr.

GATE: PASS
