---
title: "NIP-07: Signer per Estensione Browser"
date: 2026-01-28
translationOf: /en/topics/nip-07.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Signing
  - Security
---

NIP-07 definisce un'interfaccia standard per le estensioni browser per fornire capacità di firma ai client Nostr basati su web, mantenendo le chiavi private sicure nell'estensione invece di esporle ai siti web.

## Come Funziona

Le estensioni browser iniettano un oggetto `window.nostr` che le web app possono usare:

```javascript
// Ottieni la chiave pubblica
const pubkey = await window.nostr.getPublicKey();

// Firma un evento
const signedEvent = await window.nostr.signEvent(unsignedEvent);

// Crittografa (NIP-04, legacy)
const ciphertext = await window.nostr.nip04.encrypt(pubkey, plaintext);

// Decrittografa (NIP-04, legacy)
const plaintext = await window.nostr.nip04.decrypt(pubkey, ciphertext);

// Metodi NIP-44 (moderni, se supportati)
// const ciphertext = await window.nostr.nip44.encrypt(pubkey, plaintext);
// const plaintext = await window.nostr.nip44.decrypt(pubkey, ciphertext);
```

## Modello di Sicurezza

- **Isolamento Chiavi**: Le chiavi private non lasciano mai l'estensione
- **Approvazione Utente**: Le estensioni possono richiedere conferma per ogni richiesta di firma
- **Controllo Dominio**: Le estensioni possono limitare quali siti possono richiedere firme

## Implementazioni

Le estensioni NIP-07 popolari includono:
- **Alby** - Wallet Lightning con firma Nostr
- **nos2x** - Signer Nostr leggero
- **Flamingo** - Estensione Nostr ricca di funzionalità

## Limitazioni

- Solo browser (nessun supporto mobile)
- Richiede installazione dell'estensione
- Ogni estensione ha UX diverse per le approvazioni

## Alternative

- [NIP-46](/it/topics/nip-46/) - Firma remota via relay Nostr
- [NIP-55](/it/topics/nip-55/) - Signer locale Android

## Correlati

- [NIP-44](/it/topics/nip-44/) - Crittografia moderna (sostituzione di NIP-04)
- [NIP-46](/it/topics/nip-46/) - Firma Remota
