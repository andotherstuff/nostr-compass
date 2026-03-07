---
title: "NIP-58: Badges"
date: 2026-01-28
translationOf: /en/topics/nip-58.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Identity
  - Reputation
---
NIP-58 definisce un sistema di badge per Nostr. Un evento definisce il badge, un altro lo assegna e un terzo permette al destinatario di scegliere se mostrarlo sul proprio profilo.

## Come funziona

### Definizione del badge (Kind 30009)

Gli issuer creano definizioni di badge come eventi addressable:

```json
{
  "kind": 30009,
  "tags": [
    ["d", "early-adopter"],
    ["name", "Early Adopter"],
    ["description", "Joined before 2024"],
    ["image", "https://example.com/badge.png"],
    ["thumb", "https://example.com/badge-thumb.png"]
  ]
}
```

### Assegnazione del badge (Kind 8)

Gli issuer assegnano badge a uno o più utenti:

```json
{
  "kind": 8,
  "tags": [
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["p", "recipient-pubkey"]
  ]
}
```

### Visualizzazione del badge (Kind 30008)

Gli utenti scelgono quali badge mostrare sul proprio profilo:

```json
{
  "kind": 30008,
  "tags": [
    ["d", "profile_badges"],
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["e", "award-event-id"]
  ]
}
```

In un evento profile badges, i client dovrebbero leggere i tag `a` ed `e` come coppie ordinate. Un tag `a` senza il relativo evento di assegnazione, o un tag `e` senza la relativa definizione del badge, dovrebbe essere ignorato.

## Casi d'uso

- **Appartenenza a una community**: mostra l'appartenenza a gruppi o community
- **Risultati**: riconosce contributi o traguardi
- **Attestazioni**: permette a una terza parte di confermare un ruolo o uno stato
- **Controllo degli accessi**: limita funzionalità o spazi usando badge sostenuti da issuer

## Modello di fiducia

Il valore di un badge dipende interamente dalla reputazione dell'issuer. Chiunque può creare badge, quindi i client dovrebbero:

- mostrare in modo evidente le informazioni sull'issuer
- permettere agli utenti di filtrare per issuer fidati
- non trattare i badge come autorevoli senza contesto

Le assegnazioni di badge sono immutabili e non trasferibili. Questo rende i badge adatti ad attestazioni e riconoscimenti, ma non a credenziali portabili nel senso tokenizzato.

## Note di implementazione

Le definizioni di badge sono eventi addressable, quindi gli issuer possono aggiornare nel tempo grafica o descrizioni del badge senza cambiarne l'identificatore. L'evento di assegnazione è il record durevole che collega un destinatario a quella definizione in un determinato momento.

I client hanno anche margine nella presentazione. La specifica consente esplicitamente di mostrare meno badge di quelli elencati da un utente e di scegliere la dimensione della thumbnail più adatta allo spazio disponibile.

---

**Fonti primarie:**
- [NIP-58 Specification](https://github.com/nostr-protocol/nips/blob/master/58.md)

**Citato in:**
- [Newsletter #7: Five Years of Nostr Januarys](/en/newsletters/2026-01-28-newsletter/)
- [Newsletter #15: Five Years of Nostr Februaries](/en/newsletters/2026-03-04-newsletter/)

**Vedi anche:**
- [NIP-51: Lists](/it/topics/nip-51/)
- [Web of Trust](/it/topics/web-of-trust/)
