---
title: "NIP-56 : Signalement"
date: 2026-02-18
translationOf: /en/topics/nip-56.md
translationDate: 2026-02-18
draft: false
categories:
  - Moderation
  - Protocol
---

NIP-56 définit un mécanisme de signalement utilisant des événements kind 1984, permettant aux utilisateurs et aux applications de signaler du contenu répréhensible sur le réseau Nostr.

## Fonctionnement

Un utilisateur publie un événement kind 1984 avec un tag `p` référençant la pubkey signalée. Lors du signalement d'une note spécifique, un tag `e` référence l'ID de la note. Les deux tags acceptent un troisième paramètre spécifiant la catégorie de violation.

## Catégories de signalement

- **nudity** : contenu adulte
- **malware** : virus, chevaux de Troie, rançongiciels
- **profanity** : langage offensant et discours haineux
- **illegal** : contenu pouvant violer des lois
- **spam** : messages répétitifs non sollicités
- **impersonation** : usurpation d'identité frauduleuse
- **other** : violations ne correspondant pas aux catégories ci-dessus

## Comportement des clients et des relays

Les clients peuvent utiliser les signalements des utilisateurs suivis pour les décisions de modération, comme flouter le contenu lorsque plusieurs contacts de confiance le signalent. Les relays doivent éviter la modération automatique via les signalements en raison des risques de manipulation ; les signalements de modérateurs de confiance peuvent informer l'application manuelle à la place. Une classification supplémentaire est supportée via les tags `l` et `L` de NIP-32.

---

**Sources principales :**
- [Spécification NIP-56](https://github.com/nostr-protocol/nips/blob/master/56.md)

**Mentionné dans :**
- [Compass #10 : Mises à jour des projets](/fr/newsletters/2026-02-18-newsletter/#notedeck--préparation-pour-lapp-store-android)

**Voir aussi :**
- [NIP-22 : Commentaire](/fr/topics/nip-22/)
