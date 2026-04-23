---
title: "NIP-94 : métadonnées de fichier"
date: 2025-12-31
translationOf: /en/topics/nip-94.md
translationDate: 2026-04-22
draft: false
categories:
  - Médias
  - Protocole
---

NIP-94 définit un événement de métadonnées de fichier (kind 1063) pour organiser et classer les fichiers partagés sur Nostr, afin de permettre aux relays de filtrer et d'organiser le contenu efficacement.

## Comment ça fonctionne

NIP-94 utilise le kind `1063` comme événement de métadonnées autonome pour un fichier. Le champ `content` contient une description lisible par un humain, tandis que les tags portent des champs lisibles par machine comme l'URL de téléchargement, le type MIME, les hashes, les dimensions et les indices d'aperçu.

Cette séparation compte parce que l'événement de métadonnées peut être indexé, filtré et réutilisé indépendamment de toute note qui pointe vers le fichier. Un client peut traiter un événement kind `1063` comme la description canonique d'un asset au lieu d'extraire les métadonnées d'un texte libre.

## Tags obligatoires et optionnels

**Tags principaux:**
- `url` - Lien de téléchargement du fichier
- `m` - Type MIME (format en minuscules requis)
- `x` - Hash SHA-256 du fichier

**Tags optionnels:**
- `ox` - Hash SHA-256 du fichier original avant transformations du serveur
- `size` - Taille du fichier en octets
- `dim` - Dimensions (largeur x hauteur) pour images/vidéo
- `magnet` - Magnet URI pour distribution torrent
- `i` - Infohash du torrent
- `blurhash` - Image de substitution pour les aperçus
- `thumb` - URL de vignette
- `image` - URL d'image d'aperçu
- `summary` - Extrait de texte
- `alt` - Description d'accessibilité
- `fallback` - Sources de téléchargement alternatives
- `service` - Protocole de stockage ou type de service, comme NIP-96

Les tags `ox` et `x` sont faciles à négliger, mais utiles en pratique. `ox` identifie le fichier original téléversé, tandis que `x` peut identifier la version transformée qu'un serveur sert réellement. Quand un hébergeur média compresse ou redimensionne les fichiers envoyés, les clients peuvent toujours préserver l'identité du fichier original sans prétendre que le blob transformé est identique octet pour octet.

## Quand l'utiliser

NIP-94 est conçu pour les applications de partage de fichiers, pas pour les clients de contenu social ou long format. Les applications suggérées incluent :

- Relays d'indexation de torrents
- Plateformes de partage de portfolios, similaires à Pinterest
- Distribution de configuration logicielle et de mises à jour
- Bibliothèques et archives de médias

Si les métadonnées du fichier servent seulement à enrichir une URL intégrée dans un autre événement, [NIP-92: Media Attachments](/fr/topics/nip-92/) est plus léger. NIP-94 est le meilleur choix quand le fichier lui-même doit pouvoir être interrogé comme un objet de premier ordre.

## Notes d'interopérabilité

NIP-94 fonctionne avec différents backends de stockage. Un fichier peut être téléversé via [NIP-96: HTTP File Storage](/fr/topics/nip-96/), Blossom ou un autre service, puis être décrit avec la même structure d'événement kind `1063`. C'est pour cela que ce format de métadonnées survit à n'importe quel protocole de téléversement particulier.

---

**Sources principales :**
- [Spécification NIP-94](https://github.com/nostr-protocol/nips/blob/master/94.md)

**Mentionné dans :**
- [Newsletter #3: Récapitulatif de Décembre](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #14 : deep dive NIP](/fr/newsletters/2026-03-18-newsletter/)

**Voir aussi :**
- [NIP-92: Media Attachments](/fr/topics/nip-92/)
- [Blossom](/fr/topics/blossom/)
