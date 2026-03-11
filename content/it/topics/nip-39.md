---
title: "NIP-39: Identità esterne nei profili"
date: 2026-02-11
translationOf: /en/topics/nip-39.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Identity
---
NIP-39 definisce come gli utenti collegano affermazioni di identità esterna ai propri profili Nostr usando tag `i`. Questi tag collegano una pubkey Nostr ad account su piattaforme esterne come GitHub, Twitter, Mastodon o Telegram.

## Come funziona

Gli utenti pubblicano affermazioni di identità in eventi di kind 10011 come tag `i`. Ogni tag contiene un valore `platform:identity` più un puntatore alla prova che consente a un client di verificare l'affermazione:

```json
{
  "id": "5f1c7b7e2c6f3d4a9b0e6a2d8c1f7e3b4a6d9c0e1f2a3b4c5d6e7f8091a2b3c4",
  "pubkey": "3bf0c63fcb8d0d8b6a8fcb3c7f5cb2a972f8a0b5a3d6d8790bb2d4e4f0d6b1c2",
  "created_at": 1741699200,
  "kind": 10011,
  "tags": [
    ["i", "github:alice", "9f5df4e2a8b14c1f9e6d2b7c4a1e8f90"],
    ["i", "twitter:alice_dev", "1898123456789012345"]
  ],
  "content": "",
  "sig": "8f4c62d8a7e9b1c3d5f7091a2b4c6d8e0f1234567890abcdeffedcba09876543211223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

I client ricostruiscono l'URL della prova a partire dalla piattaforma e dal valore della prova, poi verificano che il post esterno contenga l'`npub` dell'utente. Questo mantiene l'affermazione portabile tra client senza richiedere un verificatore centrale.

## Modello di prova

Il dettaglio importante è che NIP-39 prova il controllo di due identità contemporaneamente: la chiave Nostr e l'account esterno. Se uno dei due lati di questa prova scompare, la verifica diventa più debole. Un gist o un tweet eliminato non invalida l'evento storico, ma rimuove la prova live da cui dipende la maggior parte dei client.

Un altro punto utile di implementazione è la strategia di fetch. Poiché le affermazioni ora vivono fuori dal kind 0, i client possono decidere se richiederle solo nelle viste di dettaglio del profilo, solo per gli utenti seguiti, o per niente. Questo evita di appesantire ulteriormente il già caldo percorso del kind 0.

## Implementazioni

- [Amethyst PR #1747](https://github.com/vitorpamplona/amethyst/pull/1747) - Pubblica identità esterne come eventi dedicati di kind 10011
- [PR #2256](https://github.com/nostr-protocol/nips/pull/2256) - Aggiunge il riferimento esplicito al registro kind 10011 al set di NIP

## Stato attuale

Secondo la spec attuale, le affermazioni di identità vivono in eventi kind 10011 dedicati invece che nei metadati kind 0. Questa separazione nasce dallo sforzo più ampio di alleggerire i fetch dei profili kind 0.

---

**Fonti primarie:**
- [NIP-39: External Identities in Profiles](https://github.com/nostr-protocol/nips/blob/master/39.md)
- [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) - Ha spostato le affermazioni di identità fuori dal kind 0
- [PR #2256](https://github.com/nostr-protocol/nips/pull/2256) - Ha aggiunto il riferimento esplicito al kind 10011

**Citato in:**
- [Newsletter #9: NIP Updates](/it/newsletters/2026-02-11-newsletter/#nip-updates)
- [Newsletter #12: Amethyst](/it/newsletters/2026-03-04-newsletter/#amethyst-nip-39-nip-c0-nip-66)
- [Newsletter #13: Aggiornamenti NIP](/it/newsletters/2026-03-11-newsletter/#aggiornamenti-nip)

**Vedi anche:**
- [NIP-05: Verifica del dominio](/it/topics/nip-05/)
