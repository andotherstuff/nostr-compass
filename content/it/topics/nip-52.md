---
title: "NIP-52: Eventi del calendario"
date: 2026-01-28
translationOf: /en/topics/nip-52.md
translationDate: 2026-04-22
draft: false
categories:
  - NIP
  - Calendar
  - Events
---
NIP-52 definisce eventi di calendario, calendari e RSVP su Nostr. Dà ai client un modo standard per pubblicare eventi basati su data o orario senza inventare un modello di evento personalizzato per ogni app.

## Kind di evento

### Kind 31922: evento di calendario basato sulla data

Usa la kind `31922` per eventi di un'intera giornata o di più giorni in cui l'orario preciso non conta.

```json
{
  "kind": 31922,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Nostr Meetup"],
    ["start", "2026-02-15"],
    ["end", "2026-02-16"],
    ["location", "Austin, TX"]
  ]
}
```

### Kind 31923: evento di calendario basato sull'orario

Usa la kind `31923` per eventi con orari di inizio e fine precisi.

```json
{
  "kind": 31923,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Weekly Call"],
    ["start", "1706900400"],
    ["end", "1706904000"],
    ["D", "19755"],
    ["start_tzid", "America/New_York"]
  ]
}
```

Gli eventi basati sull'orario richiedono anche uno o più tag `D`, ciascuno contenente il timestamp Unix a granularità giornaliera per i giorni coperti dall'evento. Quel tag esiste così relay e client possono indicizzare per giorno senza dover analizzare ogni timestamp completo.

## Supporto per calendario e RSVP

La kind `31924` è un calendario, cioè una lista indirizzabile di eventi di calendario. La kind `31925` è un RSVP che punta a uno specifico evento di calendario con un tag `a` e, facoltativamente, a una revisione specifica con un tag `e`.

Gli eventi di kind `31925` permettono agli utenti di rispondere con:

- `accepted` - Parteciperà
- `declined` - Non parteciperà
- `tentative` - Potrebbe partecipare

Gli RSVP possono anche includere valori `fb` pari a `free` o `busy`, aggiungendo contesto di pianificazione oltre allo stato di partecipazione.

## Note di implementazione

- **Indirizzabile**: eventi e calendari possono essere aggiornati senza creare duplicati
- **Supporto per i fusi orari**: gli eventi basati sull'orario possono usare identificatori di fuso orario IANA
- **Dati di posizione**: i tag possono includere posizioni leggibili, link e geohash
- **Richieste collaborative**: gli autori degli eventi possono richiedere l'inclusione nel calendario di qualcun altro taggandolo

Gli eventi ricorrenti restano intenzionalmente fuori ambito. La specifica delega le regole di ricorrenza ai client, il che mantiene semplice l'indicizzazione lato relay ed evita i soliti casi limite dei calendari legati ai cambi dell'ora legale e alle eccezioni.

## Perché è importante

NIP-52 fa più che descrivere un incontro. Separa la definizione dell'evento, l'appartenenza a un calendario e le risposte dei partecipanti in kind di eventi differenti. Questo rende possibile che un'app pubblichi un evento, un'altra aggreghi calendari e una terza gestisca lo stato degli RSVP senza che tutte e tre condividano lo stesso backend.

---

**Fonti principali:**
- [Specifica NIP-52](https://github.com/nostr-protocol/nips/blob/master/52.md)
- [PR #1752: Day-Granularity Timestamp Tag](https://github.com/nostr-protocol/nips/pull/1752)

**Citato in:**
- [Newsletter #7: Notedeck Calendar App Draft](/it/newsletters/2026-01-28-newsletter/)
- [Newsletter #10: NIP Updates](/it/newsletters/2026-02-18-newsletter/)
- [Newsletter #10: NIP Deep Dive](/it/newsletters/2026-02-18-newsletter/)

**Vedi anche:**
- [NIP-22: Comment](/it/topics/nip-22/)
- [NIP-51: Lists](/it/topics/nip-51/)
