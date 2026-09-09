## Protocol and Spec Work

### Nostr Implementation Possibilities

[NIP-01](/en/topics/nip-01/) now clarifies [the `limit: 0` filter](https://github.com/nostr-protocol/nips/pull/2460), merged September 4. A relay MUST return no stored events, MUST send `EOSE` when initial queries complete, and MUST keep the subscription active for new matching events. Clients can open a live-only subscription with one filter field while retaining local history. The clarification records compatible behavior across several relay implementations and public relays.

[NIP-78](/en/topics/nip-78/) gained an [authenticated app-data requirement](https://github.com/nostr-protocol/nips/pull/2458), merged September 3. Relays SHOULD require [NIP-42](/en/topics/nip-42/) authentication for kinds `78` and `30078` and SHOULD serve them only to the authenticated event author. That is a SHOULD, not a confidentiality guarantee: clients cannot treat arbitrary relays as private storage. The merge also discourages custom app-data kinds as generic public interchange.

[NIP-AC](/en/topics/nip-ac/) opened September 4 as an explicitly open [WebRTC-signaling proposal](https://github.com/nostr-protocol/nips/pull/2461). It uses provisional ephemeral kinds for ping, connect requests, offers, answers, and ICE candidates, addressed with `p` and grouped by a session `e` tag; kind `30600` supports discovery. Relays SHOULD broadcast and MUST NOT store those signaling events while peers connect directly. The numbers remain provisional, clients SHOULD use [NIP-65 relay lists](/en/topics/nip-65/), and applications needing confidentiality SHOULD encrypt offer, answer, and candidate content with [NIP-44](/en/topics/nip-44/).

writer_model: claude-opus-5 (bounded first-party wrapper run `7eeea05f-c01f-4f4d-a71b-7003fd6d9fa3`)

GATE: PENDING REVIEW
