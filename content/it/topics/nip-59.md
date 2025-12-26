---
title: "NIP-59: Gift Wrap"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-59 definisce il gift wrapping, una tecnica per nascondere il mittente di un evento avvolgendolo in livelli di cifratura con un'identita' usa e getta.

## Struttura

Un evento gift-wrapped ha tre livelli:

1. **Rumor** - Il contenuto dell'evento originale non firmato
2. **Seal** (kind 13) - Il rumor cifrato per il destinatario, firmato dal mittente reale
3. **Gift Wrap** (kind 1059) - Il seal cifrato per il destinatario, firmato da una chiave casuale usa e getta

Il livello esterno usa una coppia di chiavi casuale generata solo per questo messaggio, cosi' gli osservatori non possono collegarlo al mittente.

## Perche' Tre Livelli?

- Il **rumor** contiene il contenuto effettivo
- Il **seal** prova il mittente reale (visibile solo al destinatario)
- Il **gift wrap** nasconde il mittente dai relay e dagli osservatori

## Supporto Eliminazione

Gli eventi gift wrap possono ora essere eliminati tramite richieste di eliminazione NIP-09/NIP-62. Questo e' stato aggiunto per permettere agli utenti di rimuovere messaggi avvolti dai relay.

## Casi d'Uso

- Messaggi diretti privati (NIP-17)
- Segnalazioni anonime o whistleblowing
- Qualsiasi scenario dove la privacy del mittente e' importante

---

**Fonti primarie:**
- [Specifica NIP-59](https://github.com/nostr-protocol/nips/blob/master/59.md)

**Menzionato in:**
- [Newsletter #1: Notizie](/it/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1: Aggiornamenti NIP](/it/newsletters/2025-12-17-newsletter/#nip-updates)

**Vedi anche:**
- [NIP-17: Messaggi Diretti Privati](/it/topics/nip-17/)

