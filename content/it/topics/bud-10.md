---
title: "BUD-10: Schema URI Blossom"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

BUD-10 definisce uno schema URI personalizzato per Blossom che incorpora tutte le informazioni necessarie per recuperare un file da qualsiasi server disponibile.

## Formato URI

```
blossom:<sha256>.<ext>?size=<bytes>&server=<url>&server=<url>&pubkey=<hex>
```

Componenti:
- **sha256**: Hash del file (obbligatorio)
- **ext**: Estensione del file
- **size**: Dimensione del file in byte
- **server**: Uno o piu' suggerimenti server
- **pubkey**: Pubkey autori per scoperta server BUD-03

## Benefici

- Piu' resiliente degli URL HTTP statici
- Fallback automatico su piu' server
- Scoperta basata sull'autore tramite suggerimenti pubkey
- Auto-verificante (l'hash assicura l'integrita')

---

**Fonti primarie:**
- [PR BUD-10](https://github.com/hzrd149/blossom/pull/84)

**Menzionato in:**
- [Newsletter #1: Notizie](/it/newsletters/2025-12-17-newsletter/#news)

**Vedi anche:**
- [Protocollo Blossom](/it/topics/blossom/)
- [BUD-03: Lista Server Utente](/it/topics/bud-03/)

