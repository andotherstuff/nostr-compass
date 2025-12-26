---
title: "NIP-17: Messaggi Diretti Privati"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-17 definisce i messaggi diretti privati usando il gift wrapping NIP-59 per la privacy del mittente. A differenza dei DM NIP-04 che espongono il mittente, i messaggi NIP-17 nascondono chi ha inviato il messaggio. Il destinatario rimane visibile nel gift wrap esterno.

## Come Funziona

I messaggi sono avvolti in piu' livelli di cifratura:
1. Il contenuto effettivo del messaggio (kind 14)
2. Un seal che cifra il contenuto per il destinatario
3. Un gift wrap che nasconde l'identita' del mittente

Il gift wrap esterno usa una coppia di chiavi casuale e usa e getta cosi' i relay e gli osservatori non possono determinare chi ha inviato il messaggio.

## Struttura del Messaggio

- **Kind 14** - Il contenuto effettivo del DM (dentro il seal)
- Usa cifratura NIP-44 per il contenuto
- Supporta reazioni (kind 7) nelle conversazioni DM

## Garanzie di Privacy

- I relay non possono vedere il mittente (nascosto dalla coppia di chiavi usa e getta del gift wrap)
- Il destinatario e' visibile (nel tag `p` del gift wrap)
- I timestamp dei messaggi sono randomizzati in una finestra
- Nessun threading o raggruppamento conversazioni visibile sul relay

## Confronto con NIP-04

I DM NIP-04 cifrano il contenuto ma lasciano i metadati visibili:
- La pubkey del mittente e' pubblica
- La pubkey del destinatario e' nel tag `p`
- I timestamp sono esatti

NIP-17 nasconde il mittente al costo di un'implementazione piu' complessa.

---

**Fonti primarie:**
- [Specifica NIP-17](https://github.com/nostr-protocol/nips/blob/master/17.md)

**Menzionato in:**
- [Newsletter #1: Aggiornamenti NIP](/it/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #2: Notizie](/it/newsletters/2025-12-24-newsletter/#news)

**Vedi anche:**
- [NIP-59: Gift Wrap](/it/topics/nip-59/)

