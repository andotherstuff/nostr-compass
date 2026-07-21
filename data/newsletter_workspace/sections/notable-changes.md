## Notable Code and Documentation Changes

### nostream merges NIP-42 read restriction and NIP-43 membership strategies

[nostream](https://github.com/Cameri/nostream), the TypeScript relay implementation, merged seven PRs this week without cutting a release. The headline pair is [PR #702](https://github.com/Cameri/nostream/pull/702), which restricts reads of encrypted event kinds to authenticated recipients under [NIP-42](/en/topics/nip-42/), and [PR #676](https://github.com/Cameri/nostream/pull/676), which adds join and leave request strategies under [NIP-43](/en/topics/nip-43/). Together they give relay operators a working authentication-plus-membership access-control stack; this week's NIP Deep Dive walks through exactly that handshake.

### Open: NIP-47 simplification proposal

[PR #2419](https://github.com/nostr-protocol/nips/pull/2419), opened by frnandu, proposes simplifying the [NIP-47](/en/topics/nip-47/) (Nostr Wallet Connect) core spec and moving functionality into extensions. NWC is among the most widely deployed NIPs, so a structural split of its core spec is a discussion worth watching even before any merge decision. Client and wallet authors that implement NIP-47 should weigh in while the proposal is young.

### FIPS v0.4.1 tightens the transport the Iris ecosystem builds on

[jmcorgan/fips](https://github.com/jmcorgan/fips) shipped [v0.4.1](https://github.com/jmcorgan/fips/releases/tag/v0.4.1), a maintenance release capping antipoison state, fixing convergence and MTU handling, and cutting CPU use. On its own this is plumbing, but it matters this week as connective tissue: the browser TypeScript runtime [fips-ts](https://github.com/mmalmi/fips-ts) from the Iris-ecosystem cluster in this issue's News section is wire-compatible with this Rust transport, so fixes here propagate directly to what the browser runtime interoperates with.

### Open: Trusted Relay Assertions draft

[PR #2418](https://github.com/nostr-protocol/nips/pull/2418), opened by Wisp contributor Letdown2491, is a new draft proposal for publishing relay trust assertions: [NIP-66](/en/topics/nip-66/) metrics, operator reputation, and reports as relay-queryable data. No NIP number is assigned yet and the proposal is early, but it aims at a real gap, giving clients a standard way to reason about which relays to trust rather than hardcoding operator lists.

GATE: PASS
