---
title: "NIP-66: Relay Discovery and Liveness Monitoring"
date: 2026-01-21
draft: false
categories:
  - NIPs
  - Relays
---

NIP-66 standardizes publishing relay monitoring data to Nostr. Monitor services continuously test relays for availability, latency, protocol compliance, and supported NIPs, publishing results as kind 30166 events.

## How It Works

Monitors check relay availability by connecting and sending test subscriptions. Latency measurements track connection time, subscription response time, and event propagation delay. Protocol compliance testing verifies relay behavior matches specifications, catching implementation bugs or intentional deviations.

NIP support verification goes beyond [NIP-11](/en/topics/nip-11/) claims by actually testing whether advertised features work correctly. If a relay claims [NIP-50](/en/topics/nip-50/) search support but search queries fail, monitors will omit NIP-50 from the verified list. This provides ground truth about relay capabilities.

Kind 30166 events use the relay URL as the `d` tag, making them parameterized replaceable events. Each monitor publishes one event per relay, updated as measurements change. Multiple monitors can track the same relay, providing redundancy and cross-validation.

Round-trip time (rtt) tags measure latency for different operations:
- `rtt open`: WebSocket connection establishment
- `rtt read`: Subscription response time
- `rtt write`: Event publication speed

All values are in milliseconds. Clients use these metrics to prefer low-latency relays for time-sensitive operations.

Geographic information helps clients select nearby relays for better latency and censorship resistance. The `geo` tag contains country code, country name, and region. The `network` tag distinguishes clearnet relays from Tor hidden services or I2P endpoints.

## Use Cases

Monitor data powers relay selectors in clients, explorer websites, and trust evaluation systems. By providing real-time relay status independent of relay self-reporting, NIP-66 enables informed relay selection.

Combined with [NIP-11](/en/topics/nip-11/) (self-reported capabilities) and Trusted Relay Assertions (trust evaluation), the ecosystem moves toward data-driven relay selection rather than relying on hardcoded defaults.

---

**Primary sources:**
- [NIP-66 Specification](https://github.com/nostr-protocol/nips/blob/master/66.md) - Relay discovery and liveness monitoring standard

**Mentioned in:**
- [Newsletter #6: NIP Deep Dive](/en/newsletters/2026-01-21-newsletter/#nip-deep-dive-nip-11-and-nip-66)

**See also:**
- [NIP-11: Relay Information Document](/en/topics/nip-11/)
- [Trusted Relay Assertions](/en/topics/trusted-relay-assertions/)
