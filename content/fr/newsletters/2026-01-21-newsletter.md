---
title: 'Nostr Compass #6'
date: 2026-01-21
publishDate: 2026-01-21
draft: false
type: newsletters
---

Bon retour sur Nostr Compass, votre guide hebdomadaire sur Nostr.

**Cette semaine :** Bitchat remplace le Tor en C par l'implémentation Rust Arti pour une meilleure fiabilité et performance. nostrdb-rs gagne des requêtes fold en streaming qui permettent des opérations de base de données sans allocation. Listr reçoit une refonte majeure avec migration vers NDK 3 beta et maintenance assistée par IA après un an de dormance. Zeus livre 17 PR fusionnées axées sur les correctifs [NIP-47](/fr/topics/nip-47/) (Nostr Wallet Connect pour le contrôle Lightning à distance) et les améliorations Cashu, tandis que Primal Android ajoute des flux de sauvegarde de portefeuille et le support [NIP-92](/fr/topics/nip-92/) (dimensions de média pour des ratios d'aspect corrects). Un nouveau NIP brouillon propose les [Assertions de Relais de Confiance](/fr/topics/trusted-relay-assertions/) pour une notation de confiance standardisée des relais.

## Actualités

### Bitchat adopte Rust Arti pour le support Tor

Bitchat a migré du Tor en C vers [Arti](https://gitlab.torproject.org/tpo/core/arti), l'implémentation Rust du protocole Tor. [PR #958](https://github.com/permissionlesstech/bitchat/pull/958) supprime la dépendance au Tor en C et intègre Arti, apportant des garanties de sécurité mémoire et une fiabilité améliorée. Le changement élimine les tentatives de réveil en dormance qui causaient des redémarrages du service en premier plan, un problème persistant avec l'implémentation en C.

**Ce que cela signifie pour les utilisateurs :** Messagerie chiffrée plus stable avec moins de déconnexions, en particulier sur les appareils mobiles. L'implémentation Rust réduit les risques de plantage et la consommation de batterie due aux tentatives de reconnexion constantes.

Arti est une réécriture complète de Tor en Rust, développée par le projet Tor pour offrir une meilleure sécurité grâce à la sûreté mémoire et une intégration plus facile dans les applications. Pour Bitchat, les propriétés de sûreté mémoire réduisent la surface d'attaque lors du traitement des messages chiffrés et des connexions relais. La migration fait suite au récent [audit de sécurité Cure53](/fr/newsletters/2026-01-13-newsletter/#bitchat-termine-laudit-de-sécurité-cure53) de l'équipe (couvert dans la Newsletter #5), poursuivant leurs améliorations de sécurité.

La PR introduit également une couverture de tests complète pour ChatViewModel et BLEService, supprime le code mort et stabilise la suite de tests. Les améliorations de fiabilité du maillage Bluetooth Low Energy accompagnent les changements Tor, traitant les échecs de transferts importants. Ensemble, ces changements améliorent la résilience de Bitchat pour les scénarios de réseau maillé hors ligne où Tor fournit la connectivité Internet aux côtés de la communication BLE locale.


### Listr revitalisé avec maintenance assistée par IA

JeffG a annoncé une refonte majeure de [Listr](https://github.com/erskingardner/listr), l'application de gestion de listes Nostr disponible sur [listr.lol](https://listr.lol), après que le projet avait été en dormance pendant plus d'un an. Avec l'assistance IA, il a complété une mise à niveau complète incluant la migration vers [NDK](https://github.com/nostr-dev-kit/ndk) 3 beta, les mises à jour vers les dernières versions de Svelte et Vite, et toutes les dépendances mises à jour. La refonte ajoute un support de première classe pour les packs de suivi, implémente la pagination pour les listes dépassant 50 éléments et corrige de nombreux bugs qui s'étaient accumulés pendant la période de dormance.

**Ce que cela signifie pour les utilisateurs :** Listr est de retour en ligne avec des performances améliorées et de nouvelles fonctionnalités pour gérer les listes de suivi, les collections de contenu et la curation de sujets. Le correctif de pagination rend les grandes listes réellement utilisables.

JeffG a noté que sans l'assistance IA, ce travail de maintenance n'aurait probablement jamais eu lieu, empêchant le projet d'être abandonné. Listr permet la curation de contenu sur Nostr, permettant aux utilisateurs de créer, gérer et partager des listes de profils, sujets et ressources. La mise à niveau maintient l'application compatible avec les normes Nostr actuelles et les attentes des clients alors que la gestion des listes devient plus centrale pour la découverte de contenu sur le protocole.


## Mises à jour des NIP

Changements récents dans le [dépôt NIPs](https://github.com/nostr-protocol/nips) :

**Fusionnées :**

- **[NIP-29](/fr/topics/nip-29/)** (Groupes basés sur les relais) - Clarification de la clé de relais ([#2190](https://github.com/nostr-protocol/nips/pull/2190) - fusionnée) clarifie que la clé de relais est l'URL du relais elle-même, pas une pubkey. La spécification indique maintenant explicitement "La clé de relais est l'URL WebSocket du relais (par ex., wss://groups.example.com)" pour éviter toute confusion. Cela affecte la façon dont les clients identifient quel relais héberge un groupe donné, garantissant que les groupes sont correctement attribués à leurs relais d'hébergement.

**PR ouvertes et discussions :**

- **Assertions de Relais de Confiance** - Un NIP brouillon propose de standardiser la notation de confiance des relais via des événements kind 30385 contenant des scores de confiance (0-100) calculés à partir des métriques [NIP-66](/fr/topics/nip-66/) (découverte et surveillance de relais), de la réputation de l'opérateur et des rapports utilisateurs. La spécification divise la confiance en composantes de fiabilité (disponibilité, latence), qualité (TLS, documentation, vérification de l'opérateur) et accessibilité (juridiction, barrières, risque de surveillance). La vérification de l'opérateur inclut des signatures cryptographiques via [NIP-11](/fr/topics/nip-11/) (documents d'information de relais), des enregistrements DNS TXT et des fichiers .well-known. Les utilisateurs déclarent les fournisseurs d'assertions de confiance via des événements kind 10385, permettant aux clients d'interroger plusieurs fournisseurs pour des perspectives diverses. La proposition complète la découverte [NIP-66](/fr/topics/nip-66/) avec l'évaluation, aidant [NIP-46](/fr/topics/nip-46/) (signature à distance/Nostr Connect) à évaluer la fiabilité des relais dans les URI de connexion.

- **Cryptographie post-quantique** - [PR #2185](https://github.com/nostr-protocol/nips/pull/2185) (ouverte) continue d'évoluer depuis que la [Newsletter #5](/fr/newsletters/2026-01-13-newsletter/#mises-à-jour-des-nip) a introduit la proposition pour des algorithmes résistants aux attaques quantiques. La discussion de cette semaine s'est concentrée sur les détails d'implémentation pour la crypto-agilité : comment les clients gèrent les signatures doubles pendant la migration, la rétrocompatibilité pour les anciens clients et les implications de performance des signatures résistantes quantiques plus grandes. Les contributeurs ont débattu de la nécessité de n'imposer que ML-DSA-44 ou de supporter plusieurs algorithmes (ML-DSA-44, Falcon-512, Dilithium) pour la flexibilité. Le consensus penche vers une approche progressive : signatures quantiques optionnelles initialement, devenant obligatoires seulement après un support client généralisé et l'émergence d'une menace quantique réelle.


## Plongée approfondie dans les NIP : NIP-11 et NIP-66

Cette semaine, nous examinons deux NIP qui fonctionnent ensemble pour permettre la découverte et l'évaluation des relais : NIP-11 définit comment les relais se décrivent, et NIP-66 standardise comment nous mesurons le comportement des relais. Ensemble, ils forment la base des systèmes d'évaluation de la confiance des relais.

### [NIP-11](/fr/topics/nip-11/) : Document d'information de relais

[NIP-11](https://github.com/nostr-protocol/nips/blob/master/11.md) définit un document JSON que les relais servent via HTTP pour décrire leurs capacités, politiques et informations d'opérateur. Lorsqu'un client se connecte à `wss://relay.example.com`, il peut récupérer `https://relay.example.com` (en remplaçant `wss://` par `https://`) pour obtenir le document d'information du relais.

Le document utilise la négociation de contenu HTTP standard avec l'en-tête `Accept: application/nostr+json`. Cela permet aux relais de servir leur site web normal aux navigateurs tout en fournissant des métadonnées lisibles par machine aux clients Nostr. La réponse inclut le nom du logiciel de relais et la version, les informations de contact de l'opérateur (pubkey, email, contact alternatif), les NIP supportés et les paramètres opérationnels comme les exigences de paiement ou les restrictions de contenu.

Important, les documents NIP-11 de base sont du JSON non signé servi via HTTPS, s'appuyant uniquement sur les certificats TLS pour l'authenticité. Cela signifie que quiconque contrôle le serveur web du relais peut modifier le document, rendant les déclarations de l'opérateur invérifiables. La proposition d'Assertions de Relais de Confiance répond à cette lacune en introduisant des attestations signées via le champ `self` pubkey d'un relais, permettant une preuve cryptographique de l'identité de l'opérateur similaire à la façon dont les relais utilisent des événements signés pour les mécanismes d'authentification.

```json
{
  "name": "relay.example.com",
  "description": "Un relais public à usage général",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "contact": "admin@example.com",
  "supported_nips": [1, 2, 4, 9, 11, 12, 16, 20, 22],
  "software": "git+https://github.com/relay/relay.git",
  "version": "1.2.3",
  "limitation": {
    "max_message_length": 16384,
    "max_subscriptions": 20,
    "max_filters": 100,
    "max_limit": 5000,
    "max_subid_length": 100,
    "min_prefix": 4,
    "max_event_tags": 2000,
    "max_content_length": 8196,
    "min_pow_difficulty": 0,
    "auth_required": false,
    "payment_required": false
  },
  "payments_url": "https://relay.example.com/payments",
  "fees": {
    "admission": [{"amount": 5000, "unit": "msats"}],
    "subscription": [{"amount": 1000, "unit": "msats", "period": 2592000}],
    "publication": []
  }
}
```

L'objet `limitation` indique aux clients quelles contraintes le relais applique. `max_message_length` limite la taille des trames WebSocket, `max_subscriptions` limite le nombre d'abonnements REQ simultanés par connexion, `max_filters` limite les filtres par REQ, et `max_limit` restreint combien d'événements un seul filtre peut demander. Ces paramètres aident les clients à adapter leur comportement aux capacités des relais, évitant les déconnexions dues au dépassement des limites.

Les informations de paiement apparaissent dans `fees` et `payments_url`. Les relais peuvent facturer pour l'admission (accès unique), l'abonnement (accès récurrent) ou la publication (frais par événement). Le `payments_url` pointe vers les détails sur les méthodes de paiement, généralement des factures Lightning ou des coffres ecash. Les relais payants utilisent ces champs pour communiquer les tarifs avant que les clients tentent l'authentification.

Le tableau `supported_nips` permet aux clients de découvrir les capacités des relais. Si un relais liste [NIP-50](/fr/topics/nip-50/), les clients savent qu'ils peuvent envoyer des requêtes de recherche en texte intégral. Si [NIP-42](/fr/topics/nip-42/) apparaît, les clients doivent s'attendre à des défis d'authentification. Cette publicité déclarative des capacités permet une amélioration progressive : les clients peuvent utiliser des fonctionnalités avancées là où elles sont disponibles tout en se dégradant gracieusement sur les relais avec un support limité.

Les informations sur l'opérateur renforcent la responsabilité. Le champ `pubkey` identifie l'opérateur du relais sur Nostr, permettant la communication directe via les DM [NIP-17](/fr/topics/nip-17/) ou les mentions publiques. L'email `contact` fournit un repli hors protocole. Ensemble, ces champs aident les utilisateurs à joindre les opérateurs pour signaler des abus, demander l'accès ou résoudre des problèmes techniques.

Les documents [NIP-11](/fr/topics/nip-11/) sont auto-déclarés : les relais décrivent ce qu'ils prétendent supporter, pas nécessairement ce qu'ils font réellement. C'est là que NIP-66 devient important.

### [NIP-66](/fr/topics/nip-66/) : Découverte de relais et surveillance de disponibilité

[NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) standardise la publication des données de surveillance de relais sur Nostr. Les services de surveillance testent en continu les relais pour la disponibilité, la latence, la conformité au protocole et les NIP supportés. Ils publient les résultats sous forme d'événements kind 30166, fournissant un état de relais en temps réel indépendant de l'auto-déclaration des relais.

Les moniteurs vérifient la disponibilité des relais en se connectant et en envoyant des abonnements de test. Les mesures de latence suivent le temps de connexion, le temps de réponse d'abonnement et le délai de propagation d'événement. Les tests de conformité au protocole vérifient que le comportement du relais correspond aux spécifications, détectant les bugs d'implémentation ou les déviations intentionnelles. La vérification du support NIP va au-delà des déclarations [NIP-11](/fr/topics/nip-11/) en testant réellement si les fonctionnalités annoncées fonctionnent correctement.

```json
{
  "id": "a34b5c7d89e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7",
  "pubkey": "4e2d0bc6f8e7c3a5b9f1d2e3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4",
  "created_at": 1736784000,
  "kind": 30166,
  "tags": [
    ["d", "wss://relay.example.com"],
    ["rtt", "open", "143", "1736784000"],
    ["rtt", "read", "89", "1736784000"],
    ["rtt", "write", "92", "1736784000"],
    ["nips", "1", "2", "4", "9", "11", "12"],
    ["geo", "US", "United States", "New York"],
    ["other", "network", "clearnet"],
    ["other", "payment_required", "false"],
    ["other", "auth_required", "false"]
  ],
  "content": "{\"last_check\": 1736784000, \"checks\": 8760}",
  "sig": "8b9c4d5e6a7f8b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b"
}
```

Le tag `d` contient l'URL du relais, faisant de ceci un événement remplaçable paramétré. Chaque moniteur publie un événement par relais, mis à jour au fur et à mesure que les mesures changent. Plusieurs moniteurs peuvent suivre le même relais, fournissant redondance et validation croisée. Les clients interrogent plusieurs pubkeys de moniteurs pour obtenir des perspectives diverses sur la santé des relais.

Les tags de temps d'aller-retour (rtt) mesurent la latence pour différentes opérations. `rtt open` suit l'établissement de connexion WebSocket, `rtt read` mesure le temps de réponse d'abonnement et `rtt write` teste la vitesse de publication d'événement. Toutes les valeurs sont en millisecondes. Les clients utilisent ces métriques pour préférer les relais à faible latence pour les opérations sensibles au temps ou dé-prioriser les relais lents.

Le tag `nips` liste le support NIP réellement vérifié, pas seulement le support revendiqué. Les moniteurs testent chaque NIP en exerçant sa fonctionnalité. Si un relais revendique la recherche [NIP-50](/fr/topics/nip-50/) dans son document [NIP-11](/fr/topics/nip-11/) mais que les requêtes de recherche échouent, les moniteurs omettront NIP-50 de la liste vérifiée. Cela fournit une vérité terrain sur les capacités des relais.

Les informations géographiques aident les clients à sélectionner des relais proches pour une meilleure latence et résistance à la censure. Le tag `geo` contient le code pays, le nom du pays et la région. Le tag `network` distingue les relais clearnet des services cachés Tor ou des points de terminaison I2P. Ensemble, ces tags permettent la diversité géographique : les clients peuvent se connecter à des relais dans plusieurs juridictions pour résister à la censure régionale.

Les données de surveillance alimentent les sélecteurs de relais dans les clients, les sites web explorateurs et la proposition d'Assertions de Relais de Confiance. En combinant les documents [NIP-11](/fr/topics/nip-11/) auto-déclarés avec les données [NIP-66](/fr/topics/nip-66/) mesurées et les assertions de confiance calculées, l'écosystème évolue vers une sélection de relais informée plutôt que de s'appuyer sur des valeurs par défaut codées en dur ou des recommandations de bouche à oreille.

## Sorties

### 0xchat v1.5.3 - Fonctionnalités de messagerie améliorées

[0xchat v1.5.3](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.3-release) apporte des améliorations significatives au client de messagerie Nostr de style Telegram. La version corrige les problèmes de conformité [NIP-55](/fr/topics/nip-55/) (application de signature Android) qui empêchaient la signature correcte des événements via des signataires externes comme Amber. La conformité totale signifie que 0xchat délègue maintenant correctement les opérations de signature, améliorant la sécurité en gardant les clés privées isolées.

La mise à jour intègre à la fois FileDropServer et BlossomServer comme options de stockage de média par défaut, offrant aux utilisateurs une redondance pour les téléchargements de fichiers. [Blossom](https://github.com/hzrd149/blossom) fournit un stockage adressable par contenu où les fichiers sont référencés par leurs hachages SHA-256, garantissant l'intégrité et permettant la déduplication sur le réseau. L'enregistrement automatique des brouillons pour Moments empêche la perte de données lors de la composition de contenu long, répondant aux plaintes des utilisateurs concernant les publications perdues lors des changements d'application ou des interruptions de connectivité.

L'intégration du portefeuille Cashu reçoit un polissage avec un filtrage automatique des preuves qui supprime les jetons dépensés de la vue du portefeuille. Cela résout l'UX confuse où les utilisateurs voyaient des preuves invalides aux côtés de l'ecash valide, rendant les calculs de solde peu fiables. Le filtrage se fait côté client, maintenant la confidentialité tout en améliorant l'expérience de paiement pour les transactions pair-à-pair dans les discussions.

### Amber v4.1.0 Pré-versions - Refonte de l'interface

[Amber v4.1.0-pre1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.0-pre1) à [v4.1.0-pre3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.0-pre3) introduisent une interface repensée pour le signataire d'événements Android populaire. L'écran de connexion affiche maintenant clairement quelle application demande des permissions de signature, répondant à la confusion des utilisateurs concernant les flux d'autorisation. Le nouvel écran d'événements fournit une inspection détaillée des données que les applications veulent signer, permettant aux utilisateurs de prendre des décisions de sécurité éclairées avant d'approuver les opérations.

La gestion des permissions reçoit une attention significative avec une interface remaniée montrant exactement quelles capacités chaque application connectée a été accordée. Les utilisateurs peuvent révoquer des permissions spécifiques sans se déconnecter entièrement, permettant un contrôle fin sur la délégation de signature. Les compteurs de relais refactorisés utilisant la bibliothèque quartz mise à jour fournissent des statistiques en temps réel sur le débit d'événements et les performances des relais. Les connexions bunker [NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md) (Nostr Connect) affichent maintenant des messages d'erreur détaillés lorsque les connexions échouent, remplaçant les erreurs de délai d'attente cryptiques par des diagnostics exploitables.

## Changements notables de code et de documentation

*Ce sont des pull requests fusionnées et des développements en phase précoce qui méritent d'être suivis. Certains sont des fonctionnalités expérimentales qui peuvent évoluer avant la sortie.*

### Zeus (Portefeuille Lightning avec Nostr Wallet Connect)

Zeus a fusionné 17 pull requests cette semaine, renforçant sa position en tant qu'implémentation [NIP-47](/fr/topics/nip-47/) Nostr Wallet Connect leader. Les correctifs les plus significatifs traitent les problèmes de cohérence des données et de conformité au protocole qui causaient des problèmes d'interopérabilité avec les clients Nostr.

**Correctif de l'historique des transactions** - [PR #3542](https://github.com/ZeusLN/zeus/pull/3542) résout un bug critique où les listes de transactions NWC affichaient des entrées incorrectes ou dupliquées. Le problème se produisait lorsque Zeus mettait en cache les données de transaction sans gérer correctement les mises à jour d'événements, amenant les utilisateurs à voir des transactions fantômes ou des paiements manquants. Le correctif implémente une déduplication d'événements appropriée et une invalidation de cache, garantissant que l'historique des transactions reflète avec précision l'état du nœud Lightning.

**Conformité au protocole** - [PR #3548](https://github.com/ZeusLN/zeus/pull/3548) traite les réponses `getInfo` incomplètes qui cassaient la compatibilité avec les clients attendant une conformité NIP-47 complète. Certains clients Nostr plantaient lors de la réception de réponses partielles manquant de champs comme `block_height` ou `network`. La PR garantit que tous les champs requis retournent avec des valeurs par défaut sensées même lorsque l'implémentation Lightning sous-jacente ne les fournit pas, améliorant la compatibilité de Zeus dans l'écosystème.

**Résilience de connexion** - [PR #3543](https://github.com/ZeusLN/zeus/pull/3543) implémente des notifications de délai d'attente pour les connexions Nostr bloquées. Auparavant, les utilisateurs attendaient indéfiniment lorsque les connexions relais tombaient silencieusement. Maintenant Zeus affiche des messages de délai d'attente clairs après 30 secondes d'inactivité, permettant aux utilisateurs de réessayer ou de changer de relais. [PR #3541](https://github.com/ZeusLN/zeus/pull/3541) ajoute une validation backend pour empêcher l'activation NWC sur des implémentations Lightning incompatibles, détectant les erreurs de configuration avant qu'elles ne causent des plantages à l'exécution.

**Condition de concurrence Cashu** - [PR #3531](https://github.com/ZeusLN/zeus/pull/3531) corrige un bug de concurrence dans la gestion des jetons Cashu où des opérations de frappe simultanées pouvaient corrompre la base de données de jetons. La condition de concurrence se produisait lorsque plusieurs threads mettaient à jour les compteurs de jetons sans verrouillage approprié, résultant occasionnellement en soldes incorrects. Le correctif ajoute une protection mutex autour des sections critiques, garantissant des mises à jour atomiques de l'état des jetons.

### Primal Android (Client)

Primal Android a livré 12 PR fusionnées avec des améliorations significatives de la sécurité du portefeuille et du traitement des médias. L'implémentation de sauvegarde de portefeuille répond à l'une des fonctionnalités les plus demandées, tandis que le support NIP-92 améliore l'expérience visuelle dans toute l'application.

**Système de sauvegarde de portefeuille** - Une série de quatre PR ([#844](https://github.com/PrimalHQ/primal-android-app/pull/844), [#845](https://github.com/PrimalHQ/primal-android-app/pull/845), [#846](https://github.com/PrimalHQ/primal-android-app/pull/846), [#848](https://github.com/PrimalHQ/primal-android-app/pull/848)) implémente une fonctionnalité complète de sauvegarde de phrase de récupération. Les utilisateurs peuvent maintenant exporter leur mnémonique de 12 mots via un flux sécurisé qui empêche les captures d'écran, affiche l'état de sauvegarde dans le tableau de bord du portefeuille et guide les utilisateurs existants à travers la migration. L'implémentation suit les normes BIP-39 et inclut une validation pour empêcher les utilisateurs de perdre des fonds en raison d'un enregistrement incorrect de la phrase.

**Dimensions de média (NIP-92)** - [PR #718](https://github.com/PrimalHQ/primal-android-app/pull/718) implémente le support [NIP-92](/fr/topics/nip-92/) pour des ratios d'aspect d'image et de vidéo corrects. Sans métadonnées de dimensions, les clients doivent télécharger les images pour déterminer leur taille, causant des sauts de mise en page au chargement du contenu. NIP-92 ajoute des tags `dim` (comme `["dim", "1920x1080"]`) aux événements de métadonnées de fichiers, permettant à Primal de réserver l'espace correct avant de télécharger les médias. Cela élimine les reflux gênants dans les galeries d'images et améliore les performances perçues.

**Fiabilité du signataire distant** - [PR #841](https://github.com/PrimalHQ/primal-android-app/pull/841) corrige les problèmes de connexion [NIP-46](/fr/topics/nip-46/) où les préfixes `wss://` manquants causaient des échecs silencieux. La PR valide les URI de relais lors de la configuration de la connexion bunker, ajoutant automatiquement le préfixe de protocole lorsque les utilisateurs collent des domaines nus. [PR #843](https://github.com/PrimalHQ/primal-android-app/pull/843) traite un bug de threading où de mauvaises conditions réseau causaient la publication de réponses comme notes racines, cassant le flux de conversation. Le correctif garantit que les ID d'événement parent persistent à travers les interruptions réseau.

### Protocole Marmot : White Noise (Bibliothèque de discussion de groupe chiffrée)

White Noise, la bibliothèque Rust alimentant les discussions de groupe chiffrées du [Protocole Marmot](/fr/topics/marmot/), a fusionné six PR améliorant l'expérience utilisateur et la sécurité. Les changements rapprochent Marmot de la parité de fonctionnalités avec les applications de messagerie grand public tout en maintenant son architecture axée sur la confidentialité.

**Accusés de réception de lecture** - [PR #433](https://github.com/marmot-protocol/whitenoise-rs/pull/433) et [#436](https://github.com/marmot-protocol/whitenoise-rs/pull/436) implémentent le suivi de lecture de messages pour les conversations de groupe. Le système stocke les positions de lecture par utilisateur par groupe dans un seul appareil, permettant des badges de comptage non lu. L'implémentation utilise des horodatages monotones pour suivre la dernière position de message lu pour chaque conversation. Cette fonctionnalité fondamentale permet des indicateurs d'interface utilisateur montrant les compteurs de messages non lus par conversation.

**Épinglage de conversation** - [PR #442](https://github.com/marmot-protocol/whitenoise-rs/pull/442) ajoute l'épinglage de conversation persistant via un champ `pin_order` dans la table de jonction `accounts_groups` qui relie les comptes aux groupes. Les conversations épinglées maintiennent leur position en haut des listes de discussions indépendamment de l'activité des messages, correspondant aux attentes des utilisateurs de Signal et WhatsApp. L'implémentation utilise l'ordonnancement par entiers pour permettre des épingles illimitées avec un tri déterministe.

**Résolution déterministe de commit (MIP-03)** - [PR #152](https://github.com/marmot-protocol/mdk/pull/152) (ouverte) implémente la proposition d'amélioration Marmot 03, résolvant le problème critique des conditions de concurrence de commit dans les discussions de groupe distribuées. Lorsque plusieurs membres soumettent simultanément des changements d'état de groupe (ajout/suppression de membres, changement de permissions), les clients pouvaient diverger sur l'ordonnancement des commits, fragmentant le groupe en états incompatibles. MIP-03 introduit des instantanés d'époque et une sélection déterministe de gagnant : le commit avec l'horodatage `created_at` le plus ancien gagne, avec l'ID d'événement lexicographique comme bris d'égalité. Cela permet à tous les clients de converger vers le même état via rollback et rejeu, maintenant la cohérence du groupe même pendant les partitions réseau.

**Durcissement de sécurité** - [PR #443](https://github.com/marmot-protocol/whitenoise-rs/pull/443) empêche la copie inutile de secrets cryptographiques en utilisant des références dans `resolve_group_image_path`. Cela réduit la fenêtre pour les attaques mémoire où les secrets pourraient être récupérés à partir d'allocations tas libérées. [PR #438](https://github.com/marmot-protocol/whitenoise-rs/pull/438) active le chiffrement de base de données SQLCipher via des paramètres de trousseau, protégeant l'historique des messages au repos. L'intégration du trousseau permet un stockage sécurisé des clés dans les trousseaux de plateforme plutôt que dans les fichiers de configuration.

### nostrdb-rs (Bibliothèque de base de données) - PR ouverte

**Implémentation de requêtes en streaming** - [PR #58](https://github.com/damus-io/nostrdb-rs/pull/58) (ouverte) propose des requêtes fold en streaming pour permettre des opérations de base de données sans allocation. L'implémentation ajoute des méthodes `fold`, `try_fold`, `count`, `any`, `all` et `find_map` qui traiteraient les résultats de base de données un par un sans matérialiser des ensembles de résultats entiers en vecteurs. Cette approche réduirait la consommation de mémoire et permettrait une terminaison précoce pour les modèles de requête courants.

L'implémentation technique expose les rappels de résultats de requête de bas niveau (`ndb_query_visit`) en tant que visiteurs Rust avec état qui mappent les variantes `ControlFlow` aux actions de visiteur C. Une fois fusionné, le code d'application se lira comme une logique d'itérateur tout en s'exécutant près de la couche de base de données. Par exemple, compter les notes correspondantes diffuserait à travers les résultats plutôt que de les collecter, et `find_map` retournerait le premier résultat utile sans traiter les lignes restantes.

nostrdb alimente Damus et Notedeck, clients iOS/macOS et de bureau respectivement. Les requêtes en streaming permettraient des modèles efficaces comme la pagination, le filtrage conditionnel et les vérifications d'existence. La PR modifie 3 fichiers avec +756 ajouts et -32 suppressions, une refactorisation substantielle de la couche de requête. Les utilisateurs d'applications basées sur nostrdb-rs verraient une utilisation mémoire réduite lors de la navigation dans de grandes chronologies ou de la recherche dans des bases de données d'événements étendues.

### nak (Outil CLI)

nak, l'outil en ligne de commande Nostr de fiatjaf, a fusionné six PR axées sur les améliorations du système de construction et les nouvelles fonctionnalités. [PR #91](https://github.com/fiatjaf/nak/pull/91) implémente une fonctionnalité de miroir Blossom, permettant à nak de servir de miroir pour les serveurs de média Blossom. [Blossom](/fr/topics/blossom/) est un protocole de stockage de média adressable par contenu qui fonctionne aux côtés des événements Nostr.

Les PR restantes traitent la compatibilité du système de construction sur les plateformes Windows, macOS et Linux, permettant le support du système de fichiers FUSE pour monter les événements Nostr comme répertoires locaux.

### Damus (Client iOS) - PR ouvertes

Damus a 11 PR ouvertes explorant des améliorations architecturales significatives. Bien que celles-ci n'aient pas encore fusionné, elles signalent des directions importantes pour le développement de clients Nostr iOS, en particulier autour de la confidentialité, de l'efficacité de synchronisation et de l'optimisation des données mobiles.

**Intégration Tor** - [PR #3535](https://github.com/damus-io/damus/pull/3535) intègre le client Tor Arti directement dans Damus, permettant des connexions relais anonymes sans dépendances externes. Contrairement aux approches Orbot ou Tor Browser, l'intégration d'Arti fournit une intégration transparente avec le sandboxing iOS et les limites d'exécution en arrière-plan. L'implémentation Rust apporte la sûreté mémoire à l'anonymisation réseau, réduisant la surface d'attaque par rapport au Tor en C. Les utilisateurs pourraient basculer le mode Tor par relais ou globalement, le client gérant la gestion des circuits de manière transparente.

**Protocole de synchronisation Negentropy** - [PR #3536](https://github.com/damus-io/damus/pull/3536) implémente Negentropy, un protocole de réconciliation d'ensemble qui améliore radicalement l'efficacité de synchronisation. Au lieu de télécharger tous les événements depuis la dernière connexion, Negentropy échange des empreintes compactes (arbres Merkle) pour identifier exactement quels événements diffèrent entre le client et le relais. Pour les utilisateurs suivant des centaines de pubkeys, cela réduit la bande passante de synchronisation de mégaoctets à kilooctets. L'implémentation s'intègre avec RelayPool et SubscriptionManager, permettant une synchronisation efficace automatique sur tous les relais connectés.

**Mode données réduites** - [PR #3549](https://github.com/damus-io/damus/pull/3549) ajoute des fonctionnalités de conservation de données cellulaires répondant aux retours des utilisateurs sur la consommation de bande passante. Le mode désactive le chargement automatique d'images, la pré-extraction vidéo et réduit les limites d'abonnement. Les utilisateurs sur connexions mesurées peuvent parcourir le contenu texte sans crainte de dépasser les plafonds de données. L'implémentation respecte les paramètres de mode données réduites iOS et fournit des contrôles granulaires pour différents types de médias.

**Optimisations de base de données** - [PR #3548](https://github.com/damus-io/damus/pull/3548) retravaille le stockage d'instantané nostrdb pour des requêtes plus rapides et une utilisation disque réduite. L'optimisation change la façon dont les instantanés de base de données persistent sur disque, améliorant à la fois les performances de lecture et l'amplification d'écriture. Cela répond aux plaintes de décharge de batterie des utilisateurs avec de grandes bases de données d'événements.

---

C'est tout pour cette semaine. Vous construisez quelque chose ? Vous avez des nouvelles à partager ? Vous voulez que nous couvrions votre projet ? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contactez-nous via DM NIP-17</a> ou trouvez-nous sur Nostr.
