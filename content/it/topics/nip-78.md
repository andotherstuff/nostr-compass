---
title: "NIP-78: Dati specifici dell'applicazione"
date: 2026-05-14
draft: false
translationOf: /en/topics/nip-78.md
translationDate: 2026-05-13
categories:
  - NIPs
  - Data Storage
---

NIP-78 definisce un kind di evento standard per consentire alle applicazioni di archiviare dati arbitrari per conto di un utente tramite eventi Nostr, abilitando la sincronizzazione dello stato tra dispositivi senza un server centralizzato.

## Come funziona

Il kind di evento centrale è 30078, un evento sostituibile parametrizzato. Il tag `d` è una stringa identificatrice definita dall'applicazione che delimita lo slot di archiviazione a un'applicazione e uno scopo specifici.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1747180800,
  "kind": 30078,
  "tags": [
    ["d", "myapp-settings"]
  ],
  "content": "{\"theme\":\"dark\",\"fontSize\":14}",
  "sig": "<128-char hex>"
}
```

Un'applicazione pubblica un evento 30078 con un tag `d` univoco (per esempio `tamagostrich-pet-state` o `amethyst-settings`) e qualsiasi contenuto JSON o testo che deve persistere. Poiché 30078 è sostituibile e delimitato dal tag `d`, aggiornare lo stato memorizzato significa pubblicare un nuovo evento con lo stesso tag `d`; il relay conserva solo la versione più recente.

## Sincronizzazione tra dispositivi

Qualsiasi client che conosce la chiave pubblica di un utente e il tag `d` dell'applicazione può recuperare lo stato corrente dal set di relay dell'utente e ricostruirlo su qualsiasi dispositivo. L'utente possiede i dati perché vivono in eventi firmati con la sua coppia di chiavi, archiviati su relay dalla sua lista di relay [NIP-65](/it/topics/nip-65/).

## Dati privati vs. pubblici

Per i dati di applicazione privati, il campo del contenuto può essere crittografato usando [NIP-44](/it/topics/nip-44/) prima della pubblicazione, così il relay memorizza solo testo cifrato che solo il titolare della chiave può decrittare. I dati di applicazione pubblici possono essere archiviati non crittografati affinché altri client possano leggerli e visualizzarli.

## Formato del contenuto

NIP-78 lascia deliberatamente il formato del contenuto aperto; le applicazioni scelgono il proprio schema. La convenzione comune è di prefissare i tag `d` con il nome dell'applicazione per evitare collisioni tra app che utilizzano lo stesso relay.

## Implementazioni

- [Tamagostrich](https://github.com/Negr087/tamagostrich) — sincronizzazione dello stato dell'animale domestico tra dispositivi tramite eventi `tamagostrich-pet-state` kind:30078
- [Wisp](https://github.com/barrydeen/wisp-android) — backup del portafoglio kind:30078 e sincronizzazione delle impostazioni di sicurezza tra dispositivi; abbonamenti outbox uniti in un singolo REQ usando il filtro autore NIP-78
- [NosPress](https://github.com/nostrapps/nospress) — stato di orchestrazione CMS archiviato in eventi NIP-78
- Diverse implementazioni di sincronizzazione delle impostazioni dei client Nostr (Amethyst, altri)

---

**Fonti primarie:**
- [Specifica NIP-78](https://github.com/nostr-protocol/nips/blob/master/78.md)
- [Tamagostrich](https://github.com/Negr087/tamagostrich) — implementazione in produzione

**Menzionato in:**
- [Newsletter #22: NIP-78 Deep Dive](/it/newsletters/2026-05-14-newsletter/#nip-deep-dive-nip-78-app-specific-data)
- [Newsletter #22: Tamagostrich](/it/newsletters/2026-05-14-newsletter/#tamagostrich-launches-a-decentralized-nip-78-tamagotchi-with-sats-rewards)

**Vedi anche:**
- [NIP-51: Liste](/it/topics/nip-51/)
- [NIP-44: Crittografia con versione](/it/topics/nip-44/)
- [NIP-65: Metadati dell'elenco relay](/it/topics/nip-65/)
