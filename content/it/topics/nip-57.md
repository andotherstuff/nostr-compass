---
title: "NIP-57: Zaps"
date: 2025-12-17
translationOf: /en/topics/nip-57/
translationDate: 2026-03-07
draft: false
categories:
  - Wallet
  - Lightning
  - Social
---
NIP-57 definisce gli zap, un modo per associare pagamenti Lightning a identità e contenuti Nostr. Standardizza sia la richiesta di una invoice abilitata agli zap sia l'evento di ricevuta che i wallet pubblicano dopo il pagamento.

## Come funziona

1. Il client scopre l'endpoint LNURL del destinatario dai metadata del profilo o da un tag `zap` nell'evento di destinazione.
2. Il client invia una richiesta zap firmata di kind `9734` al callback LNURL del destinatario, non ai relay.
3. L'utente paga la invoice.
4. Il server wallet del destinatario pubblica una ricevuta zap di kind `9735` sui relay elencati nella richiesta zap.
5. I client convalidano e mostrano lo zap.

## Richiesta zap (kind 9734)

La richiesta zap è un evento firmato che identifica il pagatore e la destinazione prevista. Di solito include:

- tag `p` con la pubkey del destinatario
- tag `e` con l'evento che riceve lo zap (opzionale)
- tag `amount` in millisatoshi
- tag `relays` che elenca dove pubblicare la ricevuta

Il contenuto addressable può usare un tag `a` al posto di, o insieme a, un tag `e`. Il tag opzionale `k` registra il kind di destinazione.

## Ricevuta zap (kind 9735)

Pubblicata dal server wallet del destinatario dopo la conferma del pagamento. Contiene:

- La richiesta zap originale in un tag `description`
- tag `bolt11` con la invoice pagata
- tag `preimage` che prova il pagamento

I client dovrebbero convalidare la ricevuta rispetto al `nostrPubkey` LNURL del destinatario, all'importo della invoice e alla richiesta zap originale. Una ricevuta senza questa convalida è solo un'affermazione.

## Fiducia e compromessi

Gli zap sono utili perché rendono visibili i pagamenti nel social graph, ma la ricevuta viene comunque creata dall'infrastruttura wallet del destinatario. La specifica stessa osserva che una ricevuta zap non è una prova universale di pagamento. È meglio intenderla come una dichiarazione firmata dal wallet secondo cui una invoice collegata a una richiesta zap è stata pagata.

---

**Fonti primarie:**
- [NIP-57 Specification](https://github.com/nostr-protocol/nips/blob/master/57.md)

**Citato in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: News](/en/newsletters/2025-12-24-newsletter/#news)
- [Newsletter #3: Notable Code Changes](/en/newsletters/2025-12-31-newsletter/#amethyst-android)
- [Newsletter #9: NIP Updates](/en/newsletters/2026-02-11-newsletter/#nip-updates)

**Vedi anche:**
- [NIP-47: Nostr Wallet Connect](/it/topics/nip-47/)
