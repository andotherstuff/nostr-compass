---
title: "NIP-46: Nostr Connect"
date: 2025-12-17
translationOf: /en/topics/nip-46.md
translationDate: 2026-04-22
draft: false
categories:
  - Signing
  - Protocol
---

NIP-46 definiert Remote-Signing über Nostr-Relays. Ein Client spricht mit einem separaten Signer, oft Bunker genannt, sodass Signing-Keys außerhalb der App bleiben können, die der Nutzer gerade aktiv verwendet.

## Funktionsweise

1. Der Client erzeugt ein lokales Keypair, das nur für die Bunker-Session verwendet wird.
2. Die Verbindung wird mit einer `bunker://`- oder `nostrconnect://`-URI aufgebaut.
3. Client und Signer tauschen verschlüsselte kind-`24133`-Request- und Response-Events über Relays aus.
4. Nach dem Verbinden ruft der Client `get_public_key` auf, um den tatsächlichen Nutzer-pubkey zu erfahren, für den signiert wird.

## Verbindungsmethoden

- **bunker://** - Vom Signer initiierte Verbindung
- **nostrconnect://** - Vom Client initiierte Verbindung über QR-Code oder Deep Link

`nostrconnect://`-Flows enthalten ein erforderliches Shared Secret, damit der Client verifizieren kann, dass die erste Antwort wirklich vom beabsichtigten Signer kommt. Das verhindert einfaches Connection Spoofing.

## Unterstützte Operationen

- `sign_event` - Ein beliebiges Event signieren
- `get_public_key` - Den pubkey des Nutzers vom Signer abrufen
- `nip04_encrypt/decrypt` - NIP-04-Verschlüsselungsoperationen
- `nip44_encrypt/decrypt` - NIP-44-Verschlüsselungsoperationen
- `switch_relays` - Den Signer nach einem aktualisierten Relay-Set fragen

Viele Implementierungen verwenden beim Setup außerdem Permission-Strings wie `sign_event:1` oder `nip44_encrypt`, damit der Signer einen engen Scope statt Vollzugriff freigeben kann.

## Relay- und Vertrauensmodell

NIP-46 verschiebt private keys aus dem Client heraus, entfernt aber nicht das Vertrauen in den Signer. Der Signer kann Anfragen genehmigen, ablehnen oder verzögern, und er sieht jede Operation, die der Client von ihm ausführen lassen will. Auch die Wahl der Relays ist wichtig, weil das Protokoll von der Zustellung von Requests und Responses über Relays abhängt, die beide Seiten erreichen können.

Die Methode `switch_relays` existiert, damit der Signer die Session im Lauf der Zeit auf ein anderes Relay-Set umstellen kann. Clients, die das ignorieren, arbeiten weniger zuverlässig, wenn sich die Relay-Präferenzen des Signers ändern.

---

**Primärquellen:**
- [NIP-46 Specification](https://github.com/nostr-protocol/nips/blob/master/46.md)

**Erwähnt in:**
- [Newsletter #1: Notable Code Changes](/de/newsletters/2025-12-17-newsletter/)
- [Newsletter #3: December Recap](/de/newsletters/2025-12-31-newsletter/)
- [Newsletter #4: Primal Android Becomes a Full Signing Hub](/de/newsletters/2026-01-07-newsletter/)
- [Newsletter #12: NDK Collaborative Events and NIP-46 Timeout](/de/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: NipLock signer support](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: Forgesworn Heartwood signer](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: Flotilla Aegis NIP-46 login](/en/newsletters/2026-04-22-newsletter/)

**Siehe auch:**
- [NIP-55: Android Signer](/de/topics/nip-55/)
