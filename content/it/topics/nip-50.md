---
title: "NIP-50: Search"
date: 2025-12-31
translationOf: /en/topics/nip-50.md
translationDate: 2025-12-31
draft: false
categories:
  - Protocollo
  - Relay
---

NIP-50 definisce una capacità di ricerca generalizzata per i relay Nostr, consentendo ai client di eseguire ricerche full-text oltre alle query strutturate per tag o ID.

## Come Funziona

Il protocollo aggiunge un campo `search` agli oggetti filtro nei messaggi REQ:

1. I client inviano query di ricerca leggibili dall'uomo (es. "migliori app nostr")
2. I relay interpretano e fanno corrispondere le query ai dati degli eventi, principalmente il campo `content`
3. I risultati sono ordinati per rilevanza anziché in ordine cronologico
4. Il filtro `limit` viene applicato dopo l'ordinamento per rilevanza

I filtri di ricerca possono essere combinati con altri vincoli come `kinds` e `ids` per query più specifiche.

## Estensioni di Ricerca

I relay possono opzionalmente supportare questi parametri di estensione:

- `include:spam` - Disabilita il filtraggio spam predefinito
- `domain:<domain>` - Filtra per dominio NIP-05 verificato
- `language:<code>` - Filtra per codice lingua ISO
- `sentiment:<value>` - Filtra per sentimento negativo/neutro/positivo
- `nsfw:<true/false>` - Include o esclude contenuti NSFW

## Considerazioni per i Client

- I client dovrebbero verificare le capacità del relay tramite il campo `supported_nips`
- La verifica dei risultati lato client è raccomandata
- Non tutti i relay implementano la ricerca; rimane una funzionalità opzionale

---

**Fonti primarie:**
- [Specifica NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md)

**Menzionato in:**
- [Newsletter #3: Riepilogo di Dicembre](/it/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Vedi anche:**
- [NIP-11: Informazioni Relay](/it/topics/nip-11/)
