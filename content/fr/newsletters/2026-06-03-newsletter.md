---
title: 'Nostr Compass #25'
date: 2026-06-03
publishDate: 2026-06-03
draft: false
type: newsletters
translationOf: /en/newsletters/2026-06-03-newsletter.md
translationDate: 2026-07-01
---

Amber 6.2.0 livre le chiffrement NIP-44 v3 avant la spécification. Mostro pose la fondation pour l'entiercement réglé en Cashu à travers huit PRs, enveloppant le Cashu Development Kit existant comme deuxième backend de règlement aux côtés de Lightning. Les podcasts NIP-F4 fusionnent après 27 mois de débat. fiatjaf ouvre une proposition contestée de découplage de clé NIP-17 qui rouvre l'argument architectural bunker-contre-Marmot. Amethyst livre l'étiquetage de hashtag NIP-32, un écran de podcast dédié et les zaps on-chain à travers 52 PRs non publiées.

## Articles principaux

### Amber 6.2.0 : chiffrement NIP-44 v3 livré

[Amber v6.2.0](https://github.com/greenart7c3/Amber/releases/tag/v6.2.0), publié le 1er juin, ajoute le [support de chiffrement NIP-44 v3](https://github.com/greenart7c3/Amber/pull/448) avec un écran d'approbation dédié, un aperçu d'intent, un aperçu bunker, la journalisation d'historique, et l'auto-rejet pour les demandes invalides. La sortie enregistre également les [autorités ContentProvider NIP-44 v3](https://github.com/greenart7c3/Amber/commit/8b93340) afin que d'autres apps Android puissent demander le chiffrement v3 aux côtés du chemin v2 existant. NIP-44 lui-même est la spécification de charge utile chiffrée versionnée utilisée par les DMs privés [NIP-17](/fr/topics/nip-17/), le trafic bunker NIP-46, et d'autres primitives Nostr ; v3 dans Amber est un opt-in aux côtés de v2, signalé par une méthode de signataire séparée afin que les clients côté récepteur puissent négocier l'algorithme explicitement. La PR NIPs correspondante n'a pas encore atterri, donc Amber déploie v3 avant le consensus de protocole, avec le format de câble et l'autorité ContentProvider enregistrés pour l'intégration client en aval.

Les sessions NIP-46 acceptent maintenant automatiquement les demandes de ping à la connexion, supprimant l'invite au premier aller-retour après l'appairage. La méthode de signataire `sign_message` a été entièrement supprimée après avoir été dépréciée et inutilisée.

Parce qu'Amber est le signataire Android dominant, chaque client en aval qui veut v3 doit cibler le format de câble d'Amber jusqu'à ce que la PR NIPs atterrisse. Cela donne à Amber un mot implicite sur la spécification v3 finale jusqu'à ce que le protocole rattrape. L'échange est réel : v3 en production permet à Amber de rassembler des retours d'implémentation pour le NIP éventuel, au coût d'un point de référence à implémentation unique temporaire que d'autres clients doivent maintenant égaler.

### Mostro : intégration d'entiercement Cashu via CDK

grunch a atterri huit PRs à travers MostroP2P cette semaine intégrant les primitives multisig P2PK existantes de Cashu (NUT-10 et NUT-11) comme deuxième backend de règlement aux côtés de Lightning sur l'échange Bitcoin P2P coordonné par Nostr. Les primitives cryptographiques sont celles de Cashu ; le travail est un échafaudage d'intégration et un nouveau trait de backend d'entiercement. [Mostro core v0.12.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.12.0), publié le 30 mai, ajoute les [types de protocole pour l'entiercement multisig 2-de-3](https://github.com/MostroP2P/mostro-core/pull/150), les signatures P_M par preuve, et permet les événements d'entiercement via la validation de réponse. L'architecture est documentée dans [PR #756](https://github.com/MostroP2P/mostro/pull/756) et utilise des clés de trade par commande clarifiées dans [PR #757](https://github.com/MostroP2P/mostro/pull/757).

L'implémentation s'est déployée à travers six PRs de suivi sur une seule journée. [F2 (PR #758)](https://github.com/MostroP2P/mostro/pull/758) a ajouté la config, le mode d'entiercement, et le démarrage conditionnel. La tranche suivante, [F3 (PR #760)](https://github.com/MostroP2P/mostro/pull/760), a défini un trait `EscrowBackend` avec une implémentation Lightning et un stub Cashu, permettant à Mostro de commuter les backends de règlement sans changer la machine d'état de commande. [F4 (PR #759)](https://github.com/MostroP2P/mostro/pull/759) a enveloppé [CDK](https://github.com/cashubtc/cdk) (le Cashu Development Kit) pour les opérations de mint et de portefeuille. Le travail de base de données dans [F5 (PR #761)](https://github.com/MostroP2P/mostro/pull/761) a ajouté des verrous d'entiercement compare-and-swap et des requêtes de verrous actifs. [F6 (PR #762)](https://github.com/MostroP2P/mostro/pull/762) a construit un mint conteneurisé dans une tâche CI dédiée pour les tests d'entiercement de bout en bout. Le flux Mostro utilise déjà les DMs gift-wrapped NIP-59 pour la coordination de commandes sur le relais, donc l'entiercement Cashu s'insère comme deuxième option de règlement aux côtés de Lightning sans toucher au protocole de câble.

## Sorties

### ngit v2.5.0 : fallback GRASP et fetches git paresseux

[ngit v2.5.0](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.5.0) change le comportement par défaut de `git push pr/<branch>` et `ngit send` pour produire un kind PR pour les nouvelles propositions quand le dépôt a au moins un serveur GRASP enregistré. Auparavant, cela ne se déclenchait que pour les commits surdimensionnés de plus de 60 KB ou les commits contenant des submodules. Quand une PR ne peut pas être poussée vers les serveurs GRASP du dépôt, ngit revient maintenant au routage GRASP-06 via les serveurs déclarés. Le drapeau `ngit send --git-server` ou `git push -o git-server=<url>` permet aux contributeurs de cibler une URL git personnalisée ou un serveur GRASP explicitement.

Les republications `ngit init` préservent maintenant les balises inconnues des annonces existantes, afin que les balises ajoutées par une future version de ngit ou un outil tiers survivent à la republication. Un avertissement jaune liste les balises reportées, et `--clean` les supprime à la demande. `ngit pr apply`, `ngit pr checkout`, et `ngit pr list` consultent les serveurs git paresseusement et partagent un helper de fetch unique, afin que le checkout ne fetch plus inconditionnellement quand le commit est déjà local. `ngit pr checkout` essaie également les URLs de clone fournies par le soumetteur depuis l'événement PR comme fallback quand les serveurs git déclarés du dépôt ne portent pas le tip de la PR, correspondant au comportement existant dans `ngit pr apply`. ngit est l'implémentation de référence [NIP-34](/fr/topics/nip-34/) pour la collaboration git sur Nostr, et v2.5.0 fait de GRASP le chemin de première classe pour les nouveaux contributeurs.

### Jumble v26.5.7 : stripping EXIF et compteurs de zap validés

[Jumble v26.5.7](https://github.com/CodyTseng/jumble/releases/tag/v26.5.7) ajoute deux changements qui affectent directement la vie privée de l'utilisateur et l'intégrité des données. Les identifiants de localisation et de caméra EXIF sont maintenant supprimés des uploads d'images avant qu'ils ne quittent le client, fermant une surface de fuite de métadonnées de longue date qui affectait chaque image postée depuis Jumble. Les compteurs de zap sont maintenant calculés uniquement à partir de reçus cryptographiquement validés, corrigeant les compteurs gonflés provenant d'événements de zap malformés qui permettaient aux attaquants d'exagérer les totaux de zap sur les notes. La sortie ajoute également la vérification d'identité d'expéditeur pour les DMs [NIP-17](/fr/topics/nip-17/), fermant une surface d'usurpation où un expéditeur pouvait forger sa `pubkey` dans le seal.

### nostr-calendar v1.6.0 : RSVP et gestion des participants en double

[nostr-calendar v1.6.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.6.0) atterrit le flux RSVP de Formstr ([PR #169](https://github.com/formstr-hq/nostr-calendar/pull/169)) et empêche les participants en double dans les invitations à un événement ([PR #168](https://github.com/formstr-hq/nostr-calendar/pull/168)). L'option `waitForAll` dans la fonction de publication par défaut est maintenant à false pour que l'UI ne se bloque pas sur les relais lents ([PR #170](https://github.com/formstr-hq/nostr-calendar/pull/170)). [PR #157](https://github.com/formstr-hq/nostr-calendar/pull/157) a livré les deux brouillons de proposition NIP de Formstr pour la planification de rendez-vous et les réservations.

### Sprout 0.3.6 : Sprout × mesh-llm et sections de canal

[Sprout v0.3.6](https://github.com/block/sprout/releases/tag/v0.3.6) est le titre d'une série de six sorties de v0.3.1 à v0.3.6 cette semaine. L'intégration in-process de Sprout × mesh-llm atterrit dans [PR #798](https://github.com/block/sprout/pull/798), permettant à Sprout de servir et consommer des nœuds mesh-llm via l'admission de relais. Les sections de canal définies par l'utilisateur se synchronisent entre les appareils via Nostr dans [PR #792](https://github.com/block/sprout/pull/792), et les sections de canal arrivent sur mobile avec la synchronisation relais dans [PR #800](https://github.com/block/sprout/pull/800). Les notifications conscientes des fils avec des contrôles mute et follow mutables arrivent dans [PR #761](https://github.com/block/sprout/pull/761).

Les pièces jointes de type de fichier arbitraire avec cartes de téléchargement sont arrivées dans [PR #810](https://github.com/block/sprout/pull/810), étendant Sprout au-delà des pièces jointes image uniquement. Mobile a gagné un onglet de fil social Pulse ([PR #772](https://github.com/block/sprout/pull/772)) et le polissage Pulse à travers les surfaces de fil, composition et filtre ([PR #796](https://github.com/block/sprout/pull/796)).

### NostrBotKit v0.5.0 : chat de groupe Marmot dans un framework de bot Rust

[NostrBotKit v0.5.0](https://codeberg.org/Tuxor/NostrBotKit/src/branch/main/CHANGELOG.md), publié le 24 mai sur Codeberg, ajoute le support [Marmot](/fr/topics/marmot/) (MLS-over-Nostr, [NIP-104](https://github.com/nostr-protocol/nips/pull/2014)) au framework de bot Rust auto-hébergé. Quand `marmot: true` est défini, le bot publie ses key packages MLS (kind 443, 30443, 10051), accepte les invitations de groupe automatiquement, et écoute les messages dans les groupes rejoints. Deux nouveaux types de commande, `dm_marmot` et `dm_marmot_npub`, permettent aux bots d'envoyer des messages dans des groupes Marmot nommés ou des chats Marmot 1:1 via des tâches cron ou des webhooks. Pour prévenir les boucles de rétroaction avec d'autres bots, les bots NostrBotKit ne répondent qu'aux messages explicitement adressés à eux via `/command` ou `@botname/command`. Les pièces jointes chiffrées utilisant MIP-04 sont automatiquement déchiffrées et re-uploadées via Blossom ou NIP-96, et la base de données d'état MLS est chiffrée avec une clé dérivée de la clé privée du bot. NostrBotKit est le premier framework Rust à livrer un support de bot NIP-104, ouvrant le déploiement de bots chiffrés par Marmot à un profil d'opérateur différent du chemin TypeScript existant.

### noscrypt v0.1.14 : sortie de bibliothèque cryptographique signée

[noscrypt v0.1.14](https://github.com/vnuge/noscrypt/releases/tag/v0.1.14) est une sortie de sécurité de la bibliothèque cryptographique C utilisée par plusieurs clients Nostr pour les primitives secp256k1, NIP-04 et NIP-44. La sortie livre des [téléchargements signés PGP](https://www.vaughnnugent.com/resources/software/modules/noscrypt) vérifiables contre la clé publique du mainteneur. Les clients en aval qui empaquettent noscrypt devraient valider la signature avant l'intégration.

### Chama v1.3.0 : nouvel entiercement P2P Nostr-natif avec Fedimint

[Chama v1.3.0](https://github.com/jesuspirate/chama/releases/tag/v1.3.0), publié le 1er juin, est le titre d'une série de quatre sorties pour un nouveau client d'entiercement P2P Nostr-natif qui utilise l'ecash Fedimint et le partage de secret Shamir 2-de-3 pour le règlement. Le projet est livré sur [getchama.app](https://getchama.app) et fonctionne sans serveur. v1.3.0 introduit « heal that sticks » (rediffusion réussie et guérison de trade qui survivent aux redémarrages de session) et l'appariement de rails de paiement, où les Chamas orientées US font surface les rails de paiement US en premier. Le travail préparatoire pour les vitrines multi-unités a atterri à travers [v1.2.11](https://github.com/jesuspirate/chama/releases/tag/v1.2.11) (schéma multi-unités) et [v1.2.12](https://github.com/jesuspirate/chama/releases/tag/v1.2.12) (comptable de stock de vitrine + durcissement de récupération de pont Fedimint natif). Chama rejoint Mostro et Shopstr dans la catégorie marketplace Nostr, distinguée par son architecture sans serveur et son règlement d'entiercement basé sur Fedimint.

## Changements non publiés

### Amethyst : étiquetage de hashtag NIP-32, écran de podcast, pistes musicales

Amethyst a fusionné 52 PRs et 411 commits cette semaine sans couper une balise de sortie. Le plus grand ajout fonctionnel est [PR #3111](https://github.com/vitorpamplona/amethyst/pull/3111), qui implémente l'étiquetage de hashtag [NIP-32](/fr/topics/nip-32/) et un fil de hashtag basé sur les étiquettes utilisant des événements kind 1985 avec des balises `L` de namespace et `l` d'étiquette. Cela remplace le mécanisme fragile de correspondance de texte `#tag` par un modèle de découverte basé sur les étiqueteurs où les utilisateurs peuvent suivre des npubs d'étiqueteurs spécifiques comme ils suivent des créateurs de contenu. [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) ajoute un écran de podcast dédié avec liste d'épisodes et lecteur en ligne, atterrissant dans les jours suivant la fusion de la spécification podcast [NIP-F4](/fr/topics/nip-f4/). [PR #3071](https://github.com/vitorpamplona/amethyst/pull/3071) ajoute un fil d'applications logicielles avec filtrage de liste de suivis, et [PR #3067](https://github.com/vitorpamplona/amethyst/pull/3067) ajoute le support des pistes musicales et playlists via les ensembles [NIP-51](/fr/topics/nip-51/).

Les signataires éphémères pour les uploads de posts anonymes atterrissent dans [PR #3123](https://github.com/vitorpamplona/amethyst/pull/3123), permettant aux utilisateurs de poster anonymement sans exposer leur clé d'identité aux services d'upload. Un watchdog d'auto-guérison Tor avec des tests d'intégration contre Arti v2.3.0 arrive dans [PR #3053](https://github.com/vitorpamplona/amethyst/pull/3053), renforçant le routage Tor d'Amethyst pendant les pannes réseau transitoires. Les zaps on-chain et un filtre NIP-05 pour les utilisateurs revenant de Gemini atterrissent dans [PR #3052](https://github.com/vitorpamplona/amethyst/pull/3052), élargissant la surface de zap au-delà de Lightning aux paiements Bitcoin on-chain.

### Shopstr : validation d'URL d'aperçu OpenGraph

[PR #504](https://github.com/shopstr-eng/shopstr/pull/504) valide les URLs d'aperçu OpenGraph avant de les rendre dans les annonces de marketplace, fermant une surface XSS potentielle où des vendeurs malveillants pourraient intégrer du contenu scripté via des métadonnées OG conçues. Les boutiques hébergées par Shopstr affichent des aperçus OG pour les liens externes, et les URLs non validées permettent à un attaquant d'injecter du contenu arbitraire dans l'UI de la boutique.

## Mises à jour NIP et travail de spécification de protocole

### NIP-F4 (Podcasts) fusionné après deux ans

[PR #1093](https://github.com/nostr-protocol/nips/pull/1093) a fusionné le 28 mai, deux ans et trois mois après que fiatjaf ait ouvert le projet original. NIP-F4 définit les épisodes de podcast comme événements kind 54 avec des balises `imeta` pour les métadonnées de fichier audio (URL, type mime, code de langue ISO, URLs de fallback, drapeau de service NIP-96, débit binaire, durée), une balise `title`, des balises optionnelles `image` et `description`, et des balises `t` pour les étiquettes de sujet. La spécification garde délibérément RSS comme source de vérité : les épisodes peuvent porter une balise `i` référençant le GUID de podcast RSS, permettant aux clients Nostr de créer des liens vers les flux de podcast existants sans dupliquer l'hébergement audio. Le long débat dans le fil de la PR (avec le co-auteur podcast-namespace Dave Jones, Alex Gleason, et Mike Terenzio) s'est stabilisé sur un modèle de coexistence où Nostr fournit la couche sociale au-dessus de RSS tandis que RSS garde la couche de distribution. [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) d'Amethyst atterrit l'écran de podcast dans les jours suivant la fusion de la spécification, et le travail du sélecteur de GIF de Jumble inclut également un échafaudage précoce de pièces jointes de podcast.

### Découplage de clé NIP-17 (PR #2361)

fiatjaf a ouvert [PR #2361](https://github.com/nostr-protocol/nips/pull/2361) le 1er juin, proposant que NIP-17 sépare la clé d'identité de la clé de chiffrement. Les destinataires annoncent leur clé de chiffrement dans un nouvel événement kind 10044, et les expéditeurs utilisent cette clé annoncée (quand présente) pour le seal interne gift-wrap, ne revenant à la clé d'identité du destinataire que quand l'annonce est absente. La PR ajoute également une balise `n` au seal portant la pubkey de chiffrement de l'expéditeur, afin que les récepteurs puissent dériver la bonne clé de conversation sans déchiffrement d'essai contre chaque clé retirée. La motivation déclarée est l'UX bunker : sous la conception actuelle, un utilisateur bunker doit faire l'aller-retour de chaque DM reçu à travers le signataire pour déchiffrer, puisque la clé de chiffrement est la clé d'identité détenue par le signataire. Le découplage permet au client de détenir la clé de chiffrement localement tout en gardant la clé d'identité dans le bunker pour les signatures.

La proposition a attiré la revue la plus contestée de la semaine. Cody Tseng (Jumble) la soutient comme le chemin le plus facile vers l'interopérabilité DM inter-clients. Vitor Pamplona (Amethyst) objecte sur deux terrains : elle ajoute un nouveau secret de déchiffrement à long terme en dehors du bunker, et les clients qui ne la livrent pas échoueront silencieusement à déchiffrer les messages des clients qui la livrent, sans chemin de dégradation parce que la rupture est à la couche seal. Pamplona soutient que le problème est déjà correctement résolu par les key packages et la rotation d'époque de [Marmot](/fr/topics/marmot/), et que rétrofitter la séparation de clé dans la spécification NIP-17 de base crée le genre d'échec d'interop que Marmot a mis deux ans à concevoir. Le contre-argument de fiatjaf a trois parties : le découplage est optionnel par destinataire, le correctif de balise n aborde la préoccupation de déchiffrement d'essai, et l'alternative est de garder l'UX bunker cassée pendant que Telegram mange le cas d'usage de messagerie. Le fil reste ouvert sans décision de fusion et est la discussion NIP la plus surveillée du trimestre.

### Flux de paiement NIP-Silent Payments (PR #2362)

[silentius-satoshi a ouvert PR #2362](https://github.com/nostr-protocol/nips/pull/2362) le 1er juin comme compagnon du projet NIP Nostr Silent Payments plus large ([PR #2355](https://github.com/nostr-protocol/nips/pull/2355)). Le NIP de flux de paiement définit kind 8352 pour les notifications de reçu de silent payment (livrées via gift wrap [NIP-59](/fr/topics/nip-59/) afin que le lien de reçu ne soit pas publiquement observable) et kind 10353 pour un cache UTXO chiffré qui se synchronise entre les appareils pour le même portefeuille Silent Payments. La paire ensemble permet à un payeur de signaler un paiement à une adresse Silent Payments en utilisant des primitives Nostr-natives sans exposer le lien on-chain sur la couche relais ouverte.

### NIP-PIP Perfect IP Packets (PR #2364)

[RandyMcMillan a ouvert PR #2364](https://github.com/nostr-protocol/nips/pull/2364) le 1er juin comme brouillon. Il introduit un transport packet-tree avec trois nouveaux kinds adressables : 39078 porte le manifeste, 39079 porte les tranches individuelles, et 39080 porte les demandes de réparation. La spécification définit un format de câble où les gros fichiers sont divisés en tranches adressables, avec des manifestes décrivant l'arbre des tranches et des demandes de réparation permettant aux récepteurs de demander les tranches manquantes. Le statut d'ébauche précoce s'applique, et la proposition n'a pas encore attiré de revue de mainteneur.

### Espaces live audio/vidéo NIP-29 (PR #2238)

[PR #2238](https://github.com/nostr-protocol/nips/pull/2238) a fusionné le 28 mai, étendant les groupes relais [NIP-29](/fr/topics/nip-29/) avec le support d'espaces live audio et vidéo. Les groupes peuvent maintenant référencer une session d'espace live active, permettant aux événements de style [NIP-53](/fr/topics/nip-53/) live activity de s'ancrer dans un contexte de groupe NIP-29.

### Pistes audio multiples vidéo NIP-71 (PR #2255)

[PR #2255](https://github.com/nostr-protocol/nips/pull/2255) a fusionné le 28 mai, ajoutant des balises `imeta` de piste audio aux événements vidéo NIP-71. Le nouveau format porte l'URL, le hash, le type mime, la balise de langue (avec ISO-639-1 plus drapeau de version originale), les URLs de fallback, le signal de service NIP-96, le débit binaire, et la durée. Cela permet le streaming audio uniquement (podcasts vidéo), la commutation de résolution avec audio stable, les pistes multilingues, et un stockage réduit quand les serveurs n'intègrent pas directement l'audio dans les fichiers vidéo. Les clients devraient vérifier la disponibilité de piste audio avant d'assumer un comportement à piste unique.

### Gift wrap éphémère NIP-59 (PR #2245)

[PR #2245](https://github.com/nostr-protocol/nips/pull/2245) a fusionné le 28 mai, ajoutant kind 21059 comme équivalent éphémère du gift wrap kind 1059 existant. La sémantique correspond au wrap standard NIP-59 mais suit les règles d'événement éphémère selon NIP-01 (les relais les abandonnent après la diffusion et ne les persistent pas). Cela permet aux apps de choisir la persistance selon les exigences : les indicateurs de saisie et les pings de présence bénéficient de l'éphémère, tandis que l'historique DM a besoin de persistance.

### Kind spécifique à l'application NIP-78 (PR #2292)

[PR #2292](https://github.com/nostr-protocol/nips/pull/2292) a fusionné le 28 mai, reclassant les données spécifiques à l'application NIP-78 comme kind adressable normal, abandonnant la plage séparée précédente. Cela simplifie la sémantique de remplaçabilité et aligne NIP-78 avec le modèle d'événement adressable utilisé par d'autres NIPs d'état d'application.

### Clarifications NIP-85 (PR #2304)

[PR #2304](https://github.com/nostr-protocol/nips/pull/2304) a fusionné le 28 mai avec de petites améliorations au langage autour de plusieurs clés et relais par fournisseur de service dans les Trusted Assertions [NIP-85](/fr/topics/nip-85/), clarifiant le chemin de rotation de clé d'opérateur pour les services d'assertion de relais.

### Gestion de connexion de relais NIP-01 en une ligne (PR #2307)

[PR #2307](https://github.com/nostr-protocol/nips/pull/2307) a fusionné le 28 mai, ajoutant une seule phrase à NIP-01 sur la façon dont les clients devraient gérer les durées de vie de connexion aux relais. Le correctif aborde une lacune de longue date où les clients différaient sur l'opportunité de garder les connexions WebSocket ouvertes après la récupération, menant à une perte silencieuse de messages sur les relais qui abandonnent les connexions inactives.

### Contrainte de chat kind 9 NIP-C7 (PR #2310)

[PR #2310](https://github.com/nostr-protocol/nips/pull/2310) a fusionné le 28 mai, restreignant les vues de chat NIP-C7 aux messages kind 9 uniquement. Cela sépare le chat éphémère des posts de timeline kind 1 dans les clients qui implémentent des surfaces de chat de style NIP-C7.

### Simplification NIP-55 (PR #2363)

[PR #2363](https://github.com/nostr-protocol/nips/pull/2363) par greenart7c3, ouvert le 1er juin, simplifie la spécification d'application signataire Android. Vitor Pamplona a signé « Looks good » et fiatjaf a demandé si c'était prêt à fusionner. Le changement ouvre la voie à l'enregistrement d'autorité ContentProvider NIP-44 v3 qu'Amber a livré cette semaine.

### NIP-44 v3 (implémentation Amber avant la spécification)

Amber a livré NIP-44 v3 dans v6.2.0 avec huit commits implémentant la mise à niveau de chiffrement et l'enregistrement d'autorité ContentProvider, mais la PR de spécification du dépôt NIPs n'a pas encore atterri. NIP-44 lui-même définit un format de charge utile chiffrée versionnée utilisé à l'intérieur des événements signés ; le v2 existant (en production depuis 2024) utilise ECDH secp256k1, HKDF, padding, ChaCha20, HMAC-SHA256, et base64. Le format de câble v3 ajoute un nouvel octet de version (0x03) avant le nonce, permettant aux clients récepteurs de négocier l'algorithme explicitement. L'implémentation d'Amber inclut l'auto-rejet pour les demandes v3 invalides, un écran d'approbation dédié distinct des approbations v2, et la journalisation de texte-clair par direction pour l'historique. Jusqu'à ce que la PR NIPs fusionne, v3 reste comme extension spécifique à Amber. Traitez-la comme un signal prospectif, pas comme une signalisation stable à l'échelle du protocole.

## NIP deep dive : NIP-32 (Étiquetage)

[NIP-32](/fr/topics/nip-32/) définit un moyen structuré pour tout acteur Nostr d'étiqueter des événements, pubkeys, relais, URLs, ou sujets en utilisant des événements adressables kind 1985 avec un vocabulaire d'étiquettes à namespace. La spécification introduit deux nouvelles balises : `L` dénote un namespace d'étiquette, et `l` dénote une étiquette dans ce namespace. Les balises cible d'étiquette (`e`, `p`, `a`, `r`, ou `t`) spécifient ce qui est étiqueté. L'exigence de namespace empêche plusieurs systèmes d'étiquettes d'entrer en collision : une étiquette `spam` dans `nip28.moderation` porte une sémantique différente d'une étiquette `spam` dans `relay-report`.

Le choix de conception qui rend NIP-32 utile au-delà de la modération est que les étiquettes sont des assertions, pas une vérité au niveau du protocole. Un événement kind 1985 dit seulement qu'un pubkey particulier a étiqueté une cible particulière dans un namespace particulier. Le modèle de confiance est délégué au client : chaque client choisit quels étiqueteurs honorer, quels namespaces lire, et quelle affordance UI donner à chaque étiquette. La même primitive porte les avertissements de contenu, l'attribution de licence, les balises de langue ISO-639-1 sur les notes kind 1, les balises géographiques ISO-3166-2, la classification de contenu, les suggestions de modération distribuée, et les scores de réputation.

[PR #3111](https://github.com/vitorpamplona/amethyst/pull/3111) d'Amethyst cette semaine est le plus grand déploiement à ce jour. Il ajoute l'étiquetage de hashtag via NIP-32 et un fil de hashtag basé sur les étiquettes, permettant aux utilisateurs de parcourir par étiquettes assignées par des étiqueteurs de confiance. Le mécanisme de correspondance de texte `#tag` antérieur qui pilotait initialement la découverte de hashtag sur Nostr reste comme fallback pour les notes non étiquetées. Le modèle hashtag-comme-étiquette signifie que la même note peut être découvrable sous plusieurs étiquettes assignées par différents étiqueteurs, et les utilisateurs peuvent mute ou booster des étiqueteurs spécifiques sans affecter les notes sous-jacentes.

L'auto-étiquetage est également supporté. Un auteur peut attacher directement des balises `L` et `l` à ses propres notes kind 1 pour déclarer la langue, l'emplacement et le sujet. Une note étiquetée `["L", "ISO-639-1"], ["l", "en", "ISO-639-1"]` s'auto-identifie comme anglaise et peut être filtrée par des clients conscients de la langue sans infrastructure d'étiquetage tierce.

Exemple d'événement d'étiquette NIP-32 étiquetant une note kind 1 comme anglaise et lui assignant une balise de modération :

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748908800,
  "kind": 1985,
  "tags": [
    ["L", "ISO-639-1"],
    ["l", "en", "ISO-639-1"],
    ["L", "nip28.moderation"],
    ["l", "approve", "nip28.moderation"],
    ["e", "8b39f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3", "wss://relay.example.com"]
  ],
  "content": "Labeled as English-language content approved for NIP-28 chat moderation",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

Le déploiement Amethyst combiné avec le récent travail sur les Trusted Relay Assertions suggère que NIP-32 devient le substrat standard pour tout modèle « assertion pilotée par l'utilisateur sur une cible » sur Nostr. Le prochain test est de savoir si les étiqueteurs eux-mêmes développeront des hiérarchies de confiance : si les utilisateurs suivront des npubs d'étiqueteurs spécifiques comme ils suivent des créateurs de contenu.

## NIP deep dive : NIP-F4 (Podcasts)

[NIP-F4](https://github.com/nostr-protocol/nips/blob/master/F4.md) a fusionné cette semaine, deux ans et trois mois après que fiatjaf ait ouvert le projet original (PR #1093). Le préfixe F est un simple numérotage hex : NIP-F0 à NIP-FF utilisent le même espace hex de 1 octet que NIP-0A à NIP-0D, avec la plage hex supérieure servant de dépassement maintenant que la plage décimale 01-99 se remplit. NIP-F4 définit comment les podcasts publient des épisodes et des métadonnées comme événements Nostr tout en gardant RSS comme couche complémentaire pour le fichier audio lui-même.

Le choix architectural central est que chaque podcast est sa propre paire de clés Nostr. La spécification s'ouvre directement avec cela : « chaque podcast est sa propre paire de clés Nostr ». Cela permet aux podcasts de combiner leur présence de podcasting avec une présence normale de microblogging kind 0 / kind 1, et permet à un podcast de changer de propriété au fil du temps par transfert de clé ou signature partagée de style MuSig2. Quatre kinds d'événements portent la couche de publication :

- **`kind:10154`** : métadonnées de podcast remplaçables. Porte les balises `title`, `image`, `description`, `website` optionnelles, et des balises `p` optionnelles marquant les auteurs avec un `role` de `host`, `cohost`, ou `editor`.
- **`kind:10164`** : contre-revendication d'auteur. L'exemple dans la spécification utilise kind `10064` (une faute de frappe ouverte à la correction), mais le titre et le texte environnant l'identifient comme `kind:10164`. Les utilisateurs listent les pubkeys de podcast dont ils sont auteurs, afin que les clients puissent vérifier les balises `p` dans `kind:10154` contre une revendication équivalente de l'auteur supposé. Sans cela, un podcast pourrait faussement étiqueter n'importe qui comme hôte.
- **`kind:54`** : événements d'épisode rédigés par la pubkey du podcast directement. Les balises incluent `title`, `image` optionnel, `description`, et une ou plusieurs balises `audio`. Chaque balise `audio` est `["audio", "<audio-url>", "<optional_media_type>"]`. La spécification note « d'autres champs importants à spécifier ici plus tard après une découverte plus approfondie », et la forme fusionnée est délibérément minimale.
- **`kind:10054`** : une liste de podcasts favoris de style [NIP-51](/fr/topics/nip-51/), permettant aux utilisateurs de marquer quels podcasts ils suivent.

Le débat de fil autour de la fusion impliquait le co-auteur Podcasting 2.0 [Dave Jones](https://github.com/daveajones), [Alex Gleason](https://github.com/alexgleason), [Mike Terenzio](https://github.com/mterenzio), [Pablo F7z](https://github.com/pablof7z), et [staab](https://github.com/staab). Jones a argumenté fortement contre toute tentative de remplacer RSS : « Ça a été essayé plusieurs fois et échoue toujours », citant JSONfeed, XMPP, AMP, l'API Twitter, et la migration ratée de Spotify. Terenzio a recadré la proposition comme une couche sociale au-dessus de RSS, gardant RSS lui-même comme couche de distribution. fiatjaf a accepté de reculer et de laisser la proposition mûrir : « Je suis d'accord avec tout ce que vous avez dit mais je pense toujours qu'on peut y arriver, arrêtons ici pour un moment. » Deux ans plus tard, la spécification fusionnée atterrit plus près de la coexistence que du remplacement.

Trois questions de conception restent explicites dans la spécification fusionnée :

- La faute de frappe `kind:10164` (l'exemple montre `10064`) doit être réconciliée avant que les clients puissent interopérer en toute sécurité.
- La découverte au niveau épisode sans liaison GUID RSS est laissée ouverte. La spécification fusionnée n'a pas de balise `i`, pas de format `podcast:item:guid`, et pas de mécanisme de pontage RSS. Les clients qui veulent ponter un catalogue RSS existant vers des événements kind 54 doivent définir la convention de pontage eux-mêmes.
- Le stub « autres champs importants » sur la définition `kind:54` laisse le débit binaire, la durée, la langue, les pointeurs de transcription, les chapitres, et les métadonnées par segment comme territoire ouvert pour des propositions de suivi.

[PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) d'Amethyst atterrit un écran de podcast dédié avec liste d'épisodes et lecteur en ligne dans les jours suivant la fusion, la première implémentation majeure de client. Jumble a livré un échafaudage précoce de pièces jointes de podcast aux côtés de son sélecteur de GIF. Wavlake reste la plus grande plateforme de podcast Nostr-native et devra décider s'il faut aligner ses événements de piste musicale kind 31337 existants avec le modèle d'épisode kind 54 de NIP-F4.

Exemple d'événement d'épisode kind 54 NIP-F4, correspondant à l'ensemble minimal de balises de la spécification fusionnée :

```json
{
  "id": "55807e7d5cd90d0303d7dce7397f996fdbaed8697903f326c7cf8ad999b9de3d",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748995200,
  "kind": 54,
  "tags": [
    ["title", "Episode 42: Why RSS Won"],
    ["image", "https://podcast.example.com/ep42-cover.jpg"],
    ["description", "Dave Jones and fiatjaf on protocol coexistence and the social layer."],
    ["audio", "https://podcast.example.com/audio/ep42.mp3", "audio/mpeg"]
  ],
  "content": "In this episode we discuss the two-year journey of NIP-F4 from draft to merge, and why coexistence with RSS turned out to be the right architectural choice.",
  "sig": "abc123def456789012345678901234567890abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef01234567"
}
```

PR #1093 est resté ouvert pendant 27 mois, bien au-dessus de la durée médiane d'ouverture pour les PRs NIPs fusionnées. Le prochain test pour NIP-F4 est de savoir si la faute de frappe kind 10164 est réconciliée, si les conventions de découverte d'épisode et de pontage RSS émergent des implémenteurs, et si les grands hôtes de podcast publient sous des paires de clés par podcast comme la spécification le recommande.
