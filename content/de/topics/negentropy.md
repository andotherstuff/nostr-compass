---
title: "Negentropy: Set-Reconciliation-Protokoll"
date: 2026-01-28
translationOf: /en/topics/negentropy.md
translationDate: 2026-01-28
draft: false
categories:
  - Protocol
  - Sync
---

Negentropy ist ein Set-Reconciliation-Protokoll, das eine effiziente Synchronisierung zwischen Nostr-Clients und Relays ermöglicht, indem fehlende Events identifiziert werden, ohne den gesamten Datensatz zu übertragen.

## Funktionsweise

Anstatt alle Events anzufordern, die einem Filter entsprechen, ermöglicht negentropy Clients, ihr lokales Event-Set mit dem Set eines Relays zu vergleichen und nur die Unterschiede zu identifizieren. Dies wird durch ein mehrrundiges Protokoll erreicht:

1. **Fingerprinting**: Client und Relay berechnen jeweils einen Fingerprint ihrer Event-Sets
2. **Vergleich**: Fingerprints werden ausgetauscht und verglichen
3. **Reconciliation**: Nur fehlende Event-IDs werden identifiziert und übertragen

## Bedeutung

Traditionelle Nostr-Synchronisierung verwendet zeitstempelbasierte `since`-Filter, die Events verpassen können aufgrund von:
- Uhrendrift zwischen Client und Relay
- Mehreren Events mit identischen Zeitstempeln
- Events, die außer der Reihe ankommen

Negentropy löst diese Probleme, indem tatsächliche Event-Sets verglichen werden, anstatt sich auf Zeitstempel zu verlassen.

## Anwendungsfälle

- **DM-Wiederherstellung**: Clients können fehlende Direktnachrichten erkennen und abrufen, auch mit alten Zeitstempeln
- **Feed-Synchronisierung**: Gewährleistet vollständige Timeline-Synchronisierung über Relays hinweg
- **Offline-Synchronisierung**: Effizientes Aufholen nach Zeiten der Trennung

## Implementierung

Negentropy erfordert Relay-Unterstützung. Clients implementieren es typischerweise als Fallback-Wiederherstellungsmechanismus anstatt Standard-REQ-Subscriptions zu ersetzen und degradieren elegant, wenn Relays das Protokoll nicht unterstützen.

## Verwandt

- [NIP-01](/de/topics/nip-01/) - Grundprotokoll
