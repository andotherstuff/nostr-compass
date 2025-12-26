---
title: "NIP-19: Entita' Codificate Bech32"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Identity
---

NIP-19 definisce formati user-friendly per condividere identificatori Nostr. Queste stringhe codificate bech32 sono usate per visualizzazione e condivisione ma non sono mai usate nel protocollo stesso (che usa esadecimale).

## Perche' Bech32?

Le chiavi esadecimali grezze sono soggette a errori nella copia e visualmente indistinguibili. La codifica bech32 aggiunge un prefisso leggibile e un checksum, rendendo immediatamente chiaro che tipo di dato state guardando.

## Formati Base

Questi codificano valori grezzi a 32 byte:

- **npub** - Chiave pubblica (la vostra identita', sicura da condividere)
- **nsec** - Chiave privata (mantenere segreta, usata per firmare)
- **note** - ID evento (referenzia un evento specifico)

Esempio: La pubkey esadecimale `3bf0c63f...` diventa `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`.

## Identificatori Condivisibili

Questi usano codifica TLV (Type-Length-Value) per includere metadati:

- **nprofile** - Profilo con suggerimenti relay (aiuta i client a trovare l'utente)
- **nevent** - Evento con suggerimenti relay, pubkey autore e kind
- **naddr** - Riferimento evento indirizzabile (pubkey + kind + tag-d + relay)

Questi risolvono il problema della scoperta: quando qualcuno condivide un ID nota, come fanno i client a sapere quale relay ce l'ha? Raggruppando suggerimenti relay nell'identificatore, i link condivisi diventano piu' affidabili.

## Note di Implementazione

- Usate bech32 solo per interfacce umane: visualizzazione, copia/incolla, codici QR, URL
- Non usate mai formati bech32 nei messaggi del protocollo, eventi o risposte NIP-05
- Tutta la comunicazione del protocollo deve usare codifica esadecimale
- Quando generate nevent/nprofile/naddr, includete suggerimenti relay per migliore reperibilita'

---

**Fonti primarie:**
- [Specifica NIP-19](https://github.com/nostr-protocol/nips/blob/master/19.md)

**Menzionato in:**
- [Newsletter #1: Approfondimento NIP](/it/newsletters/2025-12-17-newsletter/#nip-19-bech32-encoded-identifiers)

**Vedi anche:**
- [NIP-01: Protocollo Base](/it/topics/nip-01/)
- [NIP-21: Schema URI nostr:](https://github.com/nostr-protocol/nips/blob/master/21.md)

