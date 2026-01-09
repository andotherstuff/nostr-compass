---
title: 'Nostr Compass #4'
date: 2026-01-07
publishDate: 2026-01-07
draft: false
type: newsletters
---

Welcome back to Nostr Compass, your weekly guide to the Nostr protocol ecosystem.

**This week:** Primal Android ships [NIP-46](/en/topics/nip-46/) remote signing and [NIP-55](/en/topics/nip-55/) local signer support, making it a full-fledged signing hub for other Android apps. The [Marmot Protocol](/en/topics/marmot/) team addressed findings from a security audit with 18 merged PRs hardening [MLS](/en/topics/mls/)-based encrypted messaging. Citrine hits v1.0 and Applesauce ships v5.0 across its entire library suite. TENEX builds out AI agent supervision on Nostr, and Jumble adds smart relay pooling. A NIP-55 spec fix clarifies `nip44_encrypt` return fields, and a [NIP-50](/en/topics/nip-50/) PR proposes query expression extensions for advanced search. In our deep dive, we explain [NIP-04](/en/topics/nip-04/) and [NIP-44](/en/topics/nip-44/): why the legacy encryption has security flaws and how the modern replacement fixes them.

## News

**Primal Android Becomes a Full Signing Hub** - [Version 2.6.18](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18) adds both [NIP-46](/en/topics/nip-46/) remote signing and [NIP-55](/en/topics/nip-55/) local signing, turning Primal into a complete signer for other Nostr apps. Remote signing via NIP-46 lets users connect to bunker services over Nostr relays, keeping keys off their device entirely. Local signing via NIP-55 exposes Primal as an Android content provider, so apps like Amethyst or Citrine can request signatures without ever touching the private key. [Several follow-up PRs](https://github.com/PrimalHQ/primal-android-app/pull/839) fixed compatibility issues with the NIP-55 spec's hex pubkey requirement, and improved parsing of malformed `nostrconnect://` URIs. The release also includes media pre-caching for smoother scrolling, improved thread load times, and avatar pre-caching.

**Marmot Protocol Hardens Security After Audit** - The [Marmot Development Kit](https://github.com/marmot-protocol/mdk) (mdk), which implements [NIP-104](/en/topics/nip-104/) MLS-based end-to-end encrypted messaging, received extensive security fixes this week. Eighteen merged pull requests addressed audit findings including: [hash verification for encrypted group images](https://github.com/marmot-protocol/mdk/pull/97) to prevent storage-level blob substitution attacks, [pagination for pending welcomes](https://github.com/marmot-protocol/mdk/pull/110) to prevent memory exhaustion, [MLS Group ID leakage in error messages](https://github.com/marmot-protocol/mdk/pull/112), and [base64 encoding enforcement](https://github.com/marmot-protocol/mdk/pull/98) for key packages. The [Marmot spec itself was updated](https://github.com/marmot-protocol/marmot/pull/20) with MIP-04 v2 versioning and security improvements. Active PRs continue addressing nonce reuse, secret zeroization, and cache pollution vectors.

**Nostrability Tracks Relay Hint Support** - A new [relay hints compatibility tracker](https://github.com/nostrability/nostrability/issues/270) documents how clients construct and consume relay hints across the ecosystem. The tracker reveals that while most clients now construct hints per [NIP-10](/en/topics/nip-10/) and [NIP-19](/en/topics/nip-19/), consumption varies widely: some clients include hints in outgoing events but don't use incoming hints for fetching. Six clients earned "Full" tier status for complete implementation. The tracker is useful for developers checking interoperability and for users wondering why some clients find content others can't.

**Nostria 2.0 Ships Cross-Platform Feature Overhaul** - The [Nostria](https://nostria.app) client [released version 2.0](nostr:naddr1qvzqqqr4gupzp5daxvenwv7ucsglpm5f8vuts530cr0zylllgkwejpzvak0x2kqmqqykummnw3exjcfdxgedqf5p) on December 30 with significant additions across iOS (TestFlight), Android (Play Store), Web, and Windows. The release adds native music support with playlist creation, track uploading, zap-based artist payments, and a WinAmp-style player with functional equalizer. Live streaming gets Game API integration showing rich metadata during gameplay streams. A new Summary feature generates hourly, daily, or weekly activity digests as compressed timeline views. The Discover section offers curated lists for finding content and profiles. Media publishing is simplified with automatic short-form post generation for cross-client discoverability. Remote signer connections now work via QR code scanning without manual configuration. Profile discovery addresses a common Nostr pain point: when users move between relays without bringing their metadata, Nostria locates their profile and republishes it to their current relays. Premium subscribers gain YouTube channel integration, private Memos, analytics dashboards, and automatic following list backups with merge/restore options.

## NIP Updates

Recent changes to the [NIPs repository](https://github.com/nostr-protocol/nips):

**Merged:**
- **[NIP-55](/en/topics/nip-55/)** - Fixed the return field for `nip44_encrypt` method ([#2184](https://github.com/nostr-protocol/nips/pull/2184)). Android signers must now return the encrypted payload in the `signature` field (matching `nip44_decrypt`) rather than a separate field. This aligns the spec with existing implementations in Amber and Primal.

**Open PRs:**
- **[NIP-50](/en/topics/nip-50/)** - Query Expression Extensions ([#2182](https://github.com/nostr-protocol/nips/pull/2182)) proposes extending NIP-50 search with structured query expressions. The PR adds operators like `kind:1`, `author:npub1...`, and boolean combinations (`AND`, `OR`, `NOT`), enabling more precise search queries beyond simple text matching. This would let clients build advanced search interfaces while maintaining backward compatibility with basic search strings.

## NIP Deep Dive: NIP-04 and NIP-44

This week we cover Nostr's encryption standards: the legacy NIP-04 that you'll still encounter, and its modern replacement NIP-44 that fixes critical security flaws.

### [NIP-04](/en/topics/nip-04/): Encrypted Direct Messages (Legacy)

[NIP-04](https://github.com/nostr-protocol/nips/blob/master/04.md) was Nostr's first attempt at encrypted messaging, using kind 4 events. While simple to implement, it has known security weaknesses and is deprecated in favor of NIP-44.

**How it works:** NIP-04 uses ECDH (Elliptic Curve Diffie-Hellman) to derive a shared secret between sender and recipient, then encrypts with AES-256-CBC.

```json
{
  "id": "<event-id>",
  "pubkey": "<sender-pubkey>",
  "created_at": 1736200000,
  "kind": 4,
  "tags": [["p", "<recipient-pubkey>"]],
  "content": "base64-ciphertext?iv=base64-iv",
  "sig": "<signature>"
}
```

The encryption flow:
1. Compute shared point: `shared = ECDH(sender_privkey, recipient_pubkey)`
2. Derive key: `key = SHA256(shared_x_coordinate)`
3. Generate random 16-byte IV
4. Encrypt: `ciphertext = AES-256-CBC(key, iv, plaintext)`
5. Format content: `base64(ciphertext)?iv=base64(iv)`

**Security problems:**

- **No authentication:** AES-CBC provides confidentiality but not integrity. An attacker who controls a relay could modify ciphertext bits, causing predictable changes to plaintext (bit-flipping attacks).
- **IV in the clear:** The initialization vector is transmitted alongside ciphertext, and CBC mode with predictable IVs enables chosen-plaintext attacks.
- **No padding validation:** Implementations vary in how they handle PKCS#7 padding, potentially enabling padding oracle attacks.
- **Metadata exposure:** The sender pubkey, recipient pubkey, and timestamp are all visible to relays.
- **Key reuse:** The same shared secret is used for all messages between two parties, forever.

**Why it still exists:** Many older clients and relays only support NIP-04. You'll encounter it when interacting with legacy systems. Signers like Amber and apps like Primal still implement `nip04_encrypt`/`nip04_decrypt` for backward compatibility.

### [NIP-44](/en/topics/nip-44/): Versioned Encryption

[NIP-44](https://github.com/nostr-protocol/nips/blob/master/44.md) is the modern encryption standard, designed to fix NIP-04's well-known flaws. A Cure53 security audit of NIP-44 implementations identified 10 issues (including timing attacks and forward secrecy concerns) that were addressed before the spec was finalized. It uses ChaCha20-Poly1305 with proper key derivation and authenticated encryption.

**Key improvements over NIP-04:**

| Aspect         | NIP-04                     | NIP-44                  |
|:---------------|:---------------------------|:------------------------|
| Cipher         | AES-256-CBC                | XChaCha20-Poly1305      |
| Authentication | None                       | Poly1305 MAC            |
| Key derivation | SHA256(shared_x)           | HKDF with salt          |
| Nonce          | 16-byte IV, reused pattern | 24-byte random nonce    |
| Padding        | PKCS#7 (leaks length)      | Padded to power of 2    |
| Versioning     | None                       | Version byte prefix     |

**Encryption flow:**

1. **Conversation key:** Derive a stable key for each sender-recipient pair:
   ```
   shared_x = ECDH(sender_privkey, recipient_pubkey).x
   conversation_key = HKDF-SHA256(
     ikm = shared_x,
     salt = "nip44-v2",
     info = ""
   )
   ```

2. **Message keys:** For each message, generate a random 32-byte nonce and derive encryption/authentication keys:
   ```
   keys = HKDF-SHA256(
     ikm = conversation_key,
     salt = nonce,
     info = "nip44-v2"
   )
   chacha_key = keys[0:32]
   chacha_nonce = keys[32:44]
   hmac_key = keys[44:76]
   ```

3. **Pad plaintext:** Pad to the next power of 2 (minimum 32 bytes) to hide message length:
   ```
   padded = [length_u16_be] + [plaintext] + [zeros to next power of 2]
   ```

4. **Encrypt and authenticate:**
   ```
   ciphertext = XChaCha20(chacha_key, chacha_nonce, padded)
   mac = HMAC-SHA256(hmac_key, nonce + ciphertext)
   ```

5. **Format payload:**
   ```
   payload = [version=0x02] + [nonce] + [ciphertext] + [mac]
   content = base64(payload)
   ```

**Version byte:** The first byte (`0x02`) indicates the encryption version. This allows future upgrades without breaking existing messages. Version `0x01` was an earlier draft that was never widely deployed.

**Decryption:**

1. Decode base64, check version byte is `0x02`
2. Extract nonce (bytes 1-32), ciphertext, and MAC (last 32 bytes)
3. Derive conversation key using recipient's private key and sender's public key
4. Derive message keys from conversation key and nonce
5. Verify MAC before decrypting (reject if invalid)
6. Decrypt ciphertext, extract length prefix, return unpadded plaintext

**Security properties:**

- **Authenticated encryption:** Poly1305 MAC ensures any tampering is detected before decryption
- **Forward secrecy (partial):** Each message uses a unique nonce, so compromising one message doesn't reveal others. However, compromising a private key still reveals all past messages (no ratcheting).
- **Length hiding:** Power-of-2 padding obscures exact message length
- **Timing attack resistance:** Constant-time comparison for MAC verification

**Usage in practice:** NIP-44 is the encryption layer for:
- [NIP-17](/en/topics/nip-17/) private direct messages (inside gift wrap)
- [NIP-46](/en/topics/nip-46/) remote signer communication
- [NIP-59](/en/topics/nip-59/) seal encryption
- [Marmot Protocol](/en/topics/nip-104/) group messages, where NIP-44 wraps MLS-encrypted content using a key derived from the MLS exporter secret
- Any application needing secure point-to-point encryption

**Migration guidance:** New applications should use NIP-44 exclusively. For backward compatibility, check if a contact's client supports NIP-44 (via [NIP-89](/en/topics/nip-89/) app metadata or relay support) before falling back to NIP-04. When receiving messages, attempt NIP-44 decryption first, then fall back to NIP-04 for legacy content.

## Releases

**Primal Android v2.6.18** - [Full release](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18) adds [NIP-46](/en/topics/nip-46/) remote signing and [NIP-55](/en/topics/nip-55/) local signing, turning Primal into a signing hub for other Android apps. Performance improvements include media pre-caching, avatar pre-caching, and faster thread loading. Bug fixes address self-mentions in bios, media gallery crashes, and stream title fallbacks. On iOS, Primal uses background audio playback to keep the app alive for receiving NIP-46 signing requests; users can change the sound or mute it entirely in settings.

**Mostro v0.15.6** - The [NIP-69](/en/topics/nip-69/) P2P Bitcoin trading platform's [latest release](https://github.com/MostroP2P/mostro/releases/tag/v0.15.6) completes the development fund implementation with Phase 4 audit events. Dev fee payments are now tracked via kind 38383 Nostr events published after each successful payment, enabling third-party verification and analytics. Amount calculations were fixed for buyer/seller messages, and premium logic was aligned with the lnp2pbot reference implementation.

**Aegis v0.3.5** - The cross-platform signer [adds dark mode](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.5), improved app icon display, and cleaner UI layouts. Bug fixes address iOS iCloud Private Relay conflicts and event parsing issues. The release also improves how event JSON is passed to the Rust signing function.

**Citrine v1.0.0** - The Android relay app [reaches 1.0](https://github.com/greenart7c3/Citrine/releases/tag/v1.0.0). Citrine lets you run a personal Nostr relay directly on your Android device, useful for local caching, backup, or as a NIP-55 companion. This release adds a crash report handler, improves database query efficiency, and updates translations via Crowdin.

**Applesauce v5.0.0** - hzrd149's TypeScript library suite [ships a major version](https://github.com/hzrd149/applesauce/releases) with breaking changes focused on correctness and simplicity. The core package now [verifies event signatures by default](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%405.0.0) and renames coordinate methods to use clearer "address" terminology (`parseCoordinate` → `parseReplaceableAddress`). The relay package [lowers default retries from 10 to 3](https://github.com/hzrd149/applesauce/releases/tag/applesauce-relay%405.0.0) and ignores unreachable relays by default, plus adds `createUnifiedEventLoader` for simpler event fetching. The wallet package gains [NIP-87](/en/topics/nip-87/) [Cashu mint discovery](https://github.com/hzrd149/applesauce/releases/tag/applesauce-wallet%405.0.0). Direct `nostr-tools` dependencies were removed across packages, reducing bundle size and version conflicts.

## Notable code and documentation changes

*These are open pull requests and early-stage work, perfect for getting feedback before they merge. If something catches your eye, consider reviewing or commenting!*

### Damus (iOS)

A series of PRs improve the longform article experience. [Reading UX improvements](https://github.com/damus-io/damus/pull/3496) add a progress bar, estimated read time, sepia mode, adjustable line height, and focus mode that hides navigation while scrolling. [Image fixes](https://github.com/damus-io/damus/pull/3489) ensure images in markdown content display with proper aspect ratios by preprocessing standalone images as block-level elements. [Longform preview cards](https://github.com/damus-io/damus/pull/3497) replace inline `@naddr1...` text with rich preview cards showing article title and metadata. A new [relay integration test suite](https://github.com/damus-io/damus/pull/3508) adds 137 network-related tests including [NIP-01](/en/topics/nip-01/) protocol verification and behavior under degraded network conditions (3G simulation).

### Bitchat (Encrypted Messaging)

Security hardening in the iOS Nostr+Cashu messenger. [Noise protocol DH secret clearing](https://github.com/permissionlesstech/bitchat/pull/928) fixes six locations where shared secrets weren't being zeroed after Diffie-Hellman key agreement, restoring forward secrecy guarantees. [Thread safety for read receipt queues](https://github.com/permissionlesstech/bitchat/pull/929) adds barrier synchronization to prevent race conditions in NostrTransport. [Message deduplicator optimization](https://github.com/permissionlesstech/bitchat/pull/920) improves performance with high message volumes, and [hex string parsing hardening](https://github.com/permissionlesstech/bitchat/pull/919) prevents crashes from malformed input.

### Frostr (Threshold Signing)

The [FROST](/en/topics/frost/)-based threshold signing protocol [added QR code display](https://github.com/FROSTR-ORG/igloo-desktop/pull/62) for group credentials and share credentials during onboarding and in the signer interface. This enables easier setup when distributing key shares across multiple devices, letting users scan credentials instead of manually copying long strings.

### Marmot mdk (Library)

Beyond the security fixes mentioned above, active PRs address remaining audit findings: [Secret<T> type for zeroization](https://github.com/marmot-protocol/mdk/pull/109) introduces a wrapper type that automatically zeros sensitive data on drop, [messages query pagination](https://github.com/marmot-protocol/mdk/pull/111) prevents memory exhaustion when loading chat history, and [encrypted storage](https://github.com/marmot-protocol/mdk/pull/102) adds at-rest encryption for the SQLite database storing group state and messages.

### Amethyst (Android)

A busy week of stability fixes across the Android client. [Lenient JSON parsing](https://github.com/vitorpamplona/amethyst/commit/2c42796) prevents crashes from malformed events by making Kotlin Serialization more forgiving. Event validation now [checks kind field size](https://github.com/vitorpamplona/amethyst/commit/40f9622) before processing to avoid exceptions from oversized values. The trust score UI got a smaller icon to reduce visual interference, and [improved error logging](https://github.com/vitorpamplona/amethyst/commit/69c53ac) helps diagnose relay connection issues. Translation updates arrived via Crowdin, and several SonarQube warnings were addressed.

### TENEX (AI Agents)

The Nostr-native AI agent framework saw 81 commits this week building out autonomous capabilities. New [agent supervision system](https://github.com/tenex-chat/tenex/pull/48) implements behavioral heuristics to monitor agent actions and intervene when needed. [Delegation transparency](https://github.com/tenex-chat/tenex/commit/b244c10) adds user intervention logging to delegation transcripts, so users can audit what agents did on their behalf. The [LLM provider registry](https://github.com/tenex-chat/tenex/pull/47) was modularized for easier integration of different AI backends. Cross-project conversation support lets agents maintain context across multiple Nostr-based projects.

### Jumble (Web Client)

The relay-focused web client added several user experience improvements. [Smart relay pool](https://github.com/CodyTseng/jumble/commit/695f2fe) intelligently manages connections based on usage patterns. [Live feed toggle](https://github.com/CodyTseng/jumble/commit/917fcd9) lets users switch between real-time streaming and manual refresh. [Auto-show new notes](https://github.com/CodyTseng/jumble/commit/d1b3a8c) at top surfaces fresh content without requiring page reload. [Persistent cache](https://github.com/CodyTseng/jumble/commit/fd9f41c) for following feed and notifications improves load times on return visits. Users can now [change default relays](https://github.com/CodyTseng/jumble/commit/53a67d8) through settings.

---

That's it for this week. Building something? Have news to share? Want us to cover your project? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Reach out via NIP-17 DM</a> or find us on Nostr.
