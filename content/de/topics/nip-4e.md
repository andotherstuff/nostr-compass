---
title: "NIP-4E: Entkopplung von Verschlüsselung und Identität"
date: 2026-07-15
translationOf: /en/topics/nip-4e.md
translationDate: 2026-07-15
draft: false
categories:
  - NIP
  - Protocol
  - Encryption
---

NIP-4E ist ein offener Entwurf, vorgeschlagen von fiatjaf, zum Teilen privater Daten zwischen den eigenen Geräten eines Nutzers, ohne dass jedes Gerät den Haupt-Nostr-Identitätsschlüssel des Nutzers besitzen muss. Es ist nicht gemergt und bleibt ein `draft`/`optional`-Vorschlag.

## Das adressierte Problem

Viele bestehende NIPs, darunter NIP-51-Listen und NIP-60-Cashu-Wallets, verschlüsseln Daten vom Nutzer an sich selbst unter Verwendung des Identitätsschlüssels, damit sie später auf jedem Gerät wieder gelesen werden können. Das funktioniert nicht mehr, wenn der Identitätsschlüssel nicht direkt zugänglich ist, beispielsweise wenn ein Remote Signer durch FROST-Threshold-Shares, MuSig2 oder ein gehostetes Secure Enclave geschützt ist, da Ver- und Entschlüsselung dann jedes Mal einen Roundtrip zu diesem Signer erfordern. Offline-Verschlüsselung wird ebenfalls unmöglich, wenn der Signaturschlüssel in einem Remote Bunker liegt.

## Funktionsweise

NIP-4E trennt einen gerätespezifischen „Client Key" von einem gemeinsamen „Encryption Key", der nicht der Identitätsschlüssel des Nutzers ist:

1. Der erste Client, den ein Nutzer einrichtet, generiert ein zufälliges Verschlüsselungs-Schlüsselpaar und kündigt dessen öffentliche Hälfte in einem `kind:10044`-Event an, das mit dem Identitätsschlüssel des Nutzers signiert ist.
2. Jeder andere Client, der Daten für diesen Nutzer ver- oder entschlüsseln möchte, berechnet sein Diffie-Hellman-Shared-Secret gegen den angekündigten Verschlüsselungsschlüssel statt gegen den Identitätsschlüssel.
3. Wenn ein zweites Gerät einen neuen Client installiert, generiert dieser Client seinen eigenen lokalen „Client Key" und veröffentlicht eine `kind:4454`-Ankündigung (ebenfalls mit dem Identitätsschlüssel des Nutzers signiert), die den ersten Client bittet, den Verschlüsselungsschlüssel zu teilen.
4. Der ursprüngliche Client erkennt die neue `kind:4454`-Ankündigung, verschlüsselt den gemeinsamen Verschlüsselungsschlüssel an den Schlüssel des neuen Clients mittels [NIP-44](/de/topics/nip-44/) und veröffentlicht ihn, damit der neue Client ihn entschlüsseln und fortan verwenden kann.

Das Ergebnis ist, dass Ver- und Entschlüsselung niemals den Identitätsschlüssel-Signer abfragen müssen, sobald ein Client den gemeinsamen Verschlüsselungsschlüssel lokal besitzt, und ein Remote-Signer-Setup (FROST, MuSig2, gehostetes Enclave) für die Identität verwendet werden kann, während gewöhnliche Verschlüsselung schnell bleibt und offline funktioniert.

## Warum es wichtig ist

NIP-4E wird als Grundlage für andere Vorschläge zitiert, die einen laufwerk- oder kontoweiten symmetrischen Schlüssel benötigen, ohne bei jedem Ver-/Entschlüsselungsaufruf auf einen Remote Signer angewiesen zu sein, darunter ein Vorschlag für ein privates verschlüsseltes Laufwerk ([PR #2412](https://github.com/nostr-protocol/nips/pull/2412)) und eine engere NIP-17-spezifische Version derselben Idee ([PR #2361](https://github.com/nostr-protocol/nips/pull/2361)). Beide bleiben neben NIP-4E selbst offen, was dies zu einem aktiven, noch nicht abgeschlossenen Bereich des Protokolls macht, nicht zu einem fertigen Baustein.

---

**Primärquellen:**
- [NIP-4E-Entwurf, PR #1647](https://github.com/nostr-protocol/nips/pull/1647)

**Erwähnt in:**
- [Newsletter #31: Open: private encrypted drive extends NIP-4E](/de/newsletters/2026-07-15-newsletter/#open-private-encrypted-drive-extends-nip-4e)

**Siehe auch:**
- [NIP-44: Encrypted Payloads](/de/topics/nip-44/)
- [NIP-17: Private Direct Messages](/de/topics/nip-17/)
- [NIP-46: Nostr Connect](/de/topics/nip-46/)
- [FROST](/de/topics/frost/)
