---
title: "NIP-39: Identità Esterne nei Profili"
date: 2026-02-11
translationOf: /en/topics/nip-39.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Identity
---

NIP-39 definisce come collegare claim di identità esterna ai profili Nostr usando tag `i`. Questi tag collegano una pubkey Nostr ad account su piattaforme esterne come GitHub, Twitter o domini DNS.

## Come Funziona

Chi pubblica claim di identità li inserisce come tag `i`. Ogni tag contiene un identificatore di piattaforma e un URL di prova dove l'account esterno rimanda alla pubkey Nostr, stabilendo una verifica bidirezionale:

```json
{
  "tags": [
    ["i", "github:username", "https://gist.github.com/username/proof"],
    ["i", "twitter:handle", "https://twitter.com/handle/status/proof_tweet_id"]
  ]
}
```

I client verificano i claim recuperando l'URL di prova e controllando che contenga la pubkey Nostr dell'utente. Questo crea una rete di connessioni identitarie che non richiede servizi di verifica centralizzati.

## Modifiche Recenti

A febbraio 2026, la [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) ha estratto i tag identità dagli eventi kind 0 (metadata utente) in un nuovo kind dedicato 10011. Lo spostamento fa parte della campagna di snellimento kind 0 di vitorpamplona, motivato dalla bassa adozione: quasi nessun client implementava la verifica dei tag `i`, eppure ogni fetch kind 0 ne portava il peso. Il nuovo kind 10011 permette ai client interessati di recuperare i claim di identità separatamente.

---

**Fonti primarie**
- [NIP-39: External Identities in Profiles](https://github.com/nostr-protocol/nips/blob/master/39.md)

**Menzionato in**
- [Newsletter #9, Aggiornamenti NIP](/it/newsletters/2026-02-11-newsletter/#aggiornamenti-nip)

**Vedi anche**
- [NIP-05, Verifica Basata su DNS](/it/topics/nip-05/)
