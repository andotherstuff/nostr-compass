---
title: 'Nostr Compass #11'
date: 2026-02-25
translationOf: /en/newsletters/2026-02-25-newsletter.md
translationDate: 2026-02-25
draft: false
type: newsletters
---

Bienvenue dans Nostr Compass, votre guide hebdomadaire sur Nostr.

**Cette semaine :** [White Noise v0.3.0](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.3.0) apporte la messagerie en temps réel et le support du signataire Amber avec plus de 160 améliorations fusionnées. [diVine 1.0.5](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.5) corrige les problèmes de lecture vidéo et ajoute des événements de visionnage Kind 22236 pour les analyses des créateurs. [Pika](https://github.com/sledtools/pika), [Ridestr](https://github.com/variablefate/ridestr) et [Unfiltered](https://github.com/dmcarrington/unfiltered) livrent des mises à jour. [FIPS](https://github.com/jmcorgan/fips) livre une implémentation Rust fonctionnelle du réseau maillé natif Nostr. Notecrumbs reçoit des correctifs de stabilité pour les aperçus de liens damus.io. [ContextVM](https://contextvm.org) fait le pont entre Nostr et le Model Context Protocol. Parmi les nouveaux projets : [Burrow](https://github.com/CentauriAgent/burrow) pour la messagerie chiffrée MLS entre agents IA et humains, et [Nostria Signer](https://github.com/nostria-app/nostria-signer-extension) pour le coffre-fort et la gestion d'identité dans le navigateur. Les approfondissements portent sur la signature Android NIP-55 et la synchronisation de portefeuille Cashu NIP-60.

## Actualités

### Améliorations de stabilité pour Notecrumbs

[Notecrumbs](https://github.com/damus-io/notecrumbs), l'API Nostr et le serveur web qui alimente les aperçus de liens damus.io, a reçu une série de correctifs traitant des problèmes de fiabilité.

Un [correctif de concurrence](https://github.com/damus-io/notecrumbs/commit/3f201f63ea49) a remplacé le mécanisme de déduplication des requêtes en vol par des canaux watch. Deux appelants demandant la même note pouvaient tous deux devenir récupérateurs, menant à un interblocage lorsque l'un terminait avant que l'autre ne s'abonne à la notification. Grâce aux canaux watch avec opérations atomiques, un seul récupérateur s'exécute tandis que les autres attendent le résultat.

La [limitation de débit](https://github.com/damus-io/notecrumbs/commit/b0d0bf5a2f17) implémente une défense à deux niveaux contre le martèlement des relays. Lorsque les utilisateurs accèdent de manière répétée à la même note, le système débonde maintenant les requêtes aux relays avec une fenêtre de refroidissement de 5 minutes. Cette protection s'étend à tous les types [NIP-19](/fr/topics/nip-19/) et aux flux de profils, empêchant le spam proportionnel vers les relays lors d'un trafic intense.

Un ensemble d'[améliorations de performance](https://github.com/damus-io/notecrumbs/commit/38670b3972b6) a déplacé les récupérations de données secondaires vers des tâches tokio en arrière-plan. Désormais les pages se rendent instantanément avec des données en cache au lieu de bloquer sur des timeouts de relays séquentiels qui pouvaient s'additionner jusqu'à 7,5 secondes. Une mise à niveau vers nostrdb 0.10.0 a accompagné ces correctifs.

### ContextVM : MCP sur Nostr

[ContextVM](https://contextvm.org) est une suite d'outils faisant le pont entre Nostr et le [Model Context Protocol](https://modelcontextprotocol.io/) (MCP). De récents commits ont introduit la nouvelle spécification [CEP-8](https://docs.contextvm.org/spec/ceps/cep-8/) permettant les paiements, et ont fait avancer les améliorations du [SDK](https://github.com/ContextVM/sdk) tout au long de février.

Le SDK fournit des transports client et serveur TypeScript pour MCP sur Nostr. Avec ce SDK, les développeurs peuvent exposer des serveurs MCP à travers le réseau Nostr et les clients peuvent s'y connecter. Agissant comme un bus de messages aveugle, les relays routent simplement les événements chiffrés de manière aveugle. Une couche proxy permet aux clients sans support Nostr natif de se connecter. La bibliothèque gère la gestion des relays et la signature cryptographique pour l'authentification des événements. Elle fonctionne dans les environnements Node.js et navigateur.

[CVMI](https://github.com/ContextVM/cvmi) fournit une CLI pour la découverte de serveurs et l'invocation de méthodes. [Relatr](https://github.com/ContextVM/relatr) calcule des scores de confiance personnalisés à partir de la distance du graphe social combinée à la validation de profil.

ContextVM se positionne comme une couche de pont : les serveurs MCP existants gagnent l'interopérabilité Nostr tout en maintenant leurs transports conventionnels.

### White Noise documente la recherche d'utilisateurs décentralisée

Un [article de blog de jgmontoya](https://blog.jgmontoya.com/2026/02/22/user-search.html) détaille comment [White Noise](https://github.com/marmot-protocol/whitenoise) gère la recherche d'utilisateurs à travers le réseau de relays décentralisé.

La distribution de profils crée le défi : contrairement aux messageries centralisées avec des bases de données unifiées, les profils Nostr se dispersent sur des dizaines de relays sans index central. White Noise résout cela grâce à une architecture producteur-consommateur fonctionnant en parallèle.

Un processus producteur étend continuellement le graphe social vers l'extérieur depuis les abonnements de l'utilisateur, récupérant les listes d'abonnements à des distances croissantes et mettant en file d'attente les pubkeys découvertes pour la résolution de profil. Le consommateur résout les correspondances à travers cinq niveaux de plus en plus coûteux : table d'utilisateurs locale (plus rapide), profils en cache de recherches précédentes, relays connectés, listes de relays utilisateur selon [NIP-65](/fr/topics/nip-65/) et requêtes directes vers les relays déclarés par l'utilisateur (plus lent).

Prenant environ 3 secondes, les recherches à froid sont nettement plus lentes que les recherches chaudes depuis le cache qui descendent à environ 10 millisecondes. Pour les nouveaux utilisateurs sans graphes sociaux établis, le système injecte des nœuds d'amorçage bien connectés pour assurer la fonctionnalité de recherche. L'appartenance à un groupe fournit un signal social implicite aux côtés des abonnements explicites.

L'instrumentation s'est avérée critical pour l'optimisation, note l'auteur. Sans métriques, les améliorations n'étaient que des suppositions.

### FIPS : réseau maillé natif Nostr

[FIPS](https://github.com/jmcorgan/fips) (Free Internetworking Peering System) est une implémentation Rust fonctionnelle d'un réseau maillé auto-organisé qui utilise les paires de clés Nostr (secp256k1) comme identités de nœuds. La [documentation de conception](https://github.com/jmcorgan/fips/blob/master/docs/design/fips-intro.md) accompagne le code fonctionnel.

Le protocole répond à l'indépendance d'infrastructure : les nœuds se découvrent automatiquement sans serveurs centraux ni autorités de certification. Un arbre couvrant fournit un routage basé sur les coordonnées tandis que les filtres bloom propagent les informations d'accessibilité, permettant aux nœuds de prendre des décisions de transfert avec seulement une connaissance locale. Grâce à l'agnosticisme de transport, le même protocole fonctionne sur UDP, Ethernet, Bluetooth, radio LoRa ou tout support capable de datagrammes.

Deux couches de chiffrement protègent le trafic. Pour la couche liaison, le chiffrement (pattern Noise IK) sécurise la communication saut par saut entre voisins avec authentification mutuelle et secret parfait de transmission. Au niveau session, le chiffrement (pattern Noise XK) fournit une protection de bout en bout contre les routeurs intermédiaires, où seule la destination peut déchiffrer la charge utile. Cela reflète la façon dont TLS protège le trafic HTTP même lors de la traversée de réseaux non fiables.

Utilisant un arbre couvrant greedy embedding pour le routage, l'architecture attribue à chaque nœud des coordonnées basées sur sa position par rapport à la racine de l'arbre et au parent. Routant de manière avide vers les coordonnées plus proches de la destination, les paquets bénéficient de filtres bloom annonçant les points d'accès accessibles. Lorsque le routage avide échoue (minima locaux), les nœuds peuvent se rabattre sur des chemins basés sur l'arbre.

Incluant déjà le transport UDP avec découverte par filtre bloom, l'implémentation Rust progresse rapidement. Le travail futur cible l'intégration de relays Nostr pour l'amorçage de pairs.

## Versions

Cette semaine a apporté des versions à travers l'infrastructure de relays et les applications clientes, avec de nouveaux projets entrant également dans l'espace.

### HAVEN v1.2.0

[HAVEN](https://github.com/bitvora/haven), le relay personnel tout-en-un regroupant quatre fonctions de relay avec un serveur média [Blossom](/fr/topics/blossom/), a livré [v1.2.0](https://github.com/bitvora/haven/releases/tag/v1.2.0). Cette version va au-delà du stade RC [couvert la semaine dernière](/fr/newsletters/2026-02-18-newsletter/#haven-v120-rc3).

Le support multi-npub permet à une seule instance HAVEN de servir plusieurs identités Nostr via whitelisting, avec une nouvelle fonctionnalité de blacklisting pour le contrôle d'accès. Réécrit entièrement, un système de sauvegarde utilise le format JSONL portable, avec une commande `haven restore` pour importer des notes depuis des fichiers JSONL. L'intégration de stockage cloud ajoute les flags `--to-cloud` et `--from-cloud` pour la gestion des sauvegardes distantes.

Parmi les améliorations de [Web of Trust](/fr/topics/web-of-trust/) : des niveaux de profondeur configurables pour les calculs de confiance et des intervalles de rafraîchissement automatique de 24 heures avec optimisation sans verrou réduisant la surcharge mémoire. Complétant la version, la configuration de user-agent pour les requêtes de relays et les paramètres de timeout Blastr configurables s'ajoutent à l'exportation de données vers JSONL compressé.

### White Noise v0.3.0

[White Noise](https://github.com/marmot-protocol/whitenoise), l'application de messagerie chiffrée basée sur [MLS](/fr/topics/mls/) implémentant le protocole [Marmot](/fr/topics/marmot/), a livré [v0.3.0](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.3.0) avec plus de 160 améliorations fusionnées.

Cette version apporte la messagerie en temps réel via des connexions en streaming au lieu du polling, de sorte que les messages arrivent instantanément. Avec le support Amber ([NIP-55](/fr/topics/nip-55/)), les clés privées n'ont jamais besoin de toucher l'application. Fonctionnant maintenant avec suivi de la progression du téléversement et des emplacements réservés blurhash lors du chargement, le partage d'images s'améliore grandement. L'affichage plein écran supporte le pincement pour zoomer.

Recevant des améliorations de fiabilité avec des listes de conversations montrant les noms d'expéditeur et le chiffrement [MLS](/fr/topics/mls/) assurant le secret parfait de transmission, la messagerie de groupe progresse également. S'étendant vers l'extérieur depuis les abonnements jusqu'à quatre degrés de séparation avec des résultats en streaming au fur et à mesure de leur découverte, la recherche d'utilisateurs devient plus puissante.

Un changement cassant réinitialise toutes les données locales lors de la mise à niveau en raison des changements du protocole Marmot et du passage au stockage local chiffré. Avant de mettre à niveau, sauvegardez vos clés nsec.

### diVine 1.0.5

[diVine](https://github.com/divinevideo/divine-mobile), le client vidéo courte en boucle construit sur les archives Vine restaurées, a livré [1.0.5](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.5) avec d'importants correctifs de lecture vidéo et un nouveau système d'analyse décentralisé.

Plusieurs problèmes de lecture vidéo ont dominé les correctifs. Pause fantôme résolue. Audio double entre vidéos éliminé. Flash noir entre miniatures et premières frames corrigé. Crashs de lecteur disposé tous résolus. Gérant maintenant le flux Home pour une lecture cohérente, un lecteur vidéo poolé remplace l'ancien système.

Permettant les analyses de créateurs et les recommandations, la version introduit des événements de visionnage éphémères Kind 22236. Suivant les sources de trafic (accueil, variantes de découverte, profil, partage, recherche) et les comptages de boucles tout en filtrant les auto-vues, le système fournit des métriques utiles. Corrigées avec des URLs Blossom canoniques construites côté client selon la spécification BUD-01, les fuites de chemins de fichiers locaux dans les tags imeta d'événements Nostr disparaissent.

Côté signataire distant [NIP-46](/fr/topics/nip-46/), plusieurs améliorations arrivent. Connexions de relays parallélisées implémentées. Support d'URL de rappel ajouté. Reconnectant les connexions WebSocket lors de la reprise de l'application après approbation du signataire, Android fonctionne mieux.

### Coracle 0.6.30

[Coracle](https://github.com/coracle-social/coracle), le client Nostr web axé sur la gestion de relays et la modération par [Web of Trust](/fr/topics/web-of-trust/), a livré [0.6.30](https://github.com/coracle-social/coracle/releases/tag/0.6.30) avec support des miniatures vidéo, améliorant la navigation média dans les flux.

### Nostur v1.26.0

[Nostur](https://github.com/nostur-com/nostur-ios-public), le client Nostr iOS, a livré [v1.26.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.26.0) avec une nouvelle section de flux Live Streams et un écran Paramètres repensé. Pouvant maintenant être hébergés sur des serveurs média Blossom, les GIFs réduisent la dépendance aux services centralisés. Fournissant une sauvegarde lorsque Tenor devient indisponible, l'intégration de GIFs Klipy aide. Complétant les changements visibles par l'utilisateur, des en-têtes d'année dans les conversations DM et l'affichage du comptage de mentions s'ajoutent.

Cette semaine a également apporté des mises à jour pour les outils de développement et les applications CLI.

### nak v0.18.5

[nak](https://github.com/fiatjaf/nak), le couteau suisse en ligne de commande pour Nostr de fiatjaf, a livré [v0.18.5](https://github.com/fiatjaf/nak/releases/tag/v0.18.5) avec une nouvelle sous-commande `nak profile` pour récupérer et afficher les profils utilisateur. Supportant maintenant les noms [NIP-05](/fr/topics/nip-05/) dans les URIs `nostr://`, la commande `git clone` permet le clonage de dépôts par identifiants lisibles par l'humain.

### Pika v0.5.3

[Pika](https://github.com/sledtools/pika), la messagerie chiffrée [MLS](/fr/topics/mls/) pour iOS, Android et desktop construite sur le protocole [Marmot](/fr/topics/marmot/), a livré [v0.5.3](https://github.com/sledtools/pika/releases/tag/pikachat-v0.5.3). Ajoutant le téléversement de fichiers et le support de glisser-déposer de médias à l'application desktop, aux côtés des correctifs de déploiement Cloudflare Workers, les commits récents améliorent l'expérience.

Utilisant un noyau Rust qui possède toute la logique métier tandis qu'iOS (SwiftUI) et Android (Kotlin) agissent comme des couches UI fines rendant des instantanés d'état, Pika adopte une architecture claire. Fournissant l'implémentation MLS, MDK (Marmot Development Kit) sert de base. Notant un statut alpha et mettant en garde contre l'utilisation pour des charges de travail sensibles, le projet reste expérimental.

### Ridestr v0.2.6

[Ridestr](https://github.com/variablefate/ridestr), la plateforme de covoiturage décentralisée avec paiements Cashu, a livré [v0.2.6](https://github.com/variablefate/ridestr/releases/tag/v0.2.6). Corrigeant des problèmes d'accessibilité TalkBack et résolvant des bugs où les conducteurs disparaissaient de la liste à proximité lors du changement de méthodes de paiement ou où les comptages de conducteurs sélectionnés ne se mettaient pas à jour lorsque les conducteurs passaient hors ligne, cette version améliore la stabilité.

Devenant Broadcast RoadFlare avec des correctifs pour les échecs silencieux sur les installations de conducteurs fraîches, la fonctionnalité Send to All évolue. Implémentant l'escrow HTLC pour les paiements de trajet sans confiance et la synchronisation de portefeuille [NIP-60](/fr/topics/nip-60/) sur les appareils, Ridestr progresse techniquement.

### Unfiltered v1.0.6

[Unfiltered](https://github.com/dmcarrington/unfiltered), l'application de partage de photos de type Instagram pour Android, a livré [v1.0.6](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.6) avec recherche d'utilisateurs améliorée et reconnexion automatique de relay toutes les 60 secondes.

Construit avec Kotlin et Jetpack Compose, Unfiltered utilise des liaisons rust-nostr et des serveurs compatibles Blossom pour l'hébergement d'images. Gérant la gestion sécurisée des clés, l'intégration Amber ([NIP-55](/fr/topics/nip-55/)) protège les utilisateurs. Montrant les publications des comptes suivis en ordre chronologique sans algorithmes ni publicités, l'application reste fidèle à l'esprit Nostr.

Deux nouveaux projets de messagerie et de signature ont également été lancés cette semaine.

### Burrow : messagerie MLS pour agents IA

[Burrow](https://github.com/CentauriAgent/burrow) est une messagerie implémentant le protocole [Marmot](/fr/topics/marmot/) pour la communication chiffrée MLS sans numéros de téléphone ni serveurs centralisés. Humains et agents IA peuvent tous participer.

Gérant l'intégration avec les systèmes automatisés, un daemon CLI Rust pur avec mode de sortie JSONL sert les besoins programmatiques. Couvrant Android, iOS, Linux, macOS et Windows, une application Flutter multiplateforme sert les utilisateurs humains. Chiffrant aux côtés des messages, les pièces jointes média restent protégées, et WebRTC gère les appels audio et vidéo avec des serveurs TURN configurables.

Superposant le chiffrement MLS sur l'infrastructure Nostr, Burrow utilise des paires de clés Nostr (secp256k1) pour l'identité tandis que les KeyPackages MLS publient comme événements kind 443. Pour les messages, le chiffrement [NIP-44](/fr/topics/nip-44/) produit des événements kind 445. Utilisant le gift-wrapping [NIP-59](/fr/topics/nip-59/), les invitations de bienvenue protègent les métadonnées.

Permettant la participation d'agents IA avec accès complet aux outils, l'intégration [OpenClaw](https://openclaw.ai) ouvre de nouvelles possibilités. Gérant les permissions de contacts et de groupes avec journalisation d'audit, les listes de contrôle d'accès assurent la sécurité. Positionnant Burrow pour les scénarios de messagerie agent-à-agent et agent-à-humain nécessitant un chiffrement de niveau Signal sur une infrastructure décentralisée, cette combinaison de fonctionnalités est puissante.

### Extension Nostria Signer

[Nostria Signer](https://github.com/nostria-app/nostria-signer-extension) est une extension de navigateur basée sur Chromium fournissant un coffre-fort et une gestion d'identité pour les utilisateurs Nostr.

Permettant aux utilisateurs d'organiser les identités pour différents contextes, plusieurs coffres contenant plusieurs comptes offrent de la flexibilité. Incluant le support des langues RTL, l'internationalisation est complète. Fonctionnant à la fois comme extension de navigateur et Progressive Web App, la construction avec Angular et TypeScript (79,2 % de la base de code) assure une bonne maintenabilité.

Implémentant [NIP-07](/fr/topics/nip-07/) pour la signature d'extension de navigateur, Nostria Signer permet aux clients Nostr web de demander des signatures d'événements sans accéder directement aux clés privées. Gérant les mises à jour distribuées via le Chrome Web Store, la migration automatique de portefeuille facilite la vie des utilisateurs. Restant également possible pour les utilisateurs avancés, le chargement depuis le dossier `dist/extension` offre une alternative.

Soulignant le statut expérimental, les développeurs insistent : les utilisateurs doivent gérer leurs propres phrases de récupération secrètes puisque les développeurs ne peuvent pas restaurer l'accès aux clés perdues.

## Mises à jour des projets

### Formstr migre vers une nouvelle organisation

[Formstr](https://github.com/formstr-hq/nostr-forms), l'alternative à Google Forms sur Nostr, a migré son dépôt de `abh3po/nostr-forms` vers l'organisation `formstr-hq`. Continuant le développement au nouvel emplacement, ce bénéficiaire de subvention OpenSats progresse.

### PRs ouvertes notables

Travail en cours à travers les projets Nostr :

- **Modèle Outbox Damus** ([PR #3602](https://github.com/damus-io/damus/pull/3602)) : Plan d'implémentation pour le modèle de relay gossip/outbox sur iOS. Améliorant la livraison de messages en publiant vers les relays où les destinataires lisent réellement, ce changement architectural est significatif.

- **Notifications multiplateforme Notedeck** ([PR #1296](https://github.com/damus-io/notedeck/pull/1296)) : Système de notifications natif pour le client desktop Damus couvrant Android FCM, macOS et Linux.

- **Mise à niveau Cashu v3 NDK** ([PR #370](https://github.com/nostr-dev-kit/ndk/pull/370)) : Met à jour l'intégration de portefeuille du Nostr Development Kit vers cashu-ts v3.

- **Zeus Cashu Offline** ([PR #3742](https://github.com/ZeusLN/zeus/pull/3742)) : Envoi et réception d'ecash hors ligne pour le portefeuille Lightning Zeus.

- **Livraison numérique chiffrée Shopstr** ([PR #231](https://github.com/shopstr-eng/shopstr/pull/231)) : Ajoute la livraison chiffrée pour les biens numériques avec support de poids dynamique pour les articles physiques.

## Mises à jour des NIP

Changements récents dans le [dépôt NIPs](https://github.com/nostr-protocol/nips) :

**Fusionnés cette semaine :**

- **[Découvrabilité du fournisseur de services NIP-85](https://github.com/nostr-protocol/nips/pull/2223)** : Incluant maintenant des conseils sur la façon dont les clients découvrent les fournisseurs d'assertions de confiance, la spécification [NIP-85](/fr/topics/nip-85/) s'améliore. Lorsqu'un client a besoin de scores de [Web of Trust](/fr/topics/web-of-trust/) ou d'autres métriques calculées, il peut interroger les relays pour les annonces kind 30085 des fournisseurs que l'utilisateur suit déjà ou en qui il a confiance.

- **[NIP-29 supprime les groupes non gérés](https://github.com/nostr-protocol/nips/pull/2229)** : Abandonnant le support des groupes non gérés (où tout membre pouvait ajouter d'autres), la spécification de chat de groupe [NIP-29](/fr/topics/nip-29/) se simplifie. Nécessitant maintenant une gestion côté relay avec des rôles d'administrateur explicites, tous les groupes NIP-29 deviennent plus contrôlables. Simplifiant les implémentations et réduisant les vecteurs de spam, ce changement améliore la sécurité.

- **[NIP-11 supprime les champs dépréciés](https://github.com/nostr-protocol/nips/pull/2231)** : N'incluant plus les champs dépréciés `software` et `version`, les documents d'information de relay [NIP-11](/fr/topics/nip-11/) se nettoient. Devant retirer ceux-ci de leurs réponses, les implémentations s'alignent.

- **[NIP-39 déplace les tags d'identité](https://github.com/nostr-protocol/nips/pull/2227)** : Déplacées des profils kind 0 vers des événements dédiés kind 30382, les revendications d'identité externe (tags `i` [NIP-39](/fr/topics/nip-39/) pour GitHub, Twitter, etc.) changent d'emplacement. Séparant la vérification d'identité des métadonnées de profil, ce changement clarifie les responsabilités.

**Progression des NIP d'agents IA :**

Continuant un développement actif, quatre NIP axés sur l'IA progressent. Depuis [la couverture de la semaine dernière](/fr/newsletters/2026-02-18-newsletter/#ai-agent-nips-arrive) :

- **[NIP-AE : Agents](https://github.com/nostr-protocol/nips/pull/2220)** (mis à jour le 19 février) : Définissant l'identité d'agent avec kind 4199 pour les définitions d'agent et kind 4201 pour le prompting (nudges), cette spec structure les agents. Pouvant référencer des métadonnées de fichier [NIP-94](/fr/topics/nip-94/) pour des descriptions étendues, les agents gagnent en expressivité.

- **[NIP-XX : AI Agent Messages](https://github.com/nostr-protocol/nips/pull/2226)** (mis à jour le 18 février) : Standardisant la messagerie conversationnelle avec sept kinds d'événements éphémères (25800-25806) pour le statut, les deltas en streaming, les prompts, les réponses, les appels d'outils, les erreurs et l'annulation, cette spec couvre beaucoup. Permettant aux agents d'annoncer les modèles et capacités supportés, les événements AI Info kind 31340 facilitent la découverte.

- **[NIP-AC : DVM Agent Coordination](https://github.com/nostr-protocol/nips/pull/2228)** (ouvert le 18 février) : Étendant [NIP-90](/fr/topics/nip-90/) pour les flux de travail d'agents autonomes, cette proposition ajoute beaucoup. Heartbeats pour la découverte d'agents. Revues de tâches pour le suivi de qualité. Escrow de données pour l'engagement de résultats. Chaînes de flux de travail pour les pipelines multi-étapes. Enchère en essaim pour la sélection de fournisseurs compétitifs. Fonctionnant sur 2020117.xyz, une implémentation de référence existe.

- **[NIP-AD : MCP Server Announcements](https://github.com/nostr-protocol/nips/pull/2221)** (ouvert le 12 février) : Standardisant l'annonce de serveurs Model Context Protocol et de compétences sur Nostr, cette spec trouve déjà un usage. Déjà utilisée sur la plateforme TENEX, l'adoption commence.

**Autres PRs ouvertes :**

- **[NIP-144 : Service Authorization Protocol](https://github.com/nostr-protocol/nips/pull/2232)** : Définissant comment les clients prouvent l'identité et les permissions aux fournisseurs de services sur Nostr, cette spec aborde l'autorisation.

- **[NIP-DC : Nostr Webxdc](https://github.com/nostr-protocol/nips/pull/2230)** : Proposant d'intégrer Webxdc (applications web décentralisées) avec les événements Nostr, alexgleason explore de nouvelles directions.

## Approfondissement NIP : NIP-55 (Android Signer Application)

[NIP-55](https://github.com/nostr-protocol/nips/blob/master/55.md) définit comment les clients Nostr Android demandent des opérations cryptographiques à des applications de signature dédiées. Ajoutant tous deux le support Amber cette semaine, [White Noise v0.3.0](#white-noise-v030) et [Unfiltered v1.0.6](#unfiltered-v106) justifient un examen du protocole de signature Android.

**Canaux de communication :**

Permettant la signature inter-applications via deux mécanismes, NIP-55 offre de la flexibilité. Fournissant une approbation manuelle de l'utilisateur avec feedback visuel pour les opérations ponctuelles, les Intents conviennent aux actions explicites. Permettant la signature automatisée lorsque les utilisateurs accordent des permissions persistantes, les Content Resolvers autorisent les applications à signer en arrière-plan sans invites répétées.

Utilisant le schéma URI personnalisé `nostrsigner:`, la communication reste simple. Un client initie le contact avec :

```
nostrsigner:<base64-encoded-event>?type=sign_event&callbackUrl=myapp://callback
```

**Opérations supportées :**

La spec définit sept méthodes cryptographiques. Signature d'événement (`sign_event`). Récupération de clé publique (`get_public_key`). Opérations de chiffrement et déchiffrement [NIP-04](/fr/topics/nip-04/). Opérations de chiffrement et déchiffrement [NIP-44](/fr/topics/nip-44/). Déchiffrement d'événement zap (`decrypt_zap_event`).

**Modèle de permissions :**

Appelant `get_public_key` une fois pour établir une relation de confiance, les clients reçoivent le nom de paquet du signataire et la pubkey de l'utilisateur. Imposant que les clients sauvegardent ces valeurs et n'appellent jamais `get_public_key` à nouveau, la spec empêche les attaques de fingerprinting.

Pouvant approuver une fois ou accorder se souvenir de mon choix pour les opérations en arrière-plan, les utilisateurs contrôlent les permissions pour les requêtes de signature. Retournant un statut rejected et empêchant les invites répétées si les utilisateurs rejettent systématiquement les opérations, le signataire protège l'expérience utilisateur.

**Implémentations :**

Servant de signataire NIP-55 principal pour Android, [Amber](https://github.com/greenart7c3/amber) domine. Parmi les clients supportant NIP-55 : [Amethyst](https://github.com/vitorpamplona/amethyst), [White Noise](#white-noise-v030), [Unfiltered](#unfiltered-v106) et d'autres. Ne pouvant pas recevoir directement les réponses du signataire et devant utiliser des URLs de rappel ou des opérations de presse-papiers, les applications web ont des contraintes.

**Relation avec d'autres NIP de signature :**

Complétant [NIP-07](/fr/topics/nip-07/) (extensions de navigateur) et [NIP-46](/fr/topics/nip-46/) (signature à distance sur relays), NIP-55 s'intègre dans un écosystème. Là où NIP-07 gère les navigateurs de bureau et NIP-46 gère la signature inter-appareils, NIP-55 fournit une intégration Android native avec latence minimale.

## Approfondissement NIP : NIP-60 (Cashu Wallet)

[NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md) définit comment les portefeuilles ecash [Cashu](/fr/topics/cashu/) stockent l'état sur les relays Nostr, permettant la synchronisation de portefeuille inter-applications. Utilisant NIP-60 pour la synchronisation de portefeuille sur les appareils, [Ridestr v0.2.6](#ridestr-v026) justifie un examen du protocole.

**Kinds d'événements :**

Utilisant quatre types d'événements, NIP-60 structure l'état du portefeuille. Stockant la configuration du portefeuille incluant les URLs de mint et une clé privée dédiée pour recevoir les paiements ecash P2PK, le kind remplaçable 17375 contient les paramètres essentiels. Contenant des preuves cryptographiques non dépensées, les événements de jetons (kind 7375) gardent les fonds. Enregistrant les transactions pour la transparence de l'utilisateur, l'historique de dépenses (kind 7376) aide au suivi. Suivant les quotes de paiement de mint, un kind optionnel 7374 complète l'ensemble.

**Architecture du portefeuille :**

Vivant sur les relays et le rendant accessible à travers les applications, l'état du portefeuille se décentralise. Contenant des références chiffrées aux mints Cashu et une clé privée spécifique au portefeuille séparée de l'identité Nostr de l'utilisateur, l'événement de portefeuille d'un utilisateur sépare les préoccupations. Gérant les opérations ecash tandis que la clé Nostr gère les fonctions sociales, cette séparation de la clé de portefeuille compte.

```json
{
  "kind": 17375,
  "content": "<nip44-encrypted-wallet-config>",
  "tags": [["d", "cashu-wallet"]]
}
```

**Gestion des preuves :**

Étant des instruments au porteur qui deviennent invalides une fois dépensés, les preuves Cashu nécessitent une gestion soigneuse. Gérant cela via un mécanisme de roulement, NIP-60 maintient la cohérence. Lors de la dépense, les clients créent un nouvel événement de jeton avec les preuves non dépensées restantes et suppriment l'original via [NIP-09](/fr/topics/nip-09/). Allant dans un champ `del` pour le suivi d'état, les IDs de jetons détruits restent traçables.

Devant périodiquement valider les preuves contre les mints pour détecter les credentials précédemment dépensés, les clients maintiennent la sécurité. Étant permis avec plusieurs événements de jetons par mint, la flexibilité existe. Aidant les utilisateurs à suivre les transactions même s'ils sont optionnels, les événements d'historique de dépenses améliorent l'expérience.

**Modèle de sécurité :**

Utilisant le chiffrement [NIP-44](/fr/topics/nip-44/), toutes les données sensibles restent protégées. N'apparaissant jamais en clair, la clé privée du portefeuille demeure secrète. Stockant des blobs chiffrés sans comprendre leurs contenus, les relays ne peuvent pas violer la vie privée. Restant privé même sur des relays non fiables, l'état du portefeuille bénéficie d'une architecture zero-knowledge.

**Implémentations :**

Supportant NIP-60, plusieurs portefeuilles adoptent le standard. [Nutsack](https://github.com/gandlafbtc/nutsack) implémente. [eNuts](https://github.com/cashubtc/eNuts) également. Utilisant NIP-60 pour la synchronisation inter-appareils et permettant aux utilisateurs de recharger sur desktop et de dépenser depuis mobile sans transferts manuels, les clients comme [Ridestr](#ridestr-v026) démontrent la valeur.

---

C'est tout pour cette semaine. Vous construisez quelque chose ou avez des actualités à partager ? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contactez-nous via [NIP-17](/fr/topics/nip-17/) DM</a> ou retrouvez-nous sur Nostr.
