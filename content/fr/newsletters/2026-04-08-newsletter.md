---
title: 'Nostr Compass #17'
date: 2026-04-08
translationOf: /en/newsletters/2026-04-08-newsletter.md
translationDate: 2026-04-09
draft: false
type: newsletters
---

Bienvenue dans Nostr Compass, votre guide hebdomadaire sur Nostr.

**Cette semaine :** [Amethyst](https://github.com/vitorpamplona/amethyst) livre [v1.08.0](#amethyst-livre-arti-tor-integre-mls-et-marmot-en-pur-kotlin) avec l'intégration d'Arti Tor et une interface Shorts repensée, tout en fusionnant des implémentations en pur Kotlin de [MLS](/fr/topics/mls/) et [Marmot](/fr/topics/marmot/) dans sa bibliothèque [Quartz](/fr/topics/quartz/). [Nostur](https://github.com/nostur-com/nostur-ios-public) livre [v1.27.0](#nostur-v1270-ajoute-lenregistrement-video-et-les-reponses-privees) avec enregistrement vidéo, profils GIF animés et réponses privées. [Shosho](https://github.com/r0d8lsh0p/shosho-releases) lance [v0.15.0](#shosho-v0150-lance-shows-et-un-carrousel-video-vertical) avec Shows (informations de live personnalisées connectées à OBS) et un carrousel vidéo vertical de style TikTok. [Nymchat](https://github.com/Spl0itable/NYM) [abandonne Marmot et livre des chats de groupe NIP-17 renforcés](#nymchat-abandonne-marmot-et-livre-des-chats-de-groupe-nip-17-renforces) avec des clés éphémères rotatives. [Nostr VPN](https://github.com/mmalmi/nostr-vpn) livre [le support des exit nodes et le packaging Umbrel](#nostr-vpn-livre-le-support-des-exit-nodes-et-le-packaging-umbrel) à travers six versions. [Amber](https://github.com/greenart7c3/Amber) passe à [v6.0.0-pre1](#amber-v600-pre1-ajoute-des-cles-de-signature-nip-46-par-connexion) avec des clés de signature [NIP-46](/fr/topics/nip-46/) par connexion et des mises à jour in-app via Zapstore. [Notedeck](https://github.com/damus-io/notedeck) atteint [v0.10.0-beta](#notedeck-v0100-beta-livre-lauto-update-via-zapstore) avec l'auto-update APK via Zapstore, et [NIP-58](/fr/topics/nip-58/) (Badges) reçoit une [migration de kind](#mises-a-jour-des-nip). Deux deep dives NIP couvrent [NIP-17](/fr/topics/nip-17/) (Private Direct Messages) et [NIP-46](/fr/topics/nip-46/) (Nostr Remote Signing).

## Actualités

### Amethyst livre Arti Tor, intègre MLS et Marmot en pur Kotlin

[Amethyst](https://github.com/vitorpamplona/amethyst), le client Android maintenu par vitorpamplona, a livré quatre versions de [v1.07.3](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.3) à [v1.08.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.08.0) et a fusionné un gros lot de travail non encore publié dans sa bibliothèque [Quartz](/fr/topics/quartz/) (le module Nostr Kotlin Multiplatform partagé). La version phare est v1.08.0 « Arti Tor », qui migre la connectivité Tor de l'application depuis la bibliothèque Tor en C vers [Arti](https://gitlab.torproject.org/tpo/core/arti), l'implémentation Rust du Tor Project. La migration corrige des crashes aléatoires qui survenaient avec les anciens bindings Tor en C. Arti est le remplaçant de long terme du Tor Project pour le codebase en C, réécrit depuis zéro en Rust pour la sûreté mémoire et les async I/O.

La version v1.07.3 a repensé l'interface Shorts, en remplaçant le design paginé par des flux bord à bord pour les images, les shorts et les vidéos longues. La même version a migré les badges vers le kind `10008` et les bookmarks vers le kind `10003`, en s'alignant sur la migration de kind [NIP-58](/fr/topics/nip-58/) [fusionnée cette semaine](#mises-a-jour-des-nip). v1.07.4 a corrigé un problème de gestion de secret Nostr Wallet Connect, et v1.07.5 a corrigé un crash lors du téléversement d'images.

Sur `main` mais pas encore dans une release taguée, l'équipe a écrit une implémentation complète en Kotlin de [MLS](/fr/topics/mls/) et du protocole [Marmot](/fr/topics/marmot/), supprimant le besoin de bindings natifs vers des bibliothèques C/Rust. [PR #2147](https://github.com/vitorpamplona/amethyst/pull/2147) ajoute la couche centrale de messagerie de groupe MLS de Marmot, [PR #2149](https://github.com/vitorpamplona/amethyst/pull/2149) ajoute l'interface de chat de groupe, [PR #2146](https://github.com/vitorpamplona/amethyst/pull/2146) ajoute les processeurs de messages entrants et sortants avec un gestionnaire d'abonnements, [PR #2141](https://github.com/vitorpamplona/amethyst/pull/2141) ajoute la persistance d'état de groupe MLS et la gestion de rotation des KeyPackage, [PR #2150](https://github.com/vitorpamplona/amethyst/pull/2150) ajoute une suite de tests MLS complète avec une signature GroupInfo améliorée, et [PR #2158](https://github.com/vitorpamplona/amethyst/pull/2158) ajoute le suivi du statut de publication des KeyPackage. [PR #2166](https://github.com/vitorpamplona/amethyst/pull/2166) ajoute une implémentation secp256k1 en pur Kotlin pour les opérations cryptographiques Nostr, remplaçant la dépendance à la bibliothèque C native. Combiné à l'implémentation MLS en Kotlin, [Quartz](/fr/topics/quartz/) peut exécuter la signature Nostr et la messagerie de groupe Marmot sans aucun binding natif, ce qui ouvre la voie à des cibles Kotlin Multiplatform, y compris iOS.

L'équipe construit aussi le support de [NIP-AC](/en/topics/nip-ac/) (P2P Voice and Video Calls) : [PR #2143](https://github.com/vitorpamplona/amethyst/pull/2143) ajoute une suite de tests complète pour la machine d'état d'appel NIP-AC, et [PR #2164](https://github.com/vitorpamplona/amethyst/pull/2164) empêche d'anciennes offres d'appel de se redéclencher après un redémarrage de l'application.

### Nostur v1.27.0 ajoute l'enregistrement vidéo et les réponses privées

[Nostur](https://github.com/nostur-com/nostur-ios-public), le client Nostr iOS, a livré [v1.27.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/v1.27.0) le 2 avril. La version ajoute l'enregistrement vidéo in-app avec découpe avant téléversement, de sorte que les utilisateurs puissent capturer de courts clips, les raccourcir et les publier sans quitter le client. Le support des GIFs animés s'étend aux photos de profil et de bannière, avec aussi l'ajout du rendu WebP animé. Une nouvelle intégration Shortcuts permet aux utilisateurs d'envoyer des posts Nostr depuis les automatisations Apple Shortcuts. La version ajoute aussi les réponses privées et corrige des problèmes de compatibilité DM qui affectaient la livraison des messages entre Nostur et d'autres clients.

### Shosho v0.15.0 lance Shows et un carrousel vidéo vertical

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), l'application de live streaming Nostr, a livré [v0.15.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.15.0) et [v0.15.1](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.15.1) le 7 avril. La fonctionnalité phare est Shows : les streamers peuvent préparer des informations d'émission personnalisées avant de passer en direct et connecter leur show à OBS ou à n'importe quel encodeur externe. Cela sépare les métadonnées « qu'est-ce que je diffuse » de l'acte de passer en direct, de sorte que les streamers puissent préparer titres, descriptions et produits avant de commencer la diffusion. La même version ajoute un carrousel vidéo vertical de style TikTok pour parcourir lives, clips et replays dans un flux plein écran, ainsi que Quick Add pour publier des clips vidéo et ajouter des produits directement depuis une page de profil. v0.15.1 corrige un bug où le clavier masquait le champ de saisie du chat de live.

## Versions

### Notedeck v0.10.0-beta livre l'auto-update via Zapstore

[Notedeck](https://github.com/damus-io/notedeck), le client desktop et mobile de l'équipe Damus, a livré [v0.10.0-beta.1](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.1) et [v0.10.0-beta.2](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.2) comme préreleases de test pour l'auto-update APK. [PR #1417](https://github.com/damus-io/notedeck/pull/1417) ajoute l'auto-update APK via l'updater Nostr/Zapstore sur Android, en prolongeant [le travail de découverte de mises à jour natif à Nostr de la Newsletter #14](/en/newsletters/2026-03-18-newsletter/#notedeck-moves-release-discovery-onto-nostr). Le flux de mise à jour découvre les nouvelles releases via des événements Nostr publiés sur des relays, puis télécharge l'APK depuis l'endroit où le développeur l'héberge (GitHub releases, Blossom CDN ou autres sources), vérifie le hash SHA-256 contre l'événement Nostr signé, puis l'installe. [PR #1438](https://github.com/damus-io/notedeck/pull/1438) corrige un bug d'écran d'accueil où les boutons Login et CreateAccount revenaient immédiatement en arrière, et [PR #1424](https://github.com/damus-io/notedeck/pull/1424) corrige un débordement de texte dans la vue de session Agentium AI.

### Amber v6.0.0-pre1 ajoute des clés de signature NIP-46 par connexion

[Amber](https://github.com/greenart7c3/Amber), l'application signataire [NIP-55](/fr/topics/nip-55/) (Android Signer Application), a livré [v6.0.0-pre1](https://github.com/greenart7c3/Amber/releases/tag/v6.0.0-pre1) le 4 avril. Le changement le plus important est l'ajout de clés de signature par connexion pour le protocole bunker [NIP-46](/fr/topics/nip-46/) (Nostr Remote Signing). Au lieu d'utiliser une seule paire de clés pour toutes les connexions bunker, Amber génère désormais une clé distincte pour chaque client connecté. Si la connexion d'un client est compromise, l'attaquant ne peut pas usurper le signataire auprès des autres clients.

[PR #377](https://github.com/greenart7c3/Amber/pull/377) ajoute la vérification et l'installation de mises à jour in-app via Zapstore, rejoignant [Notedeck](#notedeck-v0100-beta-livre-lauto-update-via-zapstore) dans l'adoption d'une distribution d'apps native à Nostr. [PR #375](https://github.com/greenart7c3/Amber/pull/375) gère les échecs AndroidKeyStore proprement en affichant un avertissement aux utilisateurs au lieu de crasher, et [PR #371](https://github.com/greenart7c3/Amber/pull/371) ajoute un nettoyage de base de données avec limites de taille et troncature de contenu pour empêcher une croissance de stockage non bornée. La prérelease reprend aussi la liste blanche d'auth relay [NIP-42](/fr/topics/nip-42/) et la connexion par phrase mnémonique de récupération du [cycle v5.0.x couvert la semaine dernière](/en/newsletters/2026-04-01-newsletter/#amber-v502-through-v504).

### Nostria livre une application mobile native

[Nostria](https://github.com/nostria-app/nostria), le client Nostr cross-platform maintenu par SondreB, a publié une application mobile native pour Android avec huit versions de [v3.1.11](https://github.com/nostria-app/nostria/releases/tag/v3.1.11) à [v3.1.18](https://github.com/nostria-app/nostria/releases/tag/v3.1.18). La nouveauté la plus importante est le support natif d'un signataire local pour des signataires comme [Amber](https://github.com/greenart7c3/Amber) et Aegis. Des [installeurs desktop](https://www.nostria.app/download) pour Linux, macOS et Windows sont aussi disponibles. [PR #610](https://github.com/nostria-app/nostria/pull/610) réduit la pression mémoire du flux avec des limites runtime adaptatives et un nettoyage des URLs d'aperçu. v3.1.14 corrige l'intégration avec Brainstorm, un fournisseur [Web of Trust](/fr/topics/web-of-trust/). v3.1.15 se concentre sur des améliorations musicales. La nouvelle application Android est disponible sur [Zapstore](https://zapstore.dev/apps/app.nostria).

### diVine 1.0.8 livre des téléversements reprenables et des DMs

[diVine](https://github.com/divinevideo/divine-mobile), le client vidéo short-form, a livré [1.0.8](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.8) avec 87 PRs fusionnées. Les téléversements reprenables permettent aux créateurs de reprendre des téléversements interrompus morceau par morceau au lieu de repartir de zéro sur une connexion instable. La version ajoute des réglages de qualité vidéo et de bitrate, le double tap pour liker, et des améliorations des DMs. [PR #2722](https://github.com/divinevideo/divine-mobile/pull/2722) ajoute un plugin caméra macOS pour la capture vidéo desktop, et [PR #2820](https://github.com/divinevideo/divine-mobile/pull/2820) migre le système de notifications vers une architecture BLoC avec enrichissement et regroupement. L'équipe a aussi remplacé les stickers et illustrations de catégories générés par AI par des SVG OpenMoji ([PR #2844](https://github.com/divinevideo/divine-mobile/pull/2844), [PR #2842](https://github.com/divinevideo/divine-mobile/pull/2842)).

### Manent v1.3.0 ajoute le floutage des notes sensibles et l'auth NIP-42

[Manent](https://github.com/dtonon/manent), l'application privée de notes chiffrées et de stockage de fichiers, a livré [v1.3.0](https://github.com/dtonon/manent/releases/tag/v1.3.0) le 2 avril. Les utilisateurs peuvent maintenant marquer des notes comme sensibles afin de les flouter dans la vue liste, ce qui garde le contenu privé caché lors d'un défilement occasionnel. La version ajoute aussi le support [NIP-42](/fr/topics/nip-42/) (Authentication of Clients to Relays), permettant à Manent de s'authentifier auprès des relays qui l'exigent avant d'accepter les événements. Manent stocke toutes les données chiffrées sur les relays Nostr à l'aide de la paire de clés de l'utilisateur, donc le support NIP-42 élargit l'ensemble des relays qu'il peut utiliser pour le stockage.

### Wisp v0.17.0 à v0.17.3 ajoutent les zaps sur live stream et la sauvegarde du portefeuille

[Wisp](https://github.com/barrydeen/wisp), le client Nostr Android, a livré six versions de [v0.16.2-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.2-beta) à [v0.17.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.17.3-beta) avec 44 PRs fusionnées. La version v0.17.0 ajoute des invites de sécurité pour la sauvegarde du portefeuille et des améliorations UX pour les zaps. [v0.17.1](https://github.com/barrydeen/wisp/releases/tag/v0.17.1-beta) ajoute la visibilité du chat de live stream à travers les plateformes et la fonctionnalité de zap sur live stream. [PR #423](https://github.com/barrydeen/wisp/pull/423) ajoute l'auto-search des profils, une animation de succès de zap et des améliorations du statut utilisateur. [PR #426](https://github.com/barrydeen/wisp/pull/426) corrige un crash out-of-memory dans `computeId` pour des événements avec de grandes listes de tags. Les versions v0.16.x avaient ajouté l'autocomplétion des shortcodes emoji, des améliorations de l'interface de chat de groupe et le filtrage des utilisateurs bloqués sur tous les chemins de notification.

### Mostro livre des deep links, des taux de change Nostr et un correctif de paiement en double

[Mostro](https://github.com/MostroP2P/mostro), l'échange Bitcoin pair à pair construit sur Nostr, a connu cette semaine des mises à jour à la fois sur son daemon serveur et son client mobile. Côté serveur, [PR #692](https://github.com/MostroP2P/mostro/pull/692) empêche que des écritures d'ordres obsolètes causent des paiements en double, un bug qui pouvait conduire à payer deux fois un vendeur pour la même transaction. [PR #693](https://github.com/MostroP2P/mostro/pull/693) utilise des mises à jour ciblées pour les écritures `dev_fee` au lieu d'écrasements complets d'ordres.

[Mostro Mobile](https://github.com/MostroP2P/mobile), le client Flutter, a livré [v1.2.3](https://github.com/MostroP2P/mobile/releases/tag/v1.2.3) le 3 avril. La version gère les deep links provenant de différentes instances Mostro, de sorte que les utilisateurs puissent toucher des liens qui routent vers le bon serveur d'échange. [PR #498](https://github.com/MostroP2P/mobile/pull/498) détecte les DMs admin et de litige dans le pipeline de notifications en arrière-plan, et l'application récupère désormais les taux de change depuis Nostr avec un fallback HTTP/cache. [PR #560](https://github.com/MostroP2P/mobile/pull/560) corrige un bug bloquant la connexion relay qui empêchait l'application d'atteindre les relays dans certaines conditions réseau.

### Unfiltered v1.0.12 ajoute les hashtags et les commentaires

[Unfiltered](https://github.com/dmcarrington/unfiltered), un client Nostr centré sur le contenu image-first, a livré [v1.0.12](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.12). [PR #69](https://github.com/dmcarrington/unfiltered/pull/69) ajoute le support des hashtags et [PR #72](https://github.com/dmcarrington/unfiltered/pull/72) ajoute la possibilité d'écrire et d'afficher des commentaires sur les posts. [PR #71](https://github.com/dmcarrington/unfiltered/pull/71) corrige des problèmes de navigation avec plusieurs images par post.

### Primal Android livre le partage multi-comptes du portefeuille et l'auto-reconnexion du signataire distant

[Primal](https://github.com/PrimalHQ/primal-android-app), le client Nostr Android, a livré une version le 7 avril. La mise à jour ajoute le partage multi-comptes du portefeuille et un menu overflow avec suppression du portefeuille dans Dev Tools. Le signataire distant se reconnecte désormais automatiquement lors des pertes de connexion, et le service portefeuille a gagné sa propre logique d'auto-reconnexion. Les correctifs incluent le fait que les votes zap de sondage n'apparaissent plus comme Top Zaps, la prévention des crashes sur option de sondage vide, le masquage du solde du portefeuille quand aucun portefeuille n'existe, et le mapping des types de WalletException vers des codes d'erreur dans les réponses NWC.

### Titan v0.1.0 lance un navigateur natif `nsite://` avec enregistrement de noms sur Bitcoin

[Titan](https://github.com/btcjt/titan), un navigateur desktop natif pour le web Nostr, a livré [v0.1.0](https://github.com/btcjt/titan/releases/tag/v0.1.0) le 7 avril. Titan résout les URLs `nsite://` en recherchant des noms lisibles par l'humain enregistrés sur Bitcoin, en interrogeant les relays Nostr pour les événements de contenu du site, puis en rendant les pages récupérées depuis des serveurs [Blossom](/fr/topics/blossom/). Le résultat est une expérience de navigation web sans DNS, sans certificats TLS et sans hébergeurs. Les noms sont enregistrés via une [interface web](https://npub1hmq6xuqnplk5lw0h3700cujmx5gymqn5wrn42u6432r6ntzumezqc3marw.nsite.lol/register) liée à des transactions Bitcoin. La version initiale est livrée sous forme de `.dmg` macOS (ARM, avec support Rosetta 2 pour Intel) et inclut le support d'un environnement de développement Nix.

### Bikel v1.5.0 livre un service d'avant-plan natif pour les téléphones de-Googlés

[Bikel](https://github.com/Mnpezz/bikel), un tracker cycliste décentralisé qui transforme les trajets en données d'infrastructure publique via Nostr, a livré [v1.5.0](https://github.com/Mnpezz/bikel/releases/tag/v1.5.0) le 4 avril. La version migre depuis Expo TaskManager dépendant de GMS vers un service d'avant-plan natif personnalisé, garantissant un suivi fiable des trajets en arrière-plan sur LineageOS, GrapheneOS et d'autres variantes Android de-Googlées. Le Bikel Bot a reçu une architecture dual-pocket avec collecte eCash autonome via des Cashu nutzaps. v1.4.3 et v1.4.2 corrigent la synchronisation du suivi en arrière-plan pour les environnements Android non standard, et l'application ajoute des bascules de points de carte pour les racks à vélos OSM.

### Sprout ajoute le support de NIP-01, NIP-23 et NIP-33

[Sprout](https://github.com/block/sprout), une plateforme de communication de Block avec relay Nostr intégré, a livré [desktop/v0.1.0-rc7](https://github.com/block/sprout/releases/tag/desktop/v0.1.0-rc7) le 6 avril. Cette semaine, l'équipe a ajouté le support des articles kind `30023` [NIP-23](/en/topics/nip-23/) (Long-form Content), des événements remplaçables paramétrés [NIP-33](/en/topics/nip-33/) avec remplacement indexé par tag `d`, et des text notes kind `1` et follow lists kind `3` [NIP-01](/fr/topics/nip-01/)/[NIP-02](/en/topics/nip-02/). La version ajoute aussi un système de thèmes IDE adaptatifs avec 54 thèmes, des améliorations UX de workflow et d'historique d'exécution d'agents, ainsi qu'un nettoyage de la sidebar membres.

### mesh-llm v0.56.0 livre un protocole de configuration distribué

[mesh-llm](https://github.com/michaelneale/mesh-llm), un système d'inférence LLM distribué qui utilise des paires de clés Nostr pour l'identité des nœuds, a livré [v0.56.0](https://github.com/michaelneale/mesh-llm/releases/tag/v0.56.0) le 7 avril. La version ajoute un protocole de configuration distribué avec une sémantique de propriété, une quantification asymétrique du cache KV (clés Q8_0 avec valeurs Q4) pour réduire l'usage mémoire, le stockage dans l'OS keychain pour les keystores d'identité, un streaming de chat fluide avec mise en file des messages, et des correctifs pour la mise en page fullscreen et le découpage du cache KV avec flash attention.

### Nostr VPN livre le support des exit nodes et le packaging Umbrel

[Nostr VPN](https://github.com/mmalmi/nostr-vpn), un VPN pair à pair qui utilise les relays Nostr pour le signalement et WireGuard pour les tunnels chiffrés, a livré six versions de [v0.3.0](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.0) à [v0.3.6](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.6) cette semaine. Le cycle v0.3.x ajoute le support des exit nodes sur Windows et macOS, permettant à des pairs de router le trafic internet via d'autres nœuds du réseau. La propagation des invitations et des alias se synchronise désormais sur Nostr, de sorte que les utilisateurs puissent partager l'accès réseau sans coordination hors bande. Les versions ajoutent le packaging Umbrel pour un déploiement auto-hébergé, le NAT punch-through en utilisant des endpoints publics mémorisés, le nettoyage automatique des exit nodes obsolètes, et une spécification de protocole publiée. Le projet a aussi stabilisé la gestion des routes macOS avec des routes par défaut auto-réparatrices et une réparation de l'underlay, et a ajouté une build Android via Tauri. Des builds sont disponibles pour macOS (Apple Silicon et Intel), Linux (AppImage et .deb), Windows et Android.

### Nymchat abandonne Marmot et livre des chats de groupe NIP-17 renforcés

[Nymchat](https://github.com/Spl0itable/NYM), le client de chat capable de MLS, a livré 14 versions de [v3.56.261](https://github.com/Spl0itable/NYM/releases/tag/3.56.261) à [v3.58.274](https://github.com/Spl0itable/NYM/releases/tag/v3.58.274). Le changement le plus significatif est un pivot protocolaire : [v3.57.261](https://github.com/Spl0itable/NYM/releases/tag/v3.57.261) a ajouté des chats de groupe MLS Marmot, mais [v3.58.268](https://github.com/Spl0itable/NYM/releases/tag/v3.58.268) est revenu à [NIP-17](/fr/topics/nip-17/) parce que le support multi-appareils de Marmot n'est pas encore terminé, ce qui causait des problèmes de synchronisation de l'état des chats de groupe entre appareils. v3.58.271 introduit des chats de groupe NIP-17 renforcés avec des clés éphémères rotatives pour tous les messages, conçues pour prévenir les attaques de timing et de corrélation. La semaine a aussi apporté un système d'amis avec contrôle granulaire des paramètres ([v3.58.262](https://github.com/Spl0itable/NYM/releases/tag/v3.58.262)), la synchronisation des messages de groupe MLS dans les paramètres applicatifs chiffrés, et plusieurs correctifs de connectivité relay.

### nak v0.19.5 ajoute Blossom multi-serveur et la publication outbox

[nak](https://github.com/fiatjaf/nak), la boîte à outils Nostr en ligne de commande de fiatjaf, a livré [v0.19.5](https://github.com/fiatjaf/nak/releases/tag/v0.19.5). La commande `blossom` accepte désormais plusieurs flags `--server` pour téléverser vers plusieurs serveurs [Blossom](/fr/topics/blossom/) en un seul appel. Une nouvelle commande `key` complète les clés partielles en les left-padding avec des zéros. La commande `event` gagne un flag `--outbox` pour publier des événements via le modèle outbox, et `fetch` sort maintenant avec un code d'erreur quand aucun événement n'est renvoyé.

## En développement

### White Noise ajoute des aperçus thumbhash et un pont d'enregistrement push

[White Noise](https://github.com/marmot-protocol/whitenoise), la messagerie privée construite sur le protocole [Marmot](/fr/topics/marmot/), a fusionné cinq PRs. [PR #549](https://github.com/marmot-protocol/whitenoise/pull/549) remplace les aperçus d'images blurhash par thumbhash, un algorithme plus récent qui produit des images placeholder plus nettes avec une charge utile plus petite (généralement moins de 30 bytes contre environ 50-100 bytes pour blurhash) tout en conservant le ratio d'aspect et la distribution de couleurs de l'image d'origine. Blurhash est conservé comme fallback pour les anciens contenus. [PR #548](https://github.com/marmot-protocol/whitenoise/pull/548) met à jour whitenoise-rs et ajoute le pont d'enregistrement push [MIP-05](/fr/topics/mip-05/), connectant [le travail sur la spécification des notifications push de la semaine dernière](/en/newsletters/2026-04-01-newsletter/#marmot-moves-keypackages-to-addressable-events-and-tightens-push-notifications) au client. [PR #493](https://github.com/marmot-protocol/whitenoise/pull/493) ajoute une pagination à curseur pour les messages de chat, remplaçant l'ancienne stratégie de chargement par une approche pilotée par le scroll.

### Route96 ajoute une configuration dynamique des labels et un nettoyage zéro-egress

[Route96](https://github.com/v0l/route96), le serveur média [Blossom](/fr/topics/blossom/) de v0l, a fusionné trois PRs. [PR #80](https://github.com/v0l/route96/pull/80) ajoute la configuration dynamique des modèles de labels via l'API d'administration, permettant aux opérateurs de changer de modèles de classification de contenu sans redémarrer le serveur. [PR #82](https://github.com/v0l/route96/pull/82) ajoute les champs de configuration de labels à l'interface d'administration. [PR #79](https://github.com/v0l/route96/pull/79) ajoute une politique de nettoyage de fichiers zéro-egress qui supprime automatiquement les fichiers qui n'ont jamais été téléchargés, afin de réduire les coûts de stockage pour les opérateurs.

### Snort livre du durcissement de sécurité et des factures de paiement DVM

[Snort](https://github.com/v0l/snort), le client web, a livré deux versions cette semaine avec un audit de sécurité complet. Les correctifs incluent la vérification des signatures Schnorr, la protection [NIP-46](/fr/topics/nip-46/) contre la falsification de messages relay (empêchant des attaquants d'injecter des requêtes de signature via des relays compromis), des améliorations du chiffrement du PIN, et la suppression de la confiance de délégation NIP-26. Les gains de performances viennent d'une vérification Schnorr batchée en WASM, de routes chargées paresseusement, de traductions précompilées et de l'élimination d'une double vérification par événement. [PR #618](https://github.com/v0l/snort/pull/618) ajoute l'affichage de factures kind `7000` [NIP-90](/en/topics/nip-90/) (Data Vending Machine) requérant paiement, de sorte que lorsqu'un DVM répond avec une exigence de paiement, Snort rend la facture Lightning directement dans le flux.

### Damus améliore la compaction LMDB

[Damus](https://github.com/damus-io/damus), le client iOS, a fusionné [PR #3719](https://github.com/damus-io/damus/pull/3719) ajoutant une compaction LMDB automatique planifiée, empêchant la base de données locale de croître sans borne au fil du temps. [PR #3663](https://github.com/damus-io/damus/pull/3663) améliore BlurOverlayView pour lui donner un aspect protecteur plutôt que cassé.

### Captain's Log ajoute l'indexation des tags et la synchronisation des notes

[Captain's Log](https://github.com/nodetec/captains-log) (Comet), l'outil d'écriture long-form natif à Nostr de Nodetec, a fusionné quatre PRs cette semaine. [PR #156](https://github.com/nodetec/captains-log/pull/156) ajoute l'indexation des tags et le support de synchronisation entre les notes, [PR #157](https://github.com/nodetec/captains-log/pull/157) refactorise la synchronisation des notes et la gestion des tags, et [PR #159](https://github.com/nodetec/captains-log/pull/159) corrige la synchronisation des notes mises à la corbeille afin que les notes supprimées restent supprimées sur tous les appareils.

### Relatr v0.2.x repense le système de plugins avec une marketplace de validateurs native à Nostr

[Relatr](https://github.com/ContextVM/relatr), un moteur de scoring [Web of Trust](/fr/topics/web-of-trust/) qui calcule des classements de confiance à partir de la distance dans le graphe social et de validateurs configurables, a livré la famille v0.2.x avec une refonte complète de son système de plugins. Les validateurs sont désormais écrits en Elo, un langage d'expressions fonctionnelles portable forké pour supporter des capacités multi-étapes orchestrées par l'hôte (requêtes Nostr, lookups de graphe social, résolution NIP-05). Les plugins sont publiés comme événements Nostr kind `765`, rendant leur distribution native au réseau relay. Une nouvelle [plugin marketplace](https://relatr.net) permet aux opérateurs de découvrir, installer et pondérer des validateurs depuis le navigateur, avec un CLI (`relo`) pour l'écriture et la publication locales. L'architecture est sandboxée : les plugins ne peuvent invoquer que les capacités que l'hôte fournit explicitement, de sorte qu'un validateur malveillant ne peut pas sortir de son périmètre défini. Les instances Relatr peuvent maintenant être gérées depuis le site web, avec une visibilité complète sur les plugins qui composent l'algorithme de scoring et sur leurs pondérations individuelles.

### Shopstr améliore la navigation mobile et le contrôle d'accès

[Shopstr](https://github.com/shopstr-eng/shopstr), la marketplace native à Nostr pour acheter et vendre avec Bitcoin, a poussé 158 commits cette semaine à travers son application principale et le projet compagnon [Milk Market](https://github.com/shopstr-eng/milk-market). Les correctifs incluent des améliorations de mise en page mobile pour les communautés, la fermeture des menus à la navigation et la fermeture automatique des menus déroulants. Les routes protégées ne peuvent plus être atteintes par URL directe sans connexion, et la logique de matching des slugs gère désormais correctement plusieurs correspondances exactes.

### Pollerama ajoute des notifications, la recherche de films et une nouvelle interface de notation

[Pollerama](https://github.com/formstr-hq/nostr-polls), une application de sondages, enquêtes et notation sociale construite sur Nostr, a ajouté des notifications de fil, une fonctionnalité de recherche de films et une refonte de l'interface de notation. La version corrige aussi des problèmes de chargement du flux et augmente les versions de dépendances.

### Purser construit un daemon de paiement natif à Nostr avec chiffrement Marmot

[Purser](https://github.com/EthnTuttle/purser), un daemon de paiement natif à Nostr conçu comme remplaçant de Zaprite, a fusionné neuf PRs cette semaine pour construire son architecture centrale. Le projet utilise [Marmot](/fr/topics/marmot/) MLS via MDK pour la messagerie chiffrée entre commerçants et clients, avec Strike et Square comme fournisseurs de paiement. Cette semaine ont atterri le chargement de configuration et de catalogue, la validation du schéma des messages, la couche de communication MDK, les implémentations des fournisseurs Strike et Square, un moteur de polling, une limitation anti-spam, la persistance des paiements en attente et le pipeline de traitement des commandes. Les 99 tests exercent maintenant de vraies opérations MLS mdk-core après que l'équipe a retiré le mock MLS au profit d'un chiffrement réel en mode local.

### Vector refactorise les pièces jointes DM et ajoute l'édition de profil

[Vector](https://github.com/VectorPrivacy/Vector), la messagerie Nostr centrée sur la confidentialité construite avec Tauri, a fusionné [PR #55](https://github.com/VectorPrivacy/Vector/pull/55) refactorisant le frontend. Le déchiffrement et la sauvegarde des pièces jointes DM ont été déplacés vers la bibliothèque vector-core, et l'application supporte maintenant l'édition de profil. Le flag d'annulation d'upload est correctement câblé via TauriSendCallback, et les callbacks inutilisés d'aperçu de pièces jointes ont été nettoyés.

## Travail sur le protocole et les spécifications

### Mises à jour des NIP

Changements récents dans le [dépôt NIPs](https://github.com/nostr-protocol/nips) :

**Fusionnés :**

- **[NIP-58](/fr/topics/nip-58/) (Badges) : les Profile Badges passent au kind 10008, les Badge Sets au kind 30008** ([PR #2276](https://github.com/nostr-protocol/nips/pull/2276)) : migre les Profile Badges du kind `30008` vers le kind `10008` (un événement remplaçable, un par pubkey) et introduit le kind `30008` pour les Badge Sets. Auparavant, les Profile Badges utilisaient le même kind (`30008`) que les définitions de badges, ce qui en faisait des événements remplaçables paramétrés indexés par un tag `d`. Le nouveau kind `10008` est un événement remplaçable simple : un par pubkey, sans besoin de tag `d`. Les clients interrogent un seul événement remplaçable par utilisateur au lieu de scanner des événements remplaçables paramétrés. Amethyst v1.07.3 embarque déjà cette migration.

- **[NIP-34](/fr/topics/nip-34/) (Git Stuff) : ajout de follow lists liées à git** ([PR #2130](https://github.com/nostr-protocol/nips/pull/2130)) : ajoute des conventions de follow lists pour le suivi des dépôts et des issues NIP-34. Les utilisateurs publient des ensembles de follow kind `30000` avec des tags `d` comme `git-repos` ou `git-issues` contenant des références de tag `a` vers les dépôts (kind `30617`) qu'ils veulent suivre. Les clients peuvent s'abonner à ces follow sets pour afficher l'activité des dépôts dans le flux d'un utilisateur, de manière similaire au fonctionnement des contact lists kind `3` pour les pubkeys.

**PRs ouvertes et discussions :**

- **NIP-AC : P2P Voice and Video Calls over WebRTC** ([PR #2301](https://github.com/nostr-protocol/nips/pull/2301)) : étend le NIP-100 original (implémenté par 0xChat) avec trois changements : migration vers le chiffrement [NIP-44](/fr/topics/nip-44/) enveloppé dans des gift wraps [NIP-59](/fr/topics/nip-59/) pour éliminer les fuites de métadonnées, workflow WebRTC spécifié pour l'établissement d'appels audio et vidéo (offer, answer, ICE candidates), et modèle d'appel de groupe en mesh où chaque pair établit une connexion WebRTC directe avec chaque autre pair. La spécification n'est pas rétrocompatible avec NIP-100. Amethyst construit déjà contre elle, avec une suite de tests de machine d'état d'appel ([PR #2143](https://github.com/vitorpamplona/amethyst/pull/2143)) et la gestion des offres d'appel obsolètes ([PR #2164](https://github.com/vitorpamplona/amethyst/pull/2164)) livrées cette semaine.

- **[NIP-340](/en/topics/nip-340/) (FROST Quorum)** ([PR #2299](https://github.com/nostr-protocol/nips/pull/2299)) : propose des conventions pour la signature à seuil [FROST](/fr/topics/frost/) (Flexible Round-Optimized Schnorr Threshold) sur Nostr. FROST permet à un groupe de signataires de contrôler collectivement une identité Nostr où n'importe quels membres t-of-n peuvent signer des événements sans reconstruire la clé privée complète. Le NIP définit comment coordonner les rounds de signature, distribuer les key shares et publier des événements signés à seuil, en s'appuyant sur le travail du signataire Igloo du [projet FROSTR](/en/newsletters/2026-04-01-newsletter/#igloo-signer-11).

- **[NIP-5D](/en/topics/nip-5d/) (Nostr Web Applets)** ([PR #2303](https://github.com/nostr-protocol/nips/pull/2303)) : définit un protocole `postMessage` pour des applications web sandboxées (« napplets ») tournant dans des iframes et communiquant avec une application hôte (« shell »). Le shell fournit à la napplet la signature Nostr, l'accès relay et le contexte utilisateur via une API de messages structurée, tandis que la sandbox iframe empêche l'accès direct aux clés. Cela étend le modèle d'hébergement de sites web statiques de [NIP-5A](/en/topics/nip-5a/) vers des applications interactives capables de lire et d'écrire des événements Nostr. Le NIP est en développement actif avec une implémentation runtime fonctionnelle.

- **[NIP-5C](/en/topics/nip-5c/) (Scrolls)** ([PR #2281](https://github.com/nostr-protocol/nips/pull/2281)) : renommé depuis l'ancienne proposition NIP-A5. Définit des conventions pour publier et découvrir des programmes WebAssembly sur Nostr. Les binaires WASM sont stockés comme événements Nostr, et les clients peuvent les télécharger puis les exécuter dans un runtime sandboxé. Une [demo app](https://nprogram.netlify.app/) montre des scrolls s'exécutant dans le navigateur, avec des programmes exemples publiés comme événements Nostr que n'importe quel client peut récupérer et exécuter.

- **[NIP-85](/fr/topics/nip-85/) (Trusted Assertions) : clarifications** ([PR #2304](https://github.com/nostr-protocol/nips/pull/2304)) : resserre le langage de la spécification autour de multiples clés et relays par fournisseur de services, en clarifiant comment les clients doivent gérer des assertions provenant de fournisseurs opérant à travers plusieurs pubkeys ou endpoints relay.

- **[NIP-24](/fr/topics/nip-24/) (Extra Metadata Fields) : `published_at` pour les événements remplaçables** ([PR #2300](https://github.com/nostr-protocol/nips/pull/2300)) : généralise le tag `published_at` depuis [NIP-23](/en/topics/nip-23/) (Long-form Content) à tous les événements remplaçables et adressables. Le tag est seulement destiné à l'affichage : si `published_at` égale `created_at`, les clients affichent l'événement comme « créé » à ce moment-là ; s'ils diffèrent (parce que l'événement a été mis à jour), les clients peuvent l'afficher comme « mis à jour » à la place. Cela permet aux profils kind `0` d'afficher des dates « joined at » et à d'autres événements remplaçables de préserver leur timestamp de publication d'origine à travers les mises à jour. Une proposition complémentaire [NIP-51](/fr/topics/nip-51/) ([PR #2302](https://github.com/nostr-protocol/nips/pull/2302)) ajoute le même tag aux événements de listes.

- **[NIP-59](/fr/topics/nip-59/) (Gift Wrap) : kind de gift wrap éphémère** ([PR #2245](https://github.com/nostr-protocol/nips/pull/2245)) : ajoute le kind `21059` comme contrepartie éphémère au gift wrap kind `1059` existant. Les événements éphémères (kinds `20000`-`29999`) suivent la sémantique [NIP-01](/fr/topics/nip-01/) : les relays ne sont pas censés les stocker et peuvent les supprimer après livraison. Cela permet aux applications d'envoyer des messages gift-wrapped qui disparaissent des relays une fois livrés, réduisant les besoins de stockage pour la messagerie à fort volume tout en conservant le même modèle de chiffrement à trois couches que les DMs [NIP-17](/fr/topics/nip-17/) classiques.

### OpenSats annonce sa seizième vague de subventions Nostr

[OpenSats](https://opensats.org) a annoncé sa [seizième vague de subventions Nostr](https://opensats.org/blog/sixteenth-wave-of-nostr-grants) le 8 avril, finançant quatre premières subventions et un renouvellement. [Amethyst Desktop](https://github.com/vitorpamplona/amethyst/tree/main/desktopApp) reçoit un financement pour que le contributeur Robert Nagy construise une application desktop autonome au-dessus des modules [Quartz](/fr/topics/quartz/) et Commons, apportant l'ensemble des fonctionnalités du client Android à des interfaces pilotées à la souris avec connexions relay persistantes. [Nostr Mail](https://github.com/nogringo/nostr-mail) reçoit un financement pour construire un système email complet sur Nostr en utilisant des événements kind `1301` enveloppés dans des gift wraps [NIP-59](/fr/topics/nip-59/), avec un client Flutter et des serveurs de pont SMTP pour la compatibilité Gmail/Outlook. [Nostrord](https://github.com/Nostrord/nostrord) reçoit un financement pour un client de groupe basé sur relay [NIP-29](/en/topics/nip-29/) en Kotlin Multiplatform avec messagerie de groupe, modération et fils à la Discord. [Nurunuru](https://github.com/tami1A84/null--nostr) reçoit un financement pour construire une version iOS native du client Nostr japonais inspirée de l'interface familière de LINE, avec connexion biométrique basée sur passkey pour l'onboarding. HAMSTR a reçu un renouvellement de subvention (financé pour la première fois lors de la [onzième vague](https://opensats.org/blog/eleventh-wave-of-nostr-grants#hamstr)).

## Deep Dive NIP : NIP-17 (Private Direct Messages)

[NIP-17](https://github.com/nostr-protocol/nips/blob/master/17.md) définit le standard actuel des messages directs privés sur Nostr. Il remplace l'ancien schéma [NIP-04](/fr/topics/nip-04/) (Encrypted Direct Messages), qui laissait fuiter des métadonnées (expéditeur, destinataire et timestamps étaient tous visibles sur les relays) et utilisait une construction de chiffrement plus faible. NIP-17 combine [NIP-44](/fr/topics/nip-44/) (Encrypted Payloads) pour le chiffrement avec [NIP-59](/fr/topics/nip-59/) (Gift Wrap) pour la protection des métadonnées, créant un système à trois couches où les relays ne peuvent pas voir qui parle avec qui.

Le protocole utilise trois kinds d'événements empilés les uns dans les autres. La couche la plus interne est le message réel, un événement kind `14` non signé :

```json
{
  "id": "a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744108800,
  "kind": 14,
  "tags": [
    ["p", "f1a2b3c4d5e6f7890123456789abcdef01234567890abcdef1234567890abcdef", "wss://inbox.example.com"],
    ["subject", "Project update"]
  ],
  "content": "The new relay config is deployed. Let me know if you see any issues.",
  "sig": ""
}
```

L'événement kind `14` est volontairement non signé (`sig` vide). La spécification présente cela comme une forme de déni plausible, mais en pratique cette protection reste limitée. Le seal kind `13` qui enveloppe la rumor est signé avec la vraie clé de l'expéditeur. Un destinataire peut montrer ce seal signé à un tiers, prouvant que l'expéditeur a communiqué avec lui, même sans révéler le contenu du message. Avec des preuves à divulgation nulle de connaissance, un destinataire peut prouver le contenu exact du message sans révéler sa propre clé privée. La rumor non signée ressemble à une lettre non signée placée dans une enveloppe signée : la signature de l'enveloppe relie l'expéditeur au contenu. Un véritable déni exigerait une authentification symétrique (comme les HMACs de Signal), ce qui est incompatible avec le modèle relay décentralisé de Nostr où les messages doivent être auto-authentifiants. Les véritables forces de NIP-17 sont la confidentialité des métadonnées et le secret du contenu, pas le déni plausible.

Ce message non signé est ensuite enveloppé dans un seal kind `13`, signé par l'expéditeur réel et chiffré avec [NIP-44](/fr/topics/nip-44/) pour le destinataire :

```json
{
  "id": "b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744022400,
  "kind": 13,
  "tags": [],
  "content": "<nip44-encrypted kind 14 payload>",
  "sig": "e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4"
}
```

Le seal n'a pas de tags, donc même déchiffré il ne révélerait pas le destinataire. Le seal est signé avec la vraie clé de l'expéditeur, ce qui permet au destinataire d'authentifier le message en vérifiant que le `pubkey` du seal correspond au `pubkey` du kind `14` interne.

Le seal est ensuite enveloppé dans un gift wrap kind `1059`, signé avec une clé aléatoire jetable et adressé au destinataire :

```json
{
  "id": "c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2",
  "pubkey": "9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba",
  "created_at": 1744065600,
  "kind": 1059,
  "tags": [
    ["p", "f1a2b3c4d5e6f7890123456789abcdef01234567890abcdef1234567890abcdef"]
  ],
  "content": "<nip44-encrypted kind 13 payload>",
  "sig": "fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210"
}
```

Le `pubkey` du gift wrap est une clé aléatoire générée uniquement pour ce message, et `created_at` est randomisé jusqu'à deux jours dans le passé. C'est la couche la plus externe que les relays voient réellement : un message provenant d'un pubkey inconnu adressé au destinataire, avec un timestamp qui ne reflète pas le moment réel d'envoi. Le timestamp randomisé protège contre les analyses a posteriori d'événements stockés, mais un adversaire activement connecté aux relays peut quand même observer quand le gift wrap apparaît pour la première fois, donc cette défense se limite aux observateurs passifs qui interrogent plus tard les données relay. Parce que le pubkey est aléatoire et que le timestamp est faux, les relays ne peuvent pas déterminer l'expéditeur réel. Pour lire le message, le destinataire déchiffre le gift wrap en utilisant sa propre clé et le pubkey aléatoire, trouve le seal à l'intérieur, déchiffre le seal en utilisant sa propre clé et le pubkey de l'expéditeur présent dans le seal, puis trouve le message kind `14` à l'intérieur.

NIP-17 ne fournit pas de forward secrecy. Tous les messages sont chiffrés à l'aide de la paire de clés Nostr statique (via la dérivation de clés de NIP-44 à partir des clés de l'expéditeur et du destinataire). Si une clé privée est compromise, chaque message passé et futur chiffré pour cette clé peut être déchiffré. C'est un compromis délibéré : comme le chiffrement dépend seulement du nsec, un utilisateur qui sauvegarde son nsec peut récupérer tout son historique de messages depuis n'importe quel relay qui stocke encore les gift wraps. Des protocoles comme MLS (utilisé par [Marmot](/fr/topics/marmot/)) fournissent la forward secrecy via une rotation du matériel de clé, mais au prix d'exiger une synchronisation d'état et de rendre impossible la récupération de l'historique après rotation des clés.

NIP-17 définit aussi le kind `15` pour les messages de fichiers chiffrés, qui ajoute les tags `file-type`, `encryption-algorithm`, `decryption-key` et `decryption-nonce` afin que le destinataire puisse déchiffrer un fichier joint chiffré avec AES-GCM avant téléversement vers un serveur Blossom. Le kind `10050` est utilisé pour publier la liste des relays DM préférés de l'utilisateur, afin que les expéditeurs sachent où livrer les gift wraps. L'ensemble des tags `pubkey` + `p` dans un message définit un salon de chat ; ajouter ou retirer un participant crée un nouveau salon avec un historique propre.

Les implémentations couvrent la plupart des grands clients. [nospeak](https://github.com/psic4t/nospeak) utilise NIP-17 pour toute la messagerie one-on-one. [Flotilla](https://gitea.coracle.social/coracle/flotilla) utilise NIP-17 pour ses DMs proof-of-work. [Amethyst](https://github.com/vitorpamplona/amethyst), [Primal](https://github.com/PrimalHQ/primal-android-app), [Nostur](https://github.com/nostur-com/nostur-ios-public), [Damus](https://github.com/damus-io/damus), [noStrudel](https://github.com/hzrd149/nostrudel), et [Coracle](https://github.com/coracle-social/coracle) implémentent tous NIP-17 comme protocole DM principal. La spécification supporte aussi les messages éphémères en définissant un tag `expiration` dans le gift wrap.

## Deep Dive NIP : NIP-46 (Nostr Remote Signing)

[NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md) définit un protocole permettant de séparer la clé privée de l'utilisateur de l'application cliente. Au lieu de coller un nsec dans une web app, l'utilisateur exécute un signataire distant (aussi appelé « bunker ») qui détient la clé privée et répond aux requêtes de signature via les relays Nostr. Le client ne voit jamais la clé privée. Cela réduit la surface d'attaque : un client compromis peut demander des signatures, mais ne peut pas extraire la clé elle-même.

Le protocole utilise le kind `24133` à la fois pour les requêtes et les réponses, chiffrées avec [NIP-44](/fr/topics/nip-44/) (Encrypted Payloads). Un client génère une `client-keypair` jetable pour la session et communique avec le signataire distant via des messages chiffrés NIP-44 tagués avec les pubkeys respectifs. Voici une requête de signature d'un client vers un signataire distant :

```json
{
  "id": "aa11bb22cc33dd44ee55ff6677889900aabbccdd11223344556677889900aabb",
  "pubkey": "eff37350d839ce3707332348af4549a96051bd695d3223af4aabce4993531d86",
  "created_at": 1744108800,
  "kind": 24133,
  "tags": [
    ["p", "fa984bd7dbb282f07e16e7ae87b26a2a7b9b90b7246a44771f0cf5ae58018f52"]
  ],
  "content": "<nip44-encrypted JSON-RPC request>",
  "sig": "1122334455667788990011223344556677889900aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff0011223344556677"
}
```

Le `content` chiffré contient une structure de type JSON-RPC :

```json
{
  "id": "random-request-id-1",
  "method": "sign_event",
  "params": ["{\"kind\":1,\"content\":\"Hello from remote signing\",\"tags\":[],\"created_at\":1744108800}"]
}
```

Le signataire distant déchiffre la requête, la présente à l'utilisateur pour approbation (ou l'auto-approuve selon les permissions configurées), signe l'événement avec la clé privée de l'utilisateur, puis renvoie l'événement signé dans une réponse :

```json
{
  "id": "bb22cc33dd44ee55ff6677889900aabb11223344556677889900aabbccddeeff",
  "pubkey": "fa984bd7dbb282f07e16e7ae87b26a2a7b9b90b7246a44771f0cf5ae58018f52",
  "created_at": 1744108801,
  "kind": 24133,
  "tags": [
    ["p", "eff37350d839ce3707332348af4549a96051bd695d3223af4aabce4993531d86"]
  ],
  "content": "<nip44-encrypted JSON-RPC response>",
  "sig": "aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899"
}
```

Les connexions peuvent être initiées depuis n'importe quel côté. Un signataire distant fournit une URL `bunker://` contenant son pubkey et les informations relay. Un client fournit une URL `nostrconnect://` avec son pubkey client, ses relays et un secret de vérification de connexion. Le paramètre `secret` empêche l'usurpation de connexion : seule la partie qui a reçu l'URL hors bande peut terminer le handshake.

Huit méthodes sont définies : `connect` pour établir la session, `sign_event` pour signer des événements, `get_public_key` pour apprendre le pubkey de l'utilisateur, `ping` pour le keepalive, `nip04_encrypt`/`nip04_decrypt` pour l'ancien chiffrement, `nip44_encrypt`/`nip44_decrypt` pour le chiffrement actuel, et `switch_relays` pour la gestion des relays. La migration relay est gérée par le signataire distant, qui peut déplacer la connexion vers de nouveaux relays au fil du temps sans casser la session.

Les clients demandent des capacités spécifiques au moment de la connexion via un système de permissions. Une chaîne de permissions comme `nip44_encrypt,sign_event:1,sign_event:14` demande l'accès au chiffrement NIP-44 et l'accès à la signature pour les événements kind `1` et kind `14` seulement. Le signataire distant peut accepter, rejeter ou modifier ces permissions. Cela signifie qu'un client web pour lire et publier des notes peut n'obtenir que la permission `sign_event:1`, tandis qu'un client DM peut aussi obtenir `sign_event:14` et `nip44_encrypt`.

[Amber](https://github.com/greenart7c3/Amber) implémente NIP-46 sur Android, et sa [v6.0.0-pre1](#amber-v600-pre1-ajoute-des-cles-de-signature-nip-46-par-connexion) de cette semaine ajoute des clés de signature par connexion pour isoler les clients. [nsec.app](https://github.com/nicktee/nsecapp) (anciennement Nostr Connect) fournit un bunker web. [nostr-tools](https://github.com/nbd-wtf/nostr-tools) inclut `BunkerSigner` pour les clients JavaScript, et [la PR #530 de la semaine dernière](/en/newsletters/2026-04-01-newsletter/#nostr-tools-adds-bunker-relay-control-and-fixes-nip-47-multi-relay-parsing) a ajouté `skipSwitchRelays` pour une gestion manuelle des relays. Le protocole supporte aussi les défis d'auth : lorsqu'un signataire distant a besoin d'une authentification supplémentaire (mot de passe, biométrie ou token matériel), il répond avec une `auth_url` que le client ouvre dans un navigateur pour que l'utilisateur termine l'opération.

---

C'est tout pour cette semaine. Vous construisez quelque chose ou avez des nouvelles à partager ? Envoyez-nous un DM sur Nostr ou retrouvez-nous sur [nostrcompass.org](https://nostrcompass.org).
