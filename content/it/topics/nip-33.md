---
title: "NIP-33: Event Parametrici Sostituibili (Event Indirizzabili)"
date: 2026-03-11
translationOf: /en/topics/nip-33.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-33 definiva originariamente gli event parametrici sostituibili, una classe di event in cui solo un event per tupla `(pubkey, kind, d-tag)` viene mantenuto dai relay. Il concetto è stato successivamente rinominato in "event indirizzabili" e incorporato in [NIP-01](/it/topics/nip-01/). Il documento NIP-33 ora reindirizza a NIP-01 ma rimane un riferimento comune nei codebase e nella documentazione.

## Come Funziona

Un event indirizzabile usa un kind nell'intervallo `30000-39999`. Ogni event porta un tag `d` il cui valore, insieme alla pubkey dell'autore e al numero di kind, forma un indirizzo unico. Quando un relay riceve un nuovo event che corrisponde a una tupla `(pubkey, kind, d-tag)` esistente, sostituisce l'event più vecchio con quello più recente (per `created_at`). Questo rende gli event indirizzabili utili per lo stato mutabile: profili, impostazioni, configurazioni delle app, annunci classificati e strutture simili dove conta solo l'ultima versione.

I client referenziano gli event indirizzabili con tag `a` nel formato `<kind>:<pubkey>:<d-tag>`, opzionalmente seguito da un suggerimento relay.

## Usi Comuni

- Kind `30023` articoli long-form
- Kind `30078` dati specifici dell'app (usato da NIP-78)
- Kind `31923` event calendario (NIP-52)
- Kind `31990` raccomandazioni handler (NIP-89)
- Kind `30009` definizioni badge (NIP-58)
- Kind `31991` configurazioni di esecuzione agenti (Notedeck Agentium)

## Relazione con NIP-01

NIP-33 è stato incorporato in NIP-01 come parte di un consolidamento. La specifica NIP-01 ora definisce tre categorie di conservazione degli event: event regolari (mantenuti così come sono), event sostituibili (uno per `(pubkey, kind)`), e event indirizzabili (uno per `(pubkey, kind, d-tag)`). NIP-33 rimane una scorciatoia valida per il concetto di event indirizzabili.

---

**Fonti primarie:**
- [NIP-33 (redirect)](https://github.com/nostr-protocol/nips/blob/master/33.md)
- [Specifica NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) - Sezione event indirizzabili

**Menzionato in:**
- [Newsletter #13: Notedeck](/en/newsletters/2026-03-11-newsletter/#notedeck-adds-nip-11-relay-limits-and-agentium-features)

**Vedi anche:**
- [NIP-01: Protocollo Base](/it/topics/nip-01/)
