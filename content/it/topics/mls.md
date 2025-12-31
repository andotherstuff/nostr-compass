---
title: "MLS (Message Layer Security)"
date: 2025-12-31
translationOf: /en/topics/mls.md
translationDate: 2025-12-31
draft: false
categories:
  - Crittografia
  - Protocollo
  - Messaggistica
  - Privacy
---

Message Layer Security (MLS) è un protocollo standardizzato dall'IETF per la messaggistica di gruppo con crittografia end-to-end. Fornisce un efficiente stabilimento delle chiavi con forward secrecy e sicurezza post-compromissione per gruppi che vanno da due a migliaia di partecipanti.

## Come funziona

MLS utilizza una struttura di accordo delle chiavi basata su albero chiamata TreeKEM:

1. **Pacchetti di chiavi**: Ogni partecipante pubblica un pacchetto di chiavi contenente la propria identità e chiavi di crittografia
2. **Stato del gruppo**: Un albero ratchet mantiene lo stato crittografico del gruppo
3. **Commit**: I membri aggiornano l'albero quando si uniscono, escono o ruotano le chiavi
4. **Crittografia dei messaggi**: Il contenuto viene crittografato usando chiavi derivate dal segreto condiviso del gruppo

## Proprietà di sicurezza chiave

- **Forward secrecy**: I messaggi passati rimangono sicuri anche se le chiavi attuali vengono compromesse
- **Sicurezza post-compromissione**: I messaggi futuri tornano sicuri dopo la rotazione delle chiavi
- **Autenticazione dei membri**: Tutti i membri del gruppo sono verificati crittograficamente
- **Operazione asincrona**: I membri possono unirsi/uscire senza che tutti i partecipanti siano online
- **Scalabilità**: Efficiente per gruppi fino a 50.000 partecipanti

## Standardizzazione

- **RFC 9420** (luglio 2023): Specifica del protocollo MLS principale
- **RFC 9750** (aprile 2025): Architettura MLS per l'integrazione di sistema

## Adozione in Nostr

Diverse applicazioni Nostr utilizzano MLS per la messaggistica di gruppo sicura:

- **KeyChat**: App di messaggistica crittografata basata su MLS per mobile e desktop
- **White Noise**: Messaggistica privata che utilizza MLS con integrazione del protocollo Marmot
- **Marmot Protocol**: Estensione Nostr che fornisce crittografia di gruppo basata su MLS

MLS offre garanzie di sicurezza più forti rispetto a NIP-04 o NIP-44 da soli, particolarmente per le chat di gruppo dove i membri si uniscono e escono dinamicamente.

## Adozione nell'industria

Oltre a Nostr, MLS viene adottato da:
- Google Messages (RCS con MLS via GSMA Universal Profile 3.0)
- Apple Messages (supporto RCS annunciato per MLS)
- Cisco WebEx, Wickr, Matrix

---

**Fonti principali:**
- [RFC 9420: MLS Protocol](https://datatracker.ietf.org/doc/rfc9420/)
- [RFC 9750: MLS Architecture](https://datatracker.ietf.org/doc/rfc9750/)
- [IETF MLS Working Group](https://datatracker.ietf.org/wg/mls/about/)
- [MLS Protocol Website](https://messaginglayersecurity.rocks/)

**Menzionato in:**
- [Newsletter #3: Rilasci](/it/newsletters/2025-12-31-newsletter/#releases)

**Vedi anche:**
- [Marmot Protocol](/it/topics/marmot/)
- [MIP-05: Notifiche Push che Preservano la Privacy](/it/topics/mip-05/)
- [NIP-17: Messaggi Diretti Privati](/it/topics/nip-17/)
- [NIP-44: Payload Crittografati](/it/topics/nip-44/)
