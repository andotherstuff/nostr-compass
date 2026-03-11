---
title: "NIP-91: Operatore AND per i filtri"
date: 2026-03-04
translationOf: /en/topics/nip-91.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - Protocol
---
NIP-91 aggiunge la semantica di filtro AND per gli array di tag nelle sottoscrizioni ai relay Nostr. È stato unito il 2026-03-03 dopo che implementazioni sono comparse in più relay.

## Il problema

Il sistema di filtri di Nostr ([NIP-01](/it/topics/nip-01/)) combina più valori all'interno di un singolo filtro di tag usando una logica OR. Se un client specifica due valori di tag `p` in un filtro, il relay restituisce eventi che corrispondono a una delle due pubkey. Non c'era modo di richiedere eventi che facessero riferimento a entrambe le pubkey nello stesso momento.

Questo costringeva i client a scaricare troppi eventi dai relay e a filtrarli localmente, aumentando l'uso di banda e il tempo di elaborazione.

## Come funziona

NIP-91 introduce la semantica AND per gli array di tag. Quando un client ha bisogno di eventi che corrispondano a tutti i valori di tag specificati, può scegliere il matching per intersezione invece del comportamento di unione predefinito.

Questo conta per query come "eventi che taggano entrambi i partecipanti a una conversazione" oppure "eventi che portano due etichette richieste nello stesso momento". Prima di questo cambiamento, i relay potevano rispondere solo con l'insieme più ampio e lasciare al client l'intersezione precisa.

## Perché è importante

I filtri AND rendono più utili gli indici lato relay. I client possono chiedere a un relay un insieme di risultati più piccolo e già rilevante, riducendo banda e post-elaborazione locale. Il vantaggio si nota di più sui client mobili e nelle query su grandi dataset ricchi di tag.

## Note di interoperabilità

Al momento del merge, esistevano implementazioni funzionanti in nostr-rs-relay, satellite-node, worker-relay e applesauce. La proposta era in precedenza numerata NIP-119 prima della rinumerazione.

I client devono comunque aspettarsi un supporto misto mentre l'adozione da parte dei relay procede. Un fallback pratico è mantenere il vecchio percorso di intersezione lato client per i relay che non hanno ancora implementato la nuova semantica.

---

**Fonti primarie:**
- [PR #1365](https://github.com/nostr-protocol/nips/pull/1365)

**Menzionato in:**
- [Newsletter #12: NIP Updates](/it/newsletters/2026-03-04-newsletter/#nip-updates)

**Vedi anche:**
- [NIP-01: Basic Protocol](/it/topics/nip-01/)
