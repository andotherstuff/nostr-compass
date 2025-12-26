---
title: "NIP-51: Liste"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Social
---

NIP-51 definisce vari tipi di liste per organizzare riferimenti a eventi, utenti e contenuti in Nostr.

## Tipi di Lista

- **Kind 10000**: Lista mute (utenti, thread o parole da nascondere)
- **Kind 10001**: Lista pin (eventi da evidenziare sul profilo)
- **Kind 30000**: Set follow (liste follow categorizzate)
- **Kind 30003**: Set segnalibri
- **Kind 30004**: Set curati (articoli)
- **Kind 30005**: Set video
- **Kind 30006**: Set immagini
- **Kind 30015**: Set interessi (hashtag)
- **Kind 30030**: Set emoji

## Struttura

Le liste usano tag per referenziare contenuti:
- Tag `p` per pubkey
- Tag `e` per eventi
- Tag `a` per eventi indirizzabili
- Tag `t` per hashtag
- Tag `word` per parole mutate

## Pubblico vs Privato

Le liste possono avere tag pubblici (visibili a tutti) e contenuto cifrato (privato). Gli elementi privati sono cifrati usando NIP-44 e memorizzati nel campo `content` dell'evento. La cifratura usa le proprie chiavi dell'autore (cifrando per se stessi).

Questo permette funzionalita' come segnalibri pubblici con note private, o una lista mute dove gli elementi mutati sono nascosti agli altri.

## Modifiche Recenti

- Tag hashtag e URL rimossi dai segnalibri generici; gli hashtag ora usano kind 30015
- Kind 30006 aggiunto per set di immagini curate

---

**Fonti primarie:**
- [Specifica NIP-51](https://github.com/nostr-protocol/nips/blob/master/51.md)

**Menzionato in:**
- [Newsletter #1: Aggiornamenti NIP](/it/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #2: Aggiornamenti NIP](/it/newsletters/2025-12-24-newsletter/#nip-updates)

**Vedi anche:**
- [NIP-02: Lista Follow](/it/topics/nip-02/)

