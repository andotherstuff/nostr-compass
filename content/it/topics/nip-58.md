---
title: "NIP-58: Badge"
date: 2026-01-28
translationOf: /en/topics/nip-58.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Identity
  - Reputation
---

NIP-58 definisce un sistema di badge per Nostr, permettendo agli emittenti di creare badge e assegnarli agli utenti che possono poi mostrarli sui loro profili.

## Come Funziona

### Definizione Badge (Kind 30009)

Gli emittenti creano definizioni di badge come eventi addressable:

```json
{
  "kind": 30009,
  "tags": [
    ["d", "early-adopter"],
    ["name", "Early Adopter"],
    ["description", "Iscritto prima del 2024"],
    ["image", "https://example.com/badge.png"],
    ["thumb", "https://example.com/badge-thumb.png"]
  ]
}
```

### Assegnazione Badge (Kind 8)

Gli emittenti assegnano badge agli utenti:

```json
{
  "kind": 8,
  "tags": [
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["p", "recipient-pubkey"]
  ]
}
```

### Visualizzazione Badge (Kind 30008)

Gli utenti scelgono quali badge mostrare sul loro profilo:

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

## Casi d'Uso

- **Appartenenza a Community**: Dimostrare l'appartenenza a gruppi o community
- **Traguardi**: Riconoscere contributi o milestone
- **Verifica**: Attestazioni di terze parti (dipendente, creatore, ecc.)
- **Controllo Accessi**: Limitare contenuti o funzionalità in base al possesso di badge

## Modello di Fiducia

Il valore del badge dipende interamente dalla reputazione dell'emittente. Chiunque può creare badge, quindi i client dovrebbero:
- Mostrare le informazioni sull'emittente in modo prominente
- Permettere agli utenti di filtrare per emittenti fidati
- Non trattare i badge come autorevoli senza contesto

## Correlati

- [NIP-51](/it/topics/nip-51/) - Liste
- [Web of Trust](/it/topics/web-of-trust/)
