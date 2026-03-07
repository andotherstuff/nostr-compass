---
title: "NIP-22: Comments"
date: 2026-01-28
translationOf: /en/topics/nip-22.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Social
---

NIP-22 definieert een standaard voor comments op alle adresseerbare Nostr-content, zodat threaded discussies mogelijk zijn op artikelen, video's, kalendergebeurtenissen en andere adresseerbare events.

## Hoe het werkt

Comments gebruiken kind 1111 events met plaintext `content`. Root-scope-tags zijn hoofdletters, en parent-reply-tags zijn kleine letters:

```json
{
  "kind": 1111,
  "tags": [
    ["A", "30023:pubkey:article-id", "wss://relay.example"],
    ["K", "30023"],
    ["P", "<root-pubkey>", "wss://relay.example"],
    ["a", "30023:pubkey:article-id", "wss://relay.example"],
    ["e", "<parent-event-id>", "wss://relay.example", "<parent-pubkey>"],
    ["k", "30023"],
    ["p", "<parent-pubkey>", "wss://relay.example"]
  ],
  "content": "Great article!"
}
```

## Tag-structuur

- **`A` / `E` / `I`** - Root-scope van de discussie: adresseerbaar event, event-id of externe identifier
- **`K`** - Kind of root-scope-type voor dat root-item
- **`P`** - Auteur van het root event, wanneer die bestaat
- **`a` / `e` / `i`** - Directe parent waarop wordt gereageerd
- **`k`** - Kind of scope-type van het parent-item
- **`p`** - Auteur van het parent-item

Voor top-level comments verwijzen root en parent meestal naar hetzelfde doel. Bij replies op comments blijft de root vast staan, terwijl de parent-tags in kleine letters verschuiven naar de specifieke comment waarop wordt gereageerd.

## Interop-opmerkingen

NIP-22 comments zijn geen generieke vervanging voor kind 1 replies. De spec zegt expliciet dat comments niet gebruikt mogen worden om op kind 1 notes te reageren. Voor note-to-note threads moeten clients [NIP-10](/nl/topics/nip-10/) blijven gebruiken.

Een ander nuttig onderscheid is scope. NIP-22 kan discussies verankeren aan niet-note resources via `I`- en `i`-tags, waaronder URL's en andere externe identifiers uit [NIP-73](/nl/topics/nip-73/). Dat geeft clients een standaardmanier om comment threads te koppelen aan webpagina's, podcasts of andere objecten buiten Nostr.

## Gebruikssituaties

- Discussies bij artikelen
- Video-comments
- Discussies bij [NIP-52](/nl/topics/nip-52/) kalendergebeurtenissen
- Overlegpagina's voor wiki's
- Comments op externe resources die via `I`-tags zijn geïdentificeerd

---

**Primaire bronnen:**
- [NIP-22 Specification](https://github.com/nostr-protocol/nips/blob/master/22.md)

**Vermeld in:**
- [Newsletter #7: Notedeck](/en/newsletters/2026-01-28-newsletter/#notedeck)
- [Newsletter #10: AI Agent NIPs Arrive](/en/newsletters/2026-02-18-newsletter/#ai-agent-nips-arrive)
- [Newsletter #12: diVine](/en/newsletters/2026-03-04-newsletter/#divine)

**Zie ook:**
- [NIP-10: Reply Threads](/nl/topics/nip-10/)
- [NIP-52: Calendar Events](/nl/topics/nip-52/)
- [NIP-73: External Content IDs](/nl/topics/nip-73/)
