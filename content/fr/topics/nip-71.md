---
title: "NIP-71 : Événements vidéo"
date: 2026-01-13
draft: false
categories:
  - Media
  - Protocol
---

NIP-71 définit les kinds d'événements pour le contenu vidéo sur Nostr, permettant le partage de vidéos avec un support approprié des métadonnées. La spécification couvre à la fois les événements vidéo réguliers et les événements vidéo adressables, ces derniers ayant été ajoutés en janvier 2026 pour permettre aux créateurs de mettre à jour les métadonnées vidéo sans republier.

## Kinds d'événements

NIP-71 définit quatre kinds d'événements divisés en deux catégories basées sur le ratio d'aspect et l'adressabilité.

Les événements vidéo réguliers utilisent le kind 21 pour les vidéos horizontales (paysage) et le kind 22 pour les vidéos verticales (portrait/shorts). Ce sont des événements Nostr standard avec un contenu immuable une fois publiés.

Les événements vidéo adressables utilisent le kind 34235 pour les vidéos horizontales et le kind 34236 pour les vidéos verticales. Ce sont des événements remplaçables paramétrés identifiés par la combinaison de pubkey, kind et tag `d`. Publier un nouvel événement avec les mêmes identifiants remplace la version précédente, permettant les mises à jour de métadonnées.

## Structure

Un événement vidéo adressable complet inclut des champs d'identification, des tags de métadonnées et la référence au contenu vidéo.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 34235,
  "tags": [
    ["d", "my-video-2026-01"],
    ["title", "Introduction to Nostr Video"],
    ["summary", "A walkthrough of NIP-71 video events"],
    ["url", "https://example.com/video.mp4"],
    ["thumb", "https://example.com/thumbnail.jpg"],
    ["duration", "300"],
    ["dim", "1920x1080"],
    ["origin", "youtube:dQw4w9WgXcQ"]
  ],
  "content": "Extended description, transcript, or additional notes about the video.",
  "sig": "sig1234..."
}
```

Le tag `d` fournit un identifiant unique parmi vos vidéos de ce kind, vous permettant d'avoir plusieurs vidéos adressables en utilisant différentes valeurs `d`. Les tags `title` et `summary` fournissent le titre de la vidéo et une courte description pour l'affichage dans les clients. Le tag `url` pointe vers le fichier vidéo réel, tandis que `thumb` fournit une image d'aperçu. Le tag `duration` spécifie la durée en secondes, et `dim` spécifie optionnellement les dimensions de la vidéo.

Le tag `origin` permet de suivre la plateforme source lors de l'importation de contenu depuis d'autres services. Cela préserve la provenance lors de la migration de vidéos depuis YouTube, Vimeo ou d'autres plateformes vers l'hébergement Nostr.

Le champ `content` peut contenir une description étendue, une transcription complète ou tout texte supplémentaire associé à la vidéo.

## Pourquoi les événements adressables sont importants

Les événements vidéo réguliers (kinds 21 et 22) sont immuables une fois publiés. Si vous publiez une vidéo et remarquez plus tard une faute de frappe dans le titre, voulez mettre à jour la miniature, ou devez changer l'URL d'hébergement parce que vous avez migré vers un autre service vidéo, vous ne pouvez pas modifier l'événement original. Votre seule option est de publier un nouvel événement avec un nouvel identifiant, ce qui casse toutes les références existantes et perd les métriques d'engagement.

Les événements vidéo adressables résolvent ce problème en rendant l'événement remplaçable. La combinaison de votre pubkey, du kind d'événement et du tag `d` identifie uniquement votre vidéo. Quand vous publiez un nouvel événement avec les mêmes identifiants, les relays remplacent l'ancienne version par la nouvelle. Les clients récupérant votre vidéo obtiennent toujours les dernières métadonnées.

C'est particulièrement précieux pour corriger les erreurs de métadonnées après publication, mettre à jour les miniatures à mesure que vous améliorez votre image de marque, migrer les URL d'hébergement vidéo lors d'un changement de fournisseur, et importer du contenu depuis des plateformes abandonnées comme Vine tout en préservant la provenance via le tag `origin`.

## Implémentations

Les événements vidéo adressables (kinds 34235 et 34236) sont actuellement implémentés dans Amethyst et nostrvine. Les deux clients peuvent créer, afficher et mettre à jour des événements vidéo adressables.

---

**Sources principales :**
- [Spécification NIP-71](https://github.com/nostr-protocol/nips/blob/master/71.md)
- [PR #1669](https://github.com/nostr-protocol/nips/pull/1669) - Mise à jour des événements vidéo adressables

**Mentionné dans :**
- [Newsletter #5 : Mises à jour des NIP](/fr/newsletters/2026-01-13-newsletter/#nip-updates)

**Voir aussi :**
- [NIP-94 : Métadonnées de fichier](/fr/topics/nip-94/)
