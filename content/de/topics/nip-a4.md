---
title: "NIP-A4: Öffentliche Nachrichten"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
---

NIP-A4 definiert öffentliche Nachrichten (Kind 24), die für Benachrichtigungsbildschirme konzipiert sind, mit breiter Client-Unterstützung als Ziel.

## Funktionsweise

Im Gegensatz zu Thread-Konversationen haben diese Nachrichten kein Konzept von Chat-Verlauf oder Nachrichtenketten. Sie sind einfache Einzelnachrichten, die im Benachrichtigungs-Feed eines Empfängers erscheinen sollen.

## Struktur

- Verwendet `q`-Tags (Zitate) anstelle von `e`-Tags, um Threading-Komplikationen zu vermeiden
- Kein Konversationszustand oder -verlauf
- Konzipiert für einfache öffentliche Benachrichtigungen

## Anwendungsfälle

- Öffentliche Anerkennungen oder Shoutouts
- Broadcast-Nachrichten an einen Benutzer
- Benachrichtigungen, die kein Antwort-Threading benötigen

---

**Primärquellen:**
- [NIP-A4 PR](https://github.com/nostr-protocol/nips/pull/1988)

**Erwähnt in:**
- [Newsletter #2: NIP-Updates](/de/newsletters/2025-12-24-newsletter/#nip-updates)

**Siehe auch:**
- [NIP-01: Basisprotokoll](/de/topics/nip-01/)
- [NIP-10: Textnotiz-Threading](/de/topics/nip-10/)
