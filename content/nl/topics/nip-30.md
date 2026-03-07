---
title: "NIP-30: Aangepaste emoji"
date: 2026-03-04
translationOf: /en/topics/nip-30.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Social
---

NIP-30 definieert hoe clients aangepaste emoji weergeven in Nostr-events. Aangepaste emoji worden in eventcontent aangeduid met shortcodes (`:shortcode:`) en opgelost via `emoji`-tags die elke shortcode koppelen aan een image URL.

## Hoe het werkt

Een event dat aangepaste emoji gebruikt, bevat `emoji`-tags naast de shortcodeverwijzingen in de content:

```json
{
  "content": "Hello :gleam: world :nostrich:",
  "tags": [
    ["emoji", "gleam", "https://example.com/gleam.png"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"]
  ]
}
```

Clients vervangen `:gleam:` en `:nostrich:` in de gerenderde content door inline images van de opgegeven URLs. Shortcodes moeten alfanumeriek zijn, waarbij underscores als scheidingstekens zijn toegestaan, en de image URLs moeten verwijzen naar kleine, vierkante images die geschikt zijn voor inline weergave.

## Emoji-sets

Aangepaste emoji kunnen worden georganiseerd in benoemde sets die worden gepubliceerd als kind 30030 parameterized replaceable events. Elke set groepeert verwante emoji onder een `d`-tag identifier:

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

Een update uit maart 2026 ([PR #2247](https://github.com/nostr-protocol/nips/pull/2247)) voegde optionele emoji-setadresverwijzingen toe aan emoji-tags, zodat clients de oorspronkelijke set kunnen openen om die te bekijken of op te slaan wanneer een gebruiker op een emoji klikt.

## Interop-opmerkingen

Aangepaste emoji zijn een presentatiefunctie, geen transportgarantie. Als een client NIP-30 niet ondersteunt of de image URL niet kan ophalen, moet die nog steeds de ruwe `:shortcode:`-tekst tonen. Daarom zijn leesbare shortcodes belangrijk.

De tag is event-lokaal, tenzij die naar een set verwijst. Als `:fire:` in twee verschillende events wordt hergebruikt, betekent dat niet automatisch een gedeelde globale betekenis, tenzij beide naar dezelfde image of set wijzen. Clients moeten de emojidefinitie eerst vanuit het huidige event oplossen.

## Reacties

Aangepaste emoji uit NIP-30 werken ook in kind 7 reaction events. Een reactie met `content` ingesteld op een shortcode en een bijbehorende `emoji`-tag wordt gerenderd als een aangepaste emojireactie op het event waarnaar wordt verwezen:

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
- [NIP-30-specificatie](https://github.com/nostr-protocol/nips/blob/master/30.md)
- [PR #2247](https://github.com/nostr-protocol/nips/pull/2247) - Emoji-setadres in tags

**Vermeld in:**
- [Newsletter #12: NoorNote v0.5.x](/nl/newsletters/2026-03-04-newsletter/#noornote-v05x)
- [Newsletter #12: NIP Updates](/nl/newsletters/2026-03-04-newsletter/#nip-updates)
