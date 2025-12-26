---
title: "NIP-18: Reposts"
date: 2025-12-17
draft: false
categories:
  - Social
  - Protocol
---

NIP-18 definiert, wie Events repostet werden, ähnlich wie Retweets auf anderen Plattformen.

## Struktur

Ein Repost ist ein Kind-6-Event (für Kind-1-Notizen) oder Kind 16 (generischer Repost), das Folgendes enthält:
- `e`-Tag, das auf das repostete Event verweist
- `p`-Tag, das auf den ursprünglichen Autor verweist
- Optional das vollständige Original-Event im `content`-Feld

## Aktuelle Änderungen

Verbesserte Unterstützung für das Reposten von ersetzbaren Events mit `a`-Tag-Unterstützung. Dies ermöglicht es Reposts von adressierbaren Events (Kinds 30000-39999), diese über ihre Adresse statt einer spezifischen Event-ID zu referenzieren.

---

**Primärquellen:**
- [NIP-18 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/18.md)

**Erwähnt in:**
- [Newsletter #1: NIP-Updates](/de/newsletters/2025-12-17-newsletter/#nip-updates)

**Siehe auch:**
- [NIP-01: Basisprotokoll](/de/topics/nip-01/)
