---
title: 'Nostr Compass #10'
date: 2026-02-18
translationOf: /en/newsletters/2026-02-18-newsletter.md
translationDate: 2026-02-18
draft: false
type: newsletters
---

Bienvenue dans Nostr Compass, votre guide hebdomadaire sur Nostr.

**Cette semaine :** Une couche de cache local Blossom prend forme à mesure que des projets indépendants convergent vers l'accès hors ligne aux médias sur Android. Alby lance un [bac à sable NWC pour développeurs](https://sandbox.albylabs.com) permettant de construire et tester des intégrations Nostr Wallet Connect sans risquer de vrais fonds. Des propositions concurrentes pour la communication d'agents IA sur Nostr arrivent la même semaine de deux auteurs différents. fiatjaf supprime les champs inutilisés de [NIP-11](https://github.com/nostr-protocol/nips/pull/1946), retirant les politiques de rétention, codes pays, politiques de confidentialité et tags de préférence communautaire que les opérateurs de relay n'ont jamais adoptés. [NIP-85](https://github.com/nostr-protocol/nips/pull/2223) fusionne les conseils de découverte de fournisseurs de services pour les Trusted Assertions. Un nouveau tag `D` dans [NIP-52](https://github.com/nostr-protocol/nips/pull/1752) active l'indexation des événements de calendrier à la granularité journalière. Parmi les nouveaux projets : [Mapnolia](https://github.com/zeSchlausKwab/mapnolia) pour la distribution décentralisée de tuiles cartographiques, [Pika](https://github.com/sledtools/pika) pour la messagerie chiffrée MLS, [Keep](https://github.com/privkeyio/keep-android) pour la signature à seuil FROST sur Android, [Hashtree](https://files.iris.to/#/npub1xndmdgymsf4a34rzr7346vp8qcptxf75pjqweh8naa8rklgxpfqqmfjtce/hashtree) pour le stockage adressé par contenu avec intégration Nostr, et [Prism](https://github.com/hardran3/Prism) pour partager du contenu vers Nostr depuis n'importe quelle application Android. [Primal Android](https://github.com/PrimalHQ/primal-android-app) fusionne 11 PRs NWC ajoutant le support double portefeuille et le cycle de vie automatique du service. [Mostro Mobile](https://github.com/MostroP2P/mobile) livre un [portefeuille Lightning intégré](https://github.com/MostroP2P/mobile/releases/tag/v1.2.0%2B2) via l'intégration NWC. [Notedeck](https://github.com/damus-io/notedeck) prépare sa sortie sur l'App Store Android tandis que HAVEN atteint [v1.2.0-rc3](https://github.com/bitvora/haven/releases/tag/v1.2.0-rc3) avec le support multi-npub et la sauvegarde cloud. Les approfondissements de cette semaine portent sur le système Trusted Assertions de NIP-85 pour déléguer les calculs de Web of Trust à des fournisseurs de services, et sur le protocole Événements de Calendrier de NIP-52 suite à sa mise à jour d'indexation à la granularité journalière.

## Actualités

### Une couche de cache local Blossom émerge

Plusieurs projets indépendants convergent vers le même problème : l'accès hors ligne aux médias [Blossom](/fr/topics/blossom/) sur les appareils mobiles.

[Morganite](https://github.com/greenart7c3/Morganite), une nouvelle application Android de greenart7c3 (le développeur derrière [Amber](https://github.com/greenart7c3/amber) et [Citrine](https://github.com/greenart7c3/Citrine)), implémente un cache côté client pour les médias Blossom. Les utilisateurs peuvent accéder aux images et fichiers précédemment consultés sans connexion réseau.

[Aerith](https://github.com/hardran3/Aerith) a livré [v0.2](https://github.com/hardran3/Aerith/releases/tag/v0.2) avec l'étiquetage d'images, les opérations de miroir/tag/suppression en masse, le filtrage par étiquette et type de fichier, ainsi que le support initial du cache Blossom local. Aerith est une interface de gestion pour les utilisateurs qui stockent des médias sur plusieurs serveurs Blossom et ont besoin d'organiser et de mettre en miroir leurs blobs.

Un nouveau [guide d'implémentation du cache local](https://github.com/hzrd149/blossom/blob/master/implementations/local-blossom-cache.md) dans la spécification Blossom documente le stockage de blobs côté client, tandis que [Prism](https://github.com/hardran3/Prism) (du même développeur qu'Aerith) ajoute l'intégration de téléversement Blossom à son flux de partage vers Nostr sur Android. Quatre projets indépendants ont convergé vers le même problème cette semaine : une application de cache dédiée, un gestionnaire de médias, une spécification de référence et un outil de partage avec intégration Blossom, tous implémentant un stockage local persistant au-delà du simple téléversement et récupération.

### Bac à sable NWC d'Alby pour les développeurs

[Alby](https://sandbox.albylabs.com) a lancé un environnement bac à sable pour les développeurs qui construisent avec [Nostr Wallet Connect (NIP-47)](/fr/topics/nip-47/). Le bac à sable fournit un service de portefeuille NWC hébergé où les développeurs peuvent créer des connexions de test et envoyer des paiements simulés sans connecter un vrai portefeuille Lightning, tout en observant le cycle complet requête/réponse des événements NWC en temps réel. Les développeurs génèrent une chaîne de connexion `nostr+walletconnect://` depuis le bac à sable et la transmettent à leur client. Le bac à sable affiche alors les événements de requête kind 23194 et de réponse kind 23195 résultants au fur et à mesure qu'ils transitent entre le client et le service de portefeuille.

Cela abaisse la barrière pour les nouvelles intégrations NWC. Auparavant, les tests nécessitaient soit un portefeuille Lightning personnel, soit un service NWC auto-hébergé. Le bac à sable abstrait tout cela, donnant aux développeurs une boucle de rétroaction immédiate pour implémenter les méthodes `pay_invoice`, `get_balance`, `make_invoice`, `lookup_invoice` et `list_transactions` contre un point d'accès NWC en direct.

### Des NIP pour les agents IA arrivent

Des propositions pour la communication d'agents IA sur Nostr sont apparues à quelques jours d'intervalle, abordant le problème sous des angles différents.

[NIP-XX : AI Agent Messages](https://github.com/nostr-protocol/nips/pull/2226) de joelklabo définit un protocole complet pour l'interaction d'agents IA : kinds d'événements pour les prompts, réponses, deltas en streaming, mises à jour de statut, télémétrie d'outils, erreurs, annulations et découverte de capacités. Un événement de découverte `ai.info` (kind 31340, remplaçable) permet aux agents d'annoncer leurs modèles supportés, outils avec schémas, support du streaming et limites de débit. La proposition de joelklabo inclut la corrélation d'exécutions via l'ID de prompt, la gestion de sessions, la réconciliation de flux avec ordonnancement par séquence, et des conseils [NIP-59](/fr/topics/nip-59/) pour la confidentialité des métadonnées.

[NIP-AE : Agents](https://github.com/nostr-protocol/nips/pull/2220) de pablof7z adopte une approche différente, définissant des kinds pour l'instanciation d'agents : définitions et leçons. Ce sont les types d'événements que pablof7z utilise dans [TENEX](https://github.com/tenex-chat/tenex), le système d'apprentissage autonome construit sur Nostr. Une proposition complémentaire, [NIP-AD : MCP Server and Skill Announcements](https://github.com/nostr-protocol/nips/pull/2221), également de pablof7z, définit des événements pour annoncer les serveurs [Model Context Protocol](https://modelcontextprotocol.io/) et les compétences sur Nostr. Les commentaires [NIP-22](/fr/topics/nip-22/) sont supportés, permettant à la communauté de discuter et d'évaluer les serveurs MCP directement sur Nostr.

NIP-XX couvre la communication complète entre agents tandis que NIP-AE et NIP-AD traitent de l'identité et de la découverte d'outils. Ces propositions pourraient converger vers un standard unifié ou coexister comme des couches complémentaires.

## Versions

### HAVEN v1.2.0-rc3

[HAVEN](https://github.com/bitvora/haven), le relay personnel tout-en-un qui regroupe quatre fonctions de relay avec un serveur média [Blossom](/fr/topics/blossom/), a atteint [v1.2.0-rc3](https://github.com/bitvora/haven/releases/tag/v1.2.0-rc3). Cette version candidate ajoute le support de plusieurs npubs, permettant à une seule instance HAVEN de servir plusieurs identités Nostr. Les RC précédents ont ajouté les flags `--from-cloud` et `--to-cloud` pour la sauvegarde cloud (RC2) et corrigé un bug de double comptage dans le Web of Trust (RC1).

### Mostro Mobile v1.2.0 : portefeuille Lightning intégré

[Mostro Mobile](https://github.com/MostroP2P/mobile), le client mobile pour la plateforme d'échange Bitcoin P2P [Mostro](https://github.com/MostroP2P/mostro) ([v1.1.0 couvert la semaine dernière](/fr/newsletters/2026-02-11-newsletter/#mostro-livre-sa-première-bêta-publique)), a livré [v1.2.0](https://github.com/MostroP2P/mobile/releases/tag/v1.2.0%2B2) avec un portefeuille Lightning intégré grâce à l'intégration complète de [NWC (NIP-47)](/fr/topics/nip-47/). Les acheteurs et vendeurs n'ont plus besoin de changer d'application pour gérer les factures. L'application détecte les hold invoices pour les vendeurs et les paie automatiquement via le portefeuille connecté, tandis que les acheteurs bénéficient de la génération automatique de factures. Cette version fait suite à [v1.1.1](https://github.com/MostroP2P/mobile/releases/tag/v1.1.1%2B1) publiée plus tôt dans la semaine, qui a ajouté le support multi-nœud Mostro avec un registre curé d'instances de confiance, la récupération des métadonnées kind 0 pour l'affichage des nœuds, la gestion de nœuds personnalisés par pubkey, et le basculement automatique lorsqu'un nœud sélectionné est hors ligne.

Côté serveur, [Mostro v0.16.2](https://github.com/MostroP2P/mostro/releases/tag/v0.16.2) a atterri avec des correctifs pour les paiements de frais de développement en double, la limitation de débit sur le point d'accès RPC de validation de mot de passe, et le nettoyage correct des litiges lors d'annulations coopératives.

Un nouveau projet compagnon, [mostro-skill](https://github.com/MostroP2P/mostro-skill), permet aux agents d'échanger sur Mostro via Nostr.

### Aerith v0.2

[Aerith](https://github.com/hardran3/Aerith), le gestionnaire d'images [Blossom](/fr/topics/blossom/), a livré [v0.2](https://github.com/hardran3/Aerith/releases/tag/v0.2) avec des étiquettes d'images pour organiser les médias, les opérations de miroir/tag/suppression en masse sur plusieurs serveurs, le filtrage par étiquette et type de fichier, ainsi que le support initial du cache local. Voir la [section Actualités](#une-couche-de-cache-local-blossom-émerge) pour le contexte sur la tendance plus large du cache local.

### Mapnolia : tuiles cartographiques décentralisées sur Nostr

[Mapnolia](https://github.com/zeSchlausKwab/mapnolia) est un nouveau serveur de données géospatiales qui découpe les archives de tuiles cartographiques [PMTiles](https://github.com/protomaps/PMTiles) en régions géographiques et les annonce sur Nostr pour une découverte décentralisée. Il publie des événements remplaçables paramétrés kind 34444 vers les relays Nostr contenant un index complet des fragments de tuiles cartographiques avec les métadonnées de couches, les régions géohash, les références de fichiers et les détails du serveur [Blossom](/fr/topics/blossom/).

Les clients découvrent et récupèrent les données cartographiques via le réseau Nostr plutôt que des serveurs de tuiles centralisés, les événements d'annonce portant suffisamment de métadonnées pour ne demander que les régions géographiques nécessaires aux serveurs Blossom listés. Mapnolia est le premier projet à apporter la distribution de données géospatiales sur Nostr, ouvrant des possibilités pour des applications cartographiques capables de fonctionner hors ligne.

### Pika : messagerie chiffrée basée sur Marmot

[Pika](https://github.com/sledtools/pika) est une nouvelle application de messagerie chiffrée de bout en bout pour iOS et Android utilisant le protocole [Marmot](/fr/topics/marmot/), qui superpose [Messaging Layer Security (MLS)](/fr/topics/mls/) sur les relays Nostr. L'architecture sépare les préoccupations en un noyau Rust (`pika_core`) gérant l'état MLS et le chiffrement/déchiffrement des messages sur les relays Nostr, avec des interfaces utilisateur natives légères en SwiftUI (iOS) et Kotlin (Android). L'état circule de façon unidirectionnelle : l'UI envoie des actions à l'acteur Rust, qui modifie l'état et émet des instantanés avec des numéros de révision vers l'UI via les liaisons UniFFI et JNI.

Pika rejoint un champ croissant de messageries MLS-sur-Nostr aux côtés de [White Noise](https://github.com/marmot-protocol/whitenoise), [Vector](https://github.com/VectorPrivacy) et [0xchat](https://0xchat.com). Toutes utilisent les relays Nostr comme couche de transport pour le texte chiffré MLS, empêchant les opérateurs de relay de lire le contenu des messages. Pika utilise le Marmot Development Kit (MDK) pour son implémentation MLS et nostr-sdk pour la connectivité aux relays.

### Keep : signature à seuil [FROST](/fr/topics/frost/) pour Android

[Keep](https://github.com/privkeyio/keep-android) est une nouvelle application Android pour la signature à seuil [FROST](/fr/topics/frost/) où aucun appareil unique ne détient la clé privée complète. Elle implémente [NIP-55](/fr/topics/nip-55/) (signataire Android) et [NIP-46](/fr/topics/nip-46/) (signature à distance), de sorte que les clients Nostr compatibles peuvent demander des signatures tandis que le matériel de clé reste distribué sur plusieurs appareils. Les configurations par défaut sont 2-sur-3 et 3-sur-5, bien que tout seuil t-sur-n soit supporté.

La cérémonie de génération de clés distribuées (DKG) de Keep s'exécute sur les relays Nostr en utilisant des kinds d'événements personnalisés : kind 21101 pour les annonces de groupe, kind 21102 pour les polynômes d'engagement du tour 1 (diffusés publiquement), et kind 21103 pour les parts secrètes du tour 2 (chiffrement point-à-point [NIP-44](/fr/topics/nip-44/) entre participants). Le scalaire de clé privée du groupe n'est jamais calculé ni assemblé nulle part durant le DKG. Chaque appareil ne détient que sa part d'évaluation polynomiale, et n'importe quelles t parts peuvent produire une signature Schnorr valide via un protocole en deux tours commit-puis-signer. La signature de 64 octets résultante est indiscernable d'une signature Schnorr à signataire unique. En coulisse, Keep utilise le crate `frost-secp256k1-tr` de la Zcash Foundation avec tweaking Taproot, de sorte que la clé publique de groupe fonctionne directement comme un npub Nostr.

Keep rejoint la famille de projets [Frostr](https://frostr.org) aux côtés d'[Igloo Desktop](https://github.com/FROSTR-ORG/igloo-desktop), [Igloo for Android](https://github.com/FROSTR-ORG/igloo-android), [Frost2x](https://github.com/FROSTR-ORG/frost2x) et [Igloo for iOS](https://github.com/FROSTR-ORG/igloo-ios), élargissant les options de gestion de clés à seuil sur Nostr.

### Prism : partager n'importe quoi vers Nostr depuis Android

[Prism](https://github.com/hardran3/Prism) est une nouvelle application Android (Kotlin/Jetpack Compose, API 26+) qui s'enregistre comme cible de partage système, permettant aux utilisateurs de publier du texte, des URLs, des images et des vidéos vers Nostr depuis n'importe quelle application de leur téléphone. Les URLs partagées passent par un extracteur de paramètres de suivi avant d'être composées en notes. Prism récupère les métadonnées OpenGraph pour générer des aperçus de liens enrichis et rend les références Nostr natives (`note1`, `nevent1`) inline.

Le moteur de planification utilise une approche hybride `AlarmManager`/`WorkManager` pour contourner les optimisations de batterie Android : AlarmManager gère le timing précis du réveil tandis que les tâches WorkManager expéditives assurent la livraison, avec une relance à backoff exponentiel pour les scénarios hors ligne. Les téléversements de médias passent par des serveurs [Blossom](/fr/topics/blossom/) configurables avec génération de miniatures pour les images et les frames vidéo. Toute la signature d'événements est déléguée aux signataires externes [NIP-55](/fr/topics/nip-55/) comme [Amber](https://github.com/greenart7c3/amber), avec un support multi-compte pour basculer entre les identités. Prism supporte également les publications [NIP-84 (Highlights)](/fr/topics/nip-84/). Du même développeur qu'[Aerith](#aerith-v02).

### Hashtree : stockage adressé par contenu avec intégration Nostr

[Hashtree](https://files.iris.to/#/npub1xndmdgymsf4a34rzr7346vp8qcptxf75pjqweh8naa8rklgxpfqqmfjtce/hashtree) est un système de stockage de blobs adressé par contenu basé sur le système de fichiers qui publie les racines Merkle sur Nostr pour créer des adresses mutables npub/chemin. Le système utilise un « stockage muet » fonctionnant avec tout magasin clé-valeur, découpant le contenu en blocs de 2 Mo optimisés pour les téléversements [Blossom](/fr/topics/blossom/). Contrairement à BitTorrent, aucun calcul actif de preuves Merkle n'est nécessaire — il suffit de stocker et de récupérer les blobs par hash.

L'intégration Nostr permet des URLs de dépôt git comme `htree://npub.../nom-depot` pour cloner des dépôts, avec des commandes comme `htree publish mydata <hash>` pour publier des hashes de contenu vers les adresses `npub.../mydata`. Le CLI complet supporte les modes de stockage chiffré (par défaut) et public, l'épinglage de contenu, la publication vers les serveurs Blossom et la gestion des identités Nostr. Chaque élément stocké est soit des octets bruts soit un nœud d'arbre, fournissant une base pour la distribution de contenu décentralisée via le réseau de relays Nostr.

### Espy : capture de palettes de couleurs sur Shakespeare

[Espy](https://espy.you), construit sur la plateforme [Shakespeare](https://soapbox.pub/tools/shakespeare/), permet aux utilisateurs de capturer des palettes de couleurs à partir de photos et de les partager comme événements Nostr. Shakespeare est un créateur d'applications propulsé par l'IA qui authentifie les utilisateurs via les extensions de navigateur NIP-07 et fournit une connectivité relay Nostr intégrée, de sorte que les développeurs livrent des applications sans implémenter leur propre gestion de clés ou pool de relays. Espy extrait les couleurs dominantes de la prise de vue de l'appareil photo en cartes de palettes partageables, découvrables via les flux Nostr standard.

### Flotilla 1.6.4

[Flotilla](https://gitea.coracle.social/coracle/flotilla), le client Nostr style Discord de hodlbod qui organise les relays comme des groupes, a livré [1.6.4](https://gitea.coracle.social/coracle/flotilla/releases/tag/1.6.4). La famille de projets Coracle a migré de GitHub vers une [instance Gitea auto-hébergée](https://gitea.coracle.social/coracle). Cette version ajoute les notifications push via NIP-9a et un flux de réception de portefeuille, ainsi que les annonces classifiées et le support d'URL d'espace. Les améliorations d'interface incluent les modales nettoyées et la gestion des notifications. La mise en sourdine des salles et les encoches de zone de sécurité sur mobile complètent les changements, avec des correctifs pour les téléversements d'images Safari et les détails d'événements de calendrier.

### Shosho v0.12.0

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), l'application mobile de streaming en direct avec intégration Nostr, a livré [v0.12.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.12.0). Cette version ajoute des Clips vidéo avec réponses dans le lecteur et intégration d'émojis personnalisés. La protection de fil bloque le spam de mentions indirectes, et une nouvelle fonctionnalité de partage QR permet aux utilisateurs d'échanger des profils hors ligne. Un nouveau mode de lecture horizontal donne aux flux une expérience de visionnage style Twitch, et l'écran de navigation présente maintenant les clips de créateurs aux côtés des flux en direct.

### Granary v10.0

[Granary](https://github.com/snarfed/granary), une bibliothèque de traduction du web social qui convertit des données entre Nostr, Bluesky, ActivityPub et d'autres plateformes dans un format commun, a livré [v10.0](https://github.com/snarfed/granary/releases/tag/v10.0) avec des changements cassants. La version bascule les IDs ActivityStreams 1 par défaut de Nostr de bech32 vers hex et ajoute un support Nostr étendu incluant l'analyse des mentions [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) et les tags d'articles. Une nouvelle option de sortie multiple à travers les convertisseurs permet aux développeurs de traduire entre protocoles en lot.

### Nostr MCP Server v3.0.0

[Nostr MCP Server](https://github.com/AustinKelsay/nostr-mcp-server), un serveur [Model Context Protocol](https://modelcontextprotocol.io/) qui permet aux agents IA d'interagir avec le réseau Nostr, a livré [v3.0.0](https://github.com/AustinKelsay/nostr-mcp-server/releases/tag/v3.0.0). Cette version majeure ajoute les actions sociales (abonnements, réactions, reposts, réponses) et la gestion des listes de relays avec le support [NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md) plus l'authentification optionnelle [NIP-42](/fr/topics/nip-42/). La messagerie directe via [NIP-17](/fr/topics/nip-17/) et [NIP-44](/fr/topics/nip-44/) est également nouvelle. La version s'associe aux [propositions de NIP pour agents IA](#des-nip-pour-les-agents-ia-arrivent) de cette semaine comme outillage pratique pour les agents opérant sur Nostr.

### Aegis v0.3.8

[Aegis](https://github.com/ZharlieW/Aegis), le signataire Nostr multiplateforme, a livré [v0.3.8](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.8) avec le support multilingue de l'interface et un gestionnaire de mises à jour incrémentales pour son navigateur d'applications Nostr intégré. Le nouveau mécanisme de mise à jour effectue des diffs incrémentaux par rapport à l'état local, maintenant le répertoire d'applications web Nostr dans l'application à jour avec une utilisation de bande passante réduite. La version introduit également un cache de matériel de clés de 5 minutes pour réduire les allers-retours en base de données lors de la signature de plusieurs événements consécutifs.

### SNSTR v0.3.1

[SNSTR](https://github.com/AustinKelsay/snstr) (Secure Nostr Software Toolkit for Renegades), une bibliothèque TypeScript pour le protocole Nostr, a livré [v0.3.1](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.1). La version ajoute des gardes de vérification de paquets s'assurant que tous les points d'entrée sont inclus dans les archives npm, avec application CI sur Node et Bun. [v0.3.0](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.0) a été livré la même semaine.

### Citrine v2.0.0-pre1

[Citrine](https://github.com/greenart7c3/Citrine), le relay Nostr Android de greenart7c3, a publié [v2.0.0-pre1](https://github.com/greenart7c3/Citrine/releases/tag/v2.0.0-pre1) avec des améliorations de performance via des index de base de données optimisés et une meilleure gestion des coroutines Kotlin. La version améliore également le support pour l'hébergement d'applications web, chaque application fonctionnant désormais sur son propre port.

## Mises à jour des projets

### Primal Android : expansion de l'infrastructure NWC

[Primal Android](https://github.com/PrimalHQ/primal-android-app) a fusionné 11 PRs liés à NWC cette semaine, poursuivant la construction [commencée il y a deux semaines](/fr/newsletters/2026-02-04-newsletter/#primal-android-livre-le-chiffrement-nwc). Ce lot ajoute le support NWC double portefeuille, le démarrage/arrêt automatique du service lié aux notifications backend, le routage des connexions par type de portefeuille, et un nettoyage correct des données lors de la suppression d'un portefeuille. Le service NWC gère maintenant son propre cycle de vie en fonction de l'état de connexion du portefeuille, réduisant l'intervention manuelle de l'utilisateur.

### Notedeck : préparation pour l'App Store Android

[Notedeck](https://github.com/damus-io/notedeck), le client Nostr multiplateforme de l'équipe [Damus](https://github.com/damus-io/damus), a fusionné la [préparation à la sortie sur l'App Store Android](https://github.com/damus-io/notedeck/pull/1287) cette semaine. La PR ajoute un plan de conformité UGC (User Generated Content) requis par Google Play, incluant un écran d'acceptation des Conditions d'utilisation, le blocage d'utilisateurs via les menus contextuels et les paramètres, la fonctionnalité [NIP-56 (Signalement)](/fr/topics/nip-56/) qui publie des événements de rapport aux relays, et une section Paramètres Contenu et Sécurité. Une infrastructure de build a été ajoutée pour générer des APK de publication signés et des AAB (Android App Bundles) via de nouvelles cibles Makefile. Un document EULA établit une exigence d'âge de 17 ans et des clauses de non-responsabilité spécifiques à Nostr concernant le contenu décentralisé. Les fonctionnalités de conformité elles-mêmes seront livrées dans des PRs de suivi ; cette fusion pose les bases de documentation et de signature.

Du côté de Damus iOS, un correctif a atterri pour une [régression de spinner de chargement infini](https://github.com/damus-io/damus/pull/3593) où le spinner persistait indéfiniment après le chargement du contenu.

### Nostria : relays de découverte et correctifs DM

[Nostria](https://github.com/nostria-app/nostria), le client Nostr multiplateforme axé sur l'échelle mondiale, a fusionné 9 PRs cette semaine. La plus notable ajoute l'[auto-initialisation des Discovery Relays](https://github.com/nostria-app/nostria/pull/460) pour la recherche de profils, donnant aux nouveaux utilisateurs une connectivité relay fonctionnelle sans configuration manuelle. D'autres correctifs traitent du [retour à la ligne dans les zones de texte DM](https://github.com/nostria-app/nostria/pull/466), du [remplissage du viewport en plein écran pour les vidéos](https://github.com/nostria-app/nostria/pull/479), de l'[extraction de métadonnées d'articles dans les aperçus de reposts](https://github.com/nostria-app/nostria/pull/481) et de la [résolution d'URI nostr: dans les notifications](https://github.com/nostria-app/nostria/pull/458).

### Camelus : migration vers Riverpod v3

[Camelus](https://github.com/camelus-hq/camelus), le client Nostr basé sur Flutter, a fusionné 5 PRs cette semaine centrées sur une [migration vers l'API Riverpod v3](https://github.com/camelus-hq/camelus/pull/158) et une [refonte du flux générique](https://github.com/camelus-hq/camelus/pull/159). Un [cache de notes intégrées](https://github.com/camelus-hq/camelus/pull/161) évite les récupérations redondantes depuis les relays pour les notes citées.

## Mises à jour des NIP

Changements récents dans le [dépôt NIPs](https://github.com/nostr-protocol/nips) :

**Fusionnés :**

- **[NIP-85 : Découverte des fournisseurs de services](https://github.com/nostr-protocol/nips/pull/2223)** : vitorpamplona a ajouté des conseils sur la découverte par les clients des fournisseurs de services [Trusted Assertions NIP-85](/fr/topics/nip-56/), incluant les hints de relay et les clés de service spécifiques aux algorithmes. Voir l'[approfondissement ci-dessous](#approfondissement-nip--nip-85-trusted-assertions) pour une couverture complète.

- **[NIP-11 : Nettoyage des informations relay](https://github.com/nostr-protocol/nips/pull/1946)** : fiatjaf a retiré `privacy_policy`, le tableau `retention`, `relay_countries` et le bloc de préférences communautaires de [NIP-11](/fr/topics/nip-11/). Les opérateurs de relay remplissaient rarement ces champs et les clients n'agissaient pas dessus.

- **[NIP-52 : Tag de timestamp à granularité journalière](https://github.com/nostr-protocol/nips/pull/1752)** : staab a ajouté un tag `D` obligatoire aux événements de calendrier basés sur l'heure [NIP-52](/fr/topics/nip-52/) (kind 31923) représentant le timestamp Unix à granularité journalière, calculé comme `floor(unix_seconds / 86400)`. Plusieurs tags `D` couvrent les événements multi-jours, permettant une indexation temporelle efficace sans analyser les timestamps complets.

- **[NIP-47 : Simplification](https://github.com/nostr-protocol/nips/pull/2210)** : La PR de simplification [discutée dans le Compass #9](/fr/newsletters/2026-02-11-newsletter/) a fusionné cette semaine, retirant `multi_pay_invoice` et `multi_pay_keysend` de [NIP-47 (Nostr Wallet Connect)](/fr/topics/nip-47/). Voir le [Compass #8](/fr/newsletters/2026-02-04-newsletter/#approfondissement-nip--nip-47-nostr-wallet-connect) pour l'approfondissement complet du protocole NWC.

**PRs ouvertes et discussions :**

- **[NIP-74 : Podcasts](https://github.com/nostr-protocol/nips/pull/2211)** : Couvert dans le [Compass #8](/fr/newsletters/2026-02-04-newsletter/), cette proposition de spécification de podcast a suscité une discussion animée cette semaine. staab a noté qu'au moins trois standards de podcast concurrents existent déjà dans la nature, et derekross a pointé vers une implémentation existante vieille de six mois avec des applications et podcasts actifs. La voie à suivre nécessite une convergence entre les implémentations avant qu'un numéro de NIP puisse être attribué.

- **[NIP-XX : AI Agent Messages](https://github.com/nostr-protocol/nips/pull/2226)** : joelklabo propose un protocole complet de communication d'agents IA avec des kinds d'événements pour les prompts, réponses, streaming, télémétrie d'outils, erreurs et découverte de capacités. Voir la [section Actualités](#des-nip-pour-les-agents-ia-arrivent) pour la couverture de toutes les propositions IA de cette semaine.

- **[NIP-PNS : Stockage de notes privées](https://github.com/nostr-protocol/nips/pull/1893)** : Le système de notes privées de jb55 définit des événements kind 1080 pour stocker des notes personnelles chiffrées sur les relays sans révéler qui les a écrites. Le schéma dérive une paire de clés pseudonyme déterministe depuis le nsec de l'utilisateur via HKDF : `pns_key = hkdf_extract(ikm=device_key, salt="nip-pns")`, puis génère une paire de clés secp256k1 à partir de cette clé dérivée. Une deuxième dérivation produit une clé de chiffrement symétrique : `pns_nip44_key = hkdf_extract(ikm=pns_key, salt="nip44-v2")`. Les notes internes sont chiffrées avec [NIP-44](/fr/topics/nip-44/) v2 en utilisant cette clé et publiées sous la pubkey pseudonyme, de sorte que les relays voient des événements kind 1080 d'une identité non liée à la clé principale de l'utilisateur. Contrairement aux gift wraps [NIP-59](/fr/topics/nip-59/), PNS n'est pas spammable (la clé pseudonyme est déterministe, pas aléatoire) et ne porte aucune métadonnée publique (aucun tag `p` nécessaire puisqu'il n'y a pas de destinataire). Cette semaine, jb55 a publié les résultats de l'implémentation de PNS dans le backend Rust de Notedeck (module `enostr::pns`). Il a identifié que l'appel `hkdf_extract` de la spec est ambigu car RFC 5869 HKDF comporte deux phases (Extract et Expand) qui produisent des sorties différentes, et la plupart des bibliothèques s'attendent aux deux. Il a précisé que `pns_nip44_key` contourne l'accord de clés ECDH normal de NIP-44 et est utilisé directement comme clé de conversation — un détail que les implémenteurs doivent connaître car la plupart des bibliothèques NIP-44 utilisent ECDH par défaut. Il a également signalé une variable non définie dans l'implémentation de référence TypeScript. La PR, datant à l'origine d'avril 2025, est maintenant en cours d'implémentation active.

- **[NIP-AE : Agents](https://github.com/nostr-protocol/nips/pull/2220)** : pablof7z définit quatre kinds d'événements pour l'identité des agents sur Nostr, tirés de son travail sur [TENEX](https://github.com/tenex-chat/tenex). Le template de base est kind 4199 (Agent Definition), portant le titre, la description du rôle, les instructions système, les déclarations d'outils et la version. Les modificateurs comportementaux vivent dans kind 4201 (Agent Nudge), qui utilise les tags `only-tool`, `allow-tool` et `deny-tool` pour le contrôle des capacités en exécution. Les agents publient ce qu'ils apprennent comme événements kind 4129 (Agent Lesson), catégorisés et liés à la définition parente via des tags `e`, affinables via des fils de commentaires [NIP-22](/fr/topics/nip-22/). La vérification de propriété utilise kind 14199, un événement remplaçable où les opérateurs humains listent les pubkeys de leurs agents, établissant une chaîne bidirectionnelle lorsque correspondant au tag `p` du profil kind 0 de l'agent.

- **[NIP-AD : MCP Server and Skill Announcements](https://github.com/nostr-protocol/nips/pull/2221)** : pablof7z définit des événements pour annoncer les serveurs [Model Context Protocol](https://modelcontextprotocol.io/) et les compétences individuelles sur Nostr. Les annonces de serveurs MCP portent l'URL du point d'accès du serveur et la version de protocole supportée aux côtés d'une liste d'outils disponibles avec leurs schémas d'entrée. Les commentaires [NIP-22](/fr/topics/nip-22/) sont supportés sur les annonces de serveurs, permettant à la communauté de discuter et d'évaluer les serveurs MCP directement sur Nostr.

- **[NIP-73 : Kind OSM](https://github.com/nostr-protocol/nips/pull/2224)** : DestBro propose d'ajouter les identifiants OpenStreetMap à [NIP-73 (External Content IDs)](/fr/topics/nip-73/), qui standardise comment les événements Nostr référencent le contenu externe comme les livres (ISBN), films (ISAN), flux de podcasts (GUID), géohashes et URLs via les tags `i` et `k`. Le kind OSM proposé permettrait aux événements de référencer des entités cartographiques spécifiques (bâtiments, routes, parcs) par leur ID de nœud ou de voie OpenStreetMap, connectant le contenu Nostr à la base de données géographique ouverte.

- **[NIP-XX : Variantes d'images adaptatives](https://github.com/nostr-protocol/nips/pull/2219)** : woikos propose d'étendre les événements de métadonnées de fichier [NIP-94](/fr/topics/nip-94/) avec des tags pour des variantes d'images adaptatives à différentes résolutions. Les clients pourraient sélectionner la variante appropriée en fonction de la taille d'affichage et des conditions réseau, réduisant la bande passante pour les utilisateurs mobiles consultant des images haute résolution hébergées sur des serveurs [Blossom](/fr/topics/blossom/).

## Approfondissement NIP : NIP-85 (Trusted Assertions)

[NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md) définit un système pour déléguer des calculs coûteux à des fournisseurs de services de confiance qui publient des résultats signés comme événements Nostr. Les scores de Web of Trust et les métriques d'engagement nécessitent le parcours de nombreux relays et le traitement de grands volumes d'événements — un travail impraticable sur les appareils mobiles. La [fusion](https://github.com/nostr-protocol/nips/pull/2223) de cette semaine a ajouté des conseils sur le processus de découverte des fournisseurs par les clients.

**Délégation :**

Le calcul du score de Web of Trust d'un utilisateur nécessite le parcours des graphes d'abonnements sur plusieurs sauts à travers de nombreux relays, et le comptage précis des followers implique la déduplication sur l'ensemble du réseau de relays. Les appareils mobiles et les clients de navigateur ne peuvent pas effectuer ces opérations, pourtant les résultats sont essentiels pour le filtrage du spam et le classement du contenu. NIP-85 comble cet écart en permettant aux utilisateurs de désigner des fournisseurs de confiance pour effectuer les calculs et publier les résultats comme événements Nostr standard.

**Conception du protocole :**

NIP-85 utilise quatre kinds d'événements pour les assertions sur différents types de sujets. Les assertions utilisateur (kind 30382) portent le nombre de followers, les comptages de publications/réponses/réactions, les montants de zaps, le rang normalisé (0-100), les sujets courants et les heures d'activité :

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30382,
  "tags": [
    ["d", "e88a691e98d9987c964521dff60025f60700378a4879180dcbbb4a5027850411"],
    ["rank", "89"],
    ["followers", "4521"],
    ["first_created_at", "1609459200"],
    ["post_cnt", "1283"],
    ["reply_cnt", "647"],
    ["reactions_cnt", "8920"],
    ["zap_amt_recd", "850000"],
    ["zap_amt_sent", "320000"],
    ["zap_cnt_recd", "412"],
    ["zap_cnt_sent", "198"],
    ["zap_avg_amt_day_recd", "1150"],
    ["zap_avg_amt_day_sent", "430"],
    ["reports_cnt_recd", "2"],
    ["reports_cnt_sent", "0"],
    ["t", "nostr"],
    ["t", "bitcoin"],
    ["active_hours_start", "14"],
    ["active_hours_end", "22"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

Les assertions d'événements (kind 30383) évaluent des notes individuelles avec le nombre de commentaires, de citations, de reposts, de réactions et les données de zaps :

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30383,
  "tags": [
    ["d", "<target event id>"],
    ["rank", "72"],
    ["comment_cnt", "45"],
    ["quote_cnt", "12"],
    ["repost_cnt", "89"],
    ["reaction_cnt", "310"],
    ["zap_cnt", "23"],
    ["zap_amount", "125000"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

Pour les événements adressables (articles longs, pages wiki), le kind 30384 applique les mêmes métriques d'engagement sur toutes les versions collectivement. Le kind 30385 évalue les identifiants externes (livres, films, sites web, lieux, hashtags) référencés via [NIP-73 (External Content IDs)](/fr/topics/nip-73/), qui standardise comment les événements Nostr référencent le contenu externe via les tags `i` et `k` :

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30385,
  "tags": [
    ["d", "isbn:9780765382030"],
    ["k", "isbn"],
    ["rank", "94"],
    ["comment_cnt", "67"],
    ["reaction_cnt", "203"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

Chaque assertion est un événement adressable remplaçable où le tag `d` contient le sujet : une pubkey, un ID d'événement, une adresse d'événement ou un identifiant NIP-73. Les fournisseurs de services signent ces événements avec leurs propres clés, et les clients les évaluent en fonction des relations de confiance.

**Découverte des fournisseurs :**

Les utilisateurs déclarent quels fournisseurs d'assertions ils font confiance en publiant des événements kind 10040. Chaque entrée spécifie le type d'assertion avec la pubkey du fournisseur et le hint de relay, plus des variantes d'algorithme optionnelles :

```json
{
  "id": "<event hash>",
  "pubkey": "<user pubkey>",
  "created_at": 1739836800,
  "kind": 10040,
  "tags": [
    ["30382:rank", "4fd5e210...", "wss://nip85.nostr.band"],
    ["30382:rank", "3d842afe...", "wss://nostr.wine"],
    ["30382:zap_amt_sent", "4fd5e210...", "wss://nip85.nostr.band"],
    ["30383:rank", "4fd5e210...", "wss://nip85.nostr.band"]
  ],
  "content": "",
  "sig": "<user signature>"
}
```

Les utilisateurs peuvent chiffrer la liste de tags dans `.content` en utilisant [NIP-44](/fr/topics/nip-44/) pour garder leurs préférences de fournisseur privées. Les clients construisent une liste de fournisseurs en vérifiant quels fournisseurs font confiance à leurs comptes suivis, créant une couche de réputation décentralisée pour les fournisseurs d'assertions eux-mêmes.

**Modèle de sécurité :**

Les fournisseurs doivent utiliser des clés de service différentes pour des algorithmes distincts, et une clé unique par utilisateur lorsque les algorithmes sont personnalisés, empêchant la corrélation croisée des requêtes entre utilisateurs. Chaque clé de service obtient un événement de métadonnées kind 0 décrivant le comportement de l'algorithme, donnant aux utilisateurs une transparence sur ce en quoi ils font confiance. Les événements d'assertion ne doivent être mis à jour que lorsque les données sous-jacentes changent réellement, évitant le trafic inutile sur les relays et permettant aux clients de mettre les résultats en cache avec confiance.

**Adoption actuelle :**

NIP-85 formalise un modèle qui émergeait déjà de façon informelle. Le serveur cache de Primal calcule les métriques d'engagement et les scores de Web of Trust. [Antiprimal](https://gitlab.com/soapbox-pub/antiprimal), couvert dans le [Compass #9](/fr/newsletters/2026-02-11-newsletter/#antiprimal--passerelle-conforme-aux-standards-vers-le-cache-primal), relie ces calculs aux clients Nostr standard en utilisant les kinds d'événements NIP-85. [Nostr.band](https://nostr.band) exploite le relay `wss://nip85.nostr.band` référencé dans les propres exemples de la spec, servant des événements d'assertion pour les données de son index de recherche. Côté client, [Amethyst](https://github.com/vitorpamplona/amethyst) (écrit par vitorpamplona, qui a également rédigé ce NIP) dispose d'un support expérimental des Trusted Assertions dans sa bibliothèque `quartz`, analysant les événements d'assertion et les déclarations de fournisseurs de services. [Vertex](https://vertexlab.io) calcule des métriques similaires de Web of Trust mais [a choisi une approche différente](https://vertexlab.io/blog/dvms_vs_nip_85/), utilisant une API directe plutôt que des événements NIP-85, citant le problème de découverte et la surcharge computationnelle des architectures basées sur les assertions. Avec NIP-85, tout client peut consommer des assertions de n'importe quel fournisseur via un format d'événement standard, et les fournisseurs se font concurrence sur la précision tandis que les utilisateurs choisissent en qui faire confiance.

## Approfondissement NIP : NIP-52 (Événements de calendrier)

[NIP-52](https://github.com/nostr-protocol/nips/blob/master/52.md) définit les événements de calendrier sur Nostr, donnant aux clients un moyen standard de représenter et de découvrir des occurrences à des moments spécifiques ou entre des moments. La [fusion du tag D](https://github.com/nostr-protocol/nips/pull/1752) de cette semaine a ajouté l'indexation à la granularité journalière, complétant une pièce manquante dans l'infrastructure de requête de la spec.

**Deux types d'événements :**

NIP-52 sépare les événements de calendrier en deux kinds selon la précision temporelle. Les événements basés sur la date (kind 31922) représentent les occurrences sur la journée entière comme les jours fériés ou les festivals multi-jours. Ils utilisent des chaînes de date ISO 8601 dans leurs tags `start` et `end` optionnel, sans considération de fuseau horaire :

```json
{
  "id": "<event hash>",
  "pubkey": "<event creator pubkey>",
  "created_at": 1735689600,
  "kind": 31922,
  "content": "Annual celebration of Bitcoin's genesis block",
  "tags": [
    ["d", "bitcoin-independence-day-2026"],
    ["title", "Bitcoin Independence Day"],
    ["start", "2026-01-03"],
    ["end", "2026-01-04"],
    ["location", "Worldwide"],
    ["g", "u4pruydqqv"],
    ["t", "bitcoin"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com", "host"],
    ["r", "https://bitcoinindependenceday.com"]
  ],
  "sig": "<event creator signature>"
}
```

Les événements basés sur l'heure (kind 31923) représentent des moments spécifiques avec des timestamps Unix dans leurs tags `start` et `end` optionnel, plus des identifiants de fuseau horaire IANA (`start_tzid`, `end_tzid`) pour l'affichage. Les deux kinds sont des événements remplaçables paramétrés, de sorte que les organisateurs mettent à jour les détails en publiant un nouvel événement avec le même tag `d`.

**Calendriers et RSVP :**

Les événements kind 31924 définissent les calendriers comme des collections, référençant les événements via des tags `a` pointant vers les événements kind 31922 ou 31923 par leurs coordonnées d'adresse :

```json
{
  "id": "<event hash>",
  "pubkey": "<calendar owner pubkey>",
  "created_at": 1739836800,
  "kind": 31924,
  "content": "Nostr community events worldwide",
  "tags": [
    ["d", "nostr-community-calendar"],
    ["title", "Nostr Community Events"],
    ["a", "31923:<organizer-pubkey>:nostr-meetup-2026", "wss://relay.example.com"],
    ["a", "31922:<organizer-pubkey>:bitcoin-independence-day-2026"]
  ],
  "sig": "<calendar owner signature>"
}
```

Les utilisateurs peuvent maintenir plusieurs calendriers (personnel, professionnel, communautaire) et les clients peuvent s'abonner aux calendriers de pubkeys spécifiques. Les événements de calendrier peuvent inclure un tag `a` référençant un calendrier pour demander leur inclusion, permettant une gestion collaborative des calendriers où plusieurs utilisateurs contribuent des événements aux calendriers qu'ils ne possèdent pas.

Les RSVP utilisent le kind 31925, où les utilisateurs publient leur statut de présence avec un indicateur libre/occupé optionnel :

```json
{
  "id": "<event hash>",
  "pubkey": "<attendee pubkey>",
  "created_at": 1739836800,
  "kind": 31925,
  "content": "Looking forward to it",
  "tags": [
    ["a", "31923:<organizer-pubkey>:nostr-meetup-2026", "wss://relay.example.com"],
    ["e", "<kind 31923 event id>", "wss://relay.example.com"],
    ["d", "<unique-rsvp-id>"],
    ["status", "accepted"],
    ["fb", "busy"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com"]
  ],
  "sig": "<attendee signature>"
}
```

Les valeurs de `status` valides sont « accepted », « declined », « tentative », et le tag `fb` optionnel marque l'utilisateur comme libre ou occupé pour cette période. Les événements RSVP référencent le tag `a` de l'événement de calendrier et portent le tag `p` de l'organisateur, de sorte que le client de l'organisateur peut agréger les réponses à travers les relays.

**L'ajout du tag D :**

Avant la fusion de cette semaine, les clients interrogeant des événements dans une plage de dates devaient récupérer tous les événements d'une pubkey ou d'un calendrier et filtrer côté client. Le nouveau tag `D` obligatoire sur les événements basés sur l'heure (kind 31923) contient un timestamp Unix à granularité journalière calculé comme `floor(unix_seconds / 86400)`. Les événements multi-jours portent plusieurs tags `D`, un par jour. Les relays peuvent maintenant indexer les événements par jour et répondre à des requêtes filtrées efficacement, transformant ce qui était un problème de filtrage côté client en une recherche d'index côté relay.

```json
{
  "id": "<event hash>",
  "pubkey": "<event creator pubkey>",
  "created_at": 1739836800,
  "kind": 31923,
  "content": "Monthly meetup for Nostr developers in Austin",
  "tags": [
    ["d", "nostr-meetup-2026"],
    ["title", "Nostr Developer Meetup"],
    ["summary", "Talks and demos from local Nostr builders"],
    ["image", "https://example.com/meetup-banner.jpg"],
    ["start", "1740067200"],
    ["end", "1740078000"],
    ["start_tzid", "America/New_York"],
    ["end_tzid", "America/New_York"],
    ["D", "20139"],
    ["location", "Bitcoin Commons, Austin TX"],
    ["g", "9v6knb2pg"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com", "host"],
    ["p", "<speaker-pubkey>", "wss://relay.example.com", "speaker"],
    ["t", "nostr"],
    ["t", "meetup"],
    ["r", "https://bitcoincommons.com"]
  ],
  "sig": "<event creator signature>"
}
```

La valeur `D` de `20139` est égale à `floor(1740067200 / 86400)`, plaçant cet événement le 20 février 2025. Les clients interrogeant pour « tous les événements de cette semaine » envoient un filtre avec la plage `D` correspondante, et les relays ne retournent que les événements correspondants.

**Décisions de conception :**

NIP-52 omet intentionnellement les événements récurrents. La spec laisse de côté les règles de récurrence (RRULE d'iCalendar), déléguant cette complexité aux clients. Un organisateur publie des événements individuels pour chaque occurrence, gardant le modèle de données côté relay simple. Les tags de participants portent des rôles optionnels (« host », « speaker », « attendee »), et les tags de localisation peuvent inclure des tags géohash `g` pour les requêtes spatiales aux côtés des adresses lisibles par l'humain.

**Implémentations :**

[Flockstr](https://github.com/zmeyer44/flockstr) est le principal client de calendrier construit sur NIP-52. [Coracle](https://gitea.coracle.social/coracle/coracle) affiche les événements de calendrier dans son flux social. L'ajout du tag `D` cette semaine permet l'indexation temporelle côté relay que les deux clients peuvent utiliser pour réduire la bande passante lors des requêtes d'événements dans une plage de dates spécifique.

---

C'est tout pour cette semaine. Vous construisez quelque chose ou avez des actualités à partager ? Vous souhaitez que nous couvrions votre projet ? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contactez-nous via [NIP-17](/fr/topics/nip-17/) DM</a> ou retrouvez-nous sur Nostr.
