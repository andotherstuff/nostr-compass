---
title: "NIP-56 : Signalement"
date: 2026-02-18
translationOf: /en/topics/nip-56.md
translationDate: 2026-03-07
draft: false
categories:
  - Moderation
  - Protocol
---

NIP-56 définit les événements de signalement kind `1984`. Ils permettent aux utilisateurs et aux applications de publier des signaux de modération concernant des comptes, des notes et des blobs sans nécessiter une autorité de modération unique et partagée.

## Fonctionnement

Un signalement doit inclure un tag `p` pour la pubkey signalée. Si le signalement concerne un événement spécifique, il doit également inclure un tag `e` pour cet événement. Le type de signalement apparaît comme troisième valeur dans le tag `p`, `e` ou `x` concerné.

## Catégories de signalement

- **nudity** : contenu adulte
- **malware** : virus, chevaux de Troie, rançongiciels et charges utiles similaires
- **profanity** : langage offensant et discours haineux
- **illegal** : contenu pouvant violer des lois
- **spam** : messages répétitifs non sollicités
- **impersonation** : usurpation d'identité frauduleuse
- **other** : violations ne correspondant pas aux catégories ci-dessus

Les signalements de blobs utilisent des tags `x` avec le hash du blob et peuvent inclure un tag `server` pointant vers le point de terminaison d'hébergement. Cela rend NIP-56 utilisable pour la modération de médias, pas seulement pour les notes et les profils.

## Sécurité et modèle de confiance

Les signalements sont des signaux, pas des verdicts. Les clients peuvent les pondérer en utilisant la confiance sociale, les listes de modération ou des rôles de modérateurs explicites. Les relays peuvent aussi les lire, mais la spécification met en garde contre la modération entièrement automatique car les signalements sont faciles à manipuler.

Une classification supplémentaire peut être ajoutée avec les tags `l` et `L` de [NIP-32](/fr/topics/nip-32/), ce qui est utile lorsqu'un client souhaite un vocabulaire de modération plus fin que les sept types de signalement de base.

---

**Sources principales :**
- [Spécification NIP-56](https://github.com/nostr-protocol/nips/blob/master/56.md)

**Mentionné dans :**
- [Newsletter #10 : Mises à jour des projets](/en/newsletters/2026-02-18-newsletter/#notedeck-android-app-store-prep)

**Voir aussi :**
- [NIP-22 : Commentaire](/fr/topics/nip-22/)
