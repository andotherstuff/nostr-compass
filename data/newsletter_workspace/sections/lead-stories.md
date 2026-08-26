## Top Stories

### Postr launches as a small Android composer

[Postr](https://gitworkshop.dev/npub1qwkd5wzftcxquuhtkcg0xn9ed7evksluuppf7qdmdh34ywe9uncs5uqfvl/relay.ngit.dev/postr) is a deliberately small Android composer for kind 1 notes. Private-key custody stays in [Amber](https://github.com/greenart7c3/Amber), an Android [NIP-55](/en/topics/nip-55/) (local signer) and NIP-46 signer. Version 1.0.0 ships a durable outbox that survives lost connectivity and process death, account-specific private drafts, and [Blossom](/en/topics/blossom/) attachments with verified hashes and scoped upload authorization.

A post succeeds after Postr reads back the identical signed event and checks its signature. Retries keep the same event id. Publication uses the author's [NIP-65](/en/topics/nip-65/) (relay list) write relays plus encrypted bootstrap relays, or a custom per-account list. A signed [NIP-34](/en/topics/nip-34/) (git-over-Nostr) [repository announcement](https://njump.me/nevent1qqsqxdwxa8k5e0ftf6j6q5ucs3u94ezgjqmyzwznqt99pyxxw23c74spz3mhxue69uhhyetvv9ujumn8d96zuer9wcx4nr0m) and a matching [kind 0 project profile](https://njump.me/nevent1qqs24gy97frkjkma8ys3rwc3jj8f0qrrmsxjwe39jxrhuemztrygr8qpz3mhxue69uhhyetvv9ujumn8d96zuer9wcspcsat) are published on `relay.ngit.dev`. Feeds, analytics, advertising, and key storage stay outside the app.

### Infans encrypts family tracking and co-parent sync over Nostr

Co-parents can keep feeding, sleep, and growth records on their own phones and share them without a family-data vendor. [Infans](https://github.com/TurkeyNostr/infans) is an Android baby tracker that treats a local Room database as the source of truth and publishes encrypted kind 30078 [NIP-78](/en/topics/nip-78/) (application-specific data) events for backup and partner sync. Its repository labels the local cipher [NIP-44](/en/topics/nip-44/) (payload encryption), but the implementation uses AES-256-GCM while NIP-44 v2 requires ChaCha20 with HMAC-SHA256, so local-mode payloads should not be presented as NIP-44-compatible.

[Partner sync](https://github.com/TurkeyNostr/infans/blob/main/README.md) uses d-tag `baby-tracker-sync`, while self-backups use `baby-tracker-backup`. Async notes travel inside the partner payload. The documented Amber [NIP-55](/en/topics/nip-55/) (local signer) path delegates signing and encryption to the signer, but the repository provides no interoperability test showing that every backup and partner-sync path produces NIP-44-v2 ciphertext. The repository presents neither a medical-device claim nor a third-party security review.

### walls.rip Ghost Chat brings PGP-encrypted chat to public Nostr relays

[walls.rip](https://walls.rip/comms) is an anonymous communication toolkit whose Ghost Chat mode creates or imports an OpenPGP identity in the browser. Its [open source client](https://github.com/KYC-rip/walls-rip/tree/cf40bda32df5f106007631b21afc3cd193ac0cda/src/components/ghostChat) encrypts each message to the recipient's PGP public key. Readable conversation remains in local session storage on the device; the application has no chat account or central message database.

The transport is real Nostr, but it is deliberately app-specific. Ghost Chat [publishes armored ciphertext as kind 1 events](https://github.com/KYC-rip/walls-rip/blob/cf40bda32df5f106007631b21afc3cd193ac0cda/src/utils/nostrService.ts) to five default relays and labels each event with a stable room tag derived from the recipient's PGP fingerprint. That gives developers a concrete example of using relays as censorship-resistant message transport, while also showing why decentralized delivery alone is not metadata-private or interoperable with NIP-17 direct messages.

### pakstr 0.13.0 through 0.15.0 makes Zapstore publication explicit

After [July's 0.3.1 packaging and Amber work](/en/newsletters/2026-07-29-newsletter/#pakstr-031), [pakstr](https://git.nostrdev.com/stuff/pakstr) is a CLI that turns a folder of web assets into a signed Android APK and publishes it to Zapstore with a Nostr key. [0.13.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.13.0) adds automatic release versioning. The 0.13.1 through 0.13.3 follow-ups repair Blossom publication: [authorization now uses base64url](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.13.1), [uploads carry a Content-Digest](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.13.2), and the [Zapstore application event is published before the Blossom upload](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.13.3).

[0.14.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.14.0) validates the Zapstore publisher before a publish proceeds. [0.15.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.15.0) writes listing metadata onto kind 32267 application events and puts release notes in kind 30063 release-event content, so a packaged app's Zapstore record can carry name, summary, and notes without a separate manual listing step.

### Heterodyne specifies portable personas and encrypted social communication

[Heterodyne](https://radicle.network/nodes/iris.radicle.network/rad%3Az2zX5XvPiggGJvCn8DPkp1hRNGA5) is a specification-first protocol family for portable personas, authenticated communication, own-device control, and social interaction. Its [current README](https://radicle.network/nodes/iris.radicle.network/rad%3Az2zX5XvPiggGJvCn8DPkp1hRNGA5) composes four existing layers: Nostr signed events, [Radicle](https://radicle.xyz) (peer-to-peer git) durable storage, [Marmot](/en/topics/marmot/) (MLS group messaging over Nostr) for encrypted direct and group conversations, and [KERI](https://arxiv.org/abs/1907.02143) (Key Event Receipt Infrastructure) key-event logs for identity rotation. A persona is described as a cold-root Nostr npub plus an accepted KERI log; routine signing uses rotating epoch keys, while Radicle node identities are dual-proof delegated.

The family splits that work into [four independently versioned 0.x drafts](https://radicle.network/nodes/iris.radicle.network/rad%3Az2zX5XvPiggGJvCn8DPkp1hRNGA5). Core owns identity, key-event-log verification, canonical Nostr bytes, and the Radicle repository substrate; Comms owns Nostr-native envelopes, privacy tiers, publishing, and Marmot conversations; and Social owns public following, interactions, and lists. Control, for own-device enrollment and grants, is incomplete and cannot be claimed. These documents remain drafts that may break before 1.0, and this issue introduces the family before any Heterodyne client release has landed.

GATE: PENDING REVIEW
