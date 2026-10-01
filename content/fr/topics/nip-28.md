---
title: "NIP-28 : Chat public"
date: 2026-09-30
draft: false
categories:
  - NIPs
  - Social
translationOf: /en/topics/nip-28.md
translationDate: 2026-10-01
---

NIP-28 décrit les canaux de chat public, les messages de canal et la modération côté client sous forme d'event Nostr. La spécification actuelle est marquée comme **brouillon** et **non recommandée** et oriente les développeurs vers NIP-29 pour les groupes actuels basés sur des relay.

## Modèle d'event

Le kind `40` crée un canal ; le kind `41` met à jour ses métadonnées ; le kind `42` contient un message. Les kind `43` et `44` permettent à un utilisateur de masquer un message ou de mettre un autre utilisateur en sourdine dans son client. Les tag des messages font référence à l'event de création du canal et peuvent identifier le message auquel on répond. Les relay ne sont pas tenus d'appliquer ces choix de masquage et de mise en sourdine effectués côté client.

La [modification de la spécification de septembre 2022](https://github.com/nostr-protocol/nips/commit/3423a6dfb) a fait d'un salon de chat public un objet partagé du protocole. Il reste utile de comprendre ce rôle historique, même si la [spécification actuelle](https://github.com/nostr-protocol/nips/blob/master/28.md) recommande une autre voie pour les nouvelles implémentations.

---

**Sources primaires :**
- [Spécification NIP-28 et statut actuel](https://github.com/nostr-protocol/nips/blob/master/28.md)
- [Modification du chat public de septembre 2022](https://github.com/nostr-protocol/nips/commit/3423a6dfb)

**Mentionné dans :**
- [Lettre d'information #42 : septembre 2022](/fr/newsletters/2026-09-30-newsletter/#september-2022-chat-and-delegated-actions-enter-the-specifications)

**Voir aussi :**
- [NIP-29 : Groupes basés sur des relay](/fr/topics/nip-29/)
