---
title: "NIP-72: Comunità Moderate"
date: 2026-03-25
translationOf: /en/topics/nip-72.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Communities
---

NIP-72 definisce le comunità moderate su Nostr. Le comunità forniscono un modo per organizzare i post attorno a un argomento o gruppo condiviso, con moderatori che approvano i contenuti prima che diventino visibili ai membri.

## Come Funziona

Una comunità è definita da un event di kind 34550 pubblicato dal suo creatore. Questo event contiene il nome della comunità, la descrizione, le regole e una lista di pubkey dei moderatori. L'event usa un formato di event sostituibile (intervallo kind 30000-39999), quindi la definizione della comunità può essere aggiornata nel tempo.

```json
{
  "kind": 34550,
  "tags": [
    ["d", "example-community"],
    ["name", "Example Community"],
    ["description", "A community for discussing examples"],
    ["p", "<moderator_pubkey>", "", "moderator"],
    ["relay", "wss://relay.example.com", "moderator"]
  ],
  "content": "",
  "pubkey": "<creator_pubkey>",
  "created_at": 1742860800,
  "sig": "<signature>"
}
```

Gli utenti inviano post a una comunità taggando i propri event con un tag `a` che punta alla definizione della comunità. Questi post non sono ancora visibili ai lettori della comunità. Un moderatore esamina la sottomissione e, se approvata, pubblica un event di approvazione di kind 4549 che avvolge il post originale. I client che visualizzano la comunità mostrano solo i post che hanno un event di approvazione corrispondente da un moderatore riconosciuto.

Questo modello di approvazione significa che le comunità sono filtrate in lettura, non limitate in scrittura. Chiunque può inviare un post, ma solo i post approvati appaiono nel feed della comunità. I moderatori agiscono come curatori piuttosto che come guardiani dei dati sottostanti.

## Considerazioni

Poiché gli event di approvazione sono event Nostr separati, le decisioni di moderazione sono trasparenti e verificabili. Un post rifiutato da una comunità può comunque essere approvato da un'altra. Lo stesso contenuto può esistere in più comunità con moderazione indipendente.

Il supporto dei relay è importante per la funzionalità delle comunità. I client devono interrogare sia la definizione della comunità che gli event di approvazione, il che richiede relay che indicizzino questi kind di event in modo efficiente.

---

**Fonti primarie:**
- [Specifica NIP-72](https://github.com/nostr-protocol/nips/blob/master/72.md) - Comunità Moderate

**Menzionato in:**
- [Newsletter #15](/it/newsletters/2026-03-25-newsletter/)
