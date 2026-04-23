---
title: "NIP-AC: P2P Voice and Video Calls"
date: 2026-04-08
translationOf: /en/topics/nip-ac.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Calling
  - WebRTC
description: "Definiert ein Protokoll für Peer-to-Peer-Sprach- und Videoanrufe mit Nostr für Signaling und WebRTC für den Medientransport."
---

NIP-AC schlägt ein Protokoll für Peer-to-Peer-Sprach- und Videoanrufe über Nostr vor. Die Spezifikation nutzt Nostr-Events für das Call-Signaling, also Offers, Answers und ICE Candidates, und WebRTC für den eigentlichen Medientransport. So bleibt das Call-Setup dezentral, während für Audio und Video Standard-Browser-APIs verwendet werden.

## Funktionsweise

Ein Caller veröffentlicht ein Call-Offer-Event, das ein WebRTC Session Description Protocol, SDP, Offer enthält und mit dem pubkey des Callee getaggt ist. Der Callee antwortet mit einem SDP-Answer-Event. Beide Seiten tauschen ICE-Candidate-Events aus, um den Netzwerkpfad auszuhandeln. Sobald die WebRTC-Verbindung steht, fließen die Medien direkt zwischen den Peers, ohne Relay-Beteiligung.

Die Signaling-Events sind verschlüsselt, sodass Relays nicht beobachten können, wer wen anruft. Die Call-State-Machine behandelt Übergänge für Offer, Answer, Reject, Busy und Hangup.

## Implementierungen

- [Amethyst](https://github.com/vitorpamplona/amethyst) baut NIP-AC-Unterstützung mit einer Testsuite für die Call-State-Machine und Handling für veraltete Call Offers.

---

**Primärquellen:**
- [NIP-AC PR #2301](https://github.com/nostr-protocol/nips/pull/2301) - P2P Voice and Video Calls over WebRTC

**Erwähnt in:**
- [Nostr Compass #17 (2026-04-08)](/de/newsletters/2026-04-08-newsletter/)

**Siehe auch:**
- [NIP-44 (Encrypted Payloads)](/de/topics/nip-44/)
