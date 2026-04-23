---
title: 'Nostr Compass #3'
date: 2025-12-31
translationOf: /en/newsletters/2025-12-31-newsletter.md
translationDate: 2026-04-23
draft: false
type: newsletters
---

Bienvenue dans Nostr Compass, votre guide hebdomadaire sur l'écosystème du protocole Nostr.

**Cette semaine :** Alors que 2025 s'achève, nous revenons sur cinq années de jalons de décembre dans l'évolution de Nostr. De la première version client de fiatjaf en décembre 2020, au don décisif de 14 BTC de Jack Dorsey en décembre 2022, jusqu'à la prolifération des signers [NIP-55](/fr/topics/nip-55/) et à l'accélération de cache 162x de NDK ce mois-ci, décembre a marqué de façon répétée des tournants pour le protocole. Ce numéro spécial retrace l'histoire technique de chaque mois de décembre, documentant la croissance du protocole, de deux relays expérimentaux à plus de 2 500 nœuds dans 50 pays. En plus : le module desktop d'Amethyst prend forme via Quartz, Notedeck gagne une messagerie, Citrine héberge des applications web et [NIP-54](/fr/topics/nip-54/) corrige l'internationalisation pour les écritures non latines.

## Récapitulatif de décembre : cinq années de décembres Nostr

Nostr fête ses cinq ans cette année. fiatjaf a lancé le protocole le 7 novembre 2020, et chaque mois de décembre depuis a marqué une phase distincte de son évolution : de la preuve de concept au mouvement mondial, puis à l'écosystème de production. Il s'agit d'une rétrospective technique de décembre 2020 à décembre 2025, les années formatrices qui ont posé les fondations de Nostr et catalysé son moment de bascule.

### Décembre 2020 : genèse

Le premier mois complet d'existence de Nostr a vu fiatjaf publier [Branle](https://github.com/fiatjaf/branle), le premier client du protocole, construit avec Quasar (Vue.js) et absurd-sql pour le stockage local. fiatjaf avait déjà posé l'architecture de base : des utilisateurs identifiés par des clés publiques secp256k1, des messages tous signés cryptographiquement, et des relays servant de stockage passif sans communiquer entre eux. Un ou deux relays expérimentaux servaient une poignée d'adoptants précoces qui se coordonnaient dans le groupe Telegram [@nostr_protocol](https://t.me/nostr_protocol), lancé le 16 novembre. La [documentation d'origine](https://fiatjaf.com/nostr.html) décrivait « the simplest open protocol that is able to create a censorship-resistant global social network », une promesse qui demanderait encore deux années avant d'être prouvée.

### Décembre 2021 : premiers développements

Le 31 décembre 2021, Nostr a atteint la [page d'accueil de Hacker News](https://news.ycombinator.com/item?id=29749061) avec 110 points et 138 commentaires, via une soumission de Cameri. Cela a marqué la première exposition significative du protocole auprès de la communauté de développeurs au sens large. Le réseau fonctionnait sur environ sept relays avec moins de 1 000 utilisateurs. Branle a reçu des mises à jour, dont l'import de clé privée le 31 décembre et le support multi-relays. Un client en ligne de commande, noscl, permettait une interaction via terminal. Les spécifications du protocole vivaient encore dans la documentation de fiatjaf, puisque le dépôt formel des [NIPs](https://github.com/nostr-protocol/nips) ne serait créé qu'en mai 2022. Le protocole était, selon les mots de fiatjaf, « a work in progress ».

### Décembre 2022 : le point de bascule

Décembre 2022 a transformé Nostr, d'expérience confidentielle en mouvement plus large. Le catalyseur est arrivé le 15 décembre, quand Jack Dorsey a donné [14.17171699 BTC](https://www.coindesk.com/tech/2022/12/15/jack-dorsey-gives-decentralized-social-network-nostr-14-btc-in-funding) (environ 245 000 à 250 000 dollars) à fiatjaf après avoir découvert le protocole et déclaré qu'il représentait « 100 percent what we wanted from Bluesky, but it wasn't developed from a company ». Le 16 décembre, fiatjaf a annoncé qu'il partageait les fonds avec le développeur de Damus William Casarin (jb55), et Dorsey a vérifié son compte Nostr (npub : `npub1sg6plzptd64u62a878hep2kev88swjh3tw00gjsfl8f237lmu63q0uf63m`). Ce financement a légitimé le projet du jour au lendemain.

La même semaine, le chaos sur Twitter a accéléré l'adoption. Les 14 et 15 décembre ont vu la suspension de journalistes en vue du New York Times, de CNN et du Washington Post. Le 18 décembre, Twitter a [annoncé des interdictions](https://techcrunch.com/2022/12/18/twitter-wont-let-you-post-your-facebook-instagram-and-mastodon-handles/) visant les comptes faisant la promotion de Nostr, Mastodon et d'autres plateformes. La politique a été annulée dès le lendemain après un retour de bâton. Cet exode a poussé les utilisateurs à explorer des alternatives.

Le développement du protocole s'est emballé. Le 16 décembre, [NIP-19](/fr/topics/nip-19/) a été fusionné ([#57](https://github.com/nostr-protocol/nips/pull/57)), introduisant des identifiants encodés en bech32 (`npub`, `nsec`, `note`, `nprofile`, `nevent`) qui rendaient les clés lisibles par des humains et faciles à distinguer. Le dépôt des NIPs a enregistré plus de 36 commits ce mois-là, y compris des mises à jour pour NIP-40 et NIP-07. Les clients se sont multipliés : Damus a rempli sa bêta TestFlight en quelques heures, Astral a forké Branle pour la création de profils, Snort a lancé un client web « fast, censorship-resistant », et Vitor Pamplona a commencé le développement d'Amethyst. Alby v1.22.1 « Kemble's Cascade of Stars » est sorti le 22 décembre avec le support de NIP-19. Au 7 décembre, Nostr comptait environ 800 utilisateurs avec un profil. Quand Damus est arrivé sur l'App Store le 31 janvier 2023, les vannes se sont ouvertes, poussant la croissance à plus de 315 000 utilisateurs en juin 2023.

### Décembre 2023 : maturation de l'écosystème

Décembre 2023 a marqué un point d'inflexion critique pour la sécurité du protocole Nostr. Le 20 décembre, la [révision 3 de NIP-44 a été fusionnée](https://github.com/nostr-protocol/nips/pull/746) après un audit de sécurité indépendant de Cure53 (NOS-01) qui avait identifié 10 problèmes dans les implémentations TypeScript, Go et Rust, dont des attaques temporelles et des inquiétudes autour de la forward secrecy. La spécification mise à jour a remplacé le chiffrement défaillant de [NIP-04](/fr/topics/nip-04/) par ChaCha20 et HMAC-SHA256, posant la base cryptographique qui soutient désormais les DMs privés de [NIP-17](/fr/topics/nip-17/) et le gift wrapping de [NIP-59](/fr/topics/nip-59/). La même semaine, [OpenSats a annoncé sa quatrième vague de grants](https://opensats.org/blog/nostr-grants-december-2023) le 21 décembre, finançant sept projets dont Lume, noStrudel, ZapThreads et un audit indépendant de NIP-44. Cela faisait suite à la [première vague de juillet 2023](https://opensats.org/blog/nostr-grants-july-2023), qui avait financé Damus, Coracle, Iris et d'autres, portant l'allocation totale du Nostr Fund à environ 3,4 millions de dollars sur 39 grants.

Le mois a aussi mis en lumière les tensions de soutenabilité dans l'écosystème. Le 28 décembre, William Casarin (jb55) a [écrit sur Stacker News](https://stacker.news/items/368863) que 2024 serait « likely be the last year of Damus », expliquant que « nostr clients don't make money » après que les restrictions d'Apple sur les zaps intégrés ont fortement limité le potentiel de revenus. L'équipe Damus avait auparavant rejeté un financement VC. Pendant ce temps, [Nostr Wallet Connect v0.4.1](https://github.com/getAlby/nostr-wallet-connect/releases/tag/0.4.1) est sorti le 26 décembre, étendant [NIP-47](/fr/topics/nip-47/) avec les méthodes `pay_keysend`, `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance` et `get_info`, posant les bases des intégrations wallet qui deviendraient standard dans les clients.

### Décembre 2024 : avancée du protocole

Décembre 2024 s'est ouvert avec le [lancement alpha de Notedeck](https://damus.io/notedeck/) le 30 novembre, le client desktop Rust de l'équipe Damus, avec interface multi-colonnes et support de plusieurs comptes. Construit pour Linux, macOS et Windows, avec Android prévu pour 2025, Notedeck a d'abord été livré aux abonnés Damus Purple et représentait une expansion stratégique au-delà d'iOS. Deux semaines plus tard, [OpenSats a annoncé sa neuvième vague de grants](https://opensats.org/blog/9th-wave-of-nostr-grants) le 16 décembre, finançant AlgoRelay, le premier relay algorithmique pour les flux personnalisés, Pokey, une application Android avec maillage Bluetooth pour internet restreint, Nostr Safebox (stockage de jetons [NIP-60](/fr/topics/nip-60/) [Cashu](/fr/topics/cashu/)) et LumiLumi, un client web léger et accessible, portant l'allocation totale du Nostr Fund à environ 9 millions de dollars, soit une hausse de 67 % sur un an.

Le mois a vu une maturation importante des clients dans tout l'écosystème. [Gossip 0.13.0](https://github.com/mikedilger/gossip/releases/tag/v0.13.0) est arrivé le 23 décembre avec le support de File Metadata ([NIP-92](/fr/topics/nip-92/)/[NIP-94](/fr/topics/nip-94/)), l'intégration Blossom et la recherche de relays [NIP-50](/fr/topics/nip-50/). [Coracle 0.5.0](https://github.com/coracle-social/coracle/releases/tag/0.5.0) est sorti le 12 décembre avec un onboarding retravaillé et l'intégration de nostr-editor. Le développement du protocole est resté actif avec 30 pull requests soumises entre le 9 et le 22 décembre, dont 10 fusionnées, y compris des réécritures de [NIP-46](/fr/topics/nip-46/) pour n'utiliser que le chiffrement NIP-44, ainsi que la poursuite des travaux sur [NIP-104](/fr/topics/nip-104/) pour un chiffrement à double cliquet de niveau Signal. Les statistiques réseau montraient plus de 224 000 événements quotidiens de trusted pubkeys, une multiplication par quatre d'une année sur l'autre des nouveaux profils avec listes de contacts, et une hausse de 50 % des événements d'écriture publique.

### Décembre 2025 : expansion de l'écosystème

Décembre 2025 a apporté une maturation continue du protocole et une expansion de l'écosystème. Le 21 décembre, [OpenSats a annoncé sa quatorzième vague de grants Nostr](https://opensats.org/blog/fourteenth-wave-of-nostr-grants), finançant trois projets : YakiHonne, un client multi-plateforme avec portail créateur pour le contenu long format et intégration de paiements [Cashu](/fr/topics/cashu/) et Nutzaps, Quartz, la bibliothèque Kotlin Multiplatform de Vitor Pamplona qui alimente Amethyst et rendra possible une version iOS, et Nostr Feedz, l'intégration bidirectionnelle RSS-vers-Nostr de PlebOne. Des renouvellements de grants ont été attribués à Dart NDK et au nostr-relay de Mattn.

L'évolution du protocole a continué avec [NIP-BE](/fr/topics/nip-be/), la messagerie Bluetooth Low Energy, fusionné en novembre ([#1979](https://github.com/nostr-protocol/nips/pull/1979)), ce qui permet la synchronisation hors ligne entre appareils. [NIP-A4](/fr/topics/nip-a4/), Public Messages, kind 24, a suivi plus tard dans le mois ([#1988](https://github.com/nostr-protocol/nips/pull/1988)), en définissant des messages destinés à l'écran de notification qui utilisent des tags `q` pour éviter les complications de threading. [NIP-29](/fr/topics/nip-29/) a reçu une clarification importante ([#2106](https://github.com/nostr-protocol/nips/pull/2106)), introduisant le tag `hidden` pour des groupes réellement privés et intraçables. La spécification [NIP-55](/fr/topics/nip-55/) a elle aussi été affinée ([#2166](https://github.com/nostr-protocol/nips/pull/2166)), pour corriger une erreur d'implémentation fréquente où des développeurs appelaient `get_public_key` depuis des processus en arrière-plan.

Côté client, [Primal Android est devenu un signer NIP-55 complet](/en/newsletters/2025-12-24-newsletter/#news) grâce à huit PRs fusionnées implémentant `LocalSignerContentProvider`, rejoignant Amber et Aegis parmi les options de signature Android. La [bibliothèque NDK a atteint des requêtes de cache 162x plus rapides](/en/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes), passant d'environ 3 690 ms à environ 22 ms, en éliminant les écritures en double et les recherches inutiles dans le cache LRU ([PR #371](https://github.com/nostr-dev-kit/ndk/pull/371), [PR #372](https://github.com/nostr-dev-kit/ndk/pull/372)). Shopstr a introduit [Zapsnags](/en/newsletters/2025-12-24-newsletter/#news) pour les ventes flash via zaps. White Noise a livré [MIP-05](/fr/topics/mip-05/), des notifications push préservant la vie privée. Voir [Newsletter #1](/en/newsletters/2025-12-17-newsletter/) et [Newsletter #2](/en/newsletters/2025-12-24-newsletter/) pour la couverture complète.

---

Il y a cinq ans, fiatjaf publiait Branle pour une poignée d'utilisateurs répartis sur deux relays expérimentaux. Aujourd'hui, le protocole alimente plus de 140 clients, plus de 2 500 relays dans 50 pays, et un web of trust en croissance reliant des centaines de milliers de paires de clés. Le schéma de grandes sorties en décembre s'est poursuivi ce mois-ci avec la messagerie Bluetooth, la multiplication des signers Android et des grants d'infrastructure signalant des investissements durables dans les outils cross-platform.

## Actualités

**Amethyst Desktop prend forme** - Le grant Quartz de la quatorzième vague d'OpenSats produit déjà des résultats. [PR #1625](https://github.com/vitorpamplona/amethyst/pull/1625) crée un module `:desktopApp` complet pour Amethyst en utilisant Compose Multiplatform, avec écrans de connexion et de flux global déjà fonctionnels sur Desktop JVM. L'architecture convertit le module `:commons` en Kotlin Multiplatform avec une structure propre de source sets (`commonMain`, `jvmAndroid`, `androidMain`, `jvmMain`), ce qui permet de partager des composants UI entre Android et desktop tout en laissant les décisions spécifiques à chaque plateforme à leur cible respective. Cela pose les bases de la future version iOS via la même approche Kotlin Multiplatform.

**Réponses vocales dans Amethyst** - Cadeau de Noël signé davotoula : [PR #1622](https://github.com/vitorpamplona/amethyst/pull/1622) ajoute des écrans dédiés aux réponses vocales avec visualisation de forme d'onde, possibilité de réenregistrer, sélection du serveur média et indicateurs de progression d'upload. Les utilisateurs peuvent maintenant répondre en audio aux messages vocaux racine comme aux réponses vocales.

**Notedeck ajoute la messagerie** - Notedeck, le client desktop de Damus, a gagné une fonctionnalité de messages dans [PR #1223](https://github.com/damus-io/notedeck/pull/1223), élargissant son périmètre au-delà de la navigation dans la timeline vers la communication directe.

**Citrine héberge des applications web** - Citrine peut maintenant [héberger des applications web](https://github.com/greenart7c3/Citrine/pull/81), transformant votre téléphone en serveur web Nostr local-first. Une autre [PR #85](https://github.com/greenart7c3/Citrine/pull/85) ajoute la reconnexion automatique et la diffusion d'événements quand la connectivité réseau revient, avec une couverture de tests complète à travers les niveaux d'API Android.

**Registre d'outils développeur Nostrability** - Le suivi [Developer Kits & Tooling](https://github.com/nostrability/nostrability/issues/264) maintient un registre sélectionné de SDKs, bibliothèques et outils de développement à travers les langages, dont TypeScript, Rust, Python, Go, Dart et Swift. Si vous débutez dans le développement Nostr, c'est un bon point de départ pour trouver la boîte à outils adaptée à votre stack.

## Mises à jour des NIP

Changements récents dans le [dépôt des NIPs](https://github.com/nostr-protocol/nips) :

- **[NIP-54](/fr/topics/nip-54/)** - Correctif critique d'internationalisation pour la normalisation du d-tag wiki ([#2177](https://github.com/nostr-protocol/nips/pull/2177)). Les règles précédentes convertissaient tous les caractères non ASCII en `-`, ce qui cassait la prise en charge du japonais, du chinois, de l'arabe, du cyrillique et d'autres écritures. La spécification mise à jour préserve les lettres UTF-8, n'applique les minuscules qu'aux caractères qui disposent d'une variante de casse, et inclut des exemples détaillés : `"ウィキペディア"` reste `"ウィキペディア"`, `"Москва"` devient `"москва"`, et des écritures mixtes comme `"日本語 Article"` se normalisent en `"日本語-article"`.

## Versions

**Zapstore 1.0-rc1** - La boutique d'applications permissionless basée sur Nostr livre la [première release candidate](https://github.com/zapstore/zapstore/releases/tag/1.0-rc1) de sa nouvelle architecture, avec rafraîchissement complet de l'UI, gestionnaire de paquets réécrit avec une meilleure gestion des erreurs, App Stacks pour la découverte curatée, écrans de profil repensés, vérification des mises à jour en arrière-plan et défilement infini dans les listes de versions.

**KeyChat v1.38.1** - L'application de messagerie chiffrée fondée sur MLS [ajoute le support UnifiedPush](https://github.com/keychat-io/keychat-app/releases/tag/v1.38.1%2B6489) pour les notifications push sur Android et Linux, ainsi qu'une authentification biométrique pour les opérations sensibles. Disponible sur Android, Windows, macOS et Linux.

**Alby Go v2.0.0** - Le compagnon mobile du wallet Lightning [livre une refonte visuelle](https://github.com/getAlby/go/releases/tag/v2.0.0) avec nouveau logo, palette de couleurs mise à jour, carnet d'adresses repensé et clavier de saisie des montants amélioré. BTC Map est maintenant accessible depuis l'écran d'accueil, et les descriptions de transactions apparaissent dans les notifications.

**nak v0.17.4** - L'outil Nostr en ligne de commande de fiatjaf est [sorti](https://github.com/fiatjaf/nak/releases/tag/v0.17.4), après le correctif de la restriction Linux LMDB dans v0.17.3 évoqué la semaine dernière.

## Changements de code et de documentation à surveiller

*Pull requests ouvertes et travaux encore précoces qui méritent d'être suivis.*

### Damus (iOS)

[Indices de relais NIP-19](https://github.com/damus-io/damus/pull/3477) implémente la consommation d'indices de relais pour la récupération d'événements. Quand des utilisateurs ouvrent des liens `nevent`, `nprofile` ou `naddr`, Damus extrait désormais les indices de relais depuis les données TLV bech32 et se connecte à des relays éphémères pour récupérer du contenu absent du pool de relays de l'utilisateur. L'implémentation inclut un nettoyage avec comptage de références pour éviter les conditions de course lors de recherches simultanées. [Détection d'URL d'image](https://github.com/damus-io/damus/pull/3474) convertit automatiquement les URLs d'image collées en miniatures d'aperçu dans le compositeur, avec badge de position de carrousel pour plusieurs images. [Conversion de collage npub](https://github.com/damus-io/damus/pull/3473) transforme des chaînes `npub` ou `nprofile` collées en liens de mention avec résolution de profil asynchrone.

### Amethyst (Android)

[Cibles de paiement](https://github.com/vitorpamplona/amethyst/pull/1627) ajoute une interface d'événement pour les partages de zap NIP-57, permettant aux posts de spécifier plusieurs destinataires se partageant les zaps entrants, utile pour les collaborations, le partage de revenus ou les pourboires au créateur comme à ses outils. [Documentation de parité fonctionnelle Quartz](https://github.com/vitorpamplona/amethyst/pull/1624) ajoute un tableau détaillé recensant les fonctionnalités implémentées sur Android, Desktop JVM et iOS, en signalant qu'iOS manque encore de cryptographie de base (`Secp256k1Instance`), de sérialisation JSON et de structures de données.

### Notedeck (Desktop)

[Reconstruction des filtres de timeline](https://github.com/damus-io/notedeck/pull/1226) corrige un bug où des comptes non suivis continuaient d'apparaître dans les flux. Les filtres de timeline étaient construits une seule fois à partir de la liste de contacts et n'étaient jamais mis à jour. Le correctif ajoute un suivi `contact_list_timestamp` et une méthode `invalidate()` pour déclencher une reconstruction quand l'état de suivi change.

### Citrine (relay Android)

[API ContentProvider](https://github.com/greenart7c3/Citrine/pull/86) expose la base de données d'événements du relay local à d'autres applications Android via `ContentResolver`. Contrairement à l'interface WebSocket, qui oblige les applications à maintenir une connexion persistante et à parler le protocole de relay Nostr, ContentProvider offre un accès direct et synchrone à la base via le mécanisme IPC natif d'Android. Les applications externes peuvent interroger les événements par ID, pubkey, kind ou plage de dates, insérer de nouveaux événements avec validation et supprimer des événements sans gérer de connexions socket.

### rust-nostr (bibliothèque)

[Support NIP-40 au niveau relay](https://github.com/rust-nostr/nostr/pull/1183) ajoute la gestion de l'expiration au niveau du relay builder. Les événements expirés sont désormais rejetés avant stockage et filtrés avant envoi aux clients, ce qui évite à chaque implémentation de base de données d'avoir à gérer elle-même les vérifications d'expiration.

### nak (CLI)

[Miroir Blossom](https://github.com/fiatjaf/nak/pull/91) implémente une fonctionnalité de mirroring de blobs pour l'outil en ligne de commande.

### Mostro (trading P2P)

[Événements d'audit des frais de développement](https://github.com/MostroP2P/mostro/pull/559) ajoute des pistes d'audit transparentes pour les paiements au fonds de développement via des événements Nostr de kind 8383. L'implémentation publie des événements d'audit non bloquants après les paiements de frais réussis, avec détails de commande et hash de paiement, tout en excluant les pubkeys acheteur et vendeur pour préserver la vie privée.

### MDK (Marmot Development Kit)

Trois correctifs issus d'audit de sécurité ont été fusionnés : [Vérification d'auteur](https://github.com/marmot-protocol/mdk/pull/40) impose que les pubkeys des rumors correspondent aux identifiants d'expéditeur MLS afin d'empêcher l'usurpation. [Liaison d'identité KeyPackage](https://github.com/marmot-protocol/mdk/pull/41) vérifie que l'identité du credential correspond au signataire de l'événement. [Validation des mises à jour admin](https://github.com/marmot-protocol/mdk/pull/42) empêche les ensembles d'admins vides et l'assignation d'admins non membres.

### Shopstr (marketplace)

[Escrow sur facture HODL](https://github.com/shopstr-eng/shopstr/pull/217) implémente un système de paiement minimisant la confiance pour les biens physiques. L'architecture utilise `makeHoldInvoice` d'Alby pour verrouiller les fonds de l'acheteur dans son propre wallet, avec règlement déclenché seulement après vérification de l'inventaire par le marchand. Le protocole d'échange passe par des DMs chiffrés [NIP-17](/fr/topics/nip-17/) : l'acheteur envoie une demande de commande, le marchand répond avec une facture HODL, l'acheteur paie, les fonds sont verrouillés, le marchand confirme le stock et l'expédition, puis le règlement libère les fonds. Le support des paniers multi-marchands répartit les paiements entre vendeurs.

### Jumble (client web)

[Mode de découverte par relay](https://github.com/CodyTseng/jumble/pull/713) ajoute un interrupteur pour masquer, sur certains relays, les posts d'utilisateurs suivis, ce qui permet des flux de découverte par langue, par exemple `nostr.band/lang/*`. La fonctionnalité filtre les posts dont la pubkey d'auteur apparaît dans la liste de suivis de l'utilisateur, en persistant l'état de l'option par URL de relay dans localStorage.

### White Noise (messagerie chiffrée)

[Réessai d'upload média](https://github.com/marmot-protocol/whitenoise/pull/937) ajoute des options de réessai pour les uploads échoués. [Avertissements sur l'édition de profil](https://github.com/marmot-protocol/whitenoise/pull/927) alertent les utilisateurs à propos des changements de profil. Côté backend, [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs/pull/422) corrige une condition de course lors de la création d'AccountGroup.

### npub.cash (service d'adresses Lightning)

[Réécriture v3](https://github.com/cashubtc/npubcash-server/pull/40) migre le monorepo et le serveur vers Bun, ajoute le support SQLite, abandonne la compatibilité v1, implémente LUD-21 et ajoute des mises à jour temps réel des quotes de mint.

### nostr-java (bibliothèque)

[v1.1.1](https://github.com/tcheeric/nostr-java/releases/tag/v1.1.1) livre des refactorings de gestion WebSocket et une robustesse de tests améliorée à travers [deux PRs](https://github.com/tcheeric/nostr-java/pull/499).

### Dépôt NIPs

[Migration Djot pour NIP-54](https://github.com/nostr-protocol/nips/pull/2180) propose un changement séparé pour la spécification wiki : passer le format de contenu d'Asciidoc à Djot, un langage de balisage léger à la syntaxe plus propre. La PR introduit des liens en style référence pour les wikilinks, ce qui rend les renvois entre articles wiki plus lisibles dans le source. [NIP-XX Quorum](https://github.com/nostr-protocol/nips/pull/2179) introduit une gouvernance multi-signature à seuil pour les groupes Nostr en s'appuyant sur FROST, Flexible Round-Optimized Schnorr Threshold signatures. Un Quorum est un `nsec` partagé entre ses membres dans un schéma T-sur-N où les membres peuvent se représenter eux-mêmes ou déléguer à un conseil de représentants. Quand le conseil change, l'ancien `nsec` devient obsolète et un nouveau est distribué, l'acte final de tout conseil étant la signature de l'événement de transition de gouvernance. La spécification définit l'adhésion, publique ou privée, les élections et votes, y compris les motions de défiance, des « lois » éventuelles en langage naturel, et surtout des ontologies de quorum où des quorums peuvent être membres d'autres quorums, ce qui permet des structures hiérarchiques comme des localités rejoignant des entités régionales. Les cas d'usage vont du développement logiciel aux conseils d'administration, associations de copropriété et communautés modérées.

---

C'est tout pour cette semaine et pour cette année. Vous construisez quelque chose ? Vous avez des nouvelles à partager ? Vous voulez que nous couvrions votre projet ? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contactez-nous via DM [NIP-17](/fr/topics/nip-17/)</a> ou retrouvez-nous sur Nostr.
