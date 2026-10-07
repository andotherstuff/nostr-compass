## Protocol and Spec Work

### Profile image metadata matched by exact URL

The merged [NIP-92 profile metadata change](https://github.com/nostr-protocol/nips/pull/2494) lets clients associate profile pictures and banners with [NIP-92](/en/topics/nip-92/), the media metadata format, only when URLs match exactly. Clients ignore unmatched tags and may use fallback URLs if the primary fails. Updates preserve metadata for unchanged fields and drop obsolete tags; the merge establishes specification behavior, not shipped client support.

### Signed descriptors for napplets

The open napplet proposal, for self-contained HTML applications, now uses a [signed descriptor tied to one HTML hash](https://github.com/nostr-protocol/nips/commit/020cb8b33a9e4c6b8ca4b2f9d0ed0a67843b68f7). It declares required and optional capabilities, intents, icons and a plaintext description, replacing the aggregate/path model. HTML publishing metadata cannot override the signed descriptor's authority; this remains proposed protocol text.

The [napplet CLI v0.7.0](https://github.com/napplet/web/releases/tag/%40napplet/cli%400.7.0) [implements the descriptor format and offline migration](https://github.com/napplet/web/pull/224). Unattended publishing defaults to the current format; a temporary explicit legacy option supports older shells. Migration verifies the original signed event and emits an unsigned template for review, without fetching, executing, signing or publishing its HTML. Ambiguous multi-file manifests must be rebundled, and permission and storage identities change to the artifact hash. [Explicit unknown capability declarations](https://github.com/napplet/web/pull/223) are retained with warnings; shells still decide whether they can load the app.

### Financial cashtags with separate binding and indexing

The [financial cashtag proposal](https://github.com/nostr-protocol/nips/pull/2491) separates a cashtag's location in text from its indexed financial identity. Non-indexed `cashtag` tags bind text using UTF-8 byte offsets, while [NIP-73](/en/topics/nip-73/), the external-identifier tagging convention, supplies `i` tags for symbol and instrument indexing. The proposal covers ISIN, FIGI, CAIP-19 and ISO-4217 identities, not prices or payments; implemented adoption is not established.

### Marmot membership requests and receipts

A proposed [Marmot membership workflow](https://github.com/marmot-protocol/marmot/pull/432), for encrypted group messaging, adds optional inner kind-458 requests, rejections, withdrawals and Applied receipts. Administrators independently validate KeyPackages, and an Applied receipt requires a matching accepted Commit. These checks tie receipts to accepted membership changes; the fixtures assume Messaging Layer Security group-key authorization facts and do not prove convergence.

### Marmot multi-device pairing security

Merged [Marmot multi-device design notes](https://github.com/marmot-protocol/marmot/pull/430) introduce private, single-use KeyPackages, a device-group roster, commitment-based pairing and ordered settings. The design addresses substitution, KeyPackage reuse and offline-searchable pairing. Normative wire definitions and interoperable device support remain unfinished.

### Wallet Connect commission invoices

The unimplemented [Nostr Wallet Connect commission proposal](https://github.com/nostr-wallet-connect/nwc/pull/9), for wallet-to-app communication, adds an optional `make_commission_invoice` permission governed by user-confirmed rate, payee, fee and budget limits. Shared-hash hold invoices coordinate payments, with idempotent retries to prevent duplicate requests. A preimage does not prove payment, and client delays and colluding routing remain risks.

### Cyberspace virtual brackets

The Cyberspace spatial protocol [specifies virtual brackets](https://github.com/arkin0x/cyberspace/pull/44) for games identified by their public keys. An `enter-virtual` action names the game in a `p` tag and records base and game positions; an exit returns to the entry’s base position. Verifiers follow links through unrecognized actions and compare recognized positions with the preceding recognized action, so a skipped action that moved the identity invalidates the chain. Existing client verifiers still need implementation changes.

writer_model: actual=openai-codex/gpt-6.1-sol, receipt=/opt/data/task-artifacts/compass-direct-2026-10-07/writer-protocol_and_spec_work/receipt.json; final root edits verified in assembled draft 4f46a95e8d1bad2c63d2e7b67b35c387bded0c07ac10b97c6ca12298922f354b

GATE: PENDING REVIEW
