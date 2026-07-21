## NIP Deep Dive

This week nostream, the TypeScript relay implementation, merged two pull requests that implement the relay access-control stack end to end: [PR #702](https://github.com/Cameri/nostream/pull/702) restricts reads of encrypted kinds to authenticated recipients, and [PR #676](https://github.com/Cameri/nostream/pull/676) adds join and leave request strategies. Those two changes land on two different NIPs that are designed to work as a pair, so this issue's Deep Dive covers them together.

### NIP-42: Authentication of clients to relays

[NIP-42 (client authentication to relays)](/en/topics/nip-42/) answers one question: who is connected? A relay that wants to gate reads or writes sends an `AUTH` message containing a challenge string. The client signs an ephemeral kind 22242 event that binds its pubkey to that challenge and to the relay URL, and returns it inside an `AUTH` message of its own. The relay answers with an `OK`, exactly as if the auth event were a normal write. From that point on, the connection is treated as authenticated for the duration of the session.

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

Three details do the security work. The `challenge` tag binds the event to the specific challenge the relay issued, blocking replay of a captured auth. The `relay` tag binds the event to one relay URL, blocking reuse of the same signature elsewhere. The `created_at` timestamp must be within about ten minutes of now, so a stale auth event expires on its own. Relays must never broadcast kind 22242 to other clients; it exists only as a connection-level credential. The spec also defines two machine-readable prefixes that make gating visible to clients: `auth-required:` in an `OK` or `CLOSED` message means the client has not authenticated yet, and `restricted:` means it authenticated but still lacks permission for that action. That distinction is what nostream's PR #702 builds on: reads of encrypted kinds can now be closed with `auth-required:` until the requesting pubkey proves it is the recipient.

### NIP-43: Relay Access Metadata and Requests

[NIP-43 (relay access metadata and requests)](/en/topics/nip-43/) answers the follow-up question: now that the relay knows who you are, what are you allowed to do? Where NIP-42 is a handshake on a live connection, NIP-43 is a set of published events that describe membership state and let users ask to change it. A relay publishes a kind 13534 membership list signed by the pubkey in its NIP-11 `self` field, with one `member` tag per pubkey. Kind 8000 announces a member being added, kind 8001 announces a removal. On the user side, kind 28934 is a join request carrying an invite code in a `claim` tag, kind 28935 is an ephemeral invite code a relay can hand out on demand, and kind 28936 is a leave request.

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

The relay answers the claim with an `OK` message, reusing the NIP-42 `restricted:` prefix for failures such as an expired or invalid code, and should then update its kind 13534 list and optionally publish a kind 8000 add-member event. Membership state is deliberately not derived from a single event: a client deciding whether someone is currently a member is expected to consult both the relay-signed list and the member's own events. Clients must only send join, invite, or leave requests to relays that advertise this NIP in the `supported_nips` section of their NIP-11 document, and nostream's PR #676 is the relay-side machinery that turns those request kinds into actual membership changes.

### How They Work Together

The two NIPs split access control along a clean line. NIP-42 is proof of identity, scoped to one connection, one challenge, and a few minutes of validity. It says nothing about policy. NIP-43 is policy, expressed as regular relay events: who is a member, who was added, who was removed, and how a user requests any of those transitions. A private or paid relay uses them in sequence. The user obtains an invite code out of band, submits a kind 28934 join request, and the relay records membership with an updated kind 13534 and a kind 8000. On every subsequent connection, the relay challenges with `AUTH`, the client answers with kind 22242, and only then does the relay consult the NIP-43 membership state to decide what that authenticated pubkey may read or write. Reads of restricted kinds return `auth-required:` before the handshake and `restricted:` after it if the authenticated key is not on the list.

That two-layer shape is what nostream just shipped, and it matches what relay groups and invite-only relays have been converging on: one NIP for the handshake, one NIP for the roster. It also leaves a real gap that implementers should keep in mind. NIP-43 membership events tell you the state; NIP-42 tells you the key on the wire; nothing yet standardizes the finer-grained roles and permissions that relays may attach to members, beyond the optional role metadata NIP-43 sketches. For now, any relay doing more than a binary member/non-member split is designing that layer on its own.

GATE: PASS
