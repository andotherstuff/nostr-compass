---
title: "NIP-99: Annunci classificati"
date: 2026-03-11
translationOf: /en/topics/nip-99.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Commerce
  - Marketplaces
---

NIP-99 definisce eventi di annunci classificati indirizzabili per beni, servizi, lavori, affitti e altre offerte. Offre alle app marketplace un modello di evento più semplice rispetto alla vecchia spec di marketplace [NIP-15](/it/topics/nip-15/), ed è per questo che molti client commerce attuali si basano invece su NIP-99.

## Come funziona

Gli annunci attivi usano il kind `30402`, mentre le bozze o gli annunci inattivi usano il kind `30403`. La pubkey dell'autore è il venditore o creatore dell'offerta. Il campo `content` contiene la descrizione leggibile per gli esseri umani in Markdown, mentre i tag mantengono i campi strutturati come titolo, riassunto, prezzo, località e stato.

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

L'evento è indirizzabile, quindi un venditore può aggiornare l'annuncio mantenendo la stessa tupla di identità formata da pubkey, kind e tag `d`. Questo rende le revisioni degli annunci più pulite per i client rispetto alla pubblicazione di una nuova nota immutabile per ogni variazione di prezzo o di stato.

## Perche conta

La forza di NIP-99 è che lascia spazio a design di marketplace differenti pur standardizzando la forma di base dell'annuncio. Un client può concentrarsi sugli annunci locali, un altro sugli abbonamenti e un altro ancora su cataloghi di prodotti globali. Se tutti concordano sulla struttura dell'evento, i venditori possono pubblicare una volta e ottenere comunque una certa visibilita cross-client.

Questa flessibilita spiega anche perché i progetti marketplace attuali lo favoriscono. La spec e abbastanza strutturata da supportare ricerca e visualizzazione, ma non forza ogni app dentro un singolo workflow di escrow, spedizione o pagamento.

## Note di implementazione

- I tag `price` possono descrivere pagamenti una tantum o ricorrenti aggiungendo un campo opzionale di frequenza.
- I tag `t` funzionano come categorie o parole chiave di ricerca.
- I tag `image` consentono ai client di renderizzare viste galleria senza analizzare il corpo Markdown.
- Un annuncio può collegarsi a eventi o documenti correlati con tag `e` o `a` quando un marketplace vuole un contesto di prodotto più ricco.

## Implementazioni

- [Shopstr](https://github.com/shopstr-eng/shopstr) - Marketplace Nostr che usa annunci NIP-99 con endpoint MCP rivolti agli agenti
- [Milk Market](https://github.com/shopstr-eng/milk-market) - Marketplace alimentare costruito sullo stesso livello di annunci con opzioni di pagamento miste

---

**Fonti primarie:**
- [NIP-99 Specification](https://github.com/nostr-protocol/nips/blob/master/99.md)
- [Shopstr PR #234](https://github.com/shopstr-eng/shopstr/pull/234) - Endpoint commerce MCP sopra gli annunci NIP-99
- [Milk Market PR #10](https://github.com/shopstr-eng/milk-market/pull/10) - Abbonamenti e checkout multi-merchant sopra gli annunci marketplace

**Citato in:**
- [Newsletter #13: Shopstr e Milk Market aprono superfici commerce MCP](/it/newsletters/2026-03-11-newsletter/#shopstr-e-milk-market-aprono-superfici-commerce-mcp)

**Vedi anche:**
- [NIP-15: Offerte marketplace](/it/topics/nip-15/)
- [NIP-47: Nostr Wallet Connect](/it/topics/nip-47/)
- [NIP-60: Wallet Cashu](/it/topics/nip-60/)
