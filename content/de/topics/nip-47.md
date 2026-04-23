---
title: "NIP-47: Nostr Wallet Connect"
date: 2025-12-17
translationOf: /en/topics/nip-47.md
translationDate: 2026-04-22
draft: false
categories:
  - Wallet
  - Lightning
---

NIP-47 definiert Nostr Wallet Connect, ein Protokoll, mit dem eine Nostr-App mit einem entfernten Lightning-Wallet-Service sprechen kann, ohne die Hauptzugangsdaten der Wallet jedem Client offenzulegen.

## Funktionsweise

Ein Wallet-Service veröffentlicht ein ersetzbares kind-`13194`-Info-Event, das die unterstützten Methoden und Verschlüsselungsmodi beschreibt. Ein Client verbindet sich über eine `nostr+walletconnect://`-URI, die den pubkey des Wallet-Service, ein oder mehrere Relays und ein dediziertes Secret für genau diese Verbindung enthält. Requests werden als kind-`23194`-Events gesendet, Responses kommen als kind-`23195`-Events zurück.

## Befehle und Benachrichtigungen

Zu den üblichen Methoden gehören `pay_invoice`, `pay_keysend`, `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance` und `get_info`. Wallet-Services können außerdem Benachrichtigungen wie `payment_received`, `payment_sent` und `hold_invoice_accepted` pushen.

Die Spezifikation wuchs im Lauf der Zeit um mehrere optionale Methoden, aber eine spätere Bereinigung entfernte die `multi_`-Zahlungsmethoden. In der Praxis ist die Interoperabilität besser, wenn Clients sich an die Befehle halten, die das Info-Event der Wallet bewirbt, statt einen breiten Methodensatz vorauszusetzen.

## Anwendungsfälle

- **Zapping** - sats an Beiträge, Profile oder Content-Ersteller senden
- **Payments** - Lightning-Invoices aus jeder Nostr-App bezahlen
- **Wallet UX separation** - Einen Wallet-Service in vielen Nostr-Clients verwenden

## Sicherheits- und Interop-Hinweise

Die Verbindungs-URI enthält ein dediziertes Secret, das der Client für Signing und Verschlüsselung verwendet. Dadurch bekommt jede App ihre eigene Wallet-Identität, was sowohl Widerruf als auch Privatsphäre verbessert. Eine Wallet kann Ausgabelimits setzen, Methoden deaktivieren oder eine einzelne Verbindung widerrufen, ohne andere Verbindungen zu beeinflussen.

NIP-44 ist inzwischen der bevorzugte Verschlüsselungsmodus. Die Spezifikation dokumentiert weiterhin einen NIP-04-Fallback für ältere Implementierungen, deshalb müssen Clients das von der Wallet beworbene `encryption`-Tag prüfen, statt anzunehmen, dass jede Wallet bereits migriert ist.

---

**Primärquellen:**
- [NIP-47 Specification](https://github.com/nostr-protocol/nips/blob/master/47.md)
- [PR #1913: Hold Invoice Support](https://github.com/nostr-protocol/nips/pull/1913)
- [PR #2210: Simplification](https://github.com/nostr-protocol/nips/pull/2210)

**Erwähnt in:**
- [Newsletter #1: News](/de/newsletters/2025-12-17-newsletter/)
- [Newsletter #2: Releases](/de/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: December Recap](/de/newsletters/2025-12-31-newsletter/)
- [Newsletter #8: NIP Deep Dive](/de/newsletters/2026-02-04-newsletter/)
- [Newsletter #10: NIP Updates](/de/newsletters/2026-02-18-newsletter/)
- [Newsletter #13: Shopstr and Milk Market Open MCP Commerce Surfaces](/en/newsletters/2026-03-11-newsletter/)
- [Newsletter #19: ShockWallet Nostr-native wallet sync](/en/newsletters/2026-04-22-newsletter/)

**Siehe auch:**
- [NIP-57: Zaps](/de/topics/nip-57/)
