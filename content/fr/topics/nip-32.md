---
title: "NIP-32 : Étiquetage"
date: 2026-01-21
translationOf: /en/topics/nip-32.md
translationDate: 2026-01-28
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-32 définit un standard pour attacher des étiquettes aux événements Nostr, utilisateurs et autres entités. Les étiquettes fournissent des métadonnées structurées que les clients peuvent utiliser pour la catégorisation, les avertissements de contenu, les systèmes de réputation et la modération.

## Fonctionnement

Les étiquettes utilisent des événements kind 1985 avec un tag `L` définissant l'espace de noms de l'étiquette et des tags `l` appliquant des étiquettes spécifiques au sein de cet espace de noms. L'entité étiquetée est référencée via des tags standard comme `e` (événements), `p` (pubkeys) ou `r` (URLs de relais).

```json
{
  "kind": 1985,
  "tags": [
    ["L", "content-warning"],
    ["l", "nsfw", "content-warning"],
    ["e", "<event_id>"]
  ],
  "content": "Contient des images explicites"
}
```

Le système d'espace de noms empêche les collisions d'étiquettes. Une étiquette « spam » dans l'espace de noms « ugc-moderation » a une sémantique différente de « spam » dans l'espace de noms « relay-report ». Cela permet à plusieurs systèmes d'étiquetage de coexister sans interférence.

## Cas d'utilisation

Les systèmes de modération de contenu utilisent les étiquettes pour marquer le spam, le contenu illégal ou les violations de politique. Les systèmes de réputation attachent des scores de confiance ou un statut de vérification aux pubkeys. Les plateformes médias appliquent des avertissements de contenu (NSFW, violence, spoilers). Les opérateurs de relais utilisent les étiquettes pour les appels et la résolution des litiges.

La proposition des Attestations de confiance des relais utilise les étiquettes NIP-32 pour les appels de relais. Lorsque les opérateurs contestent les scores de confiance, ils publient des événements kind 1985 avec `L` = `relay-appeal` et des types d'étiquettes comme « spam », « censorship » ou « score ».

Les implémentations clients varient dans la façon dont elles consomment les étiquettes. Certains clients traitent les étiquettes des utilisateurs suivis comme des recommandations, tandis que d'autres interrogent des services d'étiquetage spécialisés. La conception décentralisée permet aux utilisateurs de choisir quels étiqueteurs ils font confiance.

---

**Sources primaires :**
- [Spécification NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md) - Standard d'étiquetage

**Mentionné dans :**
- [Newsletter #6 : Mises à jour des NIP](/fr/newsletters/2026-01-21-newsletter/#nip-updates)

**Voir aussi :**
- [Attestations de confiance des relais](/fr/topics/trusted-relay-assertions/)
- [NIP-51 : Listes](/fr/topics/nip-51/)
