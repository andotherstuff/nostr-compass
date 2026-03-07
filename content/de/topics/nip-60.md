---
title: "NIP-60: Cashu Wallet"
date: 2025-12-31
translationOf: /en/topics/nip-60.md
translationDate: 2026-03-07
draft: false
categories:
  - Wallet
  - Ecash
---

NIP-60 definiert, wie Cashu-basierte ecash-Wallets innerhalb von Nostr funktionieren. Wallet-Informationen werden auf Relays gespeichert, wodurch portable Wallets möglich werden, die über verschiedene Anwendungen hinweg ohne separate Konten funktionieren.

## Funktionsweise

NIP-60 verwendet drei zentrale Event-Typen, die auf Relays gespeichert werden, plus ein optionales Hilfs-Event für ausstehende Quotes:

**Wallet-Event (kind 17375):** Ein ersetzbares Event mit verschlüsselter Wallet-Konfiguration, einschließlich Mint-URLs und eines privaten Schlüssels für den Zahlungsempfang. Dieser Schlüssel ist vom Nostr-Identitätsschlüssel des Nutzers getrennt.

**Token-Events (kind 7375):** Speichern verschlüsselte, nicht ausgegebene Cashu-Proofs. Wenn Proofs ausgegeben werden, löscht der Client das alte Event und erstellt ein neues mit allen verbleibenden Proofs.

**Spending History (kind 7376):** Optionale Transaktionsaufzeichnungen, die Geldbewegungen zeigen, mit verschlüsseltem Inhalt und Verweisen auf erstellte oder zerstörte Token-Events.

**Quote-Events (kind 7374):** Optionaler verschlüsselter Zustand für ausstehende Mint-Quotes. Die Spezifikation empfiehlt kurzlebige Events mit Expiration-Tags, vor allem für Fälle, in denen lokaler Zustand nicht ausreicht.

## Zustandsmodell

Bei NIP-60 geht es um die Synchronisierung des Wallet-Zustands, nicht um den eigentlichen Geldempfang. Das Wallet-Event sagt einem Client, welche Mints und welchen Wallet-Key er verwenden soll, während Token-Events den eigentlichen Kontostand darstellen, weil sie die nicht ausgegebenen Proofs enthalten.

Diese Unterscheidung ist wichtig für Interoperabilität. Zwei Clients können dieselbe Wallet nur dann gleich darstellen, wenn sie Token-Rollover gleich interpretieren: Proofs ausgeben, Ersatz-Proofs veröffentlichen und das ausgegebene Token-Event über [NIP-09](/de/topics/nip-09/) löschen, damit andere Clients ausgegebene Proofs nicht weiter als Guthaben zählen.

## Warum das wichtig ist

- **Einfache Nutzung** - Neue Nutzer können sofort ecash empfangen, ohne erst ein externes Konto einzurichten
- **Interoperabilität** - Wallet-Daten folgen Nutzern über verschiedene Nostr-Anwendungen hinweg
- **Privatsphäre** - Alle Wallet-Daten sind für die Schlüssel des Nutzers verschlüsselt
- **Proof-Management** - Wallet-Zustandswechsel werden nachverfolgt, damit Clients auf denselben Kontostand konvergieren können

## Interop-Hinweise

Clients suchen zuerst über kind 10019 nach Wallet-Relay-Informationen und greifen auf die Relay-Liste des Nutzers aus [NIP-65](/de/topics/nip-65/) zurück, wenn keine eigene Wallet-Relay-Liste vorhanden ist. Dieser Fallback ist nützlich, aber Wallet-Portabilität hängt trotzdem davon ab, dass Relays die verschlüsselten Wallet-Events tatsächlich speichern und ausliefern.

Die Spezifikation verlangt auch, dass der private Wallet-Schlüssel vom Nostr-Identitätsschlüssel des Nutzers getrennt bleibt. Dadurch bleibt die Annahme von Wallet-Zahlungen vom Hauptschlüssel isoliert und das Risiko sinkt, einen Schlüssel für zwei verschiedene Zwecke wiederzuverwenden.

## Ablauf

1. Der Client lädt die Wallet-Konfiguration von Wallet-Relays oder aus der Relay-Liste des Nutzers
2. Token-Events werden geladen und entschlüsselt, um verfügbare Mittel zu ermitteln
3. Beim Ausgeben entstehen neue Token-Events und alte werden gelöscht
4. Optionale History-Events zeichnen Transaktionen für den Nutzer auf

---

**Primärquellen:**
- [NIP-60 Specification](https://github.com/nostr-protocol/nips/blob/master/60.md)

**Erwähnt in:**
- [Newsletter #3: December Recap](/de/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #9: NIP Deep Dive](/de/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-60-cashu-wallet)

**Siehe auch:**
- [NIP-57: Zaps](/de/topics/nip-57/)
- [NIP-09: Event Deletion Request](/de/topics/nip-09/)
- [NIP-47: Nostr Wallet Connect](/de/topics/nip-47/)
