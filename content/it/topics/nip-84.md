---
title: "NIP-84: Highlights"
date: 2026-02-18
translationOf: /en/topics/nip-84.md
translationDate: 2026-03-07
draft: false
categories:
  - Content
  - Protocol
---
NIP-84 definisce eventi "highlight" di kind 9802 che permettono agli utenti di segnare e condividere passaggi che ritengono utili da contenuti long-form su Nostr.

## Come funziona

Il campo `.content` contiene il testo evidenziato. Gli eventi fanno riferimento al materiale sorgente usando tag `a` o `e` per contenuti nativi di Nostr, oppure tag `r` per URL esterni (i client dovrebbero rimuovere i parametri di tracking). I tag `p` opzionali attribuiscono gli autori originali, e un tag `context` opzionale fornisce il testo circostante quando l'highlight è una porzione di un passaggio più ampio.

Per i media non testuali, il contenuto dell'highlight può essere vuoto. Questo dà ai client un modo per puntare a un highlight audio o video mantenendo il riferimento alla sorgente nei tag.

## Quote Highlights

Gli utenti possono aggiungere un tag `comment` per creare quote highlights, che vengono renderizzati come quoted reposts. Questo evita voci duplicate nei client di microblogging. All'interno dei commenti, le menzioni con tag `p` richiedono un attributo `mention` per distinguerle dalle attribuzioni di autore o editor, e gli URL con tag `r` usano un attributo `source` per i riferimenti di origine.

## Perché è importante

NIP-84 separa il passaggio evidenziato dalla discussione circostante. Un client può renderizzare il testo selezionato come oggetto principale e poi trattare il commento come metadato opzionale invece di mescolare entrambi in una nota normale.

Questo è utile per strumenti di lettura e ricerca perché preserva l'estratto esatto. Due lettori possono commentare lo stesso articolo e produrre comunque eventi highlight portabili che altri client comprendono.

## Note di interoperabilità

I tag di attribuzione sono più importanti di quanto sembri. Un tag `p` con ruolo `author` o `editor` dice ai client chi ha creato il materiale sorgente, mentre un ruolo `mention` dentro un quote comment indica altro. Se i client uniscono questi casi, possono etichettare male la sorgente evidenziata o notificare persone in modo errato.

---

**Fonti principali:**
- [NIP-84 Specification](https://github.com/nostr-protocol/nips/blob/master/84.md)

**Menzionato in:**
- [Newsletter #10: Releases](/en/newsletters/2026-02-18-newsletter/#prism-share-anything-to-nostr-from-android)

**Vedi anche:**
- [NIP-94: File Metadata](/it/topics/nip-94/)
