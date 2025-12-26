---
title: "NIP-55: Android Signer-Anwendung"
date: 2025-12-17
draft: false
categories:
  - Signing
  - Mobile
---

NIP-55 definiert, wie Android-Anwendungen Signieroperationen von einer dedizierten Signer-App anfordern können, sodass Benutzer ihre privaten Schlüssel an einem sicheren Ort aufbewahren können, während sie mehrere Nostr-Clients verwenden.

## Funktionsweise

NIP-55 verwendet die Content-Provider-Schnittstelle von Android, um Signieroperationen bereitzustellen. Eine Signer-App registriert sich als Content Provider, und andere Nostr-Apps können Signaturen anfordern, ohne jemals direkt auf den privaten Schlüssel zuzugreifen.

Der Ablauf:
1. Client-App ruft den Content Provider des Signers auf
2. Signer zeigt dem Benutzer eine Genehmigungsoberfläche
3. Benutzer genehmigt oder lehnt die Anfrage ab
4. Signer gibt die Signatur (oder Ablehnung) an den Client zurück

## Wichtige Operationen

- **get_public_key** - Den öffentlichen Schlüssel des Benutzers abrufen (einmal beim initialen Verbindungsaufbau aufrufen)
- **sign_event** - Ein Nostr-Event signieren
- **nip04_encrypt/decrypt** - NIP-04-Nachrichten ver- oder entschlüsseln
- **nip44_encrypt/decrypt** - NIP-44-Nachrichten ver- oder entschlüsseln

## Verbindungsinitialisierung

Ein häufiger Implementierungsfehler ist das wiederholte Aufrufen von `get_public_key` aus Hintergrundprozessen. Die Spezifikation empfiehlt, es nur einmal beim initialen Verbindungsaufbau aufzurufen und dann das Ergebnis zwischenzuspeichern.

---

**Primärquellen:**
- [NIP-55 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/55.md)

**Erwähnt in:**
- [Newsletter #1: Veröffentlichungen](/de/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #2: Neuigkeiten](/de/newsletters/2025-12-24-newsletter/#news)
- [Newsletter #2: NIP-Updates](/de/newsletters/2025-12-24-newsletter/#nip-updates)

**Siehe auch:**
- [NIP-46: Nostr Connect](/de/topics/nip-46/)
