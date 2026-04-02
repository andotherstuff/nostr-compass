---
title: "NIP-99: Annunci Classificati"
date: 2026-03-11
translationOf: /en/topics/nip-99.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Commerce
  - Marketplaces
---

NIP-99 definisce event di annunci classificati indirizzabili per beni, servizi, lavori, affitti e altre offerte. Fornisce alle app marketplace un modello di event più semplice rispetto alla vecchia specifica marketplace [NIP-15](/it/topics/nip-15/), ed è per questo che molti client di commercio attuali costruiscono su NIP-99.

## Come Funziona

Gli annunci attivi usano kind `30402`, mentre le bozze o gli annunci inattivi usano kind `30403`. La pubkey dell'autore è il venditore o il creatore dell'offerta. Il campo `content` contiene la descrizione leggibile in Markdown, e i tag contengono campi strutturati come titolo, sommario, prezzo, posizione e stato.

```json
{
  "id": "b3e392b11f5d4f28321cedd09303a748acfd0487aea5a7450b3481c60b6e4f87",
  "pubkey": "a695f6b60119d9521934a691347d9f78e8770b56da16bb255ee286ddf9fda919",
  "created_at": 1741699200,
  "kind": 30402,
  "tags": [
    ["d", "shopstr-handmade-wallet-001"],
    ["title", "Handmade leather wallet"],
    ["summary", "Brown bifold wallet with Bitcoin and Nostr branding"],
    ["published_at", "1741699200"],
    ["location", "Austin, TX"],
    ["price", "75000", "SAT"],
    ["status", "active"],
    ["t", "merch"],
    ["t", "bitcoin"]
  ],
  "content": "Full listing description in Markdown, shipping details, and contact terms.",
  "sig": "4a5c7e8f9012ab34cd56ef7890ab12cd34ef56ab78cd90ef12ab34cd56ef78900112233445566778899aabbccddeeff00112233445566778899aabbccddeeff"
}
```

L'event è indirizzabile, quindi un venditore può aggiornare l'annuncio mantenendo la stessa tupla identità di pubkey, kind e tag `d`. Questo rende le revisioni degli annunci più pulite per i client rispetto alla pubblicazione di una nota immutabile nuova di zecca per ogni modifica di prezzo o stato.

## Perché È Importante

La forza di NIP-99 è che lascia spazio a diversi design di marketplace pur standardizzando la struttura fondamentale dell'annuncio. Un client può concentrarsi su classificati locali, un altro sugli abbonamenti, e un altro su cataloghi prodotto globali. Se tutti concordano sulla struttura dell'event, i venditori possono pubblicare una volta e ottenere comunque visibilità cross-client.

Questa flessibilità spiega anche perché i progetti marketplace attuali lo favoriscono. La specifica è sufficientemente strutturata per supportare ricerca e visualizzazione, ma non costringe ogni app in un singolo flusso di escrow, spedizione o pagamento.

## Note sull'Implementazione

- I tag `price` possono descrivere pagamenti una tantum o ricorrenti aggiungendo un campo di frequenza opzionale.
- I tag `t` fungono da categorie o parole chiave per la ricerca.
- I tag `image` permettono ai client di renderizzare viste galleria senza analizzare il corpo Markdown.
- Un annuncio può collegarsi a event o documenti correlati con tag `e` o `a` quando un marketplace vuole un contesto prodotto più ricco.

## Implementazioni

- [Shopstr](https://github.com/shopstr-eng/shopstr) - Marketplace Nostr che usa annunci NIP-99 con endpoint MCP per agenti
- [Milk Market](https://github.com/shopstr-eng/milk-market) - Marketplace alimentare costruito sullo stesso livello di annunci con opzioni di pagamento miste

---

**Fonti primarie:**
- [Specifica NIP-99](https://github.com/nostr-protocol/nips/blob/master/99.md)
- [Shopstr PR #234](https://github.com/shopstr-eng/shopstr/pull/234) - Endpoint di commercio MCP su annunci NIP-99
- [Milk Market PR #10](https://github.com/shopstr-eng/milk-market/pull/10) - Abbonamento e checkout multi-venditore su annunci marketplace

**Menzionato in:**
- [Newsletter #13: Shopstr e Milk Market Aprono Superfici di Commercio MCP](/en/newsletters/2026-03-11-newsletter/#shopstr-and-milk-market-open-mcp-commerce-surfaces)

**Vedi anche:**
- [NIP-15: Offerte Marketplace](/it/topics/nip-15/)
- [NIP-47: Nostr Wallet Connect](/it/topics/nip-47/)
- [NIP-60: Cashu Wallet](/it/topics/nip-60/)
