---
title: "FROST (Flexible Round-Optimized Schnorr Threshold Signatures)"
date: 2025-12-31
translationOf: /en/topics/frost.md
translationDate: 2026-03-07
draft: false
categories:
  - Cryptography
  - Protocol
---
FROST (Flexible Round-Optimized Schnorr Threshold Signatures) è uno schema di threshold signature che permette a un gruppo di produrre una singola firma Schnorr valida senza che nessun partecipante detenga l'intera chiave privata.

## Come funziona

FROST abilita la firma T-of-N. Qualsiasi sottoinsieme che soddisfa la soglia può cooperare per produrre una firma per la chiave pubblica del gruppo.

Il protocollo di firma usa due round:

1. **Round di commitment**: ogni partecipante genera e condivide commitment crittografici
2. **Round di firma**: i partecipanti combinano le loro firme parziali in una firma aggregata finale

L'output finale si verifica come una normale firma Schnorr. I verificatori vedono una firma sotto una chiave pubblica, non un elenco di cofirmatari.

## Note di sicurezza

La gestione dei nonce è critica. L'RFC è esplicito sul fatto che i nonce di firma sono monouso. Il riuso può esporre materiale di chiave.

L'RFC inoltre non standardizza la distributed key generation. Specifica il protocollo di firma stesso e include la generazione delle chiavi con trusted dealer solo come appendice. In pratica, la sicurezza di un deployment FROST dipende sia dal flusso di firma sia da come le share sono state create e conservate.

## Casi d'uso in Nostr

Nel contesto di Nostr, FROST può supportare:

- **Governance di quorum**: i gruppi possono condividere un nsec tramite schemi T-of-N, in cui i membri possono rappresentare sé stessi o delegare a consigli
- **Amministrazione multi-sig**: moderazione comunitaria che richiede più firme di amministratori
- **Gestione decentralizzata delle chiavi**: distribuzione della fiducia tra più parti per operazioni critiche

## Stato

FROST è specificato in [RFC 9591](https://datatracker.ietf.org/doc/rfc9591/), pubblicato sullo stream IRTF nel giugno 2024. Questo dà al protocollo una specifica pubblica stabile, ma non è un RFC IETF standards-track.

---

**Fonti primarie:**
- [RFC 9591: FROST Protocol](https://datatracker.ietf.org/doc/rfc9591/)
- [FROST Paper (IACR)](https://eprint.iacr.org/2020/852.pdf)
- [Zcash Foundation Rust Implementation](https://github.com/ZcashFoundation/frost)

**Citato in:**
- [Newsletter #3: NIPs Repository](/en/newsletters/2025-12-31-newsletter/#nips-repository)
- [Newsletter #8](/en/newsletters/2026-02-04-newsletter/)
- [Newsletter #10](/en/newsletters/2026-02-18-newsletter/)

**Vedi anche:**
- [NIP-46: Nostr Connect](/it/topics/nip-46/)
- [NIP-55: Android Signer Application](/it/topics/nip-55/)
