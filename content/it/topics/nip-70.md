---
title: "NIP-70: Eventi protetti"
date: 2026-03-11
translationOf: /en/topics/nip-70.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Relay
  - Access Control
---

NIP-70 definisce un modo con cui gli autori possono contrassegnare un evento come protetto tramite il semplice tag `[["-"]]`. Un evento protetto può essere accettato solo quando un relay sceglie di supportare quel comportamento e verifica che il publisher autenticato sia la stessa pubkey dell'autore dell'evento.

## Come funziona

La regola centrale è breve. Se un evento contiene il tag `[["-"]]`, un relay dovrebbe rifiutarlo per impostazione predefinita. Un relay che vuole supportare gli eventi protetti deve prima eseguire il flusso `AUTH` di [NIP-42](/it/topics/nip-42/) e confermare che il client autenticato stia pubblicando il proprio evento.

Questo rende NIP-70 una regola sull'autorità di pubblicazione, non una regola di cifratura. Il contenuto può comunque restare leggibile. Quello che cambia è chi può collocare quell'evento su un relay che onora il tag. Questo permette ai relay di supportare feed semi-chiusi e altri contesti in cui gli autori vogliono che un relay rifiuti la ripubblicazione da parte di terzi.

```json
{
  "id": "cb8feca582979d91fe90455867b34dbf4d65e4b86e86b3c68c368ca9f9eef6f2",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1707409439,
  "kind": 1,
  "tags": [
    ["-"]
  ],
  "content": "hello members of the secret group",
  "sig": "fa163f5cfb75d77d9b6269011872ee22b34fb48d23251e9879bb1e4ccbdd8aaaf4b6dc5f5084a65ef42c52fbcde8f3178bac3ba207de827ec513a6aa39fa684c"
}
```

## Implicazioni del flusso AUTH

Gli eventi protetti sono utili solo quando i relay applicano davvero l'identità dell'autore al momento della pubblicazione. Per questo NIP-70 dipende così direttamente da [NIP-42](/it/topics/nip-42/). Un relay che accetta eventi `[["-"]]` senza un controllo auth corrispondente sta trattando il tag come decorazione, non come policy.

## Comportamento e limiti dei relay

NIP-70 non promette che il contenuto resterà confinato per sempre. Qualsiasi destinatario può ancora copiare ciò che vede e pubblicare un nuovo evento altrove. La spec offre solo ai relay un modo standard per rispettare l'intento dell'autore e rifiutare la ripubblicazione diretta di eventi protetti.

Per questo il lavoro successivo conta. [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) estende la regola ai repost che incorporano eventi protetti, chiudendo un bypass semplice in cui l'evento originale restava protetto ma l'evento wrapper no.

## Implementazioni

- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - Ha aggiunto il supporto auth NIP-42 per gli eventi protetti
- [strfry PR #176](https://github.com/hoytech/strfry/pull/176) - Rifiuta i repost che incorporano eventi protetti
- [SNSTR v0.3.3](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.3) - Aggiunge supporto helper collegato alla gestione degli eventi protetti

---

**Fonti primarie:**
- [NIP-70 Specification](https://github.com/nostr-protocol/nips/blob/master/70.md)
- [PR #1030](https://github.com/nostr-protocol/nips/pull/1030) - Ha aggiunto NIP-70 al repository NIPs
- [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) - Rifiuta i repost che incorporano eventi protetti
- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - Implementazione relay per auth NIP-42 ed eventi protetti

**Citato in:**
- [Newsletter #13: Aggiornamenti NIP](/it/newsletters/2026-03-11-newsletter/#aggiornamenti-nip)
- [Newsletter #13: Approfondimento NIP](/it/newsletters/2026-03-11-newsletter/#approfondimento-nip-nip-70-eventi-protetti)

**Vedi anche:**
- [NIP-42: Autenticazione dei client ai relay](/it/topics/nip-42/)
- [NIP-11: Documento informativo del relay](/it/topics/nip-11/)
