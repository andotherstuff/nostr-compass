## NIP Deep Dive: NIP-05 and NIP-24

[NIP-05](/en/topics/nip-05/), human-readable account identifiers, connects `local@domain` to a public key; [NIP-24](/en/topics/nip-24/), additional profile metadata, makes public presentation portable across clients. The [NIP-05 specification](https://github.com/nostr-protocol/nips/blob/master/05.md) is merged, final and optional. The [NIP-24 specification](https://github.com/nostr-protocol/nips/blob/master/24.md) is merged, draft and optional: draft describes its maturity, not a newly opened proposal.

### Checking an account name

After validating the signed profile, read `nip05` from its JSON-string `content`. Split the identifier and request `https://<domain>/.well-known/nostr.json?name=<local>` over HTTPS, ignoring redirects. The local part permits `a-z0-9-_.`; the response's `names[local]` must equal the author's hexadecimal public key. Optional `relays` supplies discovery hints, not authenticated relay endorsements. `_@domain` is a root identifier that may display as the domain, according to the [lookup specification](https://github.com/nostr-protocol/nips/blob/master/05.md).

Identifier-first discovery fetches the mapping, then the key's profile and matching claim. Follows retain the public key: domain reassignment invalidates the old name association without transferring the follow. This proves an association, not legal identity or biography; the email-like string implies no mailbox. Missing names, mismatched keys, invalid JSON, redirects and unreachable endpoints cannot establish it. Browser CORS failures are indistinguishable from other fetch failures under the [NIP-05 rules](https://github.com/nostr-protocol/nips/blob/master/05.md).

The identifier server receives the requested name and may observe the client's network origin. External profile images can also reveal browsing activity to their hosts. Neither specification supplies a universal privacy proxy or cache policy; changing mappings require revalidation. NIP-05 began with [June 18, 2021's DNS-name introduction](https://github.com/nostr-protocol/nostr/commit/1aebb3911c5cc024a1de24cdc7087790b5c092ee), followed by [December's well-known JSON revision](https://github.com/nostr-protocol/nostr/commit/012ebff47d2649b37158db5105f10e3bc777f43c).

### Portable metadata and its limits

NIP-24 adds optional `display_name`, `website`, `banner`, Boolean `bot` and object `birthday`, whose year, month and day may each be omitted. Authors should still supply `name`; deprecated `displayName` and `username` should be ignored or removed. Partial birthdays reduce disclosure, but supplied details remain public. The [metadata specification](https://github.com/nostr-protocol/nips/blob/master/24.md) defines fields, not universal recovery from wrong types, invalid dates or duplicate keys.

Generic `r`, `i`, `title` and lowercase `t` tags mean web URL, external identifier, named item and hashtag unless a more specific specification overrides them. Historical kind-3 relay-map content is deprecated in favor of [NIP-65](/en/topics/nip-65/), relay-list metadata. [NIP-24's introduction](https://github.com/nostr-protocol/nips/commit/44c21c9d82dfa9fbe04655668c03400fa0ac1e34) was authored September 24 and committed September 26, 2023. [NIP-92](/en/topics/nip-92/), media attachment metadata, now permits [profile-image descriptions](https://github.com/nostr-protocol/nips/pull/2494) through URL-matched `imeta` tags.

### One signed profile, both specifications

This kind-0 profile was recovered from relay.damus.io on October 6. Under [NIP-01](/en/topics/nip-01/), basic event structure, `id` is the canonical event hash, `pubkey` the signing identity, `created_at` the author-provided Unix timestamp, `kind:0` the replaceable profile type, `tags` the event tags, `content` the exact profile JSON string, and `sig` the signature. The [event specification](https://github.com/nostr-protocol/nips/blob/master/01.md) authenticates payload integrity, not its truth.

```json
{
  "kind": 0,
  "id": "700f005cff9fcd93268053f9fda0d4f3cccb0847fc6aa4547ba80c622b98aa3a",
  "pubkey": "208ad03138eb32da4b3fb2edb79d13a8e3532842db627d76aff8168db564a0e9",
  "created_at": 1791295764,
  "tags": [
    [
      "client",
      "Nostrich"
    ]
  ],
  "content": "{\"name\":\"calavera\",\"nip05\":\"calavera@primal.net\",\"about\":\"Audentes Fortuna Iuvat\\nLe mie gesta sul video ludo 👇\",\"lud16\":\"solartern74@nostrich.org\",\"display_name\":\"Manny Calavera\",\"picture\":\"https://m.primal.net/OHcz.jpg\",\"banner\":\"https://m.primal.net/OHdW.gif\",\"website\":\"https://rumble.com/user/HomoLudensArchive\"}",
  "sig": "9bc7be81b87a7db10f812e23181fda38d5e369c49d9a52757b16fb4ff0ad544abb24486b346382d5f43fc127794ac0562d80e6e4a7df8489512f40ffbedcf670"
}
```

Here `name` is the short label, `display_name` the richer label, and `nip05` the separately checked association. `picture` and `banner` are image URLs, `website` an author-supplied link, and `about` self-description. `lud16` is a payment-address extension, not identity verification. The `client` tag self-asserts application context. No `imeta`, bot or birthday appears; [NIP-24's optional fields](https://github.com/nostr-protocol/nips/blob/master/24.md) need not all be present.

### Implementation boundaries

Amethyst's [lookup client](https://github.com/vitorpamplona/amethyst/blob/c9901247666feb0485f4b0137831092cbc924d74/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip05DnsIdentifiers/Nip05Client.kt) compares the mapped key, while its [birthday decoder](https://github.com/vitorpamplona/amethyst/blob/c9901247666feb0485f4b0137831092cbc924d74/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip01Core/metadata/BirthdayTolerantSerializer.kt) ignores undecodable birthday fields and retains the profile. The Damus client's [lookup](https://github.com/damus-io/damus/blob/4a94f666d7e159e380e10b4dbbb2967d1688709e/damus/Features/NIP05/Models/NIP05.swift) models names without explicit redirect rejection in that file, and its [profile bindings](https://github.com/damus-io/damus/blob/4a94f666d7e159e380e10b4dbbb2967d1688709e/nostrdb/src/bindings/swift/NdbProfile.swift) expose display name, website and banner. The rust-nostr library's [identifier types](https://github.com/rust-nostr/nostr/blob/463f0c2d48e1d3c9e295cc231715d8a3855c65d3/nostr/src/nips/nip05.rs) support root lookup and relay hints, while its [metadata decoder](https://github.com/rust-nostr/nostr/blob/463f0c2d48e1d3c9e295cc231715d8a3855c65d3/nostr/src/nips/nip01/mod.rs) preserves custom JSON but can reject wrong types in known fields.

writer_model: actual=openai-codex/gpt-6.1-sol, receipt=/opt/data/task-artifacts/compass-direct-2026-10-07/writer-deep_dive/receipt.json; final root edits verified in assembled draft 4f46a95e8d1bad2c63d2e7b67b35c387bded0c07ac10b97c6ca12298922f354b

GATE: PENDING REVIEW
