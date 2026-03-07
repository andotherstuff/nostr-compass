---
title: "NIP-47: Nostr Wallet Connect"
date: 2025-12-17
translationOf: /en/topics/nip-47/
translationDate: 2026-03-07
draft: false
categories:
  - Wallet
  - Lightning
---
NIP-47 definisce Nostr Wallet Connect, un protocollo che permette a un'app Nostr di comunicare con un servizio wallet Lightning remoto senza esporre le credenziali principali del wallet a ogni client.

## Come funziona

Un servizio wallet pubblica un evento informativo replaceable di kind `13194` che descrive i metodi e le modalità di crittografia che supporta. Un client si connette usando un URI `nostr+walletconnect://` che contiene la pubkey del servizio wallet, uno o più relay e un segreto dedicato per quella connessione. Le richieste vengono inviate come eventi kind `23194` e le risposte ritornano come eventi kind `23195`.

## Comandi e notifiche

I metodi comuni includono `pay_invoice`, `pay_keysend`, `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance` e `get_info`. I servizi wallet possono anche inviare notifiche come `payment_received`, `payment_sent` e `hold_invoice_accepted`.

La specifica ha aggiunto nel tempo diversi metodi opzionali, ma una recente pulizia ha rimosso i metodi di pagamento `multi_`. In pratica, l'interoperabilità è migliore quando i client si limitano ai comandi pubblicizzati dall'evento informativo del wallet invece di presumere un insieme ampio di metodi.

## Casi d'uso

- **Zapping** - Invia sats a post, profili o creatori di contenuti
- **Pagamenti** - Paga fatture Lightning da qualsiasi app Nostr
- **Separazione UX del wallet** - Usa un servizio wallet su molti client Nostr

## Note su sicurezza e interoperabilità

L'URI di connessione contiene un segreto dedicato che il client usa per firma e crittografia. Questo assegna a ogni app la propria identità wallet, cosa che aiuta sia la revoca sia la privacy. Un wallet può limitare la spesa, disabilitare metodi o revocare una connessione senza influenzarne un'altra.

NIP-44 è ora la modalità di crittografia preferita. La specifica documenta ancora il fallback a NIP-04 per le implementazioni più vecchie, quindi i client devono esaminare il tag `encryption` pubblicizzato dal wallet invece di presumere che ogni wallet abbia già migrato.

---

**Fonti primarie:**
- [NIP-47 Specification](https://github.com/nostr-protocol/nips/blob/master/47.md)
- [PR #1913: Hold Invoice Support](https://github.com/nostr-protocol/nips/pull/1913)
- [PR #2210: Simplification](https://github.com/nostr-protocol/nips/pull/2210)

**Citato in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: Releases](/en/newsletters/2025-12-24-newsletter/#releases)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #8: NIP Deep Dive](/en/newsletters/2026-02-04-newsletter/#nip-deep-dive-nip-47-nostr-wallet-connect)
- [Newsletter #10: NIP Updates](/en/newsletters/2026-02-18-newsletter/#nip-updates)

**Vedi anche:**
- [NIP-57: Zaps](/it/topics/nip-57/)
