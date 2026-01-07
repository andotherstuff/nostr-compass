---
title: "NIP-89: Handler di Applicazioni Raccomandati"
date: 2026-01-07
draft: false
categories:
  - Discovery
  - Clients
  - Protocol
---

NIP-89 definisce come le applicazioni possono annunciare le proprie capacità e come gli utenti possono raccomandare app che gestiscono tipi di evento specifici.

## Tipi di Evento

- **kind 31990** - Handler di applicazione (pubblicato dagli sviluppatori di app)
- **kind 31989** - Raccomandazione app (pubblicata dagli utenti)

## Come Funziona

1. **Le applicazioni** pubblicano eventi handler che descrivono quali tipi di evento supportano e come aprire i contenuti
2. **Gli utenti** raccomandano app che usano per tipi di evento specifici
3. **I client** cercano raccomandazioni per offrire funzionalità "apri con..." per tipi di evento sconosciuti

## Handler di Applicazione

```json
{
  "id": "<event-id>",
  "pubkey": "<app-developer-pubkey>",
  "created_at": 1736200000,
  "kind": 31990,
  "tags": [
    ["d", "<app-identifier>"],
    ["k", "30023"],
    ["web", "https://app.example.com/a/<bech32>", "naddr"],
    ["ios", "appname://open/<bech32>"]
  ],
  "content": "{\"name\": \"My App\", \"picture\": \"...\"}",
  "sig": "<signature>"
}
```

I tag `k` specificano i tipi di evento supportati. I template URL usano `<bech32>` come placeholder per entità codificate NIP-19.

## Raccomandazione Utente

```json
{
  "id": "<event-id>",
  "pubkey": "<user-pubkey>",
  "created_at": 1736200000,
  "kind": 31989,
  "tags": [
    ["d", "30023"],
    ["a", "31990:app-pubkey:identifier", "wss://relay", "web"]
  ],
  "content": "",
  "sig": "<signature>"
}
```

Il tag `d` è il tipo di evento raccomandato. Tag `a` multipli possono raccomandare diverse app per diverse piattaforme.

## Casi d'Uso

- Scoprire app che possono visualizzare articoli longform (kind 30023)
- Trovare client che supportano tipi di evento specifici
- Funzionalità "apri con..." cross-client
- Rilevare le capacità del client per il supporto della crittografia

---

**Fonti primarie:**
- [Specifica NIP-89](https://github.com/nostr-protocol/nips/blob/master/89.md)

**Menzionato in:**
- [Newsletter #4: Approfondimento NIP](/it/newsletters/2026-01-07-newsletter/#nip-44-crittografia-versionata)

**Vedi anche:**
- [NIP-19: Entità Codificate Bech32](/it/topics/nip-19/)
