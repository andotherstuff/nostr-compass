---
title: "Negentropy: Protocollo di riconciliazione degli insiemi"
date: 2026-01-28
translationOf: /en/topics/negentropy.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Sync
---
Negentropy è un protocollo di set reconciliation per individuare quali eventi possiede una parte e quali mancano all'altra, senza reinviare l'intero dataset.

## Come funziona

Invece di richiedere ogni evento che corrisponde a un filtro, negentropy confronta due insiemi ordinati e restringe il confronto soltanto agli intervalli che differiscono. Il protocollo scambia riassunti compatti degli intervalli e ricorre a liste esplicite di ID solo dove serve.

1. **Ordinamento**: entrambe le parti ordinano i record per timestamp, poi per ID
2. **Confronto degli intervalli**: scambiano fingerprint per intervalli di record
3. **Raffinamento**: gli intervalli non corrispondenti vengono suddivisi finché gli ID mancanti effettivi non sono chiari

## Perché conta

La sincronizzazione Nostr tradizionale usa filtri `since` basati sui timestamp, che possono perdere eventi a causa di:
- Deriva dell'orologio tra client e relay
- Eventi multipli con timestamp identici
- Eventi che arrivano fuori ordine

Negentropy risolve questi problemi confrontando gli insiemi reali di eventi invece di basarsi sui timestamp.

## Uso pratico

- **Recupero dei DM**: i client possono rilevare e recuperare messaggi diretti mancanti anche con timestamp vecchi
- **Sincronizzazione del feed**: garantisce una sincronizzazione completa della timeline tra relay
- **Sincronizzazione offline**: permette di recuperare in modo efficiente dopo periodi di disconnessione

Il dettaglio implementativo utile è che molti client non sostituiscono le normali subscription con negentropy. Lo usano come percorso di riparazione. Damus, per esempio, ha mantenuto il caricamento ordinario dei DM e ha aggiunto negentropy al refresh manuale per recuperare i messaggi che il flusso normale non avrebbe trovato.

## Compromessi

Negentropy richiede supporto da entrambe le parti e aggiunge complessità di protocollo oltre all'uso standard di `REQ`. È più utile quando la correttezza conta più dello sforzo minimo di implementazione.

In ambienti misti, i client hanno comunque bisogno di un fallback graduale perché non tutti i relay supportano il protocollo.

---

**Fonti primarie:**
- [Negentropy Protocol Repository](https://github.com/hoytech/negentropy)
- [Damus PR #3536](https://github.com/damus-io/damus/pull/3536)
- [Damus PR #3547](https://github.com/damus-io/damus/pull/3547)

**Menzionato in:**
- [Newsletter #6: Damus introduces negentropy per una sincronizzazione affidabile dei DM](/en/newsletters/2026-01-28-newsletter/#damus-ships-negentropy-for-reliable-dm-syncing)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**Vedi anche:**
- [NIP-01: Flusso di protocollo di base](/it/topics/nip-01/)
