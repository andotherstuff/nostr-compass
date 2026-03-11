---
title: "NIP-49: Verschlüsselung privater Schlüssel"
date: 2026-03-11
translationOf: /en/topics/nip-49.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Key Management
  - Security
---

NIP-49 definiert, wie ein Client den privaten Schlüssel eines Nutzers mit einem Passwort verschlüsseln und das Ergebnis als `ncryptsec`-String kodieren kann. Ziel ist Portabilität mit stärkeren Standards als beim Speichern eines rohen `nsec`, während sich der verschlüsselte Schlüssel weiterhin leicht zwischen Clients bewegen lässt.

## Wie es funktioniert

Der Client beginnt mit dem rohen 32-Byte-secp256k1-Private-Key, nicht mit einem Hex- oder bech32-String. Er leitet mit scrypt aus dem Passwort des Nutzers einen temporären symmetrischen Schlüssel ab, unter Verwendung eines zufälligen Salt pro Schlüssel und eines anpassbaren Arbeitsfaktors, der als `LOG_N` gespeichert wird. Danach verschlüsselt er den Private-Key mit XChaCha20-Poly1305, stellt Versions- und Schlüsselhandhabungs-Metadaten voran und kodiert das Ergebnis als bech32 mit dem Präfix `ncryptsec`.

```json
{
  "id": "4d47f4f0a6f6edbc1bbd7f4e2a45ec68f27cba91d6c6ab5cf28d8d87b0f3d57e",
  "pubkey": "1f8b4c3e7b0f9451d4f9b8a7c6e5d4c3b2a1908f7e6d5c4b3a29181716151413",
  "created_at": 1741699200,
  "kind": 30078,
  "tags": [
    ["d", "encrypted-key-backup"],
    ["format", "ncryptsec"],
    ["encryption", "nip49"]
  ],
  "content": "ncryptsec1qgg9947rlpvqu76pj5ecreduf9jxhselq2nae2kghhvd5g7dgjtcxfqtd67p9m0w57lspw8gsq6yphnm8623nsl8xn9j4jdzz84zm3frztj3z7s35vpzmqf6ksu8r89qk5z2zxfmu5gv8th8wclt0h4p",
  "sig": "6a8f6e4b2d1901735f0ad4b6e8c1f3a579d0e2b4c6f8a1d3e5f7091b2c3d4e5f11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

Das Event oben ist ein Beispielcontainer, keine NIP-49-Anforderung. NIP-49 standardisiert das Format des verschlüsselten Schlüssels selbst, nicht einen eigenen Event-kind für dessen Veröffentlichung. Clients können ein `ncryptsec` lokal speichern, über app-spezifischen Speicher synchronisieren oder als Backup-Export darstellen.

## Sicherheitsmodell

NIP-49 macht zwei Dinge gleichzeitig. Es verwandelt ein Nutzerpasswort in einen echten Verschlüsselungsschlüssel, und es verlangsamt Bruteforce-Wiederherstellungsversuche mit einer speicherharten KDF. Der Arbeitsfaktor ist wichtig. Höhere `LOG_N`-Werte machen die Entschlüsselung für legitime Nutzer langsamer, erhöhen aber auch die Kosten für Offline-Raten durch Angreifer.

Das Format trägt außerdem ein Ein-Byte-Flag, das beschreibt, ob der Schlüssel vor der Verschlüsselung jemals unsicher behandelt wurde. Das ändert den Ciphertext selbst nicht, gibt Clients aber eine Möglichkeit, zwischen einem neu erzeugten geschützten Backup und einem Schlüssel zu unterscheiden, der schon im Klartext herumgereicht wurde, bevor er verpackt wurde.

## Hinweise zur Implementierung

- Passwörter werden vor der Schlüsselableitung auf Unicode NFKC normalisiert, damit dasselbe Passwort über Clients hinweg konsistent eingegeben werden kann.
- XChaCha20-Poly1305 verwendet einen 24-Byte-Nonce und authentifizierte Verschlüsselung, daher schlägt Manipulation am Ciphertext bei der Entschlüsselung sauber fehl.
- Der symmetrische Schlüssel sollte nach der Verwendung genullt und verworfen werden.
- Die Spezifikation empfiehlt nicht, verschlüsselte Schlüssel auf öffentliche Relays zu posten, weil das Sammeln vieler verschlüsselter Schlüssel die Offline-Cracking-Position eines Angreifers verbessert.

## Implementierungen

- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - Fügt Signup-Kompatibilität mit NIP-49-verschlüsselten privaten Schlüsseln hinzu

---

**Primärquellen:**
- [NIP-49 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/49.md)
- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - Client-seitiger Signup-Flow mit NIP-49

**Erwähnt in:**
- [Newsletter #13: Formstr](/de/newsletters/2026-03-11-newsletter/#formstr)
- [Newsletter #13: NIP Deep Dive](/de/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-49-private-key-encryption)

**Siehe auch:**
- [NIP-46: Nostr Connect](/de/topics/nip-46/)
- [NIP-55: Android Signer Application](/de/topics/nip-55/)
