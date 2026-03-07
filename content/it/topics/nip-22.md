---
title: "NIP-22: Commenti"
date: 2026-01-28
translationOf: /en/topics/nip-22.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Social
---
NIP-22 definisce uno standard per commentare qualsiasi contenuto Nostr indirizzabile, rendendo possibili discussioni in thread su articoli, video, eventi di calendario e altri eventi indirizzabili.

## Come funziona

I commenti usano eventi kind 1111 con `content` in testo semplice. I tag dell'ambito radice sono in maiuscolo, mentre i tag parent-reply sono in minuscolo:

```json
{
  "kind": 1111,
  "tags": [
    ["A", "30023:pubkey:article-id", "wss://relay.example"],
    ["K", "30023"],
    ["P", "<root-pubkey>", "wss://relay.example"],
    ["a", "30023:pubkey:article-id", "wss://relay.example"],
    ["e", "<parent-event-id>", "wss://relay.example", "<parent-pubkey>"],
    ["k", "30023"],
    ["p", "<parent-pubkey>", "wss://relay.example"]
  ],
  "content": "Great article!"
}
```

## Struttura dei tag

- **`A` / `E` / `I`** - Ambito radice della discussione: evento indirizzabile, event id o identificatore esterno
- **`K`** - Kind o tipo di ambito radice per quell'elemento radice
- **`P`** - Autore dell'evento radice quando esiste
- **`a` / `e` / `i`** - Parent immediato a cui si sta rispondendo
- **`k`** - Kind o tipo di ambito dell'elemento parent
- **`p`** - Autore dell'elemento parent

Per i commenti di primo livello, radice e parent di solito puntano allo stesso obiettivo. Per le risposte ai commenti, la radice resta fissa mentre i tag parent in minuscolo si spostano sul commento specifico a cui si sta rispondendo.

## Note di interoperabilità

I commenti NIP-22 non sono un sostituto generico delle risposte kind 1. La specifica dice esplicitamente che i commenti non devono essere usati per rispondere a note kind 1. Per i thread note-to-note, i client devono continuare a usare [NIP-10](/it/topics/nip-10/).

Un'altra distinzione utile riguarda l'ambito. NIP-22 può ancorare la discussione a risorse che non sono note tramite i tag `I` e `i`, incluse URL e altri identificatori esterni da [NIP-73](/it/topics/nip-73/). Questo offre ai client un modo standard per collegare thread di commenti a pagine web, podcast o altri oggetti fuori da Nostr.

## Casi d'uso

- Discussioni su articoli
- Commenti ai video
- Discussioni su eventi di calendario [NIP-52](/it/topics/nip-52/)
- Pagine di discussione per wiki
- Commenti su risorse esterne identificate tramite tag `I`

---

**Fonti primarie:**
- [Specifica NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md)

**Citato in:**
- [Newsletter #7: Notedeck](/en/newsletters/2026-01-28-newsletter/#notedeck)
- [Newsletter #10: AI Agent NIPs Arrive](/en/newsletters/2026-02-18-newsletter/#ai-agent-nips-arrive)
- [Newsletter #12: diVine](/en/newsletters/2026-03-04-newsletter/#divine)

**Vedi anche:**
- [NIP-10: Reply Threads](/it/topics/nip-10/)
- [NIP-52: Calendar Events](/it/topics/nip-52/)
- [NIP-73: External Content IDs](/it/topics/nip-73/)
