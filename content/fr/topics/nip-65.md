---
title: "NIP-65 : Métadonnées de liste de relays"
date: 2026-01-13
draft: false
categories:
  - Protocol
  - Discovery
---

NIP-65 définit des événements kind 10002 qui annoncent quels relays un utilisateur préfère pour la lecture et l'écriture. Ces métadonnées aident les autres utilisateurs et clients à localiser votre contenu à travers le réseau de relays distribué, permettant le « modèle outbox » qui distribue la charge et améliore la résistance à la censure.

## Structure

Une liste de relays est un événement remplaçable (kind 10002) contenant des tags `r` pour chaque relay que l'utilisateur souhaite annoncer. L'événement remplace toute liste de relays précédente de la même pubkey.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 10002,
  "tags": [
    ["r", "wss://relay.damus.io", "read"],
    ["r", "wss://nos.lol"],
    ["r", "wss://relay.nostr.band", "write"]
  ],
  "content": "",
  "sig": "sig1234..."
}
```

Chaque tag `r` contient une URL WebSocket de relay et un marqueur optionnel indiquant comment l'utilisateur interagit avec ce relay. Le marqueur `read` signifie que l'utilisateur consomme des événements depuis ce relay, donc les autres devraient y publier pour atteindre l'utilisateur. Le marqueur `write` signifie que l'utilisateur publie vers ce relay, donc les autres devraient s'y abonner pour voir le contenu de l'utilisateur. L'absence de marqueur indique à la fois lecture et écriture.

Le champ `content` est vide pour les événements de liste de relays.

## Le modèle outbox

NIP-65 permet un pattern de distribution de contenu décentralisé appelé « modèle outbox ». Plutôt que tout le monde publie vers et lise depuis les mêmes relays centraux, les utilisateurs publient vers leurs propres relays préférés et les clients découvrent dynamiquement où trouver le contenu de chaque utilisateur.

Quand Alice veut trouver les publications de Bob, son client récupère d'abord l'événement kind 10002 de Bob depuis n'importe quel relay qui l'a. Elle extrait ensuite les relays que Bob a marqués pour l'écriture puisque ce sont ceux où il publie. Son client s'abonne à ces relays pour les événements de Bob. Quand Alice veut envoyer un message direct à Bob, son client cherche plutôt ses relays de lecture et y publie le message.

Les clients suivant le modèle outbox maintiennent des connexions aux relays listés dans les événements NIP-65 de leurs utilisateurs suivis. À mesure qu'ils découvrent de nouveaux comptes, ils se connectent dynamiquement à de nouveaux relays. Les relays qui apparaissent dans les listes de plusieurs utilisateurs suivis sont priorisés puisque s'y connecter dessert une plus grande partie du graphe social de l'utilisateur.

Cette architecture améliore la résistance à la censure car aucun relay unique n'a besoin de stocker ou de servir le contenu de tout le monde. Si un relay tombe en panne ou bloque un utilisateur, son contenu reste disponible sur ses autres relays listés.

## Relation avec les indices de relay

NIP-65 complète les indices de relay trouvés dans les autres NIP. Quand vous taguez quelqu'un avec `["p", "pubkey", "wss://hint.relay"]`, l'indice dit aux clients où chercher cette référence spécifique. NIP-65 fournit la liste autoritaire de relays préférés contrôlée par l'utilisateur, tandis que les indices offrent des raccourcis intégrés dans les événements individuels pour une découverte plus rapide.

## Bonnes pratiques

Gardez votre liste de relays à jour car les entrées obsolètes pointant vers des relays défunts vous rendent plus difficile à trouver. Incluez au moins deux ou trois relays pour la redondance afin que si un relay tombe en panne, votre contenu reste accessible via les autres.

Évitez de lister trop de relays. Quand vous listez dix ou quinze relays, chaque client qui veut récupérer votre contenu doit se connecter à tous, ralentissant leur expérience et augmentant la charge sur le réseau. Une liste ciblée de trois à cinq relays bien choisis vous sert mieux qu'une liste exhaustive qui surcharge tous ceux qui vous suivent.

Mélangez des relays généralistes avec des relays spécialisés que vous utilisez. Par exemple, vous pourriez lister un relay général populaire comme `wss://relay.damus.io`, un relay focalisé sur votre région géographique, et un relay pour une communauté spécifique à laquelle vous participez.

---

**Sources principales :**
- [Spécification NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md)

**Mentionné dans :**
- [Newsletter #5 : Plongée approfondie dans les NIP](/fr/newsletters/2026-01-13-newsletter/#nip-65-relay-list-metadata)

**Voir aussi :**
- [NIP-11 : Information relay](/fr/topics/nip-11/)
