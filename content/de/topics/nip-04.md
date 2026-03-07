---
title: "NIP-04: Verschlüsselte Direktnachrichten (Veraltet)"
date: 2025-12-31
translationOf: /en/topics/nip-04.md
translationDate: 2026-03-07
draft: false
categories:
  - Datenschutz
  - Messaging
---

NIP-04 definiert verschlüsselte Direktnachrichten mit Kind-4-Events und einem per ECDH abgeleiteten gemeinsamen Geheimnis. Es war Nostrs erstes DM-Schema, ist heute aber Legacy-Technik, und neue Arbeit an privaten Nachrichten ist zu NIP-17 weitergezogen.

## Wie es funktioniert

Nachrichten verwenden Kind-4-Events mit diesem grundlegenden Ablauf:

1. Der Sender leitet mit secp256k1 ECDH ein gemeinsames Geheimnis ab.
2. Der Klartext wird mit AES-256-CBC verschlüsselt.
3. Das Event enthält ein `p`-Tag, das den Empfänger benennt.
4. Der Chiffretext wird als base64 kodiert und zusammen mit dem IV in `content` gespeichert.

Das Event selbst bleibt ein normales signiertes Nostr-Event, daher können Relays die äußeren Metadaten sehen, obwohl sie den Klartext nicht lesen können.

## Sicherheits- und Datenschutzgrenzen

NIP-04 hat deutliche Schwachen beim Datenschutz:

- **Metadatenleck** - Der Pubkey des Senders ist bei jeder Nachricht öffentlich sichtbar
- **Keine Absender-Privatsphäre** - Jeder kann sehen, wer mit wem Nachrichten austauscht
- **Exakte Zeitstempel** - Der Nachrichtenzeitpunkt wird nicht randomisiert
- **Nicht standardisierte Schlüsselverarbeitung** - Das Schema verwendet nur die X-Koordinate des ECDH-Punkts, was korrekte Implementierungen über Bibliotheken hinweg erschwert und wenig Spielraum für die Weiterentwicklung des Protokolls lässt

Die Spezifikation warnt ausdrücklich davor, dass sie "nicht einmal annähernd dem Stand der Technik in verschlüsselter Kommunikation" entspricht.

## Warum es ersetzt wurde

NIP-04 verschlüsselt den Nachrichteninhalt, verbirgt aber den sozialen Graphen nicht. Relay-Betreiber können weiterhin sehen, wer das Event gesendet hat, wer es empfängt und wann es veröffentlicht wurde. Diese Metadaten reichen aus, um Gespräche abzubilden, auch ohne die Payload zu entschlüsseln.

NIP-17 begegnet dem, indem es NIP-44-Payload-Verschlüsselung mit NIP-59 gift wrapping kombiniert. Dadurch wird der Sender vor Relays und zufälligen Beobachtern verborgen. Neue Implementierungen sollten NIP-04 nur noch als Kompatibilitätsschicht behandeln.

## Implementierungsstatus

Legacy-Clients und Signer bieten weiterhin NIP-04-Methoden zum Ver- und Entschlüsseln an, weil alte Unterhaltungen und ältere Apps noch im Umlauf sind. Diese Kompatibilität ist für Migrationen wichtig, aber neue Funktionen auf Kind-4-Events aufzubauen, bedeutet meist, die alten Datenschutzgrenzen weiterzutragen.

---

**Primärquellen:**
- [NIP-04 Specification](https://github.com/nostr-protocol/nips/blob/master/04.md)

**Erwähnt in:**
- [Newsletter #4: NIP Deep Dive](/en/newsletters/2026-01-07-newsletter/#nip-04-encrypted-direct-messages-legacy)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Siehe auch:**
- [NIP-44: Encrypted Payloads](/de/topics/nip-44/)
- [NIP-17: Private Direct Messages](/de/topics/nip-17/)
- [NIP-59: Gift Wrap](/de/topics/nip-59/)
