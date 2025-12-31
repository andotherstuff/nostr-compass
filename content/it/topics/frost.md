---
title: "FROST (Flexible Round-Optimized Schnorr Threshold Signatures)"
date: 2025-12-31
translationOf: /en/topics/frost.md
translationDate: 2025-12-31
draft: false
categories:
  - Crittografia
  - Protocollo
---

FROST (Flexible Round-Optimized Schnorr Threshold Signatures) è uno schema di firme a soglia che permette a un gruppo di partecipanti di produrre collaborativamente firme Schnorr valide senza che nessuna singola parte possieda la chiave privata completa.

## Come funziona

FROST abilita la firma a soglia T-di-N, dove T partecipanti su N totali detentori di chiavi devono cooperare per produrre una firma valida. Il protocollo opera in due round:

1. **Round di impegno**: Ogni partecipante genera e condivide impegni crittografici
2. **Round di firma**: I partecipanti combinano le loro firme parziali in una firma aggregata finale

La firma risultante è indistinguibile da una firma Schnorr standard, mantenendo la compatibilità retroattiva con i sistemi di verifica esistenti.

## Proprietà chiave

- **Sicurezza a soglia**: Nessun singolo partecipante può firmare da solo; T parti devono cooperare
- **Efficienza dei round**: Solo due round di comunicazione richiesti per firmare
- **Protezione dalla falsificazione**: Tecniche innovative proteggono dagli attacchi agli schemi a soglia precedenti
- **Aggregazione delle firme**: Più firme si combinano in un'unica firma compatta
- **Privacy**: Le firme finali non rivelano quali T partecipanti hanno firmato

## Casi d'uso in Nostr

Nel contesto di Nostr, FROST permette:

- **Governance per quorum**: I gruppi possono condividere un nsec tramite schemi T-di-N, dove i membri possono rappresentare se stessi o delegare a consigli
- **Amministrazione multi-firma**: Moderazione comunitaria che richiede più firme degli amministratori
- **Gestione decentralizzata delle chiavi**: Distribuzione della fiducia tra più parti per operazioni critiche

## Standardizzazione

FROST è stato standardizzato come RFC 9591 nel giugno 2024, intitolato "The Flexible Round-Optimized Schnorr Threshold (FROST) Protocol for Two-Round Schnorr Signatures".

---

**Fonti principali:**
- [RFC 9591: FROST Protocol](https://datatracker.ietf.org/doc/rfc9591/)
- [FROST Paper (IACR)](https://eprint.iacr.org/2020/852.pdf)
- [University of Waterloo CrySP](https://crysp.uwaterloo.ca/software/frost/)
- [Zcash Foundation Rust Implementation](https://github.com/ZcashFoundation/frost)

**Menzionato in:**
- [Newsletter #3: Repository NIPs](/it/newsletters/2025-12-31-newsletter/#nips-repository)

**Vedi anche:**
- [Proposta NIP-XX Quorum](https://github.com/nostr-protocol/nips/pull/2179)
