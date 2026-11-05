---
title: 'Nostr Compass #47'
date: 2026-11-04
publishDate: 2026-11-04
draft: false
type: newsletters
translationOf: /en/newsletters/2026-11-04-newsletter.md
translationDate: 2026-11-05
---

Cette semaine, [Amethyst](/fr/newsletters/2026-11-04-newsletter/#amethyst) a livré des napplets intégrées avec des correctifs issus d'une [revue de sécurité des intégrations](https://github.com/vitorpamplona/amethyst/pull/4710), [Napplets](/fr/newsletters/2026-11-04-newsletter/#napplets---web-packages) a lié l'identité des applets à des ports propres à chaque document, et les versions nightly de [mdk de Marmot](/fr/newsletters/2026-11-04-newsletter/#marmot-protocol-mdk) ont renforcé la messagerie de groupe. Par ailleurs, des relais, des portefeuilles, des bibliothèques de signature et de nouvelles applications ont évolué, en grande partie dans du code source fusionné qui n'a pas encore été publié.

## À la une {#top-stories}

### Amethyst {#amethyst}

Amethyst, le client Android, a publié la [v1.21.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.21.0), qui exécute les napplets directement dans les notes sur Android 11+ et sur ordinateur. Les correctifs issus d'une [revue de sécurité des intégrations](https://github.com/vitorpamplona/amethyst/pull/4710) ferment une voie par laquelle toute napplet disposant d'un accès aux relais pouvait lire les DM déchiffrés. Le déchiffrement exige désormais une autorisation distincte de l'utilisateur et `nostr.signEvent` requiert la permission du signataire, tandis que le moteur de rendu Chromium sur ordinateur reste hors bac à sable. Une [modification du chiffrement des pièces jointes par fichier](https://github.com/vitorpamplona/amethyst/pull/4701) attribue à chaque pièce jointe de message direct privé [NIP-17](/fr/topics/nip-17/) une nouvelle clé et un nouveau nonce AES-GCM, alors que les lots de plusieurs fichiers réutilisaient les deux. La description du risque en amont provient d'une analyse du code sans exploit reproduit, et les fichiers déjà envoyés ne sont pas corrigés.

### Protocole Marmot (mdk) {#marmot-protocol-mdk}

mdk, le kit de messagerie chiffrée de Marmot basé sur MLS pour Nostr, a publié des préversions nightly réservées aux tests, sans version stable dans cette branche. Dans la nightly du 2 novembre, [les nouveaux envois attendent derrière les envois plus anciens en file](https://github.com/marmot-protocol/mdk/pull/2849) au sein d'un groupe, ce qui maintient l'ordre des générations de chiffrement pour les membres qui rattrapent l'historique, sans toutefois garantir contre la perte de messages. Une [réparation des Welcome perdus](https://github.com/marmot-protocol/mdk/pull/2936), fusionnée et désactivée par défaut, suit la [règle de heartbeat de Marmot](https://github.com/marmot-protocol/marmot/pull/497) et renvoie le Welcome exact conservé dès que le heartbeat de la cible montre une activité au moins dix minutes après la dernière publication du porteur. La cadence des heartbeats ou le décalage d'horloge peuvent retarder la réparation d'une heure ou plus, et son achèvement n'a pas de limite supérieure. Les [commandes de liaison d'appareils](https://github.com/marmot-protocol/mdk/pull/2922) restent derrière la fonctionnalité dev-device-groups désactivée par défaut et sont désactivées en production.

### Napplets - Paquets web {#napplets---web-packages}

Napplets, les paquets web pour applets Nostr isolées dans un bac à sable, a publié [core 0.37.0](https://github.com/napplet/web/releases/tag/%40napplet/core%400.37.0), [nap 0.36.0](https://github.com/napplet/web/releases/tag/%40napplet/nap%400.36.0) et [shim 0.35.0](https://github.com/napplet/web/releases/tag/%40napplet/shim%400.35.0), qui [lient l'identité de l'applet à un MessagePort propre à chaque document](https://github.com/napplet/web/pull/302). L'identité vérifiée (dTag, artifactHash) est liée au port transmis dans le hello depuis l'iframe créée, et tout le trafic NAP passe par ce port. Un document chargé par navigation ne reçoit aucune autorisation. Les shells qui utilisent encore la messagerie Window doivent effectuer la mise à niveau, car il n'existe aucune voie de compatibilité. Du code source ultérieur [verrouille le cadre d'aperçu sur son document vérifié](https://github.com/napplet/web/pull/305) avec frame-src 'none'.

## Versions publiées {#tagged-releases}

### Marble {#marble}

Marble, un client bêta reposant sur la signature à seuil Cosign, peut lire les relais comme des fils dans la [0.12.23](https://github.com/sybenx/marble/releases/tag/v0.12.23). Un relais ouvert par son adresse affiche sa propre description puis ses publications, des plus récentes aux plus anciennes. Les relais favoris sont conservés dans une liste de kind 10012 et les groupes de relais dans des ensembles de kind 30002, les mêmes listes que celles qu'utilise Jumble. La version remanie aussi les réactions, avec un panneau de réactions récentes et les emoji personnalisés de l'utilisateur.

### Sidecar {#sidecar}

Sidecar, une extension de navigateur pour publier des notes et des surlignages web, peut supprimer la sauvegarde de son portefeuille sur les relais dans la [1.16.6](https://github.com/dmnyc/sidecar/releases/tag/v1.16.6). Après confirmation, elle remplace la copie chiffrée par une copie vide et demande aux relais de l'oublier, en laissant le portefeuille connecté en place. Rien ne garantit que les relais effacent la sauvegarde. Depuis la [v1.16.5](https://github.com/dmnyc/sidecar/releases/tag/v1.16.5), Sidecar supprime les métadonnées EXIF, XMP et IPTC des JPEG avant l'envoi, et sa [modification de la préparation des envois](https://github.com/dmnyc/sidecar/pull/572) bloque tout JPEG qui ne peut pas être nettoyé.

### Haps {#haps}

Haps publie et installe des paquets natifs sous des clés Nostr. [Haps 0.1.25](https://github.com/mmalmi/haps/releases/tag/v0.1.25) fournit des bundles macOS, Linux et Windows avec des assistants htree épinglés par somme de contrôle et un fichier SHA256SUMS couvrant toutes les archives. Le code source de la 0.1.24 [écrit des références Hashtree versionnées](https://github.com/mmalmi/haps/commit/3dd051cefe9e506886a7f036267950282a179ee8) selon le projet de spécification Hashtree. Haps 0.1.23 et les versions antérieures ne peuvent pas lire les nouveaux catalogues sans un catalogue de transition hérité, ou sans un installateur ou une compilation Cargo mis à niveau.

### Cosign {#cosign}

Cosign, la bibliothèque de signature à seuil derrière la bêta de Marble, livre un correctif partiel de l'adhésion dans la [0.12.9](https://github.com/sybenx/cosign/releases/tag/v0.12.9) : une adhésion via un invitant scanné exige désormais la contribution de cet invitant et des fragments provenant d'au moins deux expéditeurs distincts. Les adhésions de téléphone à téléphone restent non liées, si bien qu'un attaquant disposant de deux clés suffit toujours, et les parts de déchiffrement vides échappent encore à la vérification de preuve. Dans la [0.12.8](https://github.com/sybenx/cosign/releases/tag/v0.12.8), un serveur qui écrit la liste des membres peut encore choisir des points de part dont les secrets sont connus. Les téléphones ne reçoivent les correctifs que par une version de Marble.

### nostream {#nostream}

nostream, un relais TypeScript adossé à PostgreSQL, ajoute la [synchronisation sortante entre pairs](https://github.com/cameri/nostream/pull/1043) dans la [3.12.0](https://github.com/cameri/nostream/releases/tag/nostream%403.12.0). Le worker lit les portées d'information de relais [NIP-11](/fr/topics/nip-11/) de chaque pair, s'authentifie via l'authentification client [NIP-42](/fr/topics/nip-42/) et effectue la réconciliation via la synchronisation negentropy [NIP-77](/fr/topics/nip-77/), en vérifiant l'ID, la signature et la portée des événements récupérés. Les [limites propres à chaque pair](https://github.com/cameri/nostream/pull/1034) ne s'appliquent qu'après qu'un pair configuré a terminé l'AUTH. Une version du code source ne prouve pas qu'un relais l'a déployée.

### diVine {#divine}

diVine, un client de courtes vidéos en boucle, a publié la [version stable Android 1.0.27](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.27) avec des autocollants vidéo publics interactifs ; la disponibilité sur iOS et macOS n'est pas confirmée. Une [nouvelle requête sous la fenêtre](https://github.com/divinevideo/divine-mobile/pull/10711), fusionnée, ne s'exécute qu'une fois la restauration initiale de l'historique terminée, et lit les gift wraps, les DM chiffrés obsolètes [NIP-04](/fr/topics/nip-04/) et les suppressions par pages de 100 messages par relais. Elle parcourt chaque relais indépendamment, alors que la récupération d'historique existante partage un seul curseur et peut sauter l'historique plus ancien d'un relais plafonné. La couverture est bornée et ne récupère pas l'historique complet.

### Whistle {#whistle}

Whistle, une application mobile de partage de position et de discussion en groupe, a publié la [2.0.1](https://github.com/sjmcnamara/whistle/releases/tag/v2.0.1), sa première version publique sur le protocole Marmot v2. Les groupes existants ne peuvent pas être transférés : il faut donc recréer les groupes et chaque membre doit mettre à jour, tandis que les identités npub sont conservées. La fonction scanner pour rejoindre remplace les codes et liens d'invitation. Parmi les problèmes connus, les messages de discussion envoyés hors ligne peuvent arriver en retard ou ne jamais arriver, ce que la version attribue à MarmotKit ; le partage de position n'est pas affecté.

## En développement {#in-development}

### Quartz {#quartz}

Quartz, une bibliothèque Nostr Kotlin Multiplatform, a livré la [reprise des abonnements en direct après reconnexion](https://github.com/vitorpamplona/quartz/pull/82) dans la version 2.14.0. Chaque relais reprend à partir du created_at le plus récent déjà délivré, plafonné à l'horloge de l'appareil, et les filtres gift-wrap remontent deux jours supplémentaires pour couvrir l'antidatage. Les événements à horodatage plus ancien qu'un relais a stockés pendant une panne peuvent encore être manqués. Les [fenêtres negentropy tenant compte des comptages](https://github.com/vitorpamplona/quartz/pull/85), fusionnées mais non publiées, comparent un comptage d'événements [NIP-45](/fr/topics/nip-45/) facultatif au comptage local et considèrent les comptages des relais comme non fiables.

### Buzz {#buzz}

Buzz a fusionné une modification qui [valide les suppressions de kind 5 et 9005 dans une même transaction que la suppression logique de la cible](https://github.com/block/buzz/pull/8944), de sorte qu'un échec ne peut plus accepter une suppression tout en laissant la cible active. Les lignes incohérentes historiques ne sont pas réparées. Le profil mobile de [NIP-RS](/fr/topics/nip-rs/), un brouillon Buzz pour l'état de lecture multi-appareils, a été fusionné et [synchronise les frontières de lecture entre appareils](https://github.com/block/buzz/pull/8998). Sur les relais plus anciens dépourvus de read_state_snapshot, les lectures locales fonctionnent toujours et la synchronisation entre appareils s'arrête, sans solution de repli.

### Alby Hub {#alby-hub}

Alby Hub, un nœud Lightning en autogarde qui sert les applications Nostr Wallet Connect [NIP-47](/fr/topics/nip-47/), a fusionné un [correctif de migration de base de données](https://github.com/getAlby/hub/pull/2657) qui conserve le compteur d'identifiants de chaque table lors d'un db_migrate ou d'une migration Postgres. Auparavant, une nouvelle application pouvait réutiliser l'identifiant d'une application supprimée et hériter de ses transactions et de son solde isolé. Aucune version étiquetée ni aucun déploiement contenant le correctif n'a été identifié. Une [modification des notifications](https://github.com/getAlby/hub/pull/2677) distincte isole les échecs propres à chaque application, mais les notifications en échec sont toujours abandonnées sans nouvelle tentative.

### swift-nostr-client {#swift-nostr-client}

swift-nostr-client, une bibliothèque Nostr en Swift 6, a fusionné une modification incompatible qui [fait exécuter à RemoteSigner la poignée de main de connexion avant sa première commande](https://github.com/yysskk/swift-nostr/pull/287). Le nouveau paramètre connectsAutomatically vaut true par défaut, et si la poignée de main échoue, la commande n'est pas envoyée. Comme les secrets de signature à distance [NIP-46](/fr/topics/nip-46/) sont à usage unique, les applications qui reprennent une session bunker avec une paire de clés client enregistrée doivent le régler sur false, sinon la première commande présente le secret déjà consommé. Aucune version n'a été étiquetée.

## Nouveaux projets {#new-projects}

### Trikey {#trikey}

Trikey, un portefeuille pré-alpha non audité dont l'application mobile et le gardien communiquent par messages chiffrés via des relais Nostr, corrige le blocage de l'application à l'ouverture dans la [version 0.1.10-alpha](https://njump.me/nevent1qvzqqqr4dupzqpepqn8d9d5jc8r4qf6h7kd7ldpgrpqgdaw8wjwyrxztkjltnfy4qyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpk2jxzja4q4z8avcsc7jqenpuykke49p3z3halm0xtgmn3h6r6judumrxf). Les deux côtés conservent désormais un registre, persistant après redémarrage, des identifiants de wraps déjà lus et les ignorent avant toute vérification de signature ou tout déchiffrement. Les indications d'expiration sur les requêtes et les alertes ne garantissent pas la suppression par les relais, et les mesures de performance de l'éditeur ont été réalisées sur un ordinateur portable.

### Pacto {#pacto}

Pacto, une application de bureau d'organisation communautaire qui fait fonctionner d'anciens groupes Marmot aux côtés des messages privés NIP-17, a publié la [v0.7.5](https://github.com/covenant-gov/pacto-app/releases/tag/v0.7.5), non signée, qui permet de modifier les messages envoyés pendant une minute. Ses [correctifs de distribution des messages privés](https://github.com/covenant-gov/pacto-app/pull/425) font échouer immédiatement les envois lorsque le pool ne contient aucun relais de confiance et acheminent les indicateurs de saisie via des relais de confiance. Des pull requests ouvertes et non fusionnées ajouteraient des [événements d'escouade](https://github.com/covenant-gov/pacto-app/pull/488) et des [documents d'escouade chiffrés](https://github.com/covenant-gov/pacto-app/pull/490).

### Mialuna {#mialuna}

Mialuna, un client Nostr Flutter axé sur les médias, a publié une [annonce de la version 0.19.0](https://njump.me/nevent1qvzqqqr4dupzqeyvpafs936l8quz5nfvskjg9wf8e3sm9q52q72wxmrvc7tdap4xqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqk6ltj5kr6mtq8mkyz9rzqxkkrhq9hsjz675e05rwgltwgreddw3npkkez) qui ajoute des demandes de suppression pour les stories de l'utilisateur à leur expiration. Le [commit du journal des modifications](https://github.com/Lwb89dev/mialuna/commit/d0a38cb92dac724e6e7bac6ec8f94a31a378e886) consigne les demandes de suppression adressées aux relais et la suppression des médias Blossom : les comptes à clé locale l'exécutent automatiquement, tandis que les comptes Amber ou bunker attendent que l'utilisateur choisisse « Delete now ». L'APK et son comportement sur appareil n'ont pas été vérifiés de manière indépendante. Les demandes de suppression ne peuvent pas garantir que les relais ou les serveurs effacent les données.

### whereAreYou {#whereareyou}

whereAreYou, une application Android qui partage la position au sein de cercles rejoints par code QR ou lien d'invitation, chiffre les coordonnées avec AES-256-GCM et les envoie via des relais publics. Un [commit de signature par membre](https://github.com/Dzekdrix/whereAreYou/commit/82121d0f13b4d5256b2392383e74640afde3019e) empêche les détenteurs de la clé du cercle de publier en se faisant passer pour un autre membre, et chaque appareil doit être mis à jour. Pour la [sauvegarde d'identité en Base45](https://github.com/Dzekdrix/whereAreYou/commit/82e185967dd0115b93472b3d92a4d0393c8751bc), l'auteur avertit que quiconque photographie le code QR pourrait deviner son code à huit chiffres hors ligne, selon son estimation en quelques dizaines de minutes de calcul GPU ; aucun benchmark n'a été publié. La source ne comporte aucune validation de sécurité.

## Travaux sur le protocole et les spécifications {#protocol-and-spec-work}

### Buzz définit des routes d'identifiants d'agent autorisées par le propriétaire {#buzz-defines-owner-authorized-agent-credential-routes}

Buzz a fusionné [NIP-FA](/fr/topics/nip-fa/), un [brouillon d'identifiants d'agent autorisés par le propriétaire](https://github.com/block/buzz/pull/9015) qui définit des routes d'octroi, d'assertion et de révocation pour les agents autorisés via l'attestation de propriétaire [NIP-OA](/fr/topics/nip-oa/). Un octroi provient d'un échange de jetons RFC 8693 associant la session du propriétaire à une preuve d'authentification HTTP [NIP-98](/fr/topics/nip-98/) de l'agent, et la révocation déconnecte l'agent et empêche sa clé de se réinscrire. NIP-FA est une spécification Buzz fusionnée uniquement dans le code source, sans prétention d'activation en production ni d'interopérabilité.

### Les signatures d'événements post-quantiques obtiennent des règles de validation exactes {#post-quantum-event-signatures-gain-exact-validation-rules}

La proposition ouverte de longue date sur les signatures post-quantiques a reçu des [règles de validation ML-DSA-44 exactes pour les événements Nostr](https://github.com/nostr-protocol/nips/commit/43104cbff30ae006e907d8ee0ec15c4949d0eef6). Les clés et les signatures ont des longueurs fixes, les vérificateurs contrôlent la signature sur les 32 octets bruts du condensé de l'ID d'événement avec un contexte vide, et aucun algorithme de repli n'est autorisé. L'identité proposée n'a pas d'encodage bech32 [NIP-19](/fr/topics/nip-19/), et les nouvelles signatures ne rendent pas résistants aux attaques post-quantiques les contenus chiffrés [NIP-44](/fr/topics/nip-44/) ni les gift wraps [NIP-59](/fr/topics/nip-59/).

### Une précondition signée proposée empêche la perte de remplacements d'événements {#a-proposed-signed-precondition-prevents-lost-event-replacements}

Une pull request ouverte de Buzz [propose une précondition signée NIP-CS propre au projet](https://github.com/block/buzz/pull/8835) pour les événements remplaçables et adressables ; il ne s'agit pas d'un NIP officiel. Le tag signé désigne l'ID de la tête actuelle ou `none`, et le relais le vérifie de manière atomique sous un verrou de coordonnée, rejetant une écriture obsolète par un OK à false ou un HTTP 409 et ne stockant rien. Les écritures sans tag fonctionnent comme auparavant, et le tag n'offre aucune garantie de compare-and-swap entre relais.

## Plongée dans les NIP : NIP-31 et NIP-73 {#nip-deep-dive-nip-31-and-nip-73}

Les clients rencontrent souvent des contenus qu'ils ne comprennent pas nativement. [NIP-31: Dealing with Unknown Event Kinds](/fr/topics/nip-31/) donne une étiquette lisible à un kind d'événement inconnu, et [NIP-73: External Content IDs](/fr/topics/nip-73/) nomme des sujets extérieurs à Nostr, comme des livres ou des pages web. Ces deux conventions sont des spécifications existantes et indépendantes ([texte de NIP-31](https://github.com/nostr-protocol/nips/blob/master/31.md), [texte de NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md)).

### NIP-31 est marqué comme non recommandé {#nip-31-is-marked-unrecommended}

Le [texte de NIP-31](https://github.com/nostr-protocol/nips/blob/master/31.md) actuel commence par un avertissement qui le marque `unrecommended` parce qu'il est « inutilement alourdi », et sa ligne de statut indique draft, unrecommended et optional. Des événements utilisant cette convention existent déjà sur les relais. Les mécanismes ci-dessous décrivent donc la façon dont les clients les lisent, sans recommandation pour de nouveaux protocoles.

### Ce que contient un tag alt {#what-an-alt-tag-carries}

Selon la [spécification](https://github.com/nostr-protocol/nips/blob/master/31.md), l'auteur d'un kind personnalisé qui n'est pas destiné à être lu comme du texte ajoute un tag `alt` contenant un court résumé en texte brut. On n'attend pas des clients centrés sur le kind 1 qu'ils demandent d'autres kinds, mais les utilisateurs peuvent tout de même faire référence à de tels événements depuis des notes, où un résumé apporte du contexte. Une étiquette ne permet ni de voter ni d'agir sur une requête de portefeuille. Pour une interaction plus riche, la spécification renvoie à [NIP-89: Recommended Application Handlers](/fr/topics/nip-89/).

Comme `alt` est un tag, l'identifiant d'événement et la signature définis par [NIP-01](/fr/topics/nip-01/): [Basic protocol flow description](https://github.com/nostr-protocol/nips/blob/master/01.md) le couvrent. Une signature valide authentifie un résumé contrôlé par l'auteur : elle montre que l'auteur a publié l'étiquette sans montrer qu'elle est exacte, et des résumés trompeurs sont donc possibles. Les tags sont publics : un `alt` placé sur un événement au contenu chiffré expose donc son résumé et peut révéler ce que le contenu dissimule. Ces propriétés découlent de l'enveloppe [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md), et non du texte normatif de NIP-31. Un tag `alt` de premier niveau est par ailleurs distinct du champ `alt` de description d'image situé dans `imeta`, et les moteurs de rendu les analysent séparément.

### Comment deux clients lisent alt {#how-two-clients-read-alt}

Dans la [carte d'événement inconnu de noStrudel au commit 7c68acf](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx), le premier tag `alt` est débarrassé de ses espaces de début et de fin et devient l'étiquette principale, accompagnée d'une ligne facultative `Using <client>`. Une valeur absente ou vide donne `Unknown event (kind ...)`, et jusqu'à trois lignes de contenu s'affichent indépendamment. Le même composant résout le tag `client` au moyen des modèles de gestionnaires NIP-89, en affichant Open lorsqu'une adresse partageable existe et `Open in <client>` lorsqu'un lien de gestionnaire valide est résolu. L'explication et l'ouverture dans une application sont des contrôles distincts.

Le fichier [UnknownEventDigest.kt d'Amethyst au commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt#L168-L170) privilégie le contenu qu'il classe comme de la prose et se rabat sur `alt`. Son analyseur supprime les espaces superflus des valeurs et retient le premier `alt` non vide, si bien qu'un événement dont le premier `alt` est vide peut recevoir ici une étiquette différente de celle de noStrudel. Ces deux descriptions reflètent le code source à ces commits, et non un comportement confirmé dans une version publiée.

### Exemple : un sondage avec une étiquette alt {#example-a-poll-with-an-alt-label}

Le sondage de kind 1068 ci-dessous a été récupéré depuis wss://relay.damus.io, et son identifiant comme sa signature BIP340 sont valides selon les règles de [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md). Un moteur de rendu générique peut afficher le texte `alt` bilingue, tandis qu'un client qui gère les sondages lit les tags `option` et `polltype`.

```json
{
  "kind": 1068,
  "id": "7d1df3922833b47645922de43c2edd83e928a0ad083cee592beeee2b262bb743",
  "pubkey": "5f6dc275f3f9f8752d010a110c226148a9ba3399c5b63a0f469ee93b1394a53e",
  "created_at": 1793626294,
  "tags": [
    [
      "option",
      "z25mgp",
      "Windows"
    ],
    [
      "option",
      "ncddq0",
      "macOS"
    ],
    [
      "option",
      "4wta6q",
      "Linux"
    ],
    [
      "option",
      "p9ykti",
      "UNIX or FreeBSD/NetBSD/OpenBSD"
    ],
    [
      "polltype",
      "singlechoice"
    ],
    [
      "alt",
      "Poll: Which one do you usually use?\n普段どれを使っていますか？"
    ],
    [
      "client",
      "Ditto",
      "31990:781a1527055f74c1f70230f10384609b34548f8ab6a0a6caa74025827f9fdae5:ditto"
    ]
  ],
  "content": "Which one do you usually use?\n普段どれを使っていますか？",
  "sig": "f1378a723c65e83bd3105b593f10767903bde993788cfaf625583466fca21f1ef2be945bb2ca526aa9e898c93d5f1677a2f5ceaf70cb3a59c99f97eb179658fa"
}
```

### Sujets et familles NIP-73 {#nip-73-subjects-and-families}

La [spécification NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md) (draft, optional, sans mention unrecommended) place un sujet externe dans un tag `i` et sa famille d'identifiants dans un tag `k`, ce qui permet aux clients d'interroger un sujet précis ou une famille entière. Un livre utilise `["i", "isbn:9780765382030"]` avec `["k", "isbn"]`, et une page web utilise son URL avec `k` défini à `web`. NIP-73 ne définit aucun kind d'événement : ce sont d'autres événements qui portent ces tags.

### Normalisation et indications d'URL {#normalization-and-url-hints}

La correspondance repose sur des chaînes identiques, et la [spécification](https://github.com/nostr-protocol/nips/blob/master/73.md) fixe donc une forme par famille : URL normalisées sans fragment, ISBN sans tirets, geohashes en minuscules, codes ISO 3166 en majuscules. Un troisième élément facultatif du tableau contient une indication d'URL destinée aux clients qui n'ont pas d'avis sur l'identifiant. L'auteur choisit cette indication, et elle ne fait pas partie de l'identité. Elle ne prouve pas non plus une quelconque propriété et ne désigne aucun site canonique.

### Ce qu'un identifiant partagé ne prouve pas {#what-a-shared-identifier-does-not-prove}

Selon [NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md), des identifiants égaux réunissent des conversations et n'établissent rien d'autre. Un commentaire signé identifie son auteur, mais il n'authentifie ni le livre, ni le site, ni l'éditeur du podcast, et ne montre pas qui les contrôle. Les alias, les ISBN propres à une édition et les URL qui se normalisent différemment peuvent scinder un même sujet en plusieurs fils. Le contexte compte : [NIP-22](/fr/topics/nip-22/): [Comment](https://github.com/nostr-protocol/nips/blob/master/22.md) utilise `I`/`K` en majuscules pour la portée racine et `i`/`k` en minuscules pour le parent, et [NIP-39: External Identities in Profiles](/fr/topics/nip-39/) utilise `i` pour les identités de profil. Tout tag `i` n'est donc pas un sujet NIP-73.

### NIP-73 dans le code d'analyse et de rendu {#nip-73-in-parser-and-renderer-code}

Le fichier [nip73.rs de rust-nostr au commit 4c8099a](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs) analyse les préfixes connus pour produire un `ExternalContentId` typé et convertit une indication facultative en URL typée, en n'émettant le troisième élément du tag que lorsqu'une indication existe. Ses tests conservent les ISBN avec tirets : l'analyseur retire le préfixe et stocke le reste sans appliquer la normalisation de la spécification, si bien qu'une analyse typée ne garantit pas des chaînes canoniques. Il sépare les identifiants de chaîne de la famille, en associant `ethereum:100:tx:<hash>` à `ethereum:tx`. Cette révision ne comporte aucune variante de pays `iso3166`.

Le fichier [DisplayExternalId.kt d'Amethyst au commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt) envoie les identifiants geohash et hashtag vers des affichages dédiés. Les identifiants d'URL disposent aussi d'un affichage dédié, tandis que les autres types pris en charge aboutissent à une puce de portée générique. Une URL ouvre la route de fil propre à l'application pour cette page. Lorsque les aperçus sont désactivés, le rendu normal affiche une simple puce de lien et ne demande aucun aperçu. Lorsqu'ils sont activés, la récupération d'un aperçu manquant peut contacter le site cible. Désactiver les aperçus évite cette requête lors du rendu normal. Aucun de ces fichiers n'établit le comportement d'une version publiée.

### Exemple : un commentaire sur une page web {#example-a-comment-on-a-webpage}

Ce commentaire de kind 1111, récupéré depuis wss://nos.lol, place la même URL publique d'un fil Reddit dans ses paires `I`/`K` et `i`/`k`, avec `web` comme famille selon [NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md) et NIP-73. Son identifiant et sa signature sont valides, ce qui identifie l'auteur du commentaire sans rien dire de la page liée.

```json
{
  "kind": 1111,
  "id": "e4229e38d93fad5d612ae21c401573bf8e87f0462dc2bd653804a252f98a238a",
  "pubkey": "ce5b8496c144a9dcd4990df6e265d9b60a21cde2515f3b206dc67b1c343790a9",
  "created_at": 1793590574,
  "tags": [
    [
      "I",
      "https://www.reddit.com/r/writinghelp/comments/1thd194/what_tools_and_systems_do_you_use_for_tracking"
    ],
    [
      "K",
      "web"
    ],
    [
      "i",
      "https://www.reddit.com/r/writinghelp/comments/1thd194/what_tools_and_systems_do_you_use_for_tracking"
    ],
    [
      "k",
      "web"
    ],
    [
      "client",
      "LayerTake"
    ],
    [
      "L",
      "layertake"
    ],
    [
      "l",
      "pin",
      "layertake"
    ],
    [
      "anchor",
      "{\"type\":\"text\",\"exact\":\"tools and systems\",\"prefix\":\"help • 6mo ago u/TheFarSea What \",\"suffix\":\" do you use for tracking and org\"}"
    ]
  ],
  "content": "Like this. I'm making this Public but could be just for me or friends/groups.",
  "sig": "a979389480d6ca919e4ab7b1ba92e532bf281be45c5df222e17d7d4ca62ef07d52c1004c0ce88620663dfac012b306154cfd73b858225764c701c40e3d9b7dfe"
}
```
