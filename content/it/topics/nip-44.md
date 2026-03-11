---
title: "NIP-44: Payload crittografati"
date: 2025-12-31
translationOf: /en/topics/nip-44.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - Cryptography
  - Privacy
---
NIP-44 definisce uno standard di crittografia versionato per i payload Nostr, sostituendo lo schema di crittografia NIP-04, difettoso, con primitive crittografiche moderne.

## Come funziona

NIP-44 versione 2 usa un processo di crittografia in più fasi:

1. **Accordo della chiave**: ECDH (secp256k1) tra le chiavi pubbliche del mittente e del destinatario produce un segreto condiviso
2. **Derivazione della chiave**: HKDF-extract con SHA256 e salt `nip44-v2` crea una chiave di conversazione
3. **Chiavi per messaggio**: HKDF-expand deriva chiave ChaCha, nonce e chiave HMAC da un nonce casuale
4. **Padding**: Il contenuto riceve padding per nascondere la lunghezza del messaggio
5. **Crittografia**: ChaCha20 crittografa il contenuto con padding
6. **Autenticazione**: HMAC-SHA256 fornisce l'integrità del messaggio

L'output è un payload base64 versionato che va dentro un normale evento Nostr firmato. La specifica richiede ai client di validare la firma dell'evento esterno NIP-01 prima di decrittare il payload interno NIP-44.

## Scelte crittografiche

- **ChaCha20** invece di AES: più veloce, migliore resistenza agli attacchi multi-key
- **HMAC-SHA256** invece di Poly1305: i MAC polinomiali sono più facili da falsificare
- **SHA256**: coerente con le primitive Nostr esistenti
- **Formato versionato**: permette futuri aggiornamenti degli algoritmi

## Proprietà di sicurezza

- **Authenticated Encryption**: i messaggi non possono essere manomessi
- **Length Hiding**: il padding nasconde la dimensione del messaggio
- **Chiavi di conversazione**: la stessa chiave per conversazioni in corso riduce il calcolo
- **Sottoposto ad audit**: l'audit di sicurezza di Cure53 non ha trovato vulnerabilità sfruttabili

## Note di implementazione

NIP-44 non è un sostituto diretto dei payload NIP-04. Definisce un formato di crittografia, non un kind di evento per messaggi diretti. Protocolli come [NIP-17](/it/topics/nip-17/) e [NIP-59](/it/topics/nip-59/) definiscono come i payload crittografati vengono usati nei flussi di messaggi reali.

L'input in chiaro è testo UTF-8 con una lunghezza da 1 a 65535 byte. Questo è un vincolo reale per chi implementa: se la tua applicazione deve crittografare blob binari arbitrari, ti serve una codifica aggiuntiva o un formato contenitore diverso.

## Limiti

NIP-44 non fornisce:
- **Forward Secrecy**: chiavi compromesse espongono i messaggi passati
- **Post-Compromise Security**: recupero dopo la compromissione della chiave
- **Deniability**: i messaggi sono firmati in modo dimostrabile da chiavi specifiche
- **Metadata Hiding**: l'architettura dei relay limita la privacy

Per esigenze di alta sicurezza, NIP-104 (double ratchet) o protocolli basati su MLS come Marmot offrono garanzie più forti.

## Storia

La revisione 3 di NIP-44 è stata unita a dicembre 2023 dopo un audit di sicurezza indipendente di Cure53. Costituisce la base crittografica per i DM privati di NIP-17 e per il gift wrapping di NIP-59.

---

**Fonti primarie:**
- [NIP-44 Specification](https://github.com/nostr-protocol/nips/blob/master/44.md)
- [NIP-44 Reference Implementations](https://github.com/paulmillr/nip44)
- [Cure53 Audit Report](https://cure53.de/audit-report_nip44-implementations.pdf)

**Citato in:**
- [Newsletter #4: NIP Deep Dive](/it/newsletters/2026-01-07-newsletter/#nip-44-versioned-encryption)
- [Newsletter #3: December 2023](/it/newsletters/2025-12-31-newsletter/#december-2023-ecosystem-maturation)
- [Newsletter #3: December 2024](/it/newsletters/2025-12-31-newsletter/#december-2024-protocol-advancement)
- [Newsletter #12: Marmot](/it/newsletters/2026-03-04-newsletter/#marmot-development-kit-ships-first-public-release)

**Vedi anche:**
- [NIP-04: Messaggi diretti crittografati (deprecato)](/it/topics/nip-04/)
- [NIP-17: Messaggi diretti privati](/it/topics/nip-17/)
- [NIP-59: Gift Wrap](/it/topics/nip-59/)
- [NIP-104: Double Ratchet Encryption](/it/topics/nip-104/)
- [MLS: Message Layer Security](/it/topics/mls/)
