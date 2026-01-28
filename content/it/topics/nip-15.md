---
title: "NIP-15: Nostr Marketplace"
date: 2026-01-28
translationOf: /en/topics/nip-15.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Commerce
  - Marketplace
---

NIP-15 definisce un protocollo per marketplace decentralizzati su Nostr, consentendo ai merchant di elencare prodotti e agli acquirenti di effettuare acquisti usando Bitcoin e Lightning.

## Come Funziona

### Stall dei Merchant (Kind 30017)

I merchant creano stall come eventi addressable:

```json
{
  "kind": 30017,
  "tags": [
    ["d", "my-stall"],
    ["name", "Elettronica di Bob"],
    ["description", "Elettronica usata di qualità"],
    ["currency", "sat"],
    ["shipping", "{...opzioni di spedizione...}"]
  ]
}
```

### Prodotti (Kind 30018)

I prodotti sono elencati all'interno degli stall:

```json
{
  "kind": 30018,
  "tags": [
    ["d", "product-123"],
    ["stall_id", "my-stall"],
    ["name", "Raspberry Pi 4"],
    ["price", "50000"],
    ["quantity", "5"],
    ["images", "https://..."]
  ]
}
```

## Flusso di Acquisto

1. L'acquirente esplora i prodotti attraverso più stall
2. L'acquirente invia un messaggio d'ordine crittografato al merchant
3. Il merchant risponde con una fattura Lightning
4. L'acquirente paga la fattura
5. Il merchant spedisce il prodotto

## Caratteristiche Chiave

- **Decentralizzato**: Nessun operatore centrale del marketplace
- **Interoperabile**: Qualsiasi client NIP-15 può esplorare qualsiasi merchant
- **Privato**: Gli ordini sono crittografati tra acquirente e venditore
- **Bitcoin-native**: Pagamenti Lightning integrati

## Implementazioni

- **Plebeian Market** - Marketplace NIP-15 completo
- **Shopstr** - Commercio Bitcoin permissionless
- **Amethyst** - Elenchi prodotti integrati nel feed social

## Correlati

- [NIP-44](/it/topics/nip-44/) - Messaggi crittografati per gli ordini
- [NIP-57](/it/topics/nip-57/) - Lightning Zap
