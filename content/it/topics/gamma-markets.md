---
title: "Gamma Markets"
date: 2026-07-15
translationOf: /en/topics/gamma-markets.md
translationDate: 2026-07-15
draft: false
categories:
  - Commerce
  - Marketplace
  - Protocol
---

Gamma Markets è un insieme di convenzioni e-commerce costruite direttamente su [NIP-99](/it/topics/nip-99/) classified listings, sviluppate in modo collaborativo da un gruppo di lavoro di sviluppatori di marketplace Nostr: i team dietro Shopstr, Cypher, Plebeian Market e Conduit Market. Colma le lacune relative a spedizione, flusso ordini, collezioni e recensioni che NIP-99 lascia indefinite.

## Come funziona

Gamma Markets aggiunge cinque event kind attorno all'event kind `30402` listing già esistente in NIP-99, senza modificarne la struttura:

- **Kind 30405** - collezioni di prodotti, che raggruppano più listing tramite tag `a`
- **Kind 30406** - opzioni di spedizione, con prezzi per paese e regole di costo opzionali basate su peso o distanza
- **Kind 16** - messaggi d'ordine: creazione (type 1), richieste di pagamento (type 2), aggiornamenti di stato (type 3) e aggiornamenti di spedizione (type 4)
- **Kind 14** - comunicazione generica acquirente/venditore
- **Kind 17** - ricevute di pagamento
- **Kind 31555** - recensioni di prodotto, indirizzate a una specifica pubkey del venditore e al tag `d` del listing

Le preferenze di pagamento del venditore sono dichiarate tramite un tag `payment_preference` nei metadati del profilo kind `0`, e i client scoprono le app compatibili attraverso le raccomandazioni applicative [NIP-89](/it/topics/nip-89/). La comunicazione degli ordini si basa sui messaggi privati [NIP-17](/it/topics/nip-17/), senza introdurre uno schema di cifratura proprio.

La scelta progettuale distintiva della specifica è che nulla viene ereditato automaticamente: un listing che appartiene a una collezione, o che utilizza un'opzione di spedizione, la referenzia esplicitamente con un tag `a` invece di ereditare le impostazioni del contenitore. Si tratta di un distacco deliberato dal vecchio modello stall di [NIP-15](/it/topics/nip-15/), in cui un prodotto ereditava silenziosamente la valuta e la tabella spedizioni del proprio stall genitore.

### Esempio: creazione ordine (kind 16, type 1)

```json
{
  "kind": 16,
  "content": "Please leave the package with the doorman.",
  "tags": [
    ["p", "<merchant-pubkey>"],
    ["subject", "New order"],
    ["type", "1"],
    ["order", "order-8f21"],
    ["amount", "115000"],
    ["item", "30402:<merchant-pubkey>:keyboard-mx-blue-01", "1"],
    ["shipping", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

## Perché è importante

NIP-99 da solo standardizza unicamente il listing stesso, un annuncio classificato firmato e indirizzabile. Prima di Gamma Markets, ogni client che costruiva e-commerce reale su NIP-99 inventava le proprie convenzioni private per spedizione, checkout e recensioni, il che significava che due client conformi a NIP-99 potevano ciascuno visualizzare correttamente un listing ma non avevano un modo condiviso per completare un ordine tra di loro. Gamma Markets colma questa lacuna senza modificare il formato listing di NIP-99, perciò i listing NIP-99 esistenti restano validi senza alcuna modifica.

## Implementazioni

- [Shopstr](https://github.com/shopstr-eng/shopstr) - marketplace Nostr, uno dei quattro progetti che hanno creato la specifica
- [Conduit Mono](https://github.com/Conduit-BTC/conduit-mono) - protocollo marketplace che costruisce il proprio flusso di stato ordini e checkout nello stesso spazio progettuale

---

**Fonti primarie:**
- [Repository della specifica Gamma Markets](https://github.com/GammaMarkets/market-spec)
- [Estensione del caso d'uso e-commerce per NIP-99, PR #1784](https://github.com/nostr-protocol/nips/pull/1784) - link dal documento canonico NIP-99 alla specifica Gamma Markets

**Menzionato in:**
- [Newsletter #31: NIP Deep Dive: NIP-99 e l'estensione commerce Gamma Markets](/it/newsletters/2026-07-15-newsletter/#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension)

**Vedi anche:**
- [NIP-99: Classified Listings](/it/topics/nip-99/)
- [NIP-15: Nostr Marketplace](/it/topics/nip-15/)
- [NIP-17: Private Direct Messages](/it/topics/nip-17/)
