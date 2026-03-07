---
title: "NIP-BE: Bluetooth Low Energy"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Connectivity
---

NIP-BE specifies how Nostr applications can communicate and synchronize over Bluetooth Low Energy, enabling offline-capable apps to sync data across nearby devices without internet connectivity.

## How It Works

NIP-BE reuses normal Nostr message frames over BLE instead of inventing a separate event model. Devices advertise a BLE service plus a device UUID, compare UUIDs when they meet, and deterministically decide which side becomes the GATT server and which side becomes the GATT client.

The GATT service uses a Nordic UART-style shape with one write characteristic and one read/notify characteristic. That keeps the transport simple enough for constrained mobile stacks while still carrying ordinary Nostr messages.

## Message Framing

BLE has small payload limits, so NIP-BE compresses messages with DEFLATE, splits them into indexed chunks, and sends only one message at a time. The spec caps messages at 64 KB, which is a useful reminder that this transport is for synchronization and local propagation, not bulk transfer.

## Sync Model

After a connection is established, peers use a half-duplex sync flow based on [NIP-77](https://github.com/nostr-protocol/nips/blob/master/77.md) negentropy messages such as `NEG-OPEN`, `NEG-MSG`, `EVENT`, and `EOSE`. That design choice matters because it lets implementations reuse existing relay-sync logic instead of building a BLE-only replication algorithm.

The half-duplex rule also reflects the reality of flaky BLE links. Intermittent short-range connections work better when each side knows exactly whose turn it is to speak.

## Why It Matters

NIP-BE gives Nostr applications a path for local-first networking. Two phones can sync notes or relay state directly when they are near each other, even if neither has working internet. That makes BLE useful for censorship resistance, disaster scenarios, and low-connectivity social apps.

The constraints are equally important: BLE bandwidth is low, connections are short-lived, and large histories do not fit well. In practice, NIP-BE is best for incremental sync and nearby message spread, not full archival replication.

---

**Primary sources:**
- [NIP-BE Specification](https://github.com/nostr-protocol/nips/blob/master/BE.md)
- [PR #1979](https://github.com/nostr-protocol/nips/pull/1979)

**Mentioned in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**See also:**
- [NIP-01: Basic Protocol](/en/topics/nip-01/)
