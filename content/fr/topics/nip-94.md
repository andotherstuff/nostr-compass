---
title: "NIP-94: File Metadata"
date: 2025-12-31
translationOf: /en/topics/nip-94.md
translationDate: 2025-12-31
draft: false
categories:
  - Médias
  - Protocole
---

NIP-94 définit un événement de métadonnées de fichier (kind 1063) pour organiser et classifier les fichiers partagés sur Nostr, permettant aux relays de filtrer et organiser le contenu efficacement.

## Comment Ça Fonctionne

1. L'utilisateur téléverse un fichier vers un service d'hébergement
2. Un événement kind 1063 est publié avec des métadonnées sur le fichier
3. Le contenu de l'événement contient une description lisible par l'humain
4. Des tags structurés fournissent des métadonnées lisibles par machine
5. Des clients spécialisés peuvent organiser et afficher les fichiers systématiquement

## Tags Requis et Optionnels

**Tags principaux:**
- `url` - Lien de téléchargement du fichier
- `m` - MIME type (format en minuscules requis)
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

## Cas d'Utilisation

NIP-94 est conçu pour les applications de partage de fichiers plutôt que pour les clients de contenu social ou de format long. Les applications suggérées incluent:

- Relays d'indexation de torrents
- Plateformes de partage de portfolios (similaire à Pinterest)
- Distribution de configuration et mises à jour logicielles
- Bibliothèques et archives de médias

---

**Sources principales:**
- [Spécification NIP-94](https://github.com/nostr-protocol/nips/blob/master/94.md)

**Mentionné dans:**
- [Newsletter #3: Récapitulatif de Décembre](/fr/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Voir aussi:**
- [NIP-92: Pièces Jointes Médias](/fr/topics/nip-92/)
- [Blossom](/fr/topics/blossom/)
