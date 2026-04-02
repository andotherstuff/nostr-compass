---
title: "NIP-70: Event Protetti"
date: 2026-03-11
translationOf: /en/topics/nip-70.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Relay
  - Access Control
---

NIP-70 definisce un modo per gli autori di contrassegnare un event come protetto con il semplice tag `[["-"]]`. Un event protetto può essere accettato solo quando un relay sceglie di supportare quel comportamento e verifica che il publisher autenticato è la stessa pubkey dell'autore dell'event.

## Come Funziona

La regola fondamentale è breve. Se un event contiene il tag `[["-"]]`, un relay dovrebbe rifiutarlo per impostazione predefinita. Un relay che vuole supportare gli event protetti deve prima eseguire il flusso `AUTH` di [NIP-42](/it/topics/nip-42/) e confermare che il client autenticato stia pubblicando il proprio event.

Questo rende NIP-70 una regola di autorità alla pubblicazione, non una regola di cifratura. Il contenuto può essere comunque leggibile. Ciò che cambia è chi può posizionare quell'event su un relay che onora il tag. Questo permette ai relay di supportare feed semi-chiusi e altri contesti in cui gli autori vogliono che un relay rifiuti la ripubblicazione da parte di terzi.

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

## Implicazioni del Flusso AUTH

Gli event protetti sono utili solo quando i relay applicano effettivamente la verifica dell'identità dell'autore al momento della pubblicazione. Ecco perché NIP-70 dipende così direttamente da [NIP-42](/it/topics/nip-42/). Un relay che accetta event `[["-"]]` senza un controllo auth corrispondente tratta il tag come decorazione, non come policy.

## Comportamento e Limiti dei Relay

NIP-70 non promette che il contenuto rimarrà contenuto per sempre. Qualsiasi destinatario può comunque copiare ciò che vede e pubblicare un nuovo event altrove. La specifica dà solo ai relay un modo standard per rispettare l'intento dell'autore e rifiutare la ripubblicazione diretta di event protetti.

Ecco perché il lavoro di follow-up è importante. La [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) estende la regola ai repost che incorporano event protetti, chiudendo un bypass facile in cui l'event originale rimaneva protetto ma l'event wrapper no.

## Implementazioni

- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - Aggiunto supporto auth NIP-42 per event protetti
- [strfry PR #176](https://github.com/hoytech/strfry/pull/176) - Rifiuta repost che incorporano event protetti
- [SNSTR v0.3.3](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.3) - Aggiunge supporto helper legato alla gestione degli event protetti

---

**Fonti primarie:**
- [Specifica NIP-70](https://github.com/nostr-protocol/nips/blob/master/70.md)
- [PR #1030](https://github.com/nostr-protocol/nips/pull/1030) - Aggiunto NIP-70 al repository NIPs
- [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) - Rifiuta repost che incorporano event protetti
- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - Implementazione relay per auth NIP-42 e event protetti

**Menzionato in:**
- [Newsletter #13: Aggiornamenti NIP](/en/newsletters/2026-03-11-newsletter/#nip-updates)
- [Newsletter #13: NIP Deep Dive](/en/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-70-protected-events)

**Vedi anche:**
- [NIP-42: Autenticazione dei Client](/it/topics/nip-42/)
- [NIP-11: Documento Informativo del Relay](/it/topics/nip-11/)
