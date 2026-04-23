---
title: "NIP-C7 : Messages de chat"
date: 2026-04-15
translationOf: /en/topics/nip-c7.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Messaging
---

NIP-C7 définit le kind `9` comme kind d'événement pour les messages de chat. L'objectif est de séparer le trafic orienté chat du trafic de flux social général, afin que les clients puissent appliquer des règles UX et de modération différentes à chaque contexte.

## Fonctionnement

Un événement kind `9` transporte le contenu du message ainsi que des tags qui identifient le contexte de chat. Dans les groupes basés sur relay [NIP-29](/fr/topics/nip-29/), l'événement inclut un tag `h` avec l'identifiant du groupe. Le threading des réponses utilise des tags `q` qui référencent des événements antérieurs.

NIP-C7 se concentre sur l'endroit où ces événements doivent être rendus. Au lieu d'apparaître dans les flux globaux de notes comme les text notes kind `1`, les événements kind `9` sont destinés à des vues orientées chat où l'état de la conversation et le threading sont explicites.

## Implémentations

- [Flotilla](https://gitea.coracle.social/coracle/flotilla) et [Coracle](https://github.com/coracle-social/coracle) utilisent le kind `9` dans leurs workflows de chat de groupe.
- [Amethyst](https://github.com/vitorpamplona/amethyst) inclut le support du kind `9` dans sa pile de messagerie.
- [White Noise](https://github.com/marmot-protocol/whitenoise) utilise le threading de réponses NIP-C7 avec des tags `q`.

---

**Sources principales :**
- [Spécification NIP-C7](https://github.com/nostr-protocol/nips/blob/master/C7.md)
- [PR #2310 : Restrict kind 9 to chat views](https://github.com/nostr-protocol/nips/pull/2310)

**Mentionné dans :**
- [Newsletter #18 : mises à jour NIP](/en/newsletters/2026-04-15-newsletter/)

**Voir aussi :**
- [NIP-29 : Groupes basés sur les relais](/fr/topics/nip-29/)
- [NIP-17 : Messages directs privés](/fr/topics/nip-17/)
