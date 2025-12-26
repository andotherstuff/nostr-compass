---
title: "NIP-46: Nostr Connect"
date: 2025-12-17
draft: false
categories:
  - Signing
  - Protocol
---

NIP-46 definiert Remote-Signierung, die es einer Signer-Anwendung ermöglicht, Schlüssel zu halten, während Clients Signaturen über Nostr-Relays anfordern.

## Funktionsweise

1. Der Signer generiert eine Verbindungs-URI (`bunker://` oder `nostrconnect://`)
2. Der Benutzer fügt die URI in einen Client ein
3. Der Client sendet Signaturanfragen als verschlüsselte Events an das Relay des Signers
4. Der Signer fordert den Benutzer zur Genehmigung auf und gibt signierte Events zurück

## Verbindungsmethoden

- **bunker://** - Vom Signer initiierte Verbindung
- **nostrconnect://** - Vom Client initiierte Verbindung über QR-Code oder Deep Link

## Unterstützte Operationen

- `sign_event` - Ein beliebiges Event signieren
- `get_public_key` - Den öffentlichen Schlüssel des Signers abrufen
- `nip04_encrypt/decrypt` - NIP-04-Verschlüsselungsoperationen
- `nip44_encrypt/decrypt` - NIP-44-Verschlüsselungsoperationen

---

**Primärquellen:**
- [NIP-46 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/46.md)

**Erwähnt in:**
- [Newsletter #1: Bemerkenswerte Code-Änderungen](/de/newsletters/2025-12-17-newsletter/#amethyst-android)

**Siehe auch:**
- [NIP-55: Android Signer](/de/topics/nip-55/)
