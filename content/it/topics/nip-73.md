---
title: "NIP-73 (Geotag)"
date: 2026-02-04
description: "NIP-73 definisce il tagging della posizione per gli eventi Nostr usando coordinate geografiche e identificatori."
---

NIP-73 specifica come allegare dati di posizione geografica agli eventi Nostr. Questo abilita la scoperta e il filtraggio dei contenuti basati sulla posizione.

## Come Funziona

I dati di posizione vengono aggiunti agli eventi tramite tag `g` (geohash). La codifica geohash rappresenta latitudine e longitudine come una singola stringa, con precisione determinata dalla lunghezza della stringa. Stringhe più lunghe indicano posizioni più precise.

Gli eventi possono includere più tag geohash a diversi livelli di precisione, permettendo ai client di interrogare a varie granularità. Un post taggato con un geohash di 6 caratteri copre approssimativamente un isolato, mentre un geohash di 4 caratteri copre una piccola città.

## Formato Tag

```json
{
  "tags": [
    ["g", "u4pruydqqvj", "geohash"],
    ["g", "u4pruyd", "geohash"],
    ["g", "u4pru", "geohash"]
  ]
}
```

## Codici Paese

Aggiornamenti recenti a NIP-73 ([PR #2205](https://github.com/nostr-protocol/nips/pull/2205)) hanno aggiunto supporto per i codici paese ISO 3166, permettendo agli eventi di essere taggati con posizione a livello di paese senza richiedere coordinate precise:

```json
{
  "tags": [
    ["g", "US", "countryCode"]
  ]
}
```

## Implementazioni

- I client location-aware usano NIP-73 per check-in e scoperta locale
- I filtri relay possono restringere o prioritizzare i contenuti per geografia
- Le applicazioni di mapping visualizzano le note geotaggate

## Fonti Primarie

- [Specifica NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - Aggiunge codici paese ISO 3166

## Menzionato In

- [Newsletter #8 (2026-02-04)](/it/newsletters/2026-02-04-newsletter/) - Supporto codici paese unito
