---
title: "NIP-47: Nostr Wallet Connect"
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
---

NIP-47 definiert ein Protokoll zur Verbindung von Nostr-Anwendungen mit Lightning-Wallets, das Zahlungen ermöglicht, ohne Wallet-Anmeldedaten an jede App preiszugeben.

## Funktionsweise

Eine Wallet (wie Zeus) betreibt einen NWC-Dienst, der auf Zahlungsanfragen auf bestimmten Nostr-Relays wartet. Apps verbinden sich über eine Verbindungszeichenfolge, die den Pubkey der Wallet und Relay-Informationen enthält. Zahlungsanfragen und -antworten werden zwischen der App und der Wallet verschlüsselt.

## Anwendungsfälle

- **Zapping** - Sats an Beiträge, Profile oder Inhaltsersteller senden
- **Zahlungen** - Lightning-Rechnungen von jeder Nostr-App bezahlen
- **Abonnements** - Wiederkehrende Zahlungen für Premium-Inhalte

## Hauptfunktionen

- **Budgetkontrollen** - Ausgabenlimits pro Verbindung festlegen
- **Eigene Relays** - Eigenes Relay für Wallet-Kommunikation verwenden
- **Parallele Zahlungen** - Mehrere Zaps gleichzeitig für Batch-Operationen verarbeiten

---

**Primärquellen:**
- [NIP-47 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/47.md)

**Erwähnt in:**
- [Newsletter #1: Neuigkeiten](/de/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: Veröffentlichungen](/de/newsletters/2025-12-24-newsletter/#releases)

**Siehe auch:**
- [NIP-57: Zaps](/de/topics/nip-57/)
