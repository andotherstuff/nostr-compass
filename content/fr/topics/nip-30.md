---
title: "NIP-30 : Emoji personnalisés"
date: 2026-03-04
translationOf: /en/topics/nip-30.md
translationDate: 2026-03-04
draft: false
categories:
  - NIP
  - Social
---

NIP-30 définit comment les clients affichent des emoji personnalisés dans les événements Nostr. Les emoji personnalisés sont référencés dans le contenu de l'événement à l'aide de shortcodes (`:shortcode:`) et résolus via des tags `emoji` qui associent chaque shortcode à une URL d'image.

## Fonctionnement

Un événement utilisant des emoji personnalisés inclut des tags `emoji` aux côtés des références de shortcode dans le contenu :

```json
{
  "content": "Hello :gleam: world :nostrich:",
  "tags": [
    ["emoji", "gleam", "https://example.com/gleam.png"],
    ["emoji", "nostrich", "https://example.com/nostrich.png"]
  ]
}
```

Les clients remplacent `:gleam:` et `:nostrich:` dans le contenu rendu par des images en ligne provenant des URLs spécifiées. Les shortcodes doivent être alphanumériques (avec des séparateurs underscore autorisés), et les URLs d'image doivent pointer vers de petites images carrées adaptées à l'affichage en ligne.

## Ensembles d'emoji

Les emoji personnalisés peuvent être organisés en ensembles nommés publiés sous forme d'événements remplaçables paramétrés de kind 30030. Chaque ensemble regroupe des emoji apparentés sous un identifiant de tag `d` :

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

Une mise à jour de mars 2026 ([PR #2247](https://github.com/nostr-protocol/nips/pull/2247)) a ajouté des références optionnelles d'adresse d'ensemble d'emoji dans les tags emoji, permettant aux clients d'ouvrir l'ensemble d'origine pour la navigation ou la mise en signet lorsqu'un utilisateur clique sur un emoji.

## Réactions

Les emoji personnalisés NIP-30 fonctionnent également dans les événements de réaction de kind 7. Une réaction dont le `content` est défini sur un shortcode avec un tag `emoji` correspondant s'affiche comme une réaction emoji personnalisée sur l'événement référencé :

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

**Sources principales :**
- [Spécification NIP-30](https://github.com/nostr-protocol/nips/blob/master/30.md)
- [PR #2247](https://github.com/nostr-protocol/nips/pull/2247) - Adresse d'ensemble d'emoji dans les tags

**Mentionné dans :**
- [Newsletter #12 : NoorNote v0.5.x](/fr/newsletters/2026-03-04-newsletter/#noornote-v05x)
- [Newsletter #12 : Mises à jour des NIP](/fr/newsletters/2026-03-04-newsletter/#mises-à-jour-des-nip)
