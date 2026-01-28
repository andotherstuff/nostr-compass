---
title: "NIP-52: Eventi del Calendario"
date: 2026-01-28
translationOf: /en/topics/nip-52.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Calendar
  - Events
---

NIP-52 definisce i tipi di evento per la funzionalità calendario su Nostr, abilitando programmazione, RSVP e coordinamento eventi.

## Tipi di Evento

### Kind 31922: Evento del Calendario Basato su Data
Per eventi che si estendono su uno o più giorni senza orari specifici:

```json
{
  "kind": 31922,
  "tags": [
    ["d", "identificatore-unico"],
    ["title", "Meetup Nostr"],
    ["start", "2026-02-15"],
    ["end", "2026-02-15"],
    ["location", "Austin, TX"]
  ]
}
```

### Kind 31923: Evento del Calendario Basato su Orario
Per eventi con orari di inizio e fine specifici:

```json
{
  "kind": 31923,
  "tags": [
    ["d", "identificatore-unico"],
    ["title", "Chiamata Settimanale"],
    ["start", "1706900400"],
    ["end", "1706904000"],
    ["start_tzid", "America/New_York"]
  ]
}
```

## Supporto RSVP

Gli eventi kind 31925 permettono agli utenti di rispondere agli eventi del calendario:

- `accepted` - Parteciperà
- `declined` - Non parteciperà
- `tentative` - Potrebbe partecipare

## Caratteristiche

- **Addressable**: Gli eventi possono essere aggiornati senza creare duplicati
- **Supporto Fuso Orario**: Gestione corretta dei fusi orari tramite identificatori IANA
- **Posizione**: Luoghi di incontro fisici o virtuali
- **Ricorrenza**: Supporto per eventi ricorrenti (estensione proposta)

## Correlati

- [NIP-22](/it/topics/nip-22/) - Commenti (per discussioni sugli eventi del calendario)
- [NIP-51](/it/topics/nip-51/) - Liste (per collezioni di calendari)
