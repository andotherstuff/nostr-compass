---
title: "NIP-32: Etichettatura"
date: 2026-01-21
translationOf: /en/topics/nip-32.md
translationDate: 2026-01-28
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-32 definisce uno standard per allegare etichette a eventi Nostr, utenti e altre entità. Le etichette forniscono metadati strutturati che i client possono usare per categorizzazione, avvisi sui contenuti, sistemi di reputazione e moderazione.

## Come Funziona

Le etichette usano eventi kind 1985 con un tag `L` che definisce il namespace dell'etichetta e tag `l` che applicano etichette specifiche all'interno di quel namespace. L'entità etichettata è referenziata attraverso tag standard come `e` (eventi), `p` (pubkey) o `r` (URL relay).

```json
{
  "kind": 1985,
  "tags": [
    ["L", "content-warning"],
    ["l", "nsfw", "content-warning"],
    ["e", "<event_id>"]
  ],
  "content": "Contiene immagini esplicite"
}
```

Il sistema di namespace previene collisioni tra etichette. Un'etichetta "spam" nel namespace "ugc-moderation" ha semantica diversa da "spam" nel namespace "relay-report". Questo consente a più sistemi di etichettatura di coesistere senza interferenze.

## Casi d'Uso

I sistemi di moderazione dei contenuti usano le etichette per marcare spam, contenuti illegali o violazioni delle policy. I sistemi di reputazione allegano punteggi di fiducia o stato di verifica alle pubkey. Le piattaforme media applicano avvisi sui contenuti (NSFW, violenza, spoiler). Gli operatori dei relay usano le etichette per appelli e risoluzione delle dispute.

La proposta Trusted Relay Assertions usa le etichette NIP-32 per gli appelli dei relay. Quando gli operatori contestano i punteggi di fiducia, pubblicano eventi kind 1985 con `L` = `relay-appeal` e tipi di etichetta come "spam", "censorship" o "score".

Le implementazioni dei client variano nel modo in cui consumano le etichette. Alcuni client trattano le etichette dagli utenti seguiti come raccomandazioni, mentre altri interrogano servizi di etichettatura specializzati. Il design decentralizzato permette agli utenti di scegliere di quali etichettatori fidarsi.

---

**Fonti primarie:**
- [Specifica NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md) - Standard di etichettatura

**Menzionato in:**
- [Newsletter #6: Aggiornamenti NIP](/it/newsletters/2026-01-21-newsletter/#nip-updates)

**Vedi anche:**
- [Trusted Relay Assertions](/it/topics/trusted-relay-assertions/)
- [NIP-51: Liste](/it/topics/nip-51/)
