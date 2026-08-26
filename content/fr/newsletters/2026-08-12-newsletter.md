---
title: "Nostr Compass #35"
date: 2026-08-12
publishDate: 2026-08-12
translationOf: /en/newsletters/2026-08-12-newsletter.md
translationDate: 2026-08-12
draft: false
type: newsletters
description: "Outils d'identité post-quantique, messagerie chiffrée et signature renforcées, paramètres communautaires portables, et travail protocolaire sur les NIP et Concord."
---

Bienvenue dans [Nostr Compass](https://nostrcompass.org), votre guide hebdomadaire de Nostr.

**Cette semaine :** [nostr-wot-extension](https://github.com/nostr-wot/nostr-wot-extension) ajoute des clés post-quantiques et des messages protégés sur opt-in à côté des identités Nostr existantes. [Divine](https://github.com/divinevideo/divine-mobile) resserre l'isolation des comptes, la validation des messages privés et la confirmation de publication ; [MDK](https://github.com/marmot-protocol/mdk) renforce la convergence et la récupération des groupes chiffrés ; et [Amber](https://github.com/greenart7c3/Amber) rend explicites les décisions de signature groupées. Les versions améliorent les connexions de portefeuille, le chat chiffré, la découverte sociale, la synchronisation entre appareils et la signature distante, tandis que le travail protocolaire couvre l'identité et les communautés chiffrées. Les analyses approfondies expliquent les demandes de suppression authentifiées et le signalement décentralisé.

## À la une

### nostr-wot-extension 0.4.0 ajoute des clés post-quantiques à côté d'une identité Nostr

[nostr-wot-extension 0.4.0](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.4.0) est une extension de navigateur pour gérer des identités Nostr et signer. Les comptes créés à partir d'une seed de 24 mots peuvent désormais dériver des clés de chiffrement ML-KEM-1024 et de signature ML-DSA-87 aux côtés de leur clé Nostr existante. Un flux en un clic publie une attestation de kind `10203` qui lie la pubkey Nostr aux deux clés publiques post-quantiques et inclut une preuve de possession ML-DSA. Les comptes importés depuis une mnémonique de 12 mots, un `nsec` nu, un signataire distant ou une clé en lecture seule ne peuvent pas utiliser le flux de dérivation, et l'extension explique cette limitation dans la vue du compte.

La version ajoute aussi des messages directs post-quantiques sur opt-in. Elle combine le secret partagé ML-KEM avec la [clé de conversation de message chiffré NIP-44](https://github.com/nostr-protocol/nips/blob/master/44.md) existante via HKDF, puis conserve les couches normales de gift wrap [NIP-59](/fr/topics/nip-59/) (enveloppes masquant les métadonnées) pour la livraison par relais. Le chiffrement ne retombe jamais silencieusement après qu'un destinataire a opté, tandis que le déchiffrement sélectionne automatiquement le chemin approprié. Cela protège le nouveau chemin de message contre une récupération ultérieure d'une clé privée Nostr actuelle, mais ne remplace pas les signatures d'événements secp256k1 ; la version laisse explicitement cette migration plus large à une coordination future avec les relais et les clients.

### Divine Mobile 1.0.19 resserre les comptes, les messages privés et la publication

[Divine Mobile 1.0.19](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.19) est un client mobile de vidéo courte qui publie et récupère des vidéos via Nostr. Son sélecteur de compte construit désormais chaque identité connectée autour d'un conteneur propre au compte, et une correction de publication empêche une vidéo d'être envoyée sous le mauvais compte. Les chemins de publication vers les relais attendent maintenant une réponse `OK` avec une sémantique de succès explicite, tandis qu'une trame `CLOSED` du relais peut mettre fin à sa propre requête en attente au lieu de la laisser pendante.

La [gestion des messages privés](https://github.com/divinevideo/divine-mobile/pull/6368) rejette les champs rumor non authentifiés et les seals non signés, rétablit quatre cas de messages manquants, et achemine les conversations de groupe des participants entièrement suivis vers la boîte de réception. La version préserve aussi les tags des événements vidéo adressables lors de la mise à jour des listes et consomme les demandes de suppression observées pour que les vidéos retirées disparaissent de l'état local. Ces changements suivent le travail de délai d'expiration par requête couvert la semaine dernière, mais déplacent l'accent de l'isolation de la récupération vers les frontières d'identité, la validation des messages et la confirmation de publication.

### MDK 0.9.11 renforce la convergence et la récupération des groupes Marmot

[MDK 0.9.11](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.11) est une boîte à outils de développement Rust pour Marmot, un protocole de messagerie de groupe chiffrée transporté sur Nostr. La version construit un système de convergence et de récupération plus large autour de la machine à états du groupe : les passes de convergence périmées rouvrent à la pointe actuelle du groupe, les projections de capacité entrantes s'engagent de façon atomique, les messages différés reçoivent des durées de vie bornées entre les redémarrages, et les points de contrôle adressés par commit aident à récupérer les propres fourches de commit d'une identité. Les envois non stables peuvent être mis en file d'attente et récupérés, tandis qu'un chemin de blocage d'époque escalade vers le backfill et les messages envoyés survivent au travail de convergence.

Le [stockage et les intégrations hôtes](https://github.com/marmot-protocol/mdk/pull/1201) reçoivent un durcissement parallèle. MDK supprime de façon sécurisée les projections SQLite élaguées, zéroïse les clés privées importées, les intermédiaires d'export de clés chiffrées NIP-49 et les tampons de sérialisation OpenMLS, et masque les clés d'image de groupe dans la sortie de débogage. L'import de compte peut reprendre après interruption, les chemins de stockage privé iOS et Android sont réparés, et les hôtes peuvent fermer explicitement le stockage avant la suspension. De nouvelles projections légères de roster et d'appartenance locale réduisent ce que les applications doivent lire, tandis que le connecteur Hermes peut livrer plusieurs images générées par agent comme un album Marmot.

### Nostria 4.1.67 étend l'administration des communautés chiffrées

[Nostria 4.1.67](https://github.com/nostria-app/nostria/releases/tag/v4.1.67) est un client social web et de bureau pour Nostr. Il s'appuie sur les groupes gérés par relais expérimentaux [NIP-29](/fr/topics/nip-29/) (groupes gérés par relais) et les communautés chiffrées Concord introduits en 4.1.53, en ajoutant la dissolution de communauté, l'administration de l'icône et de la bannière, les téléversements de photos chiffrés avec aperçus compressés, un sélecteur de réactions complet, et une disposition à double volet qui garde une communauté ouverte pendant que l'utilisateur lit des notes ou des articles. La version ajoute aussi la messagerie filée et un hub combiné pour les chats publics, de groupe et privés.

### Amber 6.4.0 rend explicite chaque décision de signature groupée

[Amber 6.4.0](https://github.com/greenart7c3/Amber/releases/tag/v6.4.0) est un signataire Android qui garde les clés privées Nostr séparées des applications demandant des signatures. Son écran multi-requêtes repensé fournit des contrôles Approuver et Refuser pour chaque requête et chaque groupe, remplaçant le flux précédent de sélection et confirmation. Les requêtes refusées envoyées via l'interface bunker relayée d'Amber reçoivent désormais des réponses d'erreur appropriées, de sorte que le client demandeur peut distinguer un rejet d'un signataire bloqué.

La [source étiquetée d'Amber](https://github.com/greenart7c3/Amber/tree/v6.4.0) ajoute aussi des libellés localisés et lisibles par un humain pour 113 kinds d'événements supplémentaires dans chaque locale livrée. Les ajouts couvrent les événements de groupe Concord, les marque-pages de dépôt Git NIP-51, et les événements de présence de salon NIP-53, donnant aux utilisateurs plus de contexte sur des données inconnues avant d'approuver une signature. Un garde de map concurrente corrige aussi un crash d'abonnement au relais qui pouvait produire une `NegativeArraySizeException`.

### Safebox Acorn sépare un composant de récupération portable de l'application web

[Safebox Acorn](https://github.com/trbouma/safebox-acorn) est un composant Python autonome et une interface en ligne de commande pour sauvegarder des clés, des fonds et des enregistrements contrôlés par l'utilisateur avec un état adossé à Nostr. Extraire Acorn de l'application web Safebox plus large permet à un autre projet Python d'installer le runtime et d'utiliser ses helpers de clé, profil Nostr, relais, enregistrement, Cashu, Lightning et cryptographiques sans prendre l'interface web. Ses primitives actuelles de protection d'enregistrement peuvent générer une clé fraîche de 256 bits, en dériver une à partir d'entropie fournie séparément, et encoder la clé exacte comme phrase de récupération de 24 mots avec somme de contrôle.

Le [guide de récupération et de continuité](https://trbouma.github.io/safebox-acorn/recovery-and-continuity/) du projet présente Acorn comme le composant protocolaire remplaçable à l'intérieur d'un Safebox domestique ou communautaire. La conception garde l'état chiffré disponible via un relais local et des répliques indépendantes pour que la récupération ne dépende pas d'un seul appareil, application, relais, mint ou fournisseur de service. La documentation est prudente sur la frontière actuelle : le chiffrement des enregistrements protégés reste en conception, de sorte que les applications ne devraient pas faire dépendre les enregistrements de la nouvelle clé de protection d'enregistrement tant que ce profil n'a pas été implémenté et revu.


## Versions

### Mostro Core 0.14.2 modifie l'enveloppe de chat chiffré

[Mostro Core](https://github.com/MostroP2P/mostro-core) est la bibliothèque Rust de types partagés et de fonctions pair-à-pair utilisée par le daemon d'échange Mostro et ses clients. La [version 0.14.2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.2) remplace les messages de chat gift wrap par des enveloppes de kind 14 qui utilisent des clés de chiffrement de conversation et de signature distinctes dérivées du secret partagé des pairs. Le nouveau lecteur valide l'auteur, la signature, le destinataire, l'horodatage et la taille du contenu, tandis que les helpers gift wrap hérités restent disponibles pour que les clients puissent lire les deux formats pendant la migration.

### Mostro 0.18.1 amorce un chemin d'escrow Cashu et durcit le daemon

[Mostro](https://github.com/MostroP2P/mostro) est un daemon d'échange Lightning pair-à-pair qui coordonne les ordres via Nostr. La [version 0.18.1](https://github.com/MostroP2P/mostro/releases/tag/v0.18.1) pose les bases d'un backend d'escrow Cashu, incluant configuration, helpers de base de données, intégration mint, câblage au démarrage et la première action de verrouillage. Il peut aussi utiliser des prix annoncés par un nœud de confiance sur Nostr et annonce des exigences de preuve de travail pour le premier contact dans son événement info remplaçable. La version met à jour sa dépendance Nostr pour une correction de déni de service NIP-44, retire les clés privées des journaux de session de restauration, rejette les messages d'annulation coopérative non autorisés, durcit les requêtes LNURL contre la falsification de requête côté serveur et les blocages, valide les factures de paiement, et rétablit les abonnements aux factures en attente après un redémarrage.

### LaWallet NWC 2.3.0 ajoute les notifications Nostr et les reçus de zap

[LaWallet NWC](https://github.com/lawalletio/lawallet-nwc) est une plateforme Lightning Address open source qui connecte les portefeuilles via [Nostr Wallet Connect](/fr/topics/nip-47/). La [version 2.3.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.3.0) permet à chaque portefeuille d'envoyer des notifications reçues et transférées comme événements Nostr configurables, incluant un tag `p` destinataire, des relais sélectionnés, un contenu modélisé, et un chiffrement [NIP-44](/fr/topics/nip-44/) optionnel ; les nouvelles tentatives réutilisent le même ID d'événement signé. Il accepte aussi les requêtes de zap et publie des reçus signés [NIP-57](/fr/topics/nip-57/) de kind 9735 après règlement, tandis qu'une nouvelle vue de capacité d'adresse indique si l'adresse résolue prend en charge NIP-05, NIP-57 et les protocoles Lightning Address associés.

### nostr-double-ratchet TypeScript 0.0.166 lie les invitations publiques aux clés de session

[nostr-double-ratchet](https://github.com/irislib/nostr-double-ratchet) fournit des primitives TypeScript et Rust pour la messagerie directe et de groupe chiffrée de bout en bout via des relais Nostr. [TypeScript 0.0.166](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.166) exige qu'une réponse d'invitation prouve la possession de sa clé de session, empêchant une invitation publique réutilisable de lier une identité Nostr à la session d'une autre partie. La version rejette aussi les champs rumor malformés et resserre la validation des charges utiles ; les sessions existantes continuent de fonctionner, mais un inviteur mis à jour rejette les réponses sans preuve des invités plus anciens.

### cln-nip47 0.2.0 étend et isole les requêtes NWC

[cln-nip47](https://github.com/daywalker90/cln-nip47) est un plugin Core Lightning qui expose un nœud aux portefeuilles via [Nostr Wallet Connect](/fr/topics/nip-47/). La [version 0.2.0](https://github.com/daywalker90/cln-nip47/releases/tag/v0.2.0) ajoute des méthodes NWC pour créer, annuler et régler des factures en attente plus une notification `hold_invoice_accepted`, et annonce l'ensemble de méthodes que le nœud connecté prend réellement en charge. Les réponses de liste de transactions s'arrêtent maintenant à 500 entrées et environ 128 kB, les événements de requête sont dédupliqués par ID d'événement, et l'échec de notification d'un client n'empêche plus la livraison aux autres clients. La version retire aussi les deux méthodes multi-paiement qui ne font plus partie de la spécification NWC.

### ClipRelay 0.1.3 rétablit les connexions relais et signataire après les périodes d'inactivité

[ClipRelay](https://github.com/tajava2006/cliprelay) synchronise le presse-papiers d'un utilisateur entre appareils via des relais Nostr, en chiffrant le contenu vers la même identité avec [NIP-44](/fr/topics/nip-44/). Les versions [desktop](https://github.com/tajava2006/cliprelay/releases/tag/desktop/v0.1.3) et [Android](https://github.com/tajava2006/cliprelay/releases/tag/android/v0.1.3) 0.1.3 correspondantes ajoutent une zone de texte pour envoyer du texte saisi directement vers le presse-papiers d'un autre appareil. Elles testent aussi la vivacité avec de vrais allers-retours relais après des périodes d'inactivité, en escaladant du réabonnement au remplacement de socket et à un pool de connexions reconstruit, tandis que les appels signataire [NIP-46](/fr/topics/nip-46/) (signature distante relayée) bloqués expirent maintenant et se reconstruisent automatiquement.

### NoorNote 1.3.2 déplace la découverte d'articles dans le graphe social

[NoorNote](https://github.com/77elements/noornote) est un client Nostr pour publications sociales, messages chiffrés, articles longs et autres kinds d'événements sur web, bureau et Android. La [version 1.3.2](https://github.com/77elements/noornote/releases/tag/v1.3.2) remplace son fil d'articles global plat par une découverte tirée des contacts de premier, deuxième et troisième degré, offrant aux lecteurs une chronologie d'articles enracinée dans leur graphe de suivi. Elle regroupe aussi les rafales de messages directs rejoués d'expéditeurs inconnus en une notification continue au lieu de produire une pile de toasts à l'arrivée de l'historique du relais.

### Bray 2.4.0 ajoute un dialecte compact de signature distante

[Bray](https://github.com/forgesworn/bray) est un serveur MCP Nostr qui donne aux agents logiciels et aux personnes des outils pour l'accès aux relais, l'identité, la publication et la signature distante. La [version 2.4.0](https://github.com/forgesworn/bray/releases/tag/v2.4.0) accepte une requête de signature dont l'événement est un objet ainsi que la forme stringifiée utilisée par [NIP-46](/fr/topics/nip-46/), et ajoute `sign_event_compact`, qui ne renvoie que l'ID d'événement, la signature, la pubkey et l'horodatage. Ce format de requête et de réponse plus petit réduit l'utilisation mémoire pour les signataires matériels contraints, tandis que le flux standard `sign_event` reste inchangé et les deux dialectes produisent une signature sur l'ID de l'événement reçu.


## Nouvelles découvertes

### Pact apporte des liens d'agents mutuellement consentis à Nostr

[Pact](https://github.com/bobodread876/pact), nouvellement découvert cette semaine, est une couche relationnelle précoce pour agents logiciels construite sur MATE.md et un transport brouillon NIP-BD. Ses liens signés et mutuellement consentis sont détenus par les propres clés des agents et peuvent être publiés sur Nostr, tandis que les liens privés utilisent le gift wrap [NIP-59](/fr/topics/nip-59/). Le monorepo inclut un serveur MCP, un SDK TypeScript, un client en ligne de commande, un daemon auto-hébergeable et une interface web. Sa dernière activité de dépôt précède la fenêtre hebdomadaire de ce numéro, il s'agit donc d'une note de découverte plutôt que d'une affirmation de nouvelle version.


## Changements non publiés

### nostrord garde le mutisme de groupe synchronisé entre appareils

[nostrord](https://github.com/nostrord/nostrord) est un client multiplateforme pour communautés gérées par relais. La [PR #250](https://github.com/nostrord/nostrord/pull/250) stocke les choix de mutisme par groupe de chaque compte dans un événement auto-chiffré [NIP-78](/fr/topics/nip-78/) (données spécifiques à l'application) de kind `30078`, de sorte qu'un réglage fait sur un appareil peut suivre l'utilisateur sur un autre sans révéler la liste de groupes au relais. L'enregistrement remplaçable utilise l'ordre du plus récent événement, écoute les changements en direct, et annule l'interface en cas d'échec de signature ou de publication au lieu de laisser l'état local désynchronisé. Les groupes muets cessent aussi de contribuer aux totaux de non-lus visibles tout en conservant leur position de non-lu pour la prochaine visite.

### Amethyst complète le cycle de vie des invitations Concord

[Amethyst](https://github.com/vitorpamplona/amethyst) est un client Nostr Android dont le support de communautés chiffrées implémente le protocole Concord. La [PR #3888](https://github.com/vitorpamplona/amethyst/pull/3888) permet aux liens d'invitation de survivre à un refondage de communauté en réémettant leurs bundles aux mêmes coordonnées adressables, tandis qu'une vérification de bannissement empêche un membre retiré d'utiliser ce chemin de récupération. Elle implémente aussi la liste d'invitations chiffrée CORD-05 sur l'application et le client en ligne de commande `amy`, ajoute des tombstones de révocation par lien, et exige la confirmation du relais avant de supprimer la seule clé de signature stockée pouvant retirer un lien. Le même travail donne à `amy` les chemins de livraison de clé de contrôle, refondage, rekeying et récupération de membres isolés nécessaires pour suivre les époques communautaires ultérieures.

### Buzz transporte l'apparence de chaque communauté entre bureau et mobile

[Buzz](https://github.com/block/buzz) est un espace de travail communautaire basé sur Nostr avec clients bureau et mobile. Les PR desktop fusionnées [PR #3653](https://github.com/block/buzz/pull/3653) et mobile [PR #3767](https://github.com/block/buzz/pull/3767) stockent le thème, l'accent et le choix de mode système de chaque communauté comme enregistrement chiffré NIP-78 sur le relais de cette communauté. Les deux clients partagent la même charge utile versionnée et conservent des caches locaux propres à l'identité, de sorte que changer de communauté ou de compte ne peut pas appliquer la mauvaise apparence pendant que le relais est indisponible. L'ordre de remplacement, les écritures protégées et le réabonnement après une connexion fermée permettent aux deux clients de converger à nouveau après reconnexion.

[Buzz Desktop 0.5.10](https://github.com/block/buzz/releases/tag/desktop-v0.5.10) a suivi avant la date limite du numéro avec une passe de performance et de fiabilité. Il supprime les régressions introduites après 0.5.9, accélère le chargement des canaux, borne la rétention initiale de la chronologie, fusionne la persistance de l'état de lecture, préserve les chronologies de canaux fraîches, et empêche le worker d'ingestion relais de crasher sur les réactions aux événements de projet. Il ajoute aussi l'envoi d'un message de fil vers un canal et restreint la recherche desktop à la portée prévue.


## Mises à jour des NIP et travail de spécification du protocole

### NIPs

La [PR NIPs #2435](https://github.com/nostr-protocol/nips/pull/2435) est un amendement ouvert à [NIP-34](/fr/topics/nip-34/) (collaboration sur dépôts git via Nostr). Elle ajoute un tag `b` optionnel à un événement de pull request pour que l'auteur puisse nommer une branche cible autre que la branche par défaut du dépôt. La proposition correspond à un support déjà implémenté dans ngit et GitWorkshop, mais n'est pas entrée dans la spécification.

La [PR NIPs #2434](https://github.com/nostr-protocol/nips/pull/2434) est une proposition ouverte pour des clés d'identité post-quantiques. Elle dérive des clés de chiffrement et de signature post-quantiques aux côtés de la clé secp256k1 existante à partir d'une seed de dérivation de clé mnémonique NIP-06, puis lie les clés publiques à l'identité Nostr avec une attestation de kind `10203`. Le brouillon limite sa revendication à la protection de la confidentialité des messages antérieurs si secp256k1 est un jour cassé ; il ne remplace pas les signatures d'événements actuelles.

La [PR NIPs #2431](https://github.com/nostr-protocol/nips/pull/2431) est un amendement ouvert à [NIP-07](/fr/topics/nip-07/) (signataires de navigateur). Un client pourrait joindre la pubkey qu'il attend aux requêtes de signature ou de chiffrement, exigeant que le signataire utilise ce compte ou rejette l'appel. Cela empêcherait une page de continuer silencieusement sous une identité différente après que l'utilisateur change de compte dans le signataire.

La [PR NIPs #1813](https://github.com/nostr-protocol/nips/pull/1813) reste une proposition double-ratchet ouverte après un travail substantiel pendant la fenêtre. Elle spécifie des conversations chiffrées à secret avant avec des clés qui avancent avec les messages, avec une implémentation déjà disponible dans la bibliothèque nostr-double-ratchet et Iris. C'est encore un brouillon, pas un NIP fusionné.

La [PR NIPs #2433](https://github.com/nostr-protocol/nips/pull/2433) s'est ouverte et fermée sans fusion pendant la fenêtre. Elle proposait de clarifier les erreurs de relais NIP-42 pour que `auth-required` signifierait qu'une autre authentification pourrait changer le résultat, tandis que `restricted` signifierait qu'elle ne le pourrait pas. La distinction concernait des connexions authentifiées pour une clé mais encore sans autorisation pour une autre ; le statut fermé signifie que la formulation n'est pas entrée dans la spécification.

La [PR NIPs #2378](https://github.com/nostr-protocol/nips/pull/2378), couverte précédemment alors qu'elle était encore proposée, s'est maintenant fermée sans fusion. Ses événements proposés de passeports d'agent, découverte, tâche, marketplace, facture et connexion restent donc en dehors de l'ensemble des NIP.

Le [commit NIPs 656cecc](https://github.com/nostr-protocol/nips/commit/656cecc7c0a815b6a2b218d3b5d6f078b3f4dbab) a fusionné une correction documentation-only de NIP-29. Il ajoute un tag `previous` à l'exemple de métadonnées de groupe, montrant comment un événement de remplacement peut identifier l'événement qu'il supplante. Cela clarifie un exemple et n'introduit pas de nouvelle fonctionnalité protocolaire.

### Concord et CORDs

La [PR CORD #18](https://github.com/concord-protocol/concord/pull/18) fragmenterait les listes de communauté chiffrées sur des événements de kind `33302`, supprimerait la limite de 50 adhésions, et élaguerait les entrées retirées pour rester dans les limites des relais. Deux autres propositions ouvertes ajoutent des [localisateurs de mention privée](https://github.com/concord-protocol/concord/pull/16) et un [signal de pause](https://github.com/concord-protocol/concord/pull/17) qui suspend le chat sans jeter les messages.

La [PR CORD-02 #15](https://github.com/concord-protocol/concord/pull/15) a fusionné le 6 août et restreint les écritures au plan de contrôle d'une communauté. Les propriétaires et le staff détiennent un nouveau secret de signature `control_root`, tandis que tous les membres conservent la pubkey dérivée et la clé de lecture nécessaires pour vérifier et déchiffrer l'état de modération. La clé d'écriture est une barrière anti-spam, pas un substitut aux signatures d'acteur internes et aux vérifications de roster qui établissent l'autorité.

La [PR CORD #12](https://github.com/concord-protocol/concord/pull/12), couverte précédemment comme brouillon ouvert, s'est maintenant fermée sans fusion. Sa portion plan de contrôle a été supplantée par l'amendement CORD-02 fusionné plus étroit ci-dessus, tandis que les canaux à écriture restreinte et les autres éléments du brouillon ne sont pas entrés dans la spécification.

## Analyse approfondie de NIP

### Demandes de suppression d'événements (NIP-09)

[NIP-09](/fr/topics/nip-09/) (demandes de suppression d'événements), défini par la [spécification principale](https://github.com/nostr-protocol/nips/blob/master/09.md), donne à l'auteur d'un événement un moyen signé de demander aux relais et aux clients d'arrêter de servir un ou plusieurs de ses événements. Cela n'efface pas chaque copie. Cela transporte l'intention de l'auteur via le même réseau de relais qui a distribué l'événement original.

La requête est un événement signé ordinaire de kind `5`. Ses tags contiennent une ou plusieurs références `e` vers des ID d'événements spécifiques ou des références `a` vers des coordonnées d'événements adressables, et les [règles de tags NIP-09](https://github.com/nostr-protocol/nips/blob/master/09.md#event-deletion-request) indiquent qu'il devrait inclure un tag `k` pour chaque kind d'événement référencé. Le `content` optionnel peut expliquer la raison. Pour une référence `a`, un relais devrait retirer chaque version à cette coordonnée dont l'horodatage n'est pas postérieur au `created_at` de la requête, ce qui empêche une ancienne demande de suppression de supprimer un remplacement ultérieur.

[L'auteur est la frontière de sécurité](https://github.com/nostr-protocol/nips/blob/master/09.md#relay-behavior). Un relais devrait arrêter de publier un événement référencé seulement lorsque sa `pubkey` correspond à la `pubkey` de la demande de suppression, et un client doit effectuer cette vérification avant de masquer un événement. Un relais peut ne pas posséder l'événement référencé et donc être incapable de valider la relation lors de l'acceptation de la requête, de sorte que les clients ne peuvent pas traiter l'acceptation par le relais comme preuve que la suppression était autorisée. La spécification demande aussi aux relais de conserver la requête de kind `5` parce qu'un autre client peut déjà détenir l'événement original et rencontrer la requête plus tard.

Voici un [événement signé de kind `5`](https://primal.net/e/6f39fd3d0d593d97dd093f21fabe8f78895579d6979a6ecf14e169bd85bb0943) :

```json
{
  "id": "6f39fd3d0d593d97dd093f21fabe8f78895579d6979a6ecf14e169bd85bb0943",
  "pubkey": "5877220aaae6e54a6f974602d5995c0fe24a3ea7ddabd8644bec795b9da00743",
  "created_at": 1786465675,
  "kind": 5,
  "tags": [
    ["e", "f3d47f8b813928c5baf7ac993846be0220dc37a2e7c7b128fb49a4b92711f131"],
    ["k", "30091"],
    ["a", "30091:5877220aaae6e54a6f974602d5995c0fe24a3ea7ddabd8644bec795b9da00743:survey:0ad5cebc-608b-47d7-97fd-9e6c47787199"],
    ["t", "nostr-survey"]
  ],
  "content": "Public survey summary deleted during privacy refresh",
  "sig": "846be83b038dc5f91af0c9d03a4ac81aff9bc4cfde7d85c849fa2fdae890f75cc444a4072f45aa18883b0b3871e15381b220182d6e366892f0c9c6f9c0557244"
}
```

La suppression reste une politique coopérative, pas une révocation d'un objet signé. Un relais, cache, capture d'écran ou client hors ligne peut conserver les octets originaux, et supprimer la requête de kind `5` elle-même ne l'annule pas. Les clients peuvent masquer la cible, la marquer comme désavouée, ou afficher la raison de la requête, mais devraient informer les utilisateurs qu'une suppression universelle ne peut pas être garantie. Cela diffère de [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md) (expiration d'événement), où un tag `expiration` demande aux relais d'arrêter de stocker un événement après un moment choisi lors de la publication. NIP-09 gère une décision ultérieure de l'auteur et peut pointer vers des événements déjà distribués.

Les implémentations actuelles appliquent cette politique à différentes couches. La [PR Divine #6623](https://github.com/divinevideo/divine-mobile/pull/6623) retire les vidéos supprimées du magasin d'événements du client, la [PR strfry #251](https://github.com/hoytech/strfry/pull/251) étend les demandes de suppression valides aux destinataires gift wrap, et [Amethyst](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md) déclare le support NIP-09 dans son client. Le [client de groupe de nostrord](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/network/NostrGroupClient.kt) fournit un autre chemin d'implémentation actuel.

### Signalement (NIP-56)

[NIP-56](/fr/topics/nip-56/) (événements de signalement), défini par la [spécification principale](https://github.com/nostr-protocol/nips/blob/master/56.md), standardise un signalement signé sur un compte, un événement ou un blob référencé. Il sépare le signal de signalement de la décision de modération, permettant à chaque client ou relais de choisir quels rapporteurs il fait confiance et quelle réponse convient à sa politique.

Un signalement utilise le kind `1984` et doit identifier le compte signalé dans un tag `p`. Signaler une note exige aussi un tag `e` pour l'ID d'événement. La troisième valeur du tag porte l'une des catégories spécifiées : `nudity`, `malware`, `profanity`, `illegal`, `spam`, `impersonation`, ou `other`. Un signalement sur un blob peut utiliser son hachage dans un tag `x`, un tag `e` pour l'événement qui a référencé le blob, et un tag `server` optionnel pour un emplacement. Les tags `L` et `l` optionnels de [NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md) (étiquetage) peuvent ajouter un libellé avec espace de noms lorsque la liste de catégories fixe n'est pas assez précise.

[L'événement prouve seulement qu'une clé a fait une allégation](https://github.com/nostr-protocol/nips/blob/master/56.md#reporting). Le contenu signalé ne devient pas faux, illégal ou supprimable simplement parce qu'un kind `1984` valide existe, et un relais ouvert ne peut pas compter en toute sécurité des signalements anonymes comme des votes. La spécification déconseille la modération automatique par relais parce que les signalements sont faciles à manipuler, tout en permettant aux administrateurs de relais d'agir sur les signalements de modérateurs en qui ils ont déjà confiance. Un client peut au contraire pondérer les signalements via le graphe social d'un utilisateur, par exemple en floutant le contenu après que plusieurs contacts de confiance signalent le même compte.

Voici un [événement signé de kind `1984`](https://primal.net/e/17301ea66066d34af9ba0b6957ed9d9d8854b9436939e682e21e7a5a8768e4b2) :

```json
{
  "id": "17301ea66066d34af9ba0b6957ed9d9d8854b9436939e682e21e7a5a8768e4b2",
  "pubkey": "1ff02fb5cdc633c1be55368ab655490ec25d2f5dc2e364d4703bc3196d99eab1",
  "created_at": 1786465319,
  "kind": 1984,
  "tags": [
    ["p", "3a72b02cc05ee07310dc580874b6a9ca8271c6518b90655bd2e98003c9601e68", "impersonation"]
  ],
  "content": "",
  "sig": "6362e415410feb19e0505654a4660e8456b6b2aec5ae39173a0429a6a8e5fa1381c9488198ca2982db43ee8198af056f2a25537705c763784062056d0ab2eb1a"
}
```

[NIP-56 et NIP-09 résolvent des problèmes différents](https://github.com/nostr-protocol/nips/tree/master). Un signalement de kind `1984` peut cibler le compte ou l'événement de quelqu'un d'autre, mais ne confère aucune autorité de suppression. Une requête de kind `5` exprime l'intention de l'auteur original et n'est valide que contre les propres événements de cet auteur. Aucun ne garantit la suppression : NIP-56 délède délibérément l'action à la politique de modération locale, tandis que NIP-09 dépend des relais et des clients honorant une requête authentifiée.

Les implémentations exposent ces choix dans différents produits. La [PR Divine #6591](https://github.com/divinevideo/divine-mobile/pull/6591) corrige la livraison de signalement dans un client de vidéo courte, la [PR Conduit #250](https://github.com/Conduit-BTC/conduit-mono/pull/250) lit les signalements comme contexte borné pour les participants de marketplace, et le [module NIP-56 de nostrord](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/nostr/Nip56.kt) publie et traite les événements de signalement. [Amethyst](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md#nip-support) liste aussi le support NIP-56 actuel.


---

Envoyez un DM NIP-17 pour partager un projet ou une actualité via le [projet Nostr Compass](https://github.com/andotherstuff/nostr-compass).
