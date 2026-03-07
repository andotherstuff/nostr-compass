---
title: "NIP-45: Event-Zählung"
date: 2026-02-11
translationOf: /en/topics/nip-45.md
translationDate: 2026-03-07
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-45 definiert, wie Clients Relays bitten können, Events zu zählen, die einem Filter entsprechen, ohne die passenden Events selbst zu übertragen. Es verwendet die Filtersyntax aus NIP-01 erneut, sodass ein Client eine bestehende `REQ` oft mit denselben Filtern in eine `COUNT`-Anfrage umwandeln kann.

## Wie es funktioniert

Ein Client sendet eine `COUNT`-Anfrage mit einer Subscription-ID und einem Filter:

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

Das Relay antwortet mit einer Anzahl:

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

Das vermeidet das Herunterladen von Hunderten oder Tausenden Events, nur um eine Zahl anzuzeigen. Wenn ein Client mehrere Filter in einer `COUNT`-Anfrage sendet, fasst das Relay sie zu einem einzigen Ergebnis zusammen, genau wie mehrere `REQ`-Filter per OR verknüpft werden.

## HyperLogLog Approximate Counting

Seit Februar 2026 unterstützt NIP-45 HyperLogLog, kurz HLL, für approximative Zählungen ([PR #1561](https://github.com/nostr-protocol/nips/pull/1561)). Relays können ein Ergebnis als approximativ kennzeichnen und für relay-übergreifende Deduplizierung 256 HLL-Register zusammen mit der Zahl zurückgeben:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<512-char hex string>"}]
```

HLL löst ein grundlegendes Problem: das Zählen eindeutiger Events über mehrere Relays hinweg. Wenn Relay A 50 Reaktionen meldet und Relay B 40, ist die Gesamtzahl nicht 90, weil viele Events auf beiden Relays existieren. Clients führen HLL-Werte zusammen, indem sie an jeder Registerposition den Maximalwert übernehmen. Das liefert eine netzwerkweite Schätzung, ohne die Roh-Events herunterzuladen.

Die Spezifikation legt die Registerzahl aus Interoperabilitätsgründen auf 256 fest. Dadurch bleibt die Payload klein, und Caching auf Relay-Seite bleibt praktikabel, weil jedes Relay für denselben geeigneten Filter dasselbe Registerlayout berechnet.

## Interop-Hinweise

HLL ist nur für Filter mit einem Tag-Attribut definiert, weil der Offset für den Aufbau der Register aus dem ersten getaggten Wert im Filter abgeleitet wird. Die Spezifikation nennt auch einen kleinen Satz kanonischer Abfragen, darunter Reaktionen, Reposts, Quotes, Replies, Kommentare und Follower-Zahlen. Diese Zählungen lassen sich für Relays am leichtesten vorberechnen oder cachen.

## Warum es wichtig ist

Follower-Zahlen, Reaktionszahlen und Reply-Zahlen sind die wichtigsten Anwendungsfälle. Ohne NIP-45 müssen Clients entweder der lokalen Sicht eines einzelnen Relays vertrauen oder alle passenden Events herunterladen und selbst deduplizieren. NIP-45 verlagert das Zählen ins Relay, und HLL macht relay-übergreifende Zählungen praktikabel, ohne ein einzelnes Relay zur Autorität zu machen.

---

**Primärquellen:**
- [NIP-45: Event Counting](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561: HyperLogLog Relay Response](https://github.com/nostr-protocol/nips/pull/1561)

**Erwähnt in:**
- [Newsletter #9: NIP Deep Dive](/en/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-45-event-counting-and-hyperloglog)
- [Newsletter #9: NIP Updates](/en/newsletters/2026-02-11-newsletter/#nip-updates)
- [Newsletter #12: Five Years of Nostr Februaries](/en/newsletters/2026-03-04-newsletter/)

**Siehe auch:**
- [NIP-11: Relay Information Document](/de/topics/nip-11/)
