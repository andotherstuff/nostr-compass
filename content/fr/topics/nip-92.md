---
title: "NIP-92 : Media Attachments"
date: 2025-12-31
translationOf: /en/topics/nip-92.md
translationDate: 2026-03-07
draft: false
categories:
  - Médias
  - Protocole
---

NIP-92 permet aux utilisateurs d'attacher des fichiers média aux événements Nostr en incluant des URLs accompagnées de tags de métadonnées en ligne qui décrivent ces ressources.

## Fonctionnement

Les utilisateurs placent les URLs média directement dans le contenu de l'événement, par exemple dans une note texte kind `1`. Un tag `imeta` correspondant ajoute ensuite des détails lisibles par machine pour cette URL exacte. Les clients peuvent utiliser ces métadonnées pour afficher des aperçus, réserver l'espace de mise en page, et éviter de deviner les propriétés du fichier après que la note est déjà à l'écran.

Chaque tag `imeta` doit correspondre à une URL dans le contenu de l'événement. Les clients peuvent ignorer les tags qui ne correspondent pas, ce qui donne aux implémentations une règle simple pour rejeter les métadonnées périmées ou malformées.

## Le tag imeta

Chaque tag `imeta` doit avoir une `url` et au moins un autre champ. Les champs supportés incluent :

- `url` - L'URL du média (obligatoire)
- `m` - Type MIME du fichier
- `dim` - Dimensions de l'image (largeur x hauteur)
- `blurhash` - Blurhash pour la génération d'aperçu
- `alt` - Texte alternatif pour l'accessibilité
- `x` - Hash SHA-256 (issu de NIP-94)
- `fallback` - URLs alternatives en cas d'échec de l'URL principale

Comme `imeta` peut contenir des champs issus de [NIP-94 : File Metadata](/fr/topics/nip-94/), les clients peuvent réutiliser le même type MIME, les mêmes dimensions, le même hash et le même texte d'accessibilité qu'ils comprendraient déjà pour les événements de métadonnées de fichiers autonomes.

## Pourquoi c'est important

Le bénéfice le plus immédiat est un meilleur rendu avant téléchargement. Si `dim` est présent, les clients peuvent réserver le bon espace pour une image ou une vidéo au lieu de réorganiser la timeline après le chargement du fichier. Si `blurhash` est présent, ils peuvent afficher un aperçu à faible coût d'abord. Si `alt` est présent, la pièce jointe reste utilisable pour les lecteurs d'écran et les utilisateurs malvoyants.

NIP-92 permet aussi aux clients de garder la publication elle-même comme source de vérité. L'URL reste dans `content`, donc les clients plus anciens affichent toujours un lien simple, tandis que les clients plus récents peuvent transformer la même note en une carte média plus riche.

## Notes d'interopérabilité

NIP-92 est un format de métadonnées en ligne, pas un format d'objet média séparé. Si un client a besoin d'un enregistrement de fichier réutilisable avec son propre événement, [NIP-94 : File Metadata](/fr/topics/nip-94/) est plus adapté.

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
- [PR #718 Primal Android](https://github.com/PrimalHQ/primal-android-app/pull/718) - Une implémentation client concrète pour la gestion des dimensions et du ratio d'aspect

**Mentionné dans :**
- [Newsletter #3 : December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #6 : News](/en/newsletters/2026-01-21-newsletter/#news)

**Voir aussi :**
- [NIP-94 : File Metadata](/fr/topics/nip-94/)
