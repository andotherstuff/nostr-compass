---
title: "TollGate: Pay-per-use Internet Over Nostr and Cashu"
date: 2026-04-22
draft: false
categories:
  - Protocols
---

TollGate is a protocol for selling network access in exchange for small, frequent bearer asset payments. A device that can gate connectivity, such as a WiFi router, an Ethernet switch, or a Bluetooth tether, acts as a TollGate that advertises pricing, accepts [Cashu](/en/topics/cashu/) ecash tokens, and manages sessions. Customers pay for exactly the minutes or megabytes they consume. There are no accounts, no subscriptions, no KYC.

## How It Works

TollGate separates concerns into three layers. The protocol layer defines the event shapes and payment semantics. The interface layer defines how customer and gate exchange those events. The medium layer describes the physical link carrying the paid-for traffic. A working TollGate combines one spec from each layer, and some interfaces run over Nostr relays while others run over plain HTTP.

At the protocol layer, [TIP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md) defines three base events: an Advertisement kind that lists prices and accepted mints, a Session kind that tracks how much the customer has paid for and how much they have consumed, and a Notice kind for out-of-band messaging. [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md) layers Cashu payments on top, so a customer can redeem ecash tokens from any mint the TollGate advertises and receive session credit in return.

At the interface layer, [HTTP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/HTTP-01.md) through HTTP-03 define the HTTP surface for devices on restrictive operating systems that cannot easily open WebSocket connections to arbitrary relays, and [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md) defines the Nostr-relay transport for clients that can. At the medium layer, [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md) describes how a captive-portal WiFi setup identifies and routes paying customers.

Because the payment asset is a bearer token rather than a credential, the customer does not need prior internet access to produce it. A Cashu token sitting in a local wallet is sufficient on its own to buy the first minute of connectivity, at which point the customer can top up with more tokens as needed. TollGates may also buy uplink from each other, so reach extends beyond a single operator.

## Why It Matters

Conventional paid WiFi relies on accounts, captive portals, and payment cards, each of which creates friction and a data trail. TollGate's model turns connectivity into a commodity that any router can sell to any paying customer without knowing who they are. The abstraction lets independent operators set their own prices, accept their own preferred mints, and compete on coverage and quality rather than on lock-in.

The [v0.1.0 release](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0) is the first tagged snapshot of these specifications. It does not standardize every detail but fixes enough of the surface that router firmware, client wallets, and multi-hop resellers can start building against a stable reference.

---

**Primary sources:**
- [TollGate v0.1.0 release](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)
- [TIP-01: Base Events](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md)
- [TIP-02: Cashu payments](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md)
- [HTTP-01 through HTTP-03](https://github.com/OpenTollGate/tollgate/tree/v0.1.0)
- [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md)
- [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md)
- [TollGate repository](https://github.com/OpenTollGate/tollgate)

**Mentioned in:**
- [Newsletter #19: TollGate v0.1.0](/en/newsletters/2026-04-22-newsletter/#tollgate-v010-stabilizes-pay-per-use-internet-over-nostr-and-cashu)

**See also:**
- [Cashu](/en/topics/cashu/)
- [NIP-60: Cashu Wallet](/en/topics/nip-60/)
