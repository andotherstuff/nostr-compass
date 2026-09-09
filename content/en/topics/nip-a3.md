---
title: "NIP-A3: Payment Targets"
date: 2026-09-09
draft: false
categories:
  - Protocol
  - Payments
---

NIP-A3 defines a portable way for a Nostr account to publish payment addresses for multiple networks and services. A replaceable kind `10133` event carries one or more `payto` tags.

## How It Works

Each tag has the form `["payto", "<type>", "<address>"]`. The type is lowercase, such as `bitcoin`, `lightning`, or `monero`. Clients can validate known formats and render a native payment URI where one exists; unfamiliar types fall back to the `payto:` URI scheme from RFC 8905.

The event declares destinations, not a completed payment or a Nostr zap. Clients still decide which payment types they support, how to validate an address, and how clearly to show the destination before handing it to a wallet.

## Implementations

- [Amethyst](https://github.com/vitorpamplona/amethyst/pull/4041) offers an opt-in payment handoff when it recognizes a compatible target.
- [Grimoire](https://github.com/purrgrammer/grimoire/commit/54052506f7a0da06dfc4cf7e969331ee61be7851) maps allowed target types to payment URIs.
- [Pollerama](https://github.com/formstr-hq/nostr-polls/commit/5a015f1d17abecd036f3e10c88d493d23928fa98) validates Monero targets and queries the author's relays.

---

**Primary sources:**
- [NIP-A3 specification](https://github.com/nostr-protocol/nips/blob/master/A3.md)
- [RFC 8905: The payto URI Scheme](https://www.rfc-editor.org/rfc/rfc8905.html)

**Mentioned in:**
- [Newsletter #39: NIP-A3 payment targets reach three clients](/en/newsletters/2026-09-09-newsletter/#nip-a3-payment-targets-reach-three-clients)

**See also:**
- [NIP-47: Nostr Wallet Connect](/en/topics/nip-47/)
