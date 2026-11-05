---
title: "NIP-31 : Gérer les types d'événements inconnus"
date: 2026-11-04
draft: false
translationOf: /en/topics/nip-31.md
translationDate: 2026-11-05
categories:
  - NIPs
  - Protocol
---

> **Avertissement sur le statut :** la [spécification NIP-31](https://github.com/nostr-protocol/nips/blob/master/31.md) actuelle se déclare elle-même `unrecommended`, car « inutilement alourdie », et sa ligne de statut indique draft, unrecommended et optional. Les relais conservent déjà des événements qui suivent cette convention ; cette page explique donc comment les clients les lisent. Elle ne recommande pas NIP-31 pour de nouveaux protocoles.

NIP-31 définit une étiquette `alt` de premier niveau. Cette étiquette contient un court résumé en texte brut pour les types d'événements personnalisés qui ne sont pas destinés à être lus comme des notes textuelles ordinaires.

## Fonctionnement {#how-it-works}

L'auteur d'un événement de type personnalisé ajoute une étiquette `alt` contenant un libellé lisible par un humain. Les clients conçus autour du kind 1 n'ont pas à s'abonner à tous les types qu'ils ne reconnaissent pas. Leurs utilisateurs peuvent néanmoins tomber sur un tel événement lorsqu'une note y fait référence, et le libellé apporte un peu de contexte même si le client n'implémente pas ce type.

Fragment d'étiquette, et non un événement complet :

```
["alt", "<short plaintext summary>"]
```

Un libellé lisible ne concerne que l'affichage. Il ne permet ni de voter, ni de traiter une requête de portefeuille, ni d'effectuer toute autre action propre au type. Pour une interaction plus riche, la spécification renvoie à [NIP-89 : Gestionnaires d'applications recommandés](/fr/topics/nip-89/).

## Implémentations {#implementations}

Dans la [carte d'événement inconnu de noStrudel au commit 7c68acf](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx), la première étiquette `alt` est épurée de ses espaces et devient le libellé principal, accompagnée d'une ligne facultative `Using <client>`. Une valeur absente ou vide donne `Unknown event (kind ...)`, et jusqu'à trois lignes de contenu s'affichent séparément. Le même composant résout l'étiquette `client` au moyen des modèles de gestionnaires NIP-89. Il affiche un bouton Open lorsqu'une adresse partageable existe, et `Open in <client>` lorsqu'un lien de gestionnaire valide est résolu. L'explication et le renvoi vers l'application sont des contrôles distincts.

Le fichier [UnknownEventDigest.kt d'Amethyst au commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt#L168-L170) privilégie le contenu qu'il classe comme de la prose et se rabat sur `alt`. Son analyseur épure les valeurs de leurs espaces et retient la première `alt` non vide. Par conséquent, un événement dont la première `alt` est vide peut recevoir ici un libellé différent de celui affiché dans noStrudel. Ces deux descriptions reflètent le code source à ces commits. Aucune ne confirme le comportement d'une version publiée.

## Limites {#limits}

- `alt` étant une étiquette, l'identifiant d'événement et la signature définis dans [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) la couvrent. Une signature valide montre que l'auteur a publié le libellé. Elle ne montre pas que le libellé est exact ; un résumé peut donc être trompeur.
- Les étiquettes sont publiques. Une `alt` placée sur un événement au contenu chiffré expose son résumé et peut révéler ce que le contenu dissimule.
- Ces deux propriétés découlent de l'enveloppe d'événement de NIP-01. Le texte de NIP-31 lui-même ne les énonce pas comme des exigences.
- Une étiquette `alt` de premier niveau diffère du champ `alt` de description d'image situé dans `imeta`, et les moteurs de rendu les analysent séparément.

---

**Sources primaires :**
- [Spécification NIP-31](https://github.com/nostr-protocol/nips/blob/master/31.md)
- [noStrudel embedded-unknown.tsx au commit 7c68acf](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx)
- [Amethyst UnknownEventDigest.kt au commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt)

**Mentionné dans :**
- [Nostr Compass #47 : Plongée dans les NIP](/fr/newsletters/2026-11-04-newsletter/#nip-deep-dive-nip-31-and-nip-73)

**Voir aussi :**
- [NIP-89 : Gestionnaires d'applications recommandés](/fr/topics/nip-89/)
- [NIP-73 : Identifiants de contenus externes](/fr/topics/nip-73/)
- [NIP-01 : Description du flux de base du protocole](/fr/topics/nip-01/)
