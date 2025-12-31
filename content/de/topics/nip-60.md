---
title: "NIP-60: Cashu Wallet"
date: 2025-12-31
translationOf: /en/topics/nip-60.md
translationDate: 2025-12-31
draft: false
categories:
  - Wallet
  - Ecash
---

NIP-60 definiert, wie Cashu-basierte ecash-Wallets innerhalb von Nostr funktionieren. Wallet-Informationen werden auf Relays gespeichert, wodurch portable Wallets ermöglicht werden, die über verschiedene Anwendungen hinweg funktionieren, ohne separate Konten zu erfordern.

## Funktionsweise

NIP-60 verwendet drei Arten von Events, die auf Relays gespeichert werden:

**Wallet-Event (kind 17375):** Ein ersetzbares Event, das verschlüsselte Wallet-Konfiguration enthält, einschließlich Mint-URLs und einem privaten Schlüssel für den Zahlungsempfang. Dieser Schlüssel ist vom Nostr-Identitätsschlüssel des Benutzers getrennt.

**Token-Events (kind 7375):** Speichern verschlüsselte, nicht ausgegebene Cashu-Proofs. Wenn Proofs ausgegeben werden, löscht der Client das alte Event und erstellt ein neues mit den verbleibenden Proofs.

**Ausgabenverlauf (kind 7376):** Optionale Transaktionsaufzeichnungen, die Geldbewegungen zeigen, mit verschlüsseltem Inhalt und Verweisen auf erstellte/zerstörte Token-Events.

## Hauptfunktionen

- **Benutzerfreundlichkeit** - Neue Benutzer können sofort ecash empfangen, ohne externe Kontoeinrichtung
- **Interoperabilität** - Wallet-Daten folgen Benutzern über verschiedene Nostr-Anwendungen hinweg
- **Privatsphäre** - Alle Wallet-Daten sind mit den Schlüsseln des Benutzers verschlüsselt
- **Proof-Management** - Verfolgt, welche Token-Events ausgegeben wurden, um Doppelausgaben zu verhindern

## Arbeitsablauf

1. Client ruft Wallet-Konfiguration von Relays ab
2. Token-Events werden geladen und entschlüsselt, um verfügbare Mittel zu erhalten
3. Ausgeben erstellt neue Token-Events und löscht alte
4. Optionale Verlaufs-Events zeichnen Transaktionen zur Benutzerreferenz auf

---

**Primärquellen:**
- [NIP-60 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/60.md)

**Erwähnt in:**
- [Newsletter #3: Dezember-Rückblick](/de/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Siehe auch:**
- [NIP-57: Zaps](/de/topics/nip-57/)
- [NIP-47: Nostr Wallet Connect](/de/topics/nip-47/)
