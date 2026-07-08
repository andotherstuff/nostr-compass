---
title: "NIP-82 : Applications logicielles"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-82.md
translationDate: 2026-07-01
categories:
  - Discovery
  - Apps
---

NIP-82 définit un événement d'application logicielle afin que les clients Nostr puissent afficher les applications (APK Android, apps iOS, apps web, binaires desktop) comme des objets de première classe dans les flux et les surfaces de découverte. La spécification remplace l'approche antérieure consistant à décrire les apps via des notes génériques kind 1 ou des recommandations de handler [NIP-89](/fr/topics/nip-89/) par un événement dédié et structuré qui porte les métadonnées d'application, les captures d'écran, les liens de dépôt et l'identité de l'auteur.

## Comment ça marche

Une application logicielle NIP-82 est un unique événement remplaçable adressé par pubkey d'auteur et tag `d`. L'événement porte :

- Des tags `name`, `description`, `icon`, `image` pour l'affichage
- Des tags `repository` et `web` pour les URL de la source et de la page d'accueil
- Un tag `platforms` énumérant les cibles prises en charge (android, ios, web, linux, macos, windows)
- Des tags `download` pour chaque binaire spécifique à la plateforme ou URL web
- Des tags `screenshots` portant les URL d'images pour les captures d'écran de l'application
- Des tags de sujet `t` pour la catégorisation
- Un tag `version` pour la version publiée actuelle

Un client parcourant un flux NIP-82 peut afficher la carte de l'application, faire un lien vers le dépôt canonique et faire remonter les captures d'écran sans se rabattre sur le grattage d'un article long Nostr ou d'un magasin d'applications tiers. Le pubkey de l'auteur est la source de vérité pour l'application, donc un client peut vérifier que l'éditeur correspond à l'identité de développeur attendue avant de promouvoir un lien de téléchargement.

## Sémantique de flux

Les événements NIP-82 sont adressables, donc chaque application a un événement remplaçable canonique par auteur. Un développeur publiant une nouvelle version remplace l'événement précédent sur place, et les abonnés voient la mise à jour sans gérer l'historique des événements. Les clients qui veulent un journal des changements peuvent s'abonner à l'événement adressable et afficher les montées de version comme activité sur la surface de l'application.

La spécification se compose avec [NIP-89](/fr/topics/nip-89/) (Application Handlers) : un événement NIP-82 décrit l'application en tant qu'artefact, tandis qu'un événement NIP-89 décrit que l'application peut gérer des kinds d'événements spécifiques. Les clients peuvent utiliser l'un sans l'autre, mais la paire offre une surface de découverte (NIP-82) et une surface de délégation (NIP-89) qui fonctionnent ensemble.

## Implémentations

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) intègre un flux dédié d'applications logicielles NIP-82 avec un écran de détail, des informations sur l'auteur et des captures d'écran ([PR #3036](https://github.com/vitorpamplona/amethyst/pull/3036), [PR #3078](https://github.com/vitorpamplona/amethyst/pull/3078), [PR #3200](https://github.com/vitorpamplona/amethyst/pull/3200))

---

**Sources primaires :**
- [Spécification NIP-82](https://github.com/nostr-protocol/nips/blob/master/82.md)
- [Amethyst PR #3036](https://github.com/vitorpamplona/amethyst/pull/3036) - Ajoute la prise en charge des applications logicielles NIP-82 avec un flux dédié
- [Amethyst PR #3078](https://github.com/vitorpamplona/amethyst/pull/3078) - Ajoute un écran de détail dédié aux applications logicielles NIP-82
- [Amethyst PR #3200](https://github.com/vitorpamplona/amethyst/pull/3200) - Améliore l'UI des applications logicielles NIP-82 avec informations d'auteur et captures d'écran

**Mentionné dans :**
- [Newsletter #27 : Amethyst v1.12.0 intègre les portefeuilles Cashu, les nutzaps, un pilote CLINK et l'auto-réparation Tor](/fr/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**Voir aussi :**
- [NIP-89 : Handlers d'applications](/fr/topics/nip-89/)
