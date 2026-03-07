---
title: "NIP-27 (Références de notes textuelles)"
date: 2026-02-04
description: "NIP-27 définit comment référencer des profils, notes et autres entités dans le contenu des notes en utilisant le schéma URI nostr:."
translationOf: /en/topics/nip-27.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Social
---

NIP-27 spécifie comment intégrer des références à des entités Nostr dans le contenu des notes textuelles. Les références utilisent le schéma URI `nostr:` suivi d'un identifiant encodé en bech32 (npub, note, nevent, nprofile, naddr).

## Fonctionnement

Lors de la composition d'une note qui mentionne un autre utilisateur ou référence un autre événement, la référence est intégrée directement dans le contenu :

```
Check out this post by nostr:npub1... about nostr:note1...
```

Les clients analysent ces références et les affichent de manière appropriée, généralement sous forme de liens cliquables ou de cartes de profil intégrées. Les entités référencées peuvent aussi être dupliquées dans les tags de l'événement pour l'indexation ou les notifications, mais la spécification laisse cela optionnel.

Le NIP couvre également l'analyse des hashtags. Les tags préfixés par `#` sont extraits et ajoutés aux tags `t` de l'événement pour la recherche.

## Types de références

- `nostr:npub1...` - Référence à un profil utilisateur
- `nostr:note1...` - Référence à un événement note spécifique
- `nostr:nevent1...` - Référence à un événement avec indices de relais
- `nostr:nprofile1...` - Référence à un profil avec indices de relais
- `nostr:naddr1...` - Référence à un événement adressable

## Pourquoi c'est important

NIP-27 sépare ce que les gens lisent de ce que les clients stockent. Un utilisateur peut taper `@name` dans un éditeur riche, mais l'événement publié peut contenir une référence `nostr:nprofile...` stable dans le `content`. Cela rend la référence portable entre les clients sans dépendre de la syntaxe de mention d'une application.

Un autre avantage pratique est la résilience. Un `nostr:nevent...` ou `nostr:naddr...` brut intégré dans le texte porte assez d'informations pour qu'un autre client puisse reconstruire la cible même s'il n'a jamais vu le rendu local original.

## Notes d'interopérabilité

- Utilisez la forme [NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) dans le contenu : `nostr:<bech32-id>`
- Ajoutez des tags `p` ou `q` uniquement quand votre client veut des notifications de mention ou un indexage d'événement plus fort
- Ne présumez pas que chaque référence intégrée doit devenir une relation de réponse. La spécification laisse ce choix au client

---

**Sources principales :**
- [Spécification NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md)
- [NIP-19 (Entités encodées Bech32)](/fr/topics/nip-19/) - Définit les formats d'encodage utilisés dans les références

**Mentionné dans :**
- [Newsletter #8 (2026-02-04)](/en/newsletters/2026-02-04-newsletter/) - Correction nostr-tools pour l'analyse des hashtags après les sauts de ligne

**Voir aussi :**
- [NIP-18 : Reposts](/fr/topics/nip-18/)
- [NIP-19 : Entités encodées en Bech32](/fr/topics/nip-19/)
