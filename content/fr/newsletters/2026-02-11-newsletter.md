---
title: 'Nostr Compass #9'
date: 2026-02-11
translationOf: /en/newsletters/2026-02-11-newsletter.md
translationDate: 2026-02-12
draft: false
type: newsletters
---

Bienvenue dans Nostr Compass, votre guide hebdomadaire sur Nostr.

**Cette semaine :** Mostro livre sa première bêta publique après trois ans de développement, apportant le trading P2P de Bitcoin sur mobile via Nostr. OpenSats attribue sa seizième vague de subventions Bitcoin, avec Minibits Wallet recevant un renouvellement pour son portefeuille Cashu intégré à Nostr. **Zapstore atteint sa version stable 1.0**, marquant la maturation du magasin d'applications Android décentralisé. Coracle 0.6.29 ajoute les topics et les commentaires sur les highlights. Igloo Desktop v1.0.3 livre un renforcement majeur de la sécurité pour la signature à seuil Frostr. Amber v4.1.2-pre1 migre vers l'architecture Flow. Angor atteint v0.2.5 avec la refonte de l'interface de financement et la configuration de serveur d'images NIP-96. NostrPress se lance comme outil convertissant les profils Nostr en blogs statiques. Antiprimal livre la passerelle conforme aux standards qui relie le serveur cache propriétaire de Primal aux NIP Nostr standards. Primal Android fusionne 18 PRs étendant l'infrastructure NWC avec le support double portefeuille, la journalisation d'audit et la méthode `lookup_invoice`. diVine livre les flux vidéo API-first. Le SDK TypeScript Marmot extrait son application de chat de référence dans un dépôt autonome et commence la migration vers ts-mls v2. Le dépôt NIPs fusionne le comptage approximatif HyperLogLog pour NIP-45 et extrait les tags d'identité du kind 0. Plusieurs propositions de vitorpamplona commencent à alléger systématiquement les événements de métadonnées kind 0. Au niveau du protocole, on trouve Nostr Relay Connect pour la traversée NAT et Nostr Web Tokens pour les revendications web signées. En approfondissement, le nouveau comptage approximatif HyperLogLog de NIP-45 pour les métriques d'événements inter-relais et le protocole de stockage de fichiers HTTP NIP-96, désormais déprécié en faveur de Blossom, alors que certains projets gèrent la transition entre ces deux standards média.

## Actualités

### Mostro livre sa première bêta publique

[Mostro](https://github.com/MostroP2P/mostro), la place d'échange Bitcoin pair-à-pair construite sur Nostr, a publié son [application mobile v1.1.0](https://github.com/MostroP2P/mobile/releases/tag/v1.1.0), la première bêta publique du projet après trois ans de développement. L'application permet aux utilisateurs d'échanger du Bitcoin directement en utilisant Nostr pour la coordination, avec Lightning pour le règlement et aucun intermédiaire custodial.

La version introduit les notifications push avec fiabilité améliorée en arrière-plan sur Android, un système de journalisation optionnel permettant aux utilisateurs de capturer et partager les données de diagnostic en cas de problème, la mise à jour de relais plus fluide via l'initialisation additive, et les raffinements UI Phase 2 avec le support de l'internationalisation. L'application est disponible sur [Zapstore](https://zapstore.dev) et en [téléchargement direct GitHub](https://github.com/MostroP2P/mobile/releases/tag/v1.1.0).

Mostro rejoint Shopstr et Plebeian Market parmi les applications de commerce natives Nostr, avec la particularité de se concentrer sur la coordination d'échanges fiat-Bitcoin. Le [daemon Mostro](https://github.com/MostroP2P/mostro) sous-jacent gère l'appariement et la résolution de litiges via les relais Nostr.

### Seizième vague de subventions Bitcoin d'OpenSats

[OpenSats](https://opensats.org/blog/sixteenth-wave-of-bitcoin-grants) a annoncé les subventions à 17 projets open-source. Le point pertinent ici : [Minibits Wallet](https://github.com/minibits-cash/minibits_wallet), le portefeuille Android [Cashu](/fr/topics/cashu/) avec le support d'événements de portefeuille [NIP-60](/fr/topics/nip-60/) et l'intégration nutzap, reçoit un renouvellement de subvention. Minibits utilise les événements Nostr pour stocker l'état ecash, rendant les sauvegardes de portefeuille portables entre appareils via la synchronisation par relay.

### NostrPress : du profil Nostr au blog statique

[NostrPress](https://github.com/besoeasy/NostrPress) ([blog.besoeasy.com](https://blog.besoeasy.com)) est un nouvel outil qui convertit un profil Nostr en blog entièrement statique déployable partout. On publie les articles sur Nostr via n'importe quel client, et NostrPress génère un site web autonome à partir de ces événements, avec l'hébergement local de médias et les flux RSS.

Construit avec Nunjucks et JavaScript, NostrPress produit un site libre de toute dépendance de plateforme. La sortie générée est du HTML/CSS brut hébergeable sur n'importe quel serveur de fichiers statiques, GitHub Pages, Netlify ou un VPS personnel. L'outil rejoint [Npub.pro](https://github.com/nostrband/nostrsite) et [Servus](https://github.com/servus-social/servus) parmi les options transformant du contenu Nostr en sites web traditionnels.

### Antiprimal : passerelle conforme aux standards vers le cache Primal

[antiprimal](https://gitlab.com/soapbox-pub/antiprimal) ([antiprimal.net](https://antiprimal.net)), un nouveau projet d'Alex Gleason et de l'équipe Soapbox, est la passerelle WebSocket qui relie le serveur cache propriétaire de Primal aux messages du protocole Nostr standard. Primal offre les fonctionnalités comme les statistiques d'événements, la recherche de contenu et les calculs de Web of Trust via `wss://cache.primal.net/v1`, mais y accéder nécessite un format de message propriétaire avec un champ `cache` non standard que les clients Nostr standards ne peuvent pas utiliser. Antiprimal traduit les requêtes NIP standards vers le format de Primal et convertit les réponses en retour.

La passerelle supporte les requêtes COUNT [NIP-45](/fr/topics/nip-45/) (réactions, réponses, reposts, comptages de zaps, comptages de followers), la recherche [NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md), l'information relay [NIP-11](/fr/topics/nip-11/) et les Trusted Assertions [NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md) au service des données Web of Trust précalculées de Primal. Un bot compagnon publie les événements NIP-85 kind 30382 (statistiques utilisateur) et kind 30383 (engagement événement) vers les relais configurables. Le projet est construit en TypeScript sur Bun et utilise la bibliothèque Nostrify. Créé le 6 février, il compte 53 commits dans ses trois premiers jours de développement et est en ligne sur antiprimal.net.

### Ikaros : passerelle de messagerie IA sur Signal et Nostr

[Ikaros](https://gitlab.com/soapbox-pub/ikaros), un nouveau projet de l'équipe Soapbox, est la passerelle de messagerie permettant aux agents IA de communiquer via Signal et les DM chiffrés Nostr. Le pont utilise l'[Agent Client Protocol](https://agentclientprotocol.org) (ACP) afin de connecter tout assistant de codage IA compatible ACP à de vrais réseaux de messagerie. Trois pull requests constituent la construction initiale du projet cette semaine.

La [PR #1](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/1) implémente un adaptateur complet de DM chiffrés [NIP-04](/fr/topics/nip-04/) avec support d'envoi/réception, mise en tampon avec vidage explicite à la complétion, formats de clé privée `nsec` et hex, publication multi-relay avec reconnexion automatique, et un assistant de configuration interactif. L'adaptateur utilise nostr-tools v2.23.0 et met à jour le SDK ACP vers v0.14.1.

La [PR #2](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/2) corrige la perte silencieuse de messages causée par un problème de concurrence de mise à jour de session : les notifications entrantes arrivant avant l'enregistrement d'une session dans la map étaient silencieusement perdues, et le correctif met ces notifications en tampon afin de les rejouer à la fin de l'enregistrement. La [PR #3](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/3) ajoute les métadonnées de nom/UUID Signal aux interactions d'agent, afin que l'agent IA sache à qui il parle et dans quel groupe. Le projet ouvre un nouvel espace de conception : les agents IA adressables via DM Nostr qui sont aussi accessibles depuis Signal, et inversement.

### Campagne d'allègement du Kind 0

vitorpamplona a ouvert cette semaine plusieurs PRs proposant l'extraction systématique de données du kind 0 (métadonnées utilisateur) vers les kinds d'événements dédiés. La campagne répond à un problème croissant : ces événements ont accumulé au fil du temps les champs que la plupart des clients n'utilisent pas, gonflant la taille de chaque récupération de profil.

La [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) (fusionnée) déplace les tags d'identité (tags `i`) du kind 0 vers un nouveau kind 10011, puisque l'adoption de ces tags a été minimale. La [PR #2213](https://github.com/nostr-protocol/nips/pull/2213) propose de déplacer la vérification [NIP-05](/fr/topics/nip-05/) vers le kind 10008, ce qui permettrait aux utilisateurs d'avoir plusieurs identifiants NIP-05 et de filtrer par adresse NIP-05. La [PR #2217](https://github.com/nostr-protocol/nips/pull/2217) propose d'extraire les adresses Lightning (lud06/lud16) vers un nouveau kind, évitant que tous les utilisateurs de kind 0 ne transportent les champs liés aux zaps qui n'importent qu'aux clients avec intégration Lightning.

Ces propositions ont relancé la discussion sur la question plus large de la structure du kind 0, incluant la [PR #1770](https://github.com/nostr-protocol/nips/pull/1770), la proposition de longue date visant à remplacer le JSON stringifié dans le contenu du kind 0 par les tags structurés.

### Support relay de NIP-70 : critique pour la messagerie chiffrée

L'implémentation White Noise du protocole [Marmot](/fr/topics/marmot/) a [identifié un manque critique](https://blog.jgmontoya.com/2026/02/10/nip70-relay-status.html) dans le support par les relais de [NIP-70](https://github.com/nostr-protocol/nips/blob/master/70.md) (Protected Events) et [NIP-42](/fr/topics/nip-42/) (Authentication). Ses tests ont révélé que de grands relais publics, incluant Damus, Primal et nos.lol, rejettent les événements protégés directement avec l'erreur `blocked: event marked as protected` au lieu d'initier le défi d'authentification requis.

Cela brise la fonctionnalité de sécurité clé : NIP-70 permet la suppression sécurisée de KeyPackages MLS expirés, empêchant les attaques de type << capturer maintenant, déchiffrer plus tard >>. En l'absence de support relay, les protocoles de messagerie chiffrée ne peuvent pas protéger leurs utilisateurs contre la compromission future de clés. White Noise a désactivé NIP-70 par défaut en réponse, conservant un drapeau optionnel destiné à ceux disposant de relais compatibles.

**Appel aux opérateurs de relais :** Implémentez le flux d'authentification NIP-42 complet. Lorsqu'un événement protégé arrive, défiez le client de prouver sa propriété, puis acceptez l'écriture validée. Rejeter les événements protégés directement brise les garanties de sécurité du protocole dont dépendent les applications de messagerie chiffrée.

## Versions

### Coracle 0.6.29

[Coracle](https://github.com/coracle-social/coracle) ([coracle.social](https://coracle.social)), le client web de hodlbod, a livré [0.6.29](https://github.com/coracle-social/coracle/releases/tag/0.6.29). La version ajoute l'affichage de topics et de commentaires sur les highlights kind 9802. Un nouvel élément de navigation donne un accès rapide aux listes curatées par l'utilisateur depuis l'interface principale. En interne, Coracle a été mis à jour vers la dernière version de Welshman, la bibliothèque Nostr partagée qui alimente la gestion de relais et le traitement d'événements de Coracle. La liste de relais par défaut a été rafraîchie, et le suivi d'erreurs Glitchtip a été retiré du code.

### Igloo Desktop v1.0.3

[Igloo Desktop](https://github.com/FROSTR-ORG/igloo-desktop), l'application de signature à seuil [FROST](/fr/topics/frost/) et de gestion de clés, a livré [v1.0.3](https://github.com/FROSTR-ORG/igloo-desktop/releases/tag/v1.0.3) avec un renforcement extensif de la sécurité. La version introduit la validation IPC, l'isolation Electron et les vérifications de relais sensibles au SSRF contre la falsification de requêtes côté serveur. Un nouveau flux d'intégration et d'importation de parts simplifie la distribution de clés, la planification de relais inclut désormais la normalisation et la fusion par priorité, et l'architecture API Electron basée sur le preload améliore la frontière de sécurité entre le renderer et le processus principal. Un système de maintien en vie du signataire assure la stabilité en session de signature à seuil, et les améliorations UX de récupération réduisent la friction de la restauration de clés.

### Amber v4.1.2-pre1

[Amber](https://github.com/greenart7c3/Amber), le signataire d'événements Android, a publié [v4.1.2-pre1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.2-pre1) corrigeant l'affichage manquant du score de confiance de relais introduit dans v4.1.1, résolvant les problèmes d'analyse JSON propres aux requêtes de chiffrement/déchiffrement non-Nostr, et migrant le modèle de compte de LiveData vers Flow afin d'obtenir une gestion d'état plus prévisible. La version bascule aussi les secrets bunker vers les UUIDs complets et passe à Gradle plugin 9.

### Mostro Mobile v1.1.0 et Daemon v0.16.1

Voir la [section Actualités ci-dessus](#mostro-livre-sa-première-bêta-publique) au sujet de la version mobile. Sur le serveur, le [daemon Mostro](https://github.com/MostroP2P/mostro) a livré [v0.16.1](https://github.com/MostroP2P/mostro/releases/tag/v0.16.1), ajoutant la publication automatique de métadonnées NIP-01 kind 0 au démarrage ([PR #575](https://github.com/MostroP2P/mostro/pull/575)), de sorte que le daemon annonce son identité sur le réseau quand il se connecte. La version corrige aussi la documentation du calcul de frais de développement ([PR #571](https://github.com/MostroP2P/mostro/pull/571)).

### Angor v0.2.5

[Angor](https://github.com/block-core/angor) ([angor.io](https://angor.io)), le protocole de financement P2P décentralisé construit sur Bitcoin et Nostr, a livré [v0.2.5](https://github.com/block-core/angor/releases/tag/v0.2.5) avec trois PRs fusionnées. La [PR #649](https://github.com/block-core/angor/pull/649) redessine la section de gestion de fonds (V2), remplaçant la mise en page précédente par la nouvelle interface suivant les UTXOs individuels et les positions d'investissement. La [PR #651](https://github.com/block-core/angor/pull/651) révise l'InvoiceView avec les styles de boutons mis à jour, les dialogues fermables, la commande << Copier l'adresse >>, le support de l'annulation de surveillance d'adresses et un flux d'investissement amélioré. La [PR #652](https://github.com/block-core/angor/pull/652) ajoute les serveurs d'images [NIP-96](/fr/topics/nip-96/) ([spec](https://github.com/nostr-protocol/nips/blob/master/96.md)) configurables dans les paramètres, permettant aux utilisateurs de choisir quel point d'accès de téléversement média gère les images et la documentation de leurs projets. La [v0.2.4](https://github.com/block-core/angor/releases/tag/v0.2.4) a été livrée la semaine précédente.

### Ridestr v0.2.2 et v0.2.3

[Ridestr](https://github.com/variablefate/ridestr), la plateforme de covoiturage décentralisée [couverte la semaine dernière](/fr/newsletters/2026-02-04-newsletter/#ridestr-v020--version-roadflare), a poursuivi son itération rapide avec [v0.2.2](https://github.com/variablefate/ridestr/releases/tag/v0.2.2) (Bridge Payment Hotfix) et [v0.2.3](https://github.com/variablefate/ridestr/releases/tag/v0.2.3) suite à la v0.2.0 << RoadFlare Release >>. Le hotfix v0.2.2 corrige un bug où les paiements bridge [Cashu](/fr/topics/cashu/) inter-mints annulaient automatiquement les courses pendant que le paiement était encore en traitement ou allait finalement aboutir, empêchant l'annulation prématurée lors de règlements lents. La version corrige aussi le scintillement de l'UI et les zones tactiles cassées sur le bouton << ma position >>. La v0.2.3 livre les corrections de bugs supplémentaires. Chaque version inclut les APK séparés, l'un Ridestr (application passager) et l'autre Drivestr (application conducteur).

### Nostr PHP 1.9.4

[Nostr PHP](https://github.com/nostrver-se/nostr-php) ([nostr-php.dev](https://nostr-php.dev)), la bibliothèque d'aide PHP, a livré [1.9.4](https://github.com/nostrver-se/nostr-php/releases/tag/1.9.4) ajoutant la propriété `timeout` configurable à la classe de requête ([PR #106](https://github.com/nostrver-se/nostr-php/pull/106)). Cela permet aux développeurs de définir les durées de timeout personnalisées lors de la connexion aux relais et lors de chaque requête de message, évitant les blocages indéfinis quand un relay ne répond pas ou est lent.

### Zapstore v1.0.0

[Zapstore](https://github.com/zapstore/zapstore/releases/tag/1.0.0) ([zapstore.dev](https://zapstore.dev)), le magasin d'applications Android construit sur Nostr, **a atteint son jalon de version stable 1.0** cette semaine après plusieurs mois de release candidates.

La version 1.0 inclut les améliorations de stabilité critiques : la gestion de l'état du bouton d'installation garantissant que Supprimer apparaît immédiatement après la fin de l'installation, les messages d'erreur conviviaux avec détails techniques extensibles, et un bouton << Signaler un problème >> qui envoie les DM chiffrés via Nostr avec les clés éphémères. On trouve aussi un nouvel écran de mises à jour avec polling et suivi par lots, un meilleur watchdog de téléchargement destiné aux transferts bloqués, les limites de téléchargements concurrents dynamiques basées sur la performance de l'appareil, la synchronisation plus fréquente de paquets installés et la logique de comparaison de versions améliorée. L'équipe a corrigé un problème critique avec flutter_secure_storage et amélioré la gestion de cas limites du gestionnaire de paquets.

Ce jalon représente la maturation de la première plateforme de distribution d'applications dédiée de Nostr, permettant aux développeurs de publier les applications Android directement aux utilisateurs, en dehors du contrôle centralisé de magasins d'applications.

### ZSP v0.3.1

[ZSP](https://github.com/zapstore/zsp), l'outil CLI en Go de l'équipe [Zapstore](https://github.com/zapstore/zapstore) qui remplace l'outillage de publication précédent afin de signer et téléverser les applications Android vers les relais Nostr, a publié [v0.3.1](https://github.com/zapstore/zsp/releases/tag/v0.3.1). ZSP gère l'acquisition d'APK depuis GitHub, GitLab, Codeberg, F-Droid ou les fichiers locaux, puis analyse les métadonnées, signe les événements Nostr (via clé privée, bunker [NIP-46](/fr/topics/nip-46/), ou extension navigateur [NIP-07](/fr/topics/nip-07/)), et téléverse les artefacts vers les serveurs [Blossom](/fr/topics/blossom/). Cette version ajoute un mode hors ligne complet destiné à la liaison de keystore en l'absence de connexion réseau, les en-têtes `Content-Digest` sur les téléversements Blossom assurant la conformité au protocole, la correction de la détection d'APK arm64-v8a depuis les dépôts F-Droid, les corrections de paramètres de requête de fin sur GitLab, et le support complet de fichiers `.env` dans la configuration.

### Damus iOS 1.17

[Damus](https://github.com/damus-io/damus), le client iOS Nostr, est passé à la version 1.17 ([PR #3606](https://github.com/damus-io/damus/pull/3606)). La version corrige un problème de RelayPool où les connexions se fermaient après la libération du bail éphémère ([PR #3605](https://github.com/damus-io/damus/pull/3605)), ce qui pouvait causer l'interruption inattendue d'abonnements. Elle résout aussi un bug où la timeline de favoris n'affichait pas d'événements lors du changement d'onglets ([PR #3603](https://github.com/damus-io/damus/pull/3603)).

### nak v0.18.3

[nak](https://github.com/fiatjaf/nak), le couteau suisse Nostr en CLI, a livré [v0.18.3](https://github.com/fiatjaf/nak/releases/tag/v0.18.3) avec trois corrections de stabilité : prévention d'un panic quand les tags de challenge AUTH sont nil ou trop courts, vérification d'erreurs du dateparser avant d'utiliser la valeur analysée, et gestion d'URLs de mint Cashu manquant le séparateur `://`.

### Mi : relay local en navigateur

[Mi](https://git.shakespeare.diy/npub1scvyzz02ayma34hesz62pdrd5nhsmxp74hjq8msmfs9khh3r3drsnw68d8/mi.git) ([mi.shakespeare.wtf](https://mi.shakespeare.wtf)), un nouveau MiniApp [Shakespeare](https://shakespeare.wtf), est un relay local en navigateur qui archive les événements Nostr d'un utilisateur dans IndexedDB. Mi récupère les profils (kind 0), les listes de contacts (kind 3), les listes de relais (kind 10002) et les événements de portefeuille depuis les relais connectés et stocke le tout localement, donnant un accès hors ligne à ses propres données. Construit avec React et nostr-tools 2.15.0.

### Agora v1.0.2

[Agora](https://gitlab.com/soapbox-pub/agora) ([agora.spot](https://agora.spot)), la plateforme décentralisée d'activisme et de collecte de fonds de l'équipe Soapbox, a livré [v1.0.2](https://gitlab.com/soapbox-pub/agora/-/releases/v1.0.2) avec un APK Android disponible en téléchargement direct. C'est la première mention d'Agora dans Compass, le projet ayant été lancé le 17 janvier avec cette déclaration de mission : << Rejoignez le mouvement mondial et envoyez votre soutien aux activistes sur le terrain internationalement. >>

La plateforme s'articule autour de la carte du monde où l'on parcourt par pays, crée les << actions >> géolocalisées (manifestations, campagnes, organisation communautaire) et en discute via les commentaires en fil. Tout le contenu se propage via les relais Nostr, de sorte qu'aucun serveur central ne peut être mis hors ligne afin de faire taire la coordination. Agora supporte plusieurs langues avec la parité de traduction imposée par la CI, intègre les serveurs média [Blossom](/fr/topics/blossom/) aux téléversements et inclut la recherche, la navigation par hashtags avec bascule global/régional, les profils utilisateurs et les systèmes de réactions. La version v1.0.2 est le build Android actuel, disponible en téléchargement direct d'APK.

### xonos v0.1.6

[xonos](https://codeberg.org/xonos/xonos), le client Nostr 3D expérimental construit avec le moteur de jeu Bevy, a livré [v0.1.6](https://codeberg.org/xonos/xonos/releases/tag/v0.1.6). xonos affiche les événements Nostr dans un environnement spatial 3D avec les capacités de synthèse vocale, explorant comment les données de protocole social pourraient fonctionner en dehors d'interfaces 2D conventionnelles.

## Mises à jour des projets

### Primal Android étend l'infrastructure NWC

[Primal Android](https://github.com/PrimalHQ/primal-android-app) a fusionné 18 PRs cette semaine, poursuivant la construction NWC [commencée la semaine dernière](/fr/newsletters/2026-02-04-newsletter/#primal-android-livre-le-chiffrement-nwc). La [PR #883](https://github.com/PrimalHQ/primal-android-app/pull/883) ajoute le support de connexions NWC à travers deux portefeuilles (Spark et externe), et la [PR #879](https://github.com/PrimalHQ/primal-android-app/pull/879) implémente la méthode NWC `lookup_invoice` vérifiant le statut de paiements.

La [PR #880](https://github.com/PrimalHQ/primal-android-app/pull/880) ajoute la journalisation d'audit requête-réponse NWC servant au débogage d'interactions portefeuille. La [PR #877](https://github.com/PrimalHQ/primal-android-app/pull/877) ajoute le support multi-comptes à `PrimalNwcService`, permettant aux utilisateurs avec plusieurs profils de maintenir les connexions de portefeuille séparées. La [PR #882](https://github.com/PrimalHQ/primal-android-app/pull/882) implémente le nettoyage périodique de réservations de budget expirées, empêchant les réservations de paiement périmées de bloquer le portefeuille.

Le travail sur l'UI inclut la refonte de l'écran de mise à niveau du portefeuille ([PR #889](https://github.com/PrimalHQ/primal-android-app/pull/889)), la FAQ de mise à niveau du portefeuille ([PR #885](https://github.com/PrimalHQ/primal-android-app/pull/885)), le réglage de l'adresse Lightning pendant l'intégration ([PR #888](https://github.com/PrimalHQ/primal-android-app/pull/888)) et un correctif empêchant les transactions de zap d'apparaître comme paiements réguliers dans les types non-Lightning ([PR #887](https://github.com/PrimalHQ/primal-android-app/pull/887)).

### diVine livre les flux vidéo API-first

[diVine](https://github.com/divinevideo/divine-mobile), le client vidéo courte, a fusionné 19 PRs cette semaine, s'orientant vers l'architecture API-first. La [PR #1468](https://github.com/divinevideo/divine-mobile/pull/1468) introduit les flux vidéo API-first, et la [PR #1466](https://github.com/divinevideo/divine-mobile/pull/1466) ajoute les points d'accès API tendances, récents et accueil. La [PR #1433](https://github.com/divinevideo/divine-mobile/pull/1433) indexe les contrôleurs vidéo spécifiques permettant un rendu efficace de flux.

La gestion de profils s'est améliorée avec la [PR #1440](https://github.com/divinevideo/divine-mobile/pull/1440) implémentant un pattern cache-plus-frais lors de la consultation de profils tiers, réduisant le temps de chargement tout en assurant la fraîcheur de données. L'équipe a aussi livré les corrections de notifications ([PR #1437](https://github.com/divinevideo/divine-mobile/pull/1437)), la refonte du flux de commentaires ([PR #1431](https://github.com/divinevideo/divine-mobile/pull/1431)) et le balayage d'onglets sur l'écran Notifications ([PR #1388](https://github.com/divinevideo/divine-mobile/pull/1388)).

### White Noise : unification du trousseau de clés et recherche d'utilisateurs

Le backend [White Noise](https://github.com/marmot-protocol/whitenoise-rs) du protocole [Marmot](/fr/topics/marmot/) a fusionné 4 PRs cette semaine. Deux PRs ont amélioré la gestion du trousseau de clés : la [PR #468](https://github.com/marmot-protocol/whitenoise-rs/pull/468) rend l'identifiant du service de trousseau configurable via `WhitenoiseConfig`, et la [PR #475](https://github.com/marmot-protocol/whitenoise-rs/pull/475) unifie l'implémentation sur un seul crate `keyring-core` avec les magasins natifs par plateforme, remplaçant le code fragmenté spécifique à chaque plateforme. Séparément, la [PR #470](https://github.com/marmot-protocol/whitenoise-rs/pull/470) ajoute la fonctionnalité de recherche d'utilisateurs.

### Marmot TS extrait l'application de chat de référence

Le SDK TypeScript [Marmot](/fr/topics/marmot/) ([marmot-ts](https://github.com/marmot-protocol/marmot-ts)) a fusionné la [PR #40](https://github.com/marmot-protocol/marmot-ts/pull/40), retirant l'application de chat de référence intégrée et la transférant dans un dépôt autonome : [marmots-web-chat](https://github.com/marmot-protocol/marmots-web-chat). Ce nouveau dépôt, créé le 6 février, est l'implémentation de référence du SDK TypeScript Marmot avec sa propre pipeline CI, la vue de chat à onglets et un système de build indépendant. La séparation permet au SDK de se concentrer sur les préoccupations de bibliothèque tandis que l'application de chat itère sur l'UX de façon indépendante.

La PR ouverte [#41](https://github.com/marmot-protocol/marmot-ts/pull/41) migre marmot-ts vers ts-mls v2.0.0, apportant l'API redessinée avec les objets de contexte unifiés, de nouveaux utilitaires de gestion de messages (création d'événements, lecture, désérialisation), les helpers de métadonnées de key package et le support d'événements de suppression.

### Mises à jour d'Alby Hub

[Alby Hub](https://github.com/getAlby/hub) a fusionné 5 PRs cette semaine. La [PR #2049](https://github.com/getAlby/hub/pull/2049) ajoute un Alby CLI à l'interface du magasin d'applications. La [PR #2033](https://github.com/getAlby/hub/pull/2033) corrige la gestion de données de zap invalides dans la liste de transactions, et la [PR #2046](https://github.com/getAlby/hub/pull/2046) retire la méthode `ListTransactions` inutilisée de l'interface LNClient.

### Notedeck livre le tableau de bord et Agentium

[Notedeck](https://github.com/damus-io/notedeck), le client multiplateforme Nostr de Damus, a fusionné 6 PRs cette semaine. La [PR #1247](https://github.com/damus-io/notedeck/pull/1247) ajoute un tableau de bord initial. La [PR #1293](https://github.com/damus-io/notedeck/pull/1293) introduit Agentium, un environnement de développement multi-agents qui transforme l'assistant IA Dave en un système avec deux modes IA et la gestion d'agents par scène. La [PR #1276](https://github.com/damus-io/notedeck/pull/1276) ajoute un composeur de messages multiligne avec les raccourcis clavier style Signal, et la [PR #1278](https://github.com/damus-io/notedeck/pull/1278) livre les améliorations de performance média. Parmi les PRs ouvertes à noter : [l'infrastructure outbox](https://github.com/damus-io/notedeck/pull/1288) et la [NIP-34](/fr/topics/nip-34/) [planification de l'application Git](https://github.com/damus-io/notedeck/pull/1289).

### Agora livre la refonte majeure de l'UI

[Agora](https://gitlab.com/soapbox-pub/agora) a fusionné 7 PRs cette semaine aux côtés de sa version v1.0.2. La [PR #106](https://gitlab.com/soapbox-pub/agora/-/merge_requests/106) est la plus conséquente, fermant 11 tâches UI à travers paramètres, édition de profil, interactions carte, résultats de recherche, filtrage de commentaires et gestion de serveurs Blossom. La fusion a désactivé les boutons de réaction destinés aux utilisateurs non authentifiés (qui obtenaient auparavant un échec silencieux en essayant de réagir aux publications sur la carte), corrigé le défilement de la carte sur la ligne de date et ajouté le texte en gras correspondant dans les résultats de recherche.

La [PR #108](https://gitlab.com/soapbox-pub/agora/-/merge_requests/108) ajoute le comptage de commentaires sous les publications du flux et sur les pages de fils. La [PR #107](https://gitlab.com/soapbox-pub/agora/-/merge_requests/107) ajoute le réessai automatique lors d'échecs de chargement d'événements avec un bouton de rechargement explicite quand toutes les tentatives sont épuisées. La [PR #104](https://gitlab.com/soapbox-pub/agora/-/merge_requests/104) change la navigation par hashtags afin d'utiliser par défaut la portée globale, puisque la portée par pays précédente retournait souvent zéro résultat.

La [PR #109](https://gitlab.com/soapbox-pub/agora/-/merge_requests/109) ajoute l'étape CI qui vérifie la parité de traductions à travers toutes les langues, faisant échouer le build si la moindre clé manque de valeur. La [PR #110](https://gitlab.com/soapbox-pub/agora/-/merge_requests/110) tronque les notes longues dans les flux afin de préserver le rythme de défilement, et la [PR #111](https://gitlab.com/soapbox-pub/agora/-/merge_requests/111) corrige un problème de zoom mobile iOS lors de la rédaction de commentaires sur les actions, causé par de petites tailles de police.

### Clawstr livre un CLI et les boutons Lightning Zap

[Clawstr](https://gitlab.com/soapbox-pub/clawstr), la plateforme inspirée de Reddit où les agents IA créent et gèrent les communautés sur Nostr, a fusionné 3 PRs cette semaine. La [PR #11](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/11) remplace toutes les commandes nak manuelles dans la définition de compétences d'agents IA par le nouveau package `@clawstr/cli` (`npx -y @clawstr/cli@latest`), remplaçant la construction manuelle d'événements JSON par les commandes CLI et ajoutant les opérations de portefeuille (init, balance, zap, npc) et la recherche plein texte [NIP-50](/fr/topics/nip-50/).

La [PR #13](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/13) ajoute la page de documentation << For Humans >> et un composant `ProfileZapDialog`. Le bouton de zap apparaît sur les pages de profil quand un utilisateur a configuré son adresse Lightning et fonctionne en dehors de toute connexion, utilisant LNURL-pay directement avec les montants prédéfinis en sats et l'affichage de QR code. La [PR #12](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/12) documente la commande `wallet sync`, expliquant comment les paiements vers les adresses Lightning sont retenus par NPC jusqu'à ce que les agents synchronisent explicitement leurs portefeuilles.

## Mises à jour des NIP

Changements récents dans le [dépôt NIPs](https://github.com/nostr-protocol/nips) :

**Fusionnés :**

- **[NIP-45 : Réponse relay HyperLogLog](https://github.com/nostr-protocol/nips/pull/1561)** - [NIP-45 (Comptage d'événements)](/fr/topics/nip-45/) supporte désormais le comptage approximatif HyperLogLog (HLL). Un relay peut retourner les valeurs de registres HLL de 256 octets aux côtés de réponses COUNT. En fusionnant ces registres de plusieurs relais, un client calcule la cardinalité approximative en évitant de télécharger les ensembles complets d'événements. Le cas d'utilisation principal concerne le comptage de followers et de réactions en évitant de dépendre d'un seul relay comme source faisant autorité. Même deux événements de réaction consomment plus de bande passante que la charge utile HLL de 256 octets. Avec les corrections HyperLogLog++, la précision s'améliore sur de petites cardinalités.

- **[NIP-39 : Tags d'identité déplacés du Kind 0](https://github.com/nostr-protocol/nips/pull/2216)** - Les tags de revendication d'identité [NIP-39](/fr/topics/nip-39/) (tags `i`) ont été extraits du kind 0 vers un nouveau kind 10011 dédié. La raison : presque aucun client ne supporte ces tags, ils ajoutent donc du poids à chaque récupération de kind 0 en apportant peu de valeur. C'est la première d'une série de PRs d'extraction du kind 0 de vitorpamplona (voir la [section Actualités](#campagne-dallègement-du-kind-0)).

**PRs ouvertes et discussions :**

- **[NIP-XX : Nostr Relay Connect (NRC)](https://github.com/nostr-protocol/nips/pull/2214)** - woikos propose un protocole d'accès aux relais Nostr via un tunnel chiffré passant par un relay de rendez-vous public. Le mécanisme permet l'accès aux relais derrière NAT ou pare-feu, incluant les relais personnels fonctionnant sur un serveur domestique ou un appareil mobile. Le tunnel utilise les événements kind 24891/24892 avec le chiffrement [NIP-44](/fr/topics/nip-44/) à travers un relay de rendez-vous qui ne peut pas déchiffrer le trafic. Application pratique : tout client Nostr peut exposer un stockage local (IndexedDB, SQLite) comme point d'accès relay destiné à la synchronisation inter-appareils. La sémantique NIP-01 standard (REQ, EVENT, CLOSE, COUNT) traverse le tunnel de façon transparente. Des implémentations de référence existent en Go (ORLY Relay) et TypeScript (Smesh).

- **[Nostr Web Tokens (NWT)](https://github.com/nostr-protocol/nips/pull/2187)** - pippellia-btc propose les Nostr Web Tokens, un format d'événement Nostr transmettant les revendications signées entre parties web, inspiré de JSON Web Tokens (JWTs). NWT peut représenter à la fois [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) (HTTP Auth) et [les événements d'autorisation Blossom](/fr/topics/blossom/), donnant aux clients de la flexibilité sur la durée de validité de tokens. La bibliothèque de référence en Go est disponible. L'[explication vidéo](https://github.com/pippellia-btc/nostr-web-tokens) et la [comparaison détaillée](https://github.com/pippellia-btc/nostr-web-tokens#comparisons) avec NIP-98 et Blossom Auth sont liées dans la PR.

- **[Simplification de NIP-47](https://github.com/nostr-protocol/nips/pull/2210)** - rolznz propose de retirer les méthodes `multi_` de [NIP-47 (Nostr Wallet Connect)](/fr/topics/nip-47/), qui étaient complexes à implémenter et n'ont pas gagné en adoption. La PR réduit aussi la duplication dans le chiffrement et la gestion de la rétrocompatibilité, nettoyant la spécification après [l'ajout de factures de rétention la semaine dernière](/fr/newsletters/2026-02-04-newsletter/#mises-à-jour-des-nip).

- **[NIP-05 : Déplacement vers un kind d'événement propre](https://github.com/nostr-protocol/nips/pull/2213)** - vitorpamplona propose de déplacer la vérification NIP-05 du kind 0 vers un nouveau kind 10008, permettant plusieurs identifiants NIP-05 par utilisateur et le filtrage par adresse NIP-05. Fait partie de la campagne d'allègement du kind 0.

- **[NIP-57 : Adresses Lightning depuis le Kind 0](https://github.com/nostr-protocol/nips/pull/2217)** - vitorpamplona propose d'extraire lud06/lud16 (adresses Lightning) du kind 0 vers un kind d'événement dédié par [NIP-57](/fr/topics/nip-57/), poursuivant l'effort d'allègement du kind 0.

- **[Hyperpersonnalisation de profil](https://github.com/nostr-protocol/nips/pull/2165)** - fiatjaf propose les capacités de personnalisation de profil étendues au-delà de ce que le kind 0 supporte actuellement.

## Approfondissement NIP : NIP-45 (Comptage d'événements) et HyperLogLog

[NIP-45](/fr/topics/nip-45/) ([spec](https://github.com/nostr-protocol/nips/blob/master/45.md)) définit comment un client peut demander aux relais de compter les événements correspondant à un filtre en évitant de transférer les événements eux-mêmes. La fusion cette semaine du [support HyperLogLog](https://github.com/nostr-protocol/nips/pull/1561) ajoute la structure de données probabiliste qui résout un problème fondamental : comment compter les éléments à travers plusieurs relais indépendants.

**Le problème :**

Compter les événements sur un seul relay est simple : on envoie la requête COUNT, on reçoit un nombre en retour. Compter à travers le réseau est plus difficile. Si le relay A rapporte 50 réactions et le relay B en rapporte 40, le total n'est pas 90 car beaucoup d'événements existent sur les deux relais. En l'absence de téléchargement complet servant à dédupliquer, un client ne peut pas calculer le vrai comptage.

**HyperLogLog :**

HyperLogLog (HLL) est un algorithme probabiliste qui estime le nombre d'éléments distincts dans un ensemble en utilisant une quantité fixe de mémoire. L'implémentation NIP-45 utilise 256 registres d'un octet chacun, consommant exactement 256 octets quel que soit le nombre d'événements comptés. L'algorithme fonctionne en examinant la représentation binaire de chaque ID d'événement et en suivant la position de zéros en tête. Un événement dont l'ID commence par beaucoup de zéros est statistiquement rare, donc son occurrence indique un grand ensemble.

**Fonctionnement dans NIP-45 :**

Un relay répondant à la requête COUNT peut inclure un champ `hll` contenant les valeurs de registres encodées en base64 :

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<base64 encoded 256 bytes>"}]
```

Le client collecte les valeurs HLL de plusieurs relais et fusionne le tout en prenant la valeur maximale à chaque position de registre. Ce HLL fusionné représente l'union de tous les ensembles d'événements à travers les relais, gérant automatiquement la déduplication. L'estimation finale de cardinalité est calculée à partir de registres fusionnés.

**Précision :**

Avec 256 registres, l'erreur standard est d'environ 5,2%. Un vrai comptage de 1 000 donnera typiquement une estimation entre 948 et 1 052. Avec de plus grands comptages, l'erreur relative reste constante : un vrai comptage de 100 000 s'estimera à environ 94 800-105 200. Grâce aux corrections HyperLogLog++, la précision s'améliore aussi sur de petites cardinalités (sous environ 200), où l'algorithme de base tend à surestimer.

**Importance :**

Les métriques sociales (comptages de followers, de réactions, de reposts) sont au centre de tout client de médias sociaux. En l'absence de HLL, un client doit soit interroger un seul relay << de confiance >> (centralisant le comptage), soit télécharger tous les événements de tous les relais (gaspillant la bande passante). HLL permet aux clients d'obtenir un bon comptage approximatif de plusieurs relais avec la surcharge totale de 256 octets par relay, quel que soit le comptage réel. Même deux événements de réaction consomment plus de bande passante qu'une charge utile HLL complète.

La spécification fixe le nombre de registres à 256 dans un souci d'interopérabilité. Tous les relais produisent les valeurs HLL que tout client peut fusionner, quelle que soit l'implémentation de relay. Cette standardisation signifie qu'on peut implémenter le support HLL en une fois et bénéficier de chaque relay qui le supporte.

**Statut actuel :**

La PR a été ouverte par fiatjaf et discutée pendant plusieurs mois avant d'être fusionnée cette semaine. Il faudra ajouter le calcul HLL aux gestionnaires COUNT dans les implémentations de relais, et la fusion HLL à la logique d'agrégation de comptages dans les clients.

## Approfondissement NIP : NIP-96 (Stockage de fichiers HTTP) et la transition vers Blossom

[NIP-96](/fr/topics/nip-96/) ([spec](https://github.com/nostr-protocol/nips/blob/master/96.md)) définissait comment les clients Nostr téléversent, téléchargent et gèrent les fichiers sur les serveurs média HTTP. Désormais marqué comme << non recommandé >> en faveur de [Blossom](/fr/topics/blossom/) (hébergement média basé sur BUD), NIP-96 reste pertinent cette semaine car Angor v0.2.5 [a ajouté la configuration de serveur NIP-96](#angor-v025) et ZSP v0.3.1 [téléverse vers les serveurs Blossom](#zsp-v031), illustrant la transition de protocole en cours.

**Fonctionnement de NIP-96 :**

Un client découvre la capacité d'un serveur de fichiers en récupérant `/.well-known/nostr/nip96.json`, qui retourne l'URL de l'API, les types de contenu supportés, les limites de taille et les transformations média disponibles :

```json
{
  "api_url": "https://file-server.example/api",
  "download_url": "https://cdn.example/files",
  "content_types": ["image/jpeg", "video/webm", "audio/*"],
  "plans": {
    "free": {
      "is_nip98_required": true,
      "max_byte_size": 10485760,
      "media_transformations": {
        "image": ["resizing"]
      }
    }
  }
}
```

Le client téléverse via un POST `multipart/form-data` vers l'URL de l'API avec un en-tête d'autorisation [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) (un événement Nostr signé prouvant l'identité de celui qui téléverse). Le serveur retourne la structure de métadonnées de fichier [NIP-94](/fr/topics/nip-94/) contenant l'URL du fichier, les hashes SHA-256 originaux et transformés, le type MIME et les dimensions :

```json
{
  "status": "success",
  "nip94_event": {
    "tags": [
      ["url", "https://cdn.example/files/<hash>.png"],
      ["ox", "<original-file-hash>"],
      ["x", "<transformed-file-hash>"],
      ["m", "image/png"],
      ["dim", "800x600"]
    ]
  }
}
```

On télécharge via les requêtes GET vers `<api_url>/<sha256-hash>`, avec les paramètres de requête optionnels activant les transformations côté serveur comme le redimensionnement d'images. La suppression passe par DELETE avec l'authentification NIP-98, et seul l'auteur original du téléversement peut supprimer ses fichiers. Un point d'accès de listing de fichiers retourne les résultats paginés de téléversements d'un utilisateur.

Chaque utilisateur publie les événements kind 10096 déclarant ses serveurs de téléversement préférés, permettant aux clients de sélectionner automatiquement le bon serveur en l'absence de configuration manuelle.

**Raisons de la dépréciation :**

NIP-96 liait les URLs de fichiers à un serveur spécifique. Si `files.example.com` tombait en panne, chaque note Nostr référençant ses URLs perdait ses médias. Le serveur était l'adresse, et l'adresse était fragile.

[Blossom](/fr/topics/blossom/) (Blobs Stored Simply on Mediaservers) inverse cette logique en faisant du hash SHA-256 du contenu du fichier l'identifiant canonique. L'URL Blossom ressemble à `https://blossom.example/<sha256>.png`, mais tout serveur Blossom hébergeant le même fichier le sert au même chemin de hash. Si un serveur disparaît, le client interroge un autre serveur demandant le même hash. L'adressage par contenu rend les données portables entre serveurs par défaut.

Blossom simplifie aussi l'API. NIP-96 utilisait les téléversements de formulaires multipart avec les réponses JSON, les politiques de transformation et un point de découverte. Blossom utilise un simple PUT aux téléversements, GET aux téléchargements, et les événements Nostr signés à l'autorisation. La spécification Blossom est divisée en documents modulaires : BUD-01 couvre le protocole serveur, l'autorisation et la récupération, BUD-02 couvre le téléversement de blobs, BUD-03 couvre les serveurs utilisateurs, et BUD-04 couvre le mirroring entre serveurs.

La dépréciation a eu lieu en septembre 2025 via la [PR #2047](https://github.com/nostr-protocol/nips/pull/2047), qui a marqué NIP-96 comme << non recommandé >> dans l'index de NIPs.

**La transition en pratique :**

Nostr.build et void.cat supportaient NIP-96 et ont ajouté ou migré vers les points d'accès Blossom. Sur le plan client, la version v0.2.5 d'Angor cette semaine a ajouté la configuration de serveur NIP-96 applicable aux images de projets, tandis que la version v0.3.1 de ZSP téléverse les artefacts exclusivement vers les serveurs Blossom avec les en-têtes `Content-Digest` assurant la conformité au protocole. Amethyst et Primal supportent les téléversements Blossom. La coexistence continuera probablement jusqu'à ce que toutes les implémentations NIP-96 restantes achèvent leur migration.

**Ce qui perdure :**

Les événements de préférence de serveur kind 10096 restent utiles à la sélection de serveur Blossom. Les métadonnées de fichier NIP-94 (événements kind 1063) décrivent toujours les propriétés de fichiers quel que soit le protocole de téléversement qui a servi à les créer. Le hachage SHA-256 que NIP-96 utilisait aux URLs de téléchargement est devenu le fondement de l'adressage par contenu de Blossom. La conception de NIP-96 a éclairé ce que Blossom a simplifié : la leçon était que l'hébergement média sur un réseau décentralisé nécessite un stockage adressé par contenu afin de correspondre à la résistance à la censure de la couche relay.

---

C'est tout pour cette semaine. Envoyez vos actualités et propositions de projets à couvrir via <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">NIP-17 DM</a> ou trouvez-nous sur Nostr.
