---
title: "NIP-04: Verschlüsselte Direktnachrichten (Veraltet)"
date: 2025-12-31
translationOf: /en/topics/nip-04.md
translationDate: 2025-12-31
draft: false
categories:
  - Datenschutz
  - Messaging
---

NIP-04 definiert verschlüsselte Direktnachrichten mit AES-256-CBC-Verschlüsselung. Es war die ursprüngliche Methode für private Nachrichten auf Nostr, wurde aber aufgrund erheblicher Datenschutzbeschränkungen zugunsten von NIP-17 veraltet.

## Funktionsweise

Nachrichten verwenden kind-4-Events mit folgendem Verschlüsselungsschema:
1. Ein gemeinsames Geheimnis wird mittels ECDH mit dem öffentlichen Schlüssel des Empfängers und dem privaten Schlüssel des Absenders generiert
2. Die Nachricht wird mit AES-256-CBC verschlüsselt
3. Der Chiffretext wird base64-kodiert mit angehängtem Initialisierungsvektor
4. Ein `p`-Tag identifiziert den öffentlichen Schlüssel des Empfängers

## Sicherheitsbeschränkungen

NIP-04 hat erhebliche Datenschutzmängel:

- **Metadaten-Leck** - Die pubkey des Absenders ist bei jeder Nachricht öffentlich sichtbar
- **Keine Absender-Privatsphäre** - Jeder kann sehen, wer mit wem kommuniziert
- **Exakte Zeitstempel** - Nachrichtenzeitpunkte werden nicht randomisiert
- **Nicht-standardmäßige Implementierung** - Verwendet nur die X-Koordinate des ECDH-Punktes anstelle des Standard-SHA256-Hashs

Die Spezifikation warnt ausdrücklich, dass sie "nicht annähernd dem Stand der Technik in verschlüsselter Kommunikation entspricht".

## Veraltungsstatus

NIP-04 ist zugunsten von NIP-17 veraltet, das NIP-59 Gift Wrapping verwendet, um die Identität des Absenders zu verbergen. Neue Implementierungen sollten NIP-17 für private Nachrichten verwenden.

---

**Primärquellen:**
- [NIP-04-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/04.md)

**Erwähnt in:**
- [Newsletter #3: Dezember-Rückblick](/de/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Siehe auch:**
- [NIP-17: Private Direktnachrichten](/de/topics/nip-17/)
- [NIP-59: Gift Wrap](/de/topics/nip-59/)
