---
title: "NIP-BE: Bluetooth Low Energy"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Connectivity
---

NIP-BE specifies how Nostr applications can communicate and synchronize over Bluetooth Low Energy, enabling offline-capable apps to sync data across nearby devices without internet connectivity.

## GATT Structure

Uses a Nordic UART Service with two characteristics:
- **Write characteristic** - Client sends data to server
- **Read characteristic** - Server sends data to client (via notifications)

## Message Framing

BLE has small payload limits (20-256 bytes depending on version), so messages are:
- Compressed with DEFLATE
- Split into chunks with a 2-byte index and final-batch flag
- Limited to 64KB maximum size

## Role Negotiation

Devices compare advertised UUIDs on discovery:
- Higher UUID becomes GATT server (relay role)
- Lower UUID becomes GATT client
- Predetermined UUIDs exist for single-role devices

## Synchronization

Uses half-duplex communication with standard Nostr message types (`EVENT`, `EOSE`, `NEG-MSG`) to coordinate data sync across intermittent connections.

## Use Cases

- Offline event syncing between nearby devices
- Mesh-style message propagation without internet
- Backup connectivity when network is unavailable

---

**Primary sources:**
- [NIP-BE Specification](https://github.com/nostr-protocol/nips/blob/master/BE.md)

**Mentioned in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
