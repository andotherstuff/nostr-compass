---
title: "NIP-62: Vanish Requests"
date: 2026-01-13
translationOf: /en/topics/nip-62/
translationDate: 2026-03-07
draft: false
categories:
  - Privacy
  - Protocol
---
NIP-62 definisce le vanish requests, un meccanismo con cui gli utenti possono chiedere ai relay di eliminare i propri contenuti. Anche se i relay non sono obbligati a onorare queste richieste, il supporto a NIP-62 dà agli utenti più controllo sui dati pubblicati e fornisce un modo standardizzato per segnalare l'intento di eliminazione in tutta la rete.

## Come funziona

Una vanish request è un evento kind 62 firmato dall'utente che vuole rimuovere il proprio contenuto. La richiesta può prendere di mira eventi specifici includendo i loro ID nei tag `e`, oppure può chiedere l'eliminazione di tutti i contenuti di quella pubkey omettendo del tutto i tag `e`.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 62,
  "tags": [
    ["e", "event1234...", "wss://relay.example.com"],
    ["e", "event5678...", "wss://relay.example.com"]
  ],
  "content": "Removing old posts",
  "sig": "sig1234..."
}
```

Il campo `content` contiene facoltativamente una ragione leggibile da esseri umani per la richiesta di eliminazione. I relay hint nei tag `e` indicano ai relay dove sono stati pubblicati gli eventi originali, anche se i relay possono onorare le richieste indipendentemente dal fatto di avere o meno gli eventi specificati.

## Comportamento dei relay

I relay che supportano NIP-62 dovrebbero eliminare gli eventi specificati dal proprio storage e smettere di servirli agli iscritti. La vanish request stessa può essere conservata come record del fatto che è stata chiesta un'eliminazione, il che aiuta a impedire che eventi eliminati vengano reimportati da altri relay.

Quando una vanish request omette tutti i tag `e`, i relay la interpretano come una richiesta di rimuovere tutti gli eventi di quella pubkey. Questa è un'azione più drastica e i relay possono gestirla in modo diverso, per esempio marcando la pubkey come "vanished" e rifiutando di accettare o servire qualsiasi suo evento in futuro.

I relay non sono tenuti a supportare NIP-62. La rete Nostr è decentralizzata e ogni operatore di relay decide le proprie politiche di conservazione dei dati. Gli utenti non dovrebbero presumere che il proprio contenuto venga eliminato ovunque solo perché hanno pubblicato una vanish request.

## Perché è importante

NIP-62 offre a client e operatori di relay un segnale condiviso di eliminazione che va oltre le API di moderazione ad hoc o le dashboard specifiche dei relay. Un utente può pubblicare una richiesta firmata e lasciare a ogni relay la decisione su come elaborarla.

Il limite pratico è l'ambito. Una vanish request incide solo sui relay che la vedono, la supportano e scelgono di onorarla. Non ritira screenshot, database locali, archivi di terze parti o copie ripubblicate che sono già fuori dal controllo del relay.

## Considerazioni sulla privacy

Le vanish requests sono un meccanismo di eliminazione best effort, non una garanzia di privacy. Anche dopo aver pubblicato una vanish request, copie del contenuto possono esistere altrove nella rete, inclusi altri relay che non supportano NIP-62, cache locali sui dispositivi dei client, archivi di terze parti o motori di ricerca e backup.

Anche la richiesta stessa è un evento Nostr firmato, quindi entra a far parte del tuo record pubblico. Chiunque veda la vanish request sa che hai eliminato qualcosa, anche se non può vedere cosa è stato eliminato.

Per contenuti che devono restare privati, valuta l'uso di messaggistica cifrata come [NIP-17](/it/topics/nip-17/) invece di fare affidamento sull'eliminazione a posteriori.

## Note di interoperabilità

NIP-62 integra [NIP-09](/it/topics/nip-09/). NIP-09 è l'evento generale di richiesta di eliminazione usato in tutto Nostr, mentre NIP-62 offre ai relay un segnale più forte orientato alla sparizione che può coprire eventi specifici o l'intero insieme di contenuti di una pubkey. Le implementazioni possono supportare entrambi, e i backend database di rust-nostr ora espongono configurazioni intorno a quel confine di enforcement.

---

**Fonti primarie:**
- [NIP-62 Specification](https://github.com/nostr-protocol/nips/blob/master/62.md)

**Citato in:**
- [Newsletter #5: Notable Code Changes](/en/newsletters/2026-01-13-newsletter/#rust-nostr-library)
- [Newsletter #10: rust-nostr](/en/newsletters/2026-03-04-newsletter/#rust-nostr-nip-62-request-to-vanish)

**Vedi anche:**
- [NIP-09: Event Deletion Request](/it/topics/nip-09/)
- [NIP-17: Private Direct Messages](/it/topics/nip-17/)
