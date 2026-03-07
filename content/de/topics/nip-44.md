---
title: "NIP-44: Verschlüsselte Payloads"
date: 2025-12-31
translationOf: /en/topics/nip-44.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Kryptographie
  - Datenschutz
---

NIP-44 definiert einen versionierten Verschlüsselungsstandard für Nostr-Payloads und ersetzt das fehlerhafte NIP-04-Verschlüsselungsschema durch moderne kryptographische Primitive.

## Wie es funktioniert

NIP-44 Version 2 verwendet einen mehrstufigen Verschlüsselungsprozess:

1. **Schlüsselvereinbarung**: ECDH (secp256k1) zwischen den öffentlichen Schlüsseln von Sender und Empfänger erzeugt ein gemeinsames Geheimnis
2. **Schlüsselableitung**: HKDF-extract mit SHA256 und Salt `nip44-v2` erstellt einen Konversationsschlüssel
3. **Pro-Nachricht-Schlüssel**: HKDF-expand leitet ChaCha-Schlüssel, Nonce und HMAC-Schlüssel aus einem zufälligen Nonce ab
4. **Padding**: Inhalt wird aufgefüllt, um die Nachrichtenlänge zu verbergen
5. **Verschlüsselung**: ChaCha20 verschlüsselt den aufgefüllten Inhalt
6. **Authentifizierung**: HMAC-SHA256 liefert Nachrichtenintegrität

Die Ausgabe ist eine versionierte base64-Payload, die in ein normal signiertes Nostr-Event eingebettet wird. Die Spezifikation verlangt, dass Clients vor dem Entschlüsseln der inneren NIP-44-Payload zuerst die äußere NIP-01-Event-Signatur validieren.

## Kryptographische Entscheidungen

- **ChaCha20** statt AES: schneller und widerstandsfähiger gegen Multi-Key-Angriffe
- **HMAC-SHA256** statt Poly1305: Polynomial-MACs lassen sich leichter fälschen
- **SHA256**: konsistent mit bestehenden Nostr-Primitiven
- **Versioniertes Format**: ermöglicht spätere Algorithmus-Upgrades

## Sicherheitseigenschaften

- **Authentifizierte Verschlüsselung**: Nachrichten können nicht unbemerkt verändert werden
- **Längenverschleierung**: Padding verdeckt die Nachrichtengröße
- **Konversationsschlüssel**: derselbe Schlüssel für laufende Gespräche reduziert Rechenaufwand
- **Auditiert**: Das Cure53-Sicherheitsaudit fand keine ausnutzbaren Schwachstellen

## Implementierungshinweise

NIP-44 ist kein direkter Ersatz für NIP-04-Payloads. Es definiert ein Verschlüsselungsformat, aber keinen Event-Kind für Direktnachrichten. Protokolle wie [NIP-17](/de/topics/nip-17/) und [NIP-59](/de/topics/nip-59/) legen fest, wie verschlüsselte Payloads in realen Nachrichtenflüssen verwendet werden.

Die Plaintext-Eingabe ist UTF-8-Text mit einer Länge von 1 bis 65535 Bytes. Das ist eine echte Einschränkung für Implementierer: Wenn Ihre Anwendung beliebige binäre Blobs verschlüsseln muss, brauchen Sie eine zusätzliche Kodierung oder ein anderes Containerformat.

## Einschränkungen

NIP-44 bietet nicht:
- **Forward Secrecy**: Kompromittierte Schlüssel legen vergangene Nachrichten offen
- **Post-Compromise Security**: Wiederherstellung nach Schlüsselkompromittierung
- **Abstreitbarkeit**: Nachrichten sind nachweislich von bestimmten Schlüsseln signiert
- **Metadaten-Verschleierung**: Die Relay-Architektur begrenzt die Privatsphäre

Für hohe Sicherheitsanforderungen bieten NIP-104, also Double Ratchet, oder MLS-basierte Protokolle wie Marmot stärkere Garantien.

## Geschichte

NIP-44 Revision 3 wurde im Dezember 2023 nach einem unabhängigen Cure53-Sicherheitsaudit gemerged. Sie bildet die kryptographische Grundlage für NIP-17 Private DMs und NIP-59 Gift Wrap.

---

**Primärquellen:**
- [NIP-44 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/44.md)
- [NIP-44 Referenzimplementierungen](https://github.com/paulmillr/nip44)
- [Cure53 Audit Report](https://cure53.de/audit-report_nip44-implementations.pdf)

**Erwähnt in:**
- [Newsletter #4: NIP Deep Dive](/en/newsletters/2026-01-07-newsletter/#nip-44-versioned-encryption)
- [Newsletter #3: December 2023](/en/newsletters/2025-12-31-newsletter/#december-2023-ecosystem-maturation)
- [Newsletter #3: December 2024](/en/newsletters/2025-12-31-newsletter/#december-2024-protocol-advancement)
- [Newsletter #12: Marmot](/en/newsletters/2026-03-04-newsletter/#marmot-development-kit-ships-first-public-release)

**Siehe auch:**
- [NIP-04: Verschlüsselte Direktnachrichten (veraltet)](/de/topics/nip-04/)
- [NIP-17: Private Direktnachrichten](/de/topics/nip-17/)
- [NIP-59: Gift Wrap](/de/topics/nip-59/)
- [NIP-104: Double Ratchet Encryption](/de/topics/nip-104/)
- [MLS: Message Layer Security](/de/topics/mls/)
