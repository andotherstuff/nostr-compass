---
title: "Proposta NIP-FE: Comandi HTTP per i relay"
date: 2026-09-30
translationOf: /en/topics/nip-fe.md
translationDate: 2026-10-02
draft: false
categories:
  - Project Proposals
  - Relays
---

Amethyst usa l’etichetta provvisoria NIP-FE per i comandi ai relay su HTTP nel suo lavoro sul relay Geode e sul client Quartz. L’etichetta non è un NIP assegnato né una prova di adozione da parte dei relay Nostr.

## Trasporto

Invece di aprire una connessione WebSocket, un client invia con POST un singolo frame `REQ`, `COUNT` o `EVENT` a un endpoint HTTP del relay. La risposta trasmette in streaming i frame del relay come JSON delimitato da newline. Un client deve distinguere una risposta completa da uno stream interrotto, e una richiesta autenticata usa comunque l’autorizzazione HTTP Nostr firmata. Il trasporto cambia il modo in cui i comandi raggiungono un relay; non cambia la firma né il contenuto dell’event sottostante.

L’[implementazione integrata](https://github.com/vitorpamplona/amethyst/pull/4231) di Amethyst aggiunge la route di Geode, il supporto nel client Quartz, limiti sul corpo e sulla concorrenza e test di framing e autorizzazione. È una prova di implementazione a livello di sorgente, non la dimostrazione che relay indipendenti abbiano implementato la stessa proposta.

## Collisione di nomi

Una [bozza di pull request non correlata nel repository dei NIP](https://github.com/nostr-protocol/nips/pull/2488) usa anch’essa **NIP-FE**, in questo caso per feed privati costruiti su una proposta di busta multi-destinatario. Quel lavoro è aperto e descrive un problema diverso dal trasporto HTTP di Amethyst. Nessuno dei due usi provvisori dimostra che l’etichetta sia stata assegnata a una specifica accettata; i lettori dovrebbero identificare la proposta tramite la sua fonte e il suo oggetto.

---

**Fonti primarie:**
- [PR dell’implementazione Geode e Quartz di Amethyst](https://github.com/vitorpamplona/amethyst/pull/4231)
- [Repository di Amethyst](https://github.com/vitorpamplona/amethyst)
- [Bozza aperta sui feed privati che usa anch’essa NIP-FE](https://github.com/nostr-protocol/nips/pull/2488)

**Citato in:**
- [Newsletter #42: comandi ai relay di Amethyst](/it/newsletters/2026-09-30-newsletter/#amethyst-repairs-encrypted-group-interoperability)
