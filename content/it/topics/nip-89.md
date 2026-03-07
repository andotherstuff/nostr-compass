---
title: "NIP-89: Recommended Application Handlers"
date: 2026-01-07
translationOf: /en/topics/nip-89/
translationDate: 2026-03-07
draft: false
categories:
  - Discovery
  - Clients
  - Protocol
---
NIP-89 definisce come le applicazioni possono annunciare le proprie capacità e come gli utenti possono raccomandare app che gestiscono specifici kind di evento.

## Tipi di evento

- **kind 31990** - Application handler (pubblicato dagli sviluppatori dell'app)
- **kind 31989** - Raccomandazione di app (pubblicata dagli utenti)

## Come funziona

1. **Le applicazioni** pubblicano eventi handler che descrivono quali kind di evento supportano e come aprire il contenuto
2. **Gli utenti** raccomandano le app che usano per specifici kind di evento
3. **I client** interrogano le raccomandazioni per offrire funzionalità "open in..." per tipi di evento sconosciuti

## Application Handler

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

I tag `k` specificano i kind di evento supportati. I template URL usano `<bech32>` come placeholder per entità codificate con NIP-19.

Lo stesso evento handler può pubblicizzare diversi kind supportati se condividono lo stesso schema di routing. Questo mantiene compatta la discoverability delle app ed evita di pubblicare un evento handler per ogni kind quando la logica di destinazione è identica.

## Raccomandazione dell'utente

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

Il tag `d` è il kind di evento raccomandato. Più tag `a` possono raccomandare app diverse per piattaforme diverse.

## Tag Client

NIP-89 definisce anche un tag `client` opzionale che le app di pubblicazione possono allegare agli eventi ordinari. Registra il nome del client più un puntatore all'evento handler, il che consente ad altri client di mostrare da dove proviene una nota o di recuperare metadata applicativi più ricchi.

Questo ha implicazioni per la privacy. La specifica dice esplicitamente che i client dovrebbero consentire agli utenti di disattivarlo, perché pubblicare l'identità del software su ogni evento può rivelare pattern d'uso che le persone potrebbero non voler esporre.

## Casi d'uso

- Scoprire app che possono mostrare articoli longform (kind 30023)
- Trovare client che supportano specifici tipi di evento
- Funzionalità cross-client "open in..."
- Rilevare capacità del client per il supporto alla cifratura

## Note su trust e sicurezza

NIP-89 migliora l'interoperabilità, ma crea anche una superficie di redirect. Se un client interroga annunci handler arbitrari da relay non fidati, può finire per inviare gli utenti verso applicazioni malevole o fuorvianti.

Per questo il flusso di raccomandazione parte dalle persone che segui. Le raccomandazioni filtrate socialmente non sono perfette, ma sono più sicure che trattare ogni handler pubblicato come ugualmente affidabile.

---

**Fonti principali:**
- [NIP-89 Specification](https://github.com/nostr-protocol/nips/blob/master/89.md)

**Menzionato in:**
- [Newsletter #4: NIP Deep Dive](/en/newsletters/2026-01-07-newsletter/#nip-44-versioned-encryption)
- [Newsletter #12: Damus](/en/newsletters/2026-03-04-newsletter/#damus-nip-89-recommended-application-handlers)

**Vedi anche:**
- [NIP-19: Bech32-Encoded Entities](/it/topics/nip-19/)
