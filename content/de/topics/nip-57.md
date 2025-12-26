---
title: "NIP-57: Zaps"
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
  - Social
---

NIP-57 definiert Zaps, eine Möglichkeit, Lightning-Zahlungen an Nostr-Benutzer und Inhalte mit kryptografischem Nachweis zu senden, dass die Zahlung erfolgt ist.

## Funktionsweise

1. Client ruft die Lightning-Adresse des Empfängers aus seinem Kind-0-Profil ab
2. Client fordert eine Rechnung vom LNURL-Server des Empfängers an, einschließlich eines Zap-Request-Events
3. Benutzer bezahlt die Rechnung
4. LNURL-Server veröffentlicht eine Kind-9735-Zap-Quittung an Nostr-Relays
5. Clients zeigen den Zap beim Inhalt des Empfängers an

## Zap-Anfrage (Kind 9734)

Die Zap-Anfrage ist ein signiertes Event, das beweist, wer den Zap gesendet hat und an welchen Inhalt. Es enthält:
- `p`-Tag mit Empfänger-Pubkey
- `e`-Tag mit dem gezappten Event (optional)
- `amount`-Tag in Millisatoshis
- `relays`-Tag, das auflistet, wo die Quittung veröffentlicht werden soll

## Zap-Quittung (Kind 9735)

Vom LNURL-Server nach Zahlungsbestätigung veröffentlicht. Enthält:
- Die ursprüngliche Zap-Anfrage in einem `description`-Tag
- `bolt11`-Tag mit der bezahlten Rechnung
- `preimage`-Tag als Zahlungsnachweis

---

**Primärquellen:**
- [NIP-57 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/57.md)

**Erwähnt in:**
- [Newsletter #1: Neuigkeiten](/de/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: Neuigkeiten](/de/newsletters/2025-12-24-newsletter/#news)

**Siehe auch:**
- [NIP-47: Nostr Wallet Connect](/de/topics/nip-47/)
