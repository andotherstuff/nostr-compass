---
title: 'Nostr Compass #13'
date: 2026-03-11
translationOf: /en/newsletters/2026-03-11-newsletter.md
translationDate: 2026-04-23
draft: false
type: newsletters
---

Bienvenue dans Nostr Compass, votre guide hebdomadaire sur Nostr.

**Cette semaine :** [Shopstr](https://github.com/shopstr-eng/shopstr) et [Milk Market](https://github.com/shopstr-eng/milk-market) ajoutent des surfaces MCP pour le commerce piloté par agents, tandis que [OAuth Bunker](https://github.com/flox1an/oauth-bunker), [Amber](https://github.com/greenart7c3/Amber) et [strfry](https://github.com/hoytech/strfry) ajoutent le relay-auth [NIP-42](/fr/topics/nip-42/) (Authentication of Clients to Relays) et le support des protected events à travers des logiciels d'application, de signer et de relay. [Route96](https://github.com/v0l/route96) livre deux versions autour de l'étiquetage IA, des files de modération, du perceptual hashing et d'une documentation serveur lisible par machine. [Samizdat](https://github.com/satsdisco/samizdat), déjà en ligne sur le web, a publié sa première alpha Android puis a ajouté le support signer [NIP-55](/fr/topics/nip-55/) (Android Signer Application). [Formstr](https://github.com/formstr-hq/nostr-forms) ajoute l'inscription via [NIP-49](/fr/topics/nip-49/) (Private Key Encryption), [Amethyst](https://github.com/vitorpamplona/amethyst) livre un travail de résolution [NIP-05](/fr/topics/nip-05/) (Domain Verification) fondé sur Namecoin, [Mostro](https://github.com/MostroP2P/mostro) publie [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4), et le dépôt des NIPs fusionne [NIP-91](/fr/topics/nip-91/) (AND Operator for Filters) ainsi que des recommandations défensives pour [NIP-66](/fr/topics/nip-66/) (Relay Discovery and Liveness Monitoring).

## Actualités

### Shopstr et Milk Market ouvrent des surfaces de commerce MCP

[Shopstr](https://github.com/shopstr-eng/shopstr), la marketplace pair à pair avec paiements Lightning et Cashu, a fusionné [PR #234](https://github.com/shopstr-eng/shopstr/pull/234) ([commit 94ef7d1](https://github.com/shopstr-eng/shopstr/commit/94ef7d1a4519e8e0158668d13c8cb8684b1d46e2)), ajoutant un serveur MCP avec authentification par clé d'API pour la gestion des comptes agents. Le changement ajoute `.well-known/agent.json` pour la découverte d'agents, des endpoints MCP d'onboarding et de statut, des routes de création de commande et de vérification de paiement, des outils dédiés à l'achat et à la lecture, ainsi qu'un écran de réglages pour les clés d'API. [PR #236](https://github.com/shopstr-eng/shopstr/pull/236) étend cela avec des actions côté vendeur pour les messages, les adresses, les mises à jour de commande et la sélection de spécifications produit. Un correctif de sécurité dans [PR #235](https://github.com/shopstr-eng/shopstr/pull/235) remplace le hachage SHA-256 des clés d'API en une seule itération par du PBKDF2 salé à 100 000 itérations.

Les agents peuvent lire des listings [NIP-99](/fr/topics/nip-99/) (Classified Listings) et passer par le checkout en utilisant les flux de paiement existants de [NIP-47](/fr/topics/nip-47/) (Nostr Wallet Connect) et [NIP-60](/fr/topics/nip-60/) (Cashu Wallet), sans scraper des pages ni reverse-engineerer le comportement du client.

[Milk Market](https://github.com/shopstr-eng/milk-market), une marketplace alimentaire sur Nostr accessible sur [milk.market](https://milk.market), a adopté la même base MCP et clé d'API dans [le commit da6c0b4](https://github.com/shopstr-eng/milk-market/commit/da6c0b499494b4e4861c4ff8a220e066c46285b3). [PR #10](https://github.com/shopstr-eng/milk-market/pull/10) ajoute les commandes par abonnement, la modification d'adresse de livraison après achat, et la gestion des checkouts multi-marchands et multi-devises pour Stripe et d'autres chemins de paiement fiat. Une [PR #11](https://github.com/shopstr-eng/milk-market/pull/11) corrige ensuite un bug d'initialisation de base de données au démarrage, où la table des publications relay échouées n'était pas créée sur une installation neuve, ce qui provoquait des erreurs 500 au premier chargement. L'interface côté agent fonctionne avec un checkout natif Bitcoin sur Shopstr ou un checkout mixte fiat et Bitcoin sur Milk Market.

### NIP-42 relay-auth à travers bunker, signer et relay

[OAuth Bunker](https://github.com/flox1an/oauth-bunker), un bunker [NIP-46](/fr/topics/nip-46/) (Nostr Connect) qui relie des fournisseurs OAuth à la signature Nostr, a ajouté la connexion [NIP-07](/fr/topics/nip-07/) (Browser Extension Signer), la sélection automatique quand une seule identité existe, et le nettoyage des identités supprimées ([commit f0c7683](https://github.com/flox1an/oauth-bunker/commit/f0c7683cb2374fd9a3ebd1b186055da8abd2c2ff)). Lorsqu'une seule identité existe, le bunker la sélectionne maintenant automatiquement au lieu d'afficher un choix. Supprimer une identité retire aussi ses assignations et connexions orphelines. Le [commit 6b8796c](https://github.com/flox1an/oauth-bunker/commit/6b8796c6c59c7d48dc1ede92d6de6bf54feb56cc) ajoute une voie de configuration `ALWAYS_ALLOWED_KINDS` pour les utilisateurs assignés, avec par défaut le kind `30078` pour les données spécifiques à une application, afin que les identités déléguées puissent écrire dans ce stockage sans approbation événement par événement.

[Amber](https://github.com/greenart7c3/Amber), le principal signer [NIP-55](/fr/topics/nip-55/) sur Android, a livré [v4.1.3-pre4](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3-pre4) dans une série de quatre pré-releases pendant la semaine. [PR #317](https://github.com/greenart7c3/Amber/pull/317) ajoute la gestion de l'authentification relay [NIP-42](/fr/topics/nip-42/) pour les requêtes de kind `22242`. L'implémentation ajoute une nouvelle colonne de base de données pour suivre les permissions spécifiques à un relay, avec un index unique sur `(pkKey, type, kind, relay)`. Les utilisateurs voient un écran d'auth dédié où ils peuvent autoriser ou refuser par relay ou pour tous les relays via un scope wildcard `*`, puis persister ce choix. Les permissions wildcard effacent toutes les entrées spécifiques à un relay pour un kind donné. [PR #318](https://github.com/greenart7c3/Amber/pull/318) poursuit en refactorant les écrans de requêtes multi-événements afin d'afficher les détails inline avec des cartes composables plutôt que de naviguer vers un écran séparé. La version met aussi à jour les relays de profil par défaut, ajoute un affichage des requêtes en bottom sheet et corrige un crash sur les appareils MediaTek en désactivant StrongBox keystore.

Côté relay, [strfry PR #156](https://github.com/hoytech/strfry/pull/156) implémente la gestion NIP-42 pour les [NIP-70](/fr/topics/nip-70/) (Protected Events), et [PR #176](https://github.com/hoytech/strfry/pull/176) rejette les reposts qui embarquent des protected events.

### Notedeck ajoute les limites de relay NIP-11 et des fonctionnalités Agentium

[Notedeck](https://github.com/damus-io/notedeck), le client desktop natif de l'équipe Damus, a fusionné 14 PRs cette semaine. [PR #1316](https://github.com/damus-io/notedeck/pull/1316) ajoute la récupération des limitations de relay [NIP-11](/fr/topics/nip-11/) (Relay Information Document), de sorte que tous les relays outbox respectent maintenant `max_message_length` et `max_subscriptions` depuis le relay info document. L'implémentation inclut un traitement en background jobs, un backoff exponentiel avec jitter pour les tentatives de reconnexion, et des en-têtes HTTP Accept personnalisés. [PR #1312](https://github.com/damus-io/notedeck/pull/1312) corrige un bug où les DMs échouaient parfois à se charger après un changement de compte, et [PR #1333](https://github.com/damus-io/notedeck/pull/1333) ajoute un mécanisme de backoff à la communication multicast avec les relays pour éviter le spam de diffusion en cas d'erreurs.

Le sous-système Agentium, l'UI d'agent de code intégrée à Notedeck, appelée en interne « Dave », a reçu le collage d'images depuis le presse-papiers, des configurations d'exécution nommées synchronisées entre appareils via des événements de kind `31991`, [NIP-33](/fr/topics/nip-33/) (Parameterized Replaceable Events), un créateur de git worktree et un sélecteur de modèle pour choisir les backends par session ([PR #1336](https://github.com/damus-io/notedeck/pull/1336)). [PR #1338](https://github.com/damus-io/notedeck/pull/1338) intègre `egui_kittest` pour des tests UI headless, et [PR #1339](https://github.com/damus-io/notedeck/pull/1339) ajoute une carte de tableau de bord suivant les nouvelles créations de listes de contacts par client. Une [PR #1314](https://github.com/damus-io/notedeck/pull/1314) encore ouverte porte la résolution Namecoin NIP-05 d'Amethyst dans Notedeck avec des requêtes ElectrumX, un routage Tor SOCKS5 et une intégration à la barre de recherche.

### diVine livre v1.0.6 avec une infrastructure de tests E2E et l'import NIP-49

[diVine](https://github.com/divinevideo/divine-mobile), le client vidéo court format en boucle qui restaure les archives Vine sur [divine.video](https://divine.video), a livré [v1.0.6](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.6) avec 127 PRs fusionnées. La version ajoute l'import de compte [NIP-49](/fr/topics/nip-49/), le support [NIP-05](/fr/topics/nip-05/) externe, la gestion multi-comptes, des builds macOS et Linux expérimentaux, ainsi qu'une bibliothèque de brouillons et de clips repensée, adossée au stockage local.

Côté ingénierie, [PR #1928](https://github.com/divinevideo/divine-mobile/pull/1928) ajoute une infrastructure complète de tests d'intégration E2E utilisant Patrol pour l'automatisation UI native face à une stack backend Docker, relay, API, Blossom, Postgres, Redis et ClickHouse. Cinq tests de parcours d'auth couvrent l'inscription, la vérification, la réinitialisation de mot de passe, l'expiration de session et le rafraîchissement de token. [PR #2105](https://github.com/divinevideo/divine-mobile/pull/2105) remplace le chargement vidéo HLS-first par du MP4 direct avec fallback HLS automatique, ce qui réduit les temps de chargement de 30 à 60 secondes à un niveau presque instantané. [PR #2076](https://github.com/divinevideo/divine-mobile/pull/2076) met en cache la réponse API du flux d'accueil dans SharedPreferences pour un affichage instantané au cold start. [PR #2104](https://github.com/divinevideo/divine-mobile/pull/2104) impose le masquage dans les flux des labels de contenu `ai-generated`, et [PR #2100](https://github.com/divinevideo/divine-mobile/pull/2100) ajoute un réglage de sécurité pour n'afficher que les vidéos hébergées par diVine. La migration du cache de profils de Hive vers Drift continue à travers [PR #1881](https://github.com/divinevideo/divine-mobile/pull/1881), [PR #1883](https://github.com/divinevideo/divine-mobile/pull/1883) et [PR #1903](https://github.com/divinevideo/divine-mobile/pull/1903), en remplaçant environ 1 074 lignes de code Hive par des DAOs Drift.

### Vector v0.3.2 livre la synchronisation negentropy NIP-77 et des améliorations MLS

[Vector](https://github.com/VectorPrivacy/Vector), une messagerie desktop axée sur la vie privée qui utilise le chiffrement de groupe MLS avec [NIP-17](/fr/topics/nip-17/) (Private Direct Messages) et [NIP-44](/fr/topics/nip-44/) (Encrypted Payloads), a livré [v0.3.2](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.2). Le changement principal est la negentropy NIP-77 pour la synchronisation de groupes MLS ([commit b06adf4](https://github.com/VectorPrivacy/Vector/commit/b06adf4af2673fb5ac5add01356999ea70628eac)), qui rattrape les messages manqués beaucoup plus vite grâce à un boot parallèle. La version ajoute aussi un moteur audio reconstruit avec support Linux complet, des spoilers d'image avec aperçus floutés, des hyperliens cliquables avec aperçus enrichis, des pings `@mention` avec `@everyone` pour les admins de groupe, l'autocomplétion des shortcodes emoji, la mise en sourdine de groupes, la réaction en un geste sur des réactions existantes, et des uploads de fichiers annulables. Vector filtre explicitement les événements de chat de groupe NIP-17 ([commit 2179a51](https://github.com/VectorPrivacy/Vector/commit/2179a51c0449b3a70663a1573195b7945adf58ba)), en utilisant MLS exclusivement pour le chiffrement de groupe.

## Versions

### Route96 v0.5.0 et v0.5.1

[Route96](https://github.com/v0l/route96), un serveur média compatible Blossom et [NIP-96](/fr/topics/nip-96/) (HTTP File Storage), a livré [v0.5.0](https://github.com/v0l/route96/releases/tag/v0.5.0) et [v0.5.1](https://github.com/v0l/route96/releases/tag/v0.5.1). v0.5.0 ajoute l'étiquetage IA automatisé, le backfill rétroactif des uploads non étiquetés, des files de modération pour les fichiers signalés, le rejet basé sur EXIF pour la vie privée, et la gestion de hash interdits.

v0.5.1 ajoute des hashes perceptuels d'image, du locality-sensitive hashing pour retrouver des images similaires, des endpoints admin par lots, et un [`SKILL.md`](https://github.com/v0l/route96/releases/tag/v0.5.1) publié décrivant la surface API Blossom et NIP-96 du serveur pour les outils d'agents. [PR #58](https://github.com/v0l/route96/pull/58) déplace les workers en arrière-plan vers des tâches Tokio entièrement asynchrones, et [le commit 97b00a3](https://github.com/v0l/route96/commit/97b00a39e27b07053c2ad335dbf475bacba57bf8) ajoute un backoff pour éviter des hot loops.

### Samizdat v1.0.0-alpha

[Samizdat](https://github.com/satsdisco/samizdat), lecteur et éditeur long format disponible sur [samizdat.press](https://samizdat.press), a livré son premier build Android dans [v1.0.0-alpha](https://github.com/satsdisco/samizdat/releases/tag/v1.0.0-alpha). L'application s'ouvre sur une page Press curatée d'articles Nostr long format, avec navigation par onglets entre Press, Feed, Saved et Write. Le build Android ajoute un stockage natif des clés via chiffrement Android Keystore avec déverrouillage biométrique, gère les URI `nostr:` et les deep links `samizdat.press`, et prend en charge le handoff de signer via le sélecteur d'applications Android, Amber, Primal, etc., au lieu d'exiger un import direct de clé. Le pull-to-refresh, la gestion des safe areas sur différentes tailles d'écran, et les intégrations natives de partage, presse-papiers, haptique et écran de démarrage font maintenant partie de la shell Android plutôt que du wrapper web.

[Le commit d17308f](https://github.com/satsdisco/samizdat/commit/d17308f3c2e6020e14074fbb1c03a8f60f29a3e6) ajoute la signature [NIP-55](/fr/topics/nip-55/) basée sur intents pour les parcours Amber et Primal, et [le commit e29dab8](https://github.com/satsdisco/samizdat/commit/e29dab84f7b58edd621f7b86ed7ca6458f965614) remplace un contournement JavaScript bridge par un plugin Capacitor natif utilisant `startActivityForResult`. L'application exige Android 7.0 ou plus, API 24, est distribuée sous forme d'APK debug dans cette alpha, et n'a toujours pas de notifications push. La publication dépend actuellement d'une application signer, tandis que la connexion par `nsec` couvre la lecture locale et l'accès au compte.

### Calendar by Form* v0.2.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar), une application de calendrier décentralisée avec partage d'événements privés [NIP-59](/fr/topics/nip-59/) (Gift Wrap) disponible sur [calendar.formstr.app](https://calendar.formstr.app), a livré [v0.2.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.0) avec [PR #38](https://github.com/formstr-hq/nostr-calendar/pull/38). La version étend la gestion des événements récurrents pour [NIP-52](/fr/topics/nip-52/) (Calendar Events), allant au-delà des fondations mono-événement de la v0.1.0. Les changements sous-jacents touchent aussi le stockage local des événements, la gestion des signers et le plumbing des notifications Android. C'est la deuxième application active de l'organisation Formstr après la migration de dépôt du mois dernier.

### Mostro v0.16.4

[Mostro](https://github.com/MostroP2P/mostro), la plateforme d'échange Bitcoin pair à pair construite sur Nostr, a publié [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4). Les correctifs de restauration de session de litige ([PR #599](https://github.com/MostroP2P/mostro/pull/599)) et de fermeture automatique ([PR #606](https://github.com/MostroP2P/mostro/pull/606)) [couverts la semaine dernière](/en/newsletters/2026-03-04-newsletter/) sont inclus. Nouveau dans cette version : [PR #625](https://github.com/MostroP2P/mostro/pull/625) ajoute un champ `days` aux événements d'évaluation utilisateur de kind `38384`, [PR #612](https://github.com/MostroP2P/mostro/pull/612) ajoute une expiration à ces événements d'évaluation, et [PR #614](https://github.com/MostroP2P/mostro/pull/614) fait passer les événements de commande vers des réglages d'expiration configurés au lieu d'une fenêtre codée en dur de 24 heures. [PR #622](https://github.com/MostroP2P/mostro/pull/622) ajoute une vérification d'idempotence pour empêcher les paiements en double des frais de développement.

### Mostro Mobile v1.2.1

[Mostro Mobile](https://github.com/MostroP2P/mobile), le client Flutter pour l'échange P2P Mostro, a livré [v1.2.1](https://github.com/MostroP2P/mobile/releases/tag/v1.2.1) avec 11 nouvelles fonctionnalités et 11 corrections de bugs. La version ajoute le rendu multimédia chiffré dans le chat de litige ([PR #514](https://github.com/MostroP2P/mobile/pull/514)), la fermeture automatique de l'UI de litige quand les commandes atteignent un état terminal ([PR #503](https://github.com/MostroP2P/mobile/pull/503)), le scan QR pour l'import wallet NWC ([commit 12eaee4](https://github.com/MostroP2P/mobile/commit/12eaee4d154fa31b07f82b96819de520e825aee6)), des traductions françaises, et la gestion des notifications push FCM. [PR #496](https://github.com/MostroP2P/mobile/pull/496) corrige un bug de padding de signature Schnorr en épinglant la dépendance bip340 à la v0.2.0.

### 0xchat v1.5.4

[0xchat](https://github.com/0xchat-app/0xchat-app-main), le client de messagerie type Telegram avec support Cashu, a livré [v1.5.4](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.4-release) centrée sur les correctifs Linux desktop : icônes de dock AppImage, rendu des emojis, gels des menus contextuels, et blocages UI sur répondre/copier. La version corrige aussi les problèmes d'upload d'image et l'intégration npub.cash. [PR #49](https://github.com/0xchat-app/0xchat-app-main/pull/49) élimine des rebuilds UI inutiles en supprimant un timer de polling de 3 secondes qui forçait des repaints glassmorphic sans rien faire, et débloque l'initialisation de connexion en lançant le chargement du cache d'événements en parallèle au lieu de bloquer le démarrage relay, contacts et canaux.

### Keep v0.6.0

[Keep](https://github.com/privkeyio/keep-android), un signer à seuil FROST pour Android avec support [NIP-55](/fr/topics/nip-55/) et [NIP-46](/fr/topics/nip-46/), a livré [v0.6.0](https://github.com/privkeyio/keep-android/releases/tag/v0.6.0) et [v0.6.1](https://github.com/privkeyio/keep-android/releases/tag/v0.6.1). v0.6.0 ajoute une UI de coordination et gestion de descripteurs de wallet, un flux de sauvegarde/restauration avec authentification biométrique ([PR #184](https://github.com/privkeyio/keep-android/pull/184)), la récupération de `nsec` à partir de threshold shares ([PR #187](https://github.com/privkeyio/keep-android/pull/187)), la génération cross-platform de cadres QR animés via Rust UniFFI ([PR #188](https://github.com/privkeyio/keep-android/pull/188)), et une piste d'audit de signature avec vérification de chaîne ([PR #189](https://github.com/privkeyio/keep-android/pull/189)). v0.6.1 remplace la licence AGPL-3.0 par MIT ([PR #191](https://github.com/privkeyio/keep-android/pull/191)).

### njump v0.3.0

[njump](https://github.com/fiatjaf/njump), la passerelle statique pour consulter du contenu Nostr sur [njump.me](https://njump.me), a livré [v0.3.0](https://github.com/fiatjaf/njump/releases/tag/v0.3.0) avec un changement cassant dans le parsing des codes `note1` et une mise à jour de la bibliothèque Nostr sous-jacente.

### Roadstr v0.1.1

[Roadstr](https://github.com/jooray/roadstr), une application décentralisée de signalement d'événements routiers utilisant Nostr, a livré sa première version démo [v0.1.1](https://github.com/jooray/roadstr/releases/tag/v0.1.1). L'application affiche les événements routiers sur une carte utilisant les vector tiles d'openfreemap.org.

### Bitcredit v0.5.3

[Bitcredit](https://github.com/BitcreditProtocol/Bitcredit-Core), une application d'e-bills avec couche de transport Nostr et relay dédié sur [bit.cr](https://www.bit.cr/), a livré [v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3). [PR #846](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846) ajoute les champs `payment_actions` et `bill_state` à l'API pour l'état de paiement et d'acceptation, et [PR #849](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849) corrige la gestion des adresses de signature pour les signers anonymes.

### OpenChat v0.1.0-alpha.3

[OpenChat](https://github.com/DavidGershony/openChat), une application de chat construite sur les bibliothèques .NET MLS et C# du protocole Marmot, a livré [v0.1.0-alpha.3](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.3). La version ajoute le support de signer externe pour Amber et les flux [NIP-46](/fr/topics/nip-46/) ([commit e568d97](https://github.com/DavidGershony/openChat/commit/e568d979fe15eead19172f2eb6f8cf26ca845247)), déplace la persistance de l'état MLS dans le service MLS pour éliminer les pertes de données dans la fenêtre de crash ([commit 4720bc8](https://github.com/DavidGershony/openChat/commit/4720bc8625136a0d5b0e23322bc0c50cd80577e8)), et publie des builds Windows, Linux et Android via un nouveau pipeline CI.

### OpenSignal v1.0.0

[OpenSignal](https://github.com/turizspace/opensignal), un copilot de trading Kotlin Multiplatform pour Nostr, a livré [v1.0.0](https://github.com/turizspace/OpenSignal/releases/tag/v1.0.0). La version assemble des modules KMP partagés pour la logique métier, le rendu de graphiques, l'authentification et la publication Nostr, le support d'upload Blossom [NIP-96](/fr/topics/nip-96/), et des hooks d'inférence IA fondés sur ONNX à travers les shells Desktop et Android. L'architecture publiée inclut aussi un service IA FastAPI pour l'analyse de captures d'écran de graphiques, des pipelines d'entraînement de modèles et un moteur de risque qui produit des plans de trade structurés avec sizing et avertissements. La connexion prend en charge soit des clés `nsec` brutes, soit des signers externes, et le flux de sortie se termine par la publication d'un événement Nostr plutôt qu'une analyse locale uniquement.

## Mises à jour des projets

### Formstr

[Formstr](https://github.com/formstr-hq/nostr-forms), l'alternative à Google Forms sur Nostr, a fusionné [PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) ([commit e9c4fd5](https://github.com/formstr-hq/nostr-forms/commit/e9c4fd5dadfa0b83f1e87d7596eaf35f9fdb7da8)), ajoutant un flux d'inscription qui utilise des clés privées chiffrées [NIP-49](/fr/topics/nip-49/) (Private Key Encryption). Avant ce changement, les utilisateurs avaient besoin soit d'une extension de navigateur [NIP-07](/fr/topics/nip-07/), soit de coller un `nsec` brut pour utiliser Formstr. Le nouveau flux génère une paire de clés côté client, chiffre la clé privée avec un mot de passe choisi par l'utilisateur via le schéma scrypt + XChaCha20-Poly1305 de NIP-49, puis stocke la chaîne `ncryptsec` obtenue. Les utilisateurs peuvent ensuite se reconnecter avec leur mot de passe sans installer d'extension signer. La gestion des clés reste côté client du début à la fin.

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst), le client Android riche en fonctionnalités, a fusionné quatre PRs qui livrent le travail de résolution [NIP-05](/fr/topics/nip-05/) soutenu par Namecoin, lequel était [encore ouvert la semaine dernière](/en/newsletters/2026-03-04-newsletter/). [PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734) ajoute une vérification NIP-05 résistante à la censure via ElectrumX pour les identifiants `.bit`, `d/` et `id/`. Quand Amethyst détecte l'un de ces suffixes dans un champ NIP-05, il interroge un serveur ElectrumX-NMC pour récupérer l'historique de transaction du nom, analyse le script `NAME_UPDATE` de la dernière sortie pour en extraire la pubkey Nostr, et rejette les noms plus anciens que 36 000 blocs, la fenêtre d'expiration de Namecoin. Les connexions ElectrumX passent par SOCKS5 lorsque Tor est activé, avec sélection dynamique entre des endpoints clearnet et `.onion`. Un cache LRU avec TTL d'une heure évite les requêtes blockchain répétées.

[PR #1771](https://github.com/vitorpamplona/amethyst/pull/1771) corrige des conditions de course et des erreurs de résolution dans ce flux. [PR #1785](https://github.com/vitorpamplona/amethyst/pull/1785) permet aux nouveaux utilisateurs d'importer une liste de suivis pendant l'inscription à partir d'identifiants NIP-05 ordinaires ou fondés sur Namecoin. [PR #1786](https://github.com/vitorpamplona/amethyst/pull/1786) ajoute des réglages de serveur ElectrumX personnalisés pour laisser les utilisateurs choisir le serveur chargé de leurs requêtes.

### nostr-idb

[nostr-idb](https://github.com/hzrd149/nostr-idb), une bibliothèque fournissant des méthodes utilitaires pour stocker des événements Nostr dans IndexedDB, a fusionné [PR #6](https://github.com/hzrd149/nostr-idb/pull/6) ajoutant le support des filtres de tags AND [NIP-91](/fr/topics/nip-91/). Le changement ajoute une sémantique d'intersection à la logique de matching côté client pour que les requêtes IndexedDB puissent exiger toutes les valeurs de tag listées plutôt qu'une seule. [PR #8](https://github.com/hzrd149/nostr-idb/pull/8) met la bibliothèque à jour vers la dernière interface NIP-DB, puis un [commit b49b3d3](https://github.com/hzrd149/nostr-idb/commit/b49b3d32c575ff8214dc3fb07675109c2a971972) corrige un deadlock sur `subscribe` et retire nostr-tools des dépendances de production.

### Pensieve

[Pensieve](https://github.com/andotherstuff/pensieve), un indexeur Nostr orienté archive avec analytique ClickHouse, a fusionné [PR #8](https://github.com/andotherstuff/pensieve/pull/8) ajoutant l'application de TTL de cache par entrée et la coalescence des misses par clé pour réduire les pics CPU de l'API. Les endpoints de séries temporelles les plus coûteux, statistiques d'engagement, activité horaire et activité par kind, utilisent maintenant des TTL serveur de 10 minutes au lieu de déclencher des recomputations synchronisées en tempête.

### Blossom

[Blossom](https://github.com/hzrd149/blossom), le protocole et la stack serveur d'hébergement média décentralisé, a fusionné deux mises à jour d'autorisation BUD-11. [PR #91](https://github.com/hzrd149/blossom/pull/91) déplace l'autorisation optionnelle dans son propre BUD et clarifie le rôle des tags `x` et `server`. [PR #93](https://github.com/hzrd149/blossom/pull/93) nettoie le comportement d'auth spécifique aux endpoints et formalise l'en-tête `X-SHA-256` pour la vérification d'upload. Les deux PRs consolident la logique d'auth dans BUD-11 et suppriment les ambiguïtés autour du hachage des requêtes pour l'upload, la suppression et les flux de gestion média.

## Mises à jour des NIP

Changements récents dans le [dépôt des NIPs](https://github.com/nostr-protocol/nips) :

**Fusionnés :**

- **[NIP-91](/fr/topics/nip-91/) (AND Operator for Filters)** ([PR #1365](https://github.com/nostr-protocol/nips/pull/1365)) : ajoute une sémantique d'intersection pour les filtres de tags, permettant aux relays de répondre à des requêtes qui exigent toutes les valeurs listées au lieu d'une seule. Cela réduit le post-filtrage côté client et la bande passante sur les requêtes riches en tags.

- **[NIP-66](/fr/topics/nip-66/) (Relay Discovery and Liveness Monitoring) : mesures défensives** ([PR #2240](https://github.com/nostr-protocol/nips/pull/2240)) : après le [travail de benchmark outbox couvert la semaine dernière](/en/newsletters/2026-03-04-newsletter/), la spécification ajoute maintenant des avertissements sur les chemins dégradés des données de monitoring relay. Les clients ne doivent pas exiger les événements de monitoring kind `30166` pour fonctionner. Un moniteur peut se tromper, être obsolète ou malveillant. Les clients doivent croiser les sources et éviter de couper de larges portions du graphe de relays d'un utilisateur sur la base d'un seul flux.

- **[NIP-39](/fr/topics/nip-39/) (External Identities in Profiles) : nettoyage du registre kind 10011** ([PR #2256](https://github.com/nostr-protocol/nips/pull/2256)) : ajoute directement la référence au kind `10011` dans la spécification, en l'alignant sur l'implémentation d'Amethyst [couverte la semaine dernière](/en/newsletters/2026-03-04-newsletter/).

**PRs ouvertes et discussions :**

- **[NIP-70](/fr/topics/nip-70/) (Protected Events) : rejeter les reposts qui embarquent des protected events** ([PR #2251](https://github.com/nostr-protocol/nips/pull/2251)) : si un relay applique NIP-70 sur l'événement d'origine mais accepte les reposts qui transportent le même contenu, le tag `-` n'a pas d'effet pratique. Cette PR ajoute la règle selon laquelle les relays doivent aussi rejeter les reposts kind 6 et kind 16 d'événements protégés. [strfry PR #176](https://github.com/hoytech/strfry/pull/176) l'implémente déjà.

- **[NIP-71](/fr/topics/nip-71/) (Video Events) : pistes audio multiples** ([PR #2255](https://github.com/nostr-protocol/nips/pull/2255)) : ajoute des tags `imeta` audio pour les pistes alternatives, variantes linguistiques et flux audio-only. Un client pourrait conserver un fichier vidéo stable tout en changeant la langue audio, ou servir l'audio comme piste séparée pour un contenu de type podcast.

- **[NIP-11](/fr/topics/nip-11/) (Relay Information Document) et attributs de relay [NIP-66](/fr/topics/nip-66/)** ([PR #2257](https://github.com/nostr-protocol/nips/pull/2257)) : ajoute un champ structuré `attributes` aux relay information documents, offrant aux clients et outils de découverte des métadonnées lisibles par machine au-delà de la description en texte libre actuelle.

## NIP Deep Dive : NIP-49 (Private Key Encryption)

[NIP-49](/fr/topics/nip-49/) définit comment un client chiffre une clé privée avec un mot de passe et encode le résultat sous forme de chaîne bech32 `ncryptsec`. [Formstr](#formstr) utilise NIP-49 dans son nouveau flux d'inscription.

Le format n'est pas lié à un kind d'événement dédié. Un client part de la clé privée secp256k1 brute de 32 octets, dérive une clé symétrique à partir du mot de passe utilisateur avec scrypt, chiffre la clé avec XChaCha20-Poly1305, puis encapsule le résultat dans une chaîne bech32 `ncryptsec`. Un flag d'un octet enregistre si la clé est connue comme ayant été manipulée de manière non sûre avant chiffrement.

```json
{
  "id": "4d47f4f0a6f6edbc1bbd7f4e2a45ec68f27cba91d6c6ab5cf28d8d87b0f3d57e",
  "pubkey": "1f8b4c3e7b0f9451d4f9b8a7c6e5d4c3b2a1908f7e6d5c4b3a29181716151413",
  "created_at": 1741699200,
  "kind": 30078,
  "tags": [
    ["d", "encrypted-key-backup"],
    ["format", "ncryptsec"],
    ["encryption", "nip49"]
  ],
  "content": "ncryptsec1qgg9947rlpvqu76pj5ecreduf9jxhselq2nae2kghhvd5g7dgjtcxfqtd67p9m0w57lspw8gsq6yphnm8623nsl8xn9j4jdzz84zm3frztj3z7s35vpzmqf6ksu8r89qk5z2zxfmu5gv8th8wclt0h4p",
  "sig": "6a8f6e4b2d1901735f0ad4b6e8c1f3a579d0e2b4c6f8a1d3e5f7091b2c3d4e5f11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

L'événement JSON ci-dessus est un exemple au niveau application, pas une exigence de NIP-49. Le NIP standardise le format de clé chiffrée. Un client peut stocker la chaîne `ncryptsec` localement, la synchroniser via un stockage spécifique à l'application, ou l'exporter comme chaîne de sauvegarde. Les mots de passe sont normalisés en Unicode NFKC avant la dérivation de clé afin que le même mot de passe déchiffre de manière cohérente entre clients et plateformes.

Le flag de sécurité de clé sur un octet a trois valeurs définies : `0x00` signifie que l'historique de manipulation de la clé est inconnu, `0x01` signifie que la clé est connue pour avoir été manipulée de manière non sûre, par exemple collée en clair dans un formulaire web avant chiffrement, et `0x02` signifie que la clé a été générée et chiffrée dans un contexte sûr sans jamais être exposée. Les clients peuvent utiliser cela pour afficher des avertissements lors de l'import de clés dont l'historique est connu comme non sûr.

NIP-49 protège mieux les clés qu'un export `nsec` en clair, mais le chiffrement n'est aussi fort que le mot de passe et le coût scrypt configuré. Des valeurs `LOG_N` plus élevées compliquent le brute force offline mais ralentissent aussi les opérations légitimes de déchiffrement. La spécification met en garde contre la publication de clés chiffrées sur des relays publics, puisque les attaquants bénéficient de la collecte de ciphertext pour le cracking offline. À titre de comparaison, la signature distante [NIP-46](/fr/topics/nip-46/) évite entièrement d'exposer les clés, tandis que la signature Android [NIP-55](/fr/topics/nip-55/) garde les clés dans une application signer dédiée. NIP-49 occupe un autre créneau : la sauvegarde chiffrée portable pour les utilisateurs qui gèrent eux-mêmes leurs clés.

Les implémentations incluent [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) pour l'inscription, [Amber](https://github.com/greenart7c3/Amber) pour la sauvegarde et la restauration `ncryptsec`, [diVine v1.0.6](#divine-livre-v106-avec-une-infrastructure-de-tests-e2e-et-limport-nip-49) pour l'import de compte, [Keep v0.6.0](#keep-v060) pour l'export de FROST shares, et des outils de gestion de clés comme [nsec.app](https://nsec.app) et [Alby](https://github.com/getAlby/hub).

## NIP Deep Dive : NIP-70 (Protected Events)

[NIP-70](/fr/topics/nip-70/) définit les protected events. Quand un événement porte le tag `["-"]`, un relay doit le rejeter sauf si le relay exige une authentification [NIP-42](/fr/topics/nip-42/) et que la pubkey authentifiée correspond à l'auteur de l'événement.

Le flux d'auth NIP-42 fonctionne comme suit : le relay envoie un challenge `AUTH` contenant une chaîne aléatoire, puis le client répond avec un événement kind `22242` signé dont les tags incluent l'URL du relay et le challenge. Le relay vérifie la signature et contrôle que la pubkey de l'événement d'auth correspond à la pubkey de l'événement protégé en cours de publication. Si les pubkeys ne correspondent pas, le relay rejette l'événement avec le préfixe de message `restricted`.

Le contenu de l'événement peut malgré tout rester public. Le tag `-` ne contrôle que qui peut publier l'événement sur un relay qui respecte ce tag. Cela couvre les flux semi-fermés de [NIP-29](/fr/topics/nip-29/) (Simple Groups), les espaces relay réservés aux membres, et d'autres contextes où l'auteur veut limiter la redistribution via le graphe des relays. NIP-70 est une convention à tag unique, pas un nouveau kind d'événement, donc n'importe quel kind existant peut porter le tag `-`.

```json
{
  "id": "cb8feca582979d91fe90455867b34dbf4d65e4b86e86b3c68c368ca9f9eef6f2",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1707409439,
  "kind": 1,
  "tags": [
    ["-"]
  ],
  "content": "hello members of the secret group",
  "sig": "fa163f5cfb75d77d9b6269011872ee22b34fb48d23251e9879bb1e4ccbdd8aaaf4b6dc5f5084a65ef42c52fbcde8f3178bac3ba207de827ec513a6aa39fa684c"
}
```

Même si un relay bloque la publication tierce de l'événement original, quelqu'un peut toujours republier le contenu dans un repost. [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) traite ce problème en imposant aux relays de rejeter aussi les reposts kind 6 et kind 16 d'événements protégés. [strfry PR #156](https://github.com/hoytech/strfry/pull/156) ajoute la gestion NIP-42 pour les protected events, et [strfry PR #176](https://github.com/hoytech/strfry/pull/176) bloque les reposts qui embarquent du contenu protégé.

NIP-70 contrôle le comportement des relays. Un destinataire peut toujours recopier le contenu ailleurs, et la spécification le dit explicitement. Le tag `-` donne aux relays un signal lisible par machine leur permettant de refuser une republication. À titre de comparaison, [NIP-62](/fr/topics/nip-62/) (Request to Vanish) demande aux relays de supprimer des données après coup, tandis que NIP-70 empêche une publication non autorisée dès l'ingestion. Les deux sont complémentaires : un auteur peut marquer des événements comme protégés pour limiter leur diffusion, puis demander plus tard une suppression s'il souhaite que le contenu disparaisse des relays qui l'ont accepté.

---

C'est tout pour cette semaine. Vous construisez quelque chose ou vous avez des nouvelles à partager ? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contactez-nous via DM [NIP-17](/fr/topics/nip-17/)</a> ou retrouvez-nous sur Nostr.
