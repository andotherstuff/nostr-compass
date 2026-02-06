---
title: 'Nostr Compass #7'
date: 2026-01-28
translationOf: /en/newsletters/2026-01-28-newsletter.md
translationDate: 2026-01-28
draft: false
type: newsletters
---

Bienvenue dans Nostr Compass, votre guide hebdomadaire sur Nostr.

**Cette semaine :** Ridestr apporte le covoiturage décentralisé sur Nostr avec des paiements [Cashu](/fr/topics/cashu/) et le partage de localisation chiffré. Pomade introduit la récupération par email pour les signataires multisig. Damus intègre [negentropy](/fr/topics/negentropy/) pour une synchronisation fiable des messages privés. L'application de bureau d'Amethyst ajoute la recherche, les favoris et les zaps. Amber v4.1.1 affiche les scores de confiance des relais. Marmot fusionne MIP-03 et construit une application de chat de référence en TypeScript. diVine ajoute l'authentification QR [NIP-46](/fr/topics/nip-46/) et le support des mentions. De nouvelles propositions de NIP abordent la gestion des communautés, la synchronisation basée sur les séquences et le stockage de fichiers chiffrés. Nous revenons également sur cinq années de janvier Nostr, retraçant l'évolution du protocole depuis une poignée d'adopteurs précoces en 2021 jusqu'au lancement explosif de Damus sur l'App Store en 2023, en passant par l'écosystème de clients mature de 2025.

## Actualités

### Ridestr apporte le covoiturage décentralisé sur Nostr

[Ridestr](https://github.com/variablefate/ridestr) développe une application de covoiturage pair-à-pair entièrement construite sur Nostr, permettant des transactions directes entre conducteurs et passagers avec des paiements Bitcoin et [Cashu](/fr/topics/cashu/). Le protocole utilise des types d'événements personnalisés (30173, 3173-3175, 30180/30181) pour coordonner les trajets tout en préservant la confidentialité grâce à la divulgation progressive de la localisation et au chiffrement [NIP-44](/fr/topics/nip-44/).

Le système fonctionne selon un flux soigneusement orchestré : les conducteurs diffusent leur disponibilité en utilisant des localisations encodées en geohash (précision d'environ 5 km) via des événements kind 30173, les passagers demandent des trajets avec des estimations de tarifs via kind 3173, et les paiements sont sécurisés par des tokens séquestrés HTLC avant le début du trajet. La confidentialité de la localisation est préservée grâce à la divulgation progressive, où les détails du point de prise en charge ne sont révélés qu'à l'arrivée des conducteurs et les destinations sont partagées après vérification du code PIN. Toutes les communications entre les parties utilisent le chiffrement [NIP-44](/fr/topics/nip-44/) pour la confidentialité.

Ridestr implémente la sécurité des paiements via un séquestre HTLC avec signatures P2PK. Lorsqu'un passager accepte l'offre d'un conducteur, il verrouille des tokens [Cashu](/fr/topics/cashu/) avec un hash de paiement que seul le conducteur peut réclamer après la fin du trajet. Le protocole fonctionne actuellement avec une architecture à mint unique, exigeant que les passagers et les conducteurs utilisent le même mint [Cashu](/fr/topics/cashu/). L'implémentation Android basée sur Kotlin gère la vérification des preuves et la récupération des preuves périmées via les vérifications d'état NUT-07.

Ridestr s'attaque à des défis que la plupart des applications Nostr évitent : la coordination de localisation en temps réel, le séquestre de paiement avec résolution des litiges et les systèmes de réputation pour les interactions dans le monde physique. Le projet est en bêta et démontre que le modèle d'événements de Nostr peut supporter des places de marché de services pair-à-pair, pas seulement le partage de contenu.

### Pomade lance un système de récupération Alpha pour les signataires Multisig

[Pomade](https://github.com/coracle-social/pomade), développé par hodlbod, s'appuie sur l'écosystème [FROSTR](https://github.com/FROSTR-ORG) existant pour fournir un service de signature à seuil axé sur la récupération. En utilisant les signatures [FROST](/fr/topics/frost/) (Flexible Round-Optimized Schnorr Threshold) via la bibliothèque @frostr/bifrost, Pomade ajoute des flux de récupération par email en plus de la cryptographie à seuil. Le système fragmente la clé secrète d'un utilisateur en utilisant le partage de secret de Shamir, distribuant les fragments entre plusieurs signataires indépendants avec un seuil configurable (2-sur-3, 3-sur-5, etc.).

Le protocole fonctionne entièrement sur Nostr en utilisant un seul type d'événement (28350) avec des charges utiles chiffrées [NIP-44](/fr/topics/nip-44/). Lors de la signature, le client demande des signatures partielles à au moins `threshold` signataires, puis les agrège en une signature Schnorr valide. Pour le chiffrement, les signataires collaborent pour dériver des secrets partagés via ECDH sans qu'aucune partie n'apprenne la clé complète.

La récupération fonctionne via deux méthodes d'authentification : basée sur mot de passe (utilisant argon2id avec la pubkey du signataire comme sel) ou par OTP email. Pour prévenir les attaques MITM pendant la récupération OTP, chaque signataire génère son propre code de vérification avec un préfixe fourni par le client, exigeant que les utilisateurs s'authentifient indépendamment auprès de chaque signataire. Le protocole exige une preuve de travail sur les événements d'inscription (20+ bits selon [NIP-13](/fr/topics/nip-13/)) pour prévenir le spam.

Le modèle de confiance est explicite : si `threshold` signataires s'entendent, ils peuvent voler la clé. Les fournisseurs d'email bénéficient d'une confiance totale puisqu'ils peuvent intercepter les OTP. Les utilisateurs ne peuvent pas récupérer indépendamment leur clé secrète complète ; cela nécessite la coopération de `threshold` signataires. Le protocole est conçu pour l'intégration de nouveaux utilisateurs non familiers avec la gestion des clés, avec la recommandation explicite que les utilisateurs migrent vers l'auto-conservation une fois à l'aise. Pomade avertit des potentiels « pertes de clés, vols, dénis de service ou fuites de métadonnées » étant donné son statut alpha non audité.

## Versions

### Damus intègre Negentropy pour une synchronisation fiable des messages privés

[Damus v1.13](https://github.com/damus-io/damus/tree/v1.13) intègre l'implémentation negentropy [que nous avions présentée comme PR ouverte la semaine dernière](/fr/newsletters/2026-01-21-newsletter/#damus-ios-client---open-prs). [PR #3536](https://github.com/damus-io/damus/pull/3536) ajoute le support de base de [negentropy](/fr/topics/negentropy/) à la couche réseau, permettant la réconciliation d'ensembles avec les relais qui supportent le protocole. Une [PR #3547](https://github.com/damus-io/damus/pull/3547) complémentaire ajoute la synchronisation des messages privés par glissement vers le bas qui utilise negentropy pour récupérer les messages manquants lorsque les abonnements REQ standard échouent.

L'implémentation suit une approche conservatrice : le chargement normal des messages privés continue inchangé, avec [negentropy](/fr/topics/negentropy/) disponible comme mécanisme de récupération lorsque les utilisateurs actualisent manuellement. Les tests automatisés démontrent la correction en générant un message privé avec un ancien horodatage que les requêtes standard manqueraient, puis en utilisant la synchronisation [negentropy](/fr/topics/negentropy/) pour le récupérer avec succès. Bien que le support de [negentropy](/fr/topics/negentropy/) nécessite des relais compatibles, l'implémentation gère gracieusement les environnements de relais mixtes en utilisant le protocole là où il est disponible.

### Amber v4.1.1 - Scores de confiance des relais

[Amber v4.1.1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.1) intègre l'affichage des scores de confiance des relais ([PR #289](https://github.com/greenart7c3/Amber/pull/289)), implémentant les concepts d'évaluation des relais discutés dans [la couverture des attestations de confiance des relais de la semaine dernière](/fr/newsletters/2026-01-21-newsletter/#nip-updates). Les scores de confiance apparaissent désormais sur la page Relais et pour les demandes de connexion NostrConnect, aidant les utilisateurs à évaluer la fiabilité des relais avant d'autoriser les connexions. La version inclut également une interface utilisateur login/événements/permissions redessinée et le support de la méthode `switch_relays`. Les améliorations de performance mettent en cache les opérations du keystore, répondant aux rapports de temps de chargement de plus de 20 secondes sur les appareils plus anciens.

### nak v0.18.2 - Intégration MCP

[nak](https://github.com/fiatjaf/nak) (Nostr Army Knife) de fiatjaf [v0.18.2](https://github.com/fiatjaf/nak/releases/tag/v0.18.2) ajoute le support du [Model Context Protocol](https://nostrify.dev/mcp) via `nak mcp`, permettant aux agents IA de rechercher des personnes sur Nostr, publier des notes, mentionner des utilisateurs et lire du contenu en utilisant le modèle outbox. La version introduit également un [installateur en une ligne](https://github.com/fiatjaf/nak/blob/master/install.sh) (`curl -sSL https://raw.githubusercontent.com/fiatjaf/nak/master/install.sh | sh`) qui télécharge des binaires pré-compilés, éliminant le besoin de la chaîne d'outils Go pour les utilisateurs finaux. Le mode Bunker supporte maintenant les sockets Unix et `switch_relays`.

### Zeus v0.12.2 Beta - Corrections NWC

[Zeus v0.12.2-beta1](https://github.com/ZeusLN/zeus/releases) intègre plusieurs corrections NWC répondant aux problèmes couverts dans [la couverture de Zeus de la semaine dernière](/fr/newsletters/2026-01-21-newsletter/#zeus-lightning-wallet-with-nostr-wallet-connect).

## Mises à jour des projets

### Amethyst Desktop - Phase 2A livrée

[Amethyst](https://github.com/vitorpamplona/amethyst) a déployé la [Phase 2A de son application de bureau](https://github.com/vitorpamplona/amethyst/pull/1676), ajoutant la Recherche, les Favoris, les Zaps, les vues de Threads et le contenu long format (Lectures) à l'expérience de bureau. Une [PR #1683](https://github.com/vitorpamplona/amethyst/pull/1683) complémentaire ajoute un retour transparent sur la diffusion des événements afin que les utilisateurs voient maintenant le statut en temps réel par relais lorsque leurs événements se propagent à travers le réseau, facilitant le diagnostic des problèmes de connectivité.

### Progression de Notedeck : Application Calendrier et perfectionnement UX

Le client de bureau [Notedeck](https://github.com/damus-io/notedeck) de l'équipe Damus a fusionné le comportement de masquage automatique de la barre d'outils ([PR #1268](https://github.com/damus-io/notedeck/pull/1268)) qui répond à la vélocité de défilement pour plus d'espace d'écran sur les vues mobiles. Une [PR brouillon #1271](https://github.com/damus-io/notedeck/pull/1271) ajoute une application Calendrier [NIP-52](/fr/topics/nip-52/) complète avec des vues mois/semaine/jour/agenda, le support RSVP et les commentaires [NIP-22](/fr/topics/nip-22/) sur les événements de calendrier, actuellement sous feature flag pour les tests.

### Jumble ajoute le mode Communauté

[Jumble](https://github.com/CodyTseng/jumble), le client web axé sur les relais, a ajouté le [mode communauté](https://github.com/CodyTseng/jumble/pull/738) et le support des [préréglages d'ensembles de relais via variables d'environnement](https://github.com/CodyTseng/jumble/pull/736), facilitant le déploiement d'instances thématiques comme [nostr.moe](https://nostr.moe/).

### Tableau de bord des commandes Shopstr

[Shopstr](https://github.com/shopstr-eng/shopstr) a remplacé sa gestion des commandes par chat par un [Tableau de bord des commandes](https://github.com/shopstr-eng/shopstr/pull/219) dédié. La nouvelle interface fournit une vue centralisée pour que les marchands suivent le statut des commandes, marquent les messages comme lus et gèrent l'exécution sans faire défiler les fils de discussion. La mise à jour déprécie la mise en cache IndexedDB en faveur des API de statut de commande côté serveur et révise la façon dont les messages privés de commande sont tagués pour un meilleur filtrage.

### Formstr ajoute les questions en grille

[Formstr](https://github.com/abh3po/nostr-forms), l'application de formulaires native Nostr, a ajouté les [questions en grille](https://github.com/abh3po/nostr-forms/pull/419) et [réécrit son SDK](https://github.com/abh3po/nostr-forms/pull/410) avec le support de l'intégration. Une [correction pour les signataires non-NIP-07](https://github.com/abh3po/nostr-forms/pull/418) a résolu les problèmes pour les utilisateurs avec des signataires bunker ou locaux essayant de soumettre des formulaires avec leur identité.

### nostr-tools met à jour les dépendances cryptographiques

[nostr-tools](https://github.com/nbd-wtf/nostr-tools), la bibliothèque JavaScript principale, [a mis à jour vers @noble/curves v2.0.1](https://github.com/nbd-wtf/nostr-tools/pull/520), répondant aux changements d'API cassants dans 27 fichiers et adoptant les dernières bibliothèques noble auditées. fiatjaf a également ajouté le support de `switch_relays` à [NIP-46](/fr/topics/nip-46/), permettant aux clients bunker de changer dynamiquement les connexions de relais.

### Zeus travaille sur les avis de mint NIP-87

[Zeus](https://github.com/ZeusLN/zeus) a une [PR ouverte pour les avis de mint NIP-87](https://github.com/ZeusLN/zeus/pull/3576), permettant aux utilisateurs de découvrir et d'évaluer les mints [Cashu](/fr/topics/cashu/) filtrés par les follows Nostr. Les avis incluent des notes étoilées et peuvent être soumis de manière anonyme ou avec le nsec de l'utilisateur.

### Camelus intègre le support complet des messages privés

[Camelus](https://github.com/camelus-hq/camelus), un client Android basé sur Flutter construit avec Dart NDK pour des performances mobiles économes en batterie, a ajouté la messagerie directe complète avec plus de 20 commits cette semaine. La mise à jour inclut les catégories de chat, les dates des messages, l'interface d'envoi optimiste, la fonctionnalité note-à-soi-même et la gestion appropriée des relais de messages privés.

### Mises à jour du protocole Marmot

La résolution déterministe des commits MIP-03 [que nous avions couverte comme PR ouverte la semaine dernière](/fr/newsletters/2026-01-21-newsletter/#marmot-protocol-white-noise-encrypted-group-chat-library) a maintenant été fusionnée. [MDK PR #152](https://github.com/marmot-protocol/mdk/pull/152) garantit que tous les chats de groupe basés sur [MLS](/fr/topics/mls/) convergent vers le même état lorsque plusieurs commits valides arrivent pour la même époque.

Une [PR spec #28](https://github.com/marmot-protocol/marmot/pull/28) complémentaire ajoute les exigences de cycle de vie des init_key répondant aux lacunes des audits d'implémentation : le matériel de clé privée des messages Welcome doit être supprimé de manière sécurisée après traitement (zéroisation, nettoyage du stockage), et les nouveaux membres doivent effectuer des auto-mises à jour dans les 24 heures pour la confidentialité persistante.

Le SDK TypeScript ([marmot-ts](https://github.com/marmot-protocol/marmot-ts)) construit une application de chat de référence. [PR #37](https://github.com/marmot-protocol/marmot-ts/pull/37) ajoute la création/liste de groupes, la gestion des paquets de clés avec les flux publier/diffuser/supprimer et les invitations par code QR. Une [PR ouverte #38](https://github.com/marmot-protocol/marmot-ts/pull/38) par hzrd149 implémente la persistance de l'historique des messages avec pagination. Le backend whitenoise-rs a fusionné 15 PRs cette semaine incluant le support multilingue ([PR #455](https://github.com/marmot-protocol/whitenoise-rs/pull/455)) et les références médias MIP-04 v2 ([PR #450](https://github.com/marmot-protocol/whitenoise-rs/pull/450)).

### diVine ajoute des fonctionnalités d'intégration Nostr

[diVine](https://github.com/divinevideo/divine-mobile), l'application de vidéos courtes, poursuit son intégration rapide de Nostr.

Les PRs ouvertes incluent l'authentification par code QR [NIP-46](/fr/topics/nip-46/) ([PR #1019](https://github.com/divinevideo/divine-mobile/pull/1019)) et la messagerie directe chiffrée [NIP-17](/fr/topics/nip-17/) ([PR #834](https://github.com/divinevideo/divine-mobile/pull/834)). L'activité de cette semaine s'est concentrée sur le [support des mentions](https://github.com/divinevideo/divine-mobile/pull/1098) convertissant les URI `nostr:` et les @mentions en liens de profil cliquables, les [fallbacks d'avatars Classic Viners](https://github.com/divinevideo/divine-mobile/pull/1097) utilisant les profils Nostr, et les outils d'édition vidéo incluant le [dessin](https://github.com/divinevideo/divine-mobile/pull/1056), les [filtres](https://github.com/divinevideo/divine-mobile/pull/1053) et les [stickers](https://github.com/divinevideo/divine-mobile/pull/1050).

## Mises à jour des NIP

Changements récents dans le [dépôt NIPs](https://github.com/nostr-protocol/nips) :

**Fusionnés :**

- **[Attestations de confiance des relais](https://github.com/nostr-protocol/nips/pull/1534)** - La proposition pour standardiser le scoring de confiance des relais [que nous avons couverte la semaine dernière](/fr/newsletters/2026-01-21-newsletter/#nip-updates) a été fusionnée. La spécification définit des événements kind 30385 pour les attestations de confiance des relais avec un scoring sur la fiabilité, la qualité et l'accessibilité. Le débat menant à la fusion portait sur le fait de savoir si les scores de confiance devraient être « globaux » (calculés une fois pour tous les utilisateurs) ou « personnalisés » (relatifs au graphe social de chaque observateur). Les algorithmes de type PageRank comme le [Trust Rank de nostr.band](https://trust.nostr.band/) et [GrapeRank](https://github.com/Pretty-Good-Freedom-Tech/graperank-nodejs) résistent aux attaques sybil en divisant tout rang passé à travers des comptes factices par la taille de la ferme de bots.

**PRs ouvertes et discussions :**

- **Communikeys** - Une [proposition complète](https://nostrhub.io) pour la gestion des communautés qui utilise les npubs existants comme identifiants de communauté au lieu d'approches basées sur les relais. N'importe quelle npub peut devenir une communauté en publiant un événement kind 10222 ; les publications ciblent les communautés via des événements kind 30222. Le contrôle d'accès utilise les badges [NIP-58](/fr/topics/nip-58/), permettant la gestion déléguée des membres avec stockage à froid pour les clés de communauté.

- **[NIP-CF : Flux de changements](https://github.com/nostr-protocol/nips/pull/2196)** - Un brouillon proposant la synchronisation d'événements basée sur les séquences comme alternative aux filtres `since` basés sur les horodatages. Le problème : la synchronisation Nostr standard utilisant les horodatages `since` peut manquer des événements lorsque plusieurs événements partagent le même horodatage à la seconde près, les horloges du client et du relais dérivent l'une par rapport à l'autre, ou le checkpointing est imprécis. NIP-CF résout cela en faisant assigner par les relais des numéros de séquence croissants de manière monotone aux événements stockés, fournissant un ordre total strict. Les clients demandent les changements depuis un numéro de séquence spécifique et reçoivent les événements dans un ordre garanti, avec un checkpointing précis qui ne manque jamais d'événements. La proposition supporte également le mode live/continu où les abonnements restent ouverts après la synchronisation initiale pour les mises à jour en temps réel.

- **[NIP-XX : Synchronisation de fichiers chiffrés](https://github.com/nostr-protocol/nips/pull/1947)** - Un protocole définissant les kinds 30800 (fichiers chiffrés), 30801 (index de coffre) et 30802 (documents partagés) pour synchroniser du contenu chiffré entre appareils en utilisant les relais Nostr. Le protocole permet aux applications de prise de notes local-first de fournir une synchronisation chiffrée de bout en bout sans serveurs centralisés. Les contenus des fichiers, les chemins, les noms et la structure des dossiers sont tous chiffrés en utilisant l'auto-chiffrement [NIP-44](/fr/topics/nip-44/), de sorte que les relais stockent des blobs qu'ils ne peuvent pas lire. Les pièces jointes binaires comme les images utilisent des serveurs [Blossom](/fr/topics/blossom/) avec chiffrement côté client. Le kind 30802 permet le partage de documents entre utilisateurs en chiffrant vers la clé publique du destinataire.

## Cinq années de janvier Nostr

[La newsletter du mois dernier](/fr/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers) a retracé les jalons de décembre de Nostr depuis la première version client de fiatjaf jusqu'au don catalyseur de Jack Dorsey. Cette rétrospective trace ce qui s'est passé chaque janvier de 2021 à 2025, en se concentrant sur les développements techniques vérifiés.

### Janvier 2021 : Développement précoce

Le troisième mois de Nostr a vu la poursuite du développement de Branle, le client Vue.js de fiatjaf lancé en décembre 2020. Un petit groupe d'adopteurs précoces, probablement moins de 15 personnes, se coordonnait via le groupe Telegram [@nostr_protocol](https://t.me/nostr_protocol) (créé le 16 novembre 2020), testant le protocole sur un ou deux relais expérimentaux. Le client en ligne de commande noscl fournissait une interaction basée sur le terminal.

Les fondations techniques étaient déjà verrouillées : les utilisateurs identifiés par des clés publiques secp256k1, les posts signés cryptographiquement avec des signatures Schnorr, et les relais servant de stockage passif qui ne communiquent pas entre eux. C'était délibérément de la cryptographie native Bitcoin, un choix de conception qui façonnerait les modèles d'adoption des années plus tard.

### Janvier 2022 : Découverte par les développeurs

Janvier 2022 s'est ouvert avec Nostr encore en effervescence après sa [première apparition sur Hacker News](https://news.ycombinator.com/item?id=29749061) (31 décembre 2021), qui a généré 110 points et 138 commentaires. Au moment de ce post, seulement environ sept relais alimentaient l'ensemble du réseau, les commentateurs notant que « le spam n'est pas encore un problème parce que nostr est super nouveau et personne ne l'utilise encore ». Robert C. Martin (« Uncle Bob ») avait soutenu Nostr comme potentiellement « la solution finale pour la communication sociale ». La discussion s'est poursuivie en janvier, avec des développeurs débattant de l'architecture des relais versus le vrai P2P, la résistance à la censure versus la modération, et si la simplicité pouvait passer à l'échelle.

Le post HN a déclenché une vague de nouvelles implémentations. Uncle Bob lui-même a commencé [more-speech](https://github.com/unclebob/more-speech), un client desktop Clojure, le 18 janvier. La bibliothèque [go-nostr](https://github.com/nbd-wtf/go-nostr) de fiatjaf (créée en janvier 2021) et le client en ligne de commande [noscl](https://github.com/fiatjaf/noscl) fournissaient des outils Go, tandis que [nostr-tools](https://github.com/nbd-wtf/nostr-tools) offrait le support JavaScript. En décembre 2022, environ 800 profils avaient des bios. Branle restait le principal client web, recevant des mises à jour incluant l'import de clés privées et le support multi-relais. Les défis techniques étaient évidents : les clés hex de 64 caractères s'avéraient peu intuitives, les délais de messages frustraient les utilisateurs, et la communauté se demandait si l'architecture pouvait gérer le trafic à l'échelle de Twitter.

### Janvier 2023 : L'explosion

Janvier 2023 a transformé Nostr d'expérience en mouvement. Damus, le client iOS de William Casarin (jb55), a bataillé avec le processus d'approbation de l'App Store d'Apple. Rejeté le 1er janvier, rejeté à nouveau le 26 janvier, il a finalement été [approuvé le 31 janvier](https://www.coindesk.com/tech/2023/02/01/decentralized-social-media-project-nostrs-damus-gets-listed-on-apple-app-store). Cette approbation a déclenché une cascade : Damus a immédiatement atteint la 10e place des Réseaux Sociaux aux États-Unis. Jack Dorsey l'a [qualifié](https://web.archive.org/web/20240304043638/https://www.theblock.co/post/207448/nostr-based-decentralized-twitter-alternative-damus-goes-live-on-apple-app-store) de « jalon pour les protocoles ouverts ».

Huit jours plus tôt, le 23 janvier, [Edward Snowden a annoncé](https://x.com/Snowden/status/1617623779626352640) sa présence sur Nostr : « Une des choses cool à propos de Nostr... au-delà de la résistance à la censure, c'est que vous n'êtes pas limité à 280 caractères ». Son soutien en tant que lanceur d'alerte de la NSA avait du poids dans les cercles soucieux de la vie privée, et les utilisateurs ont immédiatement commencé à lui envoyer des sats via Lightning.

Les clients web ont fait la course pour intégrer l'afflux. [Snort](https://github.com/v0l/snort), créé par kieran en décembre 2022, a émergé comme un client React riche en fonctionnalités ; le 13 janvier, Snort a intégré l'enregistrement NIP-05 via l'API Nostr Plebs, permettant aux nouveaux utilisateurs de revendiquer des identités lisibles par l'homme lors de l'intégration. [Iris](https://iris.to), développé à temps plein par Martti Malmi (un contributeur précoce de Bitcoin qui a reçu la deuxième transaction Bitcoin jamais effectuée de Satoshi), offrait des interfaces web et mobiles avec des identités NIP-05 gratuites sur iris.to. [Astral](https://github.com/monlovesmango/astral), construit par monlovesmango avec Quasar (Vue.js) comme fork de Branle, se concentrait sur la gestion des relais avec sa fonctionnalité de groupement de relais qui permettait aux utilisateurs d'organiser les relais en ensembles pour la publication et le filtrage. Les bêtas TestFlight pour les clients iOS se remplissaient en quelques heures, et Amethyst dominait Android.

L'infrastructure s'est démêlée pour suivre le rythme. Tous les relais étaient exploités par des enthousiastes payant de leur poche. Les relais payants utilisant des micropaiements Lightning créaient un filtrage naturel du spam mais introduisaient une friction d'accès. [Damus a été retiré de l'App Store chinois](https://techcrunch.com/2023/02/02/damus-pulled-from-apples-app-store-in-china-after-two-days/) seulement deux jours après son approbation, apparemment sur demande du principal régulateur internet chinois.

### Janvier 2024 : Durcissement du protocole

Janvier 2024 s'est concentré sur la standardisation du protocole et la construction de la communauté. [Nostr PHX](https://www.nostrphx.com/events) a lancé l'année avec un meetup le 5 janvier à Phoenix, rassemblant les cypherpunks locaux. C'était le premier de nombreux événements communautaires cette année-là incluant BTC Prague (juin), Nostriga à Riga (août) et Nostrasia.

Le développement de protocole le plus significatif a été la fusion de [NIP-59 (Gift Wrap)](https://github.com/nostr-protocol/nips/pull/716) le 29 janvier, fournissant la protection des métadonnées pour les communications chiffrées. Gift Wrap s'appuie sur [le standard de chiffrement NIP-44](https://github.com/paulmillr/nip44) (qui avait été [audité par Cure53](https://cure53.de/audit-report_nip44-implementations.pdf) en décembre 2023) pour cacher l'identité de l'expéditeur aux relais. Le protocole enveloppe les messages chiffrés dans un événement externe signé par une paire de clés aléatoire à usage unique. Les relais ne voient que la pubkey jetable, tandis que la véritable identité de l'expéditeur est enfouie dans la charge utile chiffrée que seul le destinataire peut déchiffrer. Cela empêche les opérateurs de relais et les observateurs du réseau d'apprendre qui envoie des messages à qui. Les horodatages peuvent également être randomisés pour déjouer l'analyse temporelle.

L'écosystème s'est étendu au-delà des réseaux sociaux. [Plebeian Market](https://plebeian.market) est devenu entièrement natif Nostr avec la conformité [NIP-15](/fr/topics/nip-15/), permettant les paniers d'achat multi-étals et un navigateur d'étals pour découvrir les marchands. [Shopstr](https://github.com/shopstr-eng/shopstr) a émergé comme une place de marché sans permission facilitant le commerce Bitcoin. [Zap.stream](https://zap.stream/), construit par kieran, a apporté le streaming en direct sur Nostr avec des paiements Lightning à 21 sats/minute. Les outils de développement ont mûri avec [NDK](https://github.com/nostr-dev-kit/ndk) fournissant des abstractions TypeScript et [rust-nostr](https://github.com/rust-nostr/nostr) offrant des bindings Rust. [Zeus v0.8.1](https://blog.zeusln.com/new-release-zeus-v0-8-1/) a intégré l'import de contacts Nostr et LND persistant, posant les bases de l'intégration Nostr Wallet Connect dans les versions ultérieures.

Pourtant, la durabilité de l'infrastructure [restait difficile](https://arxiv.org/abs/2402.05709). La recherche académique de cette période a trouvé que 95% des relais peinaient à couvrir les coûts opérationnels, avec 20% connaissant des temps d'arrêt significatifs. Les frais d'admission pour les relais payants étaient en moyenne inférieurs à 1 000 sats (~0,45 $), insuffisants pour maintenir les opérations.

*Une note sur les arnaques : Le « Nostr Assets Protocol » et le token « $NOSTR » associé lancés autour de cette période [ont été publiquement dénoncés par fiatjaf](https://www.aicoin.com/en/article/377704) comme « 100% frauduleux » et « une arnaque par affinité » sans aucune connexion avec le protocole Nostr réel.*

### Janvier 2025 : Maturation des clients

Janvier 2025 a vu la poursuite du développement des clients à travers l'écosystème. [Nostur 1.17.0](https://www.nobsbitcoin.com/nostur-v1-17-0/) a été livré le 13 janvier avec la synchronisation multi-appareils des états de lecture, le support de connexion multi-sig [FROST](/fr/topics/frost/) et des performances de base de données locale optimisées. Amethyst a poursuivi sa transition vers le modèle outbox, compilant automatiquement les ensembles de relais basés sur les listes de follows plutôt que de nécessiter une configuration manuelle.

Les principaux clients ont commencé à s'éloigner de [NIP-04](/fr/topics/nip-04/) pour les messages directs, migrant vers [NIP-17](/fr/topics/nip-17/) et le proposé [NIP-104](/fr/topics/nip-104/) pour un chiffrement amélioré et une protection des métadonnées. Le modèle Gossip (communication outbox/inbox) a gagné en adoption alors que l'écosystème convergeait vers des modèles d'utilisation des relais plus efficaces. Les observateurs de l'industrie ont prédit que ce serait l'année où Nostr passerait de protocole de niche à reconnaissance grand public, avec une migration potentielle de plateforme très médiatisée qui pourrait doubler l'activité quotidienne.

### Janvier 2026 : Infrastructure de sécurité et de signature

Janvier 2026 a apporté des avancées significatives dans l'infrastructure de sécurité et de signature. [Primal Android 2.6.18](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18) a intégré la signature à distance [NIP-46](/fr/topics/nip-46/) et le support de signataire local [NIP-55](/fr/topics/nip-55/), rejoignant Amber et Aegis comme hub de signature complet pour d'autres applications Android. [Bitchat a complété un audit de sécurité Cure53](https://github.com/permissionlesstech/bitchat/pulls), la même firme qui a audité Signal et NIP-44, avec plus de 17 PRs corrigeant des découvertes critiques incluant l'effacement des secrets DH et des problèmes de sécurité des threads. Bitchat et Damus ont tous deux migré de C Tor vers Rust Arti pour une fiabilité améliorée et la sécurité mémoire.

Le travail sur le protocole a continué avec la fusion de [NIP-71](https://github.com/nostr-protocol/nips/pull/1669) (événements vidéo adressables) et un NIP de cryptographie post-quantique ouvrant la discussion sur la protection future de Nostr contre les attaques quantiques. Le brouillon des Attestations de confiance des relais a proposé de standardiser le scoring de confiance des relais via des attestations signées. Le [protocole Marmot](https://github.com/marmot-protocol/mdk) a durci sa messagerie chiffrée basée sur [MLS](/fr/topics/mls/) avec 18 PRs fusionnées répondant aux découvertes d'audit.

Les applications du monde réel se sont étendues avec [Ridestr](https://github.com/variablefate/ridestr) développant le covoiturage décentralisé utilisant le séquestre [Cashu](/fr/topics/cashu/) et le chiffrement [NIP-44](/fr/topics/nip-44/), et [Pomade](https://github.com/coracle-social/pomade) ajoutant des flux de récupération par email à la signature à seuil [FROST](/fr/topics/frost/). Damus a intégré [negentropy](/fr/topics/negentropy/) pour une synchronisation fiable des messages privés, tandis que l'application de bureau d'Amethyst a atteint la Phase 2A avec la recherche, les favoris et les zaps.

### Perspectives

Six années de janvier révèlent l'évolution de Nostr du développement précoce (2021) à la découverte publique (2022) à la croissance explosive (2023) au durcissement du protocole (2024) à la maturation des clients (2025) à l'infrastructure de sécurité (2026). Le modèle est familier à quiconque a observé la croissance des protocoles ouverts : des années de construction silencieuse, une explosion soudaine quand les conditions s'alignent, puis le travail plus long pour rendre tout cela fiable. Ce qui a commencé avec sept relais et un fil Hacker News est maintenant une infrastructure auditée avec des applications réelles. La question pour 2027 : quand quelqu'un appellera un trajet, enverra un message chiffré ou récupérera une clé perdue en utilisant Nostr, saura-t-il même qu'il l'utilise ?

---

C'est tout pour cette semaine. Vous construisez quelque chose ? Vous avez des nouvelles à partager ? Vous voulez que nous couvrions votre projet ? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contactez-nous via NIP-17 DM</a> ou trouvez-nous sur Nostr.
