---
title: "Negentropy: Protocollo di Riconciliazione degli Insiemi"
date: 2026-01-28
translationOf: /en/topics/negentropy.md
translationDate: 2026-01-28
draft: false
categories:
  - Protocol
  - Sync
---

Negentropy è un protocollo di riconciliazione degli insiemi che consente una sincronizzazione efficiente tra client Nostr e relay identificando gli eventi mancanti senza trasferire l'intero dataset.

## Come Funziona

Invece di richiedere tutti gli eventi che corrispondono a un filtro, negentropy permette ai client di confrontare il loro insieme locale di eventi con quello di un relay e identificare solo le differenze. Questo si realizza attraverso un protocollo a più round:

1. **Fingerprinting**: Client e relay calcolano ciascuno un'impronta dei loro insiemi di eventi
2. **Confronto**: Le impronte vengono scambiate e confrontate
3. **Riconciliazione**: Vengono identificati e trasferiti solo gli ID degli eventi mancanti

## Perché È Importante

La sincronizzazione Nostr tradizionale usa filtri `since` basati su timestamp, che possono perdere eventi a causa di:
- Deriva degli orologi tra client e relay
- Eventi multipli con timestamp identici
- Eventi che arrivano fuori ordine

Negentropy risolve questi problemi confrontando gli insiemi di eventi effettivi piuttosto che affidarsi ai timestamp.

## Casi d'Uso

- **Recupero DM**: I client possono rilevare e recuperare messaggi diretti mancanti anche con timestamp vecchi
- **Sincronizzazione Feed**: Assicura la sincronizzazione completa della timeline attraverso i relay
- **Sincronizzazione Offline**: Recupera efficientemente dopo periodi di disconnessione

## Implementazione

Negentropy richiede supporto del relay. I client tipicamente lo implementano come meccanismo di recupero di fallback piuttosto che sostituire le sottoscrizioni REQ standard, degradando con grazia quando i relay non supportano il protocollo.

## Correlati

- [NIP-01](/it/topics/nip-01/) - Protocollo Base
