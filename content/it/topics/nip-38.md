---
title: "NIP-38: Stati utente"
date: 2026-08-26
translationOf: /en/topics/nip-38.md
translationDate: 2026-08-26
draft: false
description: "Definisce eventi di stato utente di breve durata, incluse le categorie di stato generale e musicale."
---

NIP-38 definisce eventi indirizzabili kind 30315 per brevi stati utente. Un tag `d` identifica la categoria dello stato, come `general` o `music`, mentre tag `r` e `p` opzionali possono rimandare a una URL o identificare un artista. I client possono usare il tag `expiration` dell'evento per smettere di mostrare stati non più attuali.

## Come funziona

Un utente pubblica un evento kind 30315 con il testo dello stato in `content`. L'evento è indirizzabile per pubkey, kind e tag `d`, così un evento più recente della stessa categoria sostituisce il precedente. Un campo di contenuto vuoto cancella quello stato.

---

**Fonti primarie:**
- [Specifica NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md) - Stati utente

**Menzionato in:**
- [Newsletter #37: NoorNote v1.3.6: stati di profilo e annunci](/it/newsletters/2026-08-26-newsletter/#noornote-v136-stati-di-profilo-e-annunci)
