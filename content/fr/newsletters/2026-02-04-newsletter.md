---
title: 'Nostr Compass #8'
date: 2026-02-04
translationOf: /en/newsletters/2026-02-04-newsletter.md
translationDate: 2026-02-04
draft: false
type: newsletters
---

Bienvenue dans Nostr Compass, votre guide hebdomadaire sur Nostr.

**Cette semaine :** rust-nostr livre une refonte majeure de l'API avec 21 PRs révisant l'architecture du SDK. Nostria 3.0 lance avec la navigation à double volet, la gestion des listes et une refonte complète de l'interface. Vector ajoute l'accélération SIMD atteignant des gains de 65x à 184x et livre le support du protocole [Marmot](/fr/topics/marmot/) pour la messagerie de groupe chiffrée. Frostr apporte la signature à seuil sur iOS via TestFlight. Damus implémente les indices de relais [NIP-19 (Entités encodées Bech32)](/fr/topics/nip-19/) pour la découverte de contenu inter-relais. Primal Android ajoute le chiffrement NWC et les exports de transactions du portefeuille. nostr-tools et NDK reçoivent des améliorations de fiabilité. NIP-82 (Applications logicielles) s'étend pour couvrir 98% des plateformes d'appareils. Le dépôt NIPs fusionne le support des factures de rétention pour [NIP-47 (Nostr Wallet Connect)](/fr/topics/nip-47/). Les nouvelles propositions de protocole incluent NIP-74 pour les podcasts, NIP-DB pour les bases de données d'événements navigateur et une suite TRUSTed Filters pour la curation de contenu décentralisée. Les nouveaux projets incluent Instagram to Nostr v2 pour la migration de contenu, Pod21 lançant une place de marché d'impression 3D décentralisée, Clawstr introduisant des communautés gérées par agents IA, et Shosho et NosCall étendant les capacités de streaming en direct et d'appels vidéo.

## Actualités

### rust-nostr livre une refonte majeure de l'API

Le SDK [rust-nostr](https://github.com/rust-nostr/nostr) a subi une refonte architecturale significative cette semaine avec 21 PRs fusionnées introduisant des changements cassants à travers la bibliothèque. La refonte affecte les APIs principales sur lesquelles la plupart des développeurs Rust comptent.

[PR #1245](https://github.com/rust-nostr/nostr/pull/1245) redessine les APIs de notification, tandis que [PR #1244](https://github.com/rust-nostr/nostr/pull/1244) remplace `RelayNotification::Shutdown` par `RelayStatus::Shutdown` pour une gestion d'état plus propre. Les APIs de signataire s'alignent maintenant avec les autres patterns du SDK via [PR #1243](https://github.com/rust-nostr/nostr/pull/1243). Les méthodes Client et Relay ont été nettoyées dans [PR #1242](https://github.com/rust-nostr/nostr/pull/1242), et les options client utilisent maintenant un pattern builder ([PR #1241](https://github.com/rust-nostr/nostr/pull/1241)).

Les APIs d'envoi de messages ont été redessinées dans [PR #1240](https://github.com/rust-nostr/nostr/pull/1240), le désabonnement REQ dans [PR #1239](https://github.com/rust-nostr/nostr/pull/1239), et la suppression de relais dans [PR #1229](https://github.com/rust-nostr/nostr/pull/1229). Une [PR ouverte #1246](https://github.com/rust-nostr/nostr/pull/1246) ajoute le support des APIs bloquantes pour compléter la refonte.

Les changements apportent de la cohérence au SDK mais nécessiteront un effort de migration de la part des projets existants. Les développeurs construisant sur rust-nostr devraient examiner attentivement le changelog avant de mettre à jour.

### Instagram to Nostr v2 permet la migration de contenu

Un nouvel outil permet aux créateurs de migrer leur contenu existant des plateformes centralisées vers Nostr. [Instagram to Nostr v2](https://github.com/primalpaul1/instagram-to-nostr-v2) supporte l'import depuis Instagram, TikTok, Twitter et Substack sans nécessiter l'accès aux clés privées de l'utilisateur.

L'outil répond à une barrière d'intégration courante : les utilisateurs hésitants à repartir de zéro sur une nouvelle plateforme peuvent maintenant préserver leur historique de contenu. Il supporte également l'offre de comptes Nostr à de nouveaux utilisateurs ou la proposition de contenu à des comptes existants, le rendant utile pour aider les autres à transitionner vers le protocole.

### Pod21 : Réseau d'impression 3D décentralisé

[Pod21](https://pod21.com) connecte les opérateurs d'imprimantes 3D avec les acheteurs en utilisant Nostr pour la coordination de la place de marché. La plateforme inclut un bot DM compatible [NIP-17 (Messages directs privés)](/fr/topics/nip-17/) qui gère les interactions de la place de marché, permettant aux acheteurs de demander des impressions et de négocier avec les fabricants via des messages directs chiffrés.

Les fabricants listent leur capacité et leurs capacités d'impression ; les acheteurs parcourent les annonces et initient les commandes via le bot. L'architecture suit un pattern similaire aux autres applications de commerce Nostr : découverte basée sur les relais, messagerie chiffrée pour la coordination des commandes et Lightning pour le règlement. Pod21 rejoint Ridestr et Shopstr comme applications Nostr coordonnant des transactions du monde réel via le protocole.

### Clawstr : Réseau social d'agents IA

[Clawstr](https://github.com/clawstr/clawstr) se lance comme une plateforme inspirée de Reddit où des agents IA créent et gèrent des communautés sur Nostr. La plateforme permet aux agents autonomes d'établir des communautés thématiques, de curer le contenu et d'interagir avec les utilisateurs. Les communautés fonctionnent comme des subreddits mais avec des modérateurs et curateurs IA guidant les discussions. L'architecture utilise le protocole ouvert de Nostr pour les interactions agent-à-agent et agent-à-humain, établissant un nouveau modèle pour la formation de communautés sur les médias sociaux décentralisés.

## Versions

### Ridestr v0.2.0 : Version RoadFlare

[Ridestr](https://github.com/variablefate/ridestr) a livré [v0.2.0](https://github.com/variablefate/ridestr/releases/tag/v0.2.0), baptisée la "Version RoadFlare", introduisant les réseaux de covoiturage personnels. La fonctionnalité permet aux passagers d'ajouter leurs conducteurs favoris à un réseau de confiance. Les conducteurs approuvent les abonnés et partagent des localisations chiffrées, permettant aux passagers de voir quand les conducteurs de confiance sont en ligne et à proximité. Les demandes de trajet vont directement aux conducteurs connus.

La fiabilité des paiements s'est améliorée avec la récupération automatique de séquestre, une meilleure synchronisation du portefeuille entre appareils et un traitement des paiements plus rapide via le polling progressif. [PR #37](https://github.com/variablefate/ridestr/pull/37) ajoute l'infrastructure Phase 5-6 supportant ces fonctionnalités. [v0.2.1](https://github.com/variablefate/ridestr/releases/tag/v0.2.1) a suivi avec des corrections pour les bugs de dialogue de paiement et le flux "Ajouter aux favoris" après trajet.

### Nostria 3.0

[Nostria](https://github.com/nostria-app/nostria), le client multiplateforme de sondreb conçu pour l'échelle mondiale, a livré la version 3.0 avec une refonte complète de l'interface, un nouveau logo et des centaines de corrections. La version représente un cycle de développement intensif de six semaines.

La navigation à double volet est le plus grand changement UX, permettant aux utilisateurs de bureau de réduire les changements de contexte lors des déplacements entre listes, détails et fils de discussion. Une nouvelle section Accueil fournit une vue d'ensemble de toutes les fonctionnalités disponibles, et tous les écrans partagent une barre d'outils, une mise en page et des fonctionnalités unifiées.

La gestion des listes est la mise à jour de fonctionnalité la plus significative, intégrée dans toute l'application. Les utilisateurs peuvent gérer les listes de profils et filtrer le contenu dans n'importe quelle fonctionnalité : Streams, Musique ou Flux. Fatigué du spam dans les fils de discussion ? Filtrez par favoris pour ne voir que leurs réponses. Quick Zaps ajoute le zapping en un tap avec des valeurs configurables. Copier/Capture d'écran génère des captures d'écran pour le presse-papiers pour partager des événements n'importe où. Mots masqués filtre maintenant sur les champs de profil (name, display_name, NIP-05), permettant aux utilisateurs de bloquer tous les profils relayés avec un seul mot banni. Les paramètres sont devenus recherchables pour des changements de configuration plus rapides.

La version ajoute le rendu des demandes de paiement BOLT11 et BOLT12, la sélection de taille de texte et de police, et la messagerie "Note-à-soi-même" dans la section Messages avec le rendu du contenu référencé comme les articles et événements. Le nouveau dialogue de partage permet un partage rapide par email, sites web ou messages directs vers plusieurs destinataires. Les fonctionnalités additionnelles incluent les ensembles d'emoji personnalisés, les Intérêts (listes de hashtags comme flux dynamiques), les Favoris, les Flux de relais publics et la personnalisation complète du menu incluant quelle option l'icône Nostria ouvre.

Disponible sur Android, iOS, Windows et web sur [nostria.app](https://www.nostria.app/).

### Applesauce v5.1.0

La suite de bibliothèques [Applesauce](https://github.com/hzrd149/applesauce) de hzrd149 a publié v5.1.0 pour tous les packages. [applesauce-signers](https://github.com/hzrd149/applesauce/releases/tag/applesauce-signers%405.1.0) ajoute le support des méthodes `switch_relays` et `ping` sur les signataires distants Nostr Connect, utile pour gérer les connexions de signataires de manière programmatique. [applesauce-loaders](https://github.com/hzrd149/applesauce/releases/tag/applesauce-loaders%405.1.0) introduit `loadAsyncMap` pour le chargement asynchrone parallèle. [applesauce-react](https://github.com/hzrd149/applesauce/releases/tag/applesauce-react%405.1.0) ajoute des arguments de remplissage à `useAction().run()`. [applesauce-core](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%405.1.0) met à jour le mapping event-to-store pour gérer les chaînes directement sans nécessiter `onlyEvents`.

### nak v0.18.3

[nak](https://github.com/fiatjaf/nak) (Nostr Army Knife) de fiatjaf a atteint [v0.18.3](https://github.com/fiatjaf/nak/releases/tag/v0.18.3) avec des corrections de stabilité de mattn. La version prévient les panics quand les URLs de mint manquent le séparateur `://`, valide les erreurs de dateparser avant d'utiliser les valeurs de date et gère les cas limites dans l'analyse des tags de challenge AUTH. Ces corrections défensives rendent le CLI plus résilient lors du traitement d'entrées malformées.

### Aegis v0.3.7

[Aegis](https://github.com/ZharlieW/Aegis), le signataire de bureau multiplateforme, a livré [v0.3.7](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.7) ajoutant le support du navigateur d'applications Nostr avec la signature [NIP-07 (Interface d'extension navigateur)](/fr/topics/nip-07/). La version enregistre les événements de chiffrement [NIP-04 (Messages directs chiffrés)](/fr/topics/nip-04/) et [NIP-44 (Chiffrement versionné)](/fr/topics/nip-44/), permettant aux utilisateurs de suivre quelles applications demandent des opérations de chiffrement. Le segment navigateur filtre maintenant par plateforme pour n'afficher que les applications web.

### Bitchat v1.5.1 (iOS)

[Bitchat](https://github.com/permissionlesstech/bitchat), l'application de messagerie capable de fonctionner hors ligne utilisant Nostr et le mesh Bluetooth, a publié [v1.5.1](https://github.com/permissionlesstech/bitchat/releases/tag/v1.5.1) avec un renforcement de la sécurité iOS. [PR #1012](https://github.com/permissionlesstech/bitchat/pull/1012) valide les signatures d'événements Nostr avant le traitement, rejette les giftwraps et paquets intégrés invalides, plafonne les charges utiles surdimensionnées et bloque les IDs d'expéditeur BLE annonce usurpés. [PR #998](https://github.com/permissionlesstech/bitchat/pull/998) corrige l'authentification mesh BLE iOS en liant les IDs d'expéditeur aux UUIDs de connexion, empêchant l'usurpation d'identité dans le réseau mesh. [PR #972](https://github.com/permissionlesstech/bitchat/pull/972) ajoute la limitation du taux de notifications pour prévenir les inondations de découverte de pairs quand plusieurs appareils mesh sont à proximité.

### KeyChat v1.39.2

[KeyChat](https://github.com/keychat-io/keychat-app) a publié [v1.39.2](https://github.com/keychat-io/keychat-app/releases/tag/v1.39.2%2B6495) ajoutant le support [NIP-47](/fr/topics/nip-47/) Nostr Wallet Connect via [PR #148](https://github.com/keychat-io/keychat-app/pull/148). Les utilisateurs peuvent maintenant connecter des portefeuilles Lightning externes pour les paiements dans l'application de messagerie. La version ajoute également les notifications de bureau macOS.

### Nostrmo v3.5.0

[Nostrmo](https://github.com/haorendashu/nostrmo), le client Flutter multiplateforme, a livré [v3.5.0](https://github.com/haorendashu/nostrmo/releases/tag/3.5.0) révisant son système de flux. La mise à jour remplace les flux fixes par des alternatives personnalisables : Flux général, Flux de mentions et Flux de relais, chacun configurable via de nouvelles pages d'édition. La version implémente le support du modèle outbox pour un meilleur routage des événements et étend la fonctionnalité de relais local avec des limites de taille configurables et le support des abonnements.

### Shosho v0.11.1

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), l'application de streaming en direct pour Nostr, a publié [v0.11.1](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.11.1) avec des capacités d'enregistrement et VOD. La mise à jour ajoute des indicateurs de présence dans la salle montrant qui regarde les streams, des conversations de chat en fil pour une meilleure organisation des discussions et le support Nostr Connect sur iOS via [NIP-46](/fr/topics/nip-46/). Les streamers peuvent maintenant sauvegarder leurs diffusions pour une visualisation ultérieure tout en maintenant des interactions de chat en temps réel avec leur audience.

### NosCall v0.5.0

[NosCall](https://github.com/sanah9/noscall), l'application d'appels audio et vidéo pour Nostr, a livré [v0.5.0](https://github.com/sanah9/noscall/releases/tag/v0.5.0-release) avec des groupes de contacts pour organiser les appels par catégorie, la gestion des relais pour l'optimisation des connexions et des paramètres de serveur ICE configurables pour une meilleure traversée NAT. La version ajoute également le support du mode sombre. NosCall utilise Nostr pour la signalisation et la coordination des appels, permettant des appels pair-à-pair sans serveurs centralisés.

### diVine 1.0.4

[diVine](https://github.com/divinevideo/divine-mobile), le client vidéo courte en boucle de rabble, a publié [1.0.4](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.4) comme pré-version alpha Android avant sa soumission Zapstore. La version se concentre sur les tests de gestion des clés Nostr, incluant l'import nsec, la signature à distance [NIP-46 (Nostr Connect)](/fr/topics/nip-46/) avec nsecBunker et Amber, et la gestion des URLs nostrconnect://. L'équipe sollicite des retours sur la compatibilité des relais et l'interopérabilité vidéo avec d'autres clients. [PR #1265](https://github.com/divinevideo/divine-mobile/pull/1265) corrige la gestion des chemins de fichiers iOS qui causait l'inutilisabilité des clips vidéo après les mises à jour de l'application en stockant des chemins relatifs au lieu de chemins absolus de conteneur. [PR #1251](https://github.com/divinevideo/divine-mobile/pull/1251) corrige les problèmes de navigation lors de la visualisation des profils depuis les commentaires.

### Zeus v0.12.2

[Zeus](https://github.com/ZeusLN/zeus) a livré [v0.12.2](https://github.com/ZeusLN/zeus/releases/tag/v0.12.2) comme version stable, consolidant les [corrections NWC couvertes dans les éditions précédentes](/fr/newsletters/2026-01-28-newsletter/#zeus-v0122-beta---corrections-nwc).

### Frostr Igloo iOS TestFlight

[Frostr](https://frostr.org/) a lancé [Igloo pour iOS](https://github.com/FROSTR-ORG/igloo-ios-prototype) sur [TestFlight](https://testflight.apple.com/join/72hjQe3J), étendant la signature à seuil aux appareils Apple. Frostr utilise les signatures FROST (Flexible Round-Optimized Schnorr Threshold) pour diviser les clés nsec en parts distribuées entre les appareils, permettant la signature k-sur-n avec tolérance aux pannes. Les utilisateurs rejoignant en "mode démo" participent à une expérience de signature à seuil 2-sur-2 en direct, démontrant les capacités de coordination en temps réel du protocole. La version iOS rejoint [Igloo pour Android](https://github.com/FROSTR-ORG/igloo-android) (v0.1.2), livrée en décembre avec le support [NIP-55 (Signataire Android)](/fr/topics/nip-55/) pour les demandes de signature inter-applications. Les deux clients mobiles complètent [Igloo desktop](https://github.com/FROSTR-ORG/igloo-desktop) et l'extension navigateur [Frost2x](https://github.com/FROSTR-ORG/frost2x).

## Mises à jour des projets

### Damus implémente les indices de relais NIP-19

[Damus](https://github.com/damus-io/damus) a fusionné [PR #3477](https://github.com/damus-io/damus/pull/3477), implémentant la consommation d'indices de relais [NIP-19](/fr/topics/nip-19/) pour la récupération d'événements. La fonctionnalité permet de visualiser des notes sur des relais n'étant pas dans le pool configuré de l'utilisateur en extrayant les indices de [NIP-10 (Fils de réponse)](/fr/topics/nip-10/), [NIP-18 (Reposts)](/fr/topics/nip-18/) et des références NIP-19. L'implémentation utilise des connexions de relais éphémères avec un nettoyage par comptage de références, évitant l'expansion permanente du pool de relais.

Les corrections additionnelles incluent l'analyse des factures Lightning ([PR #3566](https://github.com/damus-io/damus/pull/3566)), le chargement de la vue portefeuille ([PR #3554](https://github.com/damus-io/damus/pull/3554)), le timing de la liste de relais ([PR #3553](https://github.com/damus-io/damus/pull/3553)) et le préchargement des profils pour réduire le "popping" visuel ([PR #3550](https://github.com/damus-io/damus/pull/3550)). Une [PR brouillon #3590](https://github.com/damus-io/damus/pull/3590) montre le support DM privé [NIP-17](/fr/topics/nip-17/) en cours.

### Primal Android livre le chiffrement NWC

[Primal Android](https://github.com/PrimalHQ/primal-android-app) a eu une semaine très active avec 18 PRs fusionnées axées sur l'infrastructure de portefeuille. L'application s'intègre maintenant avec Spark, le protocole Lightning auto-custodial de Lightspark. [PR #874](https://github.com/PrimalHQ/primal-android-app/pull/874) ajoute le support du chiffrement NWC, tandis que [PR #872](https://github.com/PrimalHQ/primal-android-app/pull/872) envoie des événements info NWC quand les connexions s'établissent.

[PR #870](https://github.com/PrimalHQ/primal-android-app/pull/870) permet l'export CSV pour les transactions du portefeuille, utile pour la comptabilité et les impôts. [PR #716](https://github.com/PrimalHQ/primal-android-app/pull/716) ajoute un sélecteur de compte local dans l'éditeur de notes. Plusieurs corrections de restauration de portefeuille ([PR #876](https://github.com/PrimalHQ/primal-android-app/pull/876), [PR #875](https://github.com/PrimalHQ/primal-android-app/pull/875), [PR #873](https://github.com/PrimalHQ/primal-android-app/pull/873)) traitent les cas limites pour les utilisateurs avec des configurations de portefeuille non-Spark.

### Le SDK TypeScript Marmot ajoute l'historique des messages

L'implémentation TypeScript du protocole [Marmot](https://github.com/marmot-protocol/marmot) continue son développement. [PR #38](https://github.com/marmot-protocol/marmot-ts/pull/38) par hzrd149 implémente la persistance de l'historique des messages avec pagination pour l'application de chat de référence, tandis que [PR #39](https://github.com/marmot-protocol/marmot-ts/pull/39) améliore l'ergonomie de la bibliothèque.

Côté Rust, [PR #161](https://github.com/marmot-protocol/mdk/pull/161) implémente la gestion d'état récupérable pour préserver le contexte des messages en cas d'échec, et [PR #164](https://github.com/marmot-protocol/mdk/pull/164) passe à std::sync::Mutex pour éviter les panics tokio avec SQLite. Le backend whitenoise-rs ajoute [l'intégration Amber](https://github.com/marmot-protocol/whitenoise-rs/pull/418) ([PR #418](https://github.com/marmot-protocol/whitenoise-rs/pull/418)), [met à niveau vers MDK et nostr-sdk 0.44](https://github.com/marmot-protocol/whitenoise-rs/pull/467) ([PR #467](https://github.com/marmot-protocol/whitenoise-rs/pull/467)) et introduit le streaming de notifications en temps réel via [PR #460](https://github.com/marmot-protocol/whitenoise-rs/pull/460) avec les types d'événements NewMessage et GroupInvite.

### HAVEN ajoute le rafraîchissement périodique WoT

[HAVEN](https://github.com/bitvora/haven), le relais personnel, a fusionné [PR #108](https://github.com/bitvora/haven/pull/108) ajoutant le rafraîchissement périodique [Web of Trust](/fr/topics/web-of-trust/). La fonctionnalité assure que les scores de confiance restent à jour à mesure que les graphes sociaux des utilisateurs évoluent, améliorant la précision du filtrage de spam au fil du temps.

### nostr-tools

[nostr-tools](https://github.com/nbd-wtf/nostr-tools), la bibliothèque JavaScript principale, a reçu plusieurs améliorations cette semaine. Les commits incluent une [correction pour l'analyse des hashtags après les sauts de ligne](https://github.com/nbd-wtf/nostr-tools/commit/c2423f7f31853d97fef2e3d649204cec328e81d5) dans les mentions [NIP-27 (Références de notes textuelles)](/fr/topics/nip-27/), [l'élagage automatique des objets relay cassés avec suivi d'inactivité](https://github.com/nbd-wtf/nostr-tools/commit/ab802c8dbe35d29feb732ba54e82a346c21c32e2) pour le nettoyage des connexions, [la suppression de la file de messages](https://github.com/nbd-wtf/nostr-tools/commit/be9b91318fea6a0cb154b8734a15b50a4c1e7638) pour l'optimisation des performances mono-thread et [les exports de fichiers source](https://github.com/nbd-wtf/nostr-tools/commit/05b1fba5113182ac0aa3c72d1f511cd956a7c139) pour de meilleurs imports TypeScript.

### NDK

[NDK](https://github.com/nostr-dev-kit/ndk) a livré [beta.71](https://github.com/nostr-dev-kit/ndk/commit/26abea24726ed844fdd091744ac9f768f1a530a0) avec une [correction pour la reconnexion après les cycles veille/réveil de l'appareil et la gestion des connexions périmées](https://github.com/nostr-dev-kit/ndk/commit/33e759508bc656dc45d3d77c741edf581af323f3), traitant les problèmes de fiabilité pour les applications mobiles.

### Notedeck

[Notedeck](https://github.com/damus-io/notedeck), le client de bureau de l'équipe Damus, a une [PR ouverte #1279](https://github.com/damus-io/notedeck/pull/1279) ajoutant un visualiseur [NIP-34 (Collaboration Git)](/fr/topics/nip-34/). Cela permettrait de parcourir les dépôts git, patches et issues publiés sur les relais Nostr directement dans le client, faisant de Notedeck un potentiel front-end pour les flux de travail basés sur ngit.

### njump

[njump](https://github.com/fiatjaf/njump), la passerelle web Nostr, a ajouté le support de deux types d'événements [NIP-51 (Listes)](/fr/topics/nip-51/) via [PR #152](https://github.com/fiatjaf/njump/pull/152). La passerelle affiche maintenant les kind:30000 Follow Sets, qui sont des regroupements catégorisés d'utilisateurs que les clients peuvent afficher dans différents contextes, et les kind:39089 Starter Packs, qui sont des collections de profils curatées conçues pour le partage et le suivi en groupe. Ces ajouts permettent à njump d'afficher des listes curatées par la communauté quand les utilisateurs partagent des liens nevent.

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst), le client Android, a corrigé un bug empêchant le partage vidéo depuis la vue lecteur ([PR #1695](https://github.com/vitorpamplona/amethyst/pull/1695)). L'option "Partager vidéo" n'apparaissait pas parce que le paramètre content n'était pas passé au composant des boutons de contrôle. Les utilisateurs peuvent maintenant partager du contenu vidéo Nostr vers d'autres applications directement depuis le lecteur. [PR #1693](https://github.com/vitorpamplona/amethyst/pull/1693) corrige les crashs de désérialisation Jackson JSON qui se produisaient lors de l'analyse de certains événements malformés.

### Jumble

[Jumble](https://github.com/CodyTseng/jumble), le client web axé sur la navigation des flux de relais, a ajouté les uploads de fichiers audio via le presse-papiers dans [PR #743](https://github.com/CodyTseng/jumble/pull/743). Les utilisateurs peuvent maintenant coller des fichiers audio directement dans l'éditeur de post, qui les uploade vers les serveurs médias configurés et intègre l'URL dans la note. La fonctionnalité reflète la fonctionnalité existante de collage d'images.

### Flotilla

[Flotilla](https://github.com/coracle-social/flotilla), le client de communautés [NIP-29 (Groupes basés sur les relais)](/fr/topics/nip-29/) de hodlbod, a livré les notifications via [PR #270](https://github.com/coracle-social/flotilla/pull/270). La mise à jour refactorise le système d'alertes du polling basé sur les ancres vers les notifications pull locales pour le web et les notifications push pour le mobile. L'architecture implémente le standard NIP-9a proposé (voir [PR #2194](https://github.com/nostr-protocol/nips/pull/2194) ci-dessous), où les utilisateurs enregistrent des callbacks webhook avec les relais et reçoivent des charges utiles d'événements chiffrées quand les filtres correspondent.

### Formstr

[Formstr](https://github.com/abh3po/nostr-forms), l'application de formulaires native Nostr, a ajouté l'import de formulaires et le support des formulaires chiffrés dans [PR #422](https://github.com/abh3po/nostr-forms/pull/422). Les utilisateurs peuvent maintenant importer des formulaires existants depuis JSON ou d'autres instances Formstr. La fonctionnalité de chiffrement permet aux créateurs de formulaires de restreindre les réponses afin que seuls les destinataires désignés puissent lire les soumissions, utile pour les sondages collectant des informations sensibles.

### Pollerama

[Pollerama](https://pollerama.fun), construit sur la bibliothèque [nostr-polls](https://github.com/abh3po/nostr-polls), a ajouté le partage de sondages par DM [NIP-17](/fr/topics/nip-17/) via [PR #141](https://github.com/abh3po/nostr-polls/pull/141) et [PR #142](https://github.com/abh3po/nostr-polls/pull/142). Les utilisateurs peuvent maintenant partager des sondages directement aux contacts via des messages directs chiffrés.

### Nostrability Schemata

[Nostrability schemata](https://github.com/nostrability/schemata), la collection de schémas de vérification JSON pour les événements Nostr, a ajouté la couverture [NIP-59 (Gift Wrap)](/fr/topics/nip-59/) via [PR #59](https://github.com/nostrability/schemata/pull/59). La mise à jour inclut les schémas pour les événements kind 13 (seal) et kind 1059 (gift wrap), complétant la couverture existante des schémas [NIP-17](/fr/topics/nip-17/).

### Vector

[Vector](https://github.com/VectorPrivacy/Vector), le messager de bureau axé sur la confidentialité utilisant [NIP-17](/fr/topics/nip-17/), [NIP-44](/fr/topics/nip-44/) et [NIP-59](/fr/topics/nip-59/) pour le chiffrement sans métadonnées, a fusionné [PR #39](https://github.com/VectorPrivacy/Vector/pull/39) introduisant des optimisations de performance accélérées par SIMD. L'encodage hex s'exécute 65x plus vite, la génération d'aperçus d'images jusqu'à 38x plus vite et les recherches de messages 184x plus vite via l'indexation par recherche binaire. La PR ajoute les intrinsèques ARM64 NEON pour Apple Silicon et x86_64 AVX2/SSE2 avec détection runtime pour Windows et Linux. L'utilisation mémoire a chuté avec les structs de messages réduits de 472 à 128 octets et le stockage npub réduit de 99,6% grâce à l'internement.

Vector v0.3.0 (décembre 2025) a intégré [MDK (Marmot Development Kit)](https://github.com/marmot-protocol/mdk) pour la messagerie de groupe basée sur le protocole MLS, apportant des groupes chiffrés de bout en bout avec confidentialité persistante au client. Le partage de fichiers MIP-04 gère maintenant les pièces jointes imeta pour les groupes MLS, conçu pour l'interopérabilité avec [White Noise](/fr/newsletters/2026-01-28-newsletter/#le-sdk-typescript-marmot-ajoute-lhistorique-des-messages). La version a également introduit une plateforme Mini Apps avec des jeux multijoueurs P2P basés sur WebXDC, un app store décentralisé appelé The Nexus, l'intégration du portefeuille PIVX pour les paiements in-app, l'édition de messages avec suivi complet de l'historique et une réduction de 4x de la mémoire pendant les uploads d'images.

## Mises à jour des NIP

Changements récents dans le [dépôt NIPs](https://github.com/nostr-protocol/nips) :

**Fusionnés :**

- **[NIP-47 : Support des factures de rétention](https://github.com/nostr-protocol/nips/pull/1913)** - [NIP-47 (Nostr Wallet Connect)](/fr/topics/nip-47/) supporte maintenant les factures de rétention, permettant des flux de paiement avancés où les receveurs doivent explicitement régler ou annuler les paiements. La PR ajoute trois nouvelles méthodes RPC : `make_hold_invoice` crée une facture de rétention en utilisant une préimage pré-générée et un hash de paiement, `settle_hold_invoice` réclame le paiement en fournissant la préimage originale, et `cancel_hold_invoice` rejette le paiement en utilisant son hash de paiement. Une nouvelle notification `hold_invoice_accepted` se déclenche quand un payeur verrouille le paiement. Cela permet des cas d'usage comme le contenu pay-to-unlock, les systèmes de séquestre de place de marché et le gating de paiement. Les implémentations sont déjà en cours dans [Alby Hub](https://github.com/getAlby/hub/pull/1298), [Alby JS-SDK](https://github.com/getAlby/js-sdk/pull/382) et [dart NDK](https://github.com/relaystr/ndk/pull/147).

- **[NIP-05 : Exigence de minuscules](https://github.com/nostr-protocol/nips/pull/2208)** - [NIP-05 (Vérification de domaine)](/fr/topics/nip-05/) exige maintenant explicitement les minuscules pour les clés publiques hex et les noms locaux dans le fichier `nostr.json`. C'était implicite dans la spécification mais non déclaré, causant des problèmes d'interopérabilité quand certaines implémentations utilisaient des casses mixtes tandis que d'autres normalisaient en minuscules. Les clients validant les identifiants NIP-05 devraient maintenant rejeter toute réponse `nostr.json` contenant des caractères majuscules dans les clés ou noms.

- **[NIP-73 : Codes pays](https://github.com/nostr-protocol/nips/pull/2205)** - [NIP-73 (Géotags)](/fr/topics/nip-73/) supporte maintenant les codes pays ISO 3166 comme alternative aux geohashes. Les événements peuvent inclure des tags `["g", "US", "countryCode"]` pour indiquer la localisation au niveau du pays sans nécessiter de coordonnées précises. Cela permet le filtrage et la découverte de contenu basés sur le pays pour les applications où la localisation exacte est inutile ou indésirable. La PR a également ajouté un exemple de geohash manquant à la documentation de la spécification.

**PRs ouvertes et discussions :**

- **[NIP-82 : Applications logicielles](https://github.com/nostr-protocol/nips/pull/1336)** - franzap a annoncé une mise à jour majeure de cette spécification brouillon, qui définit comment les applications logicielles sont distribuées via Nostr en utilisant des événements release kind 30063. La mise à jour couvre maintenant environ 98% des plateformes d'appareils globalement, incluant macOS, Linux, Windows, FreeBSD, les environnements WASM, les extensions VS Code, les extensions Chrome et les Web Bundles/PWAs. L'équipe se concentre ensuite sur le support Android, PWA et iOS, invitant les développeurs à converger vers ce standard partagé. Zapstore prévoit de migrer vers le nouveau format dans les semaines à venir.

- **[NIP-74 : Podcasts](https://github.com/nostr-protocol/nips/pull/2211)** - Définit des événements adressables pour les émissions de podcast (kind 30074) et les épisodes (kind 30075). Les émissions incluent des métadonnées comme le titre, la description, les catégories et les images de couverture. Les épisodes référencent leur émission parente et incluent les URLs d'enclosure, les durées et les marqueurs de chapitres. La spécification s'intègre avec les standards de métadonnées Podcasting 2.0 et inclut des tags value pour la monétisation V4V (value-for-value) via Lightning. Des plateformes comme [transmit.fm](https://transmit.fm), une plateforme de publication de podcasts native Nostr, peuvent publier directement sur les relais en utilisant ce format, permettant aux podcasteurs de distribuer du contenu sans intermédiaires.

- **[NIP-FR : Notes réservées aux amis](https://github.com/nostr-protocol/nips/pull/2207)** - Propose un mécanisme pour publier des notes visibles uniquement par les follows mutuels. L'implémentation utilise [NIP-59 (Gift Wrap)](/fr/topics/nip-59/) pour chiffrer le contenu : l'auteur crée une note normale, puis gift-wrap des copies à chaque follow mutuel. La copie de chaque destinataire est chiffrée vers leur pubkey en utilisant NIP-44 et envoyée via le mécanisme gift wrap. Les destinataires peuvent vérifier que la note provient de quelqu'un qu'ils suivent, tandis que les non-mutuels ne peuvent pas accéder au contenu. Cette approche réutilise l'infrastructure cryptographique existante tout en permettant une fonctionnalité de confidentialité fréquemment demandée.

- **[NIP-DB : Interface de base de données d'événements Nostr navigateur](https://github.com/hzrd149/nostr-bucket)** - Propose une interface `window.nostrdb` standard pour les extensions navigateur fournissant un stockage local d'événements Nostr. L'API inclut des méthodes pour ajouter des événements, requêter par ID ou filtre, compter les correspondances et s'abonner aux mises à jour. Les applications web peuvent utiliser cette interface pour lire depuis les événements mis en cache localement sans faire de requêtes aux relais, réduisant la bande passante et la latence. L'extension navigateur [nostr-bucket](https://github.com/hzrd149/nostr-bucket) de hzrd149 fournit une implémentation de référence, injectant l'interface dans tous les onglets du navigateur. Une [bibliothèque polyfill](https://github.com/hzrd149/window.nostrdb.js) compagnon implémente la même API en utilisant IndexedDB pour les environnements sans l'extension.

- **[TRUSTed Filters](https://github.com/nostr-protocol/nips/pull/1534)** - Une suite de cinq propositions connexes pour la curation de contenu décentralisée, s'appuyant sur la [PR Trusted Assertions #1534](https://github.com/nostr-protocol/nips/pull/1534) de vitorpamplona. La spécification principale introduit les événements kind 17570 pour déclarer les préférences de fournisseur de confiance, permettant aux utilisateurs de spécifier quels services ils font confiance pour le filtrage et le classement des événements. Les fournisseurs de confiance publient des assertions (kind 37571), des statistiques (kind 37572) et des classements (kind 37573) auxquels les clients peuvent s'abonner. Le système utilise une architecture de plugins avec des tags W/w pour spécifier les types de filtres et les transformations. Cela permet aux opérations coûteuses en calcul comme la détection de spam, le scoring de réputation et le classement de contenu de s'exécuter sur une infrastructure dédiée tandis que les utilisateurs maintiennent le contrôle sur les fournisseurs auxquels ils font confiance. La suite inclut des spécifications séparées pour les préréglages de filtres, les classements d'utilisateurs, les événements de confiance et les définitions de plugins.

- **[NIP-9a : Notifications push](https://github.com/nostr-protocol/nips/pull/2194)** - hodlbod propose un standard pour les notifications push basées sur les relais utilisant des événements d'enregistrement kind 30390. Les utilisateurs créent un enregistrement contenant des filtres pour les événements qu'ils veulent recevoir et une URL de callback webhook. L'enregistrement est chiffré vers la pubkey du relais (depuis son champ `self` NIP-11). Quand des événements correspondants se produisent, les relais POST vers le callback avec l'ID de l'événement (en clair pour la déduplication) et l'événement lui-même (chiffré NIP-44 vers l'utilisateur). Cette architecture permet aux relais de pousser les notifications tout en protégeant le contenu des événements des serveurs push intermédiaires. La [PR #270](https://github.com/coracle-social/flotilla/pull/270) de Flotilla implémente ce standard.

- **[Catallax](https://github.com/SigmaEnterprise/Catallax)** - Propose un protocole de travail contractuel décentralisé avec séquestre utilisant des événements kind 33400. Le système définit trois rôles : les arbitres annoncent leur disponibilité et leurs conditions, les patrons créent des tâches financées avec du Bitcoin séquestré, et les agents libres complètent le travail pour réclamer le paiement. Les arbitres résolvent les litiges quand nécessaire. Le protocole permet la coordination de travail freelance sans confiance où les fonds sont verrouillés jusqu'à ce que les livrables soient acceptés ou que l'arbitrage conclue.

## Approfondissement NIP : NIP-47 (Nostr Wallet Connect)

[NIP-47](/fr/topics/nip-47/) définit Nostr Wallet Connect (NWC), un protocole pour le contrôle à distance de portefeuille Lightning utilisant Nostr comme couche de communication. Avec l'ajout cette semaine du support des factures de rétention, NWC couvre maintenant la gamme complète des opérations Lightning.

Le protocole fonctionne via un échange simple. Une application de portefeuille publie un événement "wallet info" (kind 13194) décrivant ses capacités. Les applications clientes envoient des requêtes chiffrées (kind 23194) demandant au portefeuille d'effectuer des opérations comme payer des factures, créer des factures ou vérifier les soldes. Le portefeuille répond avec des résultats chiffrés (kind 23195).

NWC utilise le chiffrement [NIP-44](/fr/topics/nip-44/) entre le client et le portefeuille, avec une paire de clés dédiée pour les opérations de portefeuille, la gardant séparée de l'identité principale de l'utilisateur. Cette séparation signifie que compromettre une connexion NWC n'expose pas l'identité Nostr de l'utilisateur.

**Méthodes supportées :**

La spécification définit des méthodes pour les opérations Lightning principales : `pay_invoice` envoie des paiements, `make_invoice` génère des factures pour recevoir, `lookup_invoice` vérifie le statut de paiement, `get_balance` retourne le solde du portefeuille, et `list_transactions` fournit l'historique des paiements. Le nouveau `pay_keysend` fusionné permet les paiements sans factures, et `hold_invoice` supporte les paiements conditionnels.

**Exemples d'événements :**

Le service de portefeuille publie un événement info (kind 13194) annonçant ses capacités :

```json
{
  "kind": 13194,
  "pubkey": "<pubkey du service de portefeuille>",
  "content": "pay_invoice get_balance make_invoice lookup_invoice list_transactions notifications",
  "tags": [
    ["encryption", "nip44_v2"],
    ["notifications", "payment_received payment_sent"]
  ],
  "created_at": "<horodatage unix>",
  "id": "<hash de l'événement>",
  "sig": "<signature du service de portefeuille>"
}
```

Un client envoie une requête chiffrée (kind 23194) pour payer une facture :

```json
{
  "kind": 23194,
  "pubkey": "<pubkey éphémère du client depuis le secret de l'URI de connexion>",
  "content": "<NIP-44 chiffré: {\"method\": \"pay_invoice\", \"params\": {\"invoice\": \"lnbc50n1...\"}}>",
  "tags": [
    ["p", "<pubkey du service de portefeuille>"],
    ["encryption", "nip44_v2"]
  ],
  "created_at": "<horodatage unix>",
  "id": "<hash de l'événement>",
  "sig": "<signature de la clé éphémère du client>"
}
```

Le service de portefeuille répond (kind 23195) avec le résultat du paiement :

```json
{
  "kind": 23195,
  "pubkey": "<pubkey du service de portefeuille>",
  "content": "<NIP-44 chiffré: {\"result_type\": \"pay_invoice\", \"result\": {\"preimage\": \"...\"}, \"error\": null}>",
  "tags": [
    ["p", "<pubkey éphémère du client>"],
    ["e", "<id de l'événement de requête>"]
  ],
  "created_at": "<horodatage unix>",
  "id": "<hash de l'événement>",
  "sig": "<signature du service de portefeuille>"
}
```

Le tag `e` dans la réponse référence la requête originale, permettant aux clients de faire correspondre les réponses à leurs requêtes.

**Factures de rétention :**

La [PR #1913](https://github.com/nostr-protocol/nips/pull/1913) de cette semaine a ajouté le support des factures de rétention, permettant des paiements de type séquestre. Contrairement aux factures standard où le destinataire réclame immédiatement le paiement en libérant la préimage, les factures de rétention permettent au destinataire de différer cette décision. Quand un payeur envoie vers une facture de rétention, les fonds se verrouillent le long de la route de paiement. Le destinataire choisit ensuite de régler (libérer la préimage et réclamer les fonds) ou d'annuler (rejeter le paiement, retournant les fonds au payeur). Si aucune action ne se produit, le paiement expire et les fonds retournent automatiquement. La PR ajoute trois méthodes NWC : `make_hold_invoice`, `settle_hold_invoice` et `cancel_hold_invoice`, plus une notification `hold_invoice_accepted`. Ce mécanisme alimente des applications comme le séquestre de covoiturage de Ridestr et la résolution de litiges de place de marché.

**Implémentations actuelles :**

Les principaux portefeuilles supportent NWC : Zeus, Alby et Primal (depuis la [PR #874](https://github.com/PrimalHQ/primal-android-app/pull/874) de cette semaine) implémentent tous le support côté portefeuille. Côté client, Damus, Amethyst et la plupart des clients Nostr majeurs peuvent se connecter aux portefeuilles NWC pour le zapping et les paiements.

Le protocole permet une séparation des préoccupations : les utilisateurs peuvent faire fonctionner leur portefeuille sur un appareil tout en interagissant avec Nostr depuis un autre, avec les relais Nostr servant de canal de communication. Cette architecture signifie que les clients mobiles n'ont pas besoin de détenir des fonds directement, améliorant la sécurité en gardant l'infrastructure de portefeuille séparée des clients sociaux.

**Considérations de sécurité :**

Les connexions NWC devraient être traitées comme sensibles. Bien que le chiffrement protège le contenu des messages, la pubkey du portefeuille et le secret de connexion doivent être protégés. Les applications devraient permettre aux utilisateurs de révoquer les connexions et de définir des limites de dépenses. Le protocole supporte les restrictions de capacités, permettant aux portefeuilles de limiter les opérations qu'une connexion particulière peut effectuer.

## Approfondissement NIP : NIP-59 (Gift Wrap)

[NIP-59](/fr/topics/nip-59/) définit un protocole pour encapsuler n'importe quel événement Nostr dans plusieurs couches de chiffrement, cachant l'identité de l'expéditeur aux relais et observateurs. Les propositions de cette semaine pour les notes réservées aux amis (NIP-FR) et les notifications push (NIP-9a) s'appuient toutes deux sur le gift wrapping, en faisant une primitive de confidentialité fondamentale à comprendre.

**Les trois couches :**

Le gift wrapping utilise trois structures imbriquées :

1. **Rumor** (événement non signé) : Le contenu original comme événement Nostr sans signature. Le rumor ne peut pas être envoyé directement aux relais car les relais rejettent les événements non signés.

2. **Seal** (kind 13) : Le rumor est chiffré en utilisant [NIP-44](/fr/topics/nip-44/) et placé dans un événement kind 13. Le seal EST signé par la clé de l'auteur réel. C'est la preuve cryptographique de paternité.

3. **Gift Wrap** (kind 1059) : Le seal est chiffré et placé dans un événement kind 1059 signé par une paire de clés aléatoire à usage unique. Le gift wrap inclut un tag `p` pour le routage vers le destinataire.

**Une idée fausse courante : La déniabilité**

La spécification mentionne que les rumors non signés fournissent la "déniabilité", mais c'est trompeur. La couche seal EST signée par l'auteur réel. Quand le destinataire déchiffre le gift wrap puis le seal, il a une preuve cryptographique de qui a envoyé le message. Le destinataire pourrait même construire une preuve à divulgation nulle révélant l'identité de l'expéditeur sans exposer sa propre clé privée.

Ce que le gift wrap fournit réellement est la **confidentialité de l'expéditeur vis-à-vis des observateurs** : les relais et tiers ne peuvent pas déterminer qui a envoyé le message car ils ne voient que le gift wrap signé par une clé aléatoire. Mais le destinataire sait toujours, et peut le prouver.

**Exemples d'événements :**

Voici la structure complète à trois couches de la spécification (envoyant "Tu vas à la fête ce soir ?") :

Le rumor (non signé, ne peut pas être publié aux relais) :
```json
{
  "created_at": 1691518405,
  "content": "Tu vas à la fête ce soir ?",
  "tags": [],
  "kind": 1,
  "pubkey": "611df01bfcf85c26ae65453b772d8f1dfd25c264621c0277e1fc1518686faef9",
  "id": "9dd003c6d3b73b74a85a9ab099469ce251653a7af76f523671ab828acd2a0ef9"
}
```

Le seal (kind 13, signé par l'auteur réel, contient le rumor chiffré) :
```json
{
  "kind": 13,
  "pubkey": "611df01bfcf85c26ae65453b772d8f1dfd25c264621c0277e1fc1518686faef9",
  "content": "AqBCdwoS7/tPK+QGkPCadJTn8FxGkd24iApo3BR9/M0uw6n4RFAFSPAKKMgkzVMo...",
  "created_at": 1703015180,
  "tags": [],
  "id": "28a87d7c074d94a58e9e89bb3e9e4e813e2189f285d797b1c56069d36f59eaa7",
  "sig": "02fc3facf6621196c32912b1ef53bac8f8bfe9db51c0e7102c073103586b0d29..."
}
```

Le gift wrap (kind 1059, signé par une clé éphémère aléatoire, contient le seal chiffré) :
```json
{
  "kind": 1059,
  "pubkey": "18b1a75918f1f2c90c23da616bce317d36e348bcf5f7ba55e75949319210c87c",
  "content": "AhC3Qj/QsKJFWuf6xroiYip+2yK95qPwJjVvFujhzSguJWb/6TlPpBW0CGFwfuf...",
  "created_at": 1703021488,
  "tags": [["p", "166bf3765ebd1fc55decfe395beff2ea3b2a4e0a8946e7eb578512b555737c99"]],
  "id": "5c005f3ccf01950aa8d131203248544fb1e41a0d698e846bd419cec3890903ac",
  "sig": "35fabdae4634eb630880a1896a886e40fd6ea8a60958e30b89b33a93e6235df7..."
}
```

Remarquez : la `pubkey` du seal est l'auteur réel (`611df01...`), tandis que la `pubkey` du gift wrap est une clé à usage unique aléatoire (`18b1a75...`). Les relais ne voient que le gift wrap, donc ils ne peuvent pas attribuer le message à l'auteur réel.

**Ce que chaque couche protège :**

Le rumor est non signé et ne peut pas être publié directement aux relais. Le seal est signé par l'auteur réel et prouve la paternité au destinataire. Le gift wrap est signé par une clé à usage unique aléatoire, cachant l'auteur réel aux relais et observateurs. Seul le destinataire peut déchiffrer à travers les deux couches pour atteindre le contenu original et vérifier la signature de l'auteur sur le seal.

**Applications actuelles :**

[NIP-17 (Messages directs privés)](/fr/topics/nip-17/) utilise le gift wrap pour les DM chiffrés, remplaçant l'ancien schéma NIP-04. Le NIP-FR proposé (notes réservées aux amis) gift-wrap les notes à chaque follow mutuel. NIP-9a (notifications push) chiffre les charges utiles de notification en utilisant les principes du gift wrap.

**Protection des métadonnées :**

Les horodatages devraient être randomisés pour contrecarrer l'analyse temporelle. Les relais devraient exiger AUTH avant de servir les événements kind 1059 et ne les servir qu'au destinataire marqué. Lors de l'envoi à plusieurs destinataires, créez des gift wraps séparés pour chacun.

---

C'est tout pour cette semaine. Vous construisez quelque chose ? Vous avez des nouvelles à partager ? Vous voulez que nous couvrions votre projet ? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contactez-nous via NIP-17 DM</a> ou trouvez-nous sur Nostr.
