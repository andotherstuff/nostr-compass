---
title: "NIP-07: Browser-Erweiterungs-Signer"
date: 2026-01-28
translationOf: /en/topics/nip-07.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Signing
  - Security
---

NIP-07 definiert eine Standardschnittstelle für Browser-Erweiterungen, um Signierfähigkeiten für webbasierte Nostr-Clients bereitzustellen, wobei private Schlüssel sicher in der Erweiterung bleiben, anstatt sie Websites auszusetzen.

## Funktionsweise

Browser-Erweiterungen injizieren ein `window.nostr`-Objekt, das Web-Apps verwenden können:

```javascript
// Öffentlichen Schlüssel abrufen
const pubkey = await window.nostr.getPublicKey();

// Ein Event signieren
const signedEvent = await window.nostr.signEvent(unsignedEvent);

// Verschlüsseln (NIP-04, veraltet)
const ciphertext = await window.nostr.nip04.encrypt(pubkey, plaintext);

// Entschlüsseln (NIP-04, veraltet)
const plaintext = await window.nostr.nip04.decrypt(pubkey, ciphertext);

// NIP-44 Methoden (modern, falls unterstützt)
// const ciphertext = await window.nostr.nip44.encrypt(pubkey, plaintext);
// const plaintext = await window.nostr.nip44.decrypt(pubkey, ciphertext);
```

## Sicherheitsmodell

- **Schlüsselisolierung**: Private Schlüssel verlassen die Erweiterung nie
- **Benutzergenehmigung**: Erweiterungen können für jede Signierungsanfrage nachfragen
- **Domain-Kontrolle**: Erweiterungen können einschränken, welche Seiten Signaturen anfordern dürfen

## Implementierungen

Beliebte NIP-07-Erweiterungen sind:
- **Alby** - Lightning-Wallet mit Nostr-Signierung
- **nos2x** - Leichtgewichtiger Nostr-Signer
- **Flamingo** - Funktionsreiche Nostr-Erweiterung

## Einschränkungen

- Nur für Browser (keine mobile Unterstützung)
- Erfordert Installation der Erweiterung
- Jede Erweiterung hat unterschiedliche UX für Genehmigungen

## Alternativen

- [NIP-46](/de/topics/nip-46/) - Remote-Signierung über Nostr-Relays
- [NIP-55](/de/topics/nip-55/) - Android lokaler Signer

## Verwandt

- [NIP-44](/de/topics/nip-44/) - Moderne Verschlüsselung (ersetzt NIP-04)
- [NIP-46](/de/topics/nip-46/) - Remote-Signierung
