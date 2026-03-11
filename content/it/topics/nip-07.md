---
title: "NIP-07: Firmatario tramite estensione del browser"
date: 2026-01-28
translationOf: /en/topics/nip-07.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - Signing
  - Security
---
NIP-07 definisce un'interfaccia standard che permette alle estensioni del browser di fornire capacità di firma ai client Nostr basati sul web, mantenendo le chiavi private al sicuro nell'estensione invece di esporle ai siti web.

## Come funziona

Le estensioni del browser iniettano un oggetto `window.nostr` che le web app possono usare:

```javascript
// Get public key
const pubkey = await window.nostr.getPublicKey();

// Sign an event
const signedEvent = await window.nostr.signEvent(unsignedEvent);

// Encrypt (NIP-04, legacy)
const ciphertext = await window.nostr.nip04.encrypt(pubkey, plaintext);

// Decrypt (NIP-04, legacy)
const plaintext = await window.nostr.nip04.decrypt(pubkey, ciphertext);

// NIP-44 methods (modern, if supported)
// const ciphertext = await window.nostr.nip44.encrypt(pubkey, plaintext);
// const plaintext = await window.nostr.nip44.decrypt(pubkey, ciphertext);
```

## Modello di sicurezza

- **Isolamento delle chiavi**: Le chiavi private non lasciano mai l'estensione
- **Approvazione dell'utente**: Le estensioni possono chiedere conferma per ogni richiesta di firma
- **Controllo del dominio**: Le estensioni possono limitare quali siti possono richiedere firme

NIP-07 migliora la custodia delle chiavi, ma non elimina la fiducia richiesta nell'estensione stessa. Un'estensione malevola o compromessa può comunque firmare la cosa sbagliata, perdere metadata o concedere permessi troppo ampi.

## Note sull'interoperabilità

La parte più difficile di NIP-07 non è la forma dell'API. È la variazione delle capacità. Alcune estensioni supportano solo `getPublicKey()` e `signEvent()`. Altre espongono anche `nip04`, `nip44` o metodi opzionali più recenti. Le web app hanno bisogno di feature detection e fallback ragionevoli invece di presumere che ogni signer iniettato si comporti allo stesso modo.

Anche la UX di approvazione dell'utente cambia il comportamento. Un sito che si aspetta in silenzio l'accesso in background può funzionare con un'estensione e sembrare rotto con un'altra che chiede conferma per ogni richiesta. Le buone app NIP-07 trattano la firma come un confine di permesso interattivo.

## Stato delle implementazioni

Le estensioni NIP-07 più diffuse includono:
- **Alby** - Wallet Lightning con firma Nostr
- **nos2x** - Signer Nostr leggero
- **Flamingo** - Estensione Nostr ricca di funzionalità

## Limiti

- Solo browser, nessun supporto mobile
- Richiede l'installazione di un'estensione
- Ogni estensione ha una UX diversa per le approvazioni

Per la firma tra dispositivi o su mobile, NIP-46 e NIP-55 di solito sono più adatti.

---

**Fonti primarie:**
- [NIP-07 Specification](https://github.com/nostr-protocol/nips/blob/master/07.md)
- [PR #2233](https://github.com/nostr-protocol/nips/pull/2233) - proposta `peekPublicKey()`

**Citato in:**
- [Newsletter #7: NIP Updates](/it/newsletters/2026-01-28-newsletter/#nip-updates)
- [Newsletter #8: News](/it/newsletters/2026-02-04-newsletter/#news)
- [Newsletter #11: News](/it/newsletters/2026-02-25-newsletter/#news)

**Vedi anche:**
- [NIP-04: Messaggi diretti cifrati (Deprecato)](/it/topics/nip-04/)
- [NIP-44: Encrypted Payloads](/it/topics/nip-44/)
- [NIP-46: Nostr Connect](/it/topics/nip-46/)
- [NIP-55: Applicazioni signer per Android](/it/topics/nip-55/)
