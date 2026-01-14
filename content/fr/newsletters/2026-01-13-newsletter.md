---
title: 'Nostr Compass #5'
date: 2026-01-13
publishDate: 2026-01-13
draft: false
type: newsletters
---

Bon retour sur Nostr Compass, votre guide hebdomadaire sur Nostr.

**Cette semaine :** Bitchat fait l'objet d'un audit de sécurité professionnel par Cure53, la même entreprise qui a audité Signal et [NIP-44](/fr/topics/nip-44/), avec plus de 17 PR déjà fusionnées corrigeant des découvertes critiques. [NIP-71](/fr/topics/nip-71/) est fusionnée, apportant des événements vidéo adressables au protocole. Un NIP sur la cryptographie post-quantique ouvre la discussion sur la protection de Nostr contre les attaques quantiques futures. Amethyst v1.05.0 propose des listes de favoris, des notes vocales et une version de bureau anticipée, tandis que Nostur v1.25.3 améliore les DM [NIP-17](/fr/topics/nip-17/) avec des réactions et des réponses. Côté bibliothèques, rust-nostr étend le support de [NIP-62](/fr/topics/nip-62/) aux backends SQLite et LMDB, et NDK corrige un bug de suivi des abonnements.

## Actualités

### Bitchat termine l'audit de sécurité Cure53

Bitchat, la messagerie chiffrée iOS combinant Nostr avec Cashu, a fait l'objet d'un audit de sécurité professionnel par Cure53, l'une des entreprises de sécurité les plus respectées du secteur. Cure53 a précédemment audité Signal, Mullvad VPN, et notamment la spécification de chiffrement [NIP-44](/fr/topics/nip-44/) qui sous-tend la messagerie privée moderne sur Nostr.

L'audit a révélé plus de 12 problèmes de sécurité (BCH-01-002 à BCH-01-013). L'équipe Bitchat a répondu avec plus de 17 pull requests. Les corrections clés incluent :

**Effacement des secrets DH du protocole Noise** - [PR #928](https://github.com/permissionlesstech/bitchat/pull/928) corrige six emplacements où les secrets partagés Diffie-Hellman n'étaient pas effacés après l'accord de clés, restaurant les garanties de confidentialité persistante. Lorsque les secrets persistent en mémoire plus longtemps que nécessaire, un vidage mémoire ou une attaque par démarrage à froid pourrait compromettre les communications passées.

**Vérification des signatures** - Plusieurs PR renforcent les chemins de vérification cryptographique, garantissant que les contrôles d'authenticité des messages ne peuvent pas être contournés par des entrées malformées.

**Sécurité des threads** - [PR #929](https://github.com/permissionlesstech/bitchat/pull/929) ajoute une synchronisation par barrière aux files d'accusés de réception dans NostrTransport, évitant les conditions de concurrence qui pourraient causer une corruption de données ou des plantages sous des volumes de messages élevés.

**Sécurité mémoire** - [PR #920](https://github.com/permissionlesstech/bitchat/pull/920) optimise le dédoublonneur de messages pour de meilleures performances avec un débit de messages élevé tout en évitant l'épuisement de la mémoire.

**Validation des entrées** - [PR #919](https://github.com/permissionlesstech/bitchat/pull/919) renforce l'analyse des chaînes hexadécimales pour éviter les plantages dus aux entrées malformées, un vecteur d'attaque courant pour les dénis de service.

Bitchat gère l'ecash Cashu, rendant l'examen de sécurité professionnel essentiel. L'audit fait suite à l'audit du protocole [Marmot](/fr/topics/marmot/) de l'année dernière et à l'audit NIP-44 qui a vérifié la couche de chiffrement.

## Mises à jour des NIP {#nip-updates}

Changements récents dans le [dépôt NIPs](https://github.com/nostr-protocol/nips) :

**Fusionnées :**

- **[NIP-71](/fr/topics/nip-71/)** - Événements vidéo adressables ([#1669](https://github.com/nostr-protocol/nips/pull/1669)) introduit les kinds 34235 (vidéo horizontale) et 34236 (vidéo verticale) comme événements adressables. Un tag `d` requis fournit des identifiants uniques, permettant de mettre à jour les métadonnées vidéo sans republier l'événement entier. Un tag `origin` optionnel permet de suivre les sources d'importation. Déjà implémenté dans Amethyst et nostrvine.

**PR ouvertes :**

- **Cryptographie post-quantique** - [PR #2185](https://github.com/nostr-protocol/nips/pull/2185) propose d'ajouter des algorithmes cryptographiques résistants aux attaques quantiques à Nostr. La spécification introduit ML-DSA-44 et Falcon-512 pour les signatures numériques, ciblant les « événements de très haute valeur » comme les applications et les autorités plutôt que les utilisateurs individuels. Bien que le chiffrement symétrique de [NIP-44](/fr/topics/nip-44/) (ChaCha20) soit résistant aux attaques quantiques, son échange de clés utilise secp256k1 ECDH qui est vulnérable à l'algorithme de Shor. La proposition inclut ML-KEM pour l'accord de clés afin de combler cette lacune. Il s'agit d'une proposition à un stade précoce ouvrant la discussion sur l'agilité cryptographique pour la sécurité à long terme de Nostr.
- **BOLT12 pour NIP-47** - Après 137 commentaires et une discussion approfondie, la communauté a décidé que les offres BOLT12 méritent leur propre spécification plutôt que d'étendre [NIP-47](/fr/topics/nip-47/). Les offres BOLT12 apportent des améliorations significatives par rapport aux factures BOLT11, notamment la réutilisabilité, une meilleure confidentialité grâce aux chemins masqués et des informations optionnelles sur le payeur. Le nouveau NIP définira des méthodes comme `make_offer`, `pay_offer` et `list_offers` pour les implémentations Nostr Wallet Connect.
- **NIP Audio Track** - [PR #1043](https://github.com/nostr-protocol/nips/pull/1043) propose les kinds 32100 pour les pistes musicales et 32101 pour les épisodes de podcast, donnant au contenu audio le même traitement de première classe que NIP-71 offre pour la vidéo. Actuellement, les plateformes audio comme Wavlake, Zapstr et Stemstr utilisent chacune des formats d'événements propriétaires, fragmentant l'écosystème. Un standard commun permettrait l'interopérabilité afin que les utilisateurs puissent découvrir et lire de l'audio depuis n'importe quel client compatible.
- **NIP-A3 Universal Payment Targets** - [PR #2119](https://github.com/nostr-protocol/nips/pull/2119) propose des événements kind 10133 utilisant les URI `payto:` RFC-8905 pour exposer les options de paiement sur plusieurs réseaux. Plutôt que de créer des kinds d'événements séparés pour Bitcoin, Lightning, Cashu ou les rails de paiement traditionnels, cette abstraction permet aux clients d'analyser des tags standardisés et d'invoquer des gestionnaires de paiement natifs. L'approche est pérenne puisque les nouvelles méthodes de paiement n'ont besoin que d'un schéma d'URI `payto:`.

## Plongée approfondie dans les NIP : NIP-51 et NIP-65

Cette semaine, nous couvrons deux NIP qui stockent les préférences utilisateur : NIP-51 pour organiser le contenu, et NIP-65 pour organiser les connexions relay. Les deux utilisent des événements remplaçables, ce qui signifie que chaque nouvelle publication écrase la version précédente.

### [NIP-51](/fr/topics/nip-51/) : Listes

[NIP-51](https://github.com/nostr-protocol/nips/blob/master/51.md) définit plusieurs types de listes pour organiser les références aux événements, utilisateurs, hashtags et autres contenus. Amethyst v1.05.0 ajoute le support des favoris, ce qui en fait un bon moment pour comprendre comment fonctionnent les listes.

La spécification définit plusieurs kinds de listes, chacun servant un objectif différent. Le kind 10000 est votre liste de mise en sourdine pour masquer les utilisateurs, fils de discussion ou mots. Le kind 10001 épingle les événements à mettre en avant sur votre profil. Le kind 30003 stocke les favoris, ce que Amethyst supporte maintenant. D'autres kinds gèrent les ensembles de suivi (30000), les collections d'articles sélectionnés (30004), les centres d'intérêt hashtag (30015) et les ensembles d'emojis personnalisés (30030).

Les listes référencent le contenu via des tags. Une liste de favoris utilise des tags `e` pour des événements spécifiques et des tags `a` pour du contenu adressable comme les articles :

```json
{
  "id": "ae3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1736784000,
  "kind": 30003,
  "tags": [
    ["d", "saved-articles"],
    ["e", "abc123def456...", "wss://relay.example"],
    ["a", "30023:author-pubkey:article-id", "wss://relay.example"]
  ],
  "content": "<encrypted-private-bookmarks>",
  "sig": "908a15e46fb4d8675bab026fc230a0e3542bfade63da02d542fb78b2a8513fcd0092619a2c8c1221e581946e0191f2af505dfdf8657a414dbca329186f009262"
}
```

Le tag `d` fournit un identifiant unique, vous permettant de maintenir plusieurs ensembles de favoris comme « saved-articles », « read-later » ou « favorites » sous le même kind.

Les listes supportent à la fois les éléments publics et privés. Les éléments publics apparaissent dans le tableau des tags, visibles par quiconque récupère l'événement. Les éléments privés vont dans le champ `content`, chiffrés en utilisant [NIP-44](/fr/topics/nip-44/) pour vous-même. Cette structure duale vous permet de garder des favoris publics tout en attachant des notes privées, ou de maintenir une liste de mise en sourdine sans révéler qui vous avez mis en sourdine. Pour chiffrer pour vous-même, utilisez NIP-44 avec votre propre pubkey comme destinataire.

Les kinds de la série 10000 sont remplaçables, ce qui signifie que les relays ne conservent qu'un seul événement par pubkey. La série 30000 est paramétrable et remplaçable, permettant un événement par combinaison de pubkey et de tag `d`. Dans les deux cas, mettre à jour une liste signifie publier un remplacement complet ; vous ne pouvez pas envoyer de changements incrémentiels. Les clients doivent préserver les tags inconnus lors de la modification des listes pour éviter d'écraser les données ajoutées par d'autres applications.

### [NIP-65](/fr/topics/nip-65/) : Métadonnées de liste de relays {#nip-65-relay-list-metadata}

[NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md) définit des événements kind 10002 qui annoncent quels relays un utilisateur préfère pour la lecture et l'écriture. Cela aide les autres utilisateurs et clients à trouver votre contenu.

```json
{
  "id": "bd2217a96b5835b59f9a6a42d8d8a36f8c9b7d4e5f0a1b2c3d4e5f6a7b8c9d0e1",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1736784000,
  "kind": 10002,
  "tags": [
    ["r", "wss://relay.damus.io", "read"],
    ["r", "wss://nos.lol"],
    ["r", "wss://relay.nostr.band", "write"]
  ],
  "content": "",
  "sig": "f1c2d3e4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2"
}
```

Chaque tag `r` contient une URL de relay et un marqueur optionnel. Un marqueur `write` désigne votre boîte d'envoi : les relays où vous publiez votre contenu. Un marqueur `read` désigne votre boîte de réception : les relays où vous vérifiez les mentions, réponses et tags. L'absence de marqueur indique les deux.

Quand Alice veut trouver les publications de Bob, son client récupère le kind 10002 de Bob, extrait ses relays d'écriture (sa boîte d'envoi) et s'y abonne. Quand Alice répond à Bob, son client publie vers ses relays de lecture (sa boîte de réception) pour qu'il voie la mention. Ce routage conscient des relays est le « modèle outbox », et il distribue les utilisateurs sur de nombreux relays plutôt que de concentrer tout le monde sur quelques serveurs centraux.

NIP-65 gère le routage du contenu public, mais les messages privés utilisent une liste séparée. [NIP-17](/fr/topics/nip-17/) définit le kind 10050 pour les relays de boîte de réception DM, utilisant des tags `relay` au lieu de tags `r`. Lors de l'envoi d'un message privé à quelqu'un, les clients recherchent l'événement kind 10050 du destinataire et y publient le message emballé-cadeau chiffré. Cette séparation garde le routage des DM distinct du routage du contenu public, et permet aux utilisateurs de spécifier différents relays pour les communications privées et publiques.

Le modèle outbox améliore la résistance à la censure puisqu'aucun relay unique n'a besoin de stocker ou de servir le contenu de tout le monde. Les clients maintiennent des connexions aux relays listés dans les événements NIP-65 de leurs utilisateurs suivis, se connectant dynamiquement à de nouveaux relays à mesure qu'ils découvrent de nouveaux comptes. NIP-65 complète les indices de relay trouvés dans d'autres NIP. Quand vous taguez quelqu'un avec `["p", "pubkey", "wss://hint.relay"]`, l'indice dit aux clients où chercher cette référence spécifique. NIP-65 fournit la liste autoritaire contrôlée par l'utilisateur, tandis que les indices offrent des raccourcis intégrés dans les événements individuels.

Pour de meilleurs résultats, gardez votre liste de relays à jour car les entrées obsolètes vous rendent plus difficile à trouver. La spécification recommande deux à quatre relays par catégorie. Lister trop de relays surcharge chaque client qui veut récupérer votre contenu, ralentissant leur expérience et augmentant la charge réseau. Les clients mettent en cache les événements NIP-65 et les rafraîchissent périodiquement pour rester à jour lorsque les utilisateurs mettent à jour leurs préférences.

## Versions

**Amethyst v1.05.0** - Le client Android populaire [publie une mise à jour majeure](https://github.com/vitorpamplona/amethyst/releases) avec plusieurs fonctionnalités phares. Les listes de favoris kind 30003 de [NIP-51](/fr/topics/nip-51/) permettent aux utilisateurs de sauvegarder des publications pour référence ultérieure, se synchronisant entre les clients compatibles. Les notes vocales fonctionnent maintenant dans les DM et les publications régulières avec visualisation de forme d'onde, sélection du serveur média et indicateurs de progression de téléchargement. Les scores de [Web of Trust](/fr/topics/web-of-trust/) sont maintenant visibles dans l'interface, aidant les utilisateurs à comprendre comment l'algorithme évalue les comptes par rapport à leur graphe social. La migration de base de données [Quartz](/fr/topics/quartz/) améliore les performances des requêtes dans le cadre du travail Kotlin Multiplatform financé par OpenSats. Une version de bureau anticipée amène Amethyst sur Windows, macOS et Linux via Compose Multiplatform, partageant le même code que l'application Android. De nouveaux flux d'intégration facilitent l'expérience pour les nouveaux utilisateurs Nostr.

**Nostur v1.25.3** - Le client iOS et macOS [se concentre sur la messagerie privée](https://github.com/nostur-com/nostur-ios-public/releases) avec des améliorations [NIP-17](/fr/topics/nip-17/). Les conversations DM supportent maintenant les réactions et les réponses, apportant l'interactivité des publications publiques aux messages chiffrés. La vue de conversation a été retravaillée avec un meilleur threading pour que les échanges multi-messages soient plus faciles à suivre, et les horodatages affichent « il y a » dans la liste des DM pour un balayage rapide. Les utilisateurs de bureau obtiennent des dispositions multi-colonnes pour visualiser plusieurs flux ou conversations côte à côte. Le support du signataire distant [NIP-46](/fr/topics/nip-46/) permet aux utilisateurs de garder leurs clés privées dans des applications de signature dédiées comme Amber ou nsec.app. Des corrections supplémentaires restaurent la fonctionnalité DM sur iOS 15 et iOS 16, résolvent les retards de notification et ajoutent la possibilité de configurer quels relays reçoivent les DM publiés.

## Changements notables de code et documentation

*Ce sont des pull requests ouvertes et des travaux à un stade précoce, parfaits pour obtenir des retours avant leur fusion. Si quelque chose attire votre attention, pensez à faire une revue ou à commenter !*

### Citrine (Relay Android)

[PR #89](https://github.com/greenart7c3/Citrine/pull/89) corrige une vulnérabilité d'injection SQL dans l'application de relay personnel Android. Le problème permettait à des données d'événements malformées d'exécuter des requêtes de base de données arbitraires, un défaut sérieux pour toute application qui stocke et traite des entrées non fiables. La correction assainit correctement toutes les opérations de base de données en utilisant des requêtes paramétrées. Aucune version n'a encore été taguée, donc les utilisateurs devront attendre la prochaine version ou compiler depuis les sources. [PR #90](https://github.com/greenart7c3/Citrine/pull/90) optimise les performances de requête ContentProvider avec un filtrage et une pagination au niveau de la base de données, réduisant la latence lorsque des applications externes comme Amethyst accèdent à la base de données d'événements de Citrine via la couche de communication inter-processus d'Android.

### rust-nostr (Bibliothèque) {#rust-nostr-library}

Le support de [NIP-62](/fr/topics/nip-62/) (requêtes de disparition) s'étend aux backends de base de données de rust-nostr. [PR #1180](https://github.com/rust-nostr/nostr/pull/1180), fusionnée il y a deux semaines, a ajouté le support NIP-62 à SQLite, gérant les requêtes de disparition `ALL_RELAYS` puisque la couche base de données ne connaît pas les URL de relay spécifiques. [PR #1210](https://github.com/rust-nostr/nostr/pull/1210) étend ceci au backend LMDB, garantissant que les requêtes de disparition sont persistées sur le disque et survivent aux redémarrages de relay. Une implémentation IndexedDB pour les environnements navigateur est également en cours. Ensemble, ces changements donnent aux développeurs un support NIP-62 cohérent à travers SQLite, LMDB et bientôt le stockage navigateur.

### NDK (Nostr Development Kit)

[PR #375](https://github.com/nostr-dev-kit/ndk/pull/375) corrige un bug dans le système de suivi seenEvents. Le problème faisait que certains patterns d'abonnement marquaient incorrectement les événements comme déjà vus, conduisant à du contenu manqué lorsque les utilisateurs ouvraient de nouveaux abonnements ou se reconnectaient aux relays. La correction garantit que les événements sont suivis avec précision à travers les cycles de vie des abonnements, ce qui est particulièrement important pour les applications qui s'abonnent et se désabonnent dynamiquement en fonction de la navigation de l'utilisateur. NDK est passé à la version beta.70 avec cette correction incluse.

### Damus (iOS)

[PR #3515](https://github.com/damus-io/damus/pull/3515) corrige un plantage au démarrage affectant les utilisateurs iOS 17. Le problème provenait d'un dépassement arithmétique dans `NdbUseLock`, une classe de repli utilisée car les Swift Mutexes ne sont pas disponibles sur iOS 17. La correction remplace l'approche de synchronisation précédente par `NSLock`, qui est disponible sur iOS 17 et gère correctement les conditions de concurrence restantes. Les utilisateurs iOS 18+ n'étaient pas affectés puisqu'ils ont accès à l'implémentation native Swift Mutex.

Séparément, un lot d'améliorations pour les articles longs a été intégré via [PR #3509](https://github.com/damus-io/damus/pull/3509). Des barres de progression de lecture suivent votre position dans les articles, les temps de lecture estimés apparaissent sur les aperçus, et le mode sépia avec des paramètres de hauteur de ligne ajustables offrent une lecture plus confortable. Le mode concentration masque automatiquement l'interface de navigation lors du défilement vers le bas et la restaure au toucher, réduisant l'encombrement visuel pour une lecture sans distraction. Plusieurs corrections traitent l'affichage des images dans le contenu markdown et garantissent que les articles s'ouvrent en haut plutôt qu'à mi-chemin.

### Zap.stream (Streaming en direct)

L'intégration du chat YouTube et Kick relie les messages des plateformes de streaming externes à Nostr. Les streamers qui diffusent sur YouTube, Kick et Zap.stream peuvent maintenant voir tous les messages de chat dans une vue unifiée, avec les messages de chaque plateforme apparaissant aux côtés des commentaires Nostr natifs. Cela supprime un point de friction majeur pour les créateurs qui veulent utiliser Nostr pour le streaming mais ne peuvent pas abandonner leurs audiences sur les plateformes établies. L'intégration affiche de quelle plateforme chaque message provient et gère le flux d'authentification pour connecter les comptes externes.

### Chachi (Groupes NIP-29)

Le client de chat de groupe [NIP-29](/fr/topics/nip-29/) a publié six PR fusionnées cette semaine. Une mise à jour de sécurité traite [CVE-2026-22029](https://github.com/purrgrammer/chachi/pull/89), une vulnérabilité XSS dans react-router qui pourrait permettre des attaques de redirection ouverte ; la correction met à jour vers react-router-dom 6.30.0. [PR #92](https://github.com/purrgrammer/chachi/pull/92) ajoute le chargement paginé des messages pour les chats de groupe, de sorte que les longues conversations se chargent de manière incrémentielle plutôt que tout d'un coup. [PR #91](https://github.com/purrgrammer/chachi/pull/91) corrige plusieurs bugs NIP-29 incluant une condition de concurrence qui causait des noms de groupe vides au chargement initial et des listes de participants indéfinies qui plantaient les vues de membres. La couverture de traduction s'étend maintenant aux 31 langues supportées avec 1060 clés chacune.

### 0xchat (Messagerie)

Le client de messagerie style Telegram a amélioré la conformité [NIP-55](/fr/topics/nip-55/) en sauvegardant correctement les noms de paquets des signataires lors de l'utilisation d'applications de signature externes, corrigeant les problèmes où l'application perdait la trace du signataire à utiliser après les redémarrages. La gestion des réponses NIP-17 inclut maintenant correctement le tag `e` pour le threading, garantissant que les réponses apparaissent dans le bon contexte de conversation entre les clients. Des optimisations de performance traitent le lag de défilement dans les listes de messages, un point de douleur courant lors du chargement de longs historiques de chat. La sauvegarde automatique des brouillons empêche la perte de messages si vous naviguez ailleurs en cours de composition, et les options de stockage de fichiers incluent maintenant les endpoints FileDropServer et BlossomServer par défaut.

### Primal (iOS)

Le support du signataire distant [NIP-46](/fr/topics/nip-46/) arrive sur iOS via [PR #184](https://github.com/PrimalHQ/primal-ios-app/pull/184), complétant le déploiement multiplateforme commencé avec Android il y a plusieurs semaines. Les utilisateurs peuvent maintenant garder leurs clés privées dans des services bunker dédiés comme nsec.app ou des instances nsecBunker auto-hébergées, se connectant via les relays Nostr pour signer les événements sans exposer les clés à l'application cliente. Cette séparation améliore la posture de sécurité pour les utilisateurs qui veulent utiliser les fonctionnalités de Primal tout en maintenant des pratiques de gestion de clés plus strictes. L'implémentation inclut le scan de code QR pour les URI de connexion bunker et gère le flux requête/réponse NIP-46 via des messages relay chiffrés.

---

C'est tout pour cette semaine. Vous construisez quelque chose ? Vous avez des nouvelles à partager ? Vous voulez que nous couvrions votre projet ? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contactez-nous via DM NIP-17</a> ou trouvez-nous sur Nostr.
