---
title: "NIP-69: Peer-to-Peer-Handel"
date: 2025-12-17
translationOf: /en/topics/nip-69.md
translationDate: 2026-03-07
draft: false
categories:
  - Trading
  - Protocol
---

NIP-69 definiert ein Protokoll für Peer-to-Peer-Handel über Nostr. Es schafft ein gemeinsames Orderbuch über mehrere Plattformen hinweg, statt Liquidität in getrennten Pools einzuschließen.

## Funktionsweise

NIP-69 verwendet addressable kind-38383-Events für Kauf- und Verkaufsorders. Das addressable Format ist wichtig, weil eine Order im Lauf der Zeit mehrere Zustände durchlaufen kann und über ihr `d`-Tag trotzdem dieselbe logische Identität behält.

## Order-Struktur

Orders verwenden Tags, um Handelsparameter festzulegen:

- `d` - Order-ID
- `k` - Order-Typ (buy/sell)
- `f` - Fiat-Währung (ISO-4217-Code)
- `amt` - Bitcoin-Betrag in Satoshis
- `fa` - Fiat-Betrag
- `pm` - Akzeptierte Zahlungsmethoden
- `premium` - Preisaufschlag oder Rabatt in Prozent
- `network` - Bitcoin-Netzwerk (mainnet, testnet, signet, regtest)
- `layer` - Settlement Layer (onchain, lightning, liquid)
- `expiration` - Zeitpunkt, zu dem die Order abläuft

## Lebenszyklus einer Order

Orders bewegen sich durch folgende Status:
- `pending` - Offen und verfügbar für Matching
- `in-progress` - Handel mit Gegenpartei gestartet
- `success` - Handel abgeschlossen
- `canceled` - Vom Maker zurückgezogen
- `expired` - Ablaufzeit überschritten

Die Spezifikation unterscheidet zwei Zeitgrenzen. `expires_at` markiert den Zeitpunkt, an dem eine ausstehende Order nicht mehr als offen gelten soll, während `expiration` Relays einen Zeitstempel für [NIP-40](/de/topics/nip-40/) gibt, mit dem veraltete Order-Events ganz entfernt werden können.

## Warum das wichtig ist

NIP-69 ist vor allem ein Interoperabilitätsprojekt. Mostro, lnp2pBot, RoboSats, Peach und andere P2P-Handelssysteme können Orders in ein gemeinsames Event-Format ausspielen, statt Liquidität in einzelnen Apps festzuhalten.

Das optionale `g`-Tag macht außerdem lokalen Handel von Angesicht zu Angesicht möglich, ohne den Rest des Order-Schemas zu ändern. Das ist nützlich, weil Bargeldgeschäfte vor Ort geografische Filter brauchen, Lightning-Handel online aber nicht.

## Sicherheit und Vertrauen

Das `bond`-Tag legt eine Sicherheitsleistung fest, die beide Parteien hinterlegen müssen. Das bietet Schutz gegen Abbruch oder Betrug.

Gegenparteirisiko verschwindet dadurch nicht. Zahlungsstreitigkeiten, Fiat-Betrug, Reputationssysteme und Verwahrungsregeln bleiben weiter auf Anwendungsebene. NIP-69 standardisiert die Veröffentlichung von Orders, nicht die Streitbeilegung.

---

**Primärquellen:**
- [NIP-69 Specification](https://github.com/nostr-protocol/nips/blob/master/69.md)
- [Mostro Protocol Specification](https://mostro.network/protocol/)

**Erwähnt in:**
- [Newsletter #1: NIP Updates](/de/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #1: Releases](/de/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #2: News](/de/newsletters/2025-12-24-newsletter/#news)

**Siehe auch:**
- [NIP-40: Expiration Timestamp](/de/topics/nip-40/)
