---
title: "NIP-47: Nostr Wallet Connect"
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
---

NIP-47 definisce un protocollo per connettere applicazioni Nostr a wallet Lightning, abilitando pagamenti senza esporre le credenziali del wallet a ogni app.

## Come Funziona

Un wallet (come Zeus) esegue un servizio NWC che ascolta richieste di pagamento su specifici relay Nostr. Le app si connettono usando una stringa di connessione che include la pubkey del wallet e le informazioni del relay. Le richieste e risposte di pagamento sono cifrate tra l'app e il wallet.

## Casi d'Uso

- **Zapping** - Invia sat a post, profili o creatori di contenuti
- **Pagamenti** - Paga fatture Lightning da qualsiasi app Nostr
- **Abbonamenti** - Pagamenti ricorrenti per contenuti premium

## Funzionalita' Principali

- **Controlli budget** - Imposta limiti di spesa per connessione
- **Relay personalizzati** - Usa il tuo relay per la comunicazione wallet
- **Pagamenti paralleli** - Processa piu' zap simultaneamente per operazioni batch

---

**Fonti primarie:**
- [Specifica NIP-47](https://github.com/nostr-protocol/nips/blob/master/47.md)

**Menzionato in:**
- [Newsletter #1: Notizie](/it/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: Rilasci](/it/newsletters/2025-12-24-newsletter/#releases)

**Vedi anche:**
- [NIP-57: Zap](/it/topics/nip-57/)

