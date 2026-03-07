---
title: "NIP-07: Browser-Erweiterungs-Signer"
date: 2026-01-28
translationOf: /en/topics/nip-07.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Signing
  - Security
---

NIP-07 definiert eine Standardschnittstelle, mit der Browser-Erweiterungen Signierfunktionen für webbasierte Nostr-Clients bereitstellen. Private Schlüssel bleiben in der Erweiterung, statt auf Websites offengelegt zu werden.

## Wie es funktioniert

Browser-Erweiterungen injizieren ein `window.nostr`-Objekt, das Web-Apps verwenden können:

```javascript
// Get public key
const pubkey = await window.nostr.getPublicKey();

// Sign an event
const signedEvent = await window.nostr.signEvent(unsignedEvent);

// Encrypt (NIP-04, legacy)
const ciphertext = await window.nostr.nip04.encrypt(pubkey, plaintext);

// Decrypt (NIP-04, legacy)
const plaintext = await window.nostr.nip04.decrypt(pubkey, ciphertext);

// NIP-44 methods (modern, if supported)
// const ciphertext = await window.nostr.nip44.encrypt(pubkey, plaintext);
// const plaintext = await window.nostr.nip44.decrypt(pubkey, ciphertext);
```

## Sicherheitsmodell

- **Schlüsselisolierung**: Private Schlüssel verlassen die Erweiterung nie
- **Nutzerfreigabe**: Erweiterungen können für jede Signaturanfrage nach Bestätigung fragen
- **Domain-Kontrolle**: Erweiterungen können einschränken, welche Seiten Signaturen anfordern dürfen

NIP-07 verbessert die Verwahrung von Schlüsseln, entfernt aber nicht das Vertrauen in die Erweiterung selbst. Eine bösartige oder kompromittierte Erweiterung kann weiterhin das Falsche signieren, Metadaten leaken oder Berechtigungen zu weit vergeben.

## Interop-Hinweise

Der schwierigste Teil von NIP-07 ist nicht die Form der API, sondern die Unterschiede bei den Fähigkeiten. Manche Erweiterungen unterstützen nur `getPublicKey()` und `signEvent()`. Andere bieten zusätzlich `nip04`, `nip44` oder neuere optionale Methoden an. Web-Apps brauchen Feature Detection und sinnvolle Fallbacks, statt anzunehmen, dass jeder injizierte Signer gleich funktioniert.

Auch die UX für Nutzerfreigaben verändert das Verhalten. Eine Website, die stillschweigend Hintergrundzugriff erwartet, funktioniert mit einer Erweiterung vielleicht, wirkt mit einer anderen aber defekt, wenn dort jede Anfrage bestätigt werden muss. Gute NIP-07-Apps behandeln Signieren als interaktive Berechtigungsgrenze.

## Implementierungsstatus

Beliebte NIP-07-Erweiterungen sind:
- **Alby** - Lightning-Wallet mit Nostr-Signing
- **nos2x** - Leichtgewichtiger Nostr-Signer
- **Flamingo** - Funktionsreiche Nostr-Erweiterung

## Grenzen

- Nur für Browser, keine mobile Unterstützung
- Erfordert die Installation einer Erweiterung
- Jede Erweiterung hat eine andere UX für Freigaben

Für geräteübergreifendes oder mobiles Signing passen NIP-46 und NIP-55 meist besser.

---

**Primärquellen:**
- [NIP-07 Specification](https://github.com/nostr-protocol/nips/blob/master/07.md)
- [PR #2233](https://github.com/nostr-protocol/nips/pull/2233) - `peekPublicKey()` proposal

**Erwähnt in:**
- [Newsletter #7: NIP Updates](/en/newsletters/2026-01-28-newsletter/#nip-updates)
- [Newsletter #8: News](/en/newsletters/2026-02-04-newsletter/#news)
- [Newsletter #11: News](/en/newsletters/2026-02-25-newsletter/#news)

**Siehe auch:**
- [NIP-04: Verschlüsselte Direktnachrichten (Veraltet)](/de/topics/nip-04/)
- [NIP-44: Encrypted Payloads](/de/topics/nip-44/)
- [NIP-46: Nostr Connect](/de/topics/nip-46/)
- [NIP-55: Android Signer Applications](/de/topics/nip-55/)
