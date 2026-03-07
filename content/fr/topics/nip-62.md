---
title: "NIP-62 : Requêtes de disparition"
date: 2026-01-13
translationOf: /en/topics/nip-62.md
translationDate: 2026-03-07
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-62 définit les requêtes de disparition, un mécanisme permettant aux utilisateurs de demander aux relays de supprimer leur contenu. Bien que les relays ne soient pas obligés d'honorer ces requêtes, supporter NIP-62 donne aux utilisateurs plus de contrôle sur leurs données publiées et fournit un moyen standardisé de signaler l'intention de suppression à travers le réseau.

## Fonctionnement

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

Le champ `content` contient optionnellement une raison lisible pour la requête de suppression. Les indices de relay dans les tags `e` indiquent aux relays où les événements originaux ont été publiés, bien que les relays puissent honorer les requêtes qu'ils aient ou non les événements spécifiés.

## Comportement des relays

Les relays qui supportent NIP-62 doivent supprimer les événements spécifiés de leur stockage et cesser de les servir aux abonnés. La requête de disparition elle-même peut être conservée comme enregistrement que la suppression a été demandée, ce qui aide à empêcher les événements supprimés d'être réimportés depuis d'autres relays.

Lorsqu'une requête de disparition omet tous les tags `e`, les relays interprètent cela comme une demande de suppression de tous les événements de cette pubkey. C'est une action plus drastique et les relays peuvent la gérer différemment, par exemple en marquant la pubkey comme "disparue" et en refusant d'accepter ou de servir aucun de ses événements à l'avenir.

Les relays ne sont pas obligés de supporter NIP-62. Le réseau Nostr est décentralisé, et chaque opérateur de relay décide de ses propres politiques de rétention des données. Les utilisateurs ne doivent pas supposer que leur contenu sera supprimé partout simplement parce qu'ils ont publié une requête de disparition.

## Pourquoi c'est important

NIP-62 offre aux clients et aux opérateurs de relay un signal de suppression partagé qui va au-delà des APIs de modération ad hoc ou des tableaux de bord spécifiques aux relays. Un utilisateur peut publier une seule requête signée et laisser chaque relay décider comment la traiter.

La limite pratique est la portée. Une requête de disparition n'affecte que les relays qui la voient, la supportent et choisissent de l'honorer. Elle ne retire pas les captures d'écran, les bases de données locales, les archives tierces ou les copies republieées déjà hors du contrôle du relay.

## Considérations de confidentialité

Les requêtes de disparition sont un mécanisme de suppression au mieux, pas une garantie de confidentialité. Même après avoir publié une requête de disparition, des copies du contenu peuvent exister ailleurs dans le réseau, notamment sur d'autres relays qui ne supportent pas NIP-62, dans les caches locaux des appareils clients, dans les archives tierces ou moteurs de recherche, et dans les sauvegardes.

La requête elle-même est aussi un événement Nostr signé, ce qui signifie qu'elle fait partie de votre historique public. Quiconque voit la requête de disparition sait que vous avez supprimé quelque chose, même s'il ne peut pas voir ce qui a été supprimé.

Pour le contenu qui doit rester privé, envisagez d'utiliser la messagerie chiffrée comme [NIP-17](/fr/topics/nip-17/) plutôt que de compter sur la suppression après coup.

## Notes d'interopérabilité

NIP-62 complète [NIP-09](/fr/topics/nip-09/). NIP-09 est l'événement général de demande de suppression utilisé dans tout Nostr, tandis que NIP-62 fournit aux relays un signal de disparition plus fort qui peut couvrir des événements spécifiques ou l'ensemble du contenu d'une pubkey. Les implémentations peuvent supporter les deux, et les backends de base de données de rust-nostr exposent désormais une configuration autour de cette frontière d'application.

---

**Sources principales :**
- [Spécification NIP-62](https://github.com/nostr-protocol/nips/blob/master/62.md)

**Mentionné dans :**
- [Newsletter #5 : Changements notables de code](/en/newsletters/2026-01-13-newsletter/#rust-nostr-library)
- [Newsletter #10 : rust-nostr](/en/newsletters/2026-03-04-newsletter/#rust-nostr-nip-62-request-to-vanish)

**Voir aussi :**
- [NIP-09 : Demande de suppression d'événement](/fr/topics/nip-09/)
- [NIP-17 : Messages directs privés](/fr/topics/nip-17/)
