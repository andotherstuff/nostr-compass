---
title: "NIP-4E: Separazione della cifratura dall'identità"
date: 2026-07-15
translationOf: /en/topics/nip-4e.md
translationDate: 2026-07-15
draft: false
categories:
  - NIP
  - Protocol
  - Encryption
---

NIP-4E è una bozza aperta, proposta da fiatjaf, per condividere dati privati tra i dispositivi di uno stesso utente senza che ogni dispositivo detenga la chiave di identità Nostr principale dell'utente. Non è stata unita al repository e resta una proposta `draft`/`optional`.

## Il problema che affronta

Molti NIP esistenti, tra cui le liste NIP-51 e i wallet Cashu NIP-60, cifrano i dati dall'utente verso sé stesso usando la chiave di identità, in modo da poterli rileggere in seguito su qualsiasi dispositivo. Questo meccanismo si interrompe quando la chiave di identità non è direttamente accessibile, ad esempio quando un remote signer è protetto da share FROST di soglia, MuSig2 o un enclave sicuro in hosting, perché cifrare e decifrare richiede in quel caso un round trip verso il signer ogni volta. Rende inoltre impossibile la cifratura offline ogni volta che la chiave di firma risiede in un bunker remoto.

## Come funziona

NIP-4E separa una "client key" per dispositivo da una "encryption key" condivisa che non è la chiave di identità dell'utente:

1. Il primo client configurato dall'utente genera una coppia di chiavi di cifratura casuali e ne annuncia la metà pubblica in un event `kind:10044` firmato dalla chiave di identità dell'utente.
2. Qualsiasi altro client che desideri cifrare o decifrare dati per quell'utente calcola il proprio segreto condiviso Diffie-Hellman rispetto alla chiave di cifratura annunciata anziché alla chiave di identità.
3. Quando un secondo dispositivo installa un nuovo client, quel client genera la propria "client key" locale e pubblica un annuncio `kind:4454` (anch'esso firmato dalla chiave di identità dell'utente) chiedendo al primo client di condividere la chiave di cifratura.
4. Il client originale rileva il nuovo annuncio `kind:4454`, cifra la chiave di cifratura condivisa verso la chiave del nuovo client usando [NIP-44](/it/topics/nip-44/) e la pubblica affinché il nuovo client possa decifrarla e utilizzarla da quel momento in poi.

Il risultato è che cifratura e decifratura non richiedono più di interrogare il signer della chiave di identità una volta che un client possiede localmente la chiave di cifratura condivisa, e una configurazione con remote signer (FROST, MuSig2, enclave in hosting) può essere utilizzata per l'identità mentre la cifratura ordinaria resta veloce e funziona offline.

## Perché è importante

NIP-4E è citato come fondamento per altre proposte che necessitano di una chiave simmetrica a livello di drive o di account senza dipendere da un remote signer per ogni chiamata di cifratura/decifratura, tra cui una proposta di drive cifrato privato ([PR #2412](https://github.com/nostr-protocol/nips/pull/2412)) e una versione più ristretta della stessa idea specifica per NIP-17 ([PR #2361](https://github.com/nostr-protocol/nips/pull/2361)). Entrambe restano aperte insieme a NIP-4E stesso, rendendo quest'area una parte attiva e non ancora definita del protocollo piuttosto che un elemento costruttivo già concluso.

---

**Fonti primarie:**
- [Bozza NIP-4E, PR #1647](https://github.com/nostr-protocol/nips/pull/1647)

**Menzionato in:**
- [Newsletter #31: Aperto: il drive cifrato privato estende NIP-4E](/it/newsletters/2026-07-15-newsletter/#open-private-encrypted-drive-extends-nip-4e)

**Vedi anche:**
- [NIP-44: Encrypted Payloads](/it/topics/nip-44/)
- [NIP-17: Private Direct Messages](/it/topics/nip-17/)
- [NIP-46: Nostr Connect](/it/topics/nip-46/)
- [FROST](/it/topics/frost/)
