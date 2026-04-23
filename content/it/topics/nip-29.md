---
title: "NIP-29: Gruppi basati su relay"
date: 2025-12-24
translationOf: /en/topics/nip-29.md
translationDate: 2026-04-22
draft: false
categories:
  - Social
  - Groups
---
NIP-29 definisce gruppi basati su relay, in cui un relay gestisce appartenenza al gruppo, permessi e visibilità dei messaggi.

## Come funziona

I gruppi sono identificati da un host relay più un group id, e il relay è l'autorità per membership e moderazione. Gli eventi creati dagli utenti e inviati in un gruppo portano un tag `h` con il group id. I metadata generati dal relay usano eventi indirizzabili firmati con la chiave del relay stesso.

L'evento metadata principale è kind 39000, mentre i kind da 39001 a 39003 descrivono admin, membri e ruoli supportati. Le azioni di moderazione avvengono tramite eventi della serie 9000 come `put-user`, `remove-user`, `edit-metadata` e `create-invite`.

## Modello di accesso

- **private**: Solo i membri possono leggere i messaggi del gruppo
- **closed**: Le richieste di accesso vengono ignorate a meno che il relay usi la gestione con invite code
- **hidden**: Il relay nasconde i metadata del gruppo ai non membri, rendendo il gruppo non individuabile
- **restricted**: Solo i membri possono scrivere messaggi nel gruppo

Questi tag sono indipendenti. Un gruppo può essere leggibile da tutti ma scrivibile solo dai membri, oppure completamente nascosto ai non membri. Questa separazione conta perché i client non dovrebbero trattare "private" come una scorciatoia generale per ogni regola di accesso.

## Modello di fiducia

NIP-29 non è un protocollo di gruppo trustless. Il relay che ospita decide quali eventi di moderazione sono validi, quali ruoli esistono, se le liste dei membri sono visibili e se messaggi vecchi o fuori contesto vengono accettati. Un client può verificare firme e riferimenti nella timeline, ma si affida comunque alla policy del relay per lo stato reale del gruppo.

Questo rende possibili migrazione e fork, ma non automatici. Lo stesso group id può esistere su relay diversi con storie o regole diverse, quindi l'URL del relay fa parte in pratica dell'identità del gruppo.

## Note utili per l'implementazione

- I client dovrebbero trattare l'URL del relay come chiave host del gruppo. Un chiarimento di gennaio 2026 lo ha reso esplicito nella specifica e ha rimosso l'ambiguità sull'uso di una pubkey al suo posto
- Lo stato del gruppo viene ricostruito dalla cronologia di moderazione, mentre gli eventi relay della serie 39000 sono snapshot informativi di quello stato
- I riferimenti `previous` nella timeline servono a prevenire la ritrasmissione fuori contesto attraverso fork di relay, non solo a migliorare il threading nella UI

---

**Fonti primarie:**
- [Specifica NIP-29](https://github.com/nostr-protocol/nips/blob/master/29.md)
- [PR #2106](https://github.com/nostr-protocol/nips/pull/2106) - Ha chiarito `private`, `closed` e `hidden`
- [PR #2190](https://github.com/nostr-protocol/nips/pull/2190) - Ha chiarito l'URL del relay come chiave del relay
- [PR #2111](https://github.com/nostr-protocol/nips/pull/2111) - Ha aggiunto `unallowpubkey` e `unbanpubkey`

**Citato in:**
- [Newsletter #2: NIP Updates](/it/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #6: NIP Updates](/it/newsletters/2026-01-21-newsletter/)
- [Newsletter #11: NIP Updates](/it/newsletters/2026-02-25-newsletter/)
- [Newsletter #12: NIP Updates](/it/newsletters/2026-03-04-newsletter/)

**Vedi anche:**
- [NIP-11: Relay Information Document](/it/topics/nip-11/)
