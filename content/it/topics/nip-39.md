---
title: "NIP-39: Identità esterne nei profili"
date: 2026-02-11
translationOf: /en/topics/nip-39.md
translationDate: 2026-03-07
draft: false
categories:
  - NIPs
  - Identity
---
NIP-39 definisce come gli utenti collegano affermazioni di identità esterna ai propri profili Nostr usando tag `i`. Questi tag collegano una pubkey Nostr ad account su piattaforme esterne come GitHub, Twitter, Mastodon o Telegram.

## Come funziona

Gli utenti pubblicano affermazioni di identità in eventi kind 10011 come tag `i`. Ogni tag contiene un valore `platform:identity` più un proof pointer che consente a un client di verificare l'affermazione:

```json
{
  "kind": 10011,
  "tags": [
    ["i", "github:username", "gist-id"],
    ["i", "twitter:handle", "tweet-id"]
  ]
}
```

I client ricostruiscono il proof URL a partire dalla piattaforma e dal valore della proof, poi verificano che il post esterno contenga l'`npub` dell'utente. Questo mantiene l'affermazione portabile tra client senza richiedere un verificatore centrale.

## Modello di proof

Il dettaglio importante è che NIP-39 prova il controllo di due identità contemporaneamente: la chiave Nostr e l'account esterno. Se uno dei due lati di questa proof scompare, la verifica diventa più debole. Un gist o un tweet eliminato non invalida l'evento storico, ma rimuove la proof live da cui dipende la maggior parte dei client.

Un altro punto utile di implementazione è la strategia di fetch. Poiché le affermazioni ora vivono fuori dal kind 0, i client possono decidere se richiederle solo nelle viste di dettaglio del profilo, solo per gli utenti seguiti, o per niente. Questo evita di appesantire ulteriormente il già caldo percorso del kind 0.

## Stato attuale

Secondo la spec attuale, le affermazioni di identità vivono in eventi kind 10011 dedicati invece che nei metadati kind 0. Questa separazione nasce dallo sforzo più ampio di alleggerire i fetch dei profili kind 0.

---

**Fonti primarie:**
- [NIP-39: External Identities in Profiles](https://github.com/nostr-protocol/nips/blob/master/39.md)
- [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) - Ha spostato le affermazioni di identità fuori dal kind 0

**Citato in:**
- [Newsletter #9: NIP Updates](/en/newsletters/2026-02-11-newsletter/#nip-updates)
- [Newsletter #12: Amethyst](/en/newsletters/2026-03-04-newsletter/#amethyst-nip-39-nip-c0-nip-66)

**Vedi anche:**
- [NIP-05: DNS-Based Verification](/it/topics/nip-05/)
