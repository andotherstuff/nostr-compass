---
title: "NIP-87: Ecash Mint Discoverability"
date: 2026-01-07
translationOf: /en/topics/nip-87/
translationDate: 2026-03-07
draft: false
categories:
  - Ecash
  - Discovery
  - Protocol
---
NIP-87 definisce come gli ecash mint (Cashu e Fedimint) possono annunciarsi su Nostr e come gli utenti possono raccomandare mint ad altri utenti.

## Tipi di evento

- **kind 38172** - Annuncio di mint Cashu (pubblicato dagli operatori del mint)
- **kind 38173** - Annuncio Fedimint (pubblicato dagli operatori del mint)
- **kind 38000** - Raccomandazione di mint (pubblicata dagli utenti)

## Come funziona

1. **Gli operatori del mint** pubblicano l'URL del loro mint, le feature supportate e la rete (mainnet/testnet)
2. **Gli utenti** che si fidano di un mint pubblicano raccomandazioni con recensioni opzionali
3. **Altri utenti** interrogano le raccomandazioni di persone che seguono per scoprire mint affidabili

## Annuncio di mint Cashu

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

Il tag `nuts` elenca i NUT supportati (Notation, Usage, and Terminology specs per Cashu).

Il tag `d` dovrebbe essere la pubkey Cashu del mint, che dà ai client un identificatore stabile per la discoverability anche se il mint in seguito cambia metadata o ripubblica il proprio annuncio.

## Raccomandazioni degli utenti

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
  "content": "I've used this mint for months, very reliable",
  "sig": "<signature>"
}
```

Gli utenti possono includere recensioni nel campo `content` e puntare a specifici eventi di annuncio del mint.

Gli eventi di raccomandazione sono parameterized replaceable events. Questo è utile perché un utente può rivedere una raccomandazione, aggiornare il testo della recensione o smettere di sostenere un mint senza lasciare dietro di sé diversi eventi di raccomandazione obsoleti.

## Modello di trust

NIP-87 non dice ai client quale mint sia sicuro. Fornisce loro un modo per combinare metadata pubblicati dagli operatori con raccomandazioni sociali provenienti da account di cui l'utente si fida già.

Questa distinzione conta perché le query dirette degli eventi di annuncio del mint possono essere rumorose o malevole. La specifica avverte esplicitamente i client di usare misure anti-spam o relay di alta qualità quando aggirano le raccomandazioni sociali e interrogano direttamente gli annunci.

## Note di interoperabilità

Cashu e Fedimint usano kind di annuncio diversi perché espongono dettagli di connessione diversi. Gli annunci Cashu pubblicano URL del mint e NUT supportati, mentre gli annunci Fedimint pubblicano codici di invito e moduli federation supportati. Un wallet che supporta entrambi deve fare il parse di entrambi i formati.

---

**Fonti principali:**
- [NIP-87 Specification](https://github.com/nostr-protocol/nips/blob/master/87.md)

**Menzionato in:**
- [Newsletter #4: Releases](/en/newsletters/2026-01-07-newsletter/#releases)
- [Newsletter #7: Zeus](/en/newsletters/2026-01-28-newsletter/)

**Vedi anche:**
- [Cashu](/it/topics/cashu/)
- [NIP-60: Cashu Wallet](/it/topics/nip-60/)
