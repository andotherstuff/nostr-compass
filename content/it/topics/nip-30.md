---
title: "NIP-30: Emoji personalizzati"
date: 2026-03-04
translationOf: /en/topics/nip-30.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Social
---
NIP-30 definisce come i client mostrano emoji personalizzati negli eventi Nostr. Gli emoji personalizzati vengono referenziati nel contenuto dell'evento usando shortcode (`:shortcode:`) e risolti tramite tag `emoji` che associano ogni shortcode a un image URL.

## Come funziona

Un evento che usa emoji personalizzati include tag `emoji` accanto ai riferimenti shortcode nel contenuto:

```json
{
  "content": "Hello :gleam: world :nostrich:",
  "tags": [
    ["emoji", "gleam", "https://example.com/gleam.png"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"]
  ]
}
```

I client sostituiscono `:gleam:` e `:nostrich:` nel contenuto renderizzato con immagini inline dagli URL specificati. Gli shortcode devono essere alfanumerici, con separatori underscore consentiti, e gli image URL dovrebbero puntare a immagini piccole e quadrate adatte alla visualizzazione inline.

## Set di emoji

Gli emoji personalizzati possono essere organizzati in set con nome pubblicati come eventi parameterized replaceable kind 30030. Ogni set raggruppa emoji collegati sotto un identificatore tag `d`:

```json
{
  "kind": 30030,
  "tags": [
    ["d", "nostr-animals"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"],
    ["emoji", "nostrcat", "https://example.com/nostrcat.png"]
  ]
}
```

Un aggiornamento di marzo 2026 ([PR #2247](https://github.com/nostr-protocol/nips/pull/2247)) ha aggiunto riferimenti opzionali all'indirizzo del set di emoji nei tag `emoji`, permettendo ai client di aprire il set di origine per esplorazione o bookmarking quando un utente clicca un emoji.

## Note di interoperabilità

Gli emoji personalizzati sono una funzione di presentazione, non una garanzia di trasporto. Se un client non capisce NIP-30 o non riesce a recuperare l'image URL, dovrebbe comunque mostrare il testo grezzo `:shortcode:`. Questo fallback è il motivo per cui shortcode leggibili contano.

Il tag è locale all'evento a meno che non faccia riferimento a un set. Riutilizzare `:fire:` in due eventi diversi non implica un significato globale condiviso a meno che entrambi puntino alla stessa immagine o allo stesso set. I client dovrebbero risolvere prima la definizione dell'emoji dall'evento corrente.

## Reazioni

Gli emoji personalizzati NIP-30 funzionano anche negli eventi reaction kind 7. Una reaction con `content` impostato su uno shortcode e un tag `emoji` corrispondente viene renderizzata come reaction con emoji personalizzato sull'evento referenziato:

```json
{
  "kind": 7,
  "content": ":fire:",
  "tags": [
    ["emoji", "fire", "https://example.com/fire.gif"],
    ["e", "<event-id>"]
  ]
}
```

---

**Fonti primarie:**
- [Specifica NIP-30](https://github.com/nostr-protocol/nips/blob/master/30.md)
- [PR #2247](https://github.com/nostr-protocol/nips/pull/2247) - Indirizzo del set di emoji nei tag

**Citato in:**
- [Newsletter #12: NoorNote v0.5.x](/en/newsletters/2026-03-04-newsletter/#noornote-v05x)
- [Newsletter #12: NIP Updates](/en/newsletters/2026-03-04-newsletter/#nip-updates)
