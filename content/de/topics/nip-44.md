---
title: "NIP-44: Encrypted Payloads"
date: 2025-12-31
translationOf: /en/topics/nip-44.md
translationDate: 2026-04-22
draft: false
categories:
  - NIP
  - Cryptography
  - Privacy
---

NIP-44 definiert einen versionierten Verschlüsselungsstandard für Nostr-Payloads und ersetzt das fehlerhafte NIP-04-Verschlüsselungsschema durch moderne kryptographische Primitive.

## Funktionsweise

NIP-44 Version 2 verwendet einen mehrstufigen Verschlüsselungsprozess:

1. **Key Agreement**: ECDH, secp256k1, zwischen den öffentlichen Schlüsseln von Sender und Empfänger erzeugt ein gemeinsames Geheimnis
2. **Key Derivation**: HKDF-extract mit SHA256 und Salt `nip44-v2` erzeugt einen Konversationsschlüssel
3. **Per-Message Keys**: HKDF-expand leitet ChaCha-Key, Nonce und HMAC-Key aus einer zufälligen Nonce ab
4. **Padding**: Der Inhalt wird aufgefüllt, um die Nachrichtenlänge zu verbergen
5. **Encryption**: ChaCha20 verschlüsselt den aufgefüllten Inhalt
6. **Authentication**: HMAC-SHA256 liefert Nachrichtenintegrität

Das Ergebnis ist eine versionierte base64-Payload, die in ein normal signiertes Nostr-Event eingefügt wird. Die Spezifikation verlangt, dass Clients die äußere NIP-01-Event-Signatur validieren, bevor sie die innere NIP-44-Payload entschlüsseln.

## Kryptographische Entscheidungen

- **ChaCha20** statt AES: schneller und widerstandsfähiger gegen Multi-Key-Angriffe
- **HMAC-SHA256** statt Poly1305: Polynomial-MACs lassen sich leichter fälschen
- **SHA256**: konsistent mit bestehenden Nostr-Primitiven
- **Versioned Format**: ermöglicht spätere Algorithmus-Upgrades

## Sicherheitseigenschaften

- **Authenticated Encryption**: Nachrichten können nicht unbemerkt manipuliert werden
- **Length Hiding**: Padding verschleiert die Nachrichtengröße
- **Conversation Keys**: Derselbe Schlüssel für laufende Konversationen reduziert Rechenaufwand
- **Audited**: Das Cure53-Sicherheitsaudit fand keine ausnutzbaren Schwachstellen

## Implementierungshinweise

NIP-44 ist kein direkter Ersatz für NIP-04-Payloads. Es definiert ein Verschlüsselungsformat, aber keinen Direct-Message-Event-Kind. Protokolle wie [NIP-17](/de/topics/nip-17/) und [NIP-59](/de/topics/nip-59/) definieren, wie verschlüsselte Payloads in tatsächlichen Nachrichtenflüssen verwendet werden.

Die plaintext-Eingabe ist UTF-8-Text mit einer Länge von 1 bis 65535 Bytes. Das ist eine echte Einschränkung für Implementierer: Wenn eine Anwendung beliebige binäre Blobs verschlüsseln muss, braucht sie eine zusätzliche Kodierung oder ein anderes Containerformat.

## Einschränkungen

NIP-44 bietet nicht:
- **Forward Secrecy**: Kompromittierte Schlüssel legen vergangene Nachrichten offen
- **Post-Compromise Security**: Wiederherstellung nach Schlüsselkompromittierung
- **Deniability**: Nachrichten sind nachweisbar von bestimmten Schlüsseln signiert
- **Metadata Hiding**: Die Relay-Architektur begrenzt die Privatsphäre

Für hohe Sicherheitsanforderungen liefern NIP-104, Double Ratchet, oder MLS-basierte Protokolle wie Marmot stärkere Garantien.

## Geschichte

NIP-44 Revision 3 wurde im Dezember 2023 nach einem unabhängigen Cure53-Sicherheitsaudit gemergt. Sie bildet die kryptographische Grundlage für NIP-17 Private DMs und NIP-59 Gift Wrapping.

---

**Primärquellen:**
- [NIP-44 Specification](https://github.com/nostr-protocol/nips/blob/master/44.md)
- [NIP-44 Reference Implementations](https://github.com/paulmillr/nip44)
- [Cure53 Audit Report](https://cure53.de/audit-report_nip44-implementations.pdf)

**Erwähnt in:**
- [Newsletter #4: NIP Deep Dive](/de/newsletters/2026-01-07-newsletter/)
- [Newsletter #3: December 2023](/de/newsletters/2025-12-31-newsletter/)
- [Newsletter #3: December 2024](/de/newsletters/2025-12-31-newsletter/)
- [Newsletter #12: Marmot](/de/newsletters/2026-03-04-newsletter/)
- [Newsletter #13: Vector](/en/newsletters/2026-03-11-newsletter/)
- [Newsletter #19: nostter NIP-44 migration](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: nowhere encrypts Nostr traffic](/en/newsletters/2026-04-22-newsletter/)

**Siehe auch:**
- [NIP-04: Encrypted Direct Messages (deprecated)](/de/topics/nip-04/)
- [NIP-17: Private Direct Messages](/de/topics/nip-17/)
- [NIP-59: Gift Wrap](/de/topics/nip-59/)
- [NIP-104: Double Ratchet Encryption](/de/topics/nip-104/)
- [MLS: Message Layer Security](/de/topics/mls/)
