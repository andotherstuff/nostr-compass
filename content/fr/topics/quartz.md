---
title: "Quartz"
date: 2025-12-31
translationOf: /en/topics/quartz.md
translationDate: 2026-03-07
draft: false
categories:
  - Bibliothèque
  - Développement
---

Quartz est une bibliothèque Nostr en Kotlin Multiplatform développée par Vitor Pamplona. C'est la couche partagée de protocole et de données derrière la progression d'Amethyst vers Android, le desktop et, à terme, iOS à partir d'une seule base de code.

## Comment ça fonctionne

Quartz fournit les fonctionnalités de base de Nostr sous forme de bibliothèque partagée :

- **Gestion des événements** : Analyse, validation et création d'événements Nostr
- **Cryptographie** : Signature Secp256k1, chiffrement NIP-44, gestion des clés
- **Communication avec les relays** : Gestion des connexions, ordonnancement des messages, gestion des abonnements
- **Support NIP** : Implémentation de NIPs courants comme NIP-06, NIP-19, NIP-44, et d'autres

## Pourquoi c'est important

Quartz déplace la logique lourde du protocole hors d'une application unique pour la mettre dans une bibliothèque réutilisable. Cela compte parce que la gestion des relays, l'analyse des événements, le chiffrement et les règles de stockage deviennent plus faciles à partager entre clients au lieu d'être réimplémentés sur chaque plateforme.

Le résultat concret est déjà visible dans le travail desktop d'Amethyst. Le refactoring financé par la subvention a déplacé du code partagé dans des modules Kotlin Multiplatform comme `commonMain`, `jvmAndroid` et `jvmMain`, transformant le support desktop en problème de bibliothèque et de modules plutôt qu'en réécriture complète.

## Architecture

La bibliothèque utilise une structure modulaire de source sets :
- `commonMain` : Code partagé pour toutes les plateformes
- `jvmAndroid` : Code partagé entre JVM et Android
- `androidMain` : Implémentations spécifiques à Android
- `jvmMain` : Implémentations JVM desktop
- `iosMain` : Implémentations spécifiques à iOS

## Statut actuel

En décembre 2025, OpenSats a annoncé le financement de Quartz dans sa quatorzième vague de subventions Nostr. Le dépôt existe comme bibliothèque autonome, mais une grande partie des progrès visibles jusqu'ici est arrivée via des PRs Amethyst qui convertissent les modules de l'application en code multiplateforme et suivent la parité fonctionnelle entre cibles.

---

**Sources principales :**
- [Dépôt Quartz](https://github.com/vitorpamplona/quartz)
- [Quartz sur Maven Central](https://central.sonatype.com/artifact/com.vitorpamplona.quartz/quartz)
- [Dépôt Amethyst](https://github.com/vitorpamplona/amethyst)
- [Quatorzième vague de subventions Nostr d'OpenSats](https://opensats.org/blog/fourteenth-wave-of-nostr-grants)

**Mentionné dans :**
- [Newsletter #3 : Récapitulatif de Décembre](/fr/newsletters/2025-12-31-newsletter/#december-2025-ecosystem-expansion)
- [Newsletter #3 : Actualités](/fr/newsletters/2025-12-31-newsletter/#news)
- [Newsletter #3 : Changements Notables d'Amethyst](/fr/newsletters/2025-12-31-newsletter/#amethyst-android)

**Voir aussi :**
- [Protocole Blossom](/fr/topics/blossom/)
