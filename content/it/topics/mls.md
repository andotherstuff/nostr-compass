---
title: "MLS (Message Layer Security)"
date: 2025-12-31
translationOf: /en/topics/mls.md
translationDate: 2026-03-07
draft: false
categories:
  - Cryptography
  - Protocol
  - Messaging
  - Privacy
---
Message Layer Security (MLS) è un protocollo IETF per la messaggistica di gruppo end-to-end encrypted. Fornisce forward secrecy e post-compromise security per gruppi in cui l'appartenenza può cambiare nel tempo.

## Come funziona

MLS usa una struttura di accordo sulle chiavi basata su alberi chiamata TreeKEM:

1. **Key Packages**: ogni partecipante pubblica un key package che contiene la propria identità e le chiavi di cifratura
2. **Group State**: un ratchet tree mantiene lo stato crittografico del gruppo
3. **Commits**: i membri aggiornano l'albero quando entrano, escono o ruotano le chiavi
4. **Message Encryption**: il contenuto viene cifrato usando chiavi derivate dal segreto condiviso del gruppo

## Perché conta

MLS risolve un problema che la cifratura pairwise non risolve bene: mantenere coerenti appartenenza al gruppo e stato di cifratura mentre i membri entrano, escono o ruotano le chiavi in modo asincrono.

La sua struttura ad albero è l'idea pratica. Gli aggiornamenti non richiedono che ogni partecipante rinegozi pairwise con tutti gli altri, quindi il protocollo scala molto meglio degli schemi ad hoc di chiavi di gruppo.

## Standardizzazione

- **RFC 9420** (luglio 2023): specifica del protocollo MLS di base
- **RFC 9750** (aprile 2025): architettura MLS per l'integrazione di sistema

## Adozione in Nostr

Diverse applicazioni Nostr usano MLS per la messaggistica di gruppo sicura:

- **KeyChat**: app di messaggistica cifrata basata su MLS per mobile e desktop
- **White Noise**: messaggistica privata che usa MLS con integrazione del protocollo Marmot
- **Marmot Protocol**: estensione Nostr che fornisce cifratura di gruppo basata su MLS

MLS offre garanzie di sicurezza di gruppo più forti rispetto a [NIP-04](/it/topics/nip-04/) o [NIP-44](/it/topics/nip-44/) da soli, soprattutto quando l'appartenenza cambia spesso.

## Compromessi

MLS non è un prodotto di messaggistica completo. Le applicazioni hanno comunque bisogno di identità, trasporto, resistenza allo spam, storage e gestione dei conflitti attorno al protocollo.

Per questo i progetti Nostr come Marmot aggiungono regole extra sopra MLS. La crittografia è standardizzata, ma il protocollo applicativo attorno ad essa conta ancora per l'interoperabilità.

---

**Fonti primarie:**
- [RFC 9420: MLS Protocol](https://datatracker.ietf.org/doc/rfc9420/)
- [RFC 9750: MLS Architecture](https://datatracker.ietf.org/doc/rfc9750/)
- [IETF MLS Working Group](https://datatracker.ietf.org/wg/mls/about/)
- [MLS Protocol Website](https://messaginglayersecurity.rocks/)

**Citato in:**
- [Newsletter #3: Releases](/en/newsletters/2025-12-31-newsletter/#releases)
- [Newsletter #10](/en/newsletters/2026-02-18-newsletter/)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**Vedi anche:**
- [Marmot Protocol](/it/topics/marmot/)
- [MIP-05: Privacy-Preserving Push Notifications](/it/topics/mip-05/)
- [NIP-17: Private Direct Messages](/it/topics/nip-17/)
- [NIP-44: Encrypted Payloads](/it/topics/nip-44/)
