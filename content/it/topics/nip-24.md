---
title: "NIP-24: Campi Metadati Extra"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Identity
---

NIP-24 definisce campi opzionali aggiuntivi per i metadati utente kind 0 oltre a name, about e picture di base.

## Campi Metadati Extra

- **display_name**: Un nome alternativo, piu' grande con caratteri piu' ricchi rispetto a `name`
- **website**: Un URL web relativo all'autore dell'evento
- **banner**: URL di un'immagine larga (~1024x768) per visualizzazione opzionale come sfondo
- **bot**: Booleano che indica che il contenuto e' interamente o parzialmente automatizzato
- **birthday**: Oggetto con campi opzionali anno, mese e giorno

## Tag Standard

NIP-24 standardizza anche tag di uso generale:
- `r`: Riferimento URL web
- `i`: Identificatore esterno
- `title`: Nome per vari tipi di evento
- `t`: Hashtag (deve essere minuscolo)

---

**Fonti primarie:**
- [Specifica NIP-24](https://github.com/nostr-protocol/nips/blob/master/24.md)

**Menzionato in:**
- [Newsletter #1: Aggiornamenti NIP](/it/newsletters/2025-12-17-newsletter/#nip-updates)

**Vedi anche:**
- [NIP-01: Protocollo Base](/it/topics/nip-01/)

