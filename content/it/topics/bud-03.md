---
title: "BUD-03: Lista Server Utente"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

BUD-03 definisce come gli utenti pubblicano i loro server Blossom preferiti, abilitando i client a scoprire dove caricare e recuperare i file media di un utente.

## Come Funziona

Gli utenti pubblicano un evento kind 10063 che elenca i loro server Blossom. I client possono quindi:
- Caricare media sui server preferiti dell'utente
- Scoprire dove trovare i blob di un utente data la sua pubkey

Questo abilita la scoperta basata sull'autore come alternativa all'incorporamento diretto degli URL server nel contenuto.

---

**Fonti primarie:**
- [Specifica BUD-03](https://github.com/hzrd149/blossom/blob/master/buds/03.md)

**Vedi anche:**
- [Protocollo Blossom](/it/topics/blossom/)
- [NIP-51: Liste](/it/topics/nip-51/)

