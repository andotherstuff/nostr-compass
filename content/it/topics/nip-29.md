---
title: "NIP-29: Gruppi Basati su Relay"
date: 2025-12-24
draft: false
categories:
  - Social
  - Groups
---

NIP-29 definisce gruppi basati su relay, dove un relay gestisce l'appartenenza al gruppo, i permessi e la visibilita' dei messaggi.

## Tag di Accesso al Gruppo

- **private**: Solo i membri possono leggere i messaggi del gruppo
- **closed**: Le richieste di adesione vengono ignorate (solo su invito)
- **hidden**: Il relay nasconde i metadati del gruppo ai non-membri, rendendo il gruppo non scopribile
- **restricted**: Solo i membri possono scrivere messaggi nel gruppo

Questi tag possono essere combinati. Un gruppo puo' essere `restricted` (scrittura limitata) ma non `hidden` (ancora scopribile). Omettere un tag abilita il comportamento opposto: nessun `private` significa che chiunque puo' leggere, nessun `closed` significa che le richieste di adesione vengono onorate.

## Come Funziona

Il relay e' l'autorita' per le operazioni del gruppo:
- Mantiene la lista membri e i ruoli
- Applica i permessi di scrittura
- Controlla cosa possono vedere i non-membri

I client inviano messaggi di gruppo al relay, che valida l'appartenenza prima di accettarli.

## Considerazioni sulla Privacy

- I gruppi `hidden` forniscono la protezione piu' forte dalla scoperta: non appaiono nelle ricerche o negli elenchi relay
- I gruppi `private` nascondono il contenuto dei messaggi ai non-membri
- I gruppi `closed` semplicemente ignorano le richieste di adesione; combinateli con `private` o `hidden` per un controllo accessi piu' forte
- `restricted` controlla chi puo' scrivere, indipendentemente dall'accesso in lettura

---

**Fonti primarie:**
- [Specifica NIP-29](https://github.com/nostr-protocol/nips/blob/master/29.md)

**Menzionato in:**
- [Newsletter #2: Aggiornamenti NIP](/it/newsletters/2025-12-24-newsletter/#nip-updates)

