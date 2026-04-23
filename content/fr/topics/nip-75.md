---
title: "NIP-75 : Objectifs de zap"
date: 2026-04-22
translationOf: /en/topics/nip-75.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
---

NIP-75 définit un événement d'objectif de financement vers lequel les utilisateurs peuvent envoyer des zaps. Un objectif déclare un montant cible en millisats et une liste de relays où les reçus de zap pour cet objectif sont totalisés. Tout zap [NIP-57](/fr/topics/nip-57/) qui référence l'événement de l'objectif compte dans sa progression.

## Fonctionnement

Un objectif de zap est un événement `kind:9041`. Le `.content` est une description lisible par un humain. Les tags requis sont `amount` (cible en millisats) et `relays` (liste de relays utilisée pour totaliser les reçus de zap). Les tags optionnels incluent `closed_at` pour arrêter le comptage à un timestamp donné, `image` et `summary`. L'objectif peut aussi inclure un tag `r` ou `a` pointant vers une URL externe ou un événement adressable, et il peut porter plusieurs pubkeys bénéficiaires via des tags de zap-split empruntés à l'annexe G de NIP-57.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1776500000,
  "kind": 9041,
  "tags": [
    ["relays", "wss://alicerelay.example.com", "wss://bobrelay.example.com"],
    ["amount", "210000"],
    ["image", "<image url>"],
    ["summary", "Nostrasia travel expenses"]
  ],
  "content": "Nostrasia travel expenses",
  "sig": "<128-char hex>"
}
```

Les clients attachent un zap à un objectif en incluant un tag `e` pointant vers l'événement de l'objectif à l'intérieur de la demande de zap. La progression de l'objectif est la somme des montants des reçus de zap correspondants sur les relays spécifiés par l'objectif. Quand `closed_at` est défini, les reçus de zap publiés après ce timestamp ne comptent pas.

## Implémentations

- [Amethyst](https://github.com/vitorpamplona/amethyst) affiche désormais des barres de progression d'objectif et des boutons zap en un geste dans les en-têtes de live stream via [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469), qui intègre NIP-75 dans l'écran Live Activities de NIP-53.

---

**Sources principales :**
- [Spécification NIP-75](https://github.com/nostr-protocol/nips/blob/master/75.md)
- [Amethyst PR #2469 : live stream top zappers and goal header](https://github.com/vitorpamplona/amethyst/pull/2469)

**Mentionné dans :**
- [Newsletter #19 : objectifs de zap live stream dans Amethyst](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19 : deep dive NIP-57](/en/newsletters/2026-04-22-newsletter/)

**Voir aussi :**
- [NIP-57 : Zaps](/fr/topics/nip-57/)
- [NIP-53 : Activités en direct](/fr/topics/nip-53/)
