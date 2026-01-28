---
title: "NIP-66: Scoperta Relay e Monitoraggio Disponibilità"
date: 2026-01-21
translationOf: /en/topics/nip-66.md
translationDate: 2026-01-28
draft: false
categories:
  - NIPs
  - Relays
---

NIP-66 standardizza la pubblicazione di dati di monitoraggio dei relay su Nostr. I servizi di monitoraggio testano continuamente i relay per disponibilità, latenza, conformità al protocollo e NIP supportate, pubblicando i risultati come eventi kind 30166.

## Come Funziona

I monitor verificano la disponibilità dei relay connettendosi e inviando sottoscrizioni di test. Le misurazioni di latenza tracciano tempo di connessione, tempo di risposta alle sottoscrizioni e ritardo di propagazione degli eventi. I test di conformità al protocollo verificano che il comportamento del relay corrisponda alle specifiche, rilevando bug di implementazione o deviazioni intenzionali.

La verifica del supporto NIP va oltre le dichiarazioni [NIP-11](/it/topics/nip-11/) testando effettivamente se le funzionalità pubblicizzate funzionano correttamente. Se un relay dichiara supporto per la ricerca [NIP-50](/it/topics/nip-50/) ma le query di ricerca falliscono, i monitor ometteranno NIP-50 dalla lista verificata. Questo fornisce la verità sul campo riguardo alle capacità dei relay.

Gli eventi kind 30166 usano l'URL del relay come tag `d`, rendendoli eventi sostituibili parametrizzati. Ogni monitor pubblica un evento per relay, aggiornato man mano che le misurazioni cambiano. Più monitor possono tracciare lo stesso relay, fornendo ridondanza e cross-validazione.

I tag round-trip time (rtt) misurano la latenza per diverse operazioni:
- `rtt open`: Stabilimento connessione WebSocket
- `rtt read`: Tempo di risposta alla sottoscrizione
- `rtt write`: Velocità di pubblicazione eventi

Tutti i valori sono in millisecondi. I client usano queste metriche per preferire relay a bassa latenza per operazioni time-sensitive.

Le informazioni geografiche aiutano i client a selezionare relay vicini per migliore latenza e resistenza alla censura. Il tag `geo` contiene codice paese, nome paese e regione. Il tag `network` distingue i relay clearnet dai servizi nascosti Tor o endpoint I2P.

## Casi d'Uso

I dati di monitoraggio alimentano selettori di relay nei client, siti web explorer e sistemi di valutazione della fiducia. Fornendo stato relay in tempo reale indipendente dall'auto-reporting del relay, NIP-66 abilita la selezione informata dei relay.

Combinato con [NIP-11](/it/topics/nip-11/) (capacità auto-dichiarate) e Trusted Relay Assertions (valutazione della fiducia), l'ecosistema si muove verso una selezione dei relay basata sui dati piuttosto che affidarsi a default hardcoded.

---

**Fonti primarie:**
- [Specifica NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) - Standard di scoperta relay e monitoraggio disponibilità

**Menzionato in:**
- [Newsletter #6: Approfondimento NIP](/it/newsletters/2026-01-21-newsletter/#nip-deep-dive-nip-11-and-nip-66)

**Vedi anche:**
- [NIP-11: Documento Informativo del Relay](/it/topics/nip-11/)
- [Trusted Relay Assertions](/it/topics/trusted-relay-assertions/)
