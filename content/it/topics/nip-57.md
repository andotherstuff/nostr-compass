---
title: "NIP-57: Zap"
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
  - Social
---

NIP-57 definisce gli zap, un modo per inviare pagamenti Lightning a utenti e contenuti Nostr con prova crittografica che il pagamento e' avvenuto.

## Come Funziona

1. Il client recupera l'indirizzo Lightning del destinatario dal suo profilo kind 0
2. Il client richiede una fattura dal server LNURL del destinatario, includendo un evento zap request
3. L'utente paga la fattura
4. Il server LNURL pubblica una ricevuta zap kind 9735 sui relay Nostr
5. I client visualizzano lo zap sul contenuto del destinatario

## Zap Request (kind 9734)

La zap request e' un evento firmato che prova chi ha inviato lo zap e a quale contenuto. Include:
- Tag `p` con pubkey destinatario
- Tag `e` con evento zappato (opzionale)
- Tag `amount` in millisatoshi
- Tag `relays` che elenca dove pubblicare la ricevuta

## Zap Receipt (kind 9735)

Pubblicata dal server LNURL dopo la conferma del pagamento. Contiene:
- La zap request originale in un tag `description`
- Tag `bolt11` con la fattura pagata
- Tag `preimage` che prova il pagamento

---

**Fonti primarie:**
- [Specifica NIP-57](https://github.com/nostr-protocol/nips/blob/master/57.md)

**Menzionato in:**
- [Newsletter #1: Notizie](/it/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: Notizie](/it/newsletters/2025-12-24-newsletter/#news)

**Vedi anche:**
- [NIP-47: Nostr Wallet Connect](/it/topics/nip-47/)

