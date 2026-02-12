---
title: "NIP-96 : Stockage de fichiers HTTP"
date: 2026-02-11
translationOf: /en/topics/nip-96.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Media
---

NIP-96 définissait comment les clients Nostr téléversent, téléchargent et gèrent des fichiers sur des serveurs média HTTP. Désormais marqué comme << non recommandé >> en faveur de Blossom, NIP-96 reste pertinent alors que les projets effectuent la transition entre les deux standards média.

## Fonctionnement

Un client découvre les capacités d'un serveur de fichiers en récupérant `/.well-known/nostr/nip96.json`, qui retourne l'URL de l'API, les types de contenu supportés, les limites de taille et les transformations média disponibles.

Pour téléverser, le client envoie un POST `multipart/form-data` vers l'URL de l'API avec un en-tête d'autorisation NIP-98 (un événement Nostr signé prouvant l'identité de celui qui téléverse). Le serveur retourne une structure de métadonnées de fichier NIP-94 contenant l'URL du fichier, les hashes SHA-256, le type MIME et les dimensions.

On télécharge via des requêtes GET vers `<api_url>/<sha256-hash>`, avec des paramètres optionnels pour les transformations côté serveur comme le redimensionnement d'images. La suppression passe par DELETE avec l'authentification NIP-98. Chaque utilisateur publie des événements kind 10096 pour déclarer ses serveurs de téléversement préférés.

## Raisons de la dépréciation

NIP-96 liait les URLs de fichiers à des serveurs spécifiques. Si un serveur tombait en panne, chaque note Nostr référençant ses URLs perdait ses médias. Blossom inverse cette logique en faisant du hash SHA-256 du contenu le seul identifiant canonique. Tout serveur Blossom hébergeant le même fichier le sert au même chemin de hash, rendant le contenu portable entre serveurs par défaut.

Blossom simplifie aussi l'API, avec un simple PUT pour les téléversements, GET pour les téléchargements, et des événements Nostr signés pour l'autorisation. La dépréciation a eu lieu en septembre 2025 via la [PR #2047](https://github.com/nostr-protocol/nips/pull/2047).

## La transition

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
