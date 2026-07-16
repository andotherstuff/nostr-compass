---
title: "Nostr Compass #31"
date: 2026-07-15
publishDate: 2026-07-15
translationOf: /en/newsletters/2026-07-15-newsletter.md
translationDate: 2026-07-15
draft: false
type: newsletters
description: "Vector v0.4.0 retire Marmot pour les chats de groupe au profit du protocole ouvert Concord et livre Concord v2 quelques jours plus tard, Amethyst fusionne sa propre implémentation indépendante de Concord, Sonar se sépare de Bitchat avec une alpha multiplateforme et une spécification de packs de stickers, Divine Mobile 1.0.16 livre le chiffrement au repos et la provenance ProofMode, Bitchat 1.7.0 ajoute la voix push-to-talk en direct, et MDK v0.9.4 borne la connexion par signeur externe."
---

Bon retour sur Nostr Compass, votre guide hebdomadaire sur Nostr.

**Cette semaine :** [Vector v0.4.0](#vector-v040-moves-group-chats-from-marmot-to-concord-and-amethyst-ships-its-own-concord-client-days-later) retire [Marmot](/fr/topics/marmot/) comme transport par défaut pour les Group Chats au profit de [Concord](/fr/topics/concord-protocol/), un protocole communautaire ouvert sous licence MIT également utilisé par Armada de Soapbox, et livre Concord v2 quatre jours plus tard avec un sélecteur de commandes slash pour les bots, un minuteur d'autodestruction et les badges NIP-58. [Amethyst fusionne sa propre implémentation Concord indépendante et compatible au niveau du protocole](#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities) la même semaine. [Sonar](#sonar-splits-off-from-bitchat-with-a-cross-platform-alpha-and-a-sticker-pack-spec) se sépare de Bitchat avec une alpha multiplateforme et est la source de spécification citée pour la proposition de kinds de packs de stickers de cette semaine. [Divine Mobile 1.0.16](#divine-mobile-1016-ships-a-deeper-video-editor-at-rest-encryption-and-proofmode-provenance) livre un éditeur vidéo plus complet, le chiffrement au repos et la provenance ProofMode qui survit aux téléchargements de clips filigranés. [Bitchat v1.7.0](#bitchat-v170-adds-live-push-to-talk-voice-for-dms-and-the-public-mesh) ajoute la voix push-to-talk en direct pour les DMs et le push-to-talk signé sur le mesh public. [MDK v0.9.4](#mdk-v094-bounds-external-signer-login-and-adds-draft-persistence) borne la connexion par signeur externe et ajoute la persistance des brouillons, poursuivant sa passe de durcissement la même semaine où Vector s'éloigne de la spécification pour le chat de groupe.

Les versions taguées apportent [n_cord v1.1](#n_cord-v11-adds-nsec-bunker-support) ajoutant le support NSEC Bunker, [cdk v0.17.3](#cdk-v0173-adds-nip-47-wallet-service-support-across-cdk-cdk-nwc-and-cdk-ffi) ajoutant le support du service de portefeuille NIP-47 à travers cdk, cdk-nwc et cdk-ffi, [Coop Mobile v0.2.4](#coop-mobile-v024-improves-nostr-connect-and-adds-ncryptsec1-import) améliorant Nostr Connect et ajoutant l'import ncryptsec1, [Nmail v0.14.0](#nmail-v0140-ships-on-macos-with-scheduled-send-and-push-notifications) arrivant sur macOS avec l'envoi programmé, [Nostrord v2.2.0](#nostrord-v220-adds-a-dm-master-toggle-and-richer-direct-messages) ajoutant un interrupteur principal pour les DMs, [Nostr WoT 0.3.86](#nostr-wot-0386-hardens-key-backups-and-signing-prompts) durcissant les sauvegardes de clés au format NIP-49, [Keep Android v1.1.8](#keep-android-v118-adds-first-run-frost-onboarding) ajoutant l'onboarding FROST au premier lancement, [Noscall v0.6.0](#noscall-v060-adds-a-cashu-wallet-and-relay-based-push-notifications) ajoutant un portefeuille Cashu et les notifications push via relay, [Kubo](#kubo-ships-tablet-mode-and-group-chat-photos) ajoutant le mode tablette et les photos en chat de groupe, et [Nostr Codex Phone v0.2.9](#nostr-codex-phone-v029-adds-gitdiffread-file-helper-requests) ajoutant les requêtes d'aide git, diff et lecture de fichier.

Du côté des changements non publiés, [Amethyst](#amethyst-lets-accounts-nickname-contacts-with-encrypted-nip-85-cards) permet aux comptes de donner des surnoms aux contacts avec des cartes NIP-85 chiffrées à travers 54 PRs fusionnées, [Zap Cooking](#zap-cooking-ships-my-kitchen-phase-3-and-fixes-an-ndk-pool-quorum-bug) livre My Kitchen Phase 3 et corrige un bug de quorum de pool NDK, [Kehto](#kehto-streams-outbox-reads-before-relay-discovery) diffuse les lectures outbox avant la fin de la découverte de relays, [Wired et TAO](#wired-and-tao-add-nip-57-creator-revenue-sharing) ajoutent le partage de revenus créateur NIP-57, [Conduit Mono](#conduit-mono-rebuilds-the-merchant-orders-inbox-around-ephemeral-guest-checkout) reconstruit sa boîte de réception de commandes marchandes autour du paiement invité éphémère, [Buzz](#buzz-hardens-channel-creator-provisioning-around-kind-39002) durcit le provisionnement du créateur de canal à travers 240 PRs fusionnées, et [Nostr Docs](#nostr-docs-adopts-a-nip-49-signer-with-multi-account-and-qr-pairing) adopte un signeur NIP-49 avec multi-compte et appairage QR. Nouvellement suivis cette semaine : [OpenDiscord v1.0.1](#opendiscord-v101-launches-as-a-discord-style-client-on-nostr), [Auditable Voting v0.1.140](#auditable-voting-v01140-aligns-organiser-voter-and-audit-proxy-roles), et le choix Découverte [Cambium v0.3.2](#cambium-v032-pairs-with-heartwood-as-a-keyless-nip-55-signer), un signeur NIP-55 sans clé qui redirige vers un compagnon matériel Heartwood.

Le dépôt NIPs ne fusionne rien au cours de la dernière semaine et ouvre six propositions : [kind:10011 ensembles de suivi favoris](#open-kind10011-favorite-follow-sets), un [drive privé chiffré étendant NIP-4E](#open-private-encrypted-drive-extends-nip-4e), [NIP-DA partage de données privées avec permissions](#open-nip-da-permissioned-private-data-sharing), [kinds de packs de stickers 10031 et 30031](#open-sticker-pack-kinds-10031-and-30031), [épinglage de messages NIP-29](#open-nip-29-message-pinning-with-kind9010-and-kind39005), et une [restructuration de la découverte de relays NIP-66](#open-nip-66-relay-discovery-restructure). L'analyse approfondie couvre [NIP-99 et l'extension commerce Gamma Markets](#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension).

---

## Articles principaux

### Vector v0.4.0 fait passer les Group Chats de Marmot à Concord, et Amethyst livre son propre client Concord quelques jours plus tard

[Vector](https://github.com/VectorPrivacy/Vector) est un messager Nostr construit autour d'un client à binaire unique, axé sur la vie privée, pour les DMs et les chats de groupe. [Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) réécrit le moteur de messagerie de l'application en une bibliothèque partagée `vector-core` et, dans la même version, retire [Marmot](/fr/topics/marmot/) (MLS-over-Nostr) comme transport par défaut pour les Group Chats au profit de [Concord](/fr/topics/concord-protocol/), un protocole communautaire chiffré de bout en bout ; l'historique existant des groupes Marmot n'est pas transféré, et les notes de version demandent aux utilisateurs de sauvegarder toute donnée de groupe Marmot avant la mise à jour. Les propres notes de version de Vector décrivent Concord comme « our custom messaging protocol », mais les [spécifications CORD-01 à CORD-07](https://github.com/concord-protocol/concord) sous-jacentes sont publiées séparément, sous licence MIT, et déjà implémentées en dehors de Vector : le client de type Discord de Soapbox, [Armada](https://gitlab.com/soapbox-pub/armada), construit sa fonctionnalité Communities sur la même spécification Concord, et un jour plus tard, [Amethyst a fusionné sa propre implémentation Concord indépendante et compatible au niveau du protocole](https://github.com/vitorpamplona/amethyst/pull/3566), couverte en détail ci-dessous. La même version de Vector ajoute le routage Tor optionnel pour tout le trafic, la connexion par signeur distant [NIP-46](/fr/topics/nip-46/) par QR ou URI bunker collée, les comptes multiples avec un sélecteur intégré, et les packs d'emoji personnalisés partagés entre clients. La suppression de message retire un message pour les deux côtés dans les DMs et les chats de groupe, et Vector garde délibérément la clé de signature éphémère au lieu de suivre le flux de suppression standard [NIP-17](/fr/topics/nip-17/), un écart motivé par la vie privée que le projet signale explicitement dans les notes de version. Quatre jours plus tard, [v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1) livre **Concord v2**, décrit comme apportant des améliorations majeures de confidentialité et de stabilité aux Communities tout en gardant celles existantes fonctionnelles, aux côtés d'un sélecteur de commandes slash de type Discord pour les bots avec des paramètres typés, d'un minuteur d'autodestruction par chat, et d'un système de badges NIP-58 pour les chasseurs de bugs. L'abandon de Marmot pour le chat de groupe intervient la même semaine où [MDK v0.9.4](#mdk-v094-bounds-external-signer-login-and-adds-draft-persistence) ci-dessous continue d'investir dans la spécification.

### Amethyst livre une implémentation Concord indépendante pour les communautés chiffrées de bout en bout

[Amethyst](https://github.com/vitorpamplona/amethyst) est un client Nostr Android et multiplateforme riche en fonctionnalités. [PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566) ajoute une implémentation complète de [Concord](/fr/topics/concord-protocol/) (CORD-01 à CORD-07) couvrant les communautés sans serveur, chiffrées de bout en bout : les plans gift-wrapped de contrôle, de chat et de livre d'or sur des relays ordinaires, l'application des rôles et des bannissements enracinée dans le propriétaire que chaque client vérifie localement au lieu de faire confiance à un serveur, et le renouvellement de clé pour couper l'accès aux membres retirés. Le code du protocole et de la cryptographie réside dans `quartz/`, l'état et les modèles de vue dans `commons/`, et les écrans et la navigation dans `amethyst/` pour Android, avec des verbes CLI légers sous `cli/` ; il n'y a pas encore d'interface bureau, puisque la logique partagée se trouve dans `quartz`/`commons` pour que Desktop l'adopte ultérieurement. L'implémentation est indépendante : construite à partir des spécifications CORD publiques et des constantes de protocole observées, sous la propre licence MIT d'Amethyst, distincte du code AGPL-3.0 d'Armada. Les propres valeurs de vecteurs de test d'Armada ont été portées dans les tests unitaires de Quartz pour confirmer que les deux clients interopèrent réellement au niveau du protocole, donnant à Concord trois implémentations indépendantes en quelques jours : Vector livrant en premier, Armada comme client de référence de Soapbox, et maintenant la construction d'Amethyst à partir des spécifications.

### Sonar se sépare de Bitchat avec une alpha multiplateforme et une spécification de packs de stickers

[Sonar](https://sonarprivacy.xyz/) est un messager et portefeuille Bluetooth-mesh-plus-Nostr issu de Bitchat, avec des DMs de groupe Marmot interopérables avec White Noise. Le code réside sur [hedwig-corp/bitchat-to-sonar](https://github.com/hedwig-corp/bitchat-to-sonar). [v0.1-alpha.7](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.7) ajoute le fenêtrage borné de transcription de type Signal pour que les performances d'ouverture et de défilement restent local-first, synchronise l'état de découverte de proximité entre pairs, et corrige les uploads média Blossom qui échouaient sur la gestion du content-type et du statut HTTP ; la précédente [alpha.6](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.6) drainait les events Marmot en direct pour un rafraîchissement de chat plus rapide et comblait les écarts de parité de fonctionnalités Android-iOS à travers les appels, la messagerie, le portefeuille et les push. Sonar est également la source de spécification citée pour [PR #2410](#open-sticker-pack-kinds-10031-and-30031), qui enregistre les types d'events de packs de stickers sous la propre spécification « Sonar Stickers » du projet, donnant à ce lancement un lien direct vers les travaux de protocole de cette semaine.

### Divine Mobile 1.0.16 livre un éditeur vidéo plus complet, le chiffrement au repos et la provenance ProofMode

[Divine](https://github.com/divinevideo/divine-mobile) est un client de vidéo courte construit sur Nostr avec curation de flux par Web-of-Trust. [v1.0.16](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.16), la première version taguée depuis le #30, ajoute les transitions de clips, la lecture inversée, un enregistreur de voix off et des marqueurs de beat sur la timeline à l'éditeur vidéo, aux côtés d'un contrôle d'ajustement du flux qui permet à un utilisateur de balayer pour ajuster les recommandations directement au lieu de les laisser à des signaux d'engagement opaques. La version active également le chiffrement au repos pour les données locales, ajoute les uploads en arrière-plan qui survivent à la suspension de l'application, et transporte les données de provenance [ProofMode](/fr/topics/proofmode/) lorsqu'un clip filigrané est téléchargé afin que l'attestation de fabrication humaine ne soit pas supprimée en transit. Divine livre aussi de nouvelles protections pour les comptes de moins de 16 ans et étend la localisation à 17 langues et 284 chaînes traduites.

### Bitchat v1.7.0 ajoute la voix push-to-talk en direct pour les DMs et le mesh public

[Bitchat](https://github.com/permissionlesstech/bitchat) est une application de chat Bluetooth-mesh avec une passerelle optionnelle vers les relays Nostr. [v1.7.0](https://github.com/permissionlesstech/bitchat/releases/tag/v1.7.0), publiée le soir de la publication du #30, ajoute la voix push-to-talk en direct dans [PR #1403](https://github.com/permissionlesstech/bitchat/pull/1403) qui diffuse l'audio pendant que l'expéditeur maintient le bouton et se rabat sur une note vocale si le flux tombe, plus le push-to-talk signé sur le mesh public dans [PR #1406](https://github.com/permissionlesstech/bitchat/pull/1406) pour que les rafales vocales en direct sur le canal mesh partagé portent l'authentification de l'expéditeur. La version corrige aussi la rotation d'identifiant pair en reliant le lien lors d'une ré-annonce vérifiée, reconnaissant le même pair sous son nouvel identifiant ([PR #1401](https://github.com/permissionlesstech/bitchat/pull/1401)), et les messages directs vers un pair actuellement injoignable se mettent maintenant en file d'attente avec une livraison store-and-forward au lieu d'échouer purement et simplement ([PR #1415](https://github.com/permissionlesstech/bitchat/pull/1415)). Cela poursuit directement la couverture du #30 sur le proof-of-work [NIP-13](/fr/topics/nip-13/) de la v1.6.0 et le travail de passerelle mesh-vers-Nostr.

### MDK v0.9.4 borne la connexion par signeur externe et ajoute la persistance des brouillons

[MDK](https://github.com/marmot-protocol/mdk) est le SDK de référence pour le protocole [Marmot](/fr/topics/marmot/), la couche de messagerie MLS-over-Nostr dont le #30 avait couvert l'adoption de la spécification. [v0.9.4](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.4) borne les étapes d'annuaire consultatif qu'un client traverse lors de la connexion par signeur externe dans [PR #793](https://github.com/marmot-protocol/mdk/pull/793), empêchant une boucle de retry non bornée lorsqu'un signeur distant est lent ou non réactif. La même version ajoute la persistance des brouillons de messages et les liaisons de site web de profil dans [PR #812](https://github.com/marmot-protocol/mdk/pull/812), poursuivant la passe de durcissement incrémental que MDK mène depuis la v0.9.0.

---

## Versions taguées

### n_cord v1.1 ajoute le support NSEC Bunker

[n_cord](https://github.com/0n4t3/n_cord) est un client de chat propulsé par Nostr inspiré de Discord et IRC. [v1.1](https://github.com/0n4t3/n_cord/releases/tag/v1.1) ajoute le support [NIP-46](/fr/topics/nip-46/) NSEC Bunker aux côtés d'une correction de bug de gestion des réponses.

### cdk v0.17.3 ajoute le support du service de portefeuille NIP-47 à travers cdk, cdk-nwc et cdk-ffi

[cdk](https://github.com/cashubtc/cdk) est un kit de développement Cashu ; cette version est Bitcoin/Lightning uniquement à la plupart des égards, mais [v0.17.3](https://github.com/cashubtc/cdk/releases/tag/v0.17.3) ajoute le support du service [NIP-47](/fr/topics/nip-47/) (Nostr Wallet Connect) avec un crate de service NWC dédié, une intégration portefeuille, des bindings FFI pour `cdk-ffi`, et une couverture de tests de bout en bout, donnant aux portefeuilles Cashu construits sur cdk une surface Nostr Wallet Connect standard.

### Coop Mobile v0.2.4 améliore Nostr Connect et ajoute l'import ncryptsec1

[Coop Mobile](https://git.reya.su/reya/coop-mobile) est un client de messagerie privée [NIP-17](/fr/topics/nip-17/) pour plateformes mobiles. [v0.2.4](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.4) améliore son flux [NIP-46](/fr/topics/nip-46/) Nostr Connect, corrige un indicateur de chargement qui restait bloqué en permanence sur certaines connexions, et ajoute le support d'import du format de clé chiffrée [NIP-49](/fr/topics/nip-49/) `ncryptsec1` aux côtés d'un écran d'import d'identité redessiné.

### Nmail v0.14.0 arrive sur macOS avec l'envoi programmé et les notifications push

[Nmail](https://github.com/nogringo/nostr-mail-client) est un client mail construit sur Nostr ; [v0.14.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.14.0) apporte l'application sur macOS, ajoute l'envoi programmé avec une boîte aux lettres Programmé dédiée pour les messages en file d'attente, et ajoute les notifications push. La version bascule aussi la résolution d'identifiant Nostr du carnet d'adresses vers le résolveur [NIP-05](/fr/topics/nip-05/) de NDK en remplacement d'une implémentation sur mesure.

### Nostrord v2.2.0 ajoute un interrupteur principal DM et des messages directs plus riches

[Nostrord](https://github.com/nostrord/nostrord) est un client de chat de groupe basé sur relay [NIP-29](/fr/topics/nip-29/) pour Android, iOS, web et bureau. [v2.2.0](https://github.com/nostrord/nostrord/releases/tag/v2.2.0) ajoute un interrupteur principal pour désactiver toutes les fonctionnalités de messages directs d'un coup ([PR #175](https://github.com/nostrord/nostrord/pull/175)) et livre des « messages directs plus riches » ([PR #186](https://github.com/nostrord/nostrord/pull/186)), poursuivant la couverture du #30 sur la version intégrant le pool de relays et détectant les WebSockets zombies.

### Nostr WoT 0.3.86 durcit les sauvegardes de clés et les invites de signature

[Nostr WoT](https://github.com/nostr-wot/nostr-wot-extension) est une extension de navigateur associant une identité Nostr à un portefeuille Lightning. [v0.3.86](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.3.86) migre les sauvegardes de clés chiffrées vers le format standard [NIP-49](/fr/topics/nip-49/), fait afficher l'event complet et tous les tags dans les invites de signature au lieu d'un résumé, vérifie les données de relay par rapport à leur signature, et cesse d'exposer l'identité active lors du changement de compte. L'extension supprime aussi la permission de navigateur `scripting` inutilisée.

### Keep Android v1.1.8 ajoute l'onboarding FROST au premier lancement

[Keep](https://github.com/privkeyio/keep-android) est un signeur Android construit sur les parts de clé FROST à seuil. [v1.1.8](https://github.com/privkeyio/keep-android/releases/tag/v1.1.8) ajoute un flux de premier lancement qui explique les parts de clé FROST et permet à un nouvel utilisateur de choisir une politique de signature Manual, Basic ou Auto avant l'arrivée de la première demande de signature, le premier onboarding côté Android pour le modèle de signature à seuil du crate keep-mobile sous-jacent.

### Noscall v0.6.0 ajoute un portefeuille Cashu et les notifications push via relay

[Noscall](https://github.com/sanah9/noscall) est une application d'appels audio et vidéo sécurisés construite sur Nostr. [v0.6.0](https://github.com/sanah9/noscall/releases/tag/v0.6.0-release) ajoute un portefeuille Cashu rattaché au compte avec des soldes multi-mint, l'envoi et la réception d'ecash, et le paiement et la réception Lightning avec persistance des quotes. La version migre aussi les notifications push Android de Firebase Cloud Messaging vers un chemin de livraison basé sur les relays Nostr via UnifiedPush, et améliore la fiabilité des push iOS VoIP et APNs lors des retries de connexion.

### Kubo livre le mode tablette et les photos en chat de groupe

[Kubo](https://github.com/JeroenOnNostr/kubo) est une plateforme vidéo Nostr adaptée aux enfants avec curation de flux par Web-of-Trust. [kubo-v2026.07.05](https://github.com/JeroenOnNostr/kubo/releases/tag/kubo-v2026.07.05) ajoute une grille tablette optionnelle pour le flux enfant et le support des photos jointes aux messages de chat de groupe, plus des corrections pour le bouton d'inscription caché derrière le clavier à l'écran sur Android.

### Nostr Codex Phone v0.2.9 ajoute les requêtes d'aide git/diff/lecture de fichier

[Nostr Codex Phone](https://github.com/tidley/nostr-codex-phone) est une surface de contrôle mobile pour un worker d'assistant de codage local communiquant par DMs Nostr chiffrés. [v0.2.9](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.9) ajoute les actions d'outils mobiles OpenCode incluant les requêtes d'aide git, diff, lecture de fichier, status et historique, des améliorations d'épinglage et de recherche de session, et un contrôle d'arrêt de tâche, aux côtés d'un wrapper d'upload [Blossom](/fr/topics/blossom/) chiffré livré dans la v0.2.8 précédente.

### GitWorkshop v3.0.3 corrige les refs nouvellement annoncées dans l'explorateur de dépôts et livre sa première version Android

[GitWorkshop](https://github.com/DanConwayDev/gitworkshop) est une interface web git-over-Nostr pour parcourir et examiner les dépôts NIP-34. [v3.0.3](https://github.com/DanConwayDev/gitworkshop/releases/tag/v3.0.3) corrige les vues de branches, tags, commits et navigation de code qui échouaient à résoudre une ref qu'un dépôt annonce après que l'explorateur l'ait déjà chargée, aux côtés d'un nettoyage de timing du workflow CI, confirmé directement contre le tag et l'historique des commits. La même semaine, GitWorkshop a publié sa première version Android native sur [Zapstore](https://zapstore.dev), commençant à la v3.0.0 et atteignant la v3.0.3 en quelques heures ; l'interface web reste l'interface principale, et le paquet Android apporte la même navigation de dépôts NIP-34 sur téléphone pour la première fois.

### Bitcoin-Safe atteint Flathub, mettant en lumière son plugin Nostr Sync & Chat

[Bitcoin-Safe](https://bitcoin-safe.org) est un portefeuille Bitcoin en auto-garde construit autour de workflows avec signeurs matériels. Le projet [a livré un paquet Flathub](https://flathub.org/apps/org.bitcoin_safe.BitcoinSafe) cette semaine, sa première référence dans un magasin d'applications Linux grand public. La version Flathub met le plugin Sync & Chat de Bitcoin-Safe devant un public plus large : le plugin utilise les messages directs [NIP-17](/fr/topics/nip-17/), via la propre bibliothèque [bitcoin-nostr-chat](https://github.com/andreasgriffin/bitcoin-nostr-chat) du projet, pour synchroniser les étiquettes de portefeuille entre les appareils d'un utilisateur et pour envoyer et recevoir des PSBTs pour la co-signature multisig distante entre participants de confiance. La couche Nostr elle-même a été livrée plus tôt, dans la [2.0.0](https://github.com/andreasgriffin/bitcoin-safe/releases/tag/2.0.0) (2026-06-29), qui a redessiné la signature de transactions autour d'un type de connexion « Share via Chat & Sync » aux côtés du QR, de l'USB et du Bluetooth. La nouvelle de cette semaine est le packaging Flathub mettant cette fonctionnalité existante devant un public Linux grand public pour la première fois.

---

## Changements non publiés

### Amethyst permet aux comptes de donner des surnoms aux contacts avec des cartes NIP-85 chiffrées

Au-delà de l'[implémentation Concord](#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities) couverte ci-dessus, Amethyst a fusionné 54 autres PRs au cours de la dernière semaine. Le changement principal parmi eux est [PR #3548](https://github.com/vitorpamplona/amethyst/pull/3548), qui permet à un compte de donner un surnom à tout autre utilisateur en publiant sa propre carte de contact kind 30382 [NIP-85](/fr/topics/nip-85/) à son sujet. Le petname, une note privée, et tout mappage personnalisé de shortcode emoji [NIP-30](/fr/topics/nip-30/) résident dans le contenu chiffré [NIP-44](/fr/topics/nip-44/) de la carte, de sorte que seul le compte signataire peut les lire, et les cartes se synchronisent via l'ensemble de relays outbox étendu du compte à la connexion et de manière incrémentale par la suite. Les flux, les chats et les mentions affichent le petname à la place du nom d'affichage public, avec une carte de surnom tappable sur la page de profil au-dessus du vrai nom de l'utilisateur.

### Zap Cooking livre My Kitchen Phase 3 et corrige un bug de quorum de pool NDK

[Zap Cooking](https://github.com/zapcooking/frontend) est une application de partage de recettes et de communauté culinaire construite sur Nostr. Elle a fusionné 43 PRs poursuivant sa fonctionnalité de planification de repas « My Kitchen », livrant la génération de liste de courses, un sélecteur de recettes et une grille de semaine de planification dans cette phase. Le même ensemble de changements corrige un bug de préparation au quorum du pool de connexion [NDK](https://github.com/nostr-dev-kit/ndk) (Nostr Development Kit) qui pouvait laisser les lectures de relay en attente au-delà du moment où un quorum de relays avait déjà répondu.

### Kehto diffuse les lectures outbox avant la découverte de relays

[Kehto](https://github.com/kehto/web) est un runtime web précoce pour les applets Nostr [NIP-5D](/fr/topics/nip-5d/), ou « napplets ». Il a fusionné 26 PRs. [PR #193](https://github.com/kehto/web/pull/193) corrige les lectures outbox qui attendaient précédemment la fin du chargement de la liste de relays [NIP-65](/fr/topics/nip-65/) avant d'ouvrir le moindre relay, de sorte qu'un chargement de liste de relays qui ne se terminait jamais pouvait bloquer à la fois la livraison d'events et les timeouts de requêtes ; la correction ouvre immédiatement les relay hints validés et diffuse les résultats au fur et à mesure que les relays d'écriture sont découverts. Un second changement ([PR #196](https://github.com/kehto/web/pull/196)) aligne la page d'audit d'identité du projet avec NAP-SHELL, le contrat de cycle de vie de la plateforme Napplet, faisant partie du même travail d'alignement de protocole visible ailleurs dans la version `napplet/web` de cette semaine.

### Wired et TAO ajoutent le partage de revenus créateur NIP-57

[Wired](https://github.com/smolgrrr/Wired) et [TAO](https://github.com/smolgrrr/TAO) sont des clients sociaux jumeaux axés sur la liberté d'expression construits sur Nostr, partageant la même liste de PRs ; les deux ont fusionné [PR #121](https://github.com/smolgrrr/Wired/pull/121), qui implémente le partage de revenus créateur [NIP-57](/fr/topics/nip-57/) pour que les zaps envoyés à un post puissent se répartir automatiquement entre les contributeurs au-delà de l'auteur original. Cela poursuit la couverture du #30 sur la paire augmentant son signal proof-of-work à 21 bits comme travail non publié.

### Conduit Mono reconstruit la boîte de réception de commandes marchandes autour du paiement invité éphémère

[Conduit Mono](https://github.com/Conduit-BTC/conduit-mono) est un protocole de place de marché adjacent aux annonces classées [NIP-99](/fr/topics/nip-99/). [PR #174](https://github.com/Conduit-BTC/conduit-mono/pull/174) ajoute le paiement invité utilisant une clé éphémère générée par le navigateur : l'invité envoie une commande chiffrée et un rapport de paiement au marchand en utilisant cette clé à usage unique, et le marchand assure le suivi hors bande par téléphone ou email, de sorte que l'acheteur n'a jamais besoin d'une identité de boîte de réception durable. [PR #175](https://github.com/Conduit-BTC/conduit-mono/pull/175) reconstruit la boîte de réception de commandes du marchand autour d'un modèle unique partagé d'état de commande, séparant les rôles acheteur et marchand et exigeant un code de suivi et un transporteur avant qu'une commande physique ou mixte puisse passer à l'état expédié. Le flux de paiement du projet s'appuie sur les messages privés [NIP-17](/fr/topics/nip-17/), le chiffrement [NIP-44](/fr/topics/nip-44/) et le gift wrap [NIP-59](/fr/topics/nip-59/). L'[analyse approfondie](#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension) de cette semaine couvre les conventions [Gamma Markets](/fr/topics/gamma-markets/) vers lesquelles ce même problème d'état de commande converge.

### Buzz durcit le provisionnement du créateur de canal autour du kind 39002

[Buzz](https://github.com/block/buzz) est une plateforme de communication en intelligence collective connectant agents IA et humains par Nostr. Il a fusionné 240 PRs au cours de la dernière semaine, poursuivant son arc de durcissement de la couche relay depuis la couverture du #30 sur les métriques de tour d'agent kind 44200. La correction de cette semaine ([PR #1830](https://github.com/block/buzz/pull/1830)) traite le créateur d'un canal comme un membre avant que la logique de provisionnement de canal kind 39002 ne s'exécute, fermant une condition de course où le propre canal du créateur pouvait le rejeter pendant la configuration.

### Nostr Docs adopte un signeur NIP-49 avec multi-compte et appairage QR

[Nostr Docs](https://github.com/formstr-hq/nostr-docs) est une application collaborative de documents native Nostr. Elle a fusionné 5 PRs, la notable ([PR #50](https://github.com/formstr-hq/nostr-docs/pull/50)) adoptant le paquet `@formstr/signer` pour une authentification [NIP-49](/fr/topics/nip-49/) complète avec changement multi-compte et appairage QR, remplaçant un chemin de signature sur mesure antérieur.

### Également livré

Des corrections plus petites d'interopérabilité de signeurs et de fiabilité ont atterri à travers plusieurs projets suivis au cours de la dernière semaine sans assez de surface nouvelle pour justifier leur propre paragraphe : [ngit-cli](https://github.com/DanConwayDev/ngit-cli), un client en ligne de commande pour une alternative à GitHub basée sur Nostr, livre [v2.6.3](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.6.3) faisant en sorte que `ngit init` donne des conseils de configuration actionnables au lieu de demander répétitivement un nsec ; [Manent](https://github.com/dtonon/manent), une application de notes et fichiers privés chiffrés construite sur Nostr, livre [v1.4.1](https://github.com/dtonon/manent/releases/tag/v1.4.1) corrigeant la connexion par signeur Android cassée quand Amber retourne un pubkey hex et améliorant le défilement de connexion bunker ; [NoorNote](https://github.com/77elements/noornote), un client Nostr léger sans services Google, livre [v1.2.8](https://github.com/77elements/noornote/releases/tag/v1.2.8) corrigeant les notifications de groupe Nostrord manquées et ajoutant un toggle d'alerte d'auto-post ; [Bray](https://github.com/forgesworn/bray), un serveur MCP Nostr sensible à la confiance pour agents IA et humains, livre [v1.34.0](https://github.com/forgesworn/bray/releases/tag/v1.34.0) envoyant les métadonnées de nom de client lors du connect bunker [NIP-46](/fr/topics/nip-46/) ; [Lumilumi](https://github.com/TsukemonoGit/lumilumi), un client web Nostr, met en cache les listes de relays [NIP-65](/fr/topics/nip-65/) dans le stockage local pour un repli hors ligne ; [Earthly](https://github.com/moogmodular/earthly), une application Nostr de communauté et de ville locale, ajoute la recherche géographique [NIP-50](/fr/topics/nip-50/) ; et [lnbits](https://github.com/lnbits/lnbits), un système de portefeuille et de comptes Lightning libre et open-source, livre [PR #3925](https://github.com/lnbits/lnbits/pull/3925) rendant `send_nostr_dm` non bloquant au sein d'une version par ailleurs centrée sur Lightning.

---

## Nouvellement suivis et découverts

### OpenDiscord v1.0.1 se lance comme client de type Discord sur Nostr

[OpenDiscord](https://github.com/sofia-gros/open-discord) est un client serveur-et-canal de type Discord construit sur Nostr avec des permissions basées sur les rôles et des lobbies vocaux WebRTC/SFU. [v1.0.1](https://github.com/sofia-gros/open-discord/releases/tag/v1.0.1) est la première version installable taguée du projet.

### Auditable Voting v0.1.140 aligne les rôles organisateur, votant et proxy d'audit

[Auditable Voting](https://github.com/tidley/auditable-voting) est un shell de vote Nostr côté client uniquement. [v0.1.140](https://github.com/tidley/auditable-voting/releases/tag/v0.1.140) aligne les rôles organisateur, votant et proxy d'audit avec l'event exact de définition de questionnaire public signé par l'organisateur, comblant une lacune où un proxy d'audit pouvait agir sur des comptes générés obsolètes ou un état persisté depuis un worker ou organisateur différent.

### Cambium v0.3.2 se couple avec Heartwood comme signeur NIP-55 sans clé

[Cambium](https://github.com/forgesworn/cambium) est le choix Découverte de ce numéro : un signeur Android [NIP-55](/fr/topics/nip-55/) qui ne détient aucun matériel de clé privée en propre, redirigeant chaque demande de signature par [NIP-46](/fr/topics/nip-46/) vers un signeur matériel Heartwood compagnon. Le projet partage l'organisation GitHub `forgesworn` avec le projet suivi Bray, et Heartwood lui-même avait été couvert dans le #30 livrant le pont de signature relay-vers-série que le côté Android de Cambium utilise maintenant. [v0.3.2](https://github.com/forgesworn/cambium) peaufine la feuille d'approbation pour avertir en direct lorsque l'identité sélectionnée diffère de la liaison existante de l'application et déplace les écritures du journal d'activité vers une file d'attente unique non bloquante.

### Également lancés cette semaine : echoes, Dispatch et Linky

Trois autres lancements méritent mention cette semaine. [echoes](https://github.com/Lwb89dev/echoes) est une application de notes hors ligne d'abord, chiffrée de bout en bout, qui se synchronise de manière privée par Nostr. [Dispatch](https://github.com/freecritter/dispatch) est un organisateur de voyage local-first où chaque sauvegarde est chiffrée par [NIP-44](/fr/topics/nip-44/) et sauvegardée par Nostr sous une clé dédiée et non reliée, et sa version [v0.3.0](https://github.com/freecritter/dispatch) ajoute la connexion Amber [NIP-55](/fr/topics/nip-55/) pour que l'application ne touche jamais directement la clé privée de l'utilisateur. [Linky](https://github.com/hynek-jina/linky) combine les contacts et DMs Nostr avec les paiements Lightning et Cashu dans une seule application web progressive.

---

## Travaux de protocole et mises à jour NIP

Aucune PR fusionnée dans le [dépôt NIPs](https://github.com/nostr-protocol/nips) au cours de la dernière semaine. Six propositions ont été ouvertes.

### Ouverte : kind:10011 ensembles de suivi favoris

[PR #2413](https://github.com/nostr-protocol/nips/pull/2413), de fiatjaf, ajoute kind:10011 pour les ensembles de suivi favoris. Elle reproduit le modèle existant où kind:10012 (ensembles de relays favoris) contient des tags `a` pointant vers des ensembles de relays kind:30002, étendant le même mécanisme de favori aux ensembles de suivi kind:30000 pour qu'un client puisse mettre en favori une liste de suivi sélectionnée sans remplacer sa propre liste de contacts.

### Ouverte : un drive privé chiffré étend NIP-4E

[PR #2412](https://github.com/nostr-protocol/nips/pull/2412), de l'équipe Form*, propose un event Metadata générique, kind 34578, distingué par un tag d'identifiant `d` et un tag de sous-type `t`, ainsi qu'un système de fichiers privé chiffré construit par-dessus, déjà implémenté dans le propre client Form* Drive de Form*, encore expérimental. Un enregistrement de fichier est un event Metadata avec `t=files` : les blobs de fichiers résident sur des serveurs [Blossom](/fr/topics/blossom/) tandis que seul un index chiffré se trouve sur les relays, et chaque morceau de fichier obtient sa propre paire de clés éphémère avec chiffrement HKDF dérivé [NIP-44](/fr/topics/nip-44/) v2. Un event compagnon Decoupled Encryption Key contient une seule clé symétrique à l'échelle du drive contre laquelle les métadonnées de chaque fichier se déchiffrent, et il s'appuie explicitement sur [NIP-4E](/fr/topics/nip-4e/), le brouillon d'abstraction de stockage de fiatjaf encore ouvert ([PR #1647](https://github.com/nostr-protocol/nips/pull/1647), ouvert depuis décembre 2024).

Cette clé unique à l'échelle du drive signifie qu'une clé divulguée expose les métadonnées de chaque fichier du drive, pas seulement d'un fichier, puisque les paires de clés éphémères par fichier ne font varier que la clé de chiffrement des morceaux, pas la clé de déchiffrement des métadonnées ; aucun chemin de rotation ou de révocation n'existe encore au-delà de la publication d'un nouvel event Metadata avertissant que les events plus anciens pourraient être perdus. Une seconde proposition plus ciblée vise la même idée sous-jacente NIP-4E sous un angle différent : [PR #2361](https://github.com/nostr-protocol/nips/pull/2361), de fiatjaf, découple les clés d'identité et de chiffrement au sein de la messagerie [NIP-17](/fr/topics/nip-17/) spécifiquement, ouvert depuis le 1er juin. Les deux PRs ne sont pas fusionnées, faisant de ceci un coin actif et disputé de l'espace de conception. Form* indique que le client Drive est expérimental avec une mise à jour à venir prochainement.

### Ouverte : NIP-DA partage de données privées avec permissions

[PR #2411](https://github.com/nostr-protocol/nips/pull/2411), de JAFairweather, est un nouveau brouillon NIP-DA pour le partage de données privées avec permissions via des attributions de données scopées. Chaque utilisateur conserve un enregistrement chiffré faisant autorité par scope sur les relays, et l'accès est accordé en livrant de manière privée la clé symétrique de ce scope dans un gift wrap [NIP-59](/fr/topics/nip-59/), de sorte que les relays ne stockent que du texte chiffré et n'apprennent jamais qui a accordé l'accès à qui ; une révocation est simplement une rotation de clé, sans besoin de réécrire la copie de chaque consommateur. L'auteur le positionne comme distinct des DMs [NIP-17](/fr/topics/nip-17/) (qui peuvent transporter un instantané de données mais pas des mises à jour en direct ou de la révocation) et des listes privées NIP-51 (qui ne transportent pas de matériel de clé), et cite deux implémentations indépendantes, une bibliothèque de référence JavaScript et un CLI Go sur go-nostr, testées en croisé contre relay.damus.io, nos.lol et relay.primal.net.

### Ouverte : kinds de packs de stickers 10031 et 30031

[PR #2410](https://github.com/nostr-protocol/nips/pull/2410), de vincenzopalazzo, enregistre kind 30031 (packs de stickers adressables) et kind 10031 (liste de packs de stickers d'un utilisateur) dans la table des Event Kinds, spécifiés par le format « Sonar Stickers » que [Sonar](#sonar-splits-off-from-bitchat-with-a-cross-platform-alpha-and-a-sticker-pack-spec) livre cette semaine. Les kinds se situent délibérément un cran au-dessus des kinds d'emoji personnalisés [NIP-30](/fr/topics/nip-30/) 30030 et 10030 pour qu'un client ne puisse pas confondre un pack de stickers avec un ensemble d'emoji ; les octets d'image de sticker résident sur des serveurs HTTPS compatibles [Blossom](/fr/topics/blossom/), et les références de stickers envoyés portent un hash en clair pour qu'un pack adressable modifié ne puisse pas changer silencieusement l'apparence de stickers déjà envoyés dans d'anciens messages. Une PR compagnon enregistre les mêmes kinds dans le projet séparé `registry-of-kinds`.

### Ouverte : épinglage de messages NIP-29 avec kind:9010 et kind:39005

[PR #2379](https://github.com/nostr-protocol/nips/pull/2379), d'Anderson-Juhasc, ajoute l'épinglage de messages aux groupes basés sur relay [NIP-29](/fr/topics/nip-29/) : kind:9010 `update-pin-list` est un event de modération portant la liste complète des events épinglés comme tags `e` dans l'ordre d'affichage, de sorte qu'un seul event peut épingler, désépingler, réordonner ou vider l'ensemble épinglé, et kind:39005 est un miroir généré par le relay exposant la dernière liste acceptée. La conception remplace une approche antérieure par paire ajout/suppression de [PR #1163](https://github.com/nostr-protocol/nips/pull/1163) après retour de revue, et choisit les numéros de kind 9010/39005 car 9009 et 39003 ont depuis été réclamés par `create-invite` et les rôles de groupe. Anderson-Juhasc maintient également [Nostrord](#nostrord-v220-adds-a-dm-master-toggle-and-richer-direct-messages), dont la [v2.2.0](https://github.com/nostrord/nostrord/releases/tag/v2.2.0) est livrée la même semaine.

### Ouverte : restructuration de la découverte de relays NIP-66

[PR #2241](https://github.com/nostr-protocol/nips/pull/2241), de VincenzoImp, est une restructuration substantielle de la découverte de relays [NIP-66](/fr/topics/nip-66/). Elle remplace la prose vague « Other tags include » par une section Indexed Tags structurée, ajoute un tag `W` reflétant le champ `attributes` de NIP-11 pour le filtrage de découverte de relays, ajoute un tag d'étiquette `l` utilisant des espaces de noms standardisés (`ISO-639-1`, `ISO-3166-1`, `IANA-asn`, `IANA-tz`, `nip66.label.city`), et organise les tags RTT, SSL/TLS, réseau, géographiques, DNS et HTTP en sections dédiées aux côtés d'une nouvelle table Check Types. Elle corrige aussi des events d'exemple cassés qui avaient des noms de champs erronés, un `kind` manquant et des noms de types de vérification invalides, et clôt le [ticket #2171](https://github.com/nostr-protocol/nips/issues/2171). Tous les changements restent rétrocompatibles puisque chaque tag ajouté est optionnel.

---

## Analyse approfondie : NIP-99 et l'extension commerce Gamma Markets

[NIP-15](/fr/topics/nip-15/), la spécification originale Nostr Marketplace, est patrimoniale à ce stade : elle modélisait un stall de marchand (kind 30017) avec des produits (kind 30018) classés en dessous, et les clients qui l'utilisaient autrefois, Shopstr parmi eux, sont depuis passés aux annonces classées [NIP-99](/fr/topics/nip-99/) comme spécification active. NIP-99 elle-même est un event adressable unique, kind 30402 pour une annonce active ou kind 30403 pour un brouillon, sans stall à créer au préalable. Elle laisse tout ce qui suit l'annonce indéfini : frais d'expédition, statut de commande, reçus, avis et un moyen de regrouper plusieurs annonces sous une seule vitrine, exactement les parties de NIP-15 qui n'ont jamais été transférées. [Gamma Markets](/fr/topics/gamma-markets/) comble cette lacune, et constitue la couche commerce moderne qui mérite d'être comprise aujourd'hui.

### La lacune que NIP-99 laisse ouverte

Le champ `content` d'une annonce NIP-99 porte une description Markdown, `price` et `location` se trouvent directement sur l'event, et les tags `t` la rendent cherchable comme contenu hashtag ordinaire. Parce qu'elle est adressable sur le tuple pubkey, kind et tag `d`, un vendeur modifie une annonce en place en publiant une nouvelle version avec le même tag `d` :

```json
{
  "kind": 30402,
  "content": "Vintage mechanical keyboard, Cherry MX Blue switches, barely used.",
  "tags": [
    ["d", "keyboard-mx-blue-01"],
    ["title", "Vintage Mechanical Keyboard"],
    ["summary", "Cherry MX Blue, barely used"],
    ["published_at", "1752537600"],
    ["location", "NYC"],
    ["price", "100", "USD"],
    ["t", "electronics"]
  ]
}
```

C'est toute la spécification : une petite annonce signée et modifiable. Chaque client implémentant NIP-99 pour du vrai e-commerce, au-delà d'une annonce ponctuelle, a fini par inventer ses propres conventions privées pour l'expédition, les messages de commande et les avis. Deux clients NIP-99 pouvaient chacun afficher une annonce correctement et toujours n'avoir aucun moyen partagé de compléter un paiement entre eux.

### Gamma Markets : standardiser ce que NIP-99 a laissé de côté

Gamma Markets est le nom qu'un groupe de travail de développeurs de places de marché Nostr, les équipes derrière Shopstr, Cypher, Plebeian Market et Conduit Market, a donné à un ensemble partagé de conventions e-commerce construites sur l'event kind 30402 existant de NIP-99. La spécification est liée depuis le document canonique NIP-99 via [PR #1784](https://github.com/nostr-protocol/nips/pull/1784) et maintenue dans son propre dépôt, [GammaMarkets/market-spec](https://github.com/GammaMarkets/market-spec).

Gamma Markets ajoute deux kinds autonomes adjacents aux annonces. Kind 30405 regroupe plusieurs annonces en une collection de produits, référençant chacune par un tag `a` explicite :

```json
{
  "kind": 30405,
  "content": "Summer sale picks",
  "tags": [
    ["d", "summer-picks"],
    ["title", "Summer Sale"],
    ["a", "30402:<merchant-pubkey>:keyboard-mx-blue-01"],
    ["shipping_option", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

Kind 30406 définit une option d'expédition avec tarification par pays et règles de coût optionnelles basées sur le poids ou la distance :

```json
{
  "kind": 30406,
  "content": "Standard Regional Shipping",
  "tags": [
    ["d", "standard-regional"],
    ["title", "Standard Shipping"],
    ["price", "5.99", "USD"],
    ["country", "US"],
    ["service", "standard"],
    ["duration", "24", "72", "H"],
    ["weight-max", "30", "kg"]
  ]
}
```

La création de commande, les demandes de paiement, les mises à jour de statut et d'expédition, et les reçus de paiement passent tous comme des messages privés gift-wrapped [NIP-17](/fr/topics/nip-17/) ordinaires, répartis entre trois kinds par rôle et non par ré-enveloppement du transport : kind 14 porte la communication libre acheteur/marchand, kind 16 porte chaque transition d'état de commande (un tag `type` de 1 à 4 marque la création de commande, la demande de paiement, la mise à jour de statut ou la mise à jour d'expédition), et kind 17 porte le reçu de paiement de l'acheteur. Un message de création de commande ressemble à ceci avant le gift-wrapping :

```json
{
  "kind": 16,
  "content": "Please leave the package with the doorman.",
  "tags": [
    ["p", "<merchant-pubkey>"],
    ["subject", "New order"],
    ["type", "1"],
    ["order", "order-8f21"],
    ["amount", "115000"],
    ["item", "30402:<merchant-pubkey>:keyboard-mx-blue-01", "1"],
    ["shipping", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

Noter un achat complété est un kind adressable séparé, 31555, pointant vers l'annonce qu'il évalue :

```json
{
  "kind": 31555,
  "content": "Arrived fast, exactly as described.",
  "tags": [
    ["d", "a:30402:<merchant-pubkey>:keyboard-mx-blue-01"],
    ["rating", "1", "thumb"],
    ["rating", "1.0", "quality"],
    ["rating", "0.9", "delivery"]
  ]
}
```

Faire transiter les messages de commande par NIP-17 signifie qu'un paiement Gamma Markets utilise le même transport de messages privés que les clients livrent déjà pour les DMs, au lieu d'un kind de message de commande sur mesure.

Le choix de conception central de la spécification est que rien ne se propage en cascade. Une annonce qui appartient à une collection référence celle-ci explicitement avec un tag `a` au lieu d'hériter automatiquement des options d'expédition ou de la description de la collection, et une option d'expédition qu'une annonce utilise est référencée de la même manière explicite. C'est un renversement délibéré du modèle de stall NIP-15, où un produit héritait silencieusement de la devise et du tableau d'expédition que son stall parent définissait. Le compromis est un balisage plus explicite sur chaque annonce, en échange d'une configuration toujours lisible depuis l'event lui-même, sans objet parent à résoudre au préalable.

### Où cela se manifeste en pratique

Le travail de [Conduit Mono](#conduit-mono-rebuilds-the-merchant-orders-inbox-around-ephemeral-guest-checkout) de cette semaine se situe dans le même territoire de messages de commande que Gamma Markets standardise : le paiement invité par clé éphémère de [PR #174](https://github.com/Conduit-BTC/conduit-mono/pull/174) et la reconstruction de la boîte de réception de commandes du marchand de [PR #175](https://github.com/Conduit-BTC/conduit-mono/pull/175) résolvent tous deux le problème d'état de commande acheteur/marchand que les messages kind 14, 16 et 17 de Gamma Markets formalisent ; Conduit Mono fait tourner son propre modèle d'état de commande aux côtés de ces kinds, sans les adopter directement. Shopstr, l'un des quatre projets ayant rédigé la spécification, a lui aussi fait avancer sa propre plomberie commerce au cours de la dernière semaine : [PR #568](https://github.com/shopstr-eng/shopstr/pull/568) extrait la logique de gift-wrap NIP-17 dupliquée dans un module partagé, et [PR #567](https://github.com/shopstr-eng/shopstr/pull/567) amène son parseur d'authentification HTTP [NIP-98](/fr/topics/nip-98/) à une couverture de tests complète, de la maintenance sur exactement les couches de messagerie et d'authentification dont un flux de commande Gamma Markets dépend pour atteindre un acheteur et un marchand en toute sécurité.

NIP-15 a perdu le rôle de vitrine en standardisant un stall et un produit, puis en laissant les paiements, l'expédition, les avis et le statut de commande comme un problème applicatif. Gamma Markets comble la majeure partie de cette surface manquante sans toucher à la forme d'annonce unique de NIP-99, en s'appuyant sur la pile DM existante de Nostr, NIP-17, au lieu d'inventer une nouvelle couche de messagerie.

---

C'est tout pour cette semaine. Vous construisez quelque chose ou avez des nouvelles à partager ? Contactez-nous par DM NIP-17 ou trouvez-nous sur Nostr.
