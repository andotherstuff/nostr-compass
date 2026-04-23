---
title: "NIP-55: Applicazione signer Android"
date: 2025-12-17
translationOf: /en/topics/nip-55.md
translationDate: 2026-04-22
draft: false
categories:
  - Signing
  - Mobile
---
NIP-55 definisce come le app Android richiedono operazioni di firma e cifratura a un'applicazione signer separata. Dà ai client Android un'alternativa nativa alle estensioni del browser e ai bunker remoti.

## Come funziona

NIP-55 usa due meccanismi Android:

- **Intent** per flussi in foreground con approvazione esplicita dell'utente
- **Content resolver** per flussi in background dopo che l'utente ha concesso un permesso persistente

Il normale flusso di connessione inizia con `get_public_key`. Il signer restituisce sia la pubkey dell'utente sia il nome del pacchetto del signer, e il client deve memorizzarli entrambi in cache. Ripetere `get_public_key` in loop di background è un errore di implementazione comune contro cui la specifica mette in guardia in modo esplicito.

## Operazioni principali

- **get_public_key** - Recupera la pubkey dell'utente e il nome del pacchetto del signer
- **sign_event** - Firma un evento Nostr
- **nip04_encrypt/decrypt** - Cifra o decifra messaggi NIP-04
- **nip44_encrypt/decrypt** - Cifra o decifra messaggi NIP-44
- **decrypt_zap_event** - Decifra payload di eventi legati agli zap

## Note su sicurezza e UX

NIP-55 mantiene le chiavi sul dispositivo, ma dipende comunque dai confini tra app Android e dalla gestione dei permessi del signer. Il supporto ai content resolver offre una UX molto più fluida rispetto a prompt ripetuti tramite intent, ma solo dopo che l'utente ha concesso un'autorizzazione duratura a quel client.

Per le web app su Android, NIP-55 è meno ergonomico di NIP-46. I flussi basati sul browser non possono ricevere risposte dirette in background come fanno le app Android native, quindi molte implementazioni ricadono su callback URL, trasferimento tramite clipboard o incolla manuale.

---

**Fonti principali:**
- [Specifica NIP-55](https://github.com/nostr-protocol/nips/blob/master/55.md)

**Citato in:**
- [Newsletter #1: Releases](/it/newsletters/2025-12-17-newsletter/)
- [Newsletter #2: News](/it/newsletters/2025-12-24-newsletter/)
- [Newsletter #2: NIP Updates](/it/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #7: NIP Updates](/it/newsletters/2026-01-07-newsletter/)
- [Newsletter #11: NIP Deep Dive](/it/newsletters/2026-02-25-newsletter/)

**Vedi anche:**
- [NIP-46: Nostr Connect](/it/topics/nip-46/)
