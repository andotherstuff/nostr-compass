---
title: "NIP-19: Entità codificate Bech32"
date: 2025-12-17
translationOf: /en/topics/nip-19/
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Identity
---
NIP-19 definisce formati facili da leggere per condividere identificatori Nostr. Queste stringhe codificate in bech32 vengono usate per visualizzazione e condivisione, ma non vengono mai usate nel protocollo stesso, che usa hex.

## Come funziona

Le chiavi hex grezze sono soggette a errori di copia e visivamente indistinguibili. La codifica bech32 aggiunge un prefisso leggibile dalle persone e un checksum, rendendo chiaro quale tipo di dato si sta guardando e intercettando molti errori di copia.

Le forme di base codificano un singolo valore di 32 byte:

- **npub** - Chiave pubblica (la tua identità, sicura da condividere)
- **nsec** - Chiave privata (da tenere segreta, usata per firmare)
- **note** - ID evento (fa riferimento a un evento specifico)

Esempio: la pubkey hex `3bf0c63f...` diventa `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`.

Le forme estese usano la codifica TLV così possono trasportare relay hint insieme all'identificatore stesso:

- **nprofile** - Profilo con relay hint
- **nevent** - Evento con relay hint, pubkey dell'autore e kind
- **naddr** - Riferimento a evento addressable con pubkey, kind, tag `d` e relay hint

## Perché è importante

I relay hint non sono autorevoli, ma spesso decidono se un client può recuperare un evento condiviso al primo tentativo. Per questo `nevent`, `nprofile` e `naddr` sono di solito formati di condivisione migliori rispetto a valori `note` o `npub` nudi, quando il contenuto vive fuori dall'insieme corrente di relay del destinatario.

Un'altra distinzione pratica è la stabilità. `note` punta a un singolo event id immutabile, mentre `naddr` punta a un evento addressable che può essere sostituito nel tempo. Per contenuti long-form, calendari o annunci di repository, `naddr` è di solito il tipo di link corretto.

## Note di implementazione

- Usa bech32 solo per interfacce umane: visualizzazione, copia e incolla, codici QR, URL
- Non usare mai i formati bech32 nei messaggi di protocollo, negli eventi o nelle risposte NIP-05
- Tutta la comunicazione di protocollo deve usare la codifica hex
- Quando generi nevent/nprofile/naddr, includi relay hint per una migliore individuabilità
- Tratta `nsec` come materiale segreto ovunque. Un client non dovrebbe mai mostrarlo per impostazione predefinita, registrarlo nei log o includerlo nelle esportazioni di supporto

---

**Fonti principali:**
- [Specifica NIP-19](https://github.com/nostr-protocol/nips/blob/master/19.md)

**Menzionato in:**
- [Newsletter #1: NIP Deep Dive](/en/newsletters/2025-12-17-newsletter/#nip-19-bech32-encoded-identifiers)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #3: Notable Code Changes](/en/newsletters/2025-12-31-newsletter/#damus-ios)
- [Newsletter #4: Relay Hint Support](/en/newsletters/2026-01-07-newsletter/)
- [Newsletter #8: Damus iOS](/en/newsletters/2026-02-04-newsletter/#damus-ios)
- [Newsletter #11: notecrumbs](/en/newsletters/2026-02-25-newsletter/)

**Vedi anche:**
- [NIP-01: Basic Protocol](/it/topics/nip-01/)
- [NIP-10: Reply Threads](/it/topics/nip-10/)
