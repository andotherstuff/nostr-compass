---
title: "NIP-07: Browser Extension Signer"
date: 2026-01-28
draft: false
categories:
  - NIP
  - Signing
  - Security
---

NIP-07 defines a standard interface for browser extensions to provide signing capabilities to web-based Nostr clients, keeping private keys secure in the extension rather than exposing them to websites.

## How It Works

Browser extensions inject a `window.nostr` object that web apps can use:

```javascript
// Get public key
const pubkey = await window.nostr.getPublicKey();

// Sign an event
const signedEvent = await window.nostr.signEvent(unsignedEvent);

// Encrypt (NIP-04, legacy)
const ciphertext = await window.nostr.nip04.encrypt(pubkey, plaintext);

// Decrypt (NIP-04, legacy)
const plaintext = await window.nostr.nip04.decrypt(pubkey, ciphertext);

// NIP-44 methods (modern, if supported)
// const ciphertext = await window.nostr.nip44.encrypt(pubkey, plaintext);
// const plaintext = await window.nostr.nip44.decrypt(pubkey, ciphertext);
```

## Security Model

- **Key Isolation**: Private keys never leave the extension
- **User Approval**: Extensions can prompt for each signing request
- **Domain Control**: Extensions can restrict which sites can request signatures

NIP-07 improves key custody, but it does not remove trust from the extension itself. A malicious or compromised extension can still sign the wrong thing, leak metadata, or grant permissions too broadly.

## Interop Notes

The hardest part of NIP-07 is not the API shape. It is capability variation. Some extensions support only `getPublicKey()` and `signEvent()`. Others also expose `nip04`, `nip44`, or newer optional methods. Web apps need feature detection and reasonable fallbacks instead of assuming every injected signer behaves the same way.

User approval UX also changes behavior. A site that silently expects background access may work with one extension and feel broken with another that prompts on every request. Good NIP-07 apps treat signing as an interactive permission boundary.

## Implementation Status

Popular NIP-07 extensions include:
- **Alby** - Lightning wallet with Nostr signing
- **nos2x** - Lightweight Nostr signer
- **Flamingo** - Feature-rich Nostr extension

## Limitations

- Browser-only (no mobile support)
- Requires extension installation
- Each extension has different UX for approvals

For cross-device or mobile signing, NIP-46 and NIP-55 usually fit better.

---

**Primary sources:**
- [NIP-07 Specification](https://github.com/nostr-protocol/nips/blob/master/07.md)
- [PR #2233](https://github.com/nostr-protocol/nips/pull/2233) - `peekPublicKey()` proposal

**Mentioned in:**
- [Newsletter #7: NIP Updates](/en/newsletters/2026-01-28-newsletter/#nip-updates)
- [Newsletter #8: News](/en/newsletters/2026-02-04-newsletter/#news)
- [Newsletter #11: News](/en/newsletters/2026-02-25-newsletter/#news)

**See also:**
- [NIP-04: Encrypted Direct Messages (Deprecated)](/en/topics/nip-04/)
- [NIP-44: Encrypted Payloads](/en/topics/nip-44/)
- [NIP-46: Nostr Connect](/en/topics/nip-46/)
- [NIP-55: Android Signer Applications](/en/topics/nip-55/)
