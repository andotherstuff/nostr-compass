---
title: "NIP-45: Event-Zählung"
date: 2026-02-11
translationOf: /en/topics/nip-45.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-45 definiert, wie Clients Relays bitten können, Events zu zählen, die einem Filter entsprechen, ohne die Events selbst zu übertragen. Clients senden eine COUNT-Nachricht mit derselben Filtersyntax wie REQ, und Relays antworten mit einer Zählung.

## Funktionsweise

Ein Client sendet eine COUNT-Anfrage mit einer Subscription-ID und einem Filter:

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

Das Relay antwortet mit der Zählung:

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

Das vermeidet das Herunterladen von Hunderten oder Tausenden Events, nur um eine Zahl anzuzeigen.

## HyperLogLog Approximate Counting

Seit Februar 2026 unterstützt NIP-45 HyperLogLog (HLL) Approximate Counting ([PR #1561](https://github.com/nostr-protocol/nips/pull/1561)). Relays können 256-Byte HLL-Registerwerte zusammen mit COUNT-Antworten zurückgeben:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<base64 encoded 256 bytes>"}]
```

HLL löst ein grundlegendes Problem: das Zählen eindeutiger Events über mehrere Relays hinweg. Wenn Relay A 50 Reaktionen meldet und Relay B 40, ist die Gesamtzahl nicht 90, da viele Events auf beiden Relays existieren. HLL-Register von mehreren Relays können durch Übernahme des Maximalwerts an jeder Registerposition zusammengeführt werden, was automatisch netzwerkübergreifend dedupliziert.

Mit 256 Registern beträgt der Standardfehler ungefähr 5,2%. HyperLogLog++-Korrekturen verbessern die Genauigkeit bei kleinen Kardinalitäten unter ca. 200 Events. Schon zwei Reaktions-Events verbrauchen mehr Bandbreite als die 256-Byte-HLL-Payload, was dies für jede nicht-triviale Zählung effizient macht.

Die Spec fixiert die Registeranzahl auf 256 für Interoperabilität über alle Relay-Implementierungen hinweg.

## Anwendungsfälle

Soziale Metriken (Follower-Zahlen, Reaktionszahlen, Repost-Zahlen) sind die primäre Anwendung. Ohne HLL müssen Clients entweder ein einzelnes „vertrauenswürdiges" Relay für Zählungen abfragen (was die Daten zentralisiert) oder alle Events von allen Relays herunterladen, um lokal zu deduplizieren (was Bandbreite verschwendet). HLL liefert ungefähre relay-übergreifende Zählungen mit 256 Bytes Overhead pro Relay.

---

**Primärquellen:**
- [NIP-45: Event Counting](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561: HyperLogLog Relay Response](https://github.com/nostr-protocol/nips/pull/1561)

**Erwähnt in:**
- [Newsletter #9: NIP Deep Dive](/de/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-45-event-zählung-und-hyperloglog)
- [Newsletter #9: NIP-Updates](/de/newsletters/2026-02-11-newsletter/#nip-updates)

**Siehe auch:**
- [NIP-11: Relay-Informationsdokument](/de/topics/nip-11/)
