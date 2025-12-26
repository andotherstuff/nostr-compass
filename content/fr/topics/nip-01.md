---
title: "NIP-01 : Protocole de base"
date: 2025-12-17
draft: false
categories:
  - Protocol
---

NIP-01 définit le protocole fondamental de Nostr, établissant les structures de données et les modèles de communication sur lesquels tous les autres NIPs se construisent.

## Événements

Les événements sont le seul type d'objet dans Nostr. Chaque donnée, d'une mise à jour de profil à un post textuel en passant par une réaction, est représentée comme un événement avec cette structure :

- **id** : Hash SHA256 de l'événement sérialisé (identifiant unique)
- **pubkey** : La clé publique du créateur (hex 32 octets, secp256k1)
- **created_at** : Horodatage Unix
- **kind** : Entier catégorisant le type d'événement
- **tags** : Tableau de tableaux pour les métadonnées
- **content** : La charge utile (l'interprétation dépend du kind)
- **sig** : Signature Schnorr prouvant l'authenticité

## Kinds

Les kinds déterminent comment les relais stockent et gèrent les événements :

- **Événements réguliers** (1, 2, 4-44, 1000-9999) : Stockés normalement, toutes les versions conservées
- **Événements remplaçables** (0, 3, 10000-19999) : Seul le dernier par clé publique est conservé
- **Événements éphémères** (20000-29999) : Non stockés, juste transmis aux abonnés
- **Événements adressables** (30000-39999) : Dernier par combinaison clé publique + kind + tag `d`

Les kinds de base incluent : 0 (métadonnées utilisateur), 1 (note textuelle), 3 (liste d'abonnements).

## Communication Client-Relais

Les clients communiquent avec les relais via des connexions WebSocket utilisant des tableaux JSON :

**Client vers relais :**
- `["EVENT", <event>]` - Publier un événement
- `["REQ", <sub-id>, <filter>, ...]` - S'abonner aux événements
- `["CLOSE", <sub-id>]` - Terminer un abonnement

**Relais vers client :**
- `["EVENT", <sub-id>, <event>]` - Livrer un événement correspondant
- `["EOSE", <sub-id>]` - Fin des événements stockés (maintenant en streaming live)
- `["OK", <event-id>, <true|false>, <message>]` - Accusé de réception d'acceptation/rejet
- `["NOTICE", <message>]` - Message lisible par l'humain

## Filtres

Les filtres spécifient quels événements récupérer, avec des champs incluant : `ids`, `authors`, `kinds`, `#e`/`#p`/`#t` (valeurs de tags), `since`/`until`, et `limit`. Les conditions dans un filtre utilisent la logique AND ; plusieurs filtres dans un `REQ` se combinent avec la logique OR.

---

**Sources principales :**
- [Spécification NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Mentionné dans :**
- [Newsletter #1 : Analyse approfondie NIP](/fr/newsletters/2025-12-17-newsletter/#nip-deep-dive-nip-01-and-nip-19)

**Voir aussi :**
- [NIP-19 : Entités encodées en Bech32](/fr/topics/nip-19/)
- [Registre des Kinds](/fr/kind-registry/)

