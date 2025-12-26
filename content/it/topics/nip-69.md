---
title: "NIP-69: Trading Peer-to-Peer"
date: 2025-12-17
draft: false
categories:
  - Trading
  - Protocol
---

NIP-69 definisce un protocollo per il trading peer-to-peer su Nostr, creando un order book unificato tra piu' piattaforme invece di pool di liquidita' frammentati.

## Kind Evento

- **Kind 38383** - Eventi ordine P2P

## Struttura Ordine

Gli ordini usano tag per specificare i parametri di trading:

- `d` - ID Ordine
- `k` - Tipo ordine (buy/sell)
- `f` - Valuta fiat (codice ISO 4217)
- `amt` - Importo Bitcoin in satoshi
- `fa` - Importo fiat
- `pm` - Metodi di pagamento accettati
- `premium` - Percentuale premio/sconto sul prezzo
- `network` - Layer di settlement (onchain, lightning, liquid)
- `expiration` - Quando l'ordine scade

## Ciclo di Vita dell'Ordine

Gli ordini progrediscono attraverso stati:
- `pending` - Aperto e disponibile per il matching
- `in-progress` - Trade iniziato con controparte
- `success` - Trade completato
- `canceled` - Ritirato dal maker
- `expired` - Oltre il tempo di scadenza

## Sicurezza

Il tag `bond` specifica un deposito di sicurezza che entrambe le parti devono pagare, fornendo protezione contro abbandono o frode.

---

**Fonti primarie:**
- [Specifica NIP-69](https://github.com/nostr-protocol/nips/blob/master/69.md)

**Menzionato in:**
- [Newsletter #1: Aggiornamenti NIP](/it/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #1: Rilasci](/it/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #2: Notizie](/it/newsletters/2025-12-24-newsletter/#news)

