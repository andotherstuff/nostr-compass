---
title: "BUD-03: Elenco dei server utente"
date: 2025-12-17
translationOf: /en/topics/bud-03/
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---
BUD-03 definisce come un utente pubblica i propri server Blossom preferiti, così i client sanno dove caricare i blob e dove cercare quando un URL media smette di funzionare.

## Come funziona

Gli utenti pubblicano un evento replaceable kind `10063` con uno o più tag `server`. Ogni tag contiene un URL completo di un server Blossom.

I client possono quindi:
- caricare blob sui server preferiti dell'utente
- individuare posizioni probabili dei blob dalla pubkey dell'autore
- riprovare il recupero dai server elencati quando un URL meno recente si rompe

## Dettagli utili per il lettore

L'ordine dei tag `server` conta. La specifica dice che gli utenti dovrebbero elencare prima i server più affidabili o di cui si fidano di più, e i client devono almeno provare il primo server per gli upload. Questo significa che BUD-03 non è solo una directory, è anche un debole segnale di preferenza.

Anche la guida per il recupero è pratica: quando un client estrae un hash blob da un URL, dovrebbe usare l'ultima stringa esadecimale di 64 caratteri nel percorso. Questo aiuta i client a recuperare blob sia da URL Blossom standard sia da URL non standard in stile CDN che incorporano comunque l'hash.

---

**Fonti primarie:**
- [BUD-03 Specification](https://github.com/hzrd149/blossom/blob/master/buds/03.md)
- [Blossom Repository](https://github.com/hzrd149/blossom)

**Citato in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)

**Vedi anche:**
- [Blossom Protocol](/it/topics/blossom/)
- [NIP-51: Lists](/it/topics/nip-51/)
