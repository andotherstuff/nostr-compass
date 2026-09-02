---
title: "Nostr Compass #38"
date: 2026-09-02
translationOf: /en/newsletters/2026-09-02-newsletter.md
translationDate: 2026-09-02
draft: false
type: newsletters
---

Bon retour sur [Nostr Compass](https://nostrcompass.org), votre guide hebdomadaire de Nostr.

**Cette semaine :** [Voca](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) 1.0 apporte des notes Nostr vérifiées et des abonnements aux contenus longs à un lecteur Android hors ligne qui lit les articles à voix haute, [nostream](https://github.com/cameri/nostream) étend le routage des tâches côté relay et le fonctionnement authentifié, [NDK for Dart](https://github.com/relaystr/ndk) corrige la negentropy et la durée de vie des requêtes multi-relay, [Divine Mobile](https://github.com/divinevideo/divine-mobile) rend déterministes la suppression et la signature des messages encapsulés, [Conduit Relay](https://github.com/Conduit-BTC/conduit-relay) protège par défaut les boîtes de réception de gift wraps, [Amethyst](https://github.com/vitorpamplona/amethyst) livre des passages surlignés portables et [Mostro](https://github.com/MostroP2P/mostro) vérifie les ordres signés avant son filtre antispam. [Napstr](https://github.com/lnbits/napstr) publie des catalogues audio et des signaux de présence de seeders sur Nostr tout en transférant les fichiers via Tor. Les sorties concernent [MDK](https://github.com/marmot-protocol/mdk) et [pakstr](https://git.nostrdev.com/stuff/pakstr) ; les travaux sur le protocole intègrent une indication de pagination [NIP-67](/fr/topics/nip-67/) et un schéma de tags pour les passages surlignés [NIP-84](/fr/topics/nip-84/) dans le [dépôt des NIPs](https://github.com/nostr-protocol/nips), tandis que [Nostr Wallet Connect](https://github.com/nostr-wallet-connect/nwc) ajoute le nombre total de transactions ; enfin, l'analyse approfondie des NIPs suit les reposts et les réactions à travers la forme de leurs events et leurs implémentations actuelles.

## À la une

### Voca 1.0 lit à voix haute les notes Nostr vérifiées et les abonnements sur Android

[Voca](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) est un lecteur Android hors ligne qui lit à voix haute des articles, des PDF, des fichiers Markdown et des notes Nostr avec la voix de synthèse vocale du téléphone, tout en maintenant la phrase prononcée en surbrillance sur la page. Sa [version 1.0](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en), [publiée le 2026-08-27](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) sous sa propre [clé de projet](https://njump.me/npub17h9fn2ny0lycg7kmvxmw6gqdnv2epya9h9excnjw9wvml87nyw8sqy3hpu), fait de Nostr une source à part entière : collez l'adresse d'une note, l'identifiant d'un event, un npub, un profil ou un lien web ordinaire contenant une entité Nostr, et l'application décode la référence, récupère l'event signé auprès des relays et lit le texte de l'auteur plutôt que la page web qui l'entoure.

Deux comportements vérifiés caractérisent l'intégration Nostr, tous deux décrits dans [l'annonce signée de Voca 1.0](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en). Premièrement, chaque event récupéré est contrôlé par rapport à son id recalculé et à sa signature Schnorr BIP-340 avant d'être conservé, en utilisant les relays d'amorçage, la liste de relays [NIP-65](/fr/topics/nip-65/) de l'auteur (un event kind `10002` signé et remplaçable dans lequel l'auteur répertorie les relays qu'il lit et auxquels il écrit) ainsi que les indications contenues dans la référence elle-même. Un relay peut donc refuser de répondre, mais pas faire dire à un auteur ce qu'il n'a pas dit. Deuxièmement, l'ajout du npub d'un auteur place ses articles longs [NIP-23](/fr/topics/nip-23/) (des publications adressables kind `30023` avec titres, résumés et images) dans une boîte de réception unique sur l'appareil, aux côtés des flux RSS et Atom. La mise à jour 1.1.0, [annoncée le 2026-08-28](https://gitworkshop.dev/npub17h9fn2ny0lycg7kmvxmw6gqdnv2epya9h9excnjw9wvml87nyw8sqy3hpu/voca) et publiée sur [Zapstore](https://zapstore.dev) le 2026-08-29, synchronise le défilement phrase par phrase, fluidifie les documents longs et rétablit le widget de l'écran d'accueil après un défilement manuel, un redimensionnement, un redémarrage du processus ou une mise à niveau.


### nostream étend le routage des DVM côté relay et le fonctionnement authentifié

Après les [travaux du 19 août sur l'ingestion des tâches](/fr/newsletters/2026-08-19-newsletter/#nostream-adds-a-relay-monitor-and-mints-invite-codes), [nostream](https://github.com/cameri/nostream), une implémentation de relay en TypeScript, [stocke et sert les events de gestionnaires d'applications NIP-89](https://github.com/cameri/nostream/pull/737). [NIP-89](/fr/topics/nip-89/) (découverte des gestionnaires d'applications) utilise des recommandations kind `31989` et des informations de gestionnaire kind `31990`, déjà situées dans la plage des events remplaçables paramétrés. Un client peut donc interroger ces kinds et recevoir un remplacement lorsque des tags `d` entrent en collision. Le relay ne publie pas d'informations de gestionnaire pour ses propres workers.

Les tâches [NIP-90](/fr/topics/nip-90/) (data vending machine) en attente [atteignent désormais un processus worker et reviennent sous forme d'events de résultat](https://github.com/cameri/nostream/pull/734). En cas de réussite, le relay signe avec sa propre clé un résultat d'un kind compris entre 6000 et 6999. Une expiration ou un plantage du worker marque la tâche comme échouée au lieu de la laisser soumise.

Les sessions authentifiées et les appels HTTP d'administration reposent sur des périmètres distincts. [NIP-42](/fr/topics/nip-42/) (authentification des clients auprès des relays) [suit la pubkey authentifiée pour chaque socket](https://github.com/cameri/nostream/pull/716), peut imposer AUTH avant que les clients publient des events et annonce cette exigence dans le document [NIP-11](/fr/topics/nip-11/) (informations du relay), ces deux contrôles étant désactivés par défaut. Séparément, [les routes de l'API d'administration peuvent accepter une autorisation HTTP signée selon NIP-98](https://github.com/cameri/nostream/pull/730). [NIP-98](/fr/topics/nip-98/) (authentification HTTP avec des events signés) reste désactivé jusqu'à ce qu'un opérateur l'active et indique les pubkeys autorisées.

### NDK for Dart corrige la negentropy, la durée de vie des requêtes multi-relay et la vérification des signatures

Une exécution de [NIP-77](/fr/topics/nip-77/) (réconciliation d'ensembles par negentropy) dans [NDK](https://github.com/relaystr/ndk), un kit de développement Dart pour Nostr, renvoyait les mauvais ensembles have et need sans signaler d'erreur, car le codec ne prenait pas en charge la version 1 du protocole [negentropy](/fr/topics/negentropy/). La [correction de l'encodage v1](https://github.com/relaystr/ndk/pull/722) renvoie désormais les ids détenus par le relay et ceux dont il a encore besoin.

Des filtres identiques envoyés à différents relays [étaient fusionnés en une seule requête](https://github.com/relaystr/ndk/pull/705). Les requêtes ayant le même filtre restent désormais distinctes lorsqu'elles ciblent des relays différents ou ont des durées de vie différentes. Une requête courte ne peut donc plus mêler au résultat les events d'un autre relay ni laisser une souscription active bloquée.

Le même kit [vérifie une signature une seule fois et conserve le résultat](https://github.com/relaystr/ndk/pull/726). La réception ultérieure d'un doublon ne déclenche plus une autre vérification et n'écrase plus l'event vérifié enregistré.

### Divine Mobile rend déterministes la suppression et la signature des messages directs encapsulés

Les events kind `5` de [NIP-09](/fr/topics/nip-09/) (demande de suppression d'event) encapsulés qui visaient un message n'étaient jamais appliqués dans [Divine Mobile](https://github.com/divinevideo/divine-mobile), un client mobile de vidéos courtes qui publie via Nostr. Le client [résout désormais chaque suppression par rapport au message désigné](https://github.com/divinevideo/divine-mobile/pull/8174), au lieu de considérer comme déjà traité tout élément qui n'est pas une réaction. Une seconde [demande de suppression pour tout le monde alors que la première était encore en cours](https://github.com/divinevideo/divine-mobile/pull/8164) disparaissait auparavant sans erreur et sans kind `5` sur le réseau ; les suppressions concurrentes sont désormais toutes publiées.

Après la version 1.0.22 déjà couverte, l'envoi à deux reprises en une seconde du même texte 1:1 [NIP-17](/fr/topics/nip-17/) (DM privés sous gift wrap) [produisait un seul id de rumor](https://github.com/divinevideo/divine-mobile/pull/8163), si bien que le second envoi disparaissait. Chaque envoi transporte désormais un jeton dans la rumor du [NIP-59](/fr/topics/nip-59/) (gift wrap), afin que les ids diffèrent.

Un appelant ayant déjà signé un event kind `4` ou kind `5` [conserve cette signature](https://github.com/divinevideo/divine-mobile/pull/8173), au lieu qu'un tag client soit ajouté ensuite, ce qui modifiait l'id et amenait les relays à rejeter l'event comme non valide.

### Conduit Relay renforce sa boîte de réception protégée par NIP-42

Les gift wraps kind `1059` sont stockés pour un seul destinataire. [Conduit Relay](https://github.com/Conduit-BTC/conduit-relay), un relay Go qui conserve ces wraps dans une boîte de réception protégée par destinataire, [utilise par défaut le mode enforce](https://github.com/Conduit-BTC/conduit-relay/pull/8) : une requête kind `1059` doit présenter une authentification [NIP-42](/fr/topics/nip-42/) en tant que destinataire, faute de quoi le relay la rejette. Les filtres mélangeant plusieurs kinds, les jokers, les comptages et la [negentropy](/fr/topics/negentropy/) appliqués à ces wraps sont `restricted`, afin qu'une autre AUTH ne puisse les transformer en export de la boîte de réception d'autrui.

Le même [merge de la boîte de réception protégée](https://github.com/Conduit-BTC/conduit-relay/pull/8) exige un id d'event canonique sur l'event AUTH transmis et accepte un event NIP-42 par ailleurs valide, que son `content` soit vide ou non. Le mode Challenge-only continue de proposer AUTH sans bloquer la lecture ; disabled autorise librement l'accès. Le mode enforce est utilisé par défaut dans la bibliothèque.

### Amethyst livre les passages surlignés NIP-84 et corrige deux défaillances liées aux relays

À la suite des [travaux de la semaine dernière sur l'autorisation Blossom](/fr/newsletters/2026-08-26-newsletter/#amethyst-moves-blossom-authorization-off-image-loading-threads), [Amethyst](https://github.com/vitorpamplona/amethyst), un client Nostr pour Android, livre la [v1.14.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.14.0) avec [NIP-84](/fr/topics/nip-84/) (passages surlignés portables). Un passage sélectionné devient un event kind `9802` depuis l'éditeur, un flux de passages surlignés ou un partage vers l'application.

La version ajoute des commandes de suppression et d'archivage des canaux [NIP-29](/fr/topics/nip-29/) ([PR #3812](https://github.com/vitorpamplona/amethyst/pull/3812)), mesure le comportement des relays au moyen du trafic que le client génère déjà, puis complète ces sondes [NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) par des contrôles de streaming, de lecture, d'écriture et d'URL ([PR #3836](https://github.com/vitorpamplona/amethyst/pull/3836), [PR #3857](https://github.com/vitorpamplona/amethyst/pull/3857)). Amethyst supprime aussi une vulnérabilité de collision de hachage dans SharedKeyCache et compare les codes d'authentification de message en temps constant ([PR #3833](https://github.com/vitorpamplona/amethyst/pull/3833)), corrige une course susceptible de perdre l'envoi d'AUTH à la connexion ([PR #3838](https://github.com/vitorpamplona/amethyst/pull/3838)), répartit le verrouillage de l'état des souscriptions pour mettre fin à un convoi d'ANR ([PR #3851](https://github.com/vitorpamplona/amethyst/pull/3851)) et compare tous les filtres de souscription au lieu du seul premier ([PR #3856](https://github.com/vitorpamplona/amethyst/pull/3856)).

[La Newsletter #36 avait déjà couvert ces changements d'authentification auprès des relays, de sauvegarde et de chat public](/fr/newsletters/2026-08-19-newsletter/#amethyst-rebuilds-its-relay-authentication-decision-flow) ; la v1.14.0 les livre maintenant ensemble. Les soft bans de Concord comblent des lacunes d'autorité relevées par un audit ([PR #3885](https://github.com/vitorpamplona/amethyst/pull/3885)). L'authentification auprès des relays dispose d'un parcours d'autorisation remanié ([PR #3899](https://github.com/vitorpamplona/amethyst/pull/3899)), attend la résolution du challenge au lieu d'expirer ([PR #3905](https://github.com/vitorpamplona/amethyst/pull/3905)), configure par défaut les nouveaux comptes pour qu'ils s'authentifient ([PR #3931](https://github.com/vitorpamplona/amethyst/pull/3931)), respecte cette préférence sur les relays hors de l'ensemble habituel du compte ([PR #3937](https://github.com/vitorpamplona/amethyst/pull/3937)) et conserve les autorisations de session lors des reconnexions ([PR #3955](https://github.com/vitorpamplona/amethyst/pull/3955)). Un parcours guidé au premier lancement et dans les réglages rend les sauvegardes de clés faciles à trouver ([PR #3909](https://github.com/vitorpamplona/amethyst/pull/3909)), le rattrapage des proofs Cashu et la pagination de l'historique empêchent la troncature des soldes du portefeuille ([PR #3941](https://github.com/vitorpamplona/amethyst/pull/3941)), et les chats publics peuvent désormais être mis en sourdine ([PR #3939](https://github.com/vitorpamplona/amethyst/pull/3939)).

Après ce tag, les [listes de confiance](https://github.com/vitorpamplona/amethyst/pull/3983) des kinds `30392` à `30395` sont indexées par [NIP-50](/fr/topics/nip-50/) (recherche plein texte) uniquement selon leur titre. Une liste nommée dans le texte peut ainsi être trouvée sans indexer les ids hexadécimaux de ses membres. Les refus de portefeuille reçus via [NIP-47](/fr/topics/nip-47/) (Nostr Wallet Connect) [affichent désormais leur erreur au lieu de donner l'impression que l'appui n'a rien fait](https://github.com/vitorpamplona/amethyst/pull/3987), notamment `QUOTA_EXCEEDED` et `RESTRICTED`, avec en plus une expiration lorsque le portefeuille ne répond jamais.

### Mostro valide les ordres signés avant les traitements coûteux et conserve les events d'audit des ordres

Après la [fondation de l'escrow Cashu dans la v0.18.1](/fr/newsletters/2026-08-12-newsletter/#mostro-0181-starts-a-cashu-escrow-path-and-hardens-the-daemon), [Mostro](https://github.com/MostroP2P/mostro), un daemon d'échange pair à pair qui coordonne les ordres via Nostr, a publié le tag [v0.18.5](https://github.com/MostroP2P/mostro/releases/tag/v0.18.5), qui utilise par défaut [NIP-44](/fr/topics/nip-44/) (chiffrement du payload) pour le transport et maintient le gift wrap comme option explicite.

La version ancre les expirations de l'état d'attente sur l'heure de prise enregistrée afin que la caution d'un maker ne soit pas confisquée selon la mauvaise horloge ([PR #879](https://github.com/MostroP2P/mostro/pull/879)), ne déclenche qu'une seule fois au maximum le paiement à l'acheteur pour chaque ordre réglé ([PR #881](https://github.com/MostroP2P/mostro/pull/881)) et fait passer ces paiements par des attentes `send_payment` bornées et non bloquantes ([PR #883](https://github.com/MostroP2P/mostro/pull/883)). Une tentative visant à payer le bénéficiaire de la confiscation après expiration ([PR #875](https://github.com/MostroP2P/mostro/pull/875)) a été annulée avant la publication du même tag ([PR #885](https://github.com/MostroP2P/mostro/pull/885)). Mostro cesse également de republier chaque heure et au démarrage un carnet d'ordres en attente inchangé ([PR #888](https://github.com/MostroP2P/mostro/pull/888)), et ses events de litige kind `38386` comportent désormais un tag `created_at` pour leur classement en aval ([PR #878](https://github.com/MostroP2P/mostro/pull/878)).

Après ce tag, une [vérification de signature s'exécute désormais avant le filtre antispam](https://github.com/MostroP2P/mostro/pull/892). L'id d'un event n'engage pas `sig` ; une copie du kind `14` d'une victime munie d'une signature invalide pouvait donc occuper l'emplacement de rejeu et faire disparaître silencieusement le message valide. Le daemon commence par vérifier et écarte un wrap invalide au lieu d'émettre un avertissement puis de poursuivre.

Les events d'audit des frais kind `8383` portaient une date d'expiration [NIP-40](/fr/topics/nip-40/) de 15 jours. Ils [conservent désormais une expiration d'un an](https://github.com/MostroP2P/mostro/pull/924), conformément à leur rôle de registre public des paiements. Sur un nœud compatible avec Cashu, la prise d'un ordre [demande au vendeur via Nostr de verrouiller un escrow 2 sur 3](https://github.com/MostroP2P/mostro/pull/830), publie l'event de l'ordre en attente et omet la création d'une facture Lightning hold. Cela achève le parcours de la requête ; ce changement ne résout pas à lui seul tous les cas de clôture d'escrow ou d'abus de la place de marché.

### Napstr publie des catalogues audio sur Nostr et transfère les fichiers via Tor

[Napstr](https://github.com/lnbits/napstr) est un client de partage audio pour ordinateur qui publie sur Nostr des catalogues consultables et la présence de seeders actifs, puis transfère les fichiers par l'intermédiaire d'un processus Tor intégré, sans solution de repli exposant directement l'adresse IP. La [version 0.2.0](https://github.com/lnbits/napstr/releases/tag/v0.2.0) maintient publics les profils et les métadonnées du catalogue, mais garde les requêtes, les identifiants de transfert, le contenu des fichiers et les adresses IP des pairs hors des relays.

La découverte utilise deux kinds d'events adressables définis dans le [dépôt Napstr](https://github.com/lnbits/napstr). Les entrées de catalogue kind `30421` désignent un fichier par son condensat SHA-256, son nom de base public, sa taille et son format audio ; un auteur retire un fichier en remplaçant cette coordonnée par un marqueur deleted. Les signaux de présence kind `30422` expirent au bout de dix minutes et répertorient les ids des fichiers que l'auteur est prêt à seeder. Une ligne du catalogue n'est donc active que tant qu'un signal non expiré contient encore ce condensat.

La conversation publique utilise [NIP-C7](/fr/topics/nip-c7/) (messages de chat kind 9) plutôt qu'un groupe appartenant à un relay. Le [dépôt Napstr](https://github.com/lnbits/napstr) définit un salon public commun ainsi qu'une discussion par morceau, identifiée par le condensat du fichier. Ces messages sont signés et publics. Ils ne contiennent ni adresses onion, ni identifiants de transfert, ni octets des fichiers.

Un téléchargement commence par une négociation en DM sous gift wrap selon [NIP-17](/fr/topics/nip-17/). Le [dépôt Napstr](https://github.com/lnbits/napstr) encapsule une demande, une offre ou un refus dans une rumor kind `14`, de sorte que les relays ne voient ni le nom d'hôte onion v3 temporaire ni la capacité à usage unique renvoyée par une offre acceptée. Tor intégré transfère ensuite les octets via cette adresse onion, vérifie le condensat SHA-256 complet et valide de nouveau le fichier audio avant qu'il puisse être lu.

La [comparaison de v0.1.7 à v0.2.0](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0) ajoute des collections de livres audio et Napstrfy, un compagnon Android facultatif. Les manifestes kind `30423` répertorient des chapitres ordonnés qui restent des fichiers ordinaires du catalogue ; un client qui ignore la collection peut donc toujours récupérer chaque chapitre. Napstr crée à cet effet un dossier local Audiobooks de manière non destructive. Napstrfy s'associe à une instance de bureau en fonctionnement grâce à un code QR à usage unique, puis recherche et demande des téléchargements par l'intermédiaire des services Nostr et Tor existants de cette instance, sans recevoir sa clé secrète.

La même [comparaison](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0) fait expirer une procédure d'association qui n'aboutit pas. Un seeder copie et hache le fichier partagé avant d'en servir les octets, écrit les données reçues dans un fichier temporaire privé, limite les destinations des livres audio à un véritable enfant du dossier Napstr et interrompt l'opération si cette destination change pendant le transfert.

## Sorties

### MDK v0.9.17 : KeyPackages les plus récents, activité des membres et envois durables

[La Newsletter #37 couvrait MDK 0.9.14 et 0.9.15](/fr/newsletters/2026-08-26-newsletter/#mdk-v0914-and-v0915-keypackage-selection-epoch-gap-recovery-and-split-relay-roles), notamment le passage, dans le [dépôt MDK](https://github.com/marmot-protocol/mdk), de la sélection du KeyPackage le plus ancien à celle du package valide le plus récent pour le profil actuel, les barrières de récupération des écarts d'epoch, le nettoyage des comptes et la séparation entre relays de découverte et relays opérationnels. Ces correctifs restent la base des deux versions suivantes : un package obsolète ne bloque donc plus un membre qui en a déjà publié un utilisable.

[Les events d'adhésion et d'administration font désormais avancer la liste des chats](https://github.com/marmot-protocol/mdk/pull/1551), comme le fait un nouveau message : le texte d'aperçu, l'ordre, le nombre d'éléments non lus et les marqueurs de lecture sont actualisés lorsque des personnes rejoignent ou quittent le groupe, ou changent de rôle, et l'acteur système local n'est pas traité comme un profil Nostr. Les reconnexions et les redémarrages [réutilisent une identité d'envoi unique lors d'une nouvelle tentative d'envoi durable d'un texte sortant](https://github.com/marmot-protocol/mdk/pull/1516), afin que le même message de groupe ne soit pas publié deux fois.

Les deux versions publiées depuis se concentrent sur le coût du maintien en bon état des grands groupes. La [version 0.9.16](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.16) [mesure la divergence d'epoch depuis l'epoch actuel plutôt que depuis un maximum historique](https://github.com/marmot-protocol/mdk/pull/1559), maintient accessibles les events entrants refusés ([PR #1565](https://github.com/marmot-protocol/mdk/pull/1565)), limite l'annulation d'un rejeu à l'état canonique du groupe ([PR #1563](https://github.com/marmot-protocol/mdk/pull/1563)) et introduit [marmot-c](https://github.com/marmot-protocol/mdk/pull/1545), une ABI C générée par macros au-dessus des bindings UniFFI qui permet aux hôtes d'intégrer directement le moteur. La [version 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.17) fusionne ensuite les parcours d'admission des passes en [un seul parcours des membres au lieu d'un par membre](https://github.com/marmot-protocol/mdk/pull/1617), [détermine si l'état d'un groupe est contesté sans initialiser le graphe complet de son historique](https://github.com/marmot-protocol/mdk/pull/1620), [réduit le coût d'interrogation à vide du balayage différé](https://github.com/marmot-protocol/mdk/pull/1621) et [applique la lecture par lots des composants aux trois sites de projection omis lors du premier passage](https://github.com/marmot-protocol/mdk/pull/1622). Les artefacts correspondants [marmot-c 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/marmotc-v0.9.17) et [WN Agent 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/wn-agent-v0.9.17) sont construits à partir du même commit, de sorte que les intégrateurs bénéficient ensemble de ces chemins de maintenance moins coûteux.


### pakstr v0.16.0 : identifiants kind-32267 lors de la publication

Après le [pipeline de publication Zapstore des versions 0.13.0 à 0.15.0 couvert la semaine dernière](/fr/newsletters/2026-08-26-newsletter/#pakstr-0130-through-0150-makes-zapstore-publication-explicit), [pakstr](https://git.nostrdev.com/stuff/pakstr), un CLI qui empaquette une application web en APK Android signé et la publie avec une clé Nostr, [journalise les ids des events d'application kind `32267`](https://git.nostrdev.com/stuff/pakstr/pulls/67) qu'il recherche, publie ou remplace. La [version 0.16.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0) affiche l'ancien et le nouvel id lorsqu'une republication est déclenchée par des métadonnées de fiche obsolètes, afin que l'éditeur puisse confirmer quel event de fiche est actif sur le relay.

Le même [journal des identifiants](https://git.nostrdev.com/stuff/pakstr/pulls/67) enregistre l'id trouvé pendant la recherche avant tout remplacement, puis l'id de l'event effectivement publié. Une réutilisation sans modification apparaît donc comme un id répété. Il s'agit du changement associé au tag [0.16.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0) ; les comportements Content-Digest, publication avant téléversement et validation de l'éditeur étaient déjà livrés dans les tags antérieurs.

## Changements non publiés

### Zap Cooking limite les relays du bunker et signe les endpoints payants

Le rechargement d'une session bunker sur [Zap Cooking](https://github.com/zapcooking/frontend), un site de recettes construit sur des events Nostr longs, publiait auparavant la conversation chiffrée [NIP-46](/fr/topics/nip-46/) (signature à distance via des relays) sur tous les relays déjà utilisés par la page. La [restriction du trafic du signataire aux propres relays du bunker](https://github.com/zapcooking/frontend/pull/633) s'applique désormais lors de la restauration d'une session et de l'association nostrconnect, le parcours de connexion initié par le signataire, conformément au parcours de connexion par URL de bunker. Elle refuse d'installer un ensemble de relays vide provenant d'un enregistrement stocké mal formé, afin que les relays qui n'hébergent que des recettes n'apprennent plus qu'une même pubkey maintient une session bunker active.

[L'authentification HTTP signée](https://github.com/zapcooking/frontend/pull/630) protège désormais le chat payant de l'assistant culinaire, l'introduction du livre de recettes et les mises à jour des recettes à accès restreint selon [NIP-98](/fr/topics/nip-98/) (authentification HTTP avec un event Nostr signé). Le serveur lit le corps de la requête une seule fois, vérifie la signature par rapport à ce payload exact et tire l'identité de l'event d'authentification vérifié plutôt que d'une clé publique fournie dans le corps. L'aperçu du chat fonctionne toujours sans en-tête, tandis qu'une signature présente mais invalide est rejetée et que l'introduction du livre de recettes exige toujours une signature. La mise à jour d'une recette à accès restreint impose aussi que la clé vérifiée corresponde à l'auteur enregistré ; toute autre personne apprend seulement que la recette n'existe pas, si bien que l'endpoint ne confirme pas quels enregistrements payants existent.

### nostrord répare les DM encapsulés et les liens d'events partagés

Après la [v2.9.0 de la semaine dernière](/fr/newsletters/2026-08-26-newsletter/#nostrord-v290-relay-scoped-group-state-and-media), [nostrord](https://github.com/nostrord/nostrord), un client multiplateforme pour les communautés hébergées par des relays, a intégré des correctifs de livraison afin qu'un DM sous gift wrap [NIP-17](/fr/topics/nip-17/) envoyé depuis un appareil atteigne le même compte ailleurs. [La publication indépendante de la copie destinée à l'expéditeur](https://github.com/nostrord/nostrord/pull/295) empêche que la première acceptation par un relay du wrap du destinataire fasse disparaître la copie récupérée par les autres appareils. Le même changement renvoie un wrap après l'achèvement de [NIP-42](/fr/topics/nip-42/) (authentification du client auprès des relays) et considère l'envoi comme réussi dès la première acceptation par un relay, afin qu'un hôte défaillant ne bloque pas les autres. [La nouvelle tentative périodique des gift wraps mis en attente](https://github.com/nostrord/nostrord/pull/297) dont le déchiffrement [NIP-59](/fr/topics/nip-59/) (gift wrap) a échoué se fait désormais selon un minuteur, afin qu'un bunker qui reste connecté ne laisse plus ces messages man... [truncated]

Une réponse [NIP-C7](/fr/topics/nip-c7/) (messages de chat kind `9`) répète son parent sous forme de pointeur `nevent` [NIP-19](/fr/topics/nip-19/) (entités encodées en bech32) au début du texte, à côté du tag `q`. [La suppression de ce pointeur initial vers le parent](https://github.com/nostrord/nostrord/pull/292), lorsqu'il ouvre le corps et désigne le parent de la réponse, permet d'afficher la ligne comme une citation de réponse unique ; un pointeur au milieu du corps ou constituant tout le corps reste affiché comme une carte de citation. [Les liens d'events cités encodent désormais `nevent`](https://github.com/nostrord/nostrord/pull/293) avec l'auteur, le kind et le relay depuis lequel la citation a été lue, afin qu'un event [NIP-29](/fr/topics/nip-29/) (groupes gérés par des relays) partagé dans un DM puisse être récupéré par un autre client, au lieu d'utiliser un simple identifiant de note dépourvu d'indications de recherche.

## Mises à jour des NIPs et travaux sur les spécifications du protocole

### Possibilités d'implémentation de Nostr

Deux modifications de spécification ont été intégrées cette semaine au [dépôt principal des NIPs](https://github.com/nostr-protocol/nips).

[NIP-67](/fr/topics/nip-67/) définit des indications qu'un relay peut ajouter à un message `EOSE` (fin des events stockés) afin qu'un client sache s'il doit poursuivre la pagination. L'[indication `"auth"` intégrée](https://github.com/nostr-protocol/nips/pull/2371) ajoute une troisième valeur aux côtés de `finish` et `more` : un relay peut désormais signaler que d'autres events stockés pourraient devenir visibles si l'utilisateur s'authentifie, et il doit envoyer le challenge `AUTH` de [NIP-42](/fr/topics/nip-42/) (authentification auprès du relay) avant l'`EOSE` porteur de l'indication. L'[ajout correspondant à NIP-42](https://github.com/nostr-protocol/nips/pull/2371) définit le même parcours côté client, si bien qu'un client qui reçoit un `EOSE` avec `auth` dispose déjà du challenge auquel il doit répondre.

[NIP-84](/fr/topics/nip-84/) (passages surlignés portables, les events kind `9802` désormais pris en charge par Amethyst ci-dessus) [intègre une mise à jour du schéma de tags](https://github.com/nostr-protocol/nips/pull/2454) : les passages surlignés peuvent maintenant référencer leur source au moyen de tags `i` structurés conformément à [NIP-73](/fr/topics/nip-73/) (identifiants de contenu externe), en plus des tags `a`/`e` pour les events Nostr et des tags `r` pour tout le reste ; lors de l'affichage, les citations surlignées passent en outre d'une exigence MUST à une recommandation SHOULD, comme une citation-repost.

### Nostr Wallet Connect

Une réponse `list_transactions` peut indiquer le nombre de transactions correspondant à la requête, plutôt que le nombre de lignes renvoyées par la page actuelle. Le champ [facultatif `total_count` intégré](https://github.com/nostr-wallet-connect/nwc/pull/4) à NWC-05 (l'extension d'historique du portefeuille) dans le [dépôt des extensions NWC](https://github.com/nostr-wallet-connect/nwc) ajoute ce champ à la réponse utilisée avec [NIP-47](/fr/topics/nip-47/) (contrôle chiffré d'un portefeuille distant via Nostr).

Le [commit qui ajoute `total_count`](https://github.com/nostr-wallet-connect/nwc/commit/ff3e49a47d040075edc46ee42fc0e33f10f1ef67) le décrit comme un entier facultatif : le nombre total de transactions correspondant aux filtres de la requête.

Le [commit qui exclut la pagination du décompte](https://github.com/nostr-wallet-connect/nwc/commit/06315e735f744b1afd3df0b57436fdce8a7bfc2e) précise que ce total ne tient pas compte de la pagination et compte donc toutes les transactions correspondantes sur l'ensemble des pages.

## Analyse approfondie des NIPs : reposts et réactions

Un contact peut remettre une note existante sous les yeux de ses abonnés et y joindre un like, un dislike ou un emoji compact sans écrire de réponse. [NIP-18](/fr/topics/nip-18/) (reposts) publie cette redistribution sous la forme de son propre event signé. [NIP-25](/fr/topics/nip-25/) (réactions) publie la réponse compacte dans un event signé distinct. Les deux restent des fichiers `draft` `optional` dans la [spécification canonique des reposts](https://github.com/nostr-protocol/nips/blob/master/18.md) et la [spécification canonique des réactions](https://github.com/nostr-protocol/nips/blob/master/25.md) : ils figurent dans le dépôt des NIPs et sont implémentés par les clients, tout en restant qualifiés de non définitifs.

### Reposts (NIP-18)

Lorsqu'un client écrit un event kind 6, les abonnés reçoivent un pointeur signé vers une note textuelle kind 1 déjà publiée par quelqu'un. La [spécification des reposts](https://github.com/nostr-protocol/nips/blob/master/18.md) fixe `kind` à 6, place dans `content` le JSON sérialisé de cette note (`content` vide est autorisé mais déconseillé), exige un tag `e` dont la valeur est l'`id` de la note et dont la troisième entrée est l'URL d'un relay où la note peut être récupérée, et précise que l'event SHOULD aussi porter un tag `p` contenant la `pubkey` de l'auteur d'origine. Le repost d'un event [NIP-70](/fr/topics/nip-70/) (events protégés) SHOULD conserver un `content` vide afin de ne pas copier le payload protégé dans le nouvel event.

Une citation est une référence intégrée à un autre event, et non un wrapper kind 6. Lorsqu'un client mentionne un `nevent`, une `note` ou une `naddr` au moyen d'une URI [NIP-21](/fr/topics/nip-21/) (`nostr:`), il doit convertir cette mention en un tag `q` de la forme `["q", "<event-id> or <event-address>", "<relay-url>", "<pubkey-if-a-regular-event>"]`. Les [tags de quote-repost](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts) maintiennent ces citations hors des fils de réponses et permettent aux clients de récupérer et de compter les citations d'une publication.

Le kind 6 est réservé aux notes kind 1. Un repost générique kind 16 peut encapsuler un event de n'importe quel kind autre que 1. Il SHOULD inclure un tag `k` dont la valeur est le kind sérialisé de l'event interne. Lorsque cet event interne est remplaçable, le repost générique SHOULD ajouter un tag `a` contenant la coordonnée `kind:pubkey:d-tag` ; en l'absence de ce tag `a`, le repost cible une version précise et `content` doit contenir la chaîne JSON complète de cette version. Les [règles des reposts génériques](https://github.com/nostr-protocol/nips/blob/master/18.md#generic-reposts) empêchent de publier les events longs, adressables et autres events qui ne sont pas des notes comme s'ils étaient kind 1.

L'event kind 6 suivant est un repost réel récupéré depuis `wss://relay.damus.io` au moment de l'assemblage ([ouvrir l'event](https://njump.me/nevent1qqs88k8xgv2d3d3yymawaa24f22a0kqqvknpur0p05vq9e5r4y74xjspz3mhxue69uhhyetvv9ujuerpd46hxtnfdu7elvca)) :

```json
{
  "kind": 6,
  "id": "73d8e64314d8b62426faeef5554a95d7d80065a61e0de17d1802e683a93d534a",
  "pubkey": "a60e79e0edad5100d7543b669e513dbc1c2170e8e9b74fdb8e971afd1e0e6813",
  "created_at": 1787768621,
  "tags": [
    [
      "e",
      "38980cd673ee16609dc87081d9f645c331d5a5a8b5b0d6c8147600ed29447976"
    ],
    [
      "p",
      "34d2f5274f1958fcd2cb2463dabeaddf8a21f84ace4241da888023bf05cc8095"
    ],
    [
      "client",
      "Primal iOS"
    ]
  ],
  "content": "{\"pubkey\":\"34d2f5274f1958fcd2cb2463dabeaddf8a21f84ace4241da888023bf05cc8095\",\"sig\":\"8c0271f7b438083ce491c391335598e0cbceee0758177cf98f7894531033cb5153704b01009590f3d4e9cdfadd5bbf73fc5eea54186fcbac6d30744e0e6c1cd6\",\"id\":\"38980cd673ee16609dc87081d9f645c331d5a5a8b5b0d6c8147600ed29447976\",\"tags\":[[\"r\",\"https:\/\/stacker.news\/items\/1555439\"],[\"client\",\"Damus\"]],\"created_at\":1787766056,\"content\":\"🚨 Attention CLN (Core Lightning) node runners 🚨\n\nhttps:\/\/stacker.news\/items\/1555439\",\"kind\":1}",
  "sig": "b6b97fa377cfdb651e2850f65f2ccb12ca0724c0de0fc0e39e9721f850abdfd31f5d5567517a51d988145c2a2de9ae9540b02eecf7352e554022870d5e8c64a5"
}
```

Son `kind` est 6, le tag `e` pointe vers la note repostée, le tag `p` identifie l'auteur de cette note et `content` contient l'event kind 1 d'origine sous forme de JSON sérialisé. Cet event récupéré depuis un relay omet l'indication de relay que la [spécification NIP-18](https://github.com/nostr-protocol/nips/blob/master/18.md) marque comme obligatoire, ce qui montre pourquoi les lecteurs et les clients doivent valider les events réels et tolérer les producteurs qui omettent des champs.

### Réactions (NIP-25)

Une publication peut recueillir des likes, des dislikes et des emoji signés sans que ces marques n'entrent dans le fil des réponses. La [spécification des réactions](https://github.com/nostr-protocol/nips/blob/master/25.md) définit cette marque comme un event kind 7 dont le `content` MUST contenir la valeur de la réaction. `+` ou une chaîne vide MUST être interprété comme un like ou un vote positif. `-` MUST être interprété comme un dislike ou un vote négatif. Un emoji ou le shortcode d'un emoji personnalisé [NIP-30](/fr/topics/nip-30/) SHOULD NOT être interprété comme un like ou un dislike, et un client MAY afficher cet emoji sur la publication.

La cible se trouve dans les tags, elle n'est pas déduite de `content`. Un tag `e` défini sur l'`id` de l'event cible MUST être présent et ce tag SHOULD inclure une indication de relay ; les tags `e` supplémentaires sont déconseillés et, s'ils sont présents, l'`id` de la cible doit être le dernier. Un tag `p` pour l'auteur de la cible SHOULD être présent, en dernière position si plusieurs tags `p` figurent dans l'event. Une cible adressable SHOULD également recevoir un tag `a` avec les coordonnées `kind:pubkey:d-tag`. Les tags `e` et `a` SHOULD inclure des indications de relay et de pubkey, les tags `p` SHOULD inclure des indications de relay, et un tag `k` MAY contenir le kind sérialisé de l'event ayant reçu la réaction. Ces [règles relatives aux tags](https://github.com/nostr-protocol/nips/blob/master/25.md#tags) permettent à un client de récupérer la cible et de prévenir son auteur à partir du seul event de réaction.

Un client MAY placer un seul `:shortcode:` dans `content` et un tag `emoji` qui associe ce shortcode à l'URL d'une image, conformément aux [règles des réactions avec emoji personnalisés](https://github.com/nostr-protocol/nips/blob/master/25.md#custom-emoji-reaction). Si la cible n'est pas un event Nostr natif, la réaction MUST être kind 17 et MUST porter des tags `k` et `i` [NIP-73](/fr/topics/nip-73/) (identifiants de contenu externe), comme dans les [règles relatives aux réactions à du contenu externe](https://github.com/nostr-protocol/nips/blob/master/25.md#external-content-reactions). Le kind 17 représente une réaction à un site web, un épisode de podcast ou un autre objet externe. Il ne s'agit ni d'une réaction d'event à event kind 7, ni d'un repost.

L'event kind 7 suivant est une réaction réelle récupérée depuis `wss://relay.damus.io` au moment de l'assemblage ([ouvrir l'event](https://njump.me/nevent1qqsytac63l00k7kyaphkfwqqn94wglmx78v6zhqtytg65w5k957luccpz3mhxue69uhhyetvv9ujuerpd46hxtnfdus63jym)) :

```json
{
  "kind": 7,
  "id": "45f71a8fdefb7ac4e86f64b800996ae47f66f1d9a15c0b22d1aa3a962d3dfe63",
  "pubkey": "0755cc2b972c3cbcae36913109c50b36b3fe110fa38a76dc37d1f01c5305496a",
  "created_at": 1787768605,
  "tags": [
    [
      "e",
      "519de32071d71bb2ab8b71a07e03eb9a256b6a59f9b08877b156c80966d5c320"
    ],
    [
      "a",
      "34236:5ab67f7d7fed4f781008c0ec0d26c8113f9fb46094a8346246c70c75e75db9fb:2ddda68516f4729d3ef55a1eb01fe028253393212493a34816ad8eb79f97a3b7"
    ],
    [
      "p",
      "5ab67f7d7fed4f781008c0ec0d26c8113f9fb46094a8346246c70c75e75db9fb"
    ],
    [
      "k",
      "34236"
    ],
    [
      "client",
      "Divine",
      "31990:d95aa8fc0eff8e488952495b8064991d27fb96ed8652f12cdedc5a4e8b5ae540:divine-mobile",
      "wss://relay.divine.video"
    ]
  ],
  "content": "+",
  "sig": "3c081756c7a73e2ee8aa10fadf3b5009390d5ac9a72078ba03701c42af91022ef275df7cb17724689a23dca4e29ff1a7cd5e3a24135d021983e2726a28b00b1e"
}
```

Son `content` est `+`, le like conventionnel de [NIP-25](https://github.com/nostr-protocol/nips/blob/master/25.md). Le tag `e` désigne l'event visé par la réaction ; le tag `a` ajoute sa coordonnée adressable ; le tag `p` identifie son auteur ; et le tag `k` facultatif enregistre sous forme de chaîne le kind de la cible.

### Implémentations actuelles dans les clients

[Amethyst](https://github.com/vitorpamplona/amethyst), un client Nostr pour Android, définit le [type d'event de repost](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip18Reposts/RepostEvent.kt) et le [type d'event de réaction](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip25Reactions/ReactionEvent.kt) dans sa couche de protocole actuelle.

[Snort](https://github.com/v0l/snort), un client web Nostr, implémente des [fonctions auxiliaires NIP-18 comprenant la gestion des tags de liens de citation](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip18.ts) et [crée les tags de réaction aux events NIP-25](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip25.ts).

[Ditto](https://github.com/soapbox-pub/ditto), à la fois serveur Mastodon et relay Nostr, [publie des reposts génériques kind 16 avec un tag `k` et une coordonnée `a` pour les cibles adressables](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/components/RepostMenu.tsx) et [applique la sémantique des réactions kind 7 en traitant le dernier tag `e` comme l'event cible](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/lib/nostrEvents.ts).

### Comment ils fonctionnent ensemble

Un event kind 6 ou kind 16 redistribue un event existant dans les flux des abonnés de l'auteur du repost, soit en intégrant le JSON de cet event, soit en pointant vers une coordonnée remplaçable. Un tag `q` marque une citation dans un autre event, afin que la reconstruction du fil puisse compter les citations sans traiter l'event qui cite comme une réponse ; c'est la distinction établie dans la [section consacrée aux quote-reposts](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts). Un event kind 7 laisse l'event d'origine en place et n'y joint que la valeur de la réaction et les tags de la cible, conformément au contrat de la [spécification des réactions](https://github.com/nostr-protocol/nips/blob/master/25.md). Les clients qui récupèrent les events d'une pubkey voient donc les reposts de celle-ci comme de nouveaux events kind 6 ou 16, et ses opinions comme des events kind 7 sur les publications d'autres personnes.

---

Envoyez un DM NIP-17 pour partager un projet ou une actualité par l'intermédiaire du [projet Nostr Compass](https://github.com/andotherstuff/nostr-compass).
