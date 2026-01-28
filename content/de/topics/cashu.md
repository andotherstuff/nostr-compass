---
title: "Cashu: Ecash-Protokoll"
date: 2026-01-28
translationOf: /en/topics/cashu.md
translationDate: 2026-01-28
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
---

Cashu ist ein Chaumian-Ecash-Protokoll, das auf Bitcoin und Lightning Network aufbaut und private, sofortige und kostengünstige Zahlungen durch kryptographische Tokens ermöglicht.

## Funktionsweise

Cashu verwendet Blind-Signaturen zur Erstellung nicht nachverfolgbarer Ecash-Tokens:

1. **Prägung**: Benutzer hinterlegen Bitcoin/Lightning bei einem Mint und erhalten geblindete Tokens
2. **Ausgabe**: Tokens können Peer-to-Peer ohne Mint-Beteiligung übertragen werden
3. **Einlösung**: Empfänger lösen Tokens beim Mint gegen Bitcoin/Lightning ein

Der Mint kann aufgrund des Blinding-Prozesses keine Einzahlungen mit Einlösungen verknüpfen, was starke Datenschutzgarantien bietet.

## Haupteigenschaften

- **Privatsphäre**: Mint kann Token-Transfers zwischen Benutzern nicht verfolgen
- **Sofort**: Transfers erfolgen offline, keine Blockchain-Bestätigung erforderlich
- **Geringe Gebühren**: Keine On-Chain-Gebühren für Token-Transfers
- **Treuhänderisch**: Benutzer vertrauen darauf, dass der Mint Einlösungen honoriert

## Nostr-Integration

Cashu integriert sich auf verschiedene Weise mit Nostr:

- **Nutzaps**: Ecash-Tokens, die als Zaps mit verbesserter Privatsphäre gesendet werden
- **Treuhand**: HTLC-basierte Zahlungs-Treuhand für Dienste wie Ridesharing
- **Wallets**: Nostr-native Wallets speichern verschlüsselte Cashu-Tokens auf Relays
- **[NIP-87](/de/topics/nip-87/)**: Mint-Entdeckung und Bewertungen über Nostr

## Vertrauensmodell

Anders als selbstverwahrtes Bitcoin erfordert Cashu das Vertrauen in Mint-Betreiber. Benutzer sollten:
- Seriöse, gut bewertete Mints verwenden
- Kleine Guthaben halten, die dem Vertrauensniveau angemessen sind
- Verstehen, dass Mints Exit-Scam betreiben oder offline gehen können und dabei Gelder mitnehmen

## Verwandt

- [NIP-87](/de/topics/nip-87/) - Cashu Mint Empfehlungen
- [NIP-60](/de/topics/nip-60/) - Nostr Wallet
