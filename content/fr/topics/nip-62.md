---
title: "NIP-62 : Requêtes de disparition"
date: 2026-01-13
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-62 définit les requêtes de disparition, un mécanisme permettant aux utilisateurs de demander aux relays de supprimer leur contenu. Bien que les relays ne soient pas obligés d'honorer ces requêtes, supporter NIP-62 donne aux utilisateurs plus de contrôle sur leurs données publiées et fournit un moyen standardisé de signaler l'intention de suppression à travers le réseau.

## Comment ça fonctionne

Une requête de disparition est un événement kind 62 signé par l'utilisateur qui souhaite que son contenu soit supprimé. La requête peut cibler des événements spécifiques en incluant leurs identifiants dans les tags `e`, ou elle peut demander la suppression de tout le contenu de cette pubkey en omettant complètement les tags `e`.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 62,
  "tags": [
    ["e", "event1234...", "wss://relay.example.com"],
    ["e", "event5678...", "wss://relay.example.com"]
  ],
  "content": "Removing old posts",
  "sig": "sig1234..."
}
```

Le champ `content` contient optionnellement une raison lisible par l'humain pour la requête de suppression. Les indices de relay dans les tags `e` indiquent aux relays où les événements originaux ont été publiés, bien que les relays puissent honorer les requêtes qu'ils aient ou non les événements spécifiés.

## Comportement des relays

Les relays qui supportent NIP-62 devraient supprimer les événements spécifiés de leur stockage et cesser de les servir aux abonnés. La requête de disparition elle-même peut être conservée comme un enregistrement que la suppression a été demandée, ce qui aide à empêcher les événements supprimés d'être réimportés depuis d'autres relays.

Lorsqu'une requête de disparition omet tous les tags `e`, les relays interprètent cela comme une demande de suppression de tous les événements de cette pubkey. C'est une action plus drastique et les relays peuvent la gérer différemment, par exemple en marquant la pubkey comme « disparue » et en refusant d'accepter ou de servir aucun de ses événements à l'avenir.

Les relays ne sont pas obligés de supporter NIP-62. Le réseau Nostr est décentralisé, et chaque opérateur de relay décide de ses propres politiques de rétention des données. Les utilisateurs ne devraient pas supposer que leur contenu sera supprimé partout simplement parce qu'ils ont publié une requête de disparition.

## Considérations de confidentialité

Les requêtes de disparition sont un mécanisme de suppression au mieux, pas une garantie de confidentialité. Même après avoir publié une requête de disparition, des copies du contenu peuvent exister ailleurs dans le réseau, notamment sur d'autres relays qui ne supportent pas NIP-62, dans les caches locaux des appareils clients, dans les archives tierces ou moteurs de recherche, et dans les sauvegardes.

La requête elle-même est également un événement Nostr signé, ce qui signifie qu'elle fait partie de votre historique public. Quiconque voit la requête de disparition sait que vous avez supprimé quelque chose, même s'il ne peut pas voir ce qui a été supprimé.

Pour le contenu qui doit rester privé, envisagez d'utiliser la messagerie chiffrée comme [NIP-17](/fr/topics/nip-17/) plutôt que de compter sur la suppression après coup.

---

**Sources principales :**
- [Spécification NIP-62](https://github.com/nostr-protocol/nips/blob/master/62.md)

**Mentionné dans :**
- [Newsletter #5 : Changements notables de code](/fr/newsletters/2026-01-13-newsletter/#rust-nostr-library)
