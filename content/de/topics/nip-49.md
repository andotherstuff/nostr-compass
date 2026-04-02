---
title: "NIP-49: Private Key Encryption"
date: 2026-03-11
translationOf: /en/topics/nip-49.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Key Management
  - Security
---

NIP-49 definiert, wie ein Client den privaten Schlüssel eines Nutzers mit einem Passwort verschlüsseln und das Ergebnis als `ncryptsec`-String kodieren kann. Das Ziel ist Portabilität mit stärkeren Standardeinstellungen als die Speicherung eines rohen `nsec`, wobei der verschlüsselte Schlüssel weiterhin leicht zwischen Clients übertragen werden kann.

## Funktionsweise

Der Client beginnt mit dem rohen 32-Byte-secp256k1-Privatschlüssel, nicht einem Hex- oder Bech32-String. Er leitet einen temporären symmetrischen Schlüssel aus dem Passwort des Nutzers mit scrypt ab, unter Verwendung eines pro Schlüssel zufälligen Salts und eines einstellbaren Arbeitsfaktors, der als `LOG_N` gespeichert wird. Anschließend verschlüsselt er den privaten Schlüssel mit XChaCha20-Poly1305, stellt Versionierung und Schlüsselbehandlungs-Metadaten voran und Bech32-kodiert das Ergebnis unter dem `ncryptsec`-Präfix.

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

Das obige Event ist ein Beispiel-Container, keine NIP-49-Anforderung. NIP-49 standardisiert das verschlüsselte Schlüsselformat selbst, nicht einen dedizierten Event-Kind für dessen Veröffentlichung. Clients können einen `ncryptsec` lokal speichern, über App-spezifischen Speicher synchronisieren oder als Backup-Export präsentieren.

## Sicherheitsmodell

NIP-49 leistet zwei Dinge gleichzeitig. Es verwandelt ein Nutzerpasswort in einen ordentlichen Verschlüsselungsschlüssel und verlangsamt Brute-Force-Wiederherstellungsversuche mit einer speicherharten KDF. Der Arbeitsfaktor ist entscheidend. Höhere `LOG_N`-Werte machen die Entschlüsselung für legitime Nutzer langsamer, erhöhen aber auch die Kosten des Offline-Ratens für Angreifer.

Das Format trägt auch ein Ein-Byte-Flag, das beschreibt, ob der Schlüssel jemals unsicher gehandhabt wurde, bevor er verschlüsselt wurde. Das ändert den Chiffretext selbst nicht, gibt Clients aber eine Möglichkeit, ein neu generiertes geschütztes Backup von einem Schlüssel zu unterscheiden, der bereits als Klartext herumkopiert wurde, bevor er verpackt wurde.

## Implementierungshinweise

- Passwörter werden vor der Schlüsselableitung zu Unicode NFKC normalisiert, damit dasselbe Passwort konsistent über Clients eingegeben werden kann.
- XChaCha20-Poly1305 verwendet eine 24-Byte-Nonce und authentifizierte Verschlüsselung, sodass eine Manipulation des Chiffretexts bei der Entschlüsselung sauber fehlschlägt.
- Der symmetrische Schlüssel sollte nach Gebrauch genullt und verworfen werden.
- Die Spezifikation empfiehlt nicht, verschlüsselte Schlüssel auf öffentlichen Relays zu veröffentlichen, da das Sammeln vieler verschlüsselter Schlüssel die Offline-Cracking-Position eines Angreifers verbessert.

## Implementierungen

- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - Fügt Anmelde-Kompatibilität mit NIP-49-verschlüsselten privaten Schlüsseln hinzu

---

**Primärquellen:**
- [NIP-49-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/49.md)
- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - Client-seitiger Anmelde-Flow mit NIP-49

**Erwähnt in:**
- [Newsletter #13: Formstr](/en/newsletters/2026-03-11-newsletter/#formstr)
- [Newsletter #13: NIP Deep Dive](/en/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-49-private-key-encryption)

**Siehe auch:**
- [NIP-46: Nostr Connect](/de/topics/nip-46/)
- [NIP-55: Android Signer Application](/de/topics/nip-55/)
