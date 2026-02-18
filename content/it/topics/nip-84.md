---
title: "NIP-84: Highlights"
date: 2026-02-18
translationOf: /en/topics/nip-84.md
translationDate: 2026-02-18
draft: false
categories:
  - Content
  - Protocol
---

NIP-84 definisce gli eventi kind 9802 "highlight" che permettono agli utenti di contrassegnare e condividere passaggi di valore trovati nei contenuti long-form su Nostr.

## Come Funziona

Il campo `.content` contiene il testo evidenziato. Gli eventi referenziano il materiale sorgente usando tag `a` o `e` per i contenuti nativi Nostr, o tag `r` per URL esterni (i client dovrebbero rimuovere i parametri di tracciamento). I tag `p` opzionali attribuiscono gli autori originali, e un tag `context` opzionale fornisce il testo circostante quando l'highlight è una porzione di un passaggio più ampio.

## Highlight con Citazione

Gli utenti possono aggiungere un tag `comment` per creare highlight con citazione, che si renderizzano come repost citati. Questo previene voci duplicate nei client di microblogging. All'interno dei commenti, le menzioni tramite tag `p` richiedono un attributo "mention" per distinguerle dalle attribuzioni di autore/editor, e gli URL tramite tag `r` usano un attributo "source" per i riferimenti di origine.

---

**Fonti primarie:**
- [Specifica NIP-84](https://github.com/nostr-protocol/nips/blob/master/84.md)

**Citato in:**
- [Newsletter #10: Rilasci](/it/newsletters/2026-02-18-newsletter/#prism-condividi-qualsiasi-cosa-su-nostr-da-android)

**Vedi anche:**
- [NIP-94: File Metadata](/it/topics/nip-94/)
