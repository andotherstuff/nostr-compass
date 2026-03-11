---
title: 'Nostr Compass #13'
date: 2026-03-11
translationOf: /en/newsletters/2026-03-11-newsletter.md
translationDate: 2026-03-11
draft: false
type: newsletters
---

Bienvenue dans Nostr Compass, votre guide hebdomadaire sur Nostr.

**Cette semaine :** [Shopstr](https://github.com/shopstr-eng/shopstr) et [Milk Market](https://github.com/shopstr-eng/milk-market) ajoutent des surfaces MCP pour le commerce piloté par des agents, tandis que [OAuth Bunker](https://github.com/flox1an/oauth-bunker), [Amber](https://github.com/greenart7c3/Amber) et [strfry](https://github.com/hoytech/strfry) ajoutent la prise en charge relay-auth et des événements protégés de [NIP-42](/fr/topics/nip-42/) (Authentification des clients auprès des relais) à travers des logiciels d'application, de signataire et de relay. [Route96](https://github.com/v0l/route96) livre deux versions autour de l'étiquetage AI, des files de modération, du perceptual hashing et de documents serveur lisibles par machine. [Samizdat](https://github.com/satsdisco/samizdat), déjà en ligne sur le web, a publié sa première alpha Android puis a ajouté le support de signataire [NIP-55](/fr/topics/nip-55/) (Application de signature Android). [Formstr](https://github.com/formstr-hq/nostr-forms) ajoute l'inscription via [NIP-49](/fr/topics/nip-49/) (Chiffrement de clé privée), [Amethyst](https://github.com/vitorpamplona/amethyst) livre un travail de résolution [NIP-05](/fr/topics/nip-05/) (Vérification de domaine) basé sur Namecoin, [Mostro](https://github.com/MostroP2P/mostro) publie [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4), et le dépôt NIPs fusionne [NIP-91](/fr/topics/nip-91/) (Opérateur AND pour les filtres) ainsi qu'un guidage défensif pour [NIP-66](/fr/topics/nip-66/) (Découverte et surveillance de la disponibilité des relais).

## Actualités

### Shopstr et Milk Market ouvrent des surfaces de commerce MCP

[Shopstr](https://github.com/shopstr-eng/shopstr), la marketplace pair-à-pair avec paiements Lightning et Cashu, a fusionné [PR #234](https://github.com/shopstr-eng/shopstr/pull/234) ([commit 94ef7d1](https://github.com/shopstr-eng/shopstr/commit/94ef7d1a4519e8e0158668d13c8cb8684b1d46e2)), ajoutant un serveur MCP avec authentification par clé API pour la gestion de comptes d'agents. Le changement ajoute `.well-known/agent.json` pour la découverte d'agents, des endpoints MCP d'onboarding et de statut, des routes de création de commande et de vérification de paiement, des outils dédiés d'achat et de lecture, ainsi qu'un écran de paramètres pour les clés API. [PR #236](https://github.com/shopstr-eng/shopstr/pull/236) étend cela avec des actions côté vendeur pour les messages, les adresses, les mises à jour de commandes et la sélection de spécifications produit. Un correctif de sécurité dans [PR #235](https://github.com/shopstr-eng/shopstr/pull/235) remplace le hachage SHA-256 à une seule itération des clés API par PBKDF2 salé à 100 000 itérations.

Les agents peuvent lire des annonces [NIP-99](/fr/topics/nip-99/) (Annonces classées) et passer par le checkout en utilisant les flux de paiement existants [NIP-47](/fr/topics/nip-47/) (Nostr Wallet Connect) et [NIP-60](/fr/topics/nip-60/) (Cashu Wallet) sans scraper des pages ni rétroconcevoir le comportement du client.

[Milk Market](https://github.com/shopstr-eng/milk-market), une marketplace alimentaire sur Nostr à [milk.market](https://milk.market), a intégré la même base MCP et clé API dans [commit da6c0b4](https://github.com/shopstr-eng/milk-market/commit/da6c0b499494b4e4861c4ff8a220e066c46285b3). [PR #10](https://github.com/shopstr-eng/milk-market/pull/10) ajoute les commandes par abonnement, les changements d'adresse de livraison après achat et la gestion du checkout multi-marchands et multi-devises pour Stripe et d'autres parcours de paiement fiat. Une [PR #11](https://github.com/shopstr-eng/milk-market/pull/11) de suivi corrige un bug d'initialisation de base de données au démarrage où la table des publications relay échouées n'était pas créée sur une installation fraîche, provoquant des erreurs 500 au premier chargement. L'interface exposée aux agents fonctionne avec un checkout natif Bitcoin sur Shopstr ou un checkout mixte fiat et Bitcoin sur Milk Market.

### L'auth relay NIP-42 arrive dans bunker, signataire et relay

[OAuth Bunker](https://github.com/flox1an/oauth-bunker), un bunker [NIP-46](/fr/topics/nip-46/) (Nostr Connect) qui fait le pont entre des fournisseurs OAuth et la signature Nostr, a ajouté la connexion [NIP-07](/fr/topics/nip-07/) (Signataire par extension navigateur), la sélection automatique d'une identité unique et le nettoyage des identités supprimées ([commit f0c7683](https://github.com/flox1an/oauth-bunker/commit/f0c7683cb2374fd9a3ebd1b186055da8abd2c2ff)). Lorsqu'une seule identité existe, le bunker la sélectionne maintenant automatiquement au lieu de demander. Supprimer une identité enlève aussi ses affectations et connexions orphelines. [Commit 6b8796c](https://github.com/flox1an/oauth-bunker/commit/6b8796c6c59c7d48dc1ede92d6de6bf54feb56cc) ajoute un chemin de configuration `ALWAYS_ALLOWED_KINDS` pour les utilisateurs assignés, avec kind `30078` de données spécifiques à l'application par défaut, afin que les identités déléguées puissent écrire dans ce stockage sans approbation événement par événement.

[Amber](https://github.com/greenart7c3/Amber), le principal signataire [NIP-55](/fr/topics/nip-55/) pour Android, a publié [v4.1.3-pre4](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3-pre4) avec quatre préversions pendant la semaine. [PR #317](https://github.com/greenart7c3/Amber/pull/317) ajoute la gestion de l'authentification relay [NIP-42](/fr/topics/nip-42/) pour les requêtes de kind `22242`. L'implémentation ajoute une nouvelle colonne de base de données pour suivre les permissions spécifiques à un relay avec un index unique sur `(pkKey, type, kind, relay)`. Les utilisateurs voient un écran d'auth dédié où ils peuvent autoriser ou refuser par relay ou sur tous les relays avec un scope joker `*`, puis conserver ce choix. Les permissions joker effacent toutes les entrées spécifiques à un relay pour un kind. [PR #318](https://github.com/greenart7c3/Amber/pull/318) poursuit ensuite avec une refactorisation des écrans de requêtes multi-événements pour afficher les détails en ligne avec des cartes composables au lieu de naviguer vers un écran séparé. La version met aussi à jour les relays de profil par défaut, ajoute un affichage des requêtes en bottom sheet et corrige un crash sur les appareils MediaTek en désactivant le keystore StrongBox.

Côté relay, [strfry PR #156](https://github.com/hoytech/strfry/pull/156) implémente la gestion de l'auth NIP-42 pour [NIP-70](/fr/topics/nip-70/) (Événements protégés), et [PR #176](https://github.com/hoytech/strfry/pull/176) rejette les reposts qui intègrent des événements protégés.

### Notedeck ajoute les limites de relay de NIP-11 et des fonctionnalités Agentium

[Notedeck](https://github.com/damus-io/notedeck), le client desktop natif de l'équipe Damus, a fusionné 14 PRs cette semaine. [PR #1316](https://github.com/damus-io/notedeck/pull/1316) ajoute la récupération des limites de relay [NIP-11](/fr/topics/nip-11/) (Document d'information du relais), de sorte que tous les relays outbox respectent désormais `max_message_length` et `max_subscriptions` issus du document d'information du relay. L'implémentation inclut un traitement en jobs d'arrière-plan, un exponential backoff avec jitter pour les tentatives de reconnexion, et des en-têtes HTTP Accept personnalisés. [PR #1312](https://github.com/damus-io/notedeck/pull/1312) corrige un bug où les DMs échouaient parfois à se charger après un changement de compte, et [PR #1333](https://github.com/damus-io/notedeck/pull/1333) ajoute un mécanisme de backoff à la communication multicast avec les relays pour éviter le spam de broadcast en cas d'erreurs.

Le sous-système Agentium (l'UI d'agent de code intégrée à Notedeck, appelée en interne « Dave ») a reçu le collage d'images depuis le presse-papiers, des configurations d'exécution nommées qui se synchronisent entre appareils via des événements de kind `31991` ([NIP-33](/fr/topics/nip-33/) (Événements remplaçables paramétrés)), un créateur de git worktree et un sélecteur de modèle pour choisir des backends par session ([PR #1336](https://github.com/damus-io/notedeck/pull/1336)). [PR #1338](https://github.com/damus-io/notedeck/pull/1338) intègre `egui_kittest` pour les tests UI headless, et [PR #1339](https://github.com/damus-io/notedeck/pull/1339) ajoute une carte de tableau de bord suivant les nouvelles créations de listes de contacts par client. Une [PR #1314](https://github.com/damus-io/notedeck/pull/1314) ouverte porte le travail de résolution Namecoin NIP-05 d'Amethyst vers Notedeck avec des lookups ElectrumX, du routage Tor SOCKS5 et une intégration dans la barre de recherche.

### diVine publie v1.0.6 avec une infrastructure de tests E2E et l'import NIP-49

[diVine](https://github.com/divinevideo/divine-mobile), le client vidéo en boucle courte qui restaure les archives Vine à [divine.video](https://divine.video), a publié [v1.0.6](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.6) avec 127 PRs fusionnées. La version ajoute l'import de compte [NIP-49](/fr/topics/nip-49/), le support externe [NIP-05](/fr/topics/nip-05/), la gestion multi-comptes, des builds macOS et Linux expérimental, ainsi qu'une bibliothèque de brouillons et clips repensée reposant sur le stockage local.

Sur le plan de l'ingénierie, [PR #1928](https://github.com/divinevideo/divine-mobile/pull/1928) ajoute une infrastructure complète de tests d'intégration E2E utilisant Patrol pour l'automatisation UI native contre une stack backend Docker (relay, API, Blossom, Postgres, Redis, ClickHouse). Cinq tests de parcours d'auth couvrent l'inscription, la vérification, la réinitialisation de mot de passe, l'expiration de session et le rafraîchissement de token. [PR #2105](https://github.com/divinevideo/divine-mobile/pull/2105) fait passer le chargement vidéo de HLS-first à MP4 direct avec repli HLS automatique, réduisant les temps de chargement de 30-60 secondes à presque instantané. [PR #2076](https://github.com/divinevideo/divine-mobile/pull/2076) met en cache la réponse API du flux d'accueil dans SharedPreferences pour un affichage instantané à froid. [PR #2104](https://github.com/divinevideo/divine-mobile/pull/2104) impose que les contenus étiquetés `ai-generated` soient masqués dans les flux, et [PR #2100](https://github.com/divinevideo/divine-mobile/pull/2100) ajoute un réglage de sécurité pour n'afficher que les vidéos hébergées par diVine. La migration du cache de profils de Hive vers Drift continue à travers [PR #1881](https://github.com/divinevideo/divine-mobile/pull/1881), [PR #1883](https://github.com/divinevideo/divine-mobile/pull/1883) et [PR #1903](https://github.com/divinevideo/divine-mobile/pull/1903), remplaçant environ 1 074 lignes de code Hive par des DAO Drift.

### Vector v0.3.2 apporte la synchronisation negentropy NIP-77 et des améliorations MLS

[Vector](https://github.com/VectorPrivacy/Vector), une messagerie desktop axée sur la vie privée qui utilise le chiffrement de groupe MLS avec [NIP-17](/fr/topics/nip-17/) (Messages directs privés) et [NIP-44](/fr/topics/nip-44/) (Payloads chiffrés), a publié [v0.3.2](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.2). Le changement principal est la negentropy NIP-77 pour la synchronisation de groupes MLS ([commit b06adf4](https://github.com/VectorPrivacy/Vector/commit/b06adf4af2673fb5ac5add01356999ea70628eac)), qui rattrape les messages manqués beaucoup plus vite grâce à un boot parallèle. La version ajoute aussi un moteur audio reconstruit avec support Linux complet, des spoilers d'images avec aperçus floutés, des hyperliens cliquables avec aperçus enrichis, des pings `@mention` avec `@everyone` pour les administrateurs de groupe, l'autocomplétion des shortcodes emoji, le muting de groupes, la réaction par tap sur des réactions existantes et des uploads de fichiers annulables. Vector filtre explicitement les événements de chat de groupe NIP-17 ([commit 2179a51](https://github.com/VectorPrivacy/Vector/commit/2179a51c0449b3a70663a1573195b7945adf58ba)), en utilisant MLS exclusivement pour le chiffrement de groupe.

## Versions

### Route96 v0.5.0 et v0.5.1

[Route96](https://github.com/v0l/route96), un serveur média qui supporte Blossom et [NIP-96](/fr/topics/nip-96/) (Stockage de fichiers HTTP), a publié [v0.5.0](https://github.com/v0l/route96/releases/tag/v0.5.0) et [v0.5.1](https://github.com/v0l/route96/releases/tag/v0.5.1). v0.5.0 ajoute l'étiquetage AI automatisé, le backfill rétroactif pour les uploads non étiquetés, des files de modération pour les fichiers signalés, le rejet de confidentialité basé sur EXIF et la gestion des hashes interdits.

v0.5.1 ajoute des hashes perceptuels d'image, du locality-sensitive hashing pour la recherche d'images similaires, des endpoints d'administration batch et un [`SKILL.md`](https://github.com/v0l/route96/releases/tag/v0.5.1) publié décrivant la surface API Blossom et NIP-96 du serveur pour l'outillage d'agents. [PR #58](https://github.com/v0l/route96/pull/58) déplace les workers d'arrière-plan vers des tâches Tokio entièrement async, et [commit 97b00a3](https://github.com/v0l/route96/commit/97b00a39e27b07053c2ad335dbf475bacba57bf8) ajoute du backoff pour éviter les hot loops.

### Samizdat v1.0.0-alpha

[Samizdat](https://github.com/satsdisco/samizdat), un lecteur et éditeur long format disponible à [samizdat.press](https://samizdat.press), a publié son premier build Android dans [v1.0.0-alpha](https://github.com/satsdisco/samizdat/releases/tag/v1.0.0-alpha). L'application s'ouvre sur une page Press curatée d'articles Nostr long format avec une navigation par onglets inférieurs entre Press, Feed, Saved et Write. Le build Android ajoute un stockage natif des clés via chiffrement Android Keystore avec déverrouillage biométrique, gère les URI `nostr:` et les deep links `samizdat.press`, et supporte le handoff vers un signataire via le sélecteur d'app Android (Amber, Primal, etc.) au lieu d'exiger un import direct de clé. Le pull-to-refresh, la gestion des safe areas sur différentes tailles d'écran, ainsi que les intégrations natives de partage, presse-papiers, haptics et splash screen font désormais partie de la coque Android plutôt que du wrapper web.

[Commit d17308f](https://github.com/satsdisco/samizdat/commit/d17308f3c2e6020e14074fbb1c03a8f60f29a3e6) ajoute la signature [NIP-55](/fr/topics/nip-55/) basée sur les intents pour les flux Amber et Primal, et [commit e29dab8](https://github.com/satsdisco/samizdat/commit/e29dab84f7b58edd621f7b86ed7ca6458f965614) remplace un contournement via pont JavaScript par un plugin Capacitor natif utilisant `startActivityForResult`. L'application exige Android 7.0+ (API 24), est livrée comme APK debug dans cette alpha et n'a toujours pas de notifications push. La publication dépend actuellement d'une application signataire, tandis que la connexion `nsec` couvre la lecture locale et l'accès au compte.

### Calendar by Form* v0.2.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar), une application de calendrier décentralisée avec partage privé d'événements [NIP-59](/fr/topics/nip-59/) (Gift Wrap) disponible sur [calendar.formstr.app](https://calendar.formstr.app), a publié [v0.2.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.0) avec [PR #38](https://github.com/formstr-hq/nostr-calendar/pull/38). La version étend la gestion des événements récurrents pour [NIP-52](/fr/topics/nip-52/) (Événements de calendrier), dépassant la fondation mono-événement de v0.1.0. Les changements sous-jacents touchent aussi le stockage local des événements, la gestion des signataires et la plomberie des notifications Android. Il s'agit de la deuxième application active de l'organisation Formstr après la migration du dépôt le mois dernier.

### Mostro v0.16.4

[Mostro](https://github.com/MostroP2P/mostro), l'échange Bitcoin pair-à-pair construit sur Nostr, a publié [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4). Les correctifs de restauration de session de litige ([PR #599](https://github.com/MostroP2P/mostro/pull/599)) et de fermeture automatique ([PR #606](https://github.com/MostroP2P/mostro/pull/606)) [couverts la semaine dernière](/fr/newsletters/2026-03-04-newsletter/) sont inclus. Nouveauté de cette version : [PR #625](https://github.com/MostroP2P/mostro/pull/625) ajoute un champ `days` aux événements d'évaluation utilisateur de kind `38384`, [PR #612](https://github.com/MostroP2P/mostro/pull/612) ajoute une expiration à ces événements d'évaluation, et [PR #614](https://github.com/MostroP2P/mostro/pull/614) fait passer les événements de commande à des paramètres d'expiration configurés au lieu d'une fenêtre codée en dur de 24 heures. [PR #622](https://github.com/MostroP2P/mostro/pull/622) ajoute un contrôle d'idempotence pour empêcher les paiements dupliqués de frais de développement.

### Mostro Mobile v1.2.1

[Mostro Mobile](https://github.com/MostroP2P/mobile), le client Flutter pour l'échange P2P Mostro, a publié [v1.2.1](https://github.com/MostroP2P/mobile/releases/tag/v1.2.1) avec 11 nouvelles fonctionnalités et 11 corrections de bugs. La version ajoute le rendu multimédia chiffré dans le chat de litige ([PR #514](https://github.com/MostroP2P/mobile/pull/514)), la fermeture automatique de l'UI de litige lorsque les commandes atteignent un état terminal ([PR #503](https://github.com/MostroP2P/mobile/pull/503)), le scan QR pour l'import de portefeuille NWC ([commit 12eaee4](https://github.com/MostroP2P/mobile/commit/12eaee4d154fa31b07f82b96819de520e825aee6)), les traductions françaises et la gestion des notifications push FCM. [PR #496](https://github.com/MostroP2P/mobile/pull/496) corrige un bug de padding de signature Schnorr en figeant la dépendance bip340 à v0.2.0.

### 0xchat v1.5.4

[0xchat](https://github.com/0xchat-app/0xchat-app-main), le client de messagerie de style Telegram avec support Cashu, a publié [v1.5.4](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.4-release) centré sur des correctifs Linux desktop : icônes de dock AppImage, rendu emoji, gels du menu contextuel, et blocages UI sur répondre/copier. La version corrige aussi des problèmes d'upload d'images et l'intégration npub.cash. [PR #49](https://github.com/0xchat-app/0xchat-app-main/pull/49) élimine des reconstructions UI inutiles en supprimant un timer de polling de 3 secondes qui forçait des repaints glassmorphiques sans rien faire, et débloque l'initialisation de connexion en chargeant le cache d'événements de manière concurrente au lieu de bloquer le démarrage du relay, des contacts et des canaux.

### Keep v0.6.0

[Keep](https://github.com/privkeyio/keep-android), un signataire à seuil FROST pour Android avec support [NIP-55](/fr/topics/nip-55/) et [NIP-46](/fr/topics/nip-46/), a publié [v0.6.0](https://github.com/privkeyio/keep-android/releases/tag/v0.6.0) et [v0.6.1](https://github.com/privkeyio/keep-android/releases/tag/v0.6.1). v0.6.0 ajoute la coordination de descripteurs de wallet et l'UI de gestion, un flux de backup/restore avec authentification biométrique ([PR #184](https://github.com/privkeyio/keep-android/pull/184)), la récupération `nsec` à partir de parts de seuil ([PR #187](https://github.com/privkeyio/keep-android/pull/187)), la génération multiplateforme de cadres QR animés via Rust UniFFI ([PR #188](https://github.com/privkeyio/keep-android/pull/188)), et une piste d'audit de signature avec vérification de chaîne ([PR #189](https://github.com/privkeyio/keep-android/pull/189)). v0.6.1 fait passer la licence d'AGPL-3.0 à MIT ([PR #191](https://github.com/privkeyio/keep-android/pull/191)).

### njump v0.3.0

[njump](https://github.com/fiatjaf/njump), la passerelle statique pour consulter le contenu Nostr sur [njump.me](https://njump.me), a publié [v0.3.0](https://github.com/fiatjaf/njump/releases/tag/v0.3.0) avec un changement cassant dans l'analyse du code `note1` et une mise à jour de la bibliothèque nostr sous-jacente.

### Roadstr v0.1.1

[Roadstr](https://github.com/jooray/roadstr), une application décentralisée de signalement d'événements routiers utilisant Nostr, a publié sa première version de démonstration [v0.1.1](https://github.com/jooray/roadstr/releases/tag/v0.1.1). L'application affiche les événements routiers sur une carte en utilisant des vector tiles de openfreemap.org.

### Bitcredit v0.5.3

[Bitcredit](https://github.com/BitcreditProtocol/Bitcredit-Core), une application de facture électronique avec une couche de transport Nostr et un relay dédié sur [bit.cr](https://www.bit.cr/), a publié [v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3). [PR #846](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846) ajoute des champs `payment_actions` et `bill_state` à l'API pour l'état de paiement et d'acceptation, et [PR #849](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849) corrige la gestion des adresses de signature pour les signataires anonymes.

### OpenChat v0.1.0-alpha.3

[OpenChat](https://github.com/DavidGershony/openChat), une application de chat construite sur les bibliothèques .NET MLS et C# du protocole Marmot, a publié [v0.1.0-alpha.3](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.3). La version ajoute le support de signataires externes pour Amber et les flux [NIP-46](/fr/topics/nip-46/) ([commit e568d97](https://github.com/DavidGershony/openChat/commit/e568d979fe15eead19172f2eb6f8cf26ca845247)), déplace la persistance de l'état MLS dans le service MLS afin d'éliminer les pertes de données dans les fenêtres de crash ([commit 4720bc8](https://github.com/DavidGershony/openChat/commit/4720bc8625136a0d5b0e23322bc0c50cd80577e8)), et publie des builds Windows, Linux et Android via une nouvelle pipeline CI.

### OpenSignal v1.0.0

[OpenSignal](https://github.com/turizspace/opensignal), un copilot de trading Kotlin Multiplatform pour Nostr, a publié [v1.0.0](https://github.com/turizspace/OpenSignal/releases/tag/v1.0.0). La version regroupe des modules KMP partagés pour la logique métier, le rendu de graphiques, l'authentification et la publication Nostr, le support d'upload Blossom [NIP-96](/fr/topics/nip-96/) et des hooks d'inférence AI basés sur ONNX à travers des shells Desktop et Android. L'architecture publiée inclut aussi un service AI FastAPI pour l'analyse de captures d'écran de graphiques, des pipelines d'entraînement de modèles, et un moteur de risque produisant des plans de trade structurés avec sizing et avertissements. La connexion supporte soit des clés `nsec` brutes soit des signataires externes, et le flux de sortie se termine par la publication d'événements Nostr plutôt qu'une analyse uniquement locale.

## Mises à jour des projets

### Formstr

[Formstr](https://github.com/formstr-hq/nostr-forms), l'alternative à Google Forms sur Nostr, a fusionné [PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) ([commit e9c4fd5](https://github.com/formstr-hq/nostr-forms/commit/e9c4fd5dadfa0b83f1e87d7596eaf35f9fdb7da8)), ajoutant un flux d'inscription utilisant des clés privées chiffrées [NIP-49](/fr/topics/nip-49/) (Chiffrement de clé privée). Avant ce changement, les utilisateurs avaient besoin soit d'une extension navigateur [NIP-07](/fr/topics/nip-07/), soit d'un collage brut de `nsec` pour utiliser Formstr. Le nouveau flux génère une paire de clés côté client, chiffre la clé privée avec un mot de passe choisi par l'utilisateur via le schéma scrypt + XChaCha20-Poly1305 de NIP-49, et stocke la chaîne `ncryptsec` résultante. Les utilisateurs peuvent ensuite se reconnecter avec leur mot de passe sans installer d'extension signataire. La gestion des clés reste entièrement côté client.

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst), le client Android riche en fonctionnalités, a fusionné quatre PRs livrant le travail de résolution [NIP-05](/fr/topics/nip-05/) basé sur Namecoin qui était [ouvert la semaine dernière](/fr/newsletters/2026-03-04-newsletter/). [PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734) ajoute une vérification NIP-05 résistante à la censure via ElectrumX pour les identifiants `.bit`, `d/` et `id/`. Lorsqu'Amethyst détecte l'un de ces suffixes dans un champ NIP-05, il interroge un serveur ElectrumX-NMC pour l'historique de transactions du nom, analyse le script `NAME_UPDATE` de la dernière sortie pour extraire la pubkey Nostr, et rejette les noms plus anciens que 36 000 blocs (la fenêtre d'expiration de Namecoin). Les connexions ElectrumX passent par SOCKS5 lorsque Tor est activé, avec sélection dynamique de serveur entre des endpoints clearnet et `.onion`. Un cache LRU avec un TTL d'une heure évite les requêtes blockchain répétées.

[PR #1771](https://github.com/vitorpamplona/amethyst/pull/1771) corrige des conditions de course et la justesse du resolver dans ce flux. [PR #1785](https://github.com/vitorpamplona/amethyst/pull/1785) permet aux nouveaux utilisateurs d'importer une liste de suivis pendant l'inscription à partir d'identifiants NIP-05 ordinaires ou adossés à Namecoin. [PR #1786](https://github.com/vitorpamplona/amethyst/pull/1786) ajoute des paramètres personnalisés de serveur ElectrumX pour que les utilisateurs puissent choisir quel serveur effectue leurs lookups.

### nostr-idb

[nostr-idb](https://github.com/hzrd149/nostr-idb), une bibliothèque fournissant des méthodes utilitaires pour stocker des événements Nostr dans IndexedDB, a fusionné [PR #6](https://github.com/hzrd149/nostr-idb/pull/6) ajoutant le support des filtres de tags AND [NIP-91](/fr/topics/nip-91/). Le changement ajoute une sémantique d'intersection au matching des filtres côté client afin que les requêtes IndexedDB puissent exiger toutes les valeurs de tags listées plutôt qu'une seule. [PR #8](https://github.com/hzrd149/nostr-idb/pull/8) met à jour la bibliothèque vers la dernière interface NIP-DB, et un [commit b49b3d3](https://github.com/hzrd149/nostr-idb/commit/b49b3d32c575ff8214dc3fb07675109c2a971972) de suivi corrige un deadlock de souscription et supprime nostr-tools comme dépendance de production.

### Pensieve

[Pensieve](https://github.com/andotherstuff/pensieve), un indexeur Nostr archive-first avec analytics ClickHouse, a fusionné [PR #8](https://github.com/andotherstuff/pensieve/pull/8) ajoutant l'application d'un TTL de cache par entrée et la coalescence des misses par clé pour réduire les pics CPU de l'API. Les endpoints de séries temporelles les plus coûteux (statistiques d'engagement, activité horaire, activité par kind) utilisent maintenant des TTL côté serveur de 10 minutes au lieu de déclencher des tempêtes de recomputation synchronisées.

### Blossom

[Blossom](https://github.com/hzrd149/blossom), le protocole et la stack serveur d'hébergement média décentralisé, a fusionné deux mises à jour d'autorisation BUD-11. [PR #91](https://github.com/hzrd149/blossom/pull/91) déplace l'autorisation optionnelle dans son propre BUD et clarifie le rôle des tags `x` et `server`. [PR #93](https://github.com/hzrd149/blossom/pull/93) nettoie le comportement d'auth spécifique aux endpoints et formalise l'en-tête `X-SHA-256` pour la vérification des uploads. Les deux PRs consolident la logique d'auth dans BUD-11 et retirent des ambiguïtés autour du hachage des requêtes pour les flux d'upload, de suppression et de gestion média.

## Mises à jour des NIP

Changements récents dans le [dépôt NIPs](https://github.com/nostr-protocol/nips) :

**Fusionnés :**

- **[NIP-91](/fr/topics/nip-91/) (Opérateur AND pour les filtres)** ([PR #1365](https://github.com/nostr-protocol/nips/pull/1365)) : Ajoute une sémantique d'intersection pour les filtres de tags, permettant aux relays de répondre à des requêtes qui exigent toutes les valeurs de tags listées plutôt qu'une seule. Réduit le post-filtrage côté client et la bande passante pour les requêtes riches en tags.

- **[NIP-66](/fr/topics/nip-66/) (Découverte et surveillance de la disponibilité des relais): Defensive Measures** ([PR #2240](https://github.com/nostr-protocol/nips/pull/2240)) : À la suite du [travail de benchmark sur l'outbox couvert la semaine dernière](/fr/newsletters/2026-03-04-newsletter/), la spécification ajoute maintenant des avertissements sur les chemins dégradés des données de monitoring de relay. Les clients ne doivent pas exiger des événements de monitoring de kind `30166` pour fonctionner. Un moniteur peut se tromper, être obsolète ou malveillant. Les clients sont censés croiser les sources et éviter de couper de grandes parties du graphe de relays d'un utilisateur sur la base d'un seul flux.

- **[NIP-39](/fr/topics/nip-39/) (Identités externes dans les profils) : nettoyage du registre kind 10011** ([PR #2256](https://github.com/nostr-protocol/nips/pull/2256)) : Ajoute directement la référence au kind `10011` dans la spécification, en l'alignant avec l'implémentation d'Amethyst [couverte la semaine dernière](/fr/newsletters/2026-03-04-newsletter/).

**PRs ouvertes et discussions :**

- **[NIP-70](/fr/topics/nip-70/) (Événements protégés) : rejeter les reposts qui intègrent des événements protégés** ([PR #2251](https://github.com/nostr-protocol/nips/pull/2251)) : Si un relay applique NIP-70 sur l'événement d'origine mais accepte des reposts portant le même contenu, le tag `-` n'a aucun effet pratique. Cette PR ajoute la règle selon laquelle les relays doivent aussi rejeter les reposts de kind 6 et kind 16 d'événements protégés. [strfry PR #176](https://github.com/hoytech/strfry/pull/176) l'implémente déjà.

- **[NIP-71](/fr/topics/nip-71/) (Événements vidéo) : pistes audio multiples** ([PR #2255](https://github.com/nostr-protocol/nips/pull/2255)) : Ajoute des tags audio `imeta` pour des pistes alternatives, des variantes de langue et des flux audio-only. Un client pourrait conserver un fichier vidéo stable tout en changeant de langue audio, ou servir l'audio comme piste séparée pour un contenu de type podcast.

- **[NIP-11](/fr/topics/nip-11/) (Document d'information du relais) et [NIP-66](/fr/topics/nip-66/) attributs de relay** ([PR #2257](https://github.com/nostr-protocol/nips/pull/2257)) : Ajoute un champ structuré `attributes` aux documents d'information de relay, donnant aux clients et aux outils de découverte des métadonnées lisibles par machine au-delà de la description en texte libre actuelle.

## Analyse approfondie du NIP : NIP-49 (chiffrement de clé privée)

[NIP-49](/fr/topics/nip-49/) définit comment un client chiffre une clé privée avec un mot de passe et encode le résultat sous forme de chaîne bech32 `ncryptsec`. [Formstr](#formstr) utilise NIP-49 dans son nouveau flux d'inscription.

Le format n'est pas lié à un kind d'événement dédié. Un client part de la clé privée secp256k1 brute de 32 octets, dérive une clé symétrique à partir du mot de passe de l'utilisateur avec scrypt, chiffre la clé avec XChaCha20-Poly1305, puis encapsule le résultat dans une chaîne bech32 `ncryptsec`. Un indicateur d'un octet enregistre si la clé a déjà été connue comme ayant été manipulée de manière non sûre avant le chiffrement.

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

L'événement JSON ci-dessus est un exemple au niveau de l'application, pas une exigence de NIP-49. Le NIP standardise le format de clé chiffrée. Un client peut stocker le `ncryptsec` localement, le synchroniser via un stockage spécifique à l'application ou l'exporter comme chaîne de sauvegarde. Les mots de passe sont normalisés en Unicode NFKC avant la dérivation de clé afin que le même mot de passe se déchiffre de façon cohérente entre clients et plateformes.

L'indicateur de sécurité de clé d'un octet a trois valeurs définies : `0x00` signifie que l'historique de manipulation de la clé est inconnu, `0x01` signifie que la clé est connue pour avoir été manipulée de manière non sûre (par exemple collée en clair dans un formulaire web avant chiffrement), et `0x02` signifie que la clé a été générée et chiffrée dans un contexte sûr et n'a jamais été exposée. Les clients peuvent s'en servir pour afficher des avertissements lorsqu'ils importent des clés avec un historique connu comme non sûr.

NIP-49 protège mieux les clés qu'un export `nsec` en clair, mais le chiffrement n'est solide qu'à hauteur du mot de passe et du coût scrypt configuré. Des valeurs `LOG_N` plus élevées rendent les tentatives hors ligne plus difficiles, mais ralentissent aussi les opérations de déchiffrement légitimes. La spécification met en garde contre la publication de clés chiffrées sur des relays publics, car les attaquants profitent de la collecte de ciphertext pour le cassage hors ligne. À titre de comparaison, la signature distante [NIP-46](/fr/topics/nip-46/) évite complètement d'exposer les clés, et la signature Android [NIP-55](/fr/topics/nip-55/) garde les clés dans une application signataire dédiée. NIP-49 occupe une autre place : une sauvegarde chiffrée portable pour des utilisateurs qui gèrent eux-mêmes leurs clés.

Les implémentations incluent [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) pour l'inscription, [Amber](https://github.com/greenart7c3/Amber) pour la sauvegarde et la restauration `ncryptsec`, [diVine v1.0.6](#divine-publie-v106-avec-une-infrastructure-de-tests-e2e-et-limport-nip-49) pour l'import de compte, [Keep v0.6.0](#keep-v060) pour l'export de parts FROST, ainsi que des outils de gestion de clés comme [nsec.app](https://nsec.app) et [Alby](https://github.com/getAlby/hub).

## Analyse approfondie du NIP : NIP-70 (événements protégés)

[NIP-70](/fr/topics/nip-70/) définit les événements protégés. Lorsqu'un événement porte le tag `["-"]`, un relay doit le rejeter sauf si le relay exige l'authentification [NIP-42](/fr/topics/nip-42/) et que la pubkey authentifiée correspond à l'auteur de l'événement.

Le flux d'auth NIP-42 fonctionne comme suit : le relay envoie un challenge `AUTH` contenant une chaîne aléatoire, et le client répond avec un événement signé de kind `22242` dont les tags incluent l'URL du relay et le challenge. Le relay vérifie la signature et contrôle que la pubkey dans l'événement d'auth correspond à la pubkey dans l'événement protégé en cours de publication. Si les pubkeys ne correspondent pas, le relay rejette l'événement avec un préfixe de message `restricted`.

Le contenu de l'événement peut malgré tout rester public. Le tag `-` contrôle seulement qui peut publier l'événement sur un relay qui respecte ce tag. Cela couvre des flux semi-fermés [NIP-29](/fr/topics/nip-29/) (Groupes basés sur les relais), des espaces relay réservés aux membres, et d'autres contextes où l'auteur veut limiter la redistribution à travers le graphe de relays. NIP-70 est une convention à tag unique, pas un nouveau kind d'événement, donc n'importe quel kind existant peut porter le tag `-`.

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

Même si un relay bloque la publication par des tiers de l'événement d'origine, quelqu'un peut republier le contenu à l'intérieur d'un repost. [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) traite ce problème en exigeant que les relays rejettent aussi les reposts de kind 6 et kind 16 d'événements protégés. [strfry PR #156](https://github.com/hoytech/strfry/pull/156) ajoute la gestion de l'auth NIP-42 pour les événements protégés, et [strfry PR #176](https://github.com/hoytech/strfry/pull/176) bloque les reposts qui intègrent du contenu protégé.

NIP-70 contrôle le comportement du relay. Un destinataire peut encore copier le contenu ailleurs, et la spécification le dit explicitement. Le tag `-` donne aux relays un signal lisible par machine pour refuser la republication. À titre de comparaison, [NIP-62](/fr/topics/nip-62/) (Requêtes de disparition) demande aux relays de supprimer des données après coup, tandis que NIP-70 empêche la publication non autorisée au moment de l'ingestion. Les deux sont complémentaires : un auteur peut marquer des événements comme protégés pour limiter leur diffusion, puis demander plus tard leur suppression s'il veut que le contenu soit retiré des relays qui l'ont accepté.

---

C'est tout pour cette semaine. Vous construisez quelque chose ou vous avez des nouvelles à partager ? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contactez-nous via un DM [NIP-17](/fr/topics/nip-17/)</a> ou retrouvez-nous sur Nostr.
