---
title: "NIP-30: Emoji Personalizzate"
date: 2026-03-04
translationOf: /en/topics/nip-30.md
translationDate: 2026-03-04
draft: false
categories:
  - NIP
  - Social
---

NIP-30 definisce come i client visualizzano le emoji personalizzate negli event Nostr. Le emoji personalizzate vengono referenziate nel contenuto degli event tramite shortcode (`:shortcode:`) e risolte attraverso tag `emoji` che mappano ogni shortcode a un URL immagine.

## Come Funziona

Un event che usa emoji personalizzate include tag `emoji` insieme ai riferimenti shortcode nel contenuto:

```json
{
  "content": "Hello :gleam: world :nostrich:",
  "tags": [
    ["emoji", "gleam", "https://example.com/gleam.png"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"]
  ]
}
```

I client sostituiscono `:gleam:` e `:nostrich:` nel contenuto renderizzato con immagini inline dagli URL specificati. Gli shortcode devono essere alfanumerici (con separatori underscore consentiti), e gli URL delle immagini dovrebbero puntare a immagini piccole e quadrate adatte alla visualizzazione inline.

## Set di Emoji

Le emoji personalizzate possono essere organizzate in set denominati pubblicati come event sostituibili parametrizzati di kind 30030. Ogni set raggruppa emoji correlate sotto un identificatore nel tag `d`:

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

Un aggiornamento di marzo 2026 ([PR #2247](https://github.com/nostr-protocol/nips/pull/2247)) ha aggiunto riferimenti opzionali all'indirizzo del set di emoji nei tag emoji, permettendo ai client di aprire il set di origine per la navigazione o l'aggiunta ai segnalibri quando un utente clicca su un'emoji.

## Reazioni

Le emoji personalizzate NIP-30 funzionano anche negli event di reazione di kind 7. Una reazione con `content` impostato su uno shortcode e un tag `emoji` corrispondente viene renderizzata come reazione emoji personalizzata sull'event referenziato:

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

**Menzionato in:**
- [Newsletter #12: NoorNote v0.5.x](/it/newsletters/2026-03-04-newsletter/#noornote-v05x)
- [Newsletter #12: Aggiornamenti NIP](/it/newsletters/2026-03-04-newsletter/#aggiornamenti-nip)
