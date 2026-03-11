---
title: "NIP-33: Eventi sostituibili parametrizzati (eventi indirizzabili)"
date: 2026-03-11
translationOf: /en/topics/nip-33.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-33 definiva originariamente gli eventi sostituibili parametrizzati, una classe di eventi in cui i relay conservano un solo evento per tupla `(pubkey, kind, d-tag)`. Da allora il concetto è stato rinominato in "eventi indirizzabili" e incorporato in [NIP-01](/it/topics/nip-01/). Il documento NIP-33 ora reindirizza a NIP-01, ma resta un riferimento comune nei codebase e nella documentazione.

## Come funziona

Un evento indirizzabile usa un kind nell'intervallo `30000-39999`. Ogni evento porta un tag `d` il cui valore, insieme alla pubkey dell'autore e al numero di kind, forma un indirizzo unico. Quando un relay riceve un nuovo evento che corrisponde a una tupla `(pubkey, kind, d-tag)` esistente, sostituisce l'evento più vecchio con quello più nuovo (in base a `created_at`). Questo rende gli eventi indirizzabili utili per stato mutabile: profili, impostazioni, configurazioni delle app, annunci classificati e strutture simili in cui conta solo la versione più recente.

I client referenziano gli eventi indirizzabili con tag `a` nel formato `<kind>:<pubkey>:<d-tag>`, facoltativamente seguiti da un relay hint.

## Usi comuni

- Kind `30023` articoli long-form
- Kind `30078` dati specifici dell'app (usati da NIP-78)
- Kind `31923` eventi del calendario (NIP-52)
- Kind `31990` raccomandazioni di handler (NIP-89)
- Kind `30009` definizioni di badge (NIP-58)
- Kind `31991` configurazioni di esecuzione degli agenti (Notedeck Agentium)

## Relazione con NIP-01

NIP-33 è stato unito in NIP-01 come parte di uno sforzo di consolidamento. La spec di NIP-01 definisce ora tre categorie di conservazione degli eventi: eventi regolari (conservati così come sono), eventi sostituibili (uno per `(pubkey, kind)`) ed eventi indirizzabili (uno per `(pubkey, kind, d-tag)`). NIP-33 resta una scorciatoia valida per il concetto di evento indirizzabile.

---

**Fonti primarie:**
- [NIP-33 (redirect)](https://github.com/nostr-protocol/nips/blob/master/33.md)
- [NIP-01 Specification](https://github.com/nostr-protocol/nips/blob/master/01.md) - Sezione sugli eventi indirizzabili

**Citato in:**
- [Newsletter #13: Notedeck aggiunge limiti relay NIP-11 e funzionalità Agentium](/it/newsletters/2026-03-11-newsletter/#notedeck-aggiunge-limiti-relay-nip-11-e-funzionalita-agentium)

**Vedi anche:**
- [NIP-01: Protocollo di base](/it/topics/nip-01/)
