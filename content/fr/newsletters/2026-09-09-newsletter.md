---
title: "Nostr Compass #39"
date: 2026-09-09
publishDate: 2026-09-09
translationOf: /en/newsletters/2026-09-09-newsletter.md
translationDate: 2026-09-11
draft: false
type: newsletters
description: "Nostr Compass #39 suit les flux git signés, la publication depuis le navigateur, les diffusions en direct auto-hébergées, le consentement des relais communautaires, les événements privés, les versions ciblées et le contrat de liens NIP-21/NIP-27."
---

Bienvenue dans [Nostr Compass](https://nostrcompass.org), votre guide hebdomadaire de Nostr.

**Cette semaine :** [ngit et GitWorkshop](https://ngit.dev/v3) font passer les flux git signés sur Nostr et [Blossom](/fr/topics/blossom/), [nsite-clay](https://github.com/jooray/nsite-clay) rend la publication depuis le navigateur récupérable, et [Wingman App](https://github.com/OtherStuffAI/wm-app) réunit navigation, signature locale, authentification et fichiers. [Shosho et Livelier](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.1.0) connectent les flux auto-hébergés à Nostr, [Communitator](https://github.com/dyne/communitator) rend les modèles de relais inspectables avant signature, [cal.emre.xyz](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743) publie des créneaux de rendez-vous, et [Plektos](https://github.com/derekross/plektos/pull/16) chiffre les événements privés. Des versions étiquetées ajoutent un travail de récupération et de confidentialité dans [Vector](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4), [Primal Android](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.27), [LibreNostr](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) et [SkateSpots](https://zapstore.dev/apps/org.skatespots.app). Le travail de développement couvre le rendu [NIP-27](/fr/topics/nip-27/), les préférences de relais signées dans [Conduit](https://github.com/Conduit-BTC/conduit-mono/pull/397), les cibles de paiement [NIP-A3](/fr/topics/nip-a3/) et les miroirs Blossom. Des modifications fusionnées dans le [dépôt NIPs](https://github.com/nostr-protocol/nips) clarifient les abonnements réservés au direct et les données d'application authentifiées. Notre analyse approfondie explique comment les liens [NIP-21](/fr/topics/nip-21/) et les références NIP-27 transportent les profils et événements Nostr entre les applications.

## À la une

### Les flux git signés font passer l'intégration continue, les dépôts privés et les versions sur Nostr

Le [lancement v3 du 8 septembre](https://ngit.dev/v3) réunit ngit, GitWorkshop, ngit-grasp et ngit-ci dans un flux signé unique. [ngit](https://ngit.dev/ngit.git) transporte branches, correctifs et demandes de fusion sous forme d'événements [NIP-34](/fr/topics/nip-34/), tandis que [GitWorkshop](https://ngit.dev/gitworkshop.git) fournit l'interface de révision. Le lancement ajoute ngit-ci 0.1, un service d'intégration continue auto-hébergé dont les instructions et les résultats circulent sous forme d'événements Nostr signés, de sorte que les vérifications peuvent s'exécuter sur du matériel contrôlé par les mainteneurs, parallèlement à la révision du code.

La même version offre à [ngit-grasp v3](https://ngit.dev/ngit-grasp.git) des dépôts privés grâce à l'extension de dépôts privés GRASP-08 et rend explicite l'autorité des mainteneurs. Les enregistrements de version signés peuvent pointer vers des ressources dans [Blossom](/fr/topics/blossom/), gardant les métadonnées de version et les fichiers adressés par contenu en dehors d'une forge hébergée. Le [nouveau site de documentation](https://ngit.dev/v3) rassemble le client, les dépôts privés, l'intégration continue et les composants web.

### nsite-clay rend la publication depuis le navigateur récupérable

Une [correction des invites du signataire du 31 août](https://github.com/jooray/nsite-clay/commit/064a0c5350f1e2b107f7d8f1de00ad75ef2e69d8), la [récupération de publication](https://github.com/jooray/nsite-clay/commit/d1ad514f8068eec2e007059dc62a5b6f1d240ae0) et des [contrôles d'édition du 2 septembre](https://github.com/jooray/nsite-clay/commit/8f9d7d140dd3cd3e1db8726781fcd852041713f7) font de [nsite-clay](https://github.com/jooray/nsite-clay) un outil de publication dans le navigateur pour un site d'une seule page. L'utilisateur modifie le modèle objet du document sur place, sérialise le résultat, le téléverse sous forme de blob [Blossom](/fr/topics/blossom/) adressé par contenu, puis republie le manifeste [NIP-5A](/fr/topics/nip-5a/) du site. Aucune compilation locale ni serveur n'est requis.

L'[outil de publication dans le navigateur](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/deploy.html) rend désormais une publication échouée récupérable et réduit les invites répétées du signataire, tandis que le [guide d'édition](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/guide.html) documente la boucle. Le résultat reste un site NIP-5A ordinaire pour les passerelles existantes.

### Wingman App réunit navigation, signature et fichiers

Le travail de septembre ajoute des [sélecteurs de fichiers](https://github.com/OtherStuffAI/wm-app/commit/b0c9c03d317573adeafa92b1a56d696ad399e3ec), la [publication de profil](https://github.com/OtherStuffAI/wm-app/commit/f2343add8493625d62a1eb7fb76002ceab73f704), un [signataire sûr et la restauration de session](https://github.com/OtherStuffAI/wm-app/commit/4e278d96eb9258b89dc8b9639eac7bde3ac475c6) et des [compilations mobiles testées](https://github.com/OtherStuffAI/wm-app/commit/60456ec0a8b4ed26ecde53812a61f95dc0bd22ac) à [Wingman App](https://github.com/OtherStuffAI/wm-app). Son enveloppe Flutter injecte un fournisseur [NIP-07](/fr/topics/nip-07/) dans les pages ouvertes au sein de l'application, tandis que Flight Deck et Drive, adossé à Tower, fournissent une surface de travail et un espace de fichiers à côté du navigateur.

Wingman signe les requêtes HTTP authentifiées à l'aide de [NIP-98](/fr/topics/nip-98/). L'[implémentation des requêtes](https://github.com/OtherStuffAI/wm-app/blob/67ed27d216e528da5bb431322bd10ac15553796f/crates/wmapp-core/src/auth/nip98.rs) construit l'événement qu'un serveur vérifie avant de répondre, offrant à une identité installée un chemin d'approbation cohérent pour les actions sur les relais, la signature dans les applications web et les fichiers.

### Shosho prend en charge les flux auto-hébergés de Livelier

[Shosho 1.1.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.1.0) est sorti le 1er septembre avec la prise en charge de [Livelier](https://github.com/r0d8lsh0p/livelier), dont la [mise à jour d'attribution du 31 août](https://github.com/r0d8lsh0p/livelier/commit/7d8abb875770289502b55c3d947987db08e206dc) identifie le pont et la source Owncast dans les profils pontés. Livelier surveille le répertoire public d'Owncast, vérifie si un flux vidéo est en direct, puis publie un événement adressable `kind:30311` [NIP-53](/fr/topics/nip-53/). La découverte transite par Nostr tandis que la vidéo reste sur le serveur du diffuseur.

Le chat traverse le pont sous forme d'événements `kind:1311`. La [conception du pont](https://github.com/r0d8lsh0p/livelier) n'ouvre une connexion côté source que lorsqu'un lecteur Nostr y est abonné, étiquette les identités dérivées et envoie le chat éphémère vers un relais qui le supprime au bout de trois heures. Le relais de découverte n'accepte les écritures d'événements en direct que depuis la clé du pont ; le relais de chat utilise l'[authentification NIP-42](/fr/topics/nip-42/) et les [indicateurs d'événements protégés NIP-70](/fr/topics/nip-70/).

### Communitator rend les modèles de relais inspectables avant signature

La [série de lancements du 31 août](https://github.com/dyne/communitator/commit/520edd33a253ca3249993172fd1003c80bfd9b7c) offre à [Communitator](https://github.com/dyne/communitator) des modèles canoniques pour les listes de relais de kind `10002`, les serveurs Blossom de kind `10063` et les boîtes de réception de messages privés de kind `10050`. Avant qu'un signataire ne se connecte, l'application affiche les points de terminaison normalisés, les permissions de lecture et d'écriture, les kinds d'événements, les relais de publication fixes et les destinations.

Le [flux de signature et de publication borné](https://github.com/dyne/communitator/commit/2bd04c8fab292e73fe9a4ada250c64358aee8501) sépare la connexion de l'application. Chaque événement est signé séparément, une exécution utilise au plus quatre connexions WebSocket, et une destination n'est comptabilisée qu'après un `OK` positif [NIP-01](/fr/topics/nip-01/). Les résultats distinguent les livraisons complètes, partielles, échouées et annulées. Les modèles partagés restent des recommandations non fiables ; la [surface de consentement](https://github.com/dyne/communitator#security-and-consent) explique l'observabilité des relais et du réseau.

### cal.emre.xyz publie les disponibilités de rendez-vous via NIP-52

Le dépôt public a été ouvert dans un [commit initial du 2 septembre](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743), suivi d'une [annonce signée du gestionnaire le 3 septembre](https://njump.me/6fead386f0f401c2d8641ef842ccc2ade5abb4e45d61bfd7f3872b43db04cdac) pour [cal.emre.xyz](https://cal.emre.xyz). Un hôte publie ses disponibilités sous forme d'événement `kind:31923` [NIP-52](/fr/topics/nip-52/) ; un invité publie un RSVP `kind:31925`.

Il lit les événements des hôtes et les RSVP d'occupation acceptés depuis les relais, exclut les plages horaires qui se chevauchent et conserve les événements Nostr comme registre de planification sans les copier dans une base de données distincte. Les hôtes peuvent signer avec [NIP-07](/fr/topics/nip-07/), [NIP-46](/fr/topics/nip-46/) ou une clé locale ; les invités peuvent générer une clé séparée. Son [dépôt](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743) expose également le `naddr` résultant et les liens de calendrier, l'email étant désactivé par défaut.

### Plektos fait des événements privés un canal chiffré unique

L'[implémentation des événements privés du 2 septembre](https://github.com/derekross/plektos/pull/12) fait de chaque rassemblement [Plektos](https://github.com/derekross/plektos) un canal privé au sein d'une communauté chiffrée [Concord](/fr/topics/concord-protocol/). La liste des invités, la liste des RSVP, le tableau d'inscription, le fil de discussion, les contributions, les images de couverture, les modifications et les suppressions sont chiffrés ensemble ; une invitation ne transporte que la clé de cet événement et aucun événement de calendrier en clair n'est publié.

L'[audit du cycle de vie du 6 septembre](https://github.com/derekross/plektos/pull/14) ancre l'identifiant de définition d'événement pour une recherche directe lorsque plus de 500 enveloppes existent, tout en conservant une solution de repli paginée. Les paquets d'invitation expirent 30 jours après la fin d'un événement et peuvent être désactivés, mais quelqu'un qui a déjà obtenu une clé de canal peut la conserver. Une [réparation de sécurité du parseur](https://github.com/derekross/plektos/pull/16) distincte fait échouer les identifiants [NIP-19](/fr/topics/nip-19/) type-length-value (TLV) malformés au lieu de piéger le parseur.

## Versions étiquetées

### Vector 0.4.4 rend la récupération de communauté chiffrée plus sûre

[Vector 0.4.4](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4) est sorti le 31 août avec des correctifs de récupération de communauté, de rotation des clés, de modération et de routage des réponses. La refondation ferme une communauté pillée au chemin d'invitation utilisé par les attaquants ; l'appartenance de remplacement supplante l'état local obsolète ; et un membre injoignable ne fige plus la liste des membres. Les rotations vides sont rejetées, les promotions préservent les membres en ligne, et les opérations refusent de s'exécuter lorsque les membres requis ne peuvent pas être joints.

La [version](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4) persiste également les suppressions et bannissements des modérateurs, rechiffre le livre d'or après un changement de mot de passe, lie les réponses de notification à leur conversation après un redémarrage, et n'utilise que des chemins multijoueurs vérifiés. Il s'agit de contrôles de récupération, et non d'une révocation des clés déjà obtenues.

### Primal Android 3.5.27 vérifie l'identité du signataire et du portefeuille

[Primal Android 3.5.27](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.27) est sorti le 3 septembre après la fusion, le 31 août, de la [vérification de l'identité du signataire](https://github.com/PrimalHQ/primal-android-app/pull/1108) et de l'[authentification des requêtes de portefeuille](https://github.com/PrimalHQ/primal-android-app/pull/1105). La signature locale rejette une requête dont l'identité ne correspond pas au compte détenu, et les requêtes [NIP-47](/fr/topics/nip-47/) entrantes sont authentifiées avant traitement. Le routage des sondages à zaps envoie également les votes à l'auteur du sondage lorsque celui-ci apparaît dans une réponse.

### GRAIN 0.8.0-rc2 corrige un chemin de type « acquitté mais non stocké »

[GRAIN 0.8.0-rc2](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc2) est sorti le 7 septembre après qu'une défaillance de stockage a permis l'émission d'un `OK` avant que son moteur d'écriture asynchrone de base de données LMDB ne remarque que la capacité de stockage était pleine. Le relais avertit désormais à 80 et 95 pour cent, refuse les nouveaux événements à 97 pour cent tout en laissant de la place pour les suppressions, et signale les défaillances d'écriture survenant après l'acceptation. La rétention parcourt les événements du plus ancien au plus récent, la fermeture gère les messages tardifs, et les filtres invalides n'écartent plus leurs homologues valides.

La [version](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc2) prend également en charge les annonces de moniteurs de kind `10166` et les rapports de relais de kind `30166`, expulse les rapports obsolètes, conserve les relais configurés comme solution de repli, et rapporte les limites en vigueur et l'authentification dans [NIP-11](/fr/topics/nip-11/) au lieu de zéros statiques.

### LibreNostr 0.5.0–0.5.2 fait échouer le routage Tor en mode sécurisé

[LibreNostr 0.5.0](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) est sorti le 7 septembre avec un mode Orbot qui fait passer les relais, les zaps, les téléversements, les médias, la lecture et les aperçus par un seul port SOCKS, ainsi qu'une réparation d'un plantage du panneau de zaps. Si Orbot ou le proxy est indisponible, les connexions s'arrêtent au lieu de fuiter vers une route directe. La [version 0.5.1](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.1) empêche les recherches [NIP-50](/fr/topics/nip-50/) lentes de retarder les résultats locaux ; la [0.5.2](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.2) remplace la mise en page récursive des fils de discussion et répare leur ordonnancement.

Le [comportement d'échec sécurisé](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) s'applique à chaque surface réseau répertoriée par la version, et un redémarrage est nécessaire car ces clients ont une longue durée de vie. Les versions correctives préservent ce choix tout en limitant les défaillances sans lien concernant la recherche, la profondeur de pile et la mise en page.

### SkateSpots ajoute un chemin de relais embarqué

La [version Zapstore signée du 8 septembre](https://zapstore.dev/apps/org.skatespots.app) ajoute un relais Citrine optionnel à SkateSpots. Les spots, les crews, les messages et les données cartographiques peuvent se charger localement ; les publications sont mises en file d'attente hors ligne ; et le téléphone conserve une copie locale. Les contenus de stash et de messages existants restent chiffrés de bout en bout. Les vérifications de paiement exigent les montants des factures et des reçus de zap émis par le fournisseur avant d'accorder l'accès ou de comptabiliser les contributions.

Le [relais local](https://zapstore.dev/apps/org.skatespots.app) est une option de stockage et de continuité, et non un remplacement de chaque relais distant. Il permet à un skateur de continuer à travailler pendant une période de déconnexion, puis de réconcilier plus tard l'activité signée, tandis que les changements de paiement empêchent un reçu auto-rédigé de devenir une preuve de règlement.

### Whistle 1.8.15 répare la récupération du cycle de vie des groupes chiffrés

[Whistle 1.8.15](https://github.com/sjmcnamara/whistle/releases/tag/v1.8.15) est sorti le 3 septembre après qu'une réparation du cycle de vie Android a empêché les détenteurs d'état au niveau des routes de détruire les abonnements aux relais et les mises à jour de localisation à l'échelle de l'application. Ses notes de version décrivent également un état de connexion rafraîchi après un verrouillage ou une mise en veille, ainsi qu'un arriéré de 501 événements récupéré dans le cas observé.

Le [bogue](https://github.com/sjmcnamara/whistle/releases/tag/v1.8.15) liait la propriété d'un service à longue durée de vie à un écran à courte durée de vie. Garder en vie l'instance à portée d'activité et vérifier le socket avant une lecture ponctuelle rend la navigation Android ordinaire et la suspension en arrière-plan moins susceptibles de ressembler à un groupe vide.

### TWENTY ONE Companion 1.12.0 sépare les DM chiffrés du chat historique

[TWENTY ONE Companion 1.12.0](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.12.0) est sorti le 5 septembre avec les DM emballés-cadeau de [NIP-17](/fr/topics/nip-17/). La boîte de réception chiffrée est séparée de l'ancien chat d'espaces, qui reste distinct car ces messages n'ont jamais été chiffrés et ne peuvent pas être migrés. Les PDF et les vidéos sont pris en charge sous réserve de la politique des relais, et les masquages personnels se synchronisent sans devenir des bannissements de modérateur.

La [séparation visible](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.12.0) fait partie du modèle de sécurité. Qualifier l'ancien historique de boîte de réception sécurisée dénaturerait sa provenance, tandis qu'une migration silencieuse suggérerait un chiffrement qui n'existait pas au moment de son écriture.

### ZapStore 1.1.2 valide les identifiants d'événements et la rotation des certificats

[ZapStore 1.1.2](https://github.com/zapstore/zapstore/releases/tag/1.1.2) est sorti le 4 septembre avec la validation des identifiants d'événements NIP-01 : le client recalcule l'id d'un événement entrant et rejette les non-concordances avant de l'utiliser. La version identifie également les paquets installés en dehors de ZapStore. Côté serveur, la [rétention des empreintes de certificats](https://github.com/zapstore/relay/pull/8) préserve les balises `apk_certificate_hash` répétées afin que la rotation des clés de signature Android puisse conserver une lignée approuvée.

La [vérification de l'identifiant d'événement](https://github.com/zapstore/zapstore/releases/tag/1.1.2) empêche un relais ou un cache de modifier les balises ou le contenu tout en conservant l'ancien id. L'indicateur de source d'installation fournit une provenance distincte lorsqu'un paquet Android portant le même identifiant d'application provient d'un autre canal.

### Amber 6.6.1 garde les réponses du signataire attribuables

[Amber 6.6.1](https://github.com/greenart7c3/Amber/releases/tag/v6.6.1) est sorti le 4 septembre après que l'analyse des permissions a été corrigée pour tolérer un `kind` optionnel manquant, et que les demandes de signature rejetées ont commencé à renvoyer leur identifiant de demande d'origine. Les applications appelantes peuvent associer un rejet à l'opération soumise. La version met également à jour les valeurs par défaut du signataire distant et ajoute un relais indexeur.

Ensemble, ces [corrections](https://github.com/greenart7c3/Amber/releases/tag/v6.6.1) préservent l'attribution dans les deux sens : un enregistrement de permission reste utilisable lorsqu'un champ optionnel est absent, et un refus reste lié à la demande qui l'a provoqué. Les changements de relais par défaut affectent la découverte, mais ils ne remplacent pas la décision d'autorisation locale du signataire.

## En développement

### Zap Cooking affiche les références NIP-27 avec indications de relais

[La fusion du 4 septembre](https://github.com/zapcooking/frontend/pull/665) permet à [Zap Cooking](https://github.com/zapcooking/frontend) d'afficher les références `nostr:npub` et `nostr:nprofile` dans les articles, les recettes, les aperçus de l'éditeur et les vues d'impression. Les identifiants invalides restent du texte, la résolution est non bloquante, et l'éditeur affiche un aperçu du Markdown qui sera signé. Lorsqu'une information de relais existe, un `npub` seul devient un `nprofile` avec les relais outbox et une balise `p` correspondante.

La même semaine a corrigé [les lectures du kind `30023` limitées à l'auteur](https://github.com/zapcooking/frontend/commit/6a379c680727bb49074a4ff85f070b404dba97a7), ajouté [des relais de recherche NIP-50 vérifiés](https://github.com/zapcooking/frontend/commit/1802e8d7e95ed482209d09e03c834c2d9adfc1ea) avec déduplication et protections contre les requêtes obsolètes, et réparé [les appels de portefeuille NIP-47](https://github.com/zapcooking/frontend/pull/705) après que des changements de dépendances ont cassé les soldes et l'historique.

### Conduit réconcilie les préférences signées de relais et Blossom

[Conduit](https://github.com/Conduit-BTC/conduit-mono) a fusionné [l'édition des préférences Blossom](https://github.com/Conduit-BTC/conduit-mono/pull/374) le 2 septembre et [la réconciliation des préférences signées](https://github.com/Conduit-BTC/conduit-mono/pull/397) le 7 septembre. Market et Merchant conservent la dernière liste de relais kind `10002` valide et la déclaration de boîte de réception kind `10050`, préservent une liste signée utilisable lorsqu'un événement plus récent est malformé, distinguent une liste explicitement vide d'une recherche indisponible, et ne remplacent pas les relais déclarés en échec par des valeurs par défaut codées en dur.

[L'éditeur de kind `10063`](https://github.com/Conduit-BTC/conduit-mono/pull/374) permet à un utilisateur de charger, réordonner, vérifier, signer en externe, publier et relire une liste ordonnée de serveurs multimédias HTTPS sans contacter ces serveurs ni insérer de valeur par défaut non déclarée.

### Les cibles de paiement NIP-A3 atteignent trois clients

Du 1er au 3 septembre, [Amethyst](https://github.com/vitorpamplona/amethyst/pull/4041), [Grimoire](https://github.com/purrgrammer/grimoire/commit/54052506f7a0da06dfc4cf7e969331ee61be7851) et [Pollerama](https://github.com/formstr-hq/nostr-polls/commit/5a015f1d17abecd036f3e10c88d493d23928fa98) ont implémenté les cibles de paiement NIP-A3 de kind `10133`. Amethyst propose une passation opt-in uniquement lorsqu'une cible compatible existe et ne la transforme pas en zap ; Grimoire utilise un registre fixe avant de construire les URI de portefeuille ; Pollerama valide les adresses Monero et récupère la liste de relais de l'auteur avant d'interroger les cibles. Chaque client a toujours besoin d'une méthode de paiement autorisée, d'une route de relais et d'un affichage exact.

### Ditto étend le repli Blossom et les intégrations en direct

[Ditto](https://github.com/soapbox-pub/ditto) a fusionné [un repli et une mise en miroir Blossom étendus](https://github.com/soapbox-pub/ditto/commit/1e35a0705c28f706eb40d1f99aedef3105cf6f07) le 6 septembre. Les avatars, badges, bannières, images de communauté, emoji personnalisés et icônes d'application essaient désormais les serveurs déclarés avec le même hachage de blob ; les téléversements miroirs utilisent un jeton d'autorisation BUD-11 standard. Un [changement du 4 septembre](https://github.com/soapbox-pub/ditto/commit/e2a29004a65122470179c83d6ded8336a5c10dfa) a ajouté des intégrations compactes de diffusions en direct `kind:30311`.

## Travaux sur le protocole et les spécifications

### Nostr Implementation Possibilities

[NIP-01](/fr/topics/nip-01/) clarifie désormais [le filtre `limit: 0`](https://github.com/nostr-protocol/nips/pull/2460), fusionné le 4 septembre. Un relais DOIT ne retourner aucun événement stocké, DOIT envoyer `EOSE` lorsque les requêtes initiales sont terminées, et DOIT maintenir l'abonnement actif pour les nouveaux événements correspondants. Les clients peuvent ouvrir un abonnement réservé au direct avec un seul champ de filtre tout en conservant l'historique local. La clarification consigne un comportement compatible entre plusieurs implémentations de relais et relais publics.

[NIP-78](/fr/topics/nip-78/) a gagné une [exigence d'authentification pour les données d'application](https://github.com/nostr-protocol/nips/pull/2458), fusionnée le 3 septembre. Les relais DEVRAIENT exiger une authentification [NIP-42](/fr/topics/nip-42/) pour les kinds `78` et `30078` et DEVRAIENT ne les servir qu'à l'auteur authentifié de l'événement. Il s'agit d'un DEVRAIT, et non d'une garantie de confidentialité : les clients ne peuvent pas considérer des relais arbitraires comme un stockage privé. La fusion décourage également les kinds de données d'application personnalisés comme format d'échange public générique.

[NIP-AC](/fr/topics/nip-ac/) a été ouvert le 4 septembre comme une [proposition de signalisation WebRTC](https://github.com/nostr-protocol/nips/pull/2461) explicitement ouverte. Il utilise des kinds éphémères provisoires pour le ping, les demandes de connexion, les offres, les réponses et les candidats ICE, adressés avec `p` et regroupés par une balise de session `e` ; le kind `30600` prend en charge la découverte. Les relais DEVRAIENT diffuser et ne DOIVENT PAS stocker ces événements de signalisation pendant que les pairs se connectent directement. Les numéros restent provisoires, les clients DEVRAIENT utiliser [les listes de relais NIP-65](/fr/topics/nip-65/), et les applications nécessitant la confidentialité DEVRAIENT chiffrer le contenu des offres, des réponses et des candidats avec [NIP-44](/fr/topics/nip-44/).

## Analyse approfondie d'un NIP : liens URI et références dans le texte des événements

Un identifiant Nostr a besoin d'une signification transportable avant qu'une autre application puisse l'ouvrir. [NIP-21](/fr/topics/nip-21/) place un identifiant [NIP-19](/fr/topics/nip-19/) après le schéma d'URI `nostr:`, offrant aux navigateurs, systèmes d'exploitation et applications une forme unique et distribuable. [NIP-27](/fr/topics/nip-27/) définit ce que ce même URI signifie à l'intérieur du `content` lisible d'un événement. NIP-21 franchit une frontière applicative ; NIP-27 conserve une référence de profil ou d'événement dans une prose signée. Aucun des deux ne crée un kind d'événement ni ne modifie les messages de relais ; les [deux spécifications](https://github.com/nostr-protocol/nips/tree/master) définissent uniquement le comportement de liaison et d'affichage.

### Routage des URI et sémantique de NIP-19

[La grammaire de NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) se compose de `nostr:` suivi d’une entité bech32 NIP-19. `nsec` est exclu, car il encode une clé privée. Il n’y a aucun composant d’autorité, de chemin ou de requête. Un lien conforme est donc `nostr:npub1...`, et non `nostr://npub1...`. Une plateforme ou un client peut s’enregistrer comme gestionnaire. La spécification ne choisit pas l’application installée et ne définit pas de solution de repli vers le Web.

Le préfixe indique au client ce qu’il doit décoder. `npub` contient une clé publique et `note` un identifiant d’événement. `nprofile` ajoute à un profil des indications facultatives de relais. `nevent` ajoute des relais, un auteur et un kind à un identifiant d’événement. Enfin, `naddr` contient l’auteur, le kind et l’identifiant `d` d’un événement adressable, avec des relais facultatifs. Ces formats utilisent les [champs type-longueur-valeur de NIP-19](https://github.com/nostr-protocol/nips/blob/master/19.md). Les indications facilitent la recherche, mais ne prouvent ni que le relais possède l’événement ni que l’auteur le contrôle. Pour chaque événement récupéré, il faut toujours recalculer l’identifiant et vérifier la signature.

Le format de profil donné dans la [spécification NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) est le suivant :

```
nostr:npub1sn0wdenkukak0d9dfczzeacvhkrgz92ak56egt7vdgzn8pv2wfqqhrjdv9
```

[NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) définit également des passerelles HTML : une page qui fournit un événement Nostr peut placer son `naddr` dans `<link rel="alternate">`, tandis qu’un profil peut placer un `nprofile` dans `<link rel="me">` ou `<link rel="author">`.

### Affichage selon NIP-27 et tags facultatifs

[NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) s’applique au contenu lisible des événements, comme les notes de kind `1` et les articles de kind `30023`. Un outil de rédaction peut afficher `@name`, mais publie `nostr:nprofile1...` dans la chaîne signée. Un lecteur analyse l’URI, décode son entité NIP-19, récupère la cible et peut afficher un nom, une carte, un aperçu ou un lien local. Si le décodage échoue, l’URI reste du texte ordinaire. Le contenu brut ne doit pas être réécrit : toute modification change la sérialisation NIP-01, l’identifiant et la signature.

Les références dans le contenu et les tags remplissent des fonctions liées, mais distinctes. [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) décrit les tags facultatifs `p` et `e`, ainsi que le tag `q` de [NIP-18](/fr/topics/nip-18/). Un client peut afficher une référence sans créer de notification ni de relation de fil de discussion. Pour permettre la découverte d’une citation, il convient d’écrire à la fois l’URI et un tag `q`. [L’implémentation de Zap Cooking du 4 septembre](https://github.com/zapcooking/frontend/pull/665) suit cette distinction en conservant l’URI tout en ajoutant des indications de relais et un tag `p` correspondant. L’ajout de `p` ou de `q` ne rend pas l’URI privée, et NIP-27 ne prévoit aucun mode de mention masquée.

L’[événement de kind `1` suivant](https://njump.me/note1e0my422kylehy2g4ax4d98vsthdvnvy702yq3f6eguedjr0256as200k6a) a été récupéré depuis `wss://nos.lol` et vérifié avant d’être inclus comme exemple concret de référence NIP-27. Son `content` contient un `naddr` correspondant à un événement adressable indépendant de sa version. Le décodage donne le kind `30402`, l’auteur `91036d...310a`, l’identifiant `d` du cahier d’exercices et une indication `wss://nos.lol/`. Les tags `q`, `p`, `t`, `zap` et `client` relèvent de choix applicatifs et ne sont pas exigés par NIP-27.
```json
{
  "id": "cbf64aa95627f3722915e9aad29d905ddac9b09e7a8808a7594732d90deaa6bb",
  "pubkey": "ed1b999da9a434039d22338c276ffd6e338d609b81e6b1c305a120a982df787d",
  "created_at": 1788953511,
  "kind": 1,
  "tags": [
    [
      "p",
      "91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a",
      "wss://multiplexer.huszonegy.world/"
    ],
    [
      "t",
      "archetype"
    ],
    [
      "q",
      "30402:91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a:Archetype-Workbook-Companion-Meet-your-King-Warrioir-Magician-Lover-today-oejbwe",
      "wss://nos.lol/"
    ],
    [
      "zap",
      "91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a",
      "wss://multiplexer.huszonegy.world/",
      "0.9"
    ],
    [
      "zap",
      "ed1b999da9a434039d22338c276ffd6e338d609b81e6b1c305a120a982df787d",
      "wss://relay.nostr.band/",
      "0.1"
    ],
    [
      "client",
      "Amethyst"
    ]
  ],
  "content": "You can check, read and use this Workbook already! You can also support and get it for few sats and support us in this project.\n\nI hope it'll help you in your Archetype Journey :)\n\n#archetype\n\nnostr:naddr1qpgyzunrdpjhg7tsv5k4wmmjdd3x7mmt94pk7mtsv9hxjmmw94xk2et594uk7atj949kjmn894tkzunjd9hkju3df4skw6trd9skut2vdamx2u3dw3hkgcte94hk26nzwajszrnhwden5te0dehhxtnvdakz7q3qjypkmmqcaetrcpld4m27la946cch2hrk7qr8xjehsu5j5h3uxy9qxpqqqpmvyqnrm7n",
  "sig": "aa9592e7c773271b9e9f980c8a7e17fda2ffd5a4483a1789e5dd4c4a83018ac576c5202b21b33b08770dcabe023f93998a41f1a0be4bf00e36cdde611d07915e"
}
```

### Confiance, comportement en cas d'échec et implémentations clientes

Un lecteur sûr repère un jeton `nostr:` complet, valide bech32, décode NIP-19, rejette `nsec`, ignore les types TLV inconnus et laisse inchangé tout texte mal formé ou trop volumineux. `npub` et `nprofile` conduisent à des requêtes de profils ; `note` et `nevent` identifient des événements immuables ; `naddr` sélectionne le dernier événement adressable valide pour son kind, son auteur et son tag `d`. Les indications de relais réduisent le champ de recherche, mais n'étendent pas la confiance. Selon les [règles de NIP-01 relatives aux événements](https://github.com/nostr-protocol/nips/blob/master/01.md), le client vérifie l'id d'un `nevent` récupéré et contrôle la signature de chaque candidat `naddr` avant d'appliquer les règles de remplacement des événements adressables.

L'affichage d'aperçus intégrés relève du choix du client et a un coût en matière de confidentialité et de ressources. Récupérer chaque référence révèle les centres d'intérêt du lecteur et peut provoquer une avalanche de requêtes. Les clients peuvent donc utiliser un cache, différer les récupérations jusqu'à ce que les références soient visibles, limiter les accès simultanés et exiger un clic pour les médias inconnus. Selon [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md), un aperçu doit rester distinct du texte signé par l'auteur actuel. Un échec doit apparaître comme du texte non résolu ou une carte indisponible, et non être silencieusement traité comme du contenu vérifié.

La confiance varie également selon le type d'identifiant. Un `nevent` désigne des octets immuables, de sorte qu'un client peut rejeter un événement récupéré dont l'id sérialisé diffère de l'id demandé. Un `naddr` désigne une coordonnée remplaçable. Le client doit donc vérifier chaque candidat et appliquer les règles relatives aux événements adressables avant de décider quelle version afficher. Une indication de relais est utile pour la première requête dans les deux cas, mais elle ne constitue pas une approbation du relais ni du contenu renvoyé. La [définition TLV de NIP-19](https://github.com/nostr-protocol/nips/blob/master/19.md) fournit les données nécessaires pour rendre ces vérifications explicites.

[NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) définit un lien portable qui peut être ouvert depuis l'extérieur de Nostr, tandis que NIP-27 rend ce même lien durable au sein d'un texte signé. Un client qui implémente uniquement NIP-21 peut ouvrir un URI collé, mais ne peut pas afficher les références intégrées. Une prise en charge complète de NIP-27 ajoute la détection, le décodage sécurisé, une politique de récupération, le rendu local et un choix explicite concernant les tags de notification et de citation. L'URI commun assure l'interopérabilité de ces différentes couches sans obliger les clients à les présenter de manière identique.[Damus](https://github.com/damus-io/damus) représente les références intégrées sous forme de mentions typées. Son [code de gestion des mentions](https://github.com/damus-io/damus/blob/2ef636aa07f6bd4f24b72fa998b7397dced56d2a/damus/Core/Nostr/Mentions.swift) associe `npub` et `nprofile` à des références de profils, `note` et `nevent` à des références d'événements, et `naddr` à des références d'adresses ; [NostrLink](https://github.com/damus-io/damus/blob/2ef636aa07f6bd4f24b72fa998b7397dced56d2a/damus/Core/Nostr/NostrLink.swift) les dirige vers la destination appropriée. [Primal Android](https://github.com/PrimalHQ/primal-android-app) [analyse le protocole et les formes collées](https://github.com/PrimalHQ/primal-android-app/blob/36939db97213e7f8eeefaa4adaf125d839fc662e/domain/nostr/src/commonMain/kotlin/net/primal/domain/nostr/utils/NostrUriUtils.kt), valide bech32 et extrait les indications de relais, puis [associe les références à des modèles de contenu de note](https://github.com/PrimalHQ/primal-android-app/blob/36939db97213e7f8eeefaa4adaf125d839fc662e/app/src/main/kotlin/net/primal/android/notes/feed/model/NoteNostrUriUi.kt). [Zap Cooking](https://github.com/zapcooking/frontend/pull/665) affiche les mêmes références dans les articles, les recettes, les aperçus de l'éditeur et les vues d'impression.

---

Envoyez un DM NIP-17 pour partager un projet ou une actualité par l'intermédiaire du [projet Nostr Compass](https://github.com/andotherstuff/nostr-compass).
