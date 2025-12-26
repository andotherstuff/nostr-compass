---
title: "Protocollo Marmot"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---

Marmot e' un protocollo per messaggistica di gruppo crittografata end-to-end costruito su Nostr, usando lo standard Message Layer Security (MLS) per forward secrecy e sicurezza post-compromissione.

## Come Funziona

Marmot estende Nostr con cifratura basata su MLS per chat di gruppo. A differenza dei DM NIP-17 che sono uno-a-uno, Marmot gestisce comunicazione di gruppo sicura dove i membri possono unirsi e lasciare mantenendo le garanzie di cifratura.

## Funzionalita' Principali

- Forward secrecy e sicurezza post-compromissione tramite MLS
- Gestione chiavi di gruppo per appartenenza dinamica
- Notifiche push che preservano la privacy tramite MIP-05

---

**Fonti primarie:**
- [Repository Protocollo Marmot](https://github.com/marmot-protocol/marmot)

**Menzionato in:**
- [Newsletter #1: Notizie](/it/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1: Rilasci](/it/newsletters/2025-12-17-newsletter/#releases)

**Vedi anche:**
- [MIP-05: Notifiche Push che Preservano la Privacy](/it/topics/mip-05/)
- [NIP-17: Messaggi Diretti Privati](/it/topics/nip-17/)
- [NIP-59: Gift Wrap](/it/topics/nip-59/)

