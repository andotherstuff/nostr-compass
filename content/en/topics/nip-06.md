---
title: "NIP-06: Mnemonic Key Derivation"
date: 2026-10-28
draft: false
categories: ["Identity", "Keys"]
---

NIP-06 describes how to derive a Nostr key pair from a mnemonic seed phrase. The [current official NIP-06 text](https://github.com/nostr-protocol/nips/blob/master/06.md) is marked draft and optional, and it carries this warning:

> __Warning__ `unrecommended`: prefer a single nsec

This page covers NIP-06 for historical compatibility. It does not recommend adopting seed derivation.

## How it works

According to the [current specification](https://github.com/nostr-protocol/nips/blob/master/06.md), BIP39 is used to generate the mnemonic words and to derive a binary seed from them. BIP32 then derives keys along the path `m/44'/1237'/<account>'/0/0`, where 1237 is the Nostr entry in SLIP44. A basic client can use account 0. Incrementing the account value yields other keys from the same seed. Two implementations reproduce the same identity only when they agree on the derivation steps and use the correct encodings for the result.

## Test vectors

An [October 12, 2023 commit](https://github.com/nostr-protocol/nips/commit/202e18f2b256646148805880ed58731c1c8b2b9b) added two test vectors, one built from a 12-word mnemonic and one from a 24-word mnemonic. Each lists the expected private key and public key in hex, along with the matching nsec and npub encodings. Developers can use the vectors to cross-check implementations. The vectors say nothing about key custody, do not certify security, and do not guarantee universal interoperability.

## See also

- [NIP-01](/en/topics/nip-01/)

**Primary sources:**

- [NIP-06 (current)](https://github.com/nostr-protocol/nips/blob/master/06.md)
- [Commit adding NIP-06 test vectors (October 12, 2023)](https://github.com/nostr-protocol/nips/commit/202e18f2b256646148805880ed58731c1c8b2b9b)

**Mentioned in:**

- [Newsletter #46](/en/newsletters/2026-10-28-newsletter/#october-2023-events-carry-evidence-and-requests-for-work)
