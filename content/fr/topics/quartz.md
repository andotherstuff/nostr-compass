---
title: "Quartz"
date: 2025-12-31
translationOf: /en/topics/quartz.md
translationDate: 2025-12-31
draft: false
categories:
  - Bibliothèque
  - Développement
---

Quartz est une bibliothèque Kotlin Multiplatform pour Nostr développée par Vitor Pamplona. Initialement extraite du client Android Amethyst, Quartz fournit des implémentations réutilisables du protocole Nostr pour les plateformes JVM, Android, iOS et Linux.

## Comment Ça Fonctionne

Quartz fournit les fonctionnalités de base de Nostr sous forme de bibliothèque partagée :

- **Gestion des Événements** : Analyse, validation et création d'événements Nostr
- **Cryptographie** : Signature Secp256k1, chiffrement NIP-44, gestion des clés
- **Communication avec les Relays** : Gestion des connexions, ordonnancement des messages, gestion des abonnements
- **Support NIP** : Implémentation des NIPs courants incluant NIP-06, NIP-19, NIP-44, et plus

## Fonctionnalités Clés

- **Kotlin Multiplatform** : Une base de code unique compile vers plusieurs cibles
- **Plateformes Cibles** : Android, JVM, iOS (ARM64, Simulateur), Linux
- **Optimisé pour la Performance** : Traitement efficace des événements et opérations cryptographiques
- **Intégration Blossom** : Support pour le téléversement de médias via le protocole Blossom
- **OpenTimestamp** : Port Kotlin complet pour la vérification des horodatages

## Architecture

La bibliothèque utilise une structure modulaire de source sets :
- `commonMain` : Code partagé pour toutes les plateformes
- `jvmAndroid` : Code partagé entre JVM et Android
- `androidMain` : Implémentations spécifiques à Android
- `jvmMain` : Implémentations JVM bureau
- `iosMain` : Implémentations spécifiques à iOS

## Subvention OpenSats

En décembre 2025, OpenSats a annoncé le financement de Quartz dans le cadre de sa quatorzième vague de subventions Nostr. La subvention soutient le développement continu pour permettre Amethyst sur iOS via la même approche Kotlin Multiplatform qui alimente déjà les versions Android et bureau.

---

**Sources principales :**
- [Quartz sur Maven Central](https://central.sonatype.com/artifact/com.vitorpamplona.quartz/quartz)
- [Dépôt Amethyst](https://github.com/vitorpamplona/amethyst)

**Mentionné dans :**
- [Newsletter #3 : Récapitulatif de Décembre](/fr/newsletters/2025-12-31-newsletter/#december-2025-ecosystem-expansion)
- [Newsletter #3 : Actualités](/fr/newsletters/2025-12-31-newsletter/#news)
- [Newsletter #3 : Changements Notables d'Amethyst](/fr/newsletters/2025-12-31-newsletter/#amethyst-android)

**Voir aussi :**
- [Protocole Blossom](/fr/topics/blossom/)
