---
title: "NIP-15: Nostr Marketplace"
date: 2026-01-28
translationOf: /en/topics/nip-15.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Commerce
  - Marketplace
---
NIP-15 definisce un protocollo per marketplace decentralizzati su Nostr, che permette ai merchant di elencare prodotti e ai buyer di effettuare acquisti usando Bitcoin e Lightning.

## Come funziona

### Merchant Stalls (Kind 30017)

I merchant creano stall come eventi addressable:

```json
{
  "kind": 30017,
  "tags": [
    ["d", "my-stall"],
    ["name", "Bob's Electronics"],
    ["description", "Quality used electronics"],
    ["currency", "sat"],
    ["shipping", "{...shipping options...}"]
  ]
}
```

### Products (Kind 30018)

I prodotti vengono elencati all'interno degli stall:

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

## Flusso di acquisto

1. Il buyer esplora i prodotti in più stall
2. Il buyer invia al merchant un messaggio d'ordine cifrato
3. Il merchant risponde con una invoice Lightning
4. Il buyer paga la invoice
5. Il merchant spedisce il prodotto

## Perché è importante

- **Decentralizzato**: nessun operatore centrale del marketplace
- **Interoperabile**: qualsiasi client NIP-15 può esplorare qualsiasi merchant
- **Privato**: gli ordini sono cifrati tra buyer e seller
- **Bitcoin-native**: pagamenti Lightning integrati

Il vantaggio pratico è la portabilità. Un merchant può pubblicare una sola volta i dati del catalogo e lasciare che più client li renderizzino, invece di restare vincolato a un solo front end di marketplace.

## Compromessi

NIP-15 standardizza gli annunci, non la fiducia. I buyer devono comunque decidere se un merchant è legittimo, se l'inventario è reale e come vengono gestite le controversie. Il protocollo fornisce strutture dati comuni e un flusso di messaggi comune, ma reputazione ed evasione degli ordini restano problemi a livello applicativo.

Anche pagamenti e spedizioni sono standardizzati solo in parte. Un client può comprendere stall e prodotti e avere comunque bisogno di logica personalizzata per invoice, stato dell'ordine o tracciamento della consegna.

## Stato dell'implementazione

- **Plebeian Market** - Marketplace NIP-15 completo
- **Shopstr** - Commercio Bitcoin permissionless
- **Amethyst** - Elenchi di prodotti integrati nel feed social

---

**Fonti principali:**
- [Specifica NIP-15](https://github.com/nostr-protocol/nips/blob/master/15.md)

**Menzionato in:**
- [Newsletter #7: January 2024 Protocol Hardening](/en/newsletters/2026-01-28-newsletter/#january-2024-protocol-hardening)

**Vedi anche:**
- [NIP-44: Encrypted Payloads](/it/topics/nip-44/)
- [NIP-57: Lightning Zaps](/it/topics/nip-57/)
