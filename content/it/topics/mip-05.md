---
title: "MIP-05: Notifiche Push che Preservano la Privacy"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Messaging
  - Protocol
---

MIP-05 definisce un protocollo per notifiche push che mantengono la privacy degli utenti, risolvendo il problema che i sistemi push tradizionali richiedono che i server conoscano i token dei dispositivi e le identita' degli utenti.

## Come Funziona

- I token dei dispositivi sono cifrati con ECDH+HKDF e ChaCha20-Poly1305
- Le chiavi effimere prevengono la correlazione tra notifiche
- Un protocollo gossip a tre eventi (kind 447-449) sincronizza i token cifrati tra i membri del gruppo
- Token esca tramite gift wrapping NIP-59 nascondono le dimensioni dei gruppi

## Garanzie di Privacy

- I server di notifiche push non possono identificare gli utenti
- L'appartenenza al gruppo non viene rivelata dai pattern di notifica
- I token dei dispositivi non possono essere correlati tra messaggi

## Kind degli Eventi

- **Kind 447**: Pubblicazione token dispositivo cifrato
- **Kind 448**: Richiesta sincronizzazione token
- **Kind 449**: Risposta sincronizzazione token

---

**Fonti primarie:**
- [PR MIP-05](https://github.com/marmot-protocol/marmot/pull/18)

**Menzionato in:**
- [Newsletter #1: Notizie](/it/newsletters/2025-12-17-newsletter/#news)

**Vedi anche:**
- [Protocollo Marmot](/it/topics/marmot/)
- [NIP-59: Gift Wrap](/it/topics/nip-59/)

