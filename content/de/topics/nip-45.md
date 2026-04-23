---
title: "NIP-45: Event Counting"
date: 2026-02-11
translationOf: /en/topics/nip-45.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-45 definiert, wie Clients Relays bitten können, Events zu zählen, die einem Filter entsprechen, ohne die passenden Events selbst zu übertragen. Es verwendet die Filtersyntax aus NIP-01 erneut, sodass ein Client eine bestehende `REQ` oft mit denselben Filtern in eine `COUNT`-Anfrage umwandeln kann.

## Funktionsweise

Ein Client sendet eine `COUNT`-Anfrage mit einer Subscription-ID und einem Filter:

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

Das Relay antwortet mit einer Zahl:

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

So muss der Client nicht Hunderte oder Tausende Events herunterladen, nur um eine Zahl anzuzeigen. Wenn ein Client mehrere Filter in einer `COUNT`-Anfrage sendet, aggregiert das Relay sie zu einem einzigen Ergebnis, so wie mehrere `REQ`-Filter per OR verknüpft werden.

## HyperLogLog Approximate Counting

Seit Februar 2026 unterstützt NIP-45 approximative Zählung mit HyperLogLog, HLL, ([PR #1561](https://github.com/nostr-protocol/nips/pull/1561)). Relays können ein Ergebnis als approximativ markieren und für relay-übergreifende Deduplizierung zusätzlich zu der Zahl 256 HLL-Register zurückgeben:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<512-char hex string>"}]
```

HLL löst ein fundamentales Problem: das Zählen eindeutiger Events über mehrere Relays hinweg. Wenn Relay A 50 Reaktionen meldet und Relay B 40, ist die Gesamtzahl nicht 90, weil viele Events auf beiden Relays existieren. Clients führen HLL-Werte zusammen, indem sie an jeder Registerposition den Maximalwert übernehmen. So entsteht eine netzwerkweite Schätzung, ohne die Roh-Events herunterladen zu müssen.

Die Spezifikation legt die Registeranzahl aus Interoperabilitätsgründen auf 256 fest. Das hält die Payload klein und macht Caching auf Relay-Seite praktikabel, weil jedes Relay für denselben geeigneten Filter dasselbe Registerlayout berechnet.

## Interop-Hinweise

HLL ist nur für Filter mit einem Tag-Attribut definiert, weil der Offset zum Aufbau der Register aus dem ersten getaggten Wert im Filter abgeleitet wird. Die Spezifikation nennt außerdem einen kleinen Satz kanonischer Queries, darunter Reaktionen, Reposts, Quotes, Replies, Kommentare und Follower-Zahlen. Diese Zählungen lassen sich für Relays am leichtesten vorberechnen oder cachen.

## Warum das wichtig ist

Follower-Zahlen, Reaktionszahlen und Reply-Zahlen sind die wichtigsten Anwendungsfälle. Ohne NIP-45 müssen Clients entweder der lokalen Sicht eines einzelnen Relays vertrauen oder alle passenden Events herunterladen und lokal deduplizieren. NIP-45 hält das Zählen innerhalb des Relays, und HLL macht relay-übergreifende Zählungen praktikabel, ohne ein einzelnes Relay zur Autorität zu machen.

---

## Implementierungen

- [nostream](https://github.com/Cameri/nostream) fügte in [PR #522](https://github.com/Cameri/nostream/pull/522) `COUNT`-Support hinzu, sodass Clients erfragen können, wie viele Events zu einem Filter passen, ohne sie abzurufen.

---

**Primärquellen:**
- [NIP-45: Event Counting](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561: HyperLogLog Relay Response](https://github.com/nostr-protocol/nips/pull/1561)
- [nostream PR #522](https://github.com/Cameri/nostream/pull/522) - NIP-45 COUNT support

**Erwähnt in:**
- [Newsletter #9: NIP Deep Dive](/de/newsletters/2026-02-11-newsletter/)
- [Newsletter #9: NIP Updates](/de/newsletters/2026-02-11-newsletter/)
- [Newsletter #12: Five Years of Nostr Februaries](/de/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: nostream NIP-45 support](/en/newsletters/2026-04-22-newsletter/)

**Siehe auch:**
- [NIP-11: Relay Information Document](/de/topics/nip-11/)
