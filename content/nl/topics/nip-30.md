---
title: "NIP-30: Aangepaste Emoji"
date: 2026-03-04
translationOf: /en/topics/nip-30.md
translationDate: 2026-03-04
draft: false
categories:
  - NIP
  - Social
---

NIP-30 definieert hoe clients aangepaste emoji weergeven in Nostr-events. Aangepaste emoji worden in de eventinhoud aangeduid met shortcodes (`:shortcode:`) en opgelost via `emoji`-tags die elke shortcode koppelen aan een afbeeldings-URL.

## Hoe Het Werkt

Een event dat aangepaste emoji gebruikt, bevat `emoji`-tags naast de shortcodeverwijzingen in de inhoud:

```json
{
  "content": "Hello :gleam: world :nostrich:",
  "tags": [
    ["emoji", "gleam", "https://example.com/gleam.png"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"]
  ]
}
```

Clients vervangen `:gleam:` en `:nostrich:` in de weergegeven inhoud door inline afbeeldingen van de opgegeven URL's. Shortcodes moeten alfanumeriek zijn (met underscores als scheidingstekens), en de afbeeldings-URL's moeten verwijzen naar kleine, vierkante afbeeldingen die geschikt zijn voor inline weergave.

## Emoji-Sets

Aangepaste emoji kunnen worden georganiseerd in benoemde sets, gepubliceerd als kind 30030 geparametriseerde vervangbare events. Elke set groepeert gerelateerde emoji onder een `d`-tag-identifier:

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

Een update in maart 2026 ([PR #2247](https://github.com/nostr-protocol/nips/pull/2247)) voegde optionele emoji-setadresverwijzingen toe aan emoji-tags, waardoor clients de oorspronkelijke set kunnen openen om te bladeren of als bladwijzer op te slaan wanneer een gebruiker op een emoji klikt.

## Reacties

Aangepaste emoji van NIP-30 werken ook in kind 7 reactie-events. Een reactie met `content` ingesteld op een shortcode en een bijbehorende `emoji`-tag wordt weergegeven als een aangepaste emojireactie op het gerefereerde event:

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

**Primaire bronnen:**
- [NIP-30 Specificatie](https://github.com/nostr-protocol/nips/blob/master/30.md)
- [PR #2247](https://github.com/nostr-protocol/nips/pull/2247) - Emoji-setadres in tags

**Vermeld in:**
- [Nieuwsbrief #12: NoorNote v0.5.x](/nl/newsletters/2026-03-04-newsletter/#noornote-v05x)
- [Nieuwsbrief #12: NIP-Updates](/nl/newsletters/2026-03-04-newsletter/#nip-updates)
