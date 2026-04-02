---
title: 'Nostr Compass #14'
date: 2026-03-18
translationOf: /en/newsletters/2026-03-18-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

Bienvenue dans Nostr Compass, votre guide hebdomadaire sur Nostr.

**Cette semaine :** [Amethyst](https://github.com/vitorpamplona/amethyst) implémente le support complet des méthodes [NIP-47](/fr/topics/nip-47/) (Nostr Wallet Connect), [Alby Hub](https://github.com/getAlby/hub) ajoute le support multi-relays dans [v1.21.6](https://github.com/getAlby/hub/releases/tag/v1.21.6), [Amber](https://github.com/greenart7c3/Amber) livre [v4.1.3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3) avec Tor intégré et des permissions de signature plus fines, et [Zeus](https://github.com/ZeusLN/zeus) supprime un chemin NWC keysend risqué dans [PR #3835](https://github.com/ZeusLN/zeus/pull/3835). [Notedeck](https://github.com/damus-io/notedeck) livre un updater signé dans [v0.8.0-rc2](https://github.com/damus-io/notedeck/releases/tag/v0.8.0-rc2) qui découvre les versions via des événements [NIP-94](/fr/topics/nip-94/) (File Metadata), tandis que [Damus](https://github.com/damus-io/damus) corrige l'état [NIP-65](/fr/topics/nip-65/) (Relay List Metadata) obsolète, [Nostrability Outbox](https://github.com/nostrability/outbox) révise ses résultats de benchmark avec des données corrigées, et [Primal iOS](https://github.com/PrimalHQ/primal-ios-app) teste les abonnements directs aux relays pour les DMs. [Primal Android](https://github.com/PrimalHQ/primal-android-app) livre [3.0.7](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.7), [Route96](https://github.com/v0l/route96) livre [v0.6.0](https://github.com/v0l/route96/releases/tag/v0.6.0), [OpenChat](https://github.com/DavidGershony/openChat) continue de renforcer l'interopérabilité Marmot dans [v0.1.0-alpha.11](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.11), [Pika](https://github.com/sledtools/pika) consolide son runtime dans [pika/v1.1.1](https://github.com/sledtools/pika/releases/tag/pika/v1.1.1), et [Nostria](https://github.com/nostria-app/nostria) ajoute le filtrage Web of Trust via [NIP-85](/fr/topics/nip-85/) (Trusted Assertions). Le dépôt NIPs fusionne le balisage Djot pour [NIP-54](/fr/topics/nip-54/) (Wiki) et un plafond de 5 000 caractères pour [NIP-19](/fr/topics/nip-19/) (Bech32-Encoded Entities), tandis que les PRs ouvertes proposent un format de fichier `.nostrkey` pour [NIP-49](/fr/topics/nip-49/) (Private Key Encryption), une clarification de la cohérence d'appartenance pour [NIP-43](/fr/topics/nip-43/) (Relay Access Metadata and Requests), des conseils de suppression pour [NIP-17](/fr/topics/nip-17/) (Private Direct Messages) et un URI d'intention de partage pour [NIP-222](/fr/topics/nip-222/).

## Actualités

### Le support Wallet Connect s'élargit, et les clients de portefeuille resserrent les chemins d'erreur

[Amethyst](https://github.com/vitorpamplona/amethyst), le client Android maintenu par vitorpamplona, a fusionné [PR #1828](https://github.com/vitorpamplona/amethyst/pull/1828), qui rapproche son implémentation [NIP-47](/fr/topics/nip-47/) d'une couverture complète du protocole. Le patch ajoute `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance`, `get_info`, les méthodes de hold invoices, le support keysend avec enregistrements TLV, la découverte de capacités via le kind `13194`, et les événements de notification sur le kind `23197` avec [NIP-44](/fr/topics/nip-44/) (Encrypted Payloads). Cela donne au client une surface NWC bien plus large sans s'appuyer sur des extensions spécifiques à une application.

La pile de portefeuilles environnante a évolué dans la même direction. [Alby Hub](https://github.com/getAlby/hub), le nœud Lightning auto-hébergé et service de portefeuille derrière de nombreux déploiements NWC, a livré [v1.21.6](https://github.com/getAlby/hub/releases/tag/v1.21.6) avec le support multi-relays et des flux de connexion et de swap simplifiés. [Zeus](https://github.com/ZeusLN/zeus), le portefeuille Lightning mobile, a fusionné [PR #3835](https://github.com/ZeusLN/zeus/pull/3835) supprimant le support NWC keysend après avoir identifié un chemin silencieux de drainage de fonds dans ce flux, tout en corrigeant aussi la gestion des événements en attente et de l'activité Cashu. La connectivité des portefeuilles sur Nostr s'élargit, et les implémenteurs suppriment les flux difficiles à sécuriser.

### Notedeck déplace la découverte de versions sur Nostr

[Suite à la couverture de Notedeck la semaine dernière](/en/newsletters/2026-03-11-newsletter/), [Notedeck](https://github.com/damus-io/notedeck), le client desktop natif de l'équipe Damus, a livré [v0.8.0-rc2](https://github.com/damus-io/notedeck/releases/tag/v0.8.0-rc2) après avoir fusionné [PR #1326](https://github.com/damus-io/notedeck/pull/1326). Le nouvel updater s'abonne aux événements de version signés de kind `1063`, identifie la plateforme locale, télécharge le binaire référencé et vérifie son hachage SHA256 avant l'installation. Les métadonnées de version n'ont plus besoin de provenir de l'API GitHub ou d'un site web de projet. Une pubkey de confiance et une connexion relay suffisent.

Le même patch ajoute un CLI `notedeck-release` qui publie ces événements depuis les artefacts de version GitHub, ce qui signifie que le pipeline de publication dispose maintenant d'un chemin de publication natif Nostr ainsi que d'un chemin de découverte natif Nostr. Cela rapproche aussi le modèle de mise à jour Damus et Notedeck du flux de publication signée de Zapstore via relay : l'outillage `zsp` de Zapstore gère déjà les artefacts logiciels comme événements kind `1063` ou `3063`, donc ce chemin n'est pas verrouillé sur un seul client ou un seul éditeur. Le reste du release candidate est du travail desktop pratique : colonnes de suivi, « View As User » pour les profils, support [NIP-59](/fr/topics/nip-59/) (Gift Wrap), statistiques de notes en temps réel et gestion des limitations [NIP-11](/fr/topics/nip-11/) (Relay Information Document), mais l'updater est la partie susceptible de survivre au-delà de ce seul cycle de version.

### L'état des relays se rapproche du comportement en temps réel

[Damus](https://github.com/damus-io/damus) a fusionné [PR #3665](https://github.com/damus-io/damus/pull/3665), remplaçant un identifiant d'événement de liste de relays obsolète par une requête directe à la base de données pour le dernier événement kind `10002`. Quand l'ancienne valeur devenait obsolète, les opérations d'ajout et de suppression de relays pouvaient se rabattre sur des listes d'amorçage ou vieilles d'un an, ce qui faisait que certains changements de relays semblaient réussir tout en laissant l'état actif inchangé. [PR #3690](https://github.com/damus-io/damus/pull/3690) corrige un second chemin d'échec en supprimant l'état `lock.mdb` obsolète durant la compaction LMDB pour que l'application ne plante pas avec `SIGBUS` au prochain lancement.

[Primal iOS](https://github.com/PrimalHQ/primal-ios-app) a ouvert [PR #194](https://github.com/PrimalHQ/primal-ios-app/pull/194), qui s'abonne directement aux relays d'écriture [NIP-04](/fr/topics/nip-04/) (Encrypted Direct Messages) d'un partenaire de chat pendant qu'une conversation est ouverte, gardant le serveur de cache comme repli. [Nostur](https://github.com/nostur-com/nostur-ios-public) a ouvert [PR #53](https://github.com/nostur-com/nostur-ios-public/pull/53), qui combine le scoring aléatoire de relays, le filtrage de disponibilité [NIP-66](/fr/topics/nip-66/) depuis nostr.watch, et l'échantillonnage de Thompson pour passer la sélection de relays d'une heuristique fixe à une politique apprise. Les clients ont longtemps traité le choix de relay comme une donnée de configuration. De plus en plus d'applications le traitent maintenant comme un état en direct qui nécessite une logique de mesure et de réparation.

## Versions

### Primal Android 3.0.7

[Primal Android](https://github.com/PrimalHQ/primal-android-app), le client Android de Primal, a livré [3.0.7](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.7) avec un nouveau cycle de sondages et de portefeuille. [PR #945](https://github.com/PrimalHQ/primal-android-app/pull/945) ajoute le vote par sondage basé sur les zaps, [PR #948](https://github.com/PrimalHQ/primal-android-app/pull/948) pagine le chargement des votes pour que les sondages plus importants restent utilisables, et [PR #965](https://github.com/PrimalHQ/primal-android-app/pull/965) récupère les reçus de zap pour toutes les transactions. La même version tague aussi les événements supportés avec les métadonnées client [NIP-89](/fr/topics/nip-89/) (Recommended Application Handlers) dans [PR #968](https://github.com/PrimalHQ/primal-android-app/pull/968), ce qui aide les clients en aval à attribuer les origines des événements plus proprement.

### Amber v4.1.3

[Suite à la couverture d'Amber la semaine dernière](/en/newsletters/2026-03-11-newsletter/), [Amber](https://github.com/greenart7c3/Amber), l'application de signature Android pour les flux [NIP-55](/fr/topics/nip-55/) (Android Signer Application), a livré [v4.1.3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3). La version s'appuie sur son récent travail d'authentification relay [NIP-42](/fr/topics/nip-42/) avec plus de durcissement opérationnel : [PR #327](https://github.com/greenart7c3/Amber/pull/327) ajoute Tor intégré aux côtés du support Orbot, [PR #324](https://github.com/greenart7c3/Amber/pull/324) remplace les permissions de chiffrement grossières basées sur les NIP par des règles spécifiques au type de contenu, et [PR #336](https://github.com/greenart7c3/Amber/pull/336) supprime les permissions réseau de la variante hors ligne tandis que [PR #335](https://github.com/greenart7c3/Amber/pull/335) ajoute des vérifications CI pour le maintenir ainsi. [PR #322](https://github.com/greenart7c3/Amber/pull/322) déplace aussi le stockage du PIN vers un DataStore chiffré.

Cette version resserre la frontière du signataire lui-même. C'est utile pour tout flux Android qui confie de vraies clés ou des décisions d'authentification relay à Amber, car la difficulté n'est pas seulement ce que le signataire peut faire. C'est aussi à quel point il peut être restreint.

### Route96 v0.6.0

[Suite à la couverture de Route96 la semaine dernière](/en/newsletters/2026-03-11-newsletter/), [Route96](https://github.com/v0l/route96), le serveur de médias qui supporte Blossom et [NIP-96](/fr/topics/nip-96/) (HTTP File Storage), a livré [v0.6.0](https://github.com/v0l/route96/releases/tag/v0.6.0). La version déplace la configuration et l'état de la liste blanche dans la base de données avec rechargement à chaud et ajoute des politiques de rétention pour les fichiers froids ou vieillissants. Elle ajoute aussi un endpoint `GET /user/files` plus riche ainsi que le suivi des statistiques de fichiers pour les téléchargements et le trafic sortant, ce qui donne aux opérateurs plus de visibilité sur l'utilisation de leur serveur de stockage.

### OpenChat v0.1.0-alpha.11

[Suite à la couverture d'OpenChat la semaine dernière](/en/newsletters/2026-03-11-newsletter/), [OpenChat](https://github.com/DavidGershony/openChat), le client de chat basé sur Avalonia construit sur la pile Marmot, a livré [v0.1.0-alpha.11](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.11) après une semaine de travail protocolaire rapide. [Commit c33895d](https://github.com/DavidGershony/openChat/commit/c33895d6b1a198f01b9b01a7be974bdce033fb9c) encapsule les événements Welcome dans un gift wrap [NIP-59](/fr/topics/nip-59/) et supprime les anciens shims de normalisation de tags MIP-00, [commit 2738ff4](https://github.com/DavidGershony/openChat/commit/2738ff428154f60f50debb8f2a53662d427b28f1) complète l'audit de conformité MIP-02, et [commit 8e470cf](https://github.com/DavidGershony/openChat/commit/8e470cf7945bced010168c8229d73d67db638b9f) fait de même pour le chiffrement des messages de groupe MIP-03. [Commit 129ca37](https://github.com/DavidGershony/openChat/commit/129ca37e264efaa2d1a8b04fe95cd72e5e212547) consolide aussi la gestion NIP-44 sur l'implémentation partagée marmot-cs, réduisant le risque de dérive cryptographique côté client.

### nak v0.19.0 et v0.19.1

[nak](https://github.com/fiatjaf/nak), la boîte à outils Nostr en ligne de commande de fiatjaf, a livré [v0.19.0](https://github.com/fiatjaf/nak/releases/tag/v0.19.0) et [v0.19.1](https://github.com/fiatjaf/nak/releases/tag/v0.19.1). La série 0.19 ajoute une interface de forum de groupe dans [commit 5f4efdb](https://github.com/fiatjaf/nak/commit/5f4efdbc69a36fc80ea3f97b2cdee1db6a7c5b47), passe les modifications de métadonnées de groupe à un flux de remplacement complet dans [commit da0b753](https://github.com/fiatjaf/nak/commit/da0b75337198010687aceb6a07bbae67407faee3), et remplace l'ancien traitement `no-text` par `supported_kinds` dans [commit bef67d3](https://github.com/fiatjaf/nak/commit/bef67d35d259e0450debf0fd870e1a937a2406bf). Pour les implémenteurs de groupes, cela garde le CLI aligné avec la direction que prennent les spécifications et clients de groupes.

## Mises à jour des projets

### Amethyst

[Suite à la couverture d'Amethyst la semaine dernière](/en/newsletters/2026-03-11-newsletter/), [Amethyst](https://github.com/vitorpamplona/amethyst), le client Android avec l'une des surfaces protocolaires les plus larges de Nostr, a continué à développer son travail sur les portefeuilles et les relays après le patch NIP-47. [PR #1853](https://github.com/vitorpamplona/amethyst/pull/1853) ajoute des requêtes COUNT [NIP-45](/fr/topics/nip-45/) (Event Counting) à travers les écrans de gestion des relays, pour que les utilisateurs puissent voir combien d'événements chaque relay détient réellement pour le flux d'accueil, les notifications, les DMs et les données d'index. [PR #1849](https://github.com/vitorpamplona/amethyst/pull/1849) ajoute les téléversements de fichiers chiffrés pour les chats [NIP-17](/fr/topics/nip-17/) (Private Direct Messages), avec un chemin de repli pour les téléversements non chiffrés quand un hôte de stockage rejette la version chiffrée.

[PR #1791](https://github.com/vitorpamplona/amethyst/pull/1791) apporte aussi la connexion complète au bunker desktop [NIP-46](/fr/topics/nip-46/) (Nostr Connect) avec un indicateur de heartbeat, ce qui compte parce que les échecs de signature à distance ressemblent souvent à des bugs aléatoires d'interface du côté de l'utilisateur. Le client montre si le signataire est en vie et quand il a répondu pour la dernière fois, tout en rendant évident quand la session en cours utilise un bunker.

### Nostria

[Nostria](https://github.com/nostria-app/nostria), le client multi-plateforme construit autour d'une pile local-first, a fusionné [PR #561](https://github.com/nostria-app/nostria/pull/561) ajoutant le filtrage Web of Trust pour les flux et les réponses de fils. La fonctionnalité utilise les données de rang du service de confiance existant et les expose à la fois comme filtre de flux et filtre de réponses, masquant les auteurs dont le rang ne dépasse pas le seuil tout en préservant la structure du fil quand des descendants de confiance sont présents. Cela donne aux utilisateurs une couche intermédiaire entre « montrer tout le monde » et la curation basée sur des listes codées en dur.

La même semaine a aussi apporté [PR #563](https://github.com/nostria-app/nostria/pull/563), qui ajoute le filtrage de contenu et le support des reposts sur la page de résumé. En dehors de la liste de PRs suivies, Nostria a aussi complété davantage sa surface pour utilisateurs avancés. Il supporte maintenant le dernier service Brainstorm Web of Trust avec inscription intégrée, ainsi que des flux d'envoi et de réception d'argent dans les DMs utilisant NWC et les invoices BOLT-11. Il ajoute aussi la gestion native de GIFs Nostr via le NIP emoji et un chemin d'import RSS renforcé pour les musiciens qui peut récupérer les répartitions Lightning existantes depuis les flux de podcasts. Nostria traite le classement, les médias, les paiements et la publication comme une seule surface d'application connectée.

### Nostur

[Nostur](https://github.com/nostur-com/nostur-ios-public), le client iOS maintenu par nostur-com, a ouvert [PR #53](https://github.com/nostur-com/nostur-ios-public/pull/53) pour passer le routage outbox d'un plan fixe à une politique scorée. Le patch ajoute le scoring aléatoire de relays, le filtrage de disponibilité [NIP-66](/fr/topics/nip-66/) avec un flux nostr.watch en cache, et l'échantillonnage de Thompson pour que les données de succès et d'échec des relays modifient les sélections futures. La conception conserve une soupape de sécurité quand trop de relays seraient filtrés et préserve les relays `.onion`. C'est l'un des exemples actuels les plus clairs d'un client traitant la sélection de relays comme un système adaptatif.

### Nostrability Outbox

[Suite au précédent rapport de benchmark Outbox](/fr/newsletters/2026-03-04-newsletter/), [Nostrability Outbox](https://github.com/nostrability/outbox), le projet de benchmark et d'analyse centré sur le routage client [NIP-65](/fr/topics/nip-65/) et [NIP-66](/fr/topics/nip-66/), a passé la semaine à resserrer ses propres affirmations. [PR #35](https://github.com/nostrability/outbox/pull/35) remplace les résultats d'échantillonnage de Thompson gonflés par un re-benchmark complet sur 1 511 exécutions et recommande la variante `CG3` pour le routage de type NDK. [PR #43](https://github.com/nostrability/outbox/pull/43) ajoute des comparaisons de décroissance et de cas d'usage, corrige un bug d'empoisonnement de cache `0 follows`, puis relance le jeu de données Telluride après avoir fixé les TTL de cache.

Ce n'est pas du travail produit au sens habituel, mais c'est important pour les auteurs de clients car les chiffres du projet sont maintenant plus précis et moins flatteurs aux endroits où ils avaient précédemment surestimé. Le résultat corrigé reste utile. La sélection aléatoire continue de battre le routage purement déterministe dans les cas qui intéressent Outbox, l'apprentissage de type Thompson peut améliorer matériellement la couverture quand les clients persistent l'historique utile des relays, et le filtrage de disponibilité [NIP-66](/fr/topics/nip-66/) réduit le temps perdu sur les relays morts. Le travail se transforme aussi en propositions d'implémentation concrètes, incluant [NDK #387](https://github.com/nostr-dev-kit/ndk/pull/387), [Nostur #53](https://github.com/nostur-com/nostur-ios-public/pull/53), [Amethyst #1833](https://github.com/vitorpamplona/amethyst/pull/1833), [rust-nostr #1282](https://github.com/rust-nostr/nostr/pull/1282), [welshman #53](https://github.com/coracle-social/welshman/pull/53), et [applesauce #54](https://github.com/hzrd149/applesauce/pull/54) plus [applesauce #55](https://github.com/hzrd149/applesauce/pull/55).

### Backend White Noise

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs), le backend Rust utilisé par White Noise et d'autres outils Marmot, a fusionné deux patchs de durcissement des frontières autour de la gestion des médias Blossom. [PR #637](https://github.com/marmot-protocol/whitenoise-rs/pull/637) impose HTTPS sur les URLs Blossom et ajoute un timeout de téléversement, tandis que [PR #642](https://github.com/marmot-protocol/whitenoise-rs/pull/642) plafonne les téléchargements de blobs à `100 MiB` pour empêcher les téléchargements de médias surdimensionnés de se transformer en chemin de déni de service. Pour un logiciel de messagerie privée, les URLs de médias sont l'une des interfaces les plus sensibles entre la logique applicative chiffrée et l'infrastructure réseau non fiable. Cette semaine, l'équipe a resserré cette frontière.

### rust-nostr

[rust-nostr](https://github.com/rust-nostr/nostr), la bibliothèque de protocole Rust, a fusionné [PR #1280](https://github.com/rust-nostr/nostr/pull/1280) ajoutant des constructeurs de commodité pour `LocalRelayBuilderNip42`. Les nouveaux helpers de lecture et d'écriture donnent aux configurations de relays embarqués et de tests un moyen plus clair de transformer la politique d'authentification [NIP-42](/fr/topics/nip-42/) en code. C'est un petit patch de bibliothèque, mais il compte pour les équipes construisant des relays locaux ou intégrés aux applications qui ont besoin de l'authentification activée sans répéter du code standard à chaque fois.

### Pika

[Suite à la couverture précédente de Pika](/fr/newsletters/2026-03-04-newsletter/), [Pika](https://github.com/sledtools/pika), l'application de messagerie basée sur Marmot, a livré [pika/v1.1.1](https://github.com/sledtools/pika/releases/tag/pika/v1.1.1) et [pikachat-v1.1.1](https://github.com/sledtools/pika/releases/tag/pikachat-v1.1.1) avec un cycle de versions centré sur la convergence du runtime. [PR #542](https://github.com/sledtools/pika/pull/542) introduit une façade de runtime Marmot partagée pour le CLI et le sidecar, avec l'hôte de l'application migrant sur la même surface. [PR #556](https://github.com/sledtools/pika/pull/556) resserre le cycle de vie des agents OpenClaw et l'état de provisionnement, tandis que [PR #600](https://github.com/sledtools/pika/pull/600) ajoute la restauration depuis une sauvegarde et une sécurité de récupération plus stricte pour les environnements gérés.

La surface utilisateur directe ici est plus petite que dans le dernier article sur Pika, mais le changement architectural est significatif. Regrouper la logique de groupe, média, appel et session derrière un seul runtime partagé réduit les chances que l'application et le démon divergent à mesure que la pile Marmot grandit.

## Mises à jour des NIP

Changements récents dans le [dépôt NIPs](https://github.com/nostr-protocol/nips) :

**Fusionnés :**

- **[NIP-54](/fr/topics/nip-54/) (Wiki) : Passage d'Asciidoc à Djot** ([PR #2242](https://github.com/nostr-protocol/nips/pull/2242)) : Le contenu wiki sur le kind `30818` utilise maintenant Djot comme format de balisage canonique. Le texte fusionné ajoute un comportement explicite de wikilinks, des exemples de demandes de fusion pour le kind `818`, des exemples de redirection pour le kind `30819` et des exemples de normalisation non latine pour les tags `d`. Cela donne aux implémenteurs une cible d'analyse plus propre qu'Asciidoc et supprime un chemin de spécification supplémentaire qui dépendait d'une chaîne d'outils centrée sur Ruby.

- **[NIP-19](/fr/topics/nip-19/) (Bech32-Encoded Entities) : Ajout d'une limite d'entrée** ([PR #2264](https://github.com/nostr-protocol/nips/pull/2264)) : La spécification recommande maintenant de plafonner les chaînes d'entités encodées Bech32 à 5 000 caractères. C'est un petit changement avec une vraie valeur pour les parseurs, car les chaînes NIP-19 apparaissent maintenant dans les flux QR, les liens profonds, les feuilles de partage et les entrées collées par les utilisateurs dans de nombreux clients.

**PRs ouvertes et discussions :**

- **Fichier de clé Nostr pour [NIP-49](/fr/topics/nip-49/) (Private Key Encryption)** ([PR #2269](https://github.com/nostr-protocol/nips/pull/2269)) : Propose un format de fichier `.nostrkey` pour l'export et l'import de clés chiffrées par mot de passe. S'il est fusionné, cela donnerait aux clients un chemin de sauvegarde basé sur des fichiers plus normal que la copie de chaînes `ncryptsec` brutes.

- **Cohérence de l'état d'appartenance pour [NIP-43](/fr/topics/nip-43/) (Relay Access Metadata and Requests)** ([PR #2267](https://github.com/nostr-protocol/nips/pull/2267)) : Ajoute une section clarifiant que les relays devraient maintenir un état d'appartenance autoritaire unique par pubkey. Cela simplifierait la logique des clients de groupe autour des changements d'appartenance et de l'historique rejoué.

- **Conseils de suppression pour [NIP-17](/fr/topics/nip-17/) (Private Direct Messages)** ([PR #2260](https://github.com/nostr-protocol/nips/pull/2260)) : Propose un chemin concret pour l'édition et la suppression de messages privés via des événements de suppression encapsulés en gift wrap. Le travail est encore ouvert, mais les auteurs de clients ont besoin d'une réponse ici si NIP-17 doit remplacer complètement les anciens flux de DM.

- **URI d'intention de partage pour [NIP-222](/fr/topics/nip-222/)** ([PR #2266](https://github.com/nostr-protocol/nips/pull/2266)) : Le brouillon standardiserait la manière dont les applications mobiles et desktop transmettent du contenu partagé à un client Nostr. C'est l'un des bords d'interopérabilité les plus rugueux dans les flux actuels d'application à application.

## NIP Deep Dive : NIP-94 (File Metadata)

[NIP-94](/fr/topics/nip-94/) définit le kind `1063` comme un événement de métadonnées de première classe pour un fichier. La [spécification](https://github.com/nostr-protocol/nips/blob/master/94.md) donne à l'événement son propre `content` lisible par l'humain plus des tags lisibles par machine pour l'URL de téléchargement, le type MIME, les hachages, les dimensions, les aperçus, les replis et les indications de service de stockage. C'est important car le fichier devient interrogeable sur les relays comme son propre objet. Un client n'a pas besoin d'extraire les métadonnées du contenu environnant pour comprendre ce qu'est le fichier.

```json
{
  "id": "6a92ef8d7c3a1b5d4e8f9a0b1c2d3e4f567890abcdef1234567890abcdef1234",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1742342400,
  "kind": 1063,
  "tags": [
    ["url", "https://downloads.example.org/notedeck/v0.8.0-rc2/notedeck-macos-universal.tar.gz"],
    ["m", "application/gzip"],
    ["x", "4a5b6c7d8e9f00112233445566778899aabbccddeeff00112233445566778899"],
    ["ox", "4a5b6c7d8e9f00112233445566778899aabbccddeeff00112233445566778899"],
    ["size", "48392011"],
    ["dim", "0x0"],
    ["magnet", "magnet:?xt=urn:btih:00112233445566778899aabbccddeeff00112233"],
    ["i", "00112233445566778899aabbccddeeff00112233"],
    ["blurhash", "LEHV6nWB2yk8pyo0adR*.7kCMdnj"],
    ["thumb", "https://downloads.example.org/notedeck/v0.8.0-rc2/thumb.png", "bbccddeeff00112233445566778899aabbccddeeff0011223344556677889900"],
    ["image", "https://downloads.example.org/notedeck/v0.8.0-rc2/screenshot.png", "ccddeeff00112233445566778899aabbccddeeff001122334455667788990011"],
    ["summary", "Signed macOS release artifact for Notedeck v0.8.0-rc2"],
    ["alt", "Notedeck desktop release archive"],
    ["fallback", "https://mirror.example.net/notedeck/v0.8.0-rc2/notedeck-macos-universal.tar.gz"],
    ["service", "nip96"]
  ],
  "content": "Notedeck macOS universal build",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

Les tags font plus de travail qu'il n'y paraît au premier abord. `x` identifie le fichier servi, tandis que `ox` identifie le fichier original avant toute transformation côté serveur. Les tags d'aperçu permettent aux clients de construire des index de fichiers navigables sans télécharger l'asset complet, et `summary` peut porter un court extrait à côté. `fallback` fournit une seconde source quand l'URL principale échoue, et `service` indique le protocole de stockage derrière le fichier, comme [NIP-96](/fr/topics/nip-96/) ou un autre hôte. NIP-94 se situe donc en dessous de la publication sociale et au-dessus du stockage brut. Il décrit le fichier, pas la conversation autour du fichier.

C'est pourquoi l'updater de Notedeck de cette semaine est intéressant. [PR #1326](https://github.com/damus-io/notedeck/pull/1326) utilise des événements signés de kind `1063` pour la découverte de versions logicielles, puis vérifie le binaire téléchargé par rapport au SHA256 publié. La même forme d'événement peut décrire un artefact logiciel ou un téléversement de média. NIP-94 est assez ancien pour être stable, mais il a encore de la marge pour croître car de plus en plus de projets traitent les événements de métadonnées comme un transport pour les machines, pas seulement comme une décoration pour les personnes.

## NIP Deep Dive : NIP-54 (Wiki)

[NIP-54](/fr/topics/nip-54/) définit le kind `30818` comme un événement d'article wiki. La [spécification](https://github.com/nostr-protocol/nips/blob/master/54.md) traite le tag `d` comme le sujet normalisé de l'article et permet à plusieurs auteurs de publier des entrées pour le même sujet. Le corps de l'article vit dans `content`, tandis que les tags gèrent l'identité normalisée, le titre d'affichage, les résumés et les références aux versions précédentes. Cela signifie que NIP-54 n'est pas seulement un format de contenu. C'est aussi un problème de récupération et de classement, car chaque client doit encore décider quelle version d'article afficher.

```json
{
  "id": "8c94e5d1f2a300112233445566778899aabbccddeeff00112233445566778899",
  "pubkey": "00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff",
  "created_at": 1742342400,
  "kind": 30818,
  "tags": [
    ["d", "nostr-wiki"],
    ["title", "Nostr Wiki"],
    ["summary", "Djot-formatted reference article about Nostr wiki events"],
    ["a", "30818:11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff:nostr-wiki", "wss://relay.example.org", "fork"],
    ["e", "11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff", "wss://relay.example.org", "fork"]
  ],
  "content": "Nostr is a [protocol][] for carrying events across relays.\n\n[protocol]: nostr:nevent1example",
  "sig": "33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889900112233cc44dd55ee66ff77889900aabbccddeeff00112233445566778899001122"
}
```

La fusion de cette semaine change le balisage canonique d'Asciidoc à Djot dans [PR #2242](https://github.com/nostr-protocol/nips/pull/2242). C'est important pour les implémenteurs car Djot a une spécification autonome plus resserrée et une histoire de parseur plus simple à travers les langages. Le texte fusionné clarifie aussi comment les wikilinks de style référence se résolvent, comment les demandes de fusion utilisent le kind `818`, comment les redirections utilisent le kind `30819`, et comment la normalisation des tags `d` devrait se comporter pour les écritures non latines. Ce sont les parties qui font que deux clients indépendants s'accordent sur quel article un lien pointe.

NIP-54 se situe aussi dans un endroit inhabituel du protocole. Un client wiki a besoin du rendu de contenu, mais il a aussi besoin d'une politique de classement. Les réactions, les listes de relays, les listes de contacts et les signaux de déférence explicites alimentent tous la décision de quel article gagne pour un sujet donné. Le passage à Djot ne résout pas ce problème de classement, mais il supprime l'une des ambiguïtés de parseur qui se trouvaient en dessous. C'est pourquoi la fusion compte maintenant : le changement concerne moins un formatage de prose plus agréable et davantage la facilitation d'une implémentation cohérente du comportement wiki multi-client.

Vous construisez quelque chose, ou vous voulez qu'on en parle ? Contactez-nous via [NIP-17](/fr/topics/nip-17/) DM sur Nostr à `npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923`.
