---
title: "NIP-32: Etichettatura"
date: 2026-01-21
translationOf: /en/topics/nip-32.md
translationDate: 2026-03-07
draft: false
categories:
  - NIPs
  - Protocol
---
NIP-32 definisce uno standard per allegare etichette agli eventi Nostr, agli utenti e ad altre entità. Le etichette forniscono metadati strutturati che i client possono usare per categorizzazione, avvisi sui contenuti, sistemi di reputazione e moderazione.

## Come funziona

Le etichette usano eventi kind 1985 con un tag `L` che definisce il namespace dell'etichetta e tag `l` che applicano etichette specifiche all'interno di quel namespace. L'entità etichettata viene referenziata tramite tag standard come `e` (eventi), `p` (pubkeys) o `r` (URL di relay).

```json
{
  "kind": 1985,
  "tags": [
    ["L", "content-warning"],
    ["l", "nsfw", "content-warning"],
    ["e", "<event_id>"]
  ],
  "content": "Contains explicit imagery"
}
```

Il sistema di namespace impedisce collisioni tra etichette. Un'etichetta "spam" nel namespace "ugc-moderation" ha una semantica diversa da "spam" nel namespace "relay-report". Questo consente a più sistemi di etichettatura di coesistere senza interferenze.

## Perché è importante

La scelta progettuale chiave è che le etichette sono asserzioni, non fatti incorporati nel protocollo. Un evento kind 1985 dice che un certo attore ha etichettato qualcosa in un certo namespace. I client hanno comunque bisogno di una policy di fiducia per decidere quali etichette mostrare, nascondere o ignorare.

Questo rende NIP-32 utile ben oltre la moderazione. La stessa struttura può trasportare avvisi sui contenuti, marcatori di verifica, sistemi di classificazione o dati sulla reputazione dei relay senza costringere tutti i client a usare un unico vocabolario globale.

## Casi d'uso

I sistemi di moderazione dei contenuti usano etichette per segnalare spam, contenuti illegali o violazioni di policy. I sistemi di reputazione associano punteggi di fiducia o stato di verifica alle pubkeys. Le piattaforme media applicano avvisi sui contenuti come NSFW, violenza o spoiler. Gli operatori di relay usano etichette per appelli e risoluzione delle controversie.

La proposta Trusted Relay Assertions usa etichette NIP-32 per gli appelli ai relay. Quando gli operatori contestano i punteggi di fiducia, pubblicano eventi kind 1985 con `L = relay-appeal` ed etichette come `spam`, `censorship` o `score`.

## Note di interoperabilità

I client differiscono nel modo in cui consumano le etichette. Alcuni trattano le etichette provenienti da utenti seguiti come raccomandazioni, mentre altri interrogano servizi di etichettatura specializzati. Il design decentralizzato consente agli utenti di scegliere di quali labeler fidarsi, ma significa anche che un'etichetta senza contesto di fiducia visibile può essere fuorviante.

---

**Fonti primarie:**
- [NIP-32 Specification](https://github.com/nostr-protocol/nips/blob/master/32.md) - Standard di etichettatura

**Citato in:**
- [Newsletter #6: NIP Updates](/en/newsletters/2026-01-21-newsletter/#nip-updates)

**Vedi anche:**
- [Trusted Relay Assertions](/it/topics/trusted-relay-assertions/)
- [NIP-51: Lists](/it/topics/nip-51/)
