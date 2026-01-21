---
title: "Trusted Relay Assertions"
date: 2026-01-21
draft: false
categories:
  - Protocol
  - Relays
---

Trusted Relay Assertions è una proposta di bozza NIP per standardizzare il punteggio di fiducia nei relay e la gestione della reputazione. La specifica introduce eventi kind 30385 dove i fornitori di asserzioni pubblicano punteggi di fiducia calcolati da metriche osservate, reputazione dell'operatore e segnalazioni degli utenti.

## Come Funziona

La proposta riempie una lacuna nell'ecosistema relay. Mentre [NIP-11](/it/topics/nip-11/) definisce cosa i relay affermano su se stessi e [NIP-66](/it/topics/nip-66/) misura cosa osserviamo, Trusted Relay Assertions standardizza cosa concludiamo sull'affidabilità dei relay.

I fornitori di asserzioni calcolano punteggi attraverso tre dimensioni. L'affidabilità misura disponibilità, velocità di recupero, consistenza e latenza. La qualità valuta la documentazione delle politiche, la sicurezza TLS e la responsabilità dell'operatore. L'accessibilità valuta le barriere di accesso, la libertà di giurisdizione e il rischio di sorveglianza. Un punteggio di fiducia complessivo (0-100) combina questi componenti con pesi: 40% affidabilità, 35% qualità, 25% accessibilità.

Ogni asserzione include livelli di confidenza (basso, medio, alto) basati sul conteggio delle osservazioni. La verifica dell'operatore usa più metodi: prova crittografica tramite documenti NIP-11 firmati, record TXT DNS o file .well-known. La specifica integra Web of Trust attraverso punteggi di fiducia dell'operatore. La classificazione delle politiche aiuta gli utenti a trovare relay appropriati: aperto, moderato, curato o specializzato.

Gli utenti dichiarano i fornitori di asserzioni fidati tramite eventi kind 10385. I client interrogano più fornitori e confrontano i punteggi. La proposta include un processo di appello dove gli operatori relay possono contestare i punteggi usando eventi di etichettatura [NIP-32](/it/topics/nip-32/).

## Casi d'Uso

Per i signer remoti [NIP-46](/it/topics/nip-46/), le asserzioni di fiducia aiutano gli utenti a valutare relay non familiari incorporati negli URI di connessione prima di accettare le connessioni. Combinato con le liste relay [NIP-65](/it/topics/nip-65/), i client possono prendere decisioni informate sulla selezione dei relay basate sia sulle preferenze degli utenti che sulle valutazioni di fiducia di terze parti.

La specifica complementa i meccanismi di scoperta relay esistenti. [NIP-66](/it/topics/nip-66/) fornisce la scoperta (cosa esiste), questa proposta aggiunge la valutazione (cosa è buono). Insieme abilitano la selezione informata dei relay piuttosto che fare affidamento su default codificati o raccomandazioni di passa-parola.

---

**Fonti primarie:**
- [Documento NIP in Bozza](https://nostr.com/nevent1qqsqjymvcp6ch3ps3fqsxljf6j8u3adz64ucw8npnzuj3cn6dekn0gspz9mhxue69uhkummnw3ezumrpdejz7qg3waehxw309ahx7um5wgh8w6twv5hsyga3qg) - Evento kind 30817 che propone la specifica

**Menzionato in:**
- [Newsletter #6: Notizie](/it/newsletters/2026-01-21-newsletter/#trusted-relay-assertions-un-nuovo-approccio-alla-fiducia-nei-relay)
- [Newsletter #6: Aggiornamenti NIP](/it/newsletters/2026-01-21-newsletter/#aggiornamenti-nip)

**Vedi anche:**
- [NIP-11: Documento Informativo Relay](/it/topics/nip-11/)
- [NIP-66: Scoperta Relay e Monitoraggio Liveness](/it/topics/nip-66/)
- [NIP-32: Etichettatura](/it/topics/nip-32/)
