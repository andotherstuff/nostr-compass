---
title: "NIP-04: Messaggi Diretti Crittografati (Deprecato)"
date: 2025-12-31
translationOf: /en/topics/nip-04.md
translationDate: 2025-12-31
draft: false
categories:
  - Privacy
  - Messaggistica
---

NIP-04 definisce i messaggi diretti crittografati utilizzando la crittografia AES-256-CBC. Era il metodo originale per la messaggistica privata su Nostr, ma è stato deprecato in favore di NIP-17 a causa di significative limitazioni di privacy.

## Come funziona

I messaggi utilizzano eventi di kind 4 con il seguente schema di crittografia:
1. Un segreto condiviso viene generato usando ECDH con la chiave pubblica del destinatario e la chiave privata del mittente
2. Il messaggio viene crittografato con AES-256-CBC
3. Il testo cifrato viene codificato in base64 con il vettore di inizializzazione aggiunto
4. Un tag `p` identifica la chiave pubblica del destinatario

## Limitazioni di sicurezza

NIP-04 ha significative carenze di privacy:

- **Perdita di metadati** - La pubkey del mittente è pubblicamente visibile su ogni messaggio
- **Nessuna privacy del mittente** - Chiunque può vedere chi sta inviando messaggi a chi
- **Timestamp esatti** - Il timing dei messaggi non è randomizzato
- **Implementazione non standard** - Usa solo la coordinata X del punto ECDH invece dell'hash SHA256 standard

La specifica avverte esplicitamente che "non si avvicina nemmeno allo stato dell'arte nella comunicazione crittografata".

## Stato di deprecazione

NIP-04 è deprecato in favore di NIP-17, che utilizza il gift wrapping di NIP-59 per nascondere l'identità del mittente. Le nuove implementazioni dovrebbero usare NIP-17 per la messaggistica privata.

---

**Fonti principali:**
- [Specifica NIP-04](https://github.com/nostr-protocol/nips/blob/master/04.md)

**Menzionato in:**
- [Newsletter #3: Riepilogo di Dicembre](/it/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Vedi anche:**
- [NIP-17: Messaggi Diretti Privati](/it/topics/nip-17/)
- [NIP-59: Gift Wrap](/it/topics/nip-59/)
