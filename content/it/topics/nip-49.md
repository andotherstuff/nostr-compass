---
title: "NIP-49: Cifratura della Chiave Privata"
date: 2026-03-11
translationOf: /en/topics/nip-49.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Key Management
  - Security
---

NIP-49 definisce come un client può cifrare la chiave privata di un utente con una password e codificare il risultato come stringa `ncryptsec`. L'obiettivo è la portabilità con valori predefiniti più sicuri rispetto allo storage di un `nsec` grezzo, mantenendo comunque la chiave cifrata facile da spostare tra i client.

## Come Funziona

Il client parte dalla chiave privata secp256k1 grezza a 32 byte, non una stringa hex o bech32. Deriva una chiave simmetrica temporanea dalla password dell'utente con scrypt, usando un salt casuale per ogni chiave e un fattore di lavoro regolabile memorizzato come `LOG_N`. Poi cifra la chiave privata con XChaCha20-Poly1305, antepone i metadati di versionamento e gestione della chiave, e codifica il risultato in bech32 con il prefisso `ncryptsec`.

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

L'event sopra è un contenitore di esempio, non un requisito NIP-49. NIP-49 standardizza il formato della chiave cifrata in sé, non un kind di event dedicato per pubblicarla. I client possono memorizzare un `ncryptsec` localmente, sincronizzarlo tramite storage specifico dell'app, o presentarlo come esportazione di backup.

## Modello di Sicurezza

NIP-49 fa due cose contemporaneamente. Trasforma una password utente in una chiave di cifratura appropriata, e rallenta i tentativi di recupero con forza bruta tramite una KDF memory-hard. Il fattore di lavoro è importante. Valori `LOG_N` più alti rendono la decifratura più lenta per gli utenti legittimi, ma alzano anche il costo delle ipotesi offline per gli attaccanti.

Il formato include anche un flag di un byte che descrive se la chiave è mai stata gestita in modo insicuro prima della cifratura. Questo non cambia il testo cifrato in sé, ma dà ai client un modo per distinguere un backup protetto appena generato da una chiave che era già stata copiata in chiaro prima di essere avvolta.

## Note sull'Implementazione

- Le password sono normalizzate in Unicode NFKC prima della derivazione della chiave, così la stessa password può essere inserita in modo coerente tra i client.
- XChaCha20-Poly1305 usa un nonce di 24 byte e cifratura autenticata, quindi la manomissione del testo cifrato fallisce in modo pulito durante la decifratura.
- La chiave simmetrica dovrebbe essere azzerata e scartata dopo l'uso.
- La specifica non raccomanda di pubblicare chiavi cifrate su relay pubblici, perché raccogliere molte chiavi cifrate migliora la posizione di cracking offline di un attaccante.

## Implementazioni

- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - Aggiunge compatibilità alla registrazione usando chiavi private cifrate NIP-49

---

**Fonti primarie:**
- [Specifica NIP-49](https://github.com/nostr-protocol/nips/blob/master/49.md)
- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - Flusso di registrazione lato client usando NIP-49

**Menzionato in:**
- [Newsletter #13: Formstr](/en/newsletters/2026-03-11-newsletter/#formstr)
- [Newsletter #13: NIP Deep Dive](/en/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-49-private-key-encryption)

**Vedi anche:**
- [NIP-46: Nostr Connect](/it/topics/nip-46/)
- [NIP-55: Applicazione Signer Android](/it/topics/nip-55/)
