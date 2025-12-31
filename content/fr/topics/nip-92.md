---
title: "NIP-92: Media Attachments"
date: 2025-12-31
translationOf: /en/topics/nip-92.md
translationDate: 2025-12-31
draft: false
categories:
  - Médias
  - Protocole
---

NIP-92 permet aux utilisateurs de joindre des fichiers médias aux événements Nostr en incluant des URLs accompagnées de balises de métadonnées en ligne qui décrivent ces ressources.

## Fonctionnement

1. L'utilisateur place les URLs des médias directement dans le contenu de l'événement (par exemple, dans une note texte kind 1)
2. Une balise `imeta` (métadonnées en ligne) correspondante fournit des détails sur chaque URL
3. Les clients peuvent remplacer les URLs imeta par des aperçus enrichis basés sur les métadonnées
4. Les métadonnées sont généralement générées automatiquement lors du téléchargement des fichiers pendant la composition

## La Balise imeta

Chaque balise `imeta` doit avoir une `url` et au moins un autre champ. Les champs pris en charge incluent :

- `url` - L'URL du média (obligatoire)
- `m` - Type MIME du fichier
- `dim` - Dimensions de l'image (largeur x hauteur)
- `blurhash` - Blurhash pour la génération d'aperçu
- `alt` - Texte alternatif pour l'accessibilité
- `x` - Hash SHA-256 (de NIP-94)
- `fallback` - URLs alternatives si l'URL principale échoue

## Exemple

```json
["imeta",
  "url https://example.com/image.jpg",
  "m image/jpeg",
  "dim 1920x1080",
  "blurhash LKO2?U%2Tw=w]~RBVZRi}^Xu%LRj"
]
```

---

**Sources primaires :**
- [Spécification NIP-92](https://github.com/nostr-protocol/nips/blob/master/92.md)

**Mentionné dans :**
- [Newsletter #3 : Récapitulatif de Décembre](/fr/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Voir aussi :**
- [NIP-94 : Métadonnées de Fichier](/fr/topics/nip-94/)
