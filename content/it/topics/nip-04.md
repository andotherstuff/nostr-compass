---
title: "NIP-04: Messaggi diretti cifrati (deprecato)"
date: 2025-12-31
translationOf: /en/topics/nip-04.md
translationDate: 2026-04-22
draft: false
categories:
  - Privacy
  - Messaging
---
NIP-04 definisce i messaggi diretti cifrati usando eventi kind 4 e un segreto condiviso derivato con ECDH. È stato il primo schema DM di Nostr, ma oggi è tecnologia legacy e il nuovo lavoro sulla messaggistica privata si è spostato su NIP-17.

## Come funziona

I messaggi usano eventi kind 4 con questo flusso di base:

1. Il mittente deriva un segreto condiviso con secp256k1 ECDH.
2. Il plaintext viene cifrato con AES-256-CBC.
3. L'evento include un tag `p` che identifica il destinatario.
4. Il ciphertext viene codificato in base64 e memorizzato in `content` insieme all'IV.

L'evento stesso resta un normale evento Nostr firmato, quindi i relay possono vedere i metadati esterni anche se non possono leggere il plaintext.

## Limiti di sicurezza e privacy

NIP-04 ha limiti di privacy significativi:

- **Perdita di metadati** - La pubkey del mittente è visibile pubblicamente in ogni messaggio
- **Nessuna privacy del mittente** - Chiunque può vedere chi sta scrivendo a chi
- **Timestamp esatti** - Il timing dei messaggi non viene randomizzato
- **Gestione delle chiavi non standard** - Lo schema usa solo la coordinata X del punto ECDH, cosa che ha reso più difficile la correttezza tra librerie diverse e ha lasciato poco spazio all'evoluzione del protocollo

La specifica avverte esplicitamente che "does not go anywhere near the state-of-the-art in encrypted communication."

## Perché è stato sostituito

NIP-04 cifra il contenuto dei messaggi, ma non nasconde il grafo sociale. Gli operatori dei relay possono comunque vedere chi ha inviato l'evento, chi lo riceve e quando è stato pubblicato. Sono metadati sufficienti per mappare le conversazioni anche senza decifrare il payload.

NIP-17 affronta questo problema combinando la cifratura del payload di NIP-44 con il gift wrapping di NIP-59, che nasconde il mittente ai relay e agli osservatori casuali. Le nuove implementazioni dovrebbero trattare NIP-04 solo come livello di compatibilità.

## Stato di implementazione

Client legacy e signer espongono ancora metodi di cifratura e decifratura NIP-04 perché vecchie conversazioni e applicazioni meno recenti sono ancora in circolazione. Questo livello di compatibilità conta per la migrazione, ma costruire nuove funzionalità sopra eventi kind 4 di solito significa trascinare in avanti i vecchi limiti di privacy.

---

**Fonti primarie:**
- [NIP-04 Specification](https://github.com/nostr-protocol/nips/blob/master/04.md)

**Menzionato in:**
- [Newsletter #4: NIP Deep Dive](/it/newsletters/2026-01-07-newsletter/)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/)

**Vedi anche:**
- [NIP-44: Payload cifrati](/it/topics/nip-44/)
- [NIP-17: Messaggi diretti privati](/it/topics/nip-17/)
- [NIP-59: Gift Wrap](/it/topics/nip-59/)
