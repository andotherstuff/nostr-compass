---
title: "NIP-66: Discovery dei Relay e Monitoraggio della Disponibilità"
date: 2026-01-21
translationOf: /en/topics/nip-66.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Relays
---
NIP-66 standardizza la pubblicazione su Nostr dei dati di monitoraggio dei relay. I servizi di monitoraggio testano continuamente i relay per disponibilità, latenza, conformità al protocollo e NIP supportati, pubblicando i risultati come eventi kind 30166.

## Come Funziona

I monitor verificano la disponibilità dei relay connettendosi e inviando subscription di test. Le misurazioni di latenza tracciano il tempo di connessione, il tempo di risposta della subscription e il ritardo di propagazione degli eventi. I test di conformità al protocollo verificano che il comportamento del relay corrisponda alle specifiche, individuando bug di implementazione o deviazioni intenzionali.

La verifica del supporto NIP va oltre le dichiarazioni di [NIP-11](/it/topics/nip-11/) testando davvero se le funzionalità pubblicizzate funzionano correttamente. Se un relay dichiara il supporto alla ricerca di [NIP-50](/it/topics/nip-50/) ma le query di ricerca falliscono, i monitor ometteranno NIP-50 dalla lista verificata. Questo fornisce un dato reale sulle capacità del relay.

Gli eventi kind 30166 usano l'URL del relay come tag `d`, rendendoli eventi parameterized replaceable. Ogni monitor pubblica un evento per relay, aggiornato quando cambiano le misurazioni. Più monitor possono seguire lo stesso relay, fornendo ridondanza e validazione incrociata.

I tag round-trip time (rtt) misurano la latenza per diverse operazioni:
- `rtt open`: apertura della connessione WebSocket
- `rtt read`: tempo di risposta della subscription
- `rtt write`: velocità di pubblicazione dell'evento

Tutti i valori sono in millisecondi. I client usano queste metriche per preferire relay a bassa latenza per operazioni sensibili al tempo.

Le informazioni geografiche aiutano i client a selezionare relay vicini per ottenere latenza migliore e maggiore resistenza alla censura. Il tag `geo` contiene codice del paese, nome del paese e regione. Il tag `network` distingue i relay clearnet dai servizi nascosti Tor o dagli endpoint I2P.

## Perché Conta

NIP-66 trasforma la qualità dei relay da aneddoto a dato leggibile dalle macchine. Un client non deve più fidarsi solo del documento [NIP-11](/it/topics/nip-11/) del relay o di una allowlist hardcoded. Può confrontare uptime misurato, latenza misurata e supporto alle funzionalità testato da uno o più monitor.

Questo conta soprattutto per la selezione dei relay nel modello outbox. Quando i client si connettono dinamicamente a molti relay, relay morti o configurati male impongono un costo diretto in feed più lenti e più fetch falliti.

## Casi d'Uso

I dati dei monitor alimentano i selettori di relay nei client, nei siti explorer e nei sistemi di valutazione della fiducia. Fornendo lo stato dei relay in tempo reale indipendentemente da ciò che i relay dichiarano di sé, NIP-66 permette una selezione dei relay più informata.

Combinato con [NIP-11](/it/topics/nip-11/) (capacità auto-dichiarate) e Trusted Relay Assertions (valutazione della fiducia), l'ecosistema si muove verso una selezione dei relay guidata dai dati invece di affidarsi a impostazioni predefinite hardcoded.

## Modello di Fiducia

NIP-66 non crea un singolo monitor autorevole. Più monitor possono pubblicare risultati per lo stesso relay, e i client possono confrontarli. Questo design riduce la dipendenza dal giudizio di un solo operatore, ma significa anche che i client hanno bisogno di una policy per decidere di chi fidarsi quando i risultati sono in conflitto.

---

**Fonti primarie:**
- [Specifica NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) - Standard per discovery dei relay e monitoraggio della disponibilità

**Menzionato in:**
- [Newsletter #6: Approfondimento NIP](/it/newsletters/2026-01-21-newsletter/#nip-deep-dive-nip-11-and-nip-66)

**Vedi anche:**
- [NIP-11: Documento Informativo del Relay](/it/topics/nip-11/)
- [NIP-65: Metadati della Lista Relay](/it/topics/nip-65/)
- [Trusted Relay Assertions](/it/topics/trusted-relay-assertions/)
