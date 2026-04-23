---
title: "NIP-01 : Protocole de base"
date: 2025-12-17
translationOf: /en/topics/nip-01.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
---

NIP-01 définit le modèle d'événements de base et le protocole de relais sur lesquels le reste de Nostr se construit. Si un client, un relais ou une bibliothèque parle Nostr, c'est ici que tout commence.

## Fonctionnement

Les événements sont le seul type d'objet dans Nostr. Profils, notes, réactions, listes de relais et de nombreuses charges utiles spécifiques aux applications utilisent tous la même enveloppe à sept champs :

- **id** : hash SHA256 de l'événement sérialisé (identifiant unique)
- **pubkey** : la clé publique du créateur (hex 32 octets, secp256k1)
- **created_at** : horodatage Unix
- **kind** : entier catégorisant le type d'événement
- **tags** : tableau de tableaux pour les métadonnées
- **content** : la charge utile (l'interprétation dépend du kind)
- **sig** : signature Schnorr prouvant l'authenticité

L'`id` de l'événement est le hash SHA256 des données sérialisées de l'événement, pas un identifiant arbitraire. C'est important en pratique : changer n'importe quel champ, y compris l'ordre des tags ou l'horodatage, produit un événement différent et nécessite une nouvelle signature.

## Kinds

Les kinds déterminent comment les relais stockent et gèrent les événements :

- **Événements réguliers** (1, 2, 4-44, 1000-9999) : stockés normalement, toutes les versions conservées
- **Événements remplaçables** (0, 3, 10000-19999) : seul le dernier par pubkey est conservé
- **Événements éphémères** (20000-29999) : non stockés, juste transmis aux abonnés
- **Événements adressables** (30000-39999) : dernier par combinaison pubkey + kind + tag `d`

Les kinds de base incluent : 0 (métadonnées utilisateur), 1 (note textuelle) et 3 (liste d'abonnements).

## Communication client-relais

Les clients communiquent avec les relais via des connexions WebSocket utilisant des tableaux JSON :

**Client vers relais :**
- `["EVENT", <event>]` - publier un événement
- `["REQ", <sub-id>, <filter>, ...]` - s'abonner aux événements
- `["CLOSE", <sub-id>]` - terminer un abonnement

**Relais vers client :**
- `["EVENT", <sub-id>, <event>]` - livrer un événement correspondant
- `["EOSE", <sub-id>]` - fin des événements stockés (streaming en direct désormais)
- `["OK", <event-id>, <true|false>, <message>]` - accusé d'acceptation/rejet
- `["NOTICE", <message>]` - message lisible par un humain

En pratique, la plupart des NIPs de niveau supérieur ne modifient pas la couche de transport. Ils définissent de nouveaux kinds d'événements, des tags ou des règles d'interprétation tout en utilisant les mêmes messages `EVENT`, `REQ` et `CLOSE` de NIP-01.

## Filtres

Les filtres spécifient quels événements récupérer, avec des champs incluant `ids`, `authors`, `kinds`, `#e`/`#p`/`#t`, `since`, `until` et `limit`. Les conditions dans un filtre utilisent la logique AND. Plusieurs filtres dans un `REQ` utilisent la logique OR.

## Notes d'interopérabilité

Deux détails causent de nombreux bugs d'implémentation. D'abord, les clients devraient traiter les réponses des relais comme éventuellement cohérentes, pas globalement ordonnées, car différents relais peuvent retourner des sous-ensembles différents de l'historique. Ensuite, les événements remplaçables et adressables signifient que "le plus récent" fait partie du modèle protocolaire, donc les clients ont besoin de règles déterministes pour choisir l'événement valide le plus récent lorsque plusieurs relais sont en désaccord.

---

**Sources principales :**
- [Spécification NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Mentionné dans :**
- [Newsletter #1 : Analyse approfondie NIP](/fr/newsletters/2025-12-17-newsletter/)
- [Newsletter #19 : proposition NIP-67 sur la complétude EOSE](/en/newsletters/2026-04-22-newsletter/)

**Voir aussi :**
- [NIP-19 : Entités encodées en Bech32](/fr/topics/nip-19/)
- [Registre des kinds](/fr/kind-registry/)
