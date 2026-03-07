---
title: "NIP-11: Documento informativo del relay"
date: 2025-12-17
translationOf: /en/topics/nip-11/
translationDate: 2026-03-07
draft: false
categories:
  - Relay
  - Protocol
---
NIP-11 definisce come i relay pubblicano una descrizione di sé leggibile da macchina, incluse le funzionalità che dichiarano di supportare, i limiti e i metadata dell'operatore.

## Come funziona

I client recuperano le informazioni del relay eseguendo una richiesta HTTP GET verso l'URL WebSocket del relay con un header `Accept: application/nostr+json`. Il relay restituisce un documento JSON che descrive le sue capacità.

## Campi utili

- **name** - Nome del relay leggibile da umani
- **description** - A cosa serve il relay
- **supported_nips** - Elenco del supporto NIP dichiarato
- **limitation** - Restrizioni come dimensione massima del messaggio, autenticazione richiesta e così via
- **pubkey** - Chiave pubblica dell'operatore del relay, quando fornita
- **contact** - Indirizzo di contatto dell'operatore

## Modello di fiducia

NIP-11 è metadata auto-dichiarato. Ti dice cosa un relay afferma di essere, non ciò che ha dimostrato nel traffico reale. Questo resta utile per la discovery e per la UX, ma i client non dovrebbero trattare `supported_nips` come verità di fatto senza testarne il comportamento.

Questa distinzione conta per la selezione dei relay. Un relay può pubblicizzare la ricerca NIP-50, requisiti di autenticazione o un grande limite di messaggio, ma la risposta reale emerge solo quando un client si connette davvero e percorre quei code path.

## Perché conta

- I client possono verificare se un relay supporta le funzionalità richieste prima di connettersi
- I servizi di discovery possono indicizzare le capacità dei relay
- Gli utenti possono vedere le policy del relay prima di pubblicare

## Direzione recente della specifica

La specifica è stata ridotta nel tempo. Vecchi campi opzionali come `software`, `version`, dettagli sulla privacy policy e metadata di retention sono stati rimossi dopo anni di adozione debole. Questo rende i documenti NIP-11 attuali più piccoli e più realistici, ma significa anche che i client non dovrebbero aspettarsi metadata di policy ricchi dai relay.

---

**Fonti primarie:**
- [NIP-11 Specification](https://github.com/nostr-protocol/nips/blob/master/11.md)
- [PR #1764](https://github.com/nostr-protocol/nips/pull/1764) - aggiornamento del campo d'identità del relay
- [PR #1946](https://github.com/nostr-protocol/nips/pull/1946) - pulizia dei campi usati di rado
- [PR #2231](https://github.com/nostr-protocol/nips/pull/2231) - rimozione dei campi deprecati

**Citato in:**
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)

**Vedi anche:**
- [NIP-66: Discovery dei relay e monitoraggio della disponibilità](/it/topics/nip-66/)
