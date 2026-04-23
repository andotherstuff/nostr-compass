---
title: "NIP-04: Encrypted Direct Messages (Deprecated)"
date: 2025-12-31
translationOf: /en/topics/nip-04.md
translationDate: 2026-04-22
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-04 definiert verschlüsselte Direct Messages über kind-4-Events und ein per ECDH abgeleitetes Shared Secret. Es war Nostrs erstes DM-Schema, ist inzwischen aber Legacy-Technologie. Neue private Messaging-Arbeit ist zu NIP-17 weitergewandert.

## Funktionsweise

Nachrichten nutzen kind-4-Events mit diesem Grundablauf:

1. Der Sender leitet per secp256k1 ECDH ein Shared Secret ab.
2. Der plaintext wird mit AES-256-CBC verschlüsselt.
3. Das Event enthält ein `p`-Tag mit dem Empfänger.
4. Der Ciphertext wird zusammen mit der IV als base64 in `content` gespeichert.

Das Event selbst bleibt ein normal signiertes Nostr-Event. Relays sehen also weiterhin die äußeren Metadaten, auch wenn sie den plaintext nicht lesen können.

## Sicherheits- und Datenschutzgrenzen

NIP-04 hat deutliche Privatsphäre-Schwächen:

- **Metadata leakage** - Der pubkey des Senders ist bei jeder Nachricht öffentlich sichtbar
- **Keine Sender-Privatsphäre** - Jeder kann sehen, wer mit wem schreibt
- **Exakte Timestamps** - Das Nachrichtentiming wird nicht randomisiert
- **Nicht standardisierte Key-Behandlung** - Das Schema nutzt nur die X-Koordinate des ECDH-Punkts, was Cross-Library-Korrektheit erschwerte und wenig Raum für Protokollevolution ließ

Die Spezifikation warnt ausdrücklich, dass sie nicht annähernd dem state of the art verschlüsselter Kommunikation entspricht.

## Warum es ersetzt wurde

NIP-04 verschlüsselt den Nachrichteninhalt, verbirgt aber nicht den Social Graph. Relay-Betreiber können weiterhin sehen, wer das Event gesendet hat, wer es empfängt und wann es veröffentlicht wurde. Diese Metadaten reichen aus, um Gespräche zu kartieren, selbst ohne Entschlüsselung des Inhalts.

NIP-17 begegnet dem, indem es NIP-44-Payload-Verschlüsselung mit NIP-59-Gift-Wrapping kombiniert. Dadurch wird der Sender vor Relays und zufälligen Beobachtern verborgen. Neue Implementierungen sollten NIP-04 nur noch als Kompatibilitätsschicht behandeln.

## Implementierungsstand

Legacy-Clients und Signer bieten weiterhin NIP-04-Encrypt- und Decrypt-Methoden an, weil alte Konversationen und ältere Apps noch im Umlauf sind. Diese Kompatibilität ist für Migration wichtig. Neue Features auf kind-4-Events aufzubauen bedeutet aber meistens, alte Datenschutzgrenzen mitzuschleppen.

---

**Primärquellen:**
- [NIP-04 Specification](https://github.com/nostr-protocol/nips/blob/master/04.md)

**Erwähnt in:**
- [Newsletter #4: NIP Deep Dive](/de/newsletters/2026-01-07-newsletter/)
- [Newsletter #3: December Recap](/de/newsletters/2025-12-31-newsletter/)
- [Newsletter #19: nostter NIP-44 migration](/en/newsletters/2026-04-22-newsletter/)

**Siehe auch:**
- [NIP-44: Encrypted Payloads](/de/topics/nip-44/)
- [NIP-17: Private Direct Messages](/de/topics/nip-17/)
- [NIP-59: Gift Wrap](/de/topics/nip-59/)
