---
title: "NIP-91: AND-Operator für Filter"
date: 2026-03-04
translationOf: /en/topics/nip-91.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - Protocol
---

NIP-91 ergänzt AND-Filtersemantik für Tag-Arrays in Relay-Subscriptions von Nostr. Es wurde am 2026-03-03 gemergt, nachdem bereits mehrere Relays Implementierungen veröffentlicht hatten.

## Das Problem

Das Filtersystem von Nostr in [NIP-01](/de/topics/nip-01/) kombiniert mehrere Werte innerhalb eines einzelnen Tag-Filters mit OR-Logik. Wenn ein Client in einem Filter zwei Werte für ein `p`-Tag angibt, liefert das Relay Events zurück, die auf einen der beiden Pubkeys passen. Es gab bisher keine Möglichkeit, gezielt Events anzufragen, die auf beide Pubkeys zugleich verweisen.

Dadurch mussten Clients zu viele Events von Relays laden und lokal nachfiltern, was Bandbreite und Verarbeitungszeit erhöht.

## Funktionsweise

NIP-91 führt AND-Semantik für Tag-Arrays ein. Wenn ein Client Events braucht, die auf alle angegebenen Tag-Werte passen, kann er statt des Standardverhaltens mit Vereinigungsmenge ein Schnittmengen-Matching anfordern.

Das ist wichtig für Anfragen wie "Events, die beide Teilnehmer einer Unterhaltung taggen" oder "Events, die zwei erforderliche Labels gleichzeitig tragen". Vor dieser Änderung konnten Relays nur die größere Obermenge liefern und den präzisen Schnitt dem Client überlassen.

## Warum das wichtig ist

AND-Filter machen Relay-seitige Indizes nützlicher. Clients können ein Relay nach einem kleineren, bereits relevanten Ergebnisbestand fragen. Das reduziert Bandbreite und lokale Nachverarbeitung. Am stärksten fällt das bei mobilen Clients und bei Abfragen über große, taglastige Datensätze auf.

## Interop-Hinweise

Zum Zeitpunkt des Merges gab es funktionierende Implementierungen in nostr-rs-relay, satellite-node, worker-relay und applesauce. Der Vorschlag trug früher die Nummer NIP-119, bevor er umnummeriert wurde.

Clients sollten vorerst weiter mit gemischter Unterstützung rechnen, während sich die Relay-Adoption erst verbreitet. Ein praktikabler Fallback ist, den alten clientseitigen Schnittmengenpfad für Relays beizubehalten, die die neue Semantik noch nicht implementiert haben.

---

**Primärquellen:**
- [PR #1365](https://github.com/nostr-protocol/nips/pull/1365)

**Erwähnt in:**
- [Newsletter #12: NIP Updates](/de/newsletters/2026-03-04-newsletter/#nip-updates)

**Siehe auch:**
- [NIP-01: Basic Protocol](/de/topics/nip-01/)
