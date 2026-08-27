---
title: 'Nostr Compass #29'
date: 2026-07-01
publishDate: 2026-07-01
translationOf: /en/newsletters/2026-07-01-newsletter.md
translationDate: 2026-08-27
draft: false
type: newsletters
---

Bon retour sur Nostr Compass, votre guide hebdomadaire de Nostr.

**Cette semaine :** [FIPS v0.4.0](#fips-v040-livre-un-transport-mixnet-nym-la-découverte-mdns-et-une-refonte-du-plan-de-données) livre un transport mixnet Nym, la découverte LAN mDNS facultative, un renouvellement de clés sans interruption malgré les pertes et une refonte du plan de données, compatible sur le fil avec la v0.3.0. [Whitenoise Linux](#whitenoise-linux-se-présente-comme-client-marmot-de-bureau) se présente comme client Marmot de bureau en Rust et Slint, avec une proposition de protocole visant à déplacer les effets de message vers un événement dédié de kind 9. [CustID v0.1.10-beta](#custid-se-lance-comme-coffre-didentités-mobile-avec-nip-46-et-flux-de-défi-nfc) se lance comme coffre d'identités mobile adossé au matériel, qui agit comme signataire distant NIP-46 et répond aux défis d'accès physique par NFC. [myco](#myco-lance-le-partage-nsite-pair-à-pair-sur-le-mesh-fips) lance le partage nsite pair à pair sur le mesh FIPS avec un nouveau transport BLE L2CAP dans la v0.1.0. [Nostr Codex Phone](#nostr-codex-phone-se-lance-comme-surface-de-contrôle-mobile-pour-un-worker-codex-local-via-nostr) se lance comme surface de contrôle Android pour un assistant de programmation Codex local via des DM Nostr chiffrés. [La branche non publiée d'Amethyst](#amethyst-construit-une-interface-compatible-nip-89-un-flux-git-repositories-et-une-section-discover-pour-les-napplets) ajoute l'analyse des handlers d'app NIP-89, un flux Git Repositories pour NIP-34 et une section Discover pour les nSites et napplets. [Notedeck](#notedeck-implémente-les-relays-de-synchronisation-privée-nip-37-le-calendrier-nip-52-et-les-commentaires-nip-22) intègre NIP-37, NIP-52 et NIP-22 en une semaine. [Applesauce](#applesauce-publie-12-sous-paquets-dans-une-sortie-coordonnée-62x) publie 12 sous-paquets avec des helpers nbunksec NIP-46 et une mise à niveau du wallet vers Cashu-ts v4. [Meiso v1.4.0](#meiso-v140-livre-des-listes-collaboratives-à-clé-partagée-qui-remplacent-mls-pour-le-partage-de-tâches) livre des listes collaboratives à clé partagée sur le kind adressable 35000. Le dépôt des NIP a fusionné cinq PR, dont un événement Relay Roles, la suppression de la limite de 65 535 octets de NIP-44, la sémantique des forks NIP-34, les métadonnées client NIP-46 et une méthode `signevent` NIP-86. Les analyses approfondies portent sur [NIP-86 (API de gestion des relays)](#analyse-approfondie-de-nip-86-api-de-gestion-des-relays) et [NIP-89 (handlers d'application recommandés)](#analyse-approfondie-de-nip-89-handlers-dapplication-recommandés).

---

## À la une

### FIPS v0.4.0 livre un transport mixnet Nym, la découverte mDNS et une refonte du plan de données

[FIPS](https://github.com/jmcorgan/fips) est un réseau maillé pair à pair privé et auto-organisé pour Nostr, où les nœuds se découvrent et acheminent le trafic sans infrastructure centrale. [FIPS v0.4.0](https://github.com/jmcorgan/fips/releases/tag/v0.4.0) apporte un transport mixnet Nym, la découverte LAN mDNS facultative, une refonte du plan de données, un renouvellement de clés sans interruption malgré les pertes de paquets, une TUI `fipstop` réécrite sur un banc de snapshots de rendu, un plan d'observabilité hors du chemin critique et de nouvelles cibles de packaging apk OpenWrt et flake Nix. Le tout reste compatible sur le fil avec la v0.3.0, afin que les mesh mixtes interopèrent pendant une mise à niveau progressive. Deux nouveaux transports de découverte des pairs structurent cette version. Un nouveau [transport mixnet Nym sortant](https://github.com/jmcorgan/fips/releases/tag/v0.4.0) fait passer le trafic FIPS par un proxy SOCKS5 `nym-socks5-client`, le mêlant au réseau de trafic de couverture de [Nym](https://nymtech.net/) afin que les observateurs au niveau de la liaison ne puissent pas corréler les pairs du mesh qui communiquent. Un répertoire `examples/sidecar-nostr-mixnet-relay/` montre un relay Nostr accessible par une liaison FIPS appairée de bout en bout à travers le mixnet. La découverte LAN mDNS / DNS-SD facultative permet aux nœuds d'une même liaison locale de se trouver sans configuration d'adresse ni STUN, en annonçant et adoptant des pairs via un enregistrement de service standard lorsque `node.discovery.lan.enabled: true`.

Le plan de données a été remanié pour accroître le débit d'un nœud unique. Le chiffrement et le déchiffrement par pair s'exécutent désormais dans des tâches worker dédiées, hors de la boucle de réception, de sorte qu'un pair très actif ne puisse pas sérialiser la cryptographie de tout le nœud. Sous Linux, le chemin d'envoi utilise la generic segmentation offload et, lorsqu'elle est disponible, une socket UDP connectée ; le chemin critique de réception évite les copies de buffer auparavant effectuées pour chaque paquet ; et macOS reçoit un `recvmsg_x` par lots, miroir du traitement `recvmmsg` de Linux introduit en v0.3.0. Toute la surface de lecture `show_*` de `fipsctl` et `fipstop` est maintenant servie depuis un snapshot par tick publié dans un `ArcSwap` sans verrou par la tâche d'acceptation de contrôle, ce qui permet aux requêtes opérateur de répondre rapidement même lorsque la boucle de réception du nœud est occupée. Une nouvelle requête `show_metrics`, limitée aux compteurs et exposée sous `fipsctl stats metrics`, permet le scraping Prometheus sans coût sur le chemin critique.

Le renouvellement de clés des sessions FMP et FSP est désormais sans interruption malgré les pertes et le réordonnancement de paquets dans les deux sens : les frames entrantes s'authentifient contre la session en attente avant que la bascule du bit K ne la promeuve (ainsi, une frame périmée ou usurpée ne peut pas faire dérailler le renouvellement), la retransmission du message 1 est bornée, le heartbeat de lien mort tient compte du renouvellement et les courses d'initialisation simultanée sur les liaisons à forte latence sont désynchronisées par une gigue symétrique. La TUI `fipstop` est reconstruite sur un banc de snapshots de rendu qui vérifie la grille de texte exacte et le style de chaque cellule de toutes les vues à partir de sorties prédéfinies de la socket de contrôle. De nouvelles cibles de packaging accompagnent la version : un `.apk` OpenWrt pour OpenWrt 25+ (construit sans SDK, en réutilisant la compilation croisée `.ipk` et la charge utile du système de fichiers installé) et un `flake.nix` à la racine du projet qui compile depuis les sources les quatre binaires (`fips`, `fipsctl`, `fips-gateway`, `fipstop`) sous Nix/NixOS avec la toolchain épinglée.

### Whitenoise Linux se présente comme client Marmot de bureau

[Whitenoise Linux](https://relay.ngit.dev/npub1ven4zk8xxw873876gx8y9g9l9fazkye9qnwnglcptgvfwxmygscqsxddfh/darkmatter-linux.git) est un client [Marmot](/fr/topics/marmot/) de bureau : messagerie de groupe MLS sur des relays Nostr, empaquetée dans un binaire Rust unique avec une interface Slint qui conserve chaque secret dans un coffre chiffré par mot de passe.

Le fil le plus important de la semaine propose de transporter les effets de message de Whitenoise dans un événement dédié de kind 9 référençant le message parent. Le format actuel ajoute un marqueur tel que `dmfx:sparkle` à la fin du corps du message, ce qui pollue le texte pour tout renderer qui ignore cette convention. Déplacer les effets vers leur propre événement garde le texte propre et ouvre une question de conception à laquelle toute la stack Marmot devra répondre : conventions intégrées au corps ou événements sidecar pour les fonctions enrichies facultatives.

### CustID se lance comme coffre d'identités mobile avec NIP-46 et flux de défi NFC

[CustID v0.1.10-beta](https://zapstore.dev/apps/naddr1qq9rzqtdwfshxwf0wccsygqv94d2qg37755z67q9yjz6q60lcejldsc3ttak83333gjqgyvf3aqpsgqqqyf6w24n0c) est la première bêta publique de CustID, un coffre d'identités mobile construit sur Nostr et le protocole SISTR. CustID stocke plusieurs identités Nostr dans un stockage sécurisé adossé au matériel, agit comme signataire distant [NIP-46](/fr/topics/nip-46/) pour d'autres clients et répond à des défis d'accès physiques et en ligne au moyen de NFC et de codes QR.

La bêta est complète pour le signataire NIP-46 et le flux défi-réponse NFC ; les flux d'accès par preuve à divulgation nulle de connaissance restent un jalon futur. Cette version supprime aussi la couche keep-alive [NIP-65](/fr/topics/nip-65/) en arrière-plan, qui ouvrait une WebSocket par profil et par relay de lecture pour ingérer des kinds que le client rejetait aussitôt. Seules les sockets NIP-46 qui transportent les notifications de demandes de signature restent maintenant ouvertes en arrière-plan, correction qui rend viable l'utilisation de CustID comme bunker pour d'autres clients sur un téléphone.

### myco lance le partage nsite pair à pair sur le mesh FIPS

[myco v0.1.0](https://github.com/Origami74/myco/releases/tag/v0.1.0) a ouvert cette semaine, le 27 juin, et atteint la v0.1.0 le 1er juillet. myco est une app Android en Rust qui installe des apps venues des personnes autour de vous : partage [nsite](/fr/topics/nip-5a/) pair à pair sur un mesh FIPS, avec tout transport pris en charge par le mesh (UDP, TCP, Tor, Bluetooth), entièrement hors ligne. La conception associe directement FIPS comme substrat de transport au format d'événement de site statique de NIP-5A comme charge utile, ce qui permet à une app distribuée comme nsite de passer d'un pair du mesh à l'autre sans dépendre de relays ni de HTTP.

La v0.1.0 ajoute un chemin radio Bluetooth L2CAP afin que deux téléphones équipés de FIPS puissent s'appairer par BLE sans aucun réseau, ainsi qu'un speedtest par pair et le partage déclenché par NFC depuis le bottom sheet Circle de l'app. myco est aussi publié sur Zapstore pour installation directe.

### Nostr Codex Phone se lance comme surface de contrôle mobile pour un worker Codex local via Nostr

[Nostr Codex Phone v0.1.122](https://github.com/tidley/nostr-codex-phone) se lance cette semaine comme client Android contrôlant un worker local de l'assistant de programmation Codex via des messages directs Nostr chiffrés. L'app prend en charge plusieurs sessions de dépôt, la transcription vocale, les sessions worker routées, l'upload de médias Blossom et les réponses parlées facultatives, afin qu'un développeur exécutant chez lui un worker Codex puisse envoyer des demandes depuis son téléphone partout où celui-ci accède à des relays.

Le projet est directement apparenté à [CodeDeck](/en/newsletters/2026-06-24-newsletter/#codedeck-remote-agentic-coding-over-nostr), lancé dans le #28. Tous deux placent les workflows de programmation agentique sur le transport Nostr avec des DM chiffrés, et traitent Nostr comme couche d'appairage et de messagerie permettant à un téléphone d'atteindre un worker à domicile sans ouvrir de brèche dans le réseau. Nostr comme plan de contrôle d'agents locaux devient un modèle établi.

### Coop Mobile publie ses premiers builds versionnés

[Coop Mobile v0.2.1](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.1) et [v0.2.2](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.2) sont sortis cette semaine comme premiers builds versionnés de Coop Mobile, un client de messages directs chiffrés [NIP-17](/fr/topics/nip-17/) pour Android. Les deux versions renforcent la résistance aux crashes lors de l'analyse des messages et du traitement des QR, et effacent toutes les données stockées à la déconnexion.

### Amethyst construit une interface compatible NIP-89, un flux Git Repositories et une section Discover pour les napplets

La branche principale d'[Amethyst](https://github.com/vitorpamplona/amethyst) a construit plusieurs nouvelles surfaces cette semaine. Un [flux Git Repositories](https://github.com/vitorpamplona/amethyst/pull/3406) transforme les dépôts [NIP-34](/fr/topics/nip-34/) en catégorie de timeline Android consultable et filtrable par communauté et auteur, avec un [navigateur git smart-HTTP](https://github.com/vitorpamplona/amethyst/pull/3415) qui lit le contenu et les commits du dépôt sans quitter l'app. L'hôte de napplets reçoit une [section Discover](https://github.com/vitorpamplona/amethyst/pull/3409) qui répertorie des apps web sélectionnées ainsi que les nSites et napplets suivis, à partir des événements de handler [NIP-89](/fr/topics/nip-89/) et des événements de site [NIP-5A](/fr/topics/nip-5a/). L'affichage des notes [révèle désormais quelle app Nostr a créé un événement](https://github.com/vitorpamplona/amethyst/pull/3422) grâce aux tags NIP-89. Côté synchronisation, la [prise en charge de la negentropy NIP-77](https://github.com/vitorpamplona/amethyst/pull/3434) apporte la réconciliation en streaming et un fenêtrage automatique de `created_at` pour contourner les plafonds de résultats des relays, réduisant la bande passante nécessaire pour garder de grands ensembles locaux d'événements synchronisés avec un relay.

### Buzz v0.3.38 renforce la surface d'attaque des relays et ajoute la sélection de modèle indépendante du fournisseur

[Buzz v0.3.38](https://github.com/block/buzz/releases/tag/v0.3.38) renforce la [surface d'attaque des relays](https://github.com/block/buzz/pull/1369) exposée lorsque Buzz publie des personas, équipes, agents gérés et attestations de propriétaire NIP-OA comme événements Nostr signés. Un relay Buzz constitue un registre public des identités Nostr de l'équipe et de leur état ; cette version durcit la validation des entrées et la protection contre le replay sur les kinds d'événement bien connus définis par Buzz. Elle généralise aussi la sélection de modèle afin qu'une équipe Buzz puisse choisir tout fournisseur pour lequel Buzz possède un adapter, dont un nouveau backend Databricks AI Gateway v2.

### Notedeck implémente les relays de synchronisation privée NIP-37, le calendrier NIP-52 et les commentaires NIP-22

[Notedeck](https://github.com/damus-io/notedeck), le client de bureau natif en Rust de l'équipe Damus, a intégré trois protocoles en une semaine. Les relays de synchronisation privée persistent maintenant sous forme d'une liste [NIP-37](/fr/topics/nip-37/) de kind `10013`, séparant l'ensemble des relays de contenu privé de l'utilisateur de son outbox NIP-65 public. Le panneau de calendrier `horizon` lit les événements [NIP-52](/fr/topics/nip-52/) depuis nostrdb et reçoit une nouvelle disposition à trois volets. Le panneau `headway` ajoute un modèle d'événement de commentaire [NIP-22](/fr/topics/nip-22/) sur le kind `1111`, celui que NIP-22 définit pour la surface unifiée de commentaires remplaçant les fils de réponse NIP-10.

### Applesauce publie 12 sous-paquets dans une sortie coordonnée 6.2.x

[Applesauce](https://github.com/hzrd149/applesauce), la boîte à outils Nostr modulaire pour signataires, relays, wallets et contenu, a réalisé une [sortie 6.2.x coordonnée](https://github.com/hzrd149/applesauce/releases) de ses sous-paquets. Le paquet de signataires reçoit des helpers d'import et d'export `nbunksec`, qui traitent une session bunker [NIP-46](/fr/topics/nip-46/) comme un artefact portable entre clients. Le paquet wallet met à niveau ses bindings [Cashu](/fr/topics/nip-60/) vers `@cashu/cashu-ts` v4, où les montants des proofs deviennent des objets valeur `Amount` et où l'API de décodage des tokens change.

---

## Versions taguées

### mostro-core v0.14.0

[mostro-core v0.14.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.0) apporte la prochaine itération du protocole au réseau de commerce fiat P2P [Mostro](/fr/topics/nip-69/). La version suit la [v0.13.2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.2) et accompagne [mostro-cli v0.16.0](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.16.0), qui adopte le nouveau core. Trois PR fusionnées ont rejoint le dépôt core cette semaine ; la stack environnante (daemon mostro et Mostro mobile) suit la v0.14.0 du crate de types partagé.

### ngit v2.6.1

[ngit v2.6.1](https://github.com/DanConwayDev/ngit-cli), le CLI git-over-nostr canonique pour les dépôts [NIP-34](/fr/topics/nip-34/), implémente la [sémantique de fork GRASP-06 de NIP-34](https://github.com/nostr-protocol/nips/pull/2395) fusionnée cette semaine, qui remplace le tag `personal-fork` par un tag `u` sur les événements d'état de dépôt.

### mesh-llm v0.72.0 et v0.72.1

[mesh-llm](https://github.com/Mesh-LLM/mesh-llm), le composant d'inférence de la stack ContextVM qui exécute des LLM open source derrière une surface JSON-RPC adressable via Nostr, a publié les [v0.72.0](https://github.com/Mesh-LLM/mesh-llm/releases/tag/v0.72.0) et [v0.72.1](https://github.com/Mesh-LLM/mesh-llm/releases/tag/v0.72.1), avec un correctif pour un crash du batching sur les grands prompts uniques et une migration du pont MCP hors de helpers dépréciés.

### Meiso v1.4.0 livre des listes collaboratives à clé partagée qui remplacent MLS pour le partage de tâches

[Meiso v1.4.0](https://github.com/higedamc/meiso/releases/tag/v1.4.0) introduit un modèle de listes collaboratives à clé partagée qui remplace l'ancien partage de tâches fondé sur MLS par une conception plus simple d'événements adressables. Chaque liste partagée génère une clé Nostr dédiée distribuée aux membres ; les tâches sont des événements adressables de kind `35000`, indexés par `d=task-id`, au contenu auto-chiffré avec [NIP-44](/fr/topics/nip-44/) ; et les relays appliquent Last-Write-Wins pour chaque tâche. La conception abandonne la forward secrecy et la sécurité post-compromission de MLS en échange d'une implémentation client plus simple et d'une résolution des conflits au niveau du relay.

### Cordn 0.3.2

[Cordn 0.3.2](https://github.com/Cordn-msg/cordn) livre une branche « more-private-coordinator » qui supprime les pubkeys éphémères des expéditeurs lors de la publication des messages de groupe et durcit le flux de demande d'adhésion contre les nouvelles demandes périmées. Cordn est la stack de messagerie fondée sur MLS présentée dans [le lancement de Cordn Ad-hoc CVM du #28](/en/newsletters/2026-06-24-newsletter/#cordn-ad-hoc-cvm-a-browser-based-mls-coordinator) ; cette version constitue la mise à jour correspondante côté coordinateur.

---

## Changements non publiés

### diVine pousse 108 PR fusionnées de finitions après lancement

[diVine](https://github.com/divinevideo/divine-mobile), le client de vidéos courtes en boucle qui ressuscite Vine, traverse une importante vague de finitions après lancement. Le travail visible sur Nostr cette semaine est une passe de stabilité du flux de connexion [NIP-46](/fr/topics/nip-46/) qui fait migrer les échecs `nostrconnect://` vers des codes de motif structurés.

### Zap Cooking poursuit le correctif NIP-46 transversal et la refonte du compositeur

[Zap Cooking](https://github.com/zapcooking/frontend) est un client Nostr de partage de recettes, où celles-ci sont publiées comme événements Nostr long-form. Le travail de la semaine poursuit le correctif [NIP-46](/fr/topics/nip-46/) transversal et la refonte du compositeur présentés parmi les changements non publiés du [#28](/en/newsletters/2026-06-24-newsletter/#unreleased-changes).

### Conduit renforce le flux d'annonces et la justesse de la marketplace

[Conduit](https://github.com/Conduit-BTC/conduit-mono) est un monorepo de marketplace comprenant trois apps sur Nostr : marché acheteur, portail marchand et constructeur de boutique. Le travail de la semaine poursuit l'effort de justesse de la marketplace présenté dans [la couverture du lancement du #28](/en/newsletters/2026-06-24-newsletter/#conduit-hardens-the-marketplace-mvp-and-switches-to-its-public-relay-by-default), en s'appuyant sur la vague commerciale [NIP-99](/fr/topics/nip-99/) qui constituait le sujet protocolaire du dernier numéro.

### Pollerama v1.12 à v1.13.1 ajoutent le choix du tag client, des onglets de profil et des limites de profondeur des fils

[Pollerama](https://github.com/formstr-hq/nostr-polls), un client Nostr Android centré sur les sondages et les notes avec une forte couche de découverte par web of trust, a publié les v1.12.0, v1.13.0 et v1.13.1 sur Zapstore cette semaine. Les utilisateurs peuvent désormais choisir le tag client joint aux notes et sondages qu'ils créent, à partir d'une liste prédéfinie ou en saisissant le leur. Les chaînes de commentaires et de réponses très imbriquées s'arrêtent maintenant après quelques niveaux et renvoient vers le fil complet sur la page de la note. Les pages de profil s'ouvrent par défaut sur Notes, divisées en onglets Posts et Conversations. Un bug de persistance des follows, qui faisait disparaître après redémarrage de l'app les comptes nouvellement suivis, est corrigé, et les boutons follow affichent désormais la progression.

### getwired.app et get-tao.app corrigent le flux d'envoi confess de NIP-13

[getwired.app](https://github.com/smolgrrr/Wired) et [get-tao.app](https://github.com/smolgrrr/TAO), qui partagent un flux de publication anonyme ajoutant la preuve de travail NIP-13 afin de limiter le spam au moment de l'envoi, ont corrigé le [flux d'envoi confess](https://github.com/smolgrrr/Wired/pull/57) afin de rendre cohérente l'UX pendant le minage PoW.

### nostui ajoute un onglet de timeline des mentions

[nostui](https://github.com/akiomik/nostui), un client Nostr de terminal en Rust, ajoute un [onglet de timeline des mentions](https://github.com/akiomik/nostui/pull/463) qui présente dans une vue TUI dédiée les événements de kind 1 taguant la pubkey active.

### Heartwood intègre des URI bunker NIP-46 par identité et un pont de signature en mode HSM

[Heartwood](https://github.com/forgesworn/heartwood) est un signataire [NIP-46](/fr/topics/nip-46/) dans lequel la clé de signature n'atteint jamais le client : le client parle NIP-46 à un petit relay, qui échange des frames série avec un appareil matériel connecté chargé de la signature. Cette semaine, le projet a intégré un [pont de signature relay-vers-série](https://github.com/forgesworn/heartwood/pull/11) et des [connexions bunker par identité](https://github.com/forgesworn/heartwood/pull/16), afin qu'un seul appareil matériel contenant plusieurs identités expose une URI bunker distincte pour chacune.

### Refactorisation de l'authentification et du signataire de Nostter

[Nostter](https://github.com/SnowCait/nostter) a remanié cette semaine sa [couche d'authentification et de signature](https://github.com/SnowCait/nostter/pulls?q=is%3Amerged+auth), en déplaçant l'état de connexion vers un signal unique et en extrayant le dispatch du signataire dans des modules de stratégie. La trajectoire vise une abstraction propre du signataire, où extension web NIP-07, bunker distant NIP-46 et nsec brut partagent le même chemin de code.

### Dart NDK extrait le signataire NIP-07 et randomise les timestamps NIP-59

[Dart NDK](https://github.com/relaystr/dart_ndk) a déplacé son signataire [NIP-07](/fr/topics/nip-07/) hors du paquet core vers `ndk_flutter` (où réside la WebView Flutter), et [randomisé les timestamps de ses gift wraps NIP-59](https://github.com/relaystr/dart_ndk/pull/667) pour mieux résister à la corrélation temporelle des messages chiffrés.

### Milk Market ajoute des pages de boutique NIP-23 et le traitement des paiements Square

[Milk Market](https://github.com/shopstr-eng/milk-market), la vitrine marketplace de l'équipe Shopstr, a donné à chaque boutique une page de blog alimentée par les événements long-form [NIP-23](/fr/topics/nip-23/) du vendeur, avec sections modifiables et route directe vers les réglages du blog. La même semaine a ajouté [Square](https://github.com/shopstr-eng/milk-market/pull/30) comme processeur de paiement alternatif pour les vendeurs et l'achat automatique d'étiquettes d'expédition pour les commandes payées.

### Calendar by Formstr livre une app iOS

[Calendar by Formstr](https://github.com/formstr-hq/nostr-calendar) a fusionné cette semaine la [PR #159 IOS App](https://github.com/formstr-hq/nostr-calendar/pull/159), qui porte le client de calendrier [NIP-52](/fr/topics/nip-52/) sur iOS. La [PR #197](https://github.com/formstr-hq/nostr-calendar/pull/197) corrige l'analyse des dates du calendrier en heure locale, et la [PR #201](https://github.com/formstr-hq/nostr-calendar/pull/201) ajoute un workflow E2E Playwright déclenché par un label `run-tests`.

### cagliostr applique NIP-22, NIP-09 par coordonnée et la preuve de travail NIP-13

[cagliostr](https://github.com/mattn/cagliostr), une implémentation de relay en Go, a durci trois chemins d'application cette semaine : [preuve de travail NIP-13 configurable](https://github.com/mattn/cagliostr/pull/7) sur les événements entrants, [suppression NIP-09 par coordonnée adressable](https://github.com/mattn/cagliostr/pull/8) afin que les événements remplaçables puissent être supprimés par leur tag `a` (ce que la suppression par id d'événement ne peut atteindre), et [limites de timestamp NIP-22 configurables](https://github.com/mattn/cagliostr/pull/9) rejetant les événements horodatés trop loin dans le passé ou le futur.

---

## Nouveaux projets suivis et découverts

La [suite wellbeing de Vanderwarker](https://git.vanderwarker.family/wellbeing) publie des télémétries du monde physique comme événements Nostr sous une clé de signature d'éditeur partagée. Elle comprend cinq apps sœurs : [Holy Fit](https://git.vanderwarker.family/wellbeing/holyfit-android) est un podomètre qui ancre les données de fitness dans Nostr sous `kind:30078`, [Nunlock](https://git.vanderwarker.family/wellbeing/nunlock-android) publie un compteur quotidien de déverrouillages du téléphone, [Saint Stream](https://git.vanderwarker.family/wellbeing/saintstream-android) publie la lecture média en cours sous forme de User Status, [Sister Charge](https://git.vanderwarker.family/wellbeing/sistercharge-android) publie le niveau, la tension et la température de la batterie toutes les 15 minutes, et [Cellibacy](https://git.vanderwarker.family/wellbeing/cellibacy-android) publie la consommation quotidienne de données. Les cinq sont apparues sur Zapstore entre le 24 et le 30 juin.

[ntrack v0.1.9](https://github.com/f321x/ntrack/releases/tag/v0.1.9) est une app Android chiffrée et sans serveur de partage de localisation en direct, construite en Rust et Slint et publiée le 29 juin. Elle est apparentée à [Haven](https://github.com/mehmetefeumit/Haven-App), l'app de partage de localisation fondée sur [Marmot](/fr/topics/marmot/) présentée dans le [#28](/en/newsletters/2026-06-24-newsletter/#haven-launches-private-location-sharing-on-marmot), mais adopte une autre architecture de transport : les DM Nostr chiffrés portent les mises à jour de localisation, là où Haven utilise des messages de groupe Marmot.

[NostrAppShell](https://git.nostrdev.com/stuff/NostrAppShell) est un échafaudage précoce de shell applicatif pour construire des apps Nostr. Le projet a publié cette semaine sa première documentation destinée aux utilisateurs.

[NIPs by Pollerama](https://nips.pollerama.fun) (dépôt [abh3po/better-nips](https://github.com/abh3po/better-nips), créé le 2026-06-29) est un nouveau client pour les NIP communautaires de `kind:30817` de [NostrHub](https://nostrhub.io), présenté comme une surface alternative à nostrhub.io pondérée par la confiance. Chaque NIP de `kind:30817` dispose de sa propre URL partageable (`#/nip/<naddr>`), avec rendu Markdown complet et les kinds d'événement qu'elle définit. Le client propose trois flux : Following, Web of Trust (follows-of-follows) et Global, chacun triable selon les approbations pondérées par la confiance ou par nouveauté. Les approbations sont publiées comme labels [NIP-32](/fr/topics/nip-32/) sur le kind `1985`, avec les tags `["L","nostrhub"]` et `["l","approve","nostrhub"]`, plus un tag `a` pointant vers l'adresse de la NIP cible et un tag `client` annonçant `better-nips`. C'est la forme d'événement exacte que NostrHub signe lui-même, de sorte que les approbations sont compatibles entre les deux clients. L'approbation d'un compte directement suivi pèse davantage dans le classement que celle d'un follow-of-follow au second degré.

La stack de signature est [`@formstr/signer`](https://www.npmjs.com/package/@formstr/signer), avec une modale de connexion complète couvrant l'extension [NIP-07](/fr/topics/nip-07/), le bunker et nostrconnect [NIP-46](/fr/topics/nip-46/), ncryptsec [NIP-49](/fr/topics/nip-49/) et le signataire Android [NIP-55](/fr/topics/nip-55/) ; les sessions se reconnectent silencieusement au rechargement. La couche réseau passe par [`@formstr/local-relay`](https://www.npmjs.com/package/@formstr/local-relay), un Web Worker qui répartit l'outbox [NIP-65](/fr/topics/nip-65/) de l'utilisateur entre les relays afin qu'un grand web of trust ne soit pas diffusé en éventail vers un relay unique. Le parti pris est que les NIP communautaires, qu'elles soient hébergées sur NostrHub, dans `better-nips` ou par de futurs autres clients, sont toutes égales au niveau du protocole ; le classement vient du graphe social et non d'une curation par des modérateurs, ce qui s'accorde directement avec le flux de labellisation NIP-32 présenté dans l'analyse approfondie du [#25](/en/newsletters/2026-06-03-newsletter/#nip-deep-dive-nip-32-labeling).

Deux nouveaux clusters de dépôts [NIP-34](/fr/topics/nip-34/) sont apparus cette semaine. [Vidstr](https://git.shakespeare.diy/npub14rg4vrt2v374q95ezeeydu3hkdhmzglcj950mggacap4x0lv0gyq04wun7/vidstr.git) est un client Nostr centré sur la vidéo, et un [cluster nostrapps.com](wss://gitnostr.com) publie trois projets frères : [verdana](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/verdana.git) (une VM napp pour ordinateur), [hallway](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/hallway.git) (un client de communautés personnalisable) et [napps](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/napps.git) (une spécification et un runtime de micro-apps HTML). Le cluster évolue en parallèle du travail [napplet](/fr/topics/nip-5d/) présenté à la une du dernier numéro.

---

## Travail protocolaire et mises à jour des NIP

### Fusionné : NIP-44 relève la limite de charge utile de 65 535 octets

La [PR #1907](https://github.com/nostr-protocol/nips/pull/1907) a été fusionnée le 28 juin après être restée ouverte depuis 2024-09. Le changement supprime la limite supérieure de 65 535 octets sur la charge utile en clair d'une enveloppe de chiffrement versionnée [NIP-44](/fr/topics/nip-44/), la relevant à 4 Gio (`uint32_max`). NIP-44 encode la longueur de la charge utile comme `uint16` dans le format sur le fil, ce que la spécification d'origine exigeait strictement pour l'interopérabilité ; le changement fusionné adopte un champ de longueur étendu signalé dans l'octet de version, de sorte que les implémentations v2 restent compatibles sur le fil et que les v3+ portent la longueur accrue. Les clients qui emploient NIP-44 pour les messages directs [NIP-17](/fr/topics/nip-17/), les gift wraps [NIP-59](/fr/topics/nip-59/), les charges utiles de signataire distant [NIP-46](/fr/topics/nip-46/) ou tout autre message Nostr chiffré avec NIP-44 peuvent désormais échanger des événements uniques dépassant 64 Kio sans découpage dans la couche applicative.

### Fusionné : NIP-86 reçoit une méthode signevent et un événement Relay Roles

La [PR #2389](https://github.com/nostr-protocol/nips/pull/2389) ajoute une méthode `signevent` à l'API JSON-RPC de gestion des relays [NIP-86](/fr/topics/nip-86/), permettant à un administrateur de demander au relay de signer un événement avec sa propre pubkey. La [PR #2390](https://github.com/nostr-protocol/nips/pull/2390) associée définit un événement Relay Roles : un événement remplaçable publié par un relay pour déclarer ses administrateurs et modérateurs. Ensemble, elles permettent aux clients NIP-86 d'inspecter la liste d'administrateurs d'un relay et de vérifier qu'une demande authentifiée vient d'un administrateur actuel, sans confiance hors bande. Analyse approfondie des deux changements ci-dessous.

### Fusionné : NIP-34 remplace personal-fork par `u` pour GRASP-06

La [PR #2395](https://github.com/nostr-protocol/nips/pull/2395), fusionnée le 24 juin, remplace le tag `personal-fork` de [NIP-34](/fr/topics/nip-34/) sur les événements d'état de dépôt (`kind:30618`) par un tag `u` (pour « upstream »), alignant le format sur le fil avec la sémantique de fork GRASP-06 qu'implémente la suite GitWorkshop. Le changement ferme la [PR #2384](https://github.com/nostr-protocol/nips/pull/2384) (`NIP-34: remove maintainers to solve expiry issues`), qui proposait un autre correctif de sémantique des forks. La direction fusionnée est celle qu'implémente ngit v2.6.x : la spécification et le CLI de référence sont donc alignés. Les dépôts existants utilisant `personal-fork` continuent d'interopérer ; les nouveaux dépôts et la branche ngit v2.6 publient le tag `u`.

### Fusionné : métadonnées client NIP-46, désormais upstream après leur livraison par Amber

La [PR #2381](https://github.com/nostr-protocol/nips/pull/2381), fusionnée le 23 juin, ajoute des métadonnées client facultatives à la demande `connect` [NIP-46](/fr/topics/nip-46/), permettant à un client de publier son nom, l'URL d'une icône et l'URL de sa page d'accueil lors de la connexion au signataire. [Amber v6.2.2](https://github.com/greenart7c3/Amber/releases/tag/v6.2.2) a livré cette extension de métadonnées la semaine dernière, comme présenté dans le [#28](/en/newsletters/2026-06-24-newsletter/#amber-v622-implements-nip-46-client-metadata) ; cette semaine, la NIP upstream rattrape l'implémentation déjà publiée.

### Ouvert : clés de wrapper NIP-17 déterministes par epoch

Les [PR #2397](https://github.com/nostr-protocol/nips/pull/2397) et [#2396](https://github.com/nostr-protocol/nips/pull/2396) couvrent deux propositions convergentes de clés de wrap NIP-17. La PR #2397 propose que la clé de signature éphémère utilisée pour créer un gift wrap [NIP-59](/fr/topics/nip-59/) soit dérivée de façon déterministe d'une seed par conversation liée à un epoch temporel grossier, afin qu'un destinataire connaissant la clé de conversation puisse prédire les pubkeys auxquelles s'abonner. La spécification actuelle exige une nouvelle clé aléatoire pour chaque wrap, rendant cette prédiction impossible. La PR #2396 apporte le changement associé : les wraps d'une conversation donnée devraient être signés directement avec la clé de conversation, de sorte que la pubkey du wrap serve aussi d'identifiant de conversation. Ensemble, elles tracent une voie vers des conversations NIP-17 filtrables sans fuite de métadonnées. Toutes deux sont ouvertes et en discussion.

### Ouvert : NIP-59 devrait faire rejeter les événements seal de kind 13 par le relay

La [PR #2399](https://github.com/nostr-protocol/nips/pull/2399) propose que les relays rejettent les événements de kind 13, le seal interne d'un gift wrap [NIP-59](/fr/topics/nip-59/), lorsqu'ils apparaissent au premier niveau d'une demande de publication, car un événement seal n'a de sens qu'à l'intérieur d'un wrap et qu'un seal divulgué expose la pubkey du destinataire. L'[issue #2398](https://github.com/nostr-protocol/nips/issues/2398) associée va plus loin et soutient que le seal devrait être redéfini comme kind éphémère (les kinds éphémères de NIP-01 ne sont pas stockés par les relays), ce qui durcirait la règle au niveau du protocole et supprimerait la dépendance aux politiques propres à chaque relay.

### Ouvert : états de groupe NIP-29

La [PR #2372](https://github.com/nostr-protocol/nips/pull/2372) ajoute à [NIP-29](/fr/topics/nip-29/), les groupes fondés sur des relays, une sémantique explicite des états de groupe. Elle définit ce que signifie pour un groupe d'être ouvert, fermé, public, privé ou archivé, et comment les transitions d'état interagissent avec les événements de membre. La proposition fait entrer dans la spécification du relay des sémantiques auparavant propres aux clients.

### Ouvert : prise en charge facultative de plusieurs mainteneurs dans NIP-34

La [PR #2324](https://github.com/nostr-protocol/nips/pull/2324) accompagne la [PR #2395](https://github.com/nostr-protocol/nips/pull/2395) fusionnée, dont la sémantique de fork GRASP-06 est présentée plus haut. Elle ajoute aux événements d'annonce de dépôt [NIP-34](/fr/topics/nip-34/) (`kind:30617`) la prise en charge facultative de plusieurs mainteneurs, permettant à un dépôt de déclarer plus d'une pubkey de mainteneur canonique par répétition de tags `maintainer`. Les patches et issues signés par tout mainteneur déclaré sont alors reconnus comme officiels par les clients, comblant une lacune ancienne : les dépôts NIP-34 à plusieurs mainteneurs doivent sinon tout faire passer par une seule pubkey ou revenir à une coordination hors protocole.

### Ouvert : opérateur AND de NIP-91 pour les filtres, proposition ouverte et non fusionnée

La [PR #2252](https://github.com/nostr-protocol/nips/pull/2252) propose un opérateur AND pour les [filtres](/fr/topics/nip-01/) Nostr, rouvrant une conception déjà abordée dans l'ancienne [PR #1365](https://github.com/nostr-protocol/nips/pull/1365), désormais fermée. Des implémentations existent déjà dans [nostr-rs-relay](https://github.com/v0l/nostr-rs-relay), applesauce, [Amethyst](https://github.com/vitorpamplona/amethyst) et worker-relay, mais la PR de spécification elle-même reste ouverte.

### Fermé : quatre NIP commerciales de pats2sats

Quatre propositions de commerce sur Nostr ont fermé cette semaine : Escrow ([#2334](https://github.com/nostr-protocol/nips/pull/2334)), Reservations ([#2335](https://github.com/nostr-protocol/nips/pull/2335)), une Marketplace Listing Extension [NIP-99](/fr/topics/nip-99/) ([#2346](https://github.com/nostr-protocol/nips/pull/2346)) et un Accommodation Listing Profile ([#2333](https://github.com/nostr-protocol/nips/pull/2333)). La même surface commerciale se consolide désormais dans la [Gamma Market Spec](https://github.com/GammaMarkets/market-spec), un dépôt d'extensions propre au projet qui complète les annonces marketplace NIP-99 avec une sémantique de commandes, checkout, escrow et litiges. Compass suit maintenant ce dépôt aux côtés de Marmot et Blossom comme dépôt de spécification de protocole externe au dépôt des NIP ; ses PR ouvertes cette semaine comprennent une clarification de l'attribution client ([#11](https://github.com/GammaMarkets/market-spec/pull/11)), un tag supersedes pour les changements d'identité d'un produit ([#8](https://github.com/GammaMarkets/market-spec/pull/8)) et la sémantique des évaluations de marchands ([#7](https://github.com/GammaMarkets/market-spec/pull/7)).

### Ouvert : liaison d'identités Bitcoin

Deux propositions ont été ouvertes cette semaine pour lier identités Bitcoin et Nostr : une [adresse Bitcoin Silent Payment NIP-352](https://github.com/nostr-protocol/nips/pull/2392) et une [preuve de liaison d'identité Bitcoin-OTC](https://github.com/nostr-protocol/nips/pull/2401).

---

## Analyse approfondie de NIP-86 (API de gestion des relays)

[NIP-86](/fr/topics/nip-86/) définit une interface JSON-RPC de gestion des relays, permettant aux clients autorisés d'envoyer des commandes administratives aux relays par une API standardisée. Un client unique peut gérer tout relay compatible NIP-86 sans outillage propre à chacun. Deux fusions de spécification cette semaine, les [PR #2389](https://github.com/nostr-protocol/nips/pull/2389) et [#2390](https://github.com/nostr-protocol/nips/pull/2390), ferment la boucle entre événements signés par le relay et administrateurs déclarés par celui-ci.

### Le transport

Une demande de gestion NIP-86 est un POST HTTP vers la même URI depuis laquelle le relay sert les connexions WebSocket, avec `Content-Type: application/nostr+json+rpc`. Le corps de la demande est un document JSON de la forme :

```json
{
  "method": "<method-name>",
  "params": [<arg1>, <arg2>, ...]
}
```

L'authentification utilise dans le header `Authorization` un événement signé d'authentification HTTP [NIP-98](/fr/topics/nip-98/). Avant d'exécuter la méthode, le relay vérifie que la pubkey signataire figure dans sa liste d'administrateurs. La réponse du relay est un document JSON de la forme :

```json
{
  "result": <return-value>,
  "error": "<error-string-if-any>"
}
```

### Les méthodes qui existaient avant cette semaine

L'ensemble de méthodes existant couvre le bannissement de pubkeys (`banpubkey`, `allowpubkey`, `listbannedpubkeys`), le bannissement d'événements (`banevent`, `allowevent`, `listbannedevents`), les métadonnées du relay (`changerelayname`, `changerelaydescription`, `changerelayicon`), la gestion de la liste des kinds autorisés (`allowkind`, `disallowkind`, `listallowedkinds`) et une méthode `stats` qui renvoie les statistiques du relay. La forme reste intentionnellement proche d'un service JSON-RPC standard, afin qu'un client puisse y superposer des bindings typés.

### Ce qui a changé cette semaine

La [PR #2389](https://github.com/nostr-protocol/nips/pull/2389) ajoute une méthode `signevent` à la spécification. Elle reçoit en argument un modèle d'événement partiel (kind, tags, content) et demande au relay de signer puis renvoyer un événement complet dont le champ `pubkey` contient sa propre pubkey. C'est le prérequis pour qu'un relay publie des événements de niveau protocolaire à son propre sujet : annonces de pubkeys bloquées, métadonnées du relay et nouvel événement Relay Roles ci-dessous exigent tous une signature avec la clé contrôlée par l'opérateur du relay, mais la plupart des opérateurs ne souhaitent pas conserver de clé privée dans leur client d'administration.

La [PR #2390](https://github.com/nostr-protocol/nips/pull/2390) définit un événement Relay Roles : un kind d'événement remplaçable paramétré publié par un relay, signé avec sa propre pubkey via `signevent`, qui déclare les pubkeys de ses administrateurs et modérateurs avec une sémantique explicite des rôles. Un client compatible NIP-86 peut récupérer l'événement Relay Roles de tout relay suivi, construire la liste d'administrateurs depuis ses tags et valider qu'une demande NIP-86 authentifiée vient d'un administrateur actuel sans confiance hors bande ni configuration propre au relay. Ensemble, les deux PR ferment la boucle : `signevent` est le mécanisme, Relay Roles le premier kind d'événement construit dessus.

### Exemple de demande NIP-86

Une demande `banpubkey` NIP-86 complète ressemble à ceci :

```json
{
  "method": "banpubkey",
  "params": [
    "<64-char-hex-pubkey-to-ban>",
    "spam"
  ]
}
```

avec un header `Authorization` portant un événement NIP-98 signé :

```json
{
  "id": "5e1c2f9e1d3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c",
  "pubkey": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2",
  "created_at": 1782824400,
  "kind": 27235,
  "tags": [
    ["u", "https://relay.example.com/"],
    ["method", "POST"],
    ["payload", "<sha256-of-request-body>"]
  ],
  "content": "",
  "sig": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100"
}
```

La pubkey signataire doit figurer dans l'ensemble des administrateurs du relay, désormais déclaré dans l'événement relay-roles ; le tag `u` doit correspondre à l'URL HTTPS du relay ; le tag `payload` doit correspondre au SHA-256 du corps JSON de la demande. Le relay renvoie :

```json
{
  "result": true,
  "error": null
}
```

### Implémentations

- [Amethyst](https://github.com/vitorpamplona/amethyst) livre une interface de gestion de relay NIP-86 sur Android (v1.07.0+).
- Les relays de référence qui implémentent la spécification comprennent [strfry](https://github.com/hoytech/strfry), [khatru](https://github.com/fiatjaf/khatru) et plusieurs implémentations plus petites liées depuis la section `Implementation Status` de la spécification.

Les clients compatibles NIP-86 commenceront à traiter l'événement relay-roles comme source canonique de la liste d'administrateurs d'un relay, une fois que les implémenteurs auront adopté les changements `signevent` et Relay Roles.

---

## Analyse approfondie de NIP-89 (handlers d'application recommandés)

[NIP-89](/fr/topics/nip-89/) définit deux kinds d'événements remplaçables paramétrés : `kind:31990`, le handler d'application publié par le développeur d'une app, et `kind:31989`, la recommandation qu'un utilisateur publie pour une app qu'il emploie. Ensemble, ils permettent aux clients de découvrir les applications qui savent traiter un kind d'événement inconnu sans coordination hors bande : un lecteur long-form qui rencontre un événement `kind:30030` qu'il ne traite pas nativement peut interroger le graphe NIP-89 à la recherche de handlers et proposer à l'utilisateur un flux « Open in... » vers une app publiée qui sait le faire. NIP-89 constitue l'infrastructure d'origine pour le même problème de routage entre apps que le travail napplet/napps visible dans tout ce numéro étend maintenant à des applets Nostr-native composables.

### L'événement handler d'application (`kind:31990`)

Le développeur d'une app publie un ou plusieurs événements handler décrivant les kinds d'événement pris en charge et la manière d'ouvrir une entité Nostr dans l'app :

```json
{
  "id": "8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b",
  "pubkey": "c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2",
  "created_at": 1782824400,
  "kind": 31990,
  "tags": [
    ["d", "longform-reader-v1"],
    ["k", "30023"],
    ["k", "30024"],
    ["web", "https://reader.example.com/a/<bech32>", "naddr"],
    ["ios", "longformreader://open/<bech32>"],
    ["android", "longformreader://open/<bech32>"]
  ],
  "content": "{\"name\": \"Longform Reader\", \"picture\": \"https://reader.example.com/icon.png\", \"about\": \"A native reader for NIP-23 longform.\"}",
  "sig": "1f2e3d4c5b6a798877665544332211000ffeeddccbbaa99887766554433221100ffeeddccbbaa99887766554433221100ffeeddccbbaa9988776655443322110a"
}
```

Le tag `d` identifie le handler, afin qu'il puisse être remplacé ; chaque tag `k` déclare un kind d'événement géré par l'app ; et chaque tag de plateforme (`web`, `ios`, `android`, ...) fournit un modèle d'URL où `<bech32>` sert d'espace réservé pour une entité encodée selon [NIP-19](/fr/topics/nip-19/), que le client appelant substitue à l'ouverture. Un événement handler peut annoncer plusieurs kinds pris en charge lorsqu'ils partagent le même modèle de routage, ce qui garde la découverte des apps compacte et évite un événement handler par kind.

### L'événement de recommandation utilisateur (`kind:31989`)

Un utilisateur publie une recommandation déclarant les apps qu'il emploie pour un kind d'événement donné :

```json
{
  "id": "9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d",
  "pubkey": "d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3",
  "created_at": 1782824500,
  "kind": 31989,
  "tags": [
    ["d", "30023"],
    ["a", "31990:c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2:longform-reader-v1", "wss://relay.example.com", "web"],
    ["a", "31990:e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6:reader-pro", "wss://relay.example.com", "ios"]
  ],
  "content": "",
  "sig": "2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6"
}
```

Le tag `d` porte le kind d'événement recommandé. Chaque tag `a` est un pointeur d'adresse NIP-01 vers un événement handler de `kind:31990`, avec le relay suggéré et la plateforme concernée. Une même recommandation peut répertorier plusieurs apps pour différentes plateformes.

### Le tag client et le compromis de confidentialité

NIP-89 définit aussi un tag `client` facultatif que toute app de publication peut joindre aux événements qu'elle crée :

```
["client", "Longform Reader", "31990:c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2:longform-reader-v1", "wss://relay.example.com"]
```

Cela permet à tout client affichant l'événement de faire apparaître l'app d'origine, de récupérer des métadonnées de handler plus riches et de respecter les indications de rendu déclarées par le handler. La spécification signale aussi explicitement le coût en matière de confidentialité : un client qui émet un tag `client` sur chaque événement publie l'identité du logiciel de l'utilisateur, ce qui révèle avec le temps ses habitudes d'utilisation. Elle recommande aux clients de proposer une option de désactivation.

La [PR #3422](https://github.com/vitorpamplona/amethyst/pull/3422) d'Amethyst analyse et affiche les tags NIP-89 `t`, `i`, `a` et `client` lors de l'affichage des événements, montrant directement dans la timeline quelle app a créé une note.

### Fonctionnement pratique du flux de découverte

Un client qui reçoit un kind d'événement inconnu suit les étapes suivantes. (1) Interroger le graphe de follows de l'utilisateur à la recherche d'événements `kind:31989` dont le tag `d` correspond au kind d'événement. (2) Résoudre chaque tag `a` recommandé vers son événement handler `kind:31990`. (3) Choisir le handler dont le modèle d'URL `web`, `ios` ou `android` correspond à la plateforme actuelle. (4) Substituer l'encodage `bech32` de l'entité dans le modèle d'URL. (5) Proposer l'URL obtenue à l'utilisateur comme choix « Open in... ». Le flux est filtré socialement : un client qui interrogerait des événements handler arbitraires sur des relays non fiables pourrait rediriger les utilisateurs vers des apps malveillantes ; commencer par les personnes suivies par l'utilisateur est donc un choix par défaut plus sûr que de considérer comme également fiable chaque handler publié.

### NIP-89 et la couche napplet

La section Discover d'Amethyst, le runtime hôte de napplets et l'affichage du tag `client` construisent ensemble une surface complète de consommation de NIP-89 sur Android. La spécification napplet, lancée dans le dernier numéro, étend ce que peuvent cibler ces événements handler NIP-89 : des applets sandboxées qui exécutent un runtime Nostr-native composable sur Nostr et Blossom. NIP-89 est le graphe de découverte et de routage ; le runtime napplet constitue l'une des cibles d'exécution vers lesquelles il peut pointer.

---

*Retours, corrections et projets que nous avons manqués : ouvrez une issue sur [github.com/andotherstuff/nostr-compass](https://github.com/andotherstuff/nostr-compass) ou contactez-nous par DM NIP-17 à npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923.*
