---
title: "NIP-44: Encrypted Payloads"
date: 2025-12-31
translationOf: /en/topics/nip-44.md
translationDate: 2025-12-31
draft: false
categories:
  - NIP
  - Crittografia
  - Privacy
---

NIP-44 definisce uno standard di crittografia versionato per i payload Nostr, sostituendo lo schema di crittografia difettoso di NIP-04 con primitive crittografiche moderne.

## Come Funziona

NIP-44 versione 2 utilizza un processo di crittografia a più fasi:

1. **Accordo delle Chiavi**: ECDH (secp256k1) tra le chiavi pubbliche del mittente e del destinatario produce un segreto condiviso
2. **Derivazione delle Chiavi**: HKDF-extract con SHA256 e salt `nip44-v2` crea una chiave di conversazione
3. **Chiavi Per Messaggio**: HKDF-expand deriva la chiave ChaCha, nonce e chiave HMAC da un nonce casuale
4. **Padding**: Il contenuto viene riempito per nascondere la lunghezza del messaggio
5. **Crittografia**: ChaCha20 cripta il contenuto riempito
6. **Autenticazione**: HMAC-SHA256 fornisce l'integrità del messaggio

## Scelte Crittografiche

- **ChaCha20** rispetto ad AES: Più veloce, migliore resistenza agli attacchi multi-chiave
- **HMAC-SHA256** rispetto a Poly1305: I MAC polinomiali sono più facili da falsificare
- **SHA256**: Coerente con le primitive Nostr esistenti
- **Formato Versionato**: Consente futuri aggiornamenti degli algoritmi

## Proprietà di Sicurezza

- **Crittografia Autenticata**: I messaggi non possono essere manomessi
- **Occultamento della Lunghezza**: Il padding oscura la dimensione del messaggio
- **Chiavi di Conversazione**: La stessa chiave per conversazioni continue riduce il calcolo
- **Verificato**: L'audit di sicurezza Cure53 non ha trovato vulnerabilità sfruttabili

## Limitazioni

NIP-44 non fornisce:
- **Forward Secrecy**: Le chiavi compromesse espongono i messaggi passati
- **Post-Compromise Security**: Recupero dopo la compromissione delle chiavi
- **Negabilità**: I messaggi sono probabilmente firmati da chiavi specifiche
- **Occultamento dei Metadati**: L'architettura dei relay limita la privacy

Per esigenze di alta sicurezza, NIP-104 (double ratchet) o protocolli basati su MLS come Marmot offrono garanzie più forti.

## Storia

NIP-44 revisione 3 è stato unito a dicembre 2023 a seguito di un audit di sicurezza indipendente di Cure53. Costituisce la base crittografica per i DM privati NIP-17 e il gift wrapping NIP-59.

---

**Fonti primarie:**
- [Specifica NIP-44](https://github.com/nostr-protocol/nips/blob/master/44.md)
- [Implementazioni di Riferimento NIP-44](https://github.com/paulmillr/nip44)
- [Rapporto di Audit Cure53](https://cure53.de/audit-report_nip44-implementations.pdf)

**Menzionato in:**
- [Newsletter #3: Dicembre 2023](/it/newsletters/2025-12-31-newsletter/#december-2023-ecosystem-maturation)
- [Newsletter #3: Dicembre 2024](/it/newsletters/2025-12-31-newsletter/#december-2024-protocol-advancement)

**Vedi anche:**
- [NIP-04: Encrypted Direct Messages (deprecato)](/it/topics/nip-04/)
- [NIP-17: Messaggi Diretti Privati](/it/topics/nip-17/)
- [NIP-59: Gift Wrap](/it/topics/nip-59/)
- [NIP-104: Double Ratchet Encryption](/it/topics/nip-104/)
- [MLS: Message Layer Security](/it/topics/mls/)
