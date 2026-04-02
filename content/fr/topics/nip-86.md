---
title: "NIP-86 : API de gestion des relays"
date: 2026-04-01
translationOf: /en/topics/nip-86.md
translationDate: 2026-04-01
draft: false
categories:
  - Relays
  - Protocol
---

NIP-86 définit une interface JSON-RPC pour la gestion des relays, permettant aux clients autorisés d'envoyer des commandes administratives aux relays via une API standardisée. Les opérateurs de relays peuvent bannir ou autoriser des pubkeys, gérer des listes d'accès et interroger l'état du relay sans outillage spécifique au relay.

## Fonctionnement

L'API de gestion utilise des requêtes de type JSON-RPC sur HTTP à la même URI que le point d'accès WebSocket du relay. Les requêtes utilisent le type de contenu `application/nostr+json+rpc` et s'authentifient avec un événement signé [NIP-98](/fr/topics/nip-98/) (HTTP Auth) dans l'en-tête `Authorization`. Le relay vérifie la pubkey demandante par rapport à sa liste d'administrateurs avant d'exécuter les commandes.

Les méthodes disponibles incluent le bannissement et l'autorisation de pubkeys, le listage des utilisateurs bannis et l'interrogation de la configuration du relay. L'interface standardisée signifie qu'une seule implémentation client peut gérer n'importe quel relay compatible NIP-86.

## Implémentations

- [Amethyst](https://github.com/vitorpamplona/amethyst) - Client Android avec interface de gestion de relays NIP-86 (v1.07.0+)

---

**Sources principales :**
- [Spécification NIP-86](https://github.com/nostr-protocol/nips/blob/master/86.md)
- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - Support NIP-86 côté client
- [PR #2039](https://github.com/vitorpamplona/amethyst/pull/2039) - Dialogue de recherche d'utilisateurs pour la gestion des relays

**Mentionné dans :**
- [Newsletter #16 : Amethyst livre la gestion des relays](/fr/newsletters/2026-04-01-newsletter/#amethyst-livre-les-notes-épinglées-la-gestion-des-relays-et-request-to-vanish)

**Voir aussi :**
- [NIP-11 : Document d'information du relay](/fr/topics/nip-11/)
- [NIP-98 : HTTP Auth](/fr/topics/nip-98/)
- [NIP-42 : Authentification des clients auprès des relays](/fr/topics/nip-42/)
