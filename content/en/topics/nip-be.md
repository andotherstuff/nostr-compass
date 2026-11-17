---
title: "NIP-BE: Bluetooth Low Energy"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Connectivity
---

NIP-BE specifies how Nostr applications can communicate and synchronize over Bluetooth Low Energy. It lets offline-capable apps sync data across nearby devices without internet connectivity.

## Current design

This section describes the accepted specification in the NIPs repository. It is labeled `draft`, `unrecommended` and `optional`. Its warning says it has only been implemented once, that it is unclear whether it works, and that it requires review. Open pull request #2544 proposes removing the `unrecommended` label. That change is not approved, and the label remains on the current specification.

### How it works

NIP-BE carries ordinary Nostr message frames over BLE and does not define a separate event model. Devices advertise a BLE service plus a device UUID. When two devices meet, they compare UUIDs: the device with the higher UUID becomes the GATT server (relay), and the other becomes the GATT client.

The GATT service uses a Nordic UART-style shape with one write characteristic and one read/notify characteristic. This keeps the transport simple for constrained mobile stacks while carrying ordinary Nostr messages.

### Message framing

BLE has small payload limits. NIP-BE compresses each message with DEFLATE, splits it into indexed chunks and sends one message at a time. Messages are capped at 64 KB, so the transport suits synchronization and local propagation, not bulk transfer.

### Sync model

After a connection is established, peers use a half-duplex sync flow based on [NIP-77](https://github.com/nostr-protocol/nips/blob/master/77.md) negentropy messages such as `NEG-OPEN`, `NEG-MSG`, `EVENT` and `EOSE`. Implementations can reuse existing relay-sync logic and do not need a BLE-only replication algorithm.

Half-duplex turn-taking fits intermittent short-range links, because each side knows whose turn it is to send.

### Local synchronization

NIP-BE gives Nostr applications a path for local-first networking. Two phones near each other can sync notes or relay state directly, even if neither has working internet. That makes BLE useful for censorship resistance, disaster scenarios and low-connectivity social apps.

BLE bandwidth is low, connections are short-lived and large histories do not fit well. NIP-BE suits incremental sync and nearby message spread, not full archival replication.

## Pending rewrite: PR #2544

Open pull request [#2544](https://github.com/nostr-protocol/nips/pull/2544) proposes rewriting NIP-BE. It is unmerged. Until a rewrite is merged, the design above is the accepted specification.

The proposed text would:

- Advertise only the service UUID `80E0688B-A648-4D1D-BB0D-BC58993CF926`, with no device UUID. The draft gives partial resistance to fingerprinting and tracking, plus iOS compatibility, as reasons.
- Run both GATT roles on every device and drop UUID-based role assignment.
- Open each session with a `Noise_XX_25519_ChaChaPoly_SHA256` handshake, using a fresh static key for every handshake to prevent passive tracking.
- Offer optional pairing, in which users compare a six-digit code derived from the handshake hash.
- Authenticate both devices with a modified NIP-42 exchange. Each device acts as a relay to the other, and the `relay` tag names the challenger's Noise static key from that handshake.
- Carry NIP-01 and NIP-77 messages as JSON in both directions on a sync channel, replacing the half-duplex flow.
- Move blobs on a separate channel, with optional Bao/BLAKE3 proofs for range fetches.
- Allow an optional L2CAP channel that shares the Noise session and framing, carries only blob traffic and falls back to GATT if the upgrade fails or the channel is lost.
- Replace DEFLATE chunking and the 64 KB cap with encrypted fragments and frames of up to 1 MiB.
- Remove the `unrecommended` label.

Removing the label is part of the proposal and is not approved. Deployment of the rewrite and an independent privacy review are not established in the reviewed evidence.

---

**Primary sources:**
- [NIP-BE Specification](https://raw.githubusercontent.com/nostr-protocol/nips/master/BE.md)
- [PR #1979](https://github.com/nostr-protocol/nips/pull/1979)
- [PR #2544: NIP-BE rewrite (open)](https://github.com/nostr-protocol/nips/pull/2544)

**Mentioned in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #49](/en/newsletters/2026-11-18-newsletter/#nostr-protocol-nips-2544)

**See also:**
- [NIP-01: Basic Protocol](/en/topics/nip-01/)
- [Noise Protocol Framework](/en/topics/noise/)
- [NIP-42: Client authentication](/en/topics/nip-42/)
- [NIP-77: Negentropy syncing](/en/topics/nip-77/)
