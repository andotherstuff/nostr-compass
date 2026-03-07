---
title: "NIP-50: Ricerca"
date: 2025-12-31
translationOf: /en/topics/nip-50.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Relay
---
NIP-50 definisce una capacità generale di ricerca per i relay Nostr. Aggiunge query in stile full-text sopra i filtri a corrispondenza esatta di NIP-01.

## Come funziona

Il protocollo aggiunge un campo `search` agli oggetti filtro nei messaggi `REQ`:

1. I client inviano una stringa di query leggibile da esseri umani come `best nostr apps`.
2. I relay interpretano quella query rispetto ai dati degli eventi, principalmente il campo `content`.
3. I risultati vengono ordinati per qualità della corrispondenza, non per `created_at`.
4. `limit` si applica dopo l'ordinamento per rilevanza.

I filtri di ricerca possono essere combinati con `kinds`, `ids`, autori e altri normali campi filtro per query più specifiche.

## Estensioni di ricerca

I relay possono supportare facoltativamente questi parametri di estensione:

- `include:spam` - Disabilita il filtro antispam predefinito
- `domain:<domain>` - Filtra per dominio NIP-05 verificato
- `language:<code>` - Filtra per codice lingua ISO
- `sentiment:<value>` - Filtra per sentiment negativo, neutro o positivo
- `nsfw:<true/false>` - Include o esclude contenuti NSFW

I relay dovrebbero ignorare le estensioni che non supportano, quindi i client devono trattarle come indizi, non come garanzie.

## Note di interoperabilità

- I client dovrebbero controllare le capacità del relay tramite il campo `supported_nips`
- È consigliata la verifica lato client dei risultati
- Non tutti i relay implementano la ricerca, resta una funzionalità opzionale

Poiché il ranking è definito dall'implementazione, la stessa query può restituire insiemi di risultati diversi su relay diversi. I client che tengono al recall dovrebbero interrogare più di un relay di ricerca e unire i risultati.

## Perché è importante

I filtri strutturati funzionano bene quando conosci già l'autore, il kind o il tag che vuoi. La ricerca serve per il caso opposto: la scoperta. Questo rende NIP-50 utile per directory di app, archivi lunghi e ricerca tra note pubbliche, ma significa anche che la qualità della ricerca dipende molto dalle scelte di indicizzazione e filtro antispam di ciascun relay.

---

**Fonti primarie:**
- [NIP-50 Specification](https://github.com/nostr-protocol/nips/blob/master/50.md)

**Citato in:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #7: NIP Updates](/en/newsletters/2026-01-07-newsletter/#nip-updates)

**Vedi anche:**
- [NIP-11: Relay Information](/it/topics/nip-11/)
