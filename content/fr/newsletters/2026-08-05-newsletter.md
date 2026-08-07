---
title: "Nostr Compass #34"
date: 2026-08-05
publishDate: 2026-08-05
translationOf: /en/newsletters/2026-08-05-newsletter.md
translationDate: 2026-08-06
draft: false
type: newsletters
description: "Sandstr propose des visites guidées par données fictives des clients Nostr, nostr-mill ajoute un consentement de signature par événement, et nostrord étend les groupes hébergés sur relais. Les analyses approfondies couvrent la recherche relay-assistée et les surlignages portables."
---

Bienvenue dans [Nostr Compass](https://github.com/andotherstuff/nostr-compass), votre guide hebdomadaire de Nostr.

**Cette semaine :** [Sandstr](https://sandstr.app/) permet aux nouveaux venus d'explorer des clients Nostr simulés sans créer de clés ni installer d'application. [nostr-mill](https://github.com/0ceanSlim/nostr-mill) ajoute le consentement du signataire par événement et la récupération de clés entre clients, tandis que [nostrord](https://github.com/nostrord/nostrord) étend les groupes hébergés sur relais, les signataires, la modération, les téléversements et les surlignages. Le travail protocolaire couvre les formats d'événements Nostr, les connexions de portefeuille, la découverte de relais, les napplets, Marmot et Concord ; les analyses approfondies expliquent la recherche assistée par relais et les surlignages portables.

## À la une

### nostr-mill 1.6.0 apporte le consentement de signature et la récupération de compte dans le navigateur

[nostr-mill 1.6.0](https://github.com/0ceanSlim/nostr-mill/releases/tag/v1.6.0) est un sélecteur de compte et signataire intégrable au navigateur. Il demande désormais le consentement par kind d'événement et affiche le contenu et les tags décodés avant la signature, avec des autorisations à durée limitée et un gestionnaire de permissions. La version corrige également un bug de première session qui laissait les catégories configurées pour demander à chaque fois signer sans demander. Son onboarding Google optionnel peut importer un `nsec` existant, stocke la clé chiffrée dans le dossier de données d'application Drive de l'utilisateur, prend en charge plusieurs identités et peut exporter un `ncryptsec` au format [NIP-49](/fr/topics/nip-49/) (format de clé privée chiffrée).

La [sauvegarde expérimentale sur relais](https://github.com/0ceanSlim/nostr-mill/releases/tag/v1.6.0) dérive une phrase de récupération robuste avec scrypt et HKDF, enveloppe la clé en `ncryptsec`, vérifie les événements récupérés et exige un quorum de relais avant la récupération. La connexion [NIP-55](/fr/topics/nip-55/) (intents de signataire Android) utilise désormais le chemin de retour par presse-papiers d'Amber, et les connexions [NIP-46](/fr/topics/nip-46/) (signature distante relayée) sont silencieuses par défaut. Des contrôles de marque et des écrans de permissions responsives complètent la version sans modifier les intégrations existantes, sauf si l'opérateur l'active.

### nostrord 2.5.0 donne aux groupes de relais des identités stables et propres au relais

[nostrord 2.5.0](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) est un client multiplateforme pour communautés hébergées sur relais. Il dérive désormais une identité [NIP-29](/fr/topics/nip-29/) (groupes gérés par relais) à partir de l'ID de groupe et du relais hôte, délimite de la même façon l'appartenance et les badges d'administrateur, accepte les liens profonds `naddr` de groupe et synchronise les fils de groupes privés entre appareils.

La [version](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) ajoute également une boîte de réception de modération [NIP-56](/fr/topics/nip-56/) (événements de signalement), la connexion Amber via NIP-55, un backoff de limitation de débit pour le trafic du signataire NIP-46, le rendu [NIP-84](/fr/topics/nip-84/) (surlignages portables) avec nouvelles tentatives pour les références non résolues, et des téléversements de médias via Blossom ou [NIP-96](/fr/topics/nip-96/) (stockage de fichiers HTTP). La connexion Google sauvegarde désormais la clé avant la création du compte et confirme les déconnexions. Les réponses aux fils gagnent un contenu plus riche et la suppression par les administrateurs, tandis que des corrections du trousseau de bureau et du clavier mobile maintiennent ces fonctionnalités protocolaires utilisables.

### Primal Android 3.5.25 met à jour la signature distante et le filtrage des listes de suivi

[Primal Android 3.5.25](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.25) est un client mobile Nostr avec flux, recherche et signature distante. Il met à jour son signataire distant pour le comportement actuel du protocole, ajoute une liste de masqués des abonnements, ouvre la recherche depuis Explorer, répare automatiquement les connexions de relais bloquées, expose les délais d'expiration des requêtes dans l'interface, rejette les entrées invalides de la liste de suivi et actualise les URL de relais de secours. Le préchargement des flux, la réduction de la mémoire utilisée et un plafond de cache de 100 Mo réduisent le coût du maintien à jour de ces flux. Les notes à image unique utilisent désormais toute la largeur du contenu, et les contrôles de profil ainsi que le préchargement des médias reçoivent des corrections mineures d'interaction et d'ordonnancement.

### Nostur 1.30.2 étend les réponses privées et les médias dans les messages directs

[Nostur 1.30.2](https://github.com/nostur-com/nostur-ios-public/releases/tag/527) est un client Nostr pour plateformes Apple. Il expose toujours l'action de réponse privée, ajoute des caches de médias par conversation avec limites et contrôles d'effacement, améliore l'autocomplétion des noms et des tags dans les publications et les chats, affiche les messages référencés dans le chat en direct et inclut le titre du salon dans les notifications de chat. Les corrections de pagination du flux et des réponses imbriquées traitent des régressions de récupération et de rendu des conversations.

### Chama 5.7.0 ajoute les registres d'arbitres et la récupération d'échanges en cache

[Chama 5.7.0](https://github.com/jesuspirate/chama/releases/tag/v5.7.0) coordonne les échanges entre pairs et l'arbitrage via des chaînes d'événements Nostr signés. Il affiche le montant verrouillé d'un arbitre, l'ancienneté de sa caution et son outpoint de financement ; enregistre quand un remplaçant a pris la place d'un arbitre absent ; et définit les attestations de faute dormantes de kind `38136` qui exigent les signatures des deux principaux. Une réparation explicite retente les historiques de relais incomplets contre le cache durable de l'appareil et republie les événements récupérés, tandis que les publications échouées sont mises en file d'attente pour la prochaine connexion. La version empêche également les paiements en double de la prime d'arbitre entre appareils en traitant l'événement de kind `38113` de l'auteur comme l'enregistrement du paiement.

### Auditable Voting 0.1.165 rétablit la livraison des bulletins délégués

[Auditable Voting 0.1.165](https://github.com/tidley/auditable-voting/releases/tag/v0.1.165) organise des scrutins vérifiables en séparant les identifiants de l'électeur du contenu du bulletin. Il rétablit l'émission déléguée de bulletins aveugles grâce à la livraison authentifiée des délégations et au rattrapage des DM de contrôle, maintient les messages directs d'identifiants aveugles sur les relais privés configurés et met à jour le proxy d'audit en 0.1.52.

### Sandstr permet aux nouveaux venus d'essayer les clients Nostr avec des données fictives

[Sandstr](https://sandstr.app/) propose des simulations interactives en navigateur des clients Nostr pour qu'un nouveau venu puisse comparer leurs interfaces avant d'en installer un ou de créer une paire de clés. Son lancement du 3 août comprend des reproductions vérifiées sur référence de Damus, Amethyst, Primal, Snort, YakiHonne, Coracle et Wisp, ainsi que des aperçus précoces clairement étiquetés de Gossip, Keychat et Olas. Tout s'exécute localement sur des données fictives, donc les simulations ne génèrent ni clés ni connexions aux relais. Chaque simulation renvoie au site web et au dépôt de code du client réel, faisant de Sandstr un outil d'onboarding et de comparaison d'interfaces plutôt qu'un client Nostr de plus. Il montre comment se comportent flux, profils, fils, messages directs, recherche, zaps et contrôles de relais sans demander à un utilisateur novice de prendre d'avance une décision d'identité ou de sécurité.


### mineracks signer combine une extension de navigateur et un bunker de bureau

[mineracks signer](https://github.com/mineracks/mineracks-signer) offre deux surfaces de signature à partir du même projet. Son extension de navigateur implémente [NIP-07](/fr/topics/nip-07/) pour que les applications web puissent demander des signatures sans recevoir la clé privée, tandis que l'application de bureau expose un signataire distant [NIP-46](/fr/topics/nip-46/) pour les clients qui communiquent par relais.

La [version de bureau 0.1.0](https://github.com/mineracks/mineracks-signer/releases/tag/desktop-v0.1.0) du projet stocke le matériel de clés avec l'encodage de clés chiffrées de NIP-49 et garde la clé déchiffrée dans le processus Rust plutôt que de la transmettre à l'interface. Chaque requête affiche l'application appelante et l'action demandée, tandis que l'approbation automatique par application est optionnelle et révocable. La première compilation de bureau prend en charge Apple Silicon mais pas les Mac Intel.

## Versions

### Jumble 26.8.1 ajoute des contrôles de preuve de travail et des aperçus de commentaires

[Jumble 26.8.1](https://github.com/CodyTseng/jumble/releases/tag/v26.8.1) est un client Nostr web et de bureau. Il mémorise la difficulté de la preuve de travail pour la publication, affiche des badges de travail vérifié, prévisualise les commentaires liés au-dessus du contenu externe, enregistre les images depuis la visionneuse plein écran et déploie les longues biographies de profil à la demande. Les notifications de réaction écartent désormais les kinds d'événements non pris en charge, les avis de déconnexion de relais sont moins bruyants, les relais par défaut ont été actualisés et un conflit de lecture automatique des médias a été corrigé.

### nostr-calendar 2.1.0 rétablit la liaison du signataire pour les formulaires privés

[nostr-calendar 2.1.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v2.1.0) publie calendriers, événements et réponses de formulaires comme données Nostr. Il lie les soumissions de formulaires privés au signataire actif, enregistre les événements doublons intentionnels sur les relais, corrige la récupération depuis les relais, analyse les dates de calendrier en heure locale et ajoute des notifications d'application ainsi qu'un client iOS. La correction du signataire empêche une identité périmée de produire une réponse chiffrée inutilisable.

### Manent 2.0.0 ajoute l'étiquetage et la recherche pour les notes enregistrées

[Manent 2.0.0](https://github.com/dtonon/manent/releases/tag/v2.0.0) est une archive personnelle pour notes Nostr signées. Il ajoute des tags locaux et la recherche, permettant au lecteur d'organiser et de retrouver les événements enregistrés sans modifier leur contenu signé.

### nosvelte 0.6.1 ferme les abonnements vides après l'EOSE

[nosvelte 0.6.1](https://github.com/akiomik/nosvelte/releases/tag/v0.6.1) fournit des composants et des hooks Svelte réactifs pour les données de relais. Les recherches vides se concluent désormais à l'End of Stored Events, l'annulation ferme le `REQ` sous-jacent, les nouvelles tentatives effacent les erreurs périmées et les hooks de liste retournent leur valeur vide documentée. Il reconnaît aussi les événements adressables où qu'apparaisse leur tag `d`, remplace les métadonnées et articles supplantés, déduplique les réactions par ID d'événement et conserve chaque événement du premier lot d'un relais.

## Changements non publiés

### NMP lie l'admission au relais aux déclarations et élargit les requêtes de groupe

[NMP](https://github.com/pablof7z/nmp) est une boîte à outils TypeScript pour construire des applications Nostr et des interfaces de groupes adossées à des relais. La [PR #1254](https://github.com/pablof7z/nmp/pull/1254) fait suivre à l'admission au relais le propriétaire de la déclaration qui l'autorise, maintenant la décision de permission attachée à l'état Nostr signé. La [PR #1255](https://github.com/pablof7z/nmp/pull/1255) généralise les requêtes de groupes gérés par relais de [NIP-29](/fr/topics/nip-29/) au lieu de présumer une seule forme de recherche étroite. Les deux changements sont fusionnés mais ne sont pas encore apparus dans une version étiquetée.

### Mosaico dérive l'identité de groupe géré des enregistrements du relais

[Mosaico](https://github.com/pablof7z/mosaico) est un client Nostr pour parcourir et administrer des communautés gérées par relais. La [PR #758](https://github.com/pablof7z/mosaico/pull/758) dérive l'identité d'un groupe géré du relais qui héberge ses enregistrements faisant autorité. La [PR #757](https://github.com/pablof7z/mosaico/pull/757) observe l'enregistrement publié du groupe lors de la résolution de l'état d'administration. Cela distingue deux groupes aux noms similaires sur des relais différents et offre aux clients une source adossée au relais pour leurs métadonnées de gestion.

### Divine isole les relais lents lors des requêtes multi-relais

[Divine](https://github.com/divinevideo/divine-mobile) est un client mobile de vidéo courte qui publie et récupère des vidéos via Nostr. La [PR #6673](https://github.com/divinevideo/divine-mobile/pull/6673) donne à chaque requête de relais son propre délai d'expiration au lieu de laisser une connexion bloquée consommer le budget de temps de toute une requête. Les résultats des relais réactifs peuvent ainsi arriver pendant que le point de terminaison lent est abandonné indépendamment. Le changement améliore la récupération sans traiter un relais comme faisant autorité pour le résultat combiné.

### rust-nostr durcit le chiffrement, les hachages et la réconciliation

[rust-nostr](https://github.com/rust-nostr/nostr) est une bibliothèque et une boîte à outils Rust pour clients, relais et implémentations du protocole Nostr. La [PR #1421](https://github.com/rust-nostr/nostr/pull/1421) réduit les allocations dans son chemin de chiffrement versionné [NIP-44](/fr/topics/nip-44/), tandis que la [PR #1423](https://github.com/rust-nostr/nostr/pull/1423) introduit des hachages typés qui rendent plus difficile le mélange accidentel de valeurs de condensé incompatibles. Le [commit 21e31c2](https://github.com/rust-nostr/nostr/commit/21e31c28da3dfadedb5fa6e58c712647f16e5f69) empêche un message malformé de réconciliation d'ensembles Negentropy [NIP-77](/fr/topics/nip-77/) de déconnecter le relais local. Le travail fusionné resserre à la fois le traitement des charges chiffrées et le comportement d'échec de réconciliation avant la prochaine version.

### Zeus sérialise les paiements NWC avant de débiter les budgets de dépense

[Zeus](https://github.com/ZeusLN/zeus) est un portefeuille mobile Bitcoin et Lightning qui peut exposer des opérations de portefeuille via Nostr Wallet Connect. La [PR #4305](https://github.com/ZeusLN/zeus/pull/4305) comptabilise les paiements en attente dans un budget [NIP-47](/fr/topics/nip-47/) Nostr Wallet Connect au lieu d'attendre le règlement. La [PR #4303](https://github.com/ZeusLN/zeus/pull/4303) sérialise le traitement des paiements pour que les requêtes concurrentes ne puissent pas se précipiter à travers la même limite d'autorisation. Le couple fusionné comble une lacune d'application du budget sur la surface de contrôle Nostr du portefeuille.

### Nostr Components partage une seule tentative de connexion au relais

[Nostr Components](https://github.com/saiy2k/nostr-components) est une bibliothèque réutilisable de composants web pour ajouter des données et des interactions Nostr aux applications. La [PR #105](https://github.com/saiy2k/nostr-components/pull/105) permet aux composants montés en même temps de partager une tentative de connexion au relais en cours. Chaque consommateur reçoit toujours la connexion résultante, mais les montages concurrents n'ouvrent plus de sockets en double pendant que la première poignée de main est en attente. Le changement réduit la charge évitable sur les relais dans les applications assemblées à partir de plusieurs composants indépendants.

## Mises à jour des NIP et travail de spécification du protocole

### Formats d'événements Nostr et découverte

La [PR NIP #2430](https://github.com/nostr-protocol/nips/pull/2430) propose des packs d'autocollants comme définitions adressables de kind `30031` et les packs installés d'un utilisateur comme kind remplaçable `10031`. Chaque tag d'autocollant porte un code court, un hachage SHA-256 et un type MIME ; l'image reste sur un serveur [NIP-B7](https://github.com/nostr-protocol/nips/blob/master/B7.md) (stockage de blobs Blossom). Le brouillon ouvert standardise ainsi l'identité et l'installation des packs sans placer les octets d'image dans les événements.

La [PR NIP #2429](https://github.com/nostr-protocol/nips/pull/2429) propose des documents Gopher adressables de kind `31436`. Chaque événement contient un nœud de texte ou de menu UTF-8, et les nœuds signés sous une même pubkey forment un gopherhole que toute passerelle RFC 1436 adossée à un relais peut servir. La proposition ouverte utilise le stockage ordinaire des événements adressables plutôt que de lier la publication à un seul nom d'hôte Gopher.

La [PR NIP #2428](https://github.com/nostr-protocol/nips/pull/2428) propose des groupes privés à tickets par époque. Un groupe fait tourner les identifiants d'appartenance entre les époques, et les clients présentent le ticket de l'époque courante pour participer. Le brouillon vise le chat privé sans demander à un relais de traiter un jeton porteur permanent comme une appartenance à vie.

La [PR NIP #2425](https://github.com/nostr-protocol/nips/pull/2425), couverte comme proposition la semaine dernière, a maintenant fusionné une clarification d'URI dans [NIP-B0](/fr/topics/nip-b0/) (marque-pages web adressables). Elle distingue les préfixes HTTPS omis des schémas d'URI explicites lorsqu'un marque-page stocke sa cible dans le tag `d`, empêchant les clients de reconstruire une destination ambiguë.

### Paiements et connexions de portefeuille

La [PR NIP #2419](https://github.com/nostr-protocol/nips/pull/2419), couverte comme proposition dans l'édition du 22 juillet, a maintenant fusionné un noyau [NIP-47](/fr/topics/nip-47/) (Nostr Wallet Connect) réduit. Les URI de connexion, le transport chiffré par relais, la découverte de capacités, la négociation de chiffrement et les méthodes courantes restent dans le NIP ; les notifications, les factures en attente, keysend, l'historique des transactions, les métadonnées et l'appairage par lien profond passent dans un dépôt d'extensions dédié. Les connexions existantes restent compatibles tandis que les portefeuilles peuvent implémenter les contrats optionnels indépendamment.

La [PR NWC #2](https://github.com/nostr-wallet-connect/nwc/pull/2), couverte comme proposition la semaine dernière, a maintenant fusionné les méthodes de paiement BIP-321 dans ce dépôt d'extensions. BIP-321 fournit un URI de paiement Bitcoin commun qui peut porter différents rails, de sorte que les appelants NWC peuvent demander ou envoyer un paiement sans ajouter un nouveau RPC central pour chaque type d'instruction sous-jacent.

### Capacités de l'hôte de napplets

La [PR NAP #95](https://github.com/napplet/naps/pull/95) propose la découverte de catalogues pour les applications en sandbox distribuées par Nostr. Un napplet demande à son hôte quelles applications et capacités sont disponibles, et l'hôte renvoie des métadonnées filtrées par politique au lieu d'exposer tout son environnement local. Le contrat prend en charge les décisions de lancement sans accorder d'autorité d'exécution pendant la découverte.

La [PR NAP #33](https://github.com/napplet/naps/pull/33) propose des téléversements de fichiers et de blobs médiés par le shell. Un napplet fournit les octets et l'intention ; l'hôte sélectionne un rail NIP-96 ou Blossom, signe l'autorisation, rend compte de la progression et renvoie des URL, des hachages, des données MIME et des tags [NIP-94](/fr/topics/nip-94/) (métadonnées de fichier) prêts à joindre. Les identifiants de stockage et l'autorité HTTP n'entrent jamais dans le napplet.

### Groupes chiffrés Marmot

La [PR Marmot #410](https://github.com/marmot-protocol/marmot/pull/410) a fusionné des règles de convergence et d'entrée différée. Les clients distinguent un objet auquel il manque une dépendance d'époque courante d'une entrée périmée ou invalide, le gardent éligible à une nouvelle récupération après un refus de ressources et réessayent lorsqu'un autre commit change le contexte de déchiffrement. Un engagement d'état à séparation de domaine offre aux tests de conformité un oracle de convergence partagé sans ajouter de champ de production au protocole.

### Plans communautaires Concord

La [PR Concord #14](https://github.com/concord-protocol/concord/pull/14) a fusionné les messages éphémères CORD-08. Une valeur de métadonnées de communauté fixe la durée de vie ; les rumeurs de chat et les enveloppes chiffrées portent un tag [NIP-40](/fr/topics/nip-40/) (expiration d'événement), tandis que les événements de suppression et l'avis de minuterie de kind `1740` en sont exemptés. La minuterie signée voyage avec l'état de la communauté, bien que la suppression par le relais reste une demande de rétention et non une garantie cryptographique d'effacement.

La [PR Concord #13](https://github.com/concord-protocol/concord/pull/13) a fusionné dans CORD-04 l'épinglage résistant aux rotations. Chaque salon a une liste d'épinglés à remplacement complet sur le plan de contrôle ; les entrées portent le sceau signé original plus des clés d'expansion NIP-44 par message, permettant à un nouveau membre de vérifier l'auteur et le texte en clair sans recevoir une ancienne clé d'époque. Les listes privées peuvent rester scellées à une époque du salon, des plafonds bornent la taille de la liste, et les suppressions de l'auteur retirent les épinglés sans bifurquer la chaîne du plan de contrôle.

## Analyse approfondie de NIP

### Capacité de recherche (NIP-50)

[NIP-50](/fr/topics/nip-50/), défini dans la [spécification principale](https://github.com/nostr-protocol/nips/blob/master/50.md), ajoute un filtre de recherche optionnel pour les relais. Les filtres Nostr ordinaires fonctionnent quand un client connaît déjà un auteur, un kind d'événement, un identifiant ou un tag ; NIP-50 adresse la découverte quand l'entrée est une requête humaine comme `best nostr apps`.

Le [format réseau de NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md#search-filter-field) ajoute une chaîne `search` à un filtre normal dans un message `REQ`. Une requête peut combiner ce champ avec `kinds`, `authors`, `ids`, des filtres de tags et `limit`, et un REQ peut porter plusieurs filtres indépendants. Un relais compatible devrait chercher principalement dans le `content` de l'événement, peut utiliser d'autres champs quand le kind d'événement le rend utile, et devrait trier selon son propre score de pertinence avant d'appliquer le `limit`. Cet ordre diffère du flux d'événements habituel du plus récent au plus ancien.

La chaîne de requête peut inclure les [extensions `key:value`](https://github.com/nostr-protocol/nips/blob/master/50.md#extensions) de la spécification. Elle nomme `include:spam`, `domain:`, `language:`, `sentiment:` et `nsfw:` ; un relais devrait ignorer les extensions qu'il n'implémente pas. Les clients découvrent le support déclaré via le champ `supported_nips` du [NIP-11](/fr/topics/nip-11/) du relais, mais peuvent tout de même envoyer le filtre ailleurs s'ils sont prêts à rejeter les réponses sans rapport.

La [spécification NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md) ne standardise délibérément ni la tokenisation, ni le stemming, ni le classement, ni la détection de langue, ni l'analyse de sentiment, ni la classification du spam. Deux relais conformes peuvent renvoyer des événements et des ordres différents pour la même requête. Cela fait du relais un fournisseur d'index et de classement, non une source de vérité. La spécification recommande d'interroger plusieurs relais compatibles, de vérifier si les événements retournés satisfont le cas d'usage du client, et d'abandonner les relais dont les résultats ont une mauvaise précision.

Cela diffère du [filtrage exact de NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md). Un filtre `authors` ou `#t` a une sémantique de correspondance déterministe qu'un client peut vérifier directement, tandis qu'une correspondance de recherche peut dépendre d'un index et d'un score opaque. NIP-50 conserve l'enveloppe d'événement signée et le transport de relais de NIP-01, mais accepte une variation du rappel et de l'ordre pour rendre possible la récupération ouverte.

L'événement ci-dessous est un résultat de recherche illustratif utilisant les [sept champs d'événement de NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md#events-and-signatures). Les valeurs hexadécimales répétées sont des espaces réservés et non une signature valide.

```json
{
  "id": "2943d6b43bcbf0ee4a8b4cac912111be0309607b8bb435ae40529989bea7f6c5",
  "pubkey": "3bf0c63fcb93463407af97a5e5ee64fa883d107ef9e558472c4eb9aaaefa459d",
  "created_at": 1785771175,
  "kind": 1,
  "tags": [],
  "content": "I've been working on a customizable client (mostly relay feeds, but a ton of other things and subtle details too). It's called Hallway for reasons I don't remember and it's a fork of Fevela which is a fork of Jumble, but very rewritten for speed and simplicity...",
  "sig": "5b058b89dab9bd09d81bdc10eff95536125b87fbcbbc97f08d835c1272b2a3190cc3d340e42f54acb0d7e0e4b00355ab91292d0305c84a2d73b538319c0da12c"
}
```

Les clients actuels utilisent le même filtre dans différentes surfaces de découverte. [Nostria](https://github.com/nostria-app/nostria/blob/d291c2ab091c60c36f99c90241e2fd9da1b0c4bc/src/app/services/relays/search-relay.ts) envoie des recherches NIP-50 à des relais de recherche dédiés, [Ditto](https://github.com/soapbox-pub/ditto/blob/04adb2d242ab6f5807fd27ae3e0cb9beab091641/src/hooks/useSearchEvents.ts) recherche des événements via son pool de relais, et [NoorNote](https://github.com/77elements/noornote/blob/bf1f9b431552497dc1779ea0d8fed2c3c28e6070/src/services/orchestration/SearchOrchestrator.ts) coordonne des recherches adossées à des relais pour la lecture de format long. Leur traitement différent des résultats reflète la latitude que NIP-50 laisse aux relais et aux clients.

### Surlignages (NIP-84)

[NIP-84](/fr/topics/nip-84/), défini par sa [spécification principale](https://github.com/nostr-protocol/nips/blob/master/84.md), attribue le kind `9802` à un surlignage. Il transforme un passage sélectionné, ou une référence à un média non textuel, en un événement signé qui peut circuler entre clients de lecture, sociaux et d'annotation.

Le [`content` de l'événement](https://github.com/nostr-protocol/nips/blob/master/84.md#format) contient le texte sélectionné et peut être vide lorsque la source est de l'audio, de la vidéo ou un autre média non textuel. Un surlignage pointe vers une source Nostr avec un tag `a` pour un événement adressable ou un tag `e` pour un événement ordinaire ; un tag `r` identifie une URL web. Les clients qui produisent des URL devraient retirer les paramètres de suivi et autres paramètres de requête inutiles avant de publier, afin que des variantes cosmétiques d'URL ne fragmentent pas les références à la même source.

Les [tags `p`](https://github.com/nostr-protocol/nips/blob/master/84.md#attribution) optionnels attribuent la source à une ou plusieurs pubkeys Nostr. Leur quatrième valeur peut identifier un rôle comme `author` ou `editor`, et un tag `context` peut préserver le texte environnant lorsque la sélection seule serait peu claire. Un surlignage avec citation ajoute un tag `comment` au lieu de publier une seconde note de kind `1` : le tag `r` de la source reçoit le marqueur `source`, tandis que les pubkeys ou URL mentionnées dans le commentaire portent `mention`, permettant aux moteurs de rendu de distinguer l'attribution de la réponse de l'utilisateur.

La [définition du kind `9802`](https://github.com/nostr-protocol/nips/blob/master/84.md) fait d'un surlignage un événement régulier plutôt que remplaçable. Répéter ou corriger une sélection crée un autre événement signé, et en supprimer un repose sur le flux normal de demande de suppression et la politique de rétention du relais. La spécification ne définit ni décalages d'octets, ni sélecteurs, ni instantané canonique du document, de sorte qu'un client peut être incapable de relocaliser un passage après que sa source web a changé. Les surlignages publics révèlent aussi des intérêts de lecture ; l'annotation privée exige une conception séparée de chiffrement et de partage.

NIP-84 diffère d'un [événement de format long NIP-23](https://github.com/nostr-protocol/nips/blob/master/23.md), qui publie un article entier comme kind `30023` ; un surlignage cite ou pointe dans du matériel qui peut rester ailleurs. Il diffère aussi d'un [ensemble de marque-pages NIP-51](https://github.com/nostr-protocol/nips/blob/master/51.md), qui stocke une collection remplaçable de références. NIP-84 rend chaque sélection indépendamment signée, attribuable, découvrable et discutable.

Ce surlignage illustratif contient les [sept champs d'événement de NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md#events-and-signatures). Son identifiant et sa signature sont des espaces réservés.

```json
{
  "id": "0d57c07cfdfe8ec00711e2af88a666b61fc35c167b90b02dfb5db7ffba7b794a",
  "pubkey": "07367baec8e73c076b14e47fba3b0d5c014d559d7986a7172a79a8a64419d7c2",
  "created_at": 1785797755,
  "kind": 9802,
  "tags": [
    ["context", "Quantum computers will break secp256k1 which nostr relies on for its public private key pair. This means that given an npub, a quantum computer will be able to derive your nsec, read all your encrypted data and sign events as you."],
    ["alt", "This is a highlight created in https://primal.net iOS application"],
    ["a", "30023:1ec454734dcbf6fe54901ce25c0c7c6bca5edd89443416761fadc321d38df139:nostr-quantum-preparation"],
    ["p", "1ec454734dcbf6fe54901ce25c0c7c6bca5edd89443416761fadc321d38df139", "", "mention"]
  ],
  "content": "Quantum computers will break secp256k1 which nostr relies on for its public private key pair. This means that given an npub, a quantum computer will b",
  "sig": "219f3c1e572d1a087d667dc0d3a5443c77c0db3a5d42ce4e630604901ac63d2c879a86269d81e220bb77fd48b1579adafc333075e53c6eb0a108791fdd4a1622"
}
```

Le format franchit déjà les frontières entre clients. [nostrord 2.5.0](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) a ajouté le rendu NIP-84 cette semaine, [NoorNote](https://github.com/77elements/noornote/blob/bf1f9b431552497dc1779ea0d8fed2c3c28e6070/src/components/ui/note-rendering/HighlightRenderer.ts) rend les événements de surlignage dans son client de format long, et [Ditto](https://github.com/soapbox-pub/ditto/blob/04adb2d242ab6f5807fd27ae3e0cb9beab091641/src/hooks/useCreateHighlight.ts) les publie à partir du contenu sélectionné. Ces implémentations couvrent la lecture, la création et le rendu social sans exiger qu'un seul service possède l'annotation.

---

Envoyez un DM NIP-17 pour partager un projet ou une actualité via le [projet Nostr Compass](https://github.com/andotherstuff/nostr-compass).
