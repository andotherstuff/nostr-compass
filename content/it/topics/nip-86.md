---
title: "NIP-86: API di Gestione Relay"
date: 2026-04-01
translationOf: /en/topics/nip-86.md
translationDate: 2026-04-01
draft: false
categories:
  - Relays
  - Protocol
---

NIP-86 definisce un'interfaccia JSON-RPC per la gestione dei relay, permettendo ai client autorizzati di inviare comandi amministrativi ai relay tramite un'API standardizzata. Gli operatori dei relay possono bannare o consentire pubkey, gestire liste di accesso e interrogare lo stato del relay senza strumenti specifici per ogni relay.

## Come Funziona

L'API di gestione usa richieste simili a JSON-RPC su HTTP sullo stesso URI dell'endpoint WebSocket del relay. Le richieste usano il content type `application/nostr+json+rpc` e si autenticano con un event firmato [NIP-98](/it/topics/nip-98/) (HTTP Auth) nell'header `Authorization`. Il relay verifica la pubkey richiedente rispetto alla sua lista di amministratori prima di eseguire i comandi.

I metodi disponibili includono il ban e il permesso di pubkey, l'elenco degli utenti bannati e l'interrogazione della configurazione del relay. L'interfaccia standardizzata significa che una singola implementazione client può gestire qualsiasi relay compatibile con NIP-86.

## Implementazioni

- [Amethyst](https://github.com/vitorpamplona/amethyst) - Client Android con UI di gestione relay NIP-86 (v1.07.0+)

---

**Fonti primarie:**
- [Specifica NIP-86](https://github.com/nostr-protocol/nips/blob/master/86.md)
- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - Supporto NIP-86 lato client
- [PR #2039](https://github.com/vitorpamplona/amethyst/pull/2039) - Dialog di ricerca utenti per la gestione relay

**Menzionato in:**
- [Newsletter #16: Amethyst distribuisce la gestione relay](/it/newsletters/2026-04-01-newsletter/#amethyst-distribuisce-note-fissate-gestione-relay-e-request-to-vanish)

**Vedi anche:**
- [NIP-11: Documento Informativo del Relay](/it/topics/nip-11/)
- [NIP-98: HTTP Auth](/it/topics/nip-98/)
- [NIP-42: Autenticazione dei Client verso i Relay](/it/topics/nip-42/)
