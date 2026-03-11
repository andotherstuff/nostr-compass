---
title: "NIP-17: Messaggi diretti privati"
date: 2025-12-17
translationOf: /en/topics/nip-17.md
translationDate: 2026-03-11
draft: false
categories:
  - Privacy
  - Messaging
---
NIP-17 definisce messaggi diretti privati usando il gift wrapping NIP-59 per la privacy del mittente. A differenza dei DM NIP-04, che espongono il mittente nell'evento esterno, NIP-17 nasconde il mittente ai relay e agli osservatori occasionali.

## Come funziona

I messaggi vengono avvolti in più livelli di cifratura:
1. Il contenuto reale del messaggio vive in un rumor event di kind 14.
2. Un seal cifra quel contenuto per il destinatario.
3. Un gift wrap cifra di nuovo il seal e lo pubblica da una keypair usa e getta.

Il gift wrap esterno usa una keypair casuale e usa e getta, così relay e osservatori non possono determinare chi ha inviato il messaggio.

## Struttura del messaggio

- **Kind 14** - Il contenuto reale del DM all'interno dei livelli avvolti
- **Kind 1059** - L'evento gift wrap esterno pubblicato ai relay
- Usa la cifratura NIP-44 per i payload all'interno del flusso di wrapping
- La specifica è stata rifinita per supportare meglio funzioni interattive dei DM come le reactions

## Modello di sicurezza e fiducia

- I relay non possono vedere il mittente (nascosto dalla keypair usa e getta del gift wrap)
- Il destinatario è visibile (nel tag `p` del gift wrap)
- I timestamp dei messaggi vengono randomizzati entro una finestra
- Nessun threading o raggruppamento delle conversazioni visibile sul relay

Il destinatario continua comunque a sapere chi ha inviato il messaggio dopo averlo aperto. NIP-17 nasconde l'identità del mittente dalla rete, non dall'altro partecipante. Questa è una distinzione importante quando viene descritto come "DM privati".

## Perché è importante

I DM NIP-04 cifrano il contenuto ma lasciano visibili i metadati:
- La pubkey del mittente è pubblica
- La pubkey del destinatario è nel tag `p`
- I timestamp sono esatti

NIP-17 nasconde il mittente al costo di un'implementazione più complessa.

Questa complessità compra un miglioramento reale della privacy. Un relay può ancora vedere che un messaggio avvolto è indirizzato a un destinatario, ma non può costruire direttamente un grafo mittente-destinatario a partire dai metadati dell'evento esterno come può fare con i messaggi kind 4.

## Note di interoperabilità

NIP-17 definisce anche liste di inbox relay per la messaggistica privata. I client possono pubblicare un evento kind 10050 così i mittenti sanno quali relay usare per la consegna dei DM. Tenere separato l'instradamento dei relay per i DM dall'instradamento dei contenuti pubblici aiuta a evitare che traffico privato venga pubblicato nei posti sbagliati.

---

**Fonti principali:**
- [Specifica NIP-17](https://github.com/nostr-protocol/nips/blob/master/17.md)
- [PR #2098](https://github.com/nostr-protocol/nips/pull/2098) - pulizia del testo e aggiornamento del supporto alle reactions

**Menzionato in:**
- [Newsletter #1: NIP Updates](/it/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #2: News](/it/newsletters/2025-12-24-newsletter/#news)
- [Newsletter #3: December Recap](/it/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #3: Notable Code Changes](/it/newsletters/2025-12-31-newsletter/#shopstr-marketplace)
- [Newsletter #5: News](/it/newsletters/2026-01-13-newsletter/#news)

**Vedi anche:**
- [NIP-04: Encrypted Direct Messages (Deprecated)](/it/topics/nip-04/)
- [NIP-44: Encrypted Payloads](/it/topics/nip-44/)
- [NIP-59: Gift Wrap](/it/topics/nip-59/)
