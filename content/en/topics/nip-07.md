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

## Implementations

Popular NIP-07 extensions include:
- **Alby** - Lightning wallet with Nostr signing
- **nos2x** - Lightweight Nostr signer
- **Flamingo** - Feature-rich Nostr extension

## Limitations

- Browser-only (no mobile support)
- Requires extension installation
- Each extension has different UX for approvals

## Alternatives

- [NIP-46](/en/topics/nip-46/) - Remote signing via Nostr relays
- [NIP-55](/en/topics/nip-55/) - Android local signer

## Related

- [NIP-44](/en/topics/nip-44/) - Modern encryption (replacing NIP-04)
- [NIP-46](/en/topics/nip-46/) - Remote Signing
