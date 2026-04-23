---
title: 'Nostr Compass #18'
date: 2026-04-15
translationOf: /en/newsletters/2026-04-15-newsletter.md
translationDate: 2026-04-22
draft: false
type: newsletters
---

Bienvenue dans Nostr Compass, votre guide hebdomadaire sur Nostr.

**Cette semaine :** [Amethyst](https://github.com/vitorpamplona/amethyst) fusionne 29 PRs autour de Tor desktop, d'une implémentation C secp256k1, des appels [NIP-AC](/fr/topics/nip-ac/) et du support multi-wallet [NIP-47](/fr/topics/nip-47/). [nstrfy](https://github.com/vcavallo/nstrfy-android) lance des notifications push natives à Nostr pour Android via les relays et les événements kind `7741`. [HAMSTR](https://github.com/LibertyFarmer/hamstr) ajoute Reticulum pour transporter des événements Nostr sur un mesh LoRa sans connexion internet. [Bloom](https://github.com/nostrnative/bloom) livre [v0.1.0](https://github.com/nostrnative/bloom/releases/tag/v0.1.0) avec un serveur [Blossom](/fr/topics/blossom/) auto-hébergé et un relay embarqué. [WaveFunc](https://github.com/zeSchlausKwab/wavefunc) lance une radio internet sur Nostr. [Botburrow](https://github.com/marmot-protocol/botburrow) démarre comme plateforme de bots auto-hébergée pour les chats de groupe [Marmot](/fr/topics/marmot/). [Snort](https://github.com/v0l/snort) livre une série de releases avec audit de sécurité et refonte des performances, tandis que [Primal Android](https://github.com/PrimalHQ/primal-android-app) repense sa mise en page du flux.

## Actualités

### Amethyst fusionne Tor desktop, C secp256k1, les appels WebRTC et le multi-wallet NWC

[Amethyst](https://github.com/vitorpamplona/amethyst), le client Android maintenu par vitorpamplona, a fusionné 29 PRs cette semaine à travers la cryptographie, le réseau, les appels et l'infrastructure wallet. La plus grande modification, [PR #2381](https://github.com/vitorpamplona/amethyst/pull/2381), ajoute le support de Tor sur desktop en embarquant un daemon kmp-tor avec un design fail-closed : si Tor est activé, toutes les connexions relay passent par le processus Tor embarqué, et l'application refuse de se connecter si Tor ne démarre pas.

[PR #2374](https://github.com/vitorpamplona/amethyst/pull/2374) ajoute une implémentation secp256k1 en C avec bindings JNI pour la vérification de signature, avec GLV decomposition, encodage de point wNAF et SHA-256 accéléré matériellement sur x86_64 et ARM64. Le résultat annoncé est un gain de 2x à 3x sur la vérification des signatures Schnorr. La [PR #2202](https://github.com/vitorpamplona/amethyst/pull/2202) aligne l'implémentation MLS en pur Kotlin sur RFC 9420 pour l'intégration [Marmot](/fr/topics/marmot/), tandis que la série [PR #2203](https://github.com/vitorpamplona/amethyst/pull/2203) à [PR #2211](https://github.com/vitorpamplona/amethyst/pull/2211) construit un système complet d'appels voix et vidéo pour [NIP-AC](/fr/topics/nip-ac/). Enfin, [PR #1988](https://github.com/vitorpamplona/amethyst/pull/1988) ajoute le support multi-wallet [NIP-47](/fr/topics/nip-47/), et [PR #2189](https://github.com/vitorpamplona/amethyst/pull/2189) ajoute la conversion GIF-vers-MP4 avec réglage de qualité.

### nstrfy lance des notifications push natives à Nostr pour Android

[nstrfy](https://github.com/vcavallo/nstrfy-android) a été lancé le 13 avril avec trois releases de [v1.0.0](https://github.com/vcavallo/nstrfy-android/releases/tag/v1.0.0) à [v1.2.0](https://github.com/vcavallo/nstrfy-android/releases/tag/v1.2.0). L'application est un fork de ntfy-android dans lequel le transport HTTP est remplacé par Nostr : au lieu de sonder un serveur, nstrfy s'abonne à des événements kind `7741` sur des relays configurables et les affiche comme notifications Android natives.

Le modèle de notification supporte à la fois les payloads en clair et les payloads chiffrés [NIP-44](/fr/topics/nip-44/). Quand le chiffrement est activé, nstrfy utilise [Amber](https://github.com/greenart7c3/Amber) pour la signature via [NIP-55](/fr/topics/nip-55/) ou un nsec local. L'application importe les listes de relays depuis le profil utilisateur via [NIP-65](/fr/topics/nip-65/) et respecte l'expiration d'événements [NIP-40](/fr/topics/nip-40/). Le projet compagnon [nstrfy.sh](https://github.com/vcavallo/nstrfy.sh) fournit en plus un CLI bash et un client web hébergé sur [nstrfy.sh](https://nstrfy.sh).

### HAMSTR ajoute Reticulum pour Nostr sur mesh LoRa

[HAMSTR](https://github.com/LibertyFarmer/hamstr), le projet qui envoie des événements Nostr et des zaps Lightning sur la radio amateur, a fusionné [PR #10](https://github.com/LibertyFarmer/hamstr/pull/10) le 12 avril pour ajouter [Reticulum](https://reticulum.network/) comme backend de transport mesh. Reticulum est un protocole mesh cryptographique qui fonctionne sur LoRa, HF, VHF/UHF, liaisons série et TCP/IP. Avec cet ajout, HAMSTR peut relayer des événements Nostr à travers un mesh de matériels RNode sans infrastructure internet.

Les transports AX.25 Packet Radio et VARA HF restent disponibles. L'architecture zero-knowledge de HAMSTR signifie que le serveur relay ne voit jamais les clés privées, et sa conformité [NIP-57](/fr/topics/nip-57/) garantit que les zaps Lightning hors ligne apparaissent correctement dans des clients comme Amethyst et Primal. La même semaine, [PR #11](https://github.com/LibertyFarmer/hamstr/pull/11) a migré le frontend vers Svelte 5 et TailwindCSS v4.

## Sorties

### Bloom v0.1.0 livre un serveur Blossom auto-hébergé et un relay

[Bloom](https://github.com/nostrnative/bloom) a livré sa première release, [v0.1.0](https://github.com/nostrnative/bloom/releases/tag/v0.1.0), le 9 avril. Construit avec Tauri v2 et React 19, Bloom embarque un serveur média complet [Blossom](/fr/topics/blossom/) et un relay Nostr dans une seule application desktop pour macOS, Windows et Linux. Les utilisateurs obtiennent un stockage de fichiers souverain avec adressage de contenu SHA-256, support des métadonnées de fichier [NIP-94](/fr/topics/nip-94/) et résolution du schéma d'URI `blossom://` sans gérer eux-mêmes une infrastructure serveur.

### WaveFunc v0.1.0 et v0.1.1 lancent une radio internet Nostr

[WaveFunc](https://github.com/zeSchlausKwab/wavefunc) a livré [v0.1.0](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.0) et [v0.1.1](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.1) le 13 avril, se lançant comme annuaire et lecteur de radio internet basé sur Nostr. Le modèle de données s'appuie sur des kinds personnalisés : kind `31237` pour les stations, kind `30078` pour les favoris, kind `1311` pour le live chat et kind `1111` pour les commentaires de station. Le backend relay Khatru fournit le stockage SQLite et la recherche full-text Bluge avec support [NIP-50](/fr/topics/nip-50/).

WaveFunc embarque aussi un wallet Cashu [NIP-60](/fr/topics/nip-60/) et le support nutzap. La release [v0.1.1](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.1) ajoute des carrousels de genres, un popover de dons Lightning, la gestion des stations pour les utilisateurs authentifiés et une fiche Zapstore. Les builds sont disponibles sur macOS, Windows, Linux et Android via [wavefunc.live](https://wavefunc.live).

### Snort livre v0.5.0 à v0.5.3 avec durcissement sécurité et refonte des performances

[Snort](https://github.com/v0l/snort), le client web Nostr basé sur React, a livré trois releases de [v0.5.0](https://github.com/v0l/snort/releases/tag/v0.5.0) à [v0.5.3](https://github.com/v0l/snort/releases/tag/v0.5.3). La version v0.5.0 est la plus importante : audit de sécurité, vraie vérification des signatures Schnorr, protection [NIP-46](/fr/topics/nip-46/) contre les messages relay falsifiés, améliorations du chiffrement PIN et suppression de la confiance implicite dans la délégation NIP-26.

Les gains de performance incluent une vérification batchée des signatures en WASM, des routes chargées paresseusement, un chargeur de profils prioritaire réécrit et des optimisations worker-relay. La release ajoute aussi l'affichage des factures kind `7000` requises pour paiement pour les DVM [NIP-90](/fr/topics/nip-90/). [PR #620](https://github.com/v0l/snort/pull/620) retravaille en parallèle le système de messagerie pour réduire le coût du calcul de listes de chat.

### Primal Android livre 3.0.21 et repense la mise en page du flux

[Primal Android](https://github.com/PrimalHQ/primal-android-app) a livré [v3.0.21](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.21) avec des correctifs pour les votes zap de sondages, le partage multi-comptes du wallet et l'auto-reconnexion du signataire distant et du service wallet. Sept PRs fusionnées ont suivi : [PR #1008](https://github.com/PrimalHQ/primal-android-app/pull/1008) unifie la mise en page de l'écran principal, [PR #1010](https://github.com/PrimalHQ/primal-android-app/pull/1010) introduit un nouveau design de cartes de flux, [PR #1009](https://github.com/PrimalHQ/primal-android-app/pull/1009) ajoute le support vidéo dans les cartes média, [PR #1012](https://github.com/PrimalHQ/primal-android-app/pull/1012) ajoute un champ compact pour les réponses rapides, et [PR #1013](https://github.com/PrimalHQ/primal-android-app/pull/1013) repense les barres d'application.

### Nostria v3.1.19 à v3.1.21 ajoutent la génération locale d'images

[Nostria](https://github.com/nostria-app/nostria) a livré trois releases de [v3.1.19](https://github.com/nostria-app/nostria/releases/tag/v3.1.19) à [v3.1.21](https://github.com/nostria-app/nostria/releases/tag/v3.1.21) avec plus de 80 commits. La nouveauté principale est la génération locale d'images avec Janus Pro accéléré par WebGPU, de sorte que les utilisateurs puissent générer des images sur l'appareil sans API externe. Les releases ajoutent aussi la génération d'images cloud, le chat multimodal, le support ONNX runtime, une bibliothèque de prompts et la gestion du cache AI.

### TubeStr v1.0.3 livre des mises à jour du flux et du studio

[TubeStr](https://github.com/Tubestr/tubestr-v2), application privée de partage vidéo familial construite sur Nostr, a livré [v1.0.3](https://github.com/Tubestr/tubestr-v2/releases/tag/v1.0.3) le 13 avril. La release apporte des améliorations du flux et du studio. [PR #3](https://github.com/Tubestr/tubestr-v2/pull/3) revoit les écrans d'onboarding et [PR #2](https://github.com/Tubestr/tubestr-v2/pull/2) corrige une erreur d'export vidéo. L'application utilise NDK et MDK pour le partage média chiffré entre membres d'une famille.

## En développement

### Botburrow commence comme plateforme de bots Marmot

[Botburrow](https://github.com/marmot-protocol/botburrow) est un nouveau projet de l'équipe Marmot, démarré le 3 avril. Il s'agit d'une plateforme auto-hébergée de gestion de bots où chaque bot reçoit sa propre identité Nostr, rejoint des chats de groupe [Marmot](/fr/topics/marmot/) via des messages Welcome et envoie ou reçoit des messages chiffrés de bout en bout. Le tableau de bord, construit avec Rails 8.1, communique avec un unique daemon whitenoise-rs (`wnd`) via un socket Unix.

Le projet expose déjà une couche importante de scripts et d'opérations : commandes, triggers et actions planifiées exécutent du code Ruby personnalisé, les scripts peuvent inspecter profils, appartenance aux groupes et invitations en attente via `wnd`, et l'interface inclut une vue de chat live. Une [image Docker](https://github.com/marmot-protocol/botburrow/commit/2ed012078eaab3c5b92dff16b87865c2e353bd80) cible l'auto-hébergement sans configuration sur Umbrel et Start9.

### Nostr Archives ajoute un relay de flux tendances et la résolution d'entités

[Nostr Archives](https://github.com/barrydeen/nostrarchives-api), la plateforme d'archivage et d'analytics à [nostrarchives.com](https://nostrarchives.com), poursuit son développement côté [API](https://github.com/barrydeen/nostrarchives-api) en Rust et côté [frontend](https://github.com/barrydeen/nostrarchives-frontend) en Next.js 16. [PR #118](https://github.com/barrydeen/nostrarchives-api/pull/118) ajoute le filtrage par plage de temps au leaderboard client, [PR #117](https://github.com/barrydeen/nostrarchives-api/pull/117) ajoute des compteurs d'engagement sur les réponses, [PR #85](https://github.com/barrydeen/nostrarchives-frontend/pull/85) résout directement les entités Nostr depuis les chemins d'URL, et [PR #86](https://github.com/barrydeen/nostrarchives-frontend/pull/86) ajoute une page de documentation API.

### Damus corrige la timeline des favoris

[Damus](https://github.com/damus-io/damus), le client iOS, a fusionné [PR #3708](https://github.com/damus-io/damus/pull/3708) qui réécrit `subscribe_to_favorites()` avec filtrage sur place, reconstruction de la déduplication et persistance de l'onglet sélectionné.

### Nostur ajoute les zaps privés et l'affichage des emoji personnalisés

[Nostur](https://github.com/nostur-com/nostur-ios-public), le client iOS, a poussé 10 commits cette semaine ajoutant le support des zaps privés, l'affichage des emoji personnalisés, un correctif de rendu `.webp` animé et la détection du format audio des messages vocaux.

### Amber livre v6.0.1 à v6.0.3 avec sauvegarde WebDAV et correctifs de reconnexion relay

[Amber](https://github.com/greenart7c3/Amber), l'application signataire Android [NIP-55](/fr/topics/nip-55/), a livré trois versions. [v6.0.1](https://github.com/greenart7c3/Amber/releases/tag/v6.0.1) ajoute WebDAV et le partage vers Google Drive comme nouvelles options de sauvegarde, implémente un backoff exponentiel pour les reconnexions relay et met à jour Quartz. [v6.0.2](https://github.com/greenart7c3/Amber/releases/tag/v6.0.2) ajoute une option d'index de compte lors de l'usage des seed words, et [v6.0.3](https://github.com/greenart7c3/Amber/releases/tag/v6.0.3) corrige un problème d'ID de requête vide lors de la réception d'intents.

### Plektos v0.6.0 se repense avec des thèmes Ditto

[Plektos](https://github.com/derekross/plektos), la plateforme décentralisée de meetups et d'événements construite sur [NIP-52](/fr/topics/nip-52/), a livré [v0.6.0](https://github.com/derekross/plektos/commit/7a691cdf089ceb7a8582dd5c0ee026830f2cdc77) et [v0.6.1](https://github.com/derekross/plektos/commit/3a6474ae380522d8ee1b3526423fcfc3328fd879). La mise à jour ajoute des thèmes communautaires de style Ditto avec upload d'images d'arrière-plan, configuration de la forme des avatars et refonte de l'UI. [PR #6](https://github.com/derekross/plektos/pull/6) traite une revue de code complète couvrant sécurité, architecture et UX.

### Shadow ajoute une API Nostr OS et une app wallet Cashu

[Shadow](https://github.com/justinmoon/shadow), la plateforme runtime d'apps de Justin Moon, a poussé plus de 30 commits en deux jours. [Commit 88cbda5](https://github.com/justinmoon/shadow/commit/88cbda5131814d2730a2d892029932136db005df) ajoute une application wallet Cashu tournant dans le runtime Shadow, et [Commit 865c415](https://github.com/justinmoon/shadow/commit/865c415) ajoute une démo de lecteur de podcast. Le runtime expose `Shadow.os.nostr` et `Shadow.os.audio` comme API système de premier plan.

### Lief corrige la connexion Amber et ajoute Zapstore

[Lief](https://gitlab.com/chad.curtis/lief), application Nostr d'écriture de lettres longues, a livré le build `v2026.04.12`. La mise à jour corrige un problème de connexion au signataire [Amber](https://github.com/greenart7c3/Amber) sur Android, simplifie le flux de nudge du signataire, met à jour la dépendance nostrify et ajoute l'intégration Zapstore.

### Espy revoit complètement le sélecteur de couleurs et corrige la connexion Amber

[Espy](https://gitlab.com/chad.curtis/espy), application sociale Nostr où les utilisateurs partagent des « moments couleur », a livré le build `v2026.04.12`. La mise à jour remanie le sélecteur de couleurs avec un arc de saturation courbe, corrige des bugs de scintillement sur l'anneau de teinte et ajoute des personnages cachés. La release corrige aussi un problème de connexion Amber, simplifie le flux de nudge du signataire, met à jour nostrify et ajoute Zapstore.

### Jumble ajoute des filtres de kind par flux et un onglet Articles

[Jumble](https://github.com/CodyTseng/jumble) a poussé 13 commits ajoutant le filtrage par kind dans chaque flux, un onglet Articles, la synchronisation du statut lu des notifications avec une option préservant la vie privée, un mode de masquage d'avatar et un correctif de race condition lors du changement de compte.

### Primal Web livre 8 montées de version

[Primal Web](https://github.com/PrimalHQ/primal-web-app) a livré les versions 3.0.93 à 3.0.101 en une semaine avec 21 commits. Le travail s'est concentré sur l'amélioration du chat de live stream, des correctifs sur les frontières de mentions, la pagination des bookmarks, la prévention des likes dupliqués et des correctifs du relay proxy.

## Travail sur le protocole et les spécifications

### Mises à jour des NIP

Changements récents dans le [dépôt NIPs](https://github.com/nostr-protocol/nips) :

**Fusionnés :**

- **[NIP-34](/fr/topics/nip-34/) (Git Stuff) : ajout des URL de clone `nostr://`** ([PR #2312](https://github.com/nostr-protocol/nips/pull/2312)) : la spécification définit désormais trois formes d'URL `nostr://` pour référencer des dépôts NIP-34 de manière lisible ou directement par naddr. Cela permet à des helpers `git-remote-nostr` de résoudre un npub ou une adresse [NIP-05](https://github.com/nostr-protocol/nips/blob/master/05.md), de découvrir les relays du dépôt puis de récupérer les données git. La PR resserre aussi le format du tag `d` des identifiants de dépôt afin que ces URL produisent des URI valides.

**PRs ouvertes et discussions :**

- **NIP-63a : Minimal Payment Gateway Descriptor** ([PR #2315](https://github.com/nostr-protocol/nips/pull/2315)) : propose un événement remplaçable kind `10164` permettant aux créateurs de déclarer des passerelles de paiement, des modèles tarifaires et des règles d'abonnement pour l'accès à du contenu payant.
- **NIP-XX : Relay Self-Declaration Manifest and Retention Horizon** ([PR #2314](https://github.com/nostr-protocol/nips/pull/2314)) : propose un manifeste gossipable kind `10100` pour la transparence relay et un nouveau message relay-vers-client `HORIZON` qui annonce la borne temporelle la plus ancienne que le relay conserve.
- **NIP-TPLD : Transient Private Location Data** ([PR #2309](https://github.com/nostr-protocol/nips/pull/2309)) : propose le kind `20411` pour partager des données de géolocalisation chiffrées [NIP-44](/fr/topics/nip-44/) avec des destinataires spécifiques.
- **[NIP-5C](/fr/topics/nip-5c/) (Scrolls) : mise à jour des programmes WASM** ([PR #2281](https://github.com/nostr-protocol/nips/pull/2281)) : poursuit le travail sur la publication et l'exécution de binaires WASM distribués comme événements Nostr.
- **Support des gros payloads [NIP-44](/fr/topics/nip-44/)** ([PR #1907](https://github.com/nostr-protocol/nips/pull/1907)) : propose d'étendre NIP-44 au-delà de la limite actuelle de 65 535 bytes, en particulier pour les usages comme la signature distante [NIP-46](/fr/topics/nip-46/) de grosses contact lists kind `3`.
- **[NIP-C7](/fr/topics/nip-c7/) : restreindre le kind 9 aux vues de chat** ([PR #2310](https://github.com/nostr-protocol/nips/pull/2310)) : ajoute une exigence selon laquelle les clients qui rendent une « vue chat » comme flux d'événements ordonnés ne doivent récupérer que des événements kind `9`.

## Deep Dive NIP : NIP-29 (groupes basés sur les relays)

[NIP-29](https://github.com/nostr-protocol/nips/blob/master/29.md) définit un modèle de messagerie de groupe où le relay lui-même gère l'appartenance et la modération. Les groupes vivent sur un relay spécifique, identifié par une chaîne aléatoire, et le relay fait autorité pour décider qui peut écrire dans le groupe. C'est une architecture différente de [Marmot](/fr/topics/marmot/) ou des chats de groupe [NIP-17](/fr/topics/nip-17/) : ici, le relay peut lire les messages et la modération se fait au niveau du relay.

Un groupe est identifié par le format `<host>'<group-id>`, par exemple `groups.nostr.com'abcdef`. Les événements envoyés dans le groupe portent un tag `h` avec l'identifiant du groupe, et un tag `previous` peut référencer les premiers 8 caractères hexadécimaux d'événements récents vus sur le même relay pour détecter les rediffusions hors contexte. L'appartenance se gère via des événements de modération dans la plage `9000-9020`, comme les demandes d'adhésion kind `9021`, les suppressions kind `9001`, les changements de métadonnées kind `9002` et les événements de rôles kind `39003`.

Les groupes peuvent être publics, fermés ou totalement ouverts, et la lecture comme l'écriture peuvent être contrôlées indépendamment. La spécification accepte aussi d'autres kinds que le chat : articles [NIP-23](/fr/topics/nip-23/), événements calendrier [NIP-52](/fr/topics/nip-52/) ou lives [NIP-53](/fr/topics/nip-53/) peuvent tous participer au même espace de groupe. Pour des communautés publiques, ce modèle de confiance assumée côté relay est souvent suffisant ; pour la confidentialité de groupe, [Marmot](/fr/topics/marmot/) ou [NIP-17](/fr/topics/nip-17/) restent mieux adaptés.

## Deep Dive NIP : NIP-90 (Data Vending Machines)

[NIP-90](https://github.com/nostr-protocol/nips/blob/master/90.md) définit un protocole de calcul à la demande sur Nostr. Un client publie une demande de travail, des fournisseurs peuvent y répondre, et les résultats reviennent eux aussi comme événements Nostr. Les kinds `5000-5999` sont réservés aux demandes de jobs, les kinds `6000-6999` aux résultats et le kind `7000` au feedback d'état.

Une demande peut inclure des tags `i` pour les entrées, `param` pour les paramètres, `output` pour le format de sortie attendu, `bid` pour le plafond de paiement et des hints de relays pour le retour. Les fournisseurs peuvent demander un paiement avant exécution, publier des états `processing` ou `payment-required`, puis renvoyer un résultat du kind correspondant, toujours `1000` au-dessus du kind de la demande. Le protocole supporte aussi le chaînage de jobs, ce qui permet d'enchaîner transcription, résumé et traduction sans couche d'orchestration séparée.

---

C'est tout pour cette semaine. Vous construisez quelque chose ou vous avez des nouvelles à partager ? Envoyez-nous un DM sur Nostr ou retrouvez-nous sur [nostrcompass.org](https://nostrcompass.org).
