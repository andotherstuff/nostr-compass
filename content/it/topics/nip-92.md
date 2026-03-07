---
title: "NIP-92: Media Attachments"
date: 2025-12-31
translationOf: /en/topics/nip-92.md
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---
NIP-92 permette agli utenti di allegare file multimediali agli eventi Nostr includendo URL insieme a tag di metadati inline che descrivono quelle risorse.

## Come funziona

Gli utenti inseriscono URL di contenuti multimediali direttamente nel content dell'evento, per esempio in una text note kind `1`. Un tag `imeta` corrispondente aggiunge poi dettagli leggibili dalle macchine per quell'URL preciso. I client possono usare quei metadati per mostrare anteprime, riservare spazio nel layout ed evitare di dover dedurre le proprietà del file quando la nota è già sullo schermo.

Ogni tag `imeta` dovrebbe corrispondere a un URL nel content dell'evento. I client possono ignorare i tag che non corrispondono, e questo dà alle implementazioni una regola semplice per rifiutare metadati obsoleti o malformati.

## Il tag imeta

Ogni tag `imeta` deve avere un `url` e almeno un altro campo. I campi supportati includono:

- `url` - L'URL del contenuto multimediale (obbligatorio)
- `m` - Il MIME type del file
- `dim` - Le dimensioni dell'immagine (larghezza x altezza)
- `blurhash` - Il blurhash per generare l'anteprima
- `alt` - Il testo alternativo per l'accessibilità
- `x` - L'hash SHA-256 (da NIP-94)
- `fallback` - URL alternativi se quello principale fallisce

Poiché `imeta` può trasportare campi da [NIP-94: File Metadata](/it/topics/nip-94/), i client possono riusare lo stesso MIME type, le stesse dimensioni, lo stesso hash e lo stesso testo per l'accessibilità che già comprendono per eventi autonomi di metadati dei file.

## Perché è importante

Il vantaggio più immediato è un rendering migliore prima del download. Se `dim` è presente, i client possono riservare la giusta quantità di spazio per un'immagine o un video invece di rifare il layout della timeline dopo che il file è stato caricato. Se `blurhash` è presente, possono mostrare prima un'anteprima a basso costo. Se `alt` è presente, l'allegato resta utilizzabile per utenti con screen reader e per utenti ipovedenti.

NIP-92 permette anche ai client di mantenere il post stesso come fonte di verità. L'URL resta in `content`, quindi i client più vecchi mostrano ancora un link semplice, mentre quelli più nuovi possono trasformare la stessa nota in una card multimediale più ricca.

## Note di interoperabilità

NIP-92 è metadato inline, non un formato separato per oggetti multimediali. Se un client ha bisogno di un record di file riusabile con un proprio evento, [NIP-94: File Metadata](/it/topics/nip-94/) è la scelta migliore.

## Esempio

```json
["imeta",
  "url https://example.com/image.jpg",
  "m image/jpeg",
  "dim 1920x1080",
  "blurhash LKO2?U%2Tw=w]~RBVZRi}^Xu%LRj"
]
```

---

**Fonti primarie:**
- [NIP-92 Specification](https://github.com/nostr-protocol/nips/blob/master/92.md)
- [Primal Android PR #718](https://github.com/PrimalHQ/primal-android-app/pull/718) - Un'implementazione concreta lato client per la gestione delle dimensioni e del rapporto d'aspetto

**Menzionato in:**
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #6: News](/en/newsletters/2026-01-21-newsletter/#news)

**Vedi anche:**
- [NIP-94: File Metadata](/it/topics/nip-94/)
