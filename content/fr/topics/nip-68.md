---
title: "NIP-68: Flux axés sur les images"
date: 2026-07-29
translationOf: /en/topics/nip-68.md
translationDate: 2026-07-29
draft: false
categories:
  - Media
  - Protocol
---

NIP-68 définit des events d'images adressables. Il fournit aux clients un moyen portable de publier des métadonnées d'image, des légendes, des libellés et des références à des fichiers d'image, tout en séparant l'event lui-même du stockage des blobs.

## Fonctionnement

Une image utilise le kind `20` et comporte un tag `title` ainsi qu'une description dans `content`. Le tag `imeta` décrit chaque image au moyen de champs tels que `url`, `m` pour le type MIME, `dim` pour les dimensions, le texte `alt` et un hash SHA-256 facultatif. Plusieurs tags `imeta` permettent à un event de représenter un ensemble d'images.

L'event peut inclure des tags `p` pour les personnes représentées ou créditées, des tags `t` pour les sujets ainsi que des références Nostr ordinaires. Il peut aussi inclure des tags de type de média, de hash, de localisation et d'avertissement sur le contenu, afin que les clients puissent filtrer et afficher les publications d'images de manière cohérente.

NIP-68 n'impose aucun système de stockage sous-jacent. Les clients peuvent référencer des URL HTTPS ordinaires ou un système adressé par le contenu tel que Blossom, à condition de publier suffisamment de métadonnées `imeta` pour qu'un autre client puisse afficher et vérifier l'image.

## Implémentations

[NoorNote 1.3.0](https://github.com/77elements/noornote/releases/tag/v1.3.0) a ajouté le balisage d'images NIP-68 en complément des fonctionnalités de ce client axées sur les images.

---

**Sources principales :**
- [Spécification NIP-68](https://github.com/nostr-protocol/nips/blob/master/68.md)
- [NoorNote 1.3.0](https://github.com/77elements/noornote/releases/tag/v1.3.0)

**Mentionné dans :**
- [Newsletter #33 : Versions publiées avec un tag](/fr/newsletters/2026-07-29-newsletter/#tagged-releases)

**Voir aussi :**
- [Protocole Blossom](/fr/topics/blossom/)
- [NIP-94 : Métadonnées de fichiers](/fr/topics/nip-94/)
