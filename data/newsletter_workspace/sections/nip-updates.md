## Protocol and Spec Work

### Authenticated napplet endpoints

In the NAP specifications for napplet applications, [NAP-INC endpoint identifiers](https://github.com/napplet/naps/pull/104), merged October 9, replace bare handler names with authenticated identifiers. Equal names from different publishers no longer identify the same peer. The runtime still mediates communication, and root or snapshot manifests need no named `d` coordinate.

### Handler recommendations in invocation links

[The invocation-link recommendation](https://github.com/napplet/naps/pull/99), also merged October 9, allows an optional `#naddr` handler recommendation. A shell can offer discovery and installation, with ordinary resolution as a fallback. Saved preferences and shell policy take precedence. A recommended handler therefore supplies a discovery hint without replacing the user's existing choice or transferring installation authority to the link's sender.

### Delivery acceptance and application work

[The intent advertisement and delivery changes](https://github.com/napplet/naps/pull/91) derive roles and intents from the same verified manifest, using publisher-safe identifiers. Delivery acceptance no longer depends on the source application staying alive. An `ok: true` response accepts responsibility for delivery; it does not mean the destination's application work has finished. Retry and restart behavior remains runtime policy under this merged specification change.

### Cyberspace action chains

[Cyberspace's revised chain rules](https://github.com/arkin0x/cyberspace/pull/48) make a fork invalidate a signed action chain from its spawn and require clients to confirm the live head before signing another action. The Nostr-backed world adds [140 signed synthetic chains](https://github.com/arkin0x/cyberspace/pull/49) with normative verdicts for implementations. [Copy-credit rules](https://github.com/arkin0x/cyberspace/pull/47) use `q` references to the original object and notify its author for public remixes; sealed copies omit that notification. These are merged project specifications, with deployed verifier coverage unverified.

### Relay persistence acknowledgements

[The open persistence proposal](https://github.com/nostr-protocol/nips/pull/2496) introduces persisted acknowledgements, PROOF queries and optional signed kind 1797 relay attestations. A signature makes a storage claim attributable to a relay; it does not prove continued retention. Queries also disclose which events interest the client.

### Shared pins for Marmot groups

[Marmot's open pinning proposal](https://github.com/marmot-protocol/marmot/pull/434) defines authenticated shared state for up to 64 message references, with member and administrator permissions. Effective changes require an MLS Commit and epoch transition, and every resulting member leaf must support the feature. Pins do not copy message bodies or extend retention, so unavailable targets remain unresolved. The supplied fixtures assume authenticated state; they do not demonstrate cryptographic processing or convergence across clients.

writer_model: direct-codex

GATE: PASS (source-owner content review; full publication receipts are separate)
