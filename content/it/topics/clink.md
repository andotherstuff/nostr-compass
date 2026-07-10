---
title: "CLINK: Common Lightning Interface for Nostr Keys"
date: 2026-06-17
draft: false
translationOf: /en/topics/clink.md
translationDate: 2026-07-01
categories:
  - Payments
  - Lightning
---

CLINK (Common Lightning Interface for Nostr Keys) è un formato di richiesta di pagamento proposto che consente a un mittente di pagare qualsiasi identità basata su chiavi Nostr utilizzando una singola interfaccia noffer. Un noffer CLINK codifica la chiave pubblica Nostr del destinatario più metadati di routing sufficienti affinché il wallet del mittente possa costruire un pagamento Lightning, un pagamento on-chain o una futura primitiva di regolamento che si risolve verso il destinatario. Il destinatario pubblica un noffer per identità, e i mittenti lo pagano senza sapere se il wallet ricevente regola tramite Lightning, on-chain o un altro binario.

## Come funziona

Un noffer CLINK è una richiesta di pagamento strutturata che il wallet del mittente decodifica in un'istruzione di pagamento concreta. Il noffer contiene:

- La chiave pubblica Nostr del destinatario come radice canonica dell'identità
- Uno o più endpoint di pagamento (URI del nodo Lightning, suggerimento per la derivazione di un indirizzo on-chain, futuri binari)
- Metadati opzionali per il pagamento (memo, importo, scadenza)
- Una firma del destinatario che vincola il noffer alla sua identità Nostr

Un wallet mittente che supporta CLINK legge il noffer, sceglie il binario che può servire (un wallet solo Lightning paga l'endpoint Lightning, un wallet multi-binario sceglie il percorso più economico) e invia il pagamento. Il wallet del destinatario conferma la ricezione pubblicando o recuperando il corrispondente evento di completamento, con la chiave pubblica Nostr che funge da identità duratura attraverso i binari.

## Perché un'interfaccia basata su chiavi Nostr

LNURL e BOLT-12 esistono già come formati di richiesta di pagamento Lightning, e Bitcoin dispone di un formato di indirizzo ben noto per il regolamento on-chain. CLINK non sostituisce nessuno dei due. Aggiunge un livello radicato sulla chiave Nostr in modo che un mittente possa indirizzare un destinatario tramite la sua identità Nostr e lasciare che il wallet risolva quale binario sottostante utilizzare. Un utente che cambia provider Lightning, apre una nuova mint o migra il suo wallet on-chain ripubblica il suo noffer con la stessa chiave Nostr, e i mittenti non devono aggiornare le loro rubriche.

Per Zeus Pay (che genera un noffer CLINK per ogni account), questo significa che un mittente può pagare qualsiasi utente Zeus tramite la sola chiave Nostr. Per il driver di zap on-chain di Amethyst, la macchina a stati di verifica CLINK conferma che il noffer firmato on-chain corrisponde al pubkey Nostr dichiarato nella richiesta di zap, chiudendo un percorso di contraffazione contro gli zap on-chain non firmati.

## Implementazioni

- [Zeus v13.1.0-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1) rilascia il supporto ai pagamenti tramite noffer CLINK, con Zeus Pay che genera un noffer CLINK per ogni account in modo che un mittente possa pagare qualsiasi utente Zeus tramite la sola chiave Nostr
- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) rilascia un driver CLINK per la verifica degli zap on-chain con una macchina a stati di verifica e un driver di ri-verifica ([PR #3039](https://github.com/vitorpamplona/amethyst/pull/3039), [PR #3177](https://github.com/vitorpamplona/amethyst/pull/3177), [PR #3182](https://github.com/vitorpamplona/amethyst/pull/3182))

---

**Fonti primarie:**
- [Note di rilascio Zeus v13.1.0-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1) - Rilascio del noffer CLINK
- [Amethyst PR #3039](https://github.com/vitorpamplona/amethyst/pull/3039) - Macchina a stati di verifica degli zap on-chain NIP-BC e driver di ri-verifica
- [Amethyst PR #3177](https://github.com/vitorpamplona/amethyst/pull/3177) - Implementazione di CLINK (Common Lightning Interface for Nostr Keys)
- [Amethyst PR #3182](https://github.com/vitorpamplona/amethyst/pull/3182) - Aggiunta del supporto kotlinx-serialization per i DTO del protocollo CLINK

**Menzionato in:**
- [Newsletter #27: Amethyst v1.12.0 rilascia wallet Cashu, nutzap, un driver CLINK e Tor self-heal](/it/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
- [Newsletter #27: Zeus v13.1.0-rc1 rilascia i noffer CLINK e NWC senza coda](/it/newsletters/2026-06-17-newsletter/#zeus-v1310-rc1-ships-clink-noffers-and-queue-less-nwc)

**Vedi anche:**
- [NIP-57: Zaps](/it/topics/nip-57/)
- [NIP-47: Nostr Wallet Connect](/it/topics/nip-47/)
