---
title: "NIP-22: Commenti"
date: 2026-01-28
translationOf: /en/topics/nip-22.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Social
---

NIP-22 definisce uno standard per commentare qualsiasi contenuto Nostr addressable, abilitando discussioni threaded su articoli, video, eventi del calendario e altri eventi addressable.

## Come Funziona

I commenti usano eventi kind 1111 con tag che referenziano il contenuto commentato:

```json
{
  "kind": 1111,
  "tags": [
    ["A", "30023:pubkey:article-id", "wss://relay.example"],
    ["E", "root-event-id", "wss://relay.example"],
    ["K", "30023"]
  ],
  "content": "Ottimo articolo!"
}
```

## Struttura dei Tag

- **Tag `A`**: Referenzia l'evento addressable commentato (formato kind:pubkey:d-tag)
- **Tag `E`**: Referenzia l'ID dell'evento root per il threading
- **Tag `K`**: Indica il kind dell'evento root
- **Tag `e`**: Referenzia il commento genitore per risposte annidate

## Differenza dal Kind 1

Mentre le note kind 1 possono rispondere ad altre note, i commenti NIP-22 sono specificamente progettati per:

- Contenuti addressable (articoli, video, eventi del calendario)
- Mantenere chiare relazioni genitore-figlio
- Abilitare moderazione e threading su contenuti long-form

## Casi d'Uso

- Discussioni su articoli
- Commenti sui video
- Discussioni sugli eventi del calendario [NIP-52](/it/topics/nip-52/)
- Pagine di discussione delle wiki
- Qualsiasi tipo di evento addressable

## Correlati

- [NIP-01](/it/topics/nip-01/) - Protocollo Base (note kind 1)
- [NIP-52](/it/topics/nip-52/) - Eventi del Calendario
