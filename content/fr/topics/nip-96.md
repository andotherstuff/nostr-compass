---
title: "NIP-96 : Stockage de fichiers HTTP"
date: 2026-02-11
translationOf: /en/topics/nip-96.md
translationDate: 2026-03-07
draft: false
categories:
  - NIPs
  - Médias
---

NIP-96 définit comment les clients Nostr téléversent, téléchargent et gèrent des fichiers sur des serveurs média HTTP. Il est désormais marqué comme "unrecommended" au profit de Blossom, mais il reste important parce que des serveurs et des clients existants continuent de le prendre en charge pendant la transition.

## Fonctionnement

Un client découvre les capacités d'un serveur de fichiers en récupérant `/.well-known/nostr/nip96.json`. Ce document annonce l'URL de l'API de téléversement, une éventuelle URL de téléchargement, les types de contenu pris en charge, les limites de taille et indique si le serveur gère les transformations média ou l'hébergement délégué.

Pour téléverser, le client envoie un POST `multipart/form-data` vers l'URL de l'API avec un en-tête d'autorisation [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md). Le serveur répond avec un objet de métadonnées au format NIP-94 qui inclut l'URL du fichier ainsi que des tags comme `ox` pour le hash original et, quand c'est pertinent, `x` pour le fichier transformé qui sera réellement servi.

Les téléchargements utilisent `GET <api_url>/<sha256-hash>`, avec des paramètres de requête optionnels comme la largeur d'une image. La suppression utilise `DELETE` avec l'authentification NIP-98. Les utilisateurs publient des événements kind `10096` pour déclarer leurs serveurs de téléversement préférés.

## Détails du modèle de données

Un détail utile est que NIP-96 identifie les fichiers par le hash du fichier original, même quand le serveur transforme le fichier téléversé. Cela permet à un client de supprimer ou de retélécharger l'asset à partir du même identifiant stable, tout en récupérant des vignettes générées par le serveur ou des variantes recompressées quand elles existent.

Le document well-known prend aussi en charge `delegated_to_url`, qui permet à un relay de diriger les clients vers un serveur de stockage HTTP séparé. Cela évitait au logiciel de relay d'avoir à implémenter lui-même toute l'API média.

## Pourquoi il a été déprécié

NIP-96 liait les URLs de fichiers à des serveurs spécifiques. Si un serveur tombait en panne, chaque note Nostr référençant ses URLs perdait ses médias. Blossom inverse cette logique en faisant du hash SHA-256 du contenu le seul identifiant canonique. Tout serveur Blossom hébergeant le même fichier le sert au même chemin de hash, rendant le contenu portable entre serveurs par défaut.

Blossom simplifie aussi l'API : PUT simple pour les téléversements, GET pour les téléchargements et événements Nostr signés, pas d'en-têtes HTTP, pour l'autorisation. La dépréciation a eu lieu en septembre 2025 via la [PR #2047](https://github.com/nostr-protocol/nips/pull/2047).

## Notes d'interopérabilité

Des serveurs comme nostr.build et void.cat supportaient NIP-96 et ont ajouté ou migré vers des points d'accès Blossom. Côté client, Angor v0.2.5 a ajouté la configuration de serveur NIP-96 tandis que ZSP v0.3.1 téléverse exclusivement vers des serveurs Blossom. La coexistence continuera jusqu'à ce que les implémentations NIP-96 restantes achèvent leur migration.

Les événements de préférence de serveur kind 10096 restent utiles pour la sélection de serveur Blossom. Quant aux métadonnées de fichier NIP-94 (événements kind 1063), elles décrivent les propriétés des fichiers quel que soit le protocole de téléversement qui les a créées.

---

**Sources principales :**
- [NIP-96: HTTP File Storage](https://github.com/nostr-protocol/nips/blob/master/96.md)
- [PR #2047: Mark NIP-96 as Unrecommended](https://github.com/nostr-protocol/nips/pull/2047)

**Mentionné dans :**
- [Newsletter #9 : Approfondissement NIP](/fr/newsletters/2026-02-11-newsletter/#approfondissement-nip--nip-96-stockage-de-fichiers-http-et-la-transition-vers-blossom)

**Voir aussi :**
- [Protocole Blossom](/fr/topics/blossom/)
- [NIP-94 : Métadonnées de fichier](/fr/topics/nip-94/)
