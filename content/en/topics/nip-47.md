---
title: "NIP-47: Nostr Wallet Connect"
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
---

NIP-47 defines Nostr Wallet Connect, a protocol for letting a Nostr app talk to a remote Lightning wallet service without exposing the wallet's main credentials to every client.

## How It Works

A wallet service publishes a replaceable kind `13194` info event describing the methods and encryption modes it supports. A client connects using a `nostr+walletconnect://` URI that contains the wallet service pubkey, one or more relays, and a dedicated secret for that connection. Requests are sent as kind `23194` events and responses come back as kind `23195` events.

## Commands and Notifications

Common methods include `pay_invoice`, `pay_keysend`, `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance`, and `get_info`. Wallet services can also push notifications such as `payment_received`, `payment_sent`, and `hold_invoice_accepted`.

The spec originally grew several optional methods over time, but recent cleanup removed the `multi_` payment methods. In practice, interoperability is better when clients stick to the commands advertised by the wallet's info event instead of assuming a broad method set.

## Use Cases

- **Zapping** - Send sats to posts, profiles, or content creators
- **Payments** - Pay Lightning invoices from any Nostr app
- **Wallet UX separation** - Use one wallet service across many Nostr clients

## Security and Interop Notes

The connection URI contains a dedicated secret that the client uses for signing and encryption. That gives each app its own wallet identity, which helps both revocation and privacy. A wallet can cap spending, disable methods, or revoke one connection without affecting another.

NIP-44 is now the preferred encryption mode. The spec still documents NIP-04 fallback for older implementations, so clients need to inspect the wallet's advertised `encryption` tag instead of assuming every wallet has migrated.

---

**Primary sources:**
- [NIP-47 Specification](https://github.com/nostr-protocol/nips/blob/master/47.md)
- [PR #1913: Hold Invoice Support](https://github.com/nostr-protocol/nips/pull/1913)
- [PR #2210: Simplification](https://github.com/nostr-protocol/nips/pull/2210)

**Mentioned in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: Releases](/en/newsletters/2025-12-24-newsletter/#releases)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #8: NIP Deep Dive](/en/newsletters/2026-02-04-newsletter/#nip-deep-dive-nip-47-nostr-wallet-connect)
- [Newsletter #10: NIP Updates](/en/newsletters/2026-02-18-newsletter/#nip-updates)
- [Newsletter #13: Shopstr and Milk Market Open MCP Commerce Surfaces](/en/newsletters/2026-03-11-newsletter/#shopstr-and-milk-market-open-mcp-commerce-surfaces)

**See also:**
- [NIP-57: Zaps](/en/topics/nip-57/)
