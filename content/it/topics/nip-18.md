---
title: "NIP-18: Repost"
date: 2025-12-17
draft: false
categories:
  - Social
  - Protocol
---

NIP-18 definisce come fare repost di eventi, simile ai retweet su altre piattaforme.

## Struttura

Un repost e' un evento kind 6 (per note kind 1) o kind 16 (repost generico) contenente:
- Tag `e` che referenzia l'evento repostato
- Tag `p` che referenzia l'autore originale
- Opzionalmente, l'evento originale completo nel campo `content`

## Modifiche Recenti

Migliorato il supporto per il repost di eventi sostituibili con supporto tag `a`. Questo permette ai repost di eventi indirizzabili (kind 30000-39999) di referenziarli tramite il loro indirizzo invece di uno specifico ID evento.

---

**Fonti primarie:**
- [Specifica NIP-18](https://github.com/nostr-protocol/nips/blob/master/18.md)

**Menzionato in:**
- [Newsletter #1: Aggiornamenti NIP](/it/newsletters/2025-12-17-newsletter/#nip-updates)

**Vedi anche:**
- [NIP-01: Protocollo Base](/it/topics/nip-01/)

