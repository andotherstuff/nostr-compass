---
title: "NIP-77: Negentropy-Abgleich"
date: 2026-05-14
draft: false
translationOf: /en/topics/nip-77.md
translationDate: 2026-05-13
categories:
  - NIPs
  - Sync
---

NIP-77 definiert, wie Nostr-Relays und Clients das [Negentropy](/de/topics/negentropy/)-Set-Abgleichprotokoll nutzen, um Event-Mengen effizient zu synchronisieren – sie finden heraus, welche Events auf jeder Seite fehlen, ohne den gesamten Datensatz erneut zu übertragen.

## Funktionsweise

Der Negentropy-Abgleich läuft über eine WebSocket-Verbindung mit einem dedizierten Nachrichtentyp. Client und Relay tauschen kompakte Bereichs-Fingerabdrücke über ihre sortierten Event-Mengen aus und grenzen dabei nur die unterschiedlichen Bereiche ein. Sobald die Unterschiede identifiziert sind, werden nur die fehlenden Event-IDs (und dann die fehlenden Events selbst) übertragen.

NIP-77 standardisiert das Nachrichten-Framing, damit jeder Client und jedes Relay, das die Spezifikation implementiert, eine effiziente Synchronisationssitzung aushandeln kann. Das Protokoll verwendet die Nachrichtentypen `NEG-OPEN`, `NEG-MSG` und `NEG-CLOSE` über die bestehende Nostr-WebSocket-Verbindung.

## Warum das wichtig ist

Herkömmliche Nostr-Synchronisation verwendet zeitstempelbasierte `since`-Filter, die Events aufgrund von Uhrabweichungen, Events mit identischen Zeitstempeln oder außer der Reihe eintreffenden Events verpassen können. Negentropy vergleicht tatsächliche Event-Mengen statt sich auf Zeitstempel zu verlassen und liefert eine nachweislich vollständige Synchronisation in deutlich weniger Roundtrips als einfaches Polling.

Dies ist besonders nützlich für:
- Mobile Clients, die nach dem Offline-Gang aufholen
- Relay-zu-Relay-Replikation
- Lokale Relay-Synchronisation (wie im Relay-Aggregator von Citrine)

## Implementierungen

- [Citrine](https://github.com/greenart7c3/Citrine) — [PR #139](https://github.com/greenart7c3/Citrine/pull/139) fügte NIP-77-Unterstützung für effizienten Set-Abgleich im Android-Relay-Knoten hinzu
- [strfry](https://github.com/hoytech/strfry) — relay-seitige Negentropy-Unterstützung
- [nostr-tools](https://github.com/nbd-wtf/nostr-tools) — clientseitige Negentropy-Implementierung

---

**Primäre Quellen:**
- [NIP-77-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/77.md)
- [Negentropy-Protokoll](https://github.com/hoytech/negentropy)

**Erwähnt in:**
- [Newsletter #22: Citrine v3.0.0-pre1](/de/newsletters/2026-05-14-newsletter/#citrine-v300-pre1-lands-built-in-tor-and-relay-aggregation)

**Siehe auch:**
- [Negentropy](/de/topics/negentropy/)
