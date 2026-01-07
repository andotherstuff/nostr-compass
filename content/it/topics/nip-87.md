---
title: "NIP-87: Scoperta dei Mint Ecash"
date: 2026-01-07
draft: false
categories:
  - Ecash
  - Discovery
  - Protocol
---

NIP-87 definisce come i mint ecash (Cashu e Fedimint) possono annunciarsi su Nostr, e come gli utenti possono raccomandare mint ad altri.

## Tipi di Evento

- **kind 38172** - Annuncio mint Cashu (pubblicato dagli operatori del mint)
- **kind 38173** - Annuncio Fedimint (pubblicato dagli operatori del mint)
- **kind 38000** - Raccomandazione mint (pubblicata dagli utenti)

## Come Funziona

1. **Gli operatori del mint** pubblicano l'URL del loro mint, le funzionalità supportate e la rete (mainnet/testnet)
2. **Gli utenti** che si fidano di un mint pubblicano raccomandazioni con recensioni opzionali
3. **Altri utenti** cercano raccomandazioni dalle persone che seguono per scoprire mint fidati

## Annuncio Mint Cashu

```json
{
  "id": "<event-id>",
  "pubkey": "<mint-operator-pubkey>",
  "created_at": 1736200000,
  "kind": 38172,
  "tags": [
    ["d", "<mint-pubkey>"],
    ["u", "https://mint.example.com"],
    ["nuts", "1,2,3,4,5,6,7"],
    ["n", "mainnet"]
  ],
  "content": "",
  "sig": "<signature>"
}
```

Il tag `nuts` elenca i NUT supportati (Notation, Usage, and Terminology - specifiche per Cashu).

## Raccomandazioni degli Utenti

```json
{
  "id": "<event-id>",
  "pubkey": "<recommender-pubkey>",
  "created_at": 1736200000,
  "kind": 38000,
  "tags": [
    ["k", "38172"],
    ["d", "<mint-identifier>"],
    ["a", "38172:mint-pubkey:<d-tag>", "wss://relay"]
  ],
  "content": "Ho usato questo mint per mesi, molto affidabile",
  "sig": "<signature>"
}
```

Gli utenti possono includere recensioni nel campo `content` e puntare a eventi di annuncio mint specifici.

---

**Fonti primarie:**
- [Specifica NIP-87](https://github.com/nostr-protocol/nips/blob/master/87.md)

**Menzionato in:**
- [Newsletter #4: Rilasci](/it/newsletters/2026-01-07-newsletter/#rilasci)

**Vedi anche:**
- [NIP-60: Wallet Cashu](/it/topics/nip-60/)
