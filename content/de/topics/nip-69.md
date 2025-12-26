---
title: "NIP-69: Peer-to-Peer-Handel"
date: 2025-12-17
draft: false
categories:
  - Trading
  - Protocol
---

NIP-69 definiert ein Protokoll für Peer-to-Peer-Handel über Nostr, das ein einheitliches Orderbuch über mehrere Plattformen hinweg schafft, anstatt fragmentierte Liquiditätspools.

## Event Kind

- **Kind 38383** - P2P-Order-Events

## Order-Struktur

Orders verwenden Tags zur Spezifizierung von Handelsparametern:

- `d` - Order-ID
- `k` - Order-Typ (Kauf/Verkauf)
- `f` - Fiat-Währung (ISO 4217-Code)
- `amt` - Bitcoin-Betrag in Satoshis
- `fa` - Fiat-Betrag
- `pm` - Akzeptierte Zahlungsmethoden
- `premium` - Preisaufschlag/-abschlag in Prozent
- `network` - Abwicklungsschicht (Onchain, Lightning, Liquid)
- `expiration` - Wann die Order abläuft

## Order-Lebenszyklus

Orders durchlaufen verschiedene Status:
- `pending` - Offen und zur Zuordnung verfügbar
- `in-progress` - Handel mit Gegenpartei initiiert
- `success` - Handel abgeschlossen
- `canceled` - Vom Ersteller zurückgezogen
- `expired` - Ablaufzeit überschritten

## Sicherheit

Das `bond`-Tag spezifiziert eine Sicherheitseinlage, die beide Parteien zahlen müssen, und bietet Schutz vor Abbruch oder Betrug.

---

**Primärquellen:**
- [NIP-69 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/69.md)

**Erwähnt in:**
- [Newsletter #1: NIP-Updates](/de/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #1: Veröffentlichungen](/de/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #2: Neuigkeiten](/de/newsletters/2025-12-24-newsletter/#news)
