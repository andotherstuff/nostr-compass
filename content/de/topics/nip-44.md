---
title: "NIP-44: Verschlüsselte Payloads"
date: 2025-12-31
translationOf: /en/topics/nip-44.md
translationDate: 2025-12-31
draft: false
categories:
  - NIP
  - Kryptographie
  - Datenschutz
---

NIP-44 definiert einen versionierten Verschlüsselungsstandard für Nostr-Payloads und ersetzt das fehlerhafte NIP-04-Verschlüsselungsschema durch moderne kryptographische Primitive.

## Wie Es Funktioniert

NIP-44 Version 2 verwendet einen mehrstufigen Verschlüsselungsprozess:

1. **Schlüsselvereinbarung**: ECDH (secp256k1) zwischen den öffentlichen Schlüsseln von Sender und Empfänger erzeugt ein gemeinsames Geheimnis
2. **Schlüsselableitung**: HKDF-extract mit SHA256 und Salt `nip44-v2` erstellt einen Konversationsschlüssel
3. **Pro-Nachricht-Schlüssel**: HKDF-expand leitet ChaCha-Schlüssel, Nonce und HMAC-Schlüssel aus einem zufälligen Nonce ab
4. **Padding**: Inhalt wird aufgefüllt, um die Nachrichtenlänge zu verbergen
5. **Verschlüsselung**: ChaCha20 verschlüsselt den aufgefüllten Inhalt
6. **Authentifizierung**: HMAC-SHA256 bietet Nachrichtenintegrität

## Kryptographische Entscheidungen

- **ChaCha20** über AES: Schneller, bessere Multi-Key-Angriffsresistenz
- **HMAC-SHA256** über Poly1305: Polynomiale MACs sind leichter zu fälschen
- **SHA256**: Konsistent mit bestehenden Nostr-Primitiven
- **Versioniertes Format**: Ermöglicht zukünftige Algorithmus-Upgrades

## Sicherheitseigenschaften

- **Authentifizierte Verschlüsselung**: Nachrichten können nicht manipuliert werden
- **Längenverbergung**: Padding verschleiert die Nachrichtengröße
- **Konversationsschlüssel**: Gleicher Schlüssel für laufende Konversationen reduziert Berechnung
- **Auditiert**: Cure53-Sicherheitsaudit fand keine ausnutzbaren Schwachstellen

## Einschränkungen

NIP-44 bietet nicht:
- **Forward Secrecy**: Kompromittierte Schlüssel legen vergangene Nachrichten offen
- **Post-Compromise Security**: Wiederherstellung nach Schlüsselkompromittierung
- **Abstreitbarkeit**: Nachrichten sind nachweislich von bestimmten Schlüsseln signiert
- **Metadaten-Verbergung**: Relay-Architektur begrenzt Privatsphäre

Für hohe Sicherheitsanforderungen bieten NIP-104 (Double Ratchet) oder MLS-basierte Protokolle wie Marmot stärkere Garantien.

## Geschichte

NIP-44 Revision 3 wurde im Dezember 2023 nach einem unabhängigen Cure53-Sicherheitsaudit zusammengeführt. Es bildet die kryptographische Grundlage für NIP-17 private DMs und NIP-59 Gift Wrapping.

---

**Primäre Quellen:**
- [NIP-44 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/44.md)
- [NIP-44 Referenzimplementierungen](https://github.com/paulmillr/nip44)
- [Cure53 Auditbericht](https://cure53.de/audit-report_nip44-implementations.pdf)

**Erwähnt in:**
- [Newsletter #3: Dezember 2023](/de/newsletters/2025-12-31-newsletter/#december-2023-ecosystem-maturation)
- [Newsletter #3: Dezember 2024](/de/newsletters/2025-12-31-newsletter/#december-2024-protocol-advancement)

**Siehe auch:**
- [NIP-04: Verschlüsselte Direktnachrichten (veraltet)](/de/topics/nip-04/)
- [NIP-17: Private Direktnachrichten](/de/topics/nip-17/)
- [NIP-59: Gift Wrap](/de/topics/nip-59/)
- [NIP-104: Double Ratchet Verschlüsselung](/de/topics/nip-104/)
- [MLS: Message Layer Security](/de/topics/mls/)
