---
title: "NIP-27 (Références de notes textuelles)"
date: 2026-02-04
description: "NIP-27 définit comment référencer des profils, notes et autres entités dans le contenu des notes en utilisant le schéma URI nostr:."
---

NIP-27 spécifie comment intégrer des références à des entités Nostr dans le contenu des notes textuelles. Les références utilisent le schéma URI `nostr:` suivi d'un identifiant encodé en bech32 (npub, note, nevent, nprofile, naddr).

## Fonctionnement

Lors de la composition d'une note qui mentionne un autre utilisateur ou référence un autre événement, la référence est intégrée directement dans le contenu :

```
Consultez ce post de nostr:npub1... à propos de nostr:note1...
```

Les clients analysent ces références et les affichent de manière appropriée, généralement sous forme de liens cliquables ou de cartes de profil intégrées. Les entités référencées sont également ajoutées aux tags de l'événement à des fins d'indexation et de notification.

Le NIP couvre également l'analyse des hashtags. Les tags préfixés par `#` sont extraits et ajoutés aux tags `t` de l'événement pour la recherche.

## Types de références

- `nostr:npub1...` - Référence à un profil utilisateur
- `nostr:note1...` - Référence à un événement note spécifique
- `nostr:nevent1...` - Référence à un événement avec indices de relais
- `nostr:nprofile1...` - Référence à un profil avec indices de relais
- `nostr:naddr1...` - Référence à un événement adressable

## Implémentations

Tous les clients Nostr majeurs implémentent NIP-27 :
- Les analyseurs de texte extraient les références lors de la composition
- Les moteurs de rendu affichent les références comme éléments interactifs
- Les systèmes de notification utilisent les tags associés

## Sources principales

- [Spécification NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md)
- [NIP-19 (Entités encodées Bech32)](/fr/topics/nip-19/) - Définit les formats d'encodage utilisés dans les références

## Mentionné dans

- [Newsletter #8 (2026-02-04)](/fr/newsletters/2026-02-04-newsletter/) - Correction nostr-tools pour l'analyse des hashtags après les sauts de ligne
