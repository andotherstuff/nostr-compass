---
title: "NIP-47: Nostr Wallet Connect"
date: 2025-12-17
translationOf: /en/topics/nip-47.md
translationDate: 2026-03-11
draft: false
categories:
  - Wallet
  - Lightning
---

NIP-47 definiert Nostr Wallet Connect, ein Protokoll, mit dem eine Nostr-App mit einem entfernten Lightning-Wallet-Service sprechen kann, ohne die Hauptzugangsdaten der Wallet jedem Client offenzulegen.

## Wie es funktioniert

Ein Wallet-Service veroffentlicht ein ersetzbares Info-Event vom Kind `13194`, das die unterstutzten Methoden und Verschlusselungsmodi beschreibt. Ein Client verbindet sich uber eine `nostr+walletconnect://`-URI, die den Pubkey des Wallet-Service, ein oder mehrere Relays und ein eigenes Secret fur diese Verbindung enthalt. Anfragen werden als Events vom Kind `23194` gesendet, Antworten kommen als Events vom Kind `23195` zuruck.

## Befehle und Benachrichtigungen

Zu den gangigen Methoden gehoren `pay_invoice`, `pay_keysend`, `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance` und `get_info`. Wallet-Services konnen auch Benachrichtigungen wie `payment_received`, `payment_sent` und `hold_invoice_accepted` senden.

Die Spezifikation hat im Lauf der Zeit mehrere optionale Methoden aufgenommen, aber bei einer Aufraumaktion wurden die `multi_`-Zahlungsmethoden entfernt. In der Praxis ist die Interoperabilitat besser, wenn Clients sich an die Befehle halten, die im Info-Event der Wallet beworben werden, statt einen breiten Methodensatz vorauszusetzen.

## Anwendungsfalle

- **Zapping** - Sats an Beitrage, Profile oder Content-Ersteller senden
- **Zahlungen** - Lightning-Rechnungen aus jeder Nostr-App bezahlen
- **Trennung der Wallet-UX** - Einen Wallet-Service in vielen Nostr-Clients nutzen

## Sicherheits- und Interop-Hinweise

Die Verbindungs-URI enthalt ein eigenes Secret, das der Client fur Signatur und Verschlusselung verwendet. So bekommt jede App ihre eigene Wallet-Identitat, was sowohl Widerruf als auch Privatsphare verbessert. Eine Wallet kann Ausgabelimits setzen, Methoden deaktivieren oder eine einzelne Verbindung widerrufen, ohne andere Verbindungen zu beeinflussen.

NIP-44 ist jetzt der bevorzugte Verschlusselungsmodus. Die Spezifikation dokumentiert fur altere Implementierungen weiter einen NIP-04-Fallback, deshalb mussen Clients das beworbene `encryption`-Tag der Wallet prufen, statt anzunehmen, dass jede Wallet schon migriert ist.

---

**Primarquellen:**
- [NIP-47 Specification](https://github.com/nostr-protocol/nips/blob/master/47.md)
- [PR #1913: Hold Invoice Support](https://github.com/nostr-protocol/nips/pull/1913)
- [PR #2210: Simplification](https://github.com/nostr-protocol/nips/pull/2210)

**Erwahnt in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: Releases](/en/newsletters/2025-12-24-newsletter/#releases)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #8: NIP Deep Dive](/en/newsletters/2026-02-04-newsletter/#nip-deep-dive-nip-47-nostr-wallet-connect)
- [Newsletter #10: NIP Updates](/en/newsletters/2026-02-18-newsletter/#nip-updates)

**Siehe auch:**
- [NIP-57: Zaps](/de/topics/nip-57/)
