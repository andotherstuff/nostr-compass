---
title: "NIP-63: Paywall / Premium-Inhalte"
date: 2025-12-17
translationOf: /en/topics/nip-63.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Monetization
---

NIP-63 ist ein vorgeschlagener Standard für den Umgang mit zugangsbeschränkten Inhalten im Nostr-Protokoll. Er erlaubt es Creators, eine Zahlung zu verlangen, bevor Inhalte freigeschaltet werden.

## Funktionsweise

Creators können Events veröffentlichen, bei denen der volle Inhalt verschlüsselt ist oder hinter einer Paywall liegt. Nach erfolgreicher Zahlungsprüfung wird der Inhalt für den zahlenden Nutzer freigeschaltet.

Der Vorschlag bezieht sich bewusst auf die Protokolloberfläche für Premium-Inhalte und schreibt weder einen einzelnen Payment Rail noch ein bestimmtes Geschäftsmodell vor. Das hält ihn flexibel, bedeutet aber auch, dass Wallets, Clients und Publisher sich in der Praxis immer noch auf einen gemeinsamen Unlock-Flow einigen müssen.

## Warum das wichtig ist

Ohne gemeinsames Format wird jedes Nostr-Paywall-System zu seinem eigenen Silo. Ein gemeinsames NIP würde es ermöglichen, dass ein Client Premium-Inhalte veröffentlicht und ein anderer erkennt, dass die Inhalte gesperrt sind, was bezahlt werden muss und wann sie sichtbar werden sollten.

Das garantiert noch keine Portabilität. NIP-63 ist weiterhin ein Vorschlag in [PR #2156](https://github.com/nostr-protocol/nips/pull/2156), daher können Implementierungen während der laufenden Diskussion noch voneinander abweichen.

## Anwendungsfälle

- Nur für Abonnenten verfügbare Artikel
- Premium-Medieninhalte
- Pay-per-view-Events
- Exklusiver Zugang zu Creators

## Abwägungen

Paywall-Metadaten können öffentlich sein, auch wenn der Premium-Payload es nicht ist. Das gibt Clients genug Informationen, um ein Angebot darzustellen, macht aber zugleich für jeden sichtbar, dass es bezahlte Inhalte gibt.

Creators müssen auch bedenken, was nach dem Unlock passiert. Sobald Klartext einem zahlenden Nutzer angezeigt wird, kann das Protokoll nicht verhindern, dass dieser ihn anderswo kopiert.

---

**Primärquellen:**
- [NIP-63 Proposal (PR #2156)](https://github.com/nostr-protocol/nips/pull/2156)

**Erwähnt in:**
- [Newsletter #1: NIP Updates](/de/newsletters/2025-12-17-newsletter/#nip-updates)

**Siehe auch:**
- [NIP-57: Zaps](/de/topics/nip-57/)
