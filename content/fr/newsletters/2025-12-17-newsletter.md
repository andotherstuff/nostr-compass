---
title: 'Nostr Compass #1'
date: 2025-12-17
publishDate: 2025-12-15
draft: false
type: newsletters
---

Bienvenue dans Nostr Compass, une newsletter hebdomadaire dédiée à l'écosystème du protocole Nostr. Notre mission est de tenir les développeurs, opérateurs de relais et constructeurs informés des développements importants à travers le réseau. Nous documentons l'évolution du protocole avec précision technique, neutralité et profondeur, couvrant tout, des propositions NIP aux sorties de clients en passant par les meilleures pratiques d'implémentation.

Nostr Compass s'inspire de [Bitcoin Optech](https://bitcoinops.org/), dont les années de travail dévoué à l'avancement des connaissances techniques de Bitcoin ont établi la norme pour les newsletters axées sur les protocoles. Nous sommes reconnaissants pour leur exemple et espérons apporter la même rigueur à l'écosystème Nostr.

Ce numéro inaugural établit notre format hebdomadaire. Chaque mercredi, nous vous apporterons des mises à jour NIP, des notes de version, des points forts du développement et des conseils techniques. Que vous construisiez un client, gériez un relais ou contribuiez au protocole, Nostr Compass vise à être votre source fiable pour ce qui se passe dans l'écosystème.

## Qu'est-ce que Nostr ?

*Comme c'est notre premier numéro, nous commençons par une introduction au fonctionnement de Nostr. Les lecteurs réguliers peuvent [passer directement aux actualités](#actualités).*

Nostr (Notes and Other Stuff Transmitted by Relays) est un protocole décentralisé pour les réseaux sociaux et la messagerie. Contrairement aux plateformes traditionnelles, Nostr n'a pas de serveur central, pas d'entreprise qui le contrôle et pas de point unique de défaillance. Les utilisateurs possèdent leur identité grâce à des paires de clés cryptographiques, et le contenu circule via des serveurs relais indépendants que n'importe qui peut exploiter.

**Comment ça fonctionne :** Les utilisateurs génèrent une paire de clés (une clé privée appelée nsec et une clé publique appelée npub). La clé privée signe les messages appelés « événements », et la clé publique sert d'identité. Les événements sont envoyés aux relais, qui les stockent et les transmettent aux autres utilisateurs. Comme vous contrôlez vos clés, vous pouvez passer d'un client ou d'un relais à l'autre sans perdre votre identité ou vos abonnés.

**Pourquoi c'est important :** Nostr offre une résistance à la censure grâce à la diversité des relais (si un relais vous bannit, d'autres peuvent toujours servir votre contenu), la portabilité (votre identité fonctionne sur n'importe quelle application Nostr) et l'interopérabilité (tous les clients Nostr parlent le même protocole). Il n'y a pas d'algorithme décidant ce que vous voyez, pas de publicités et pas de collecte de données.

**L'écosystème aujourd'hui :** Nostr prend en charge le microblogging (comme Twitter/X), le contenu long format (comme Medium), les messages directs, les places de marché, le streaming en direct, et plus encore. Les clients incluent Damus (iOS), Amethyst (Android), Primal, Coracle et des dizaines d'autres. L'intégration du Lightning Network permet des paiements instantanés via les « zaps ». Le protocole continue d'évoluer grâce aux NIPs (Nostr Implementation Possibilities), des spécifications pilotées par la communauté qui étendent les fonctionnalités.

## Actualités {#news}

**NIP-BE fusionné : Support Bluetooth Low Energy** - Une nouvelle capacité significative [a été intégrée au protocole](https://github.com/nostr-protocol/nips/pull/1979). [NIP-BE](/fr/topics/nip-be/) spécifie comment les applications Nostr peuvent communiquer et se synchroniser via Bluetooth Low Energy. Cela permet aux applications capables de fonctionner hors ligne de synchroniser les données entre appareils à proximité sans connectivité Internet. La spécification adapte les modèles de relais WebSocket aux contraintes du BLE, utilisant la compression DEFLATE et la messagerie fragmentée pour gérer les petites tailles MTU du BLE (20-256 octets). Les appareils négocient les rôles en fonction de la comparaison UUID, l'UUID le plus élevé devenant le serveur GATT.

**MIP-05 : Notifications push préservant la vie privée** - Le [Protocole Marmot](/fr/topics/marmot/) a publié [MIP-05](/fr/topics/mip-05/) ([spécification](https://github.com/marmot-protocol/mips/blob/main/mip-05.md)), une spécification pour les notifications push qui maintiennent la confidentialité. Les systèmes push traditionnels exigent que les serveurs connaissent les jetons d'appareil et les identités des utilisateurs ; MIP-05 résout ce problème en chiffrant les jetons d'appareil avec ECDH+HKDF et ChaCha20-Poly1305, utilisant des clés éphémères pour empêcher la corrélation. Un protocole de propagation à trois événements (kinds 447-449) synchronise les jetons chiffrés entre les membres du groupe, et les notifications utilisent l'emballage cadeau [NIP-59](/fr/topics/nip-59/) avec des jetons leurres pour masquer la taille des groupes. Cela permet à WhiteNoise et autres clients Marmot de délivrer des notifications en temps opportun sans compromettre la vie privée des utilisateurs.

**Blossom BUD-10 : Nouveau schéma URI** - Le protocole média [Blossom](/fr/topics/blossom/) obtient un schéma URI personnalisé via [BUD-10](/fr/topics/bud-10/) ([spécification](https://github.com/hzrd149/blossom/blob/master/buds/10.md)). Le nouveau format `blossom:<sha256>.ext` intègre le hash du fichier, l'extension, la taille, plusieurs indications de serveur et les clés publiques des auteurs pour la découverte de serveur [BUD-03](/fr/topics/bud-03/). Cela rend les liens blob plus résilients que les URL HTTP statiques en permettant le basculement automatique entre serveurs.

**Mises à jour de la place de marché Shopstr** - La place de marché native Nostr a [implémenté Nostr Wallet Connect](https://github.com/shopstr-eng/shopstr/pull/202) ([NIP-47](/fr/topics/nip-47/)) pour les paiements, [ajouté l'expiration des annonces](https://github.com/shopstr-eng/shopstr/pull/203) utilisant [NIP-40](/fr/topics/nip-40/), et introduit les [codes de réduction](https://github.com/shopstr-eng/shopstr/pull/210) pour les vendeurs.

## Mises à jour NIP {#nip-updates}

Changements récents dans le [dépôt NIPs](https://github.com/nostr-protocol/nips) :

**Nouveaux NIPs :**
- **[NIP-BE](/fr/topics/nip-be/)** - Messagerie Bluetooth Low Energy et synchronisation d'appareils ([#1979](https://github.com/nostr-protocol/nips/pull/1979))
- **[NIP-63](/fr/topics/nip-63/)** - Standard Paywall/Contenu Premium pour la gestion du contenu à accès restreint dans le protocole ([#2156](https://github.com/nostr-protocol/nips/pull/2156))

**Changements significatifs :**
- **[NIP-24](/fr/topics/nip-24/)** - Ajout d'un tableau optionnel `languages` aux métadonnées utilisateur Kind 0, permettant aux utilisateurs de spécifier plusieurs langues préférées en utilisant les tags IETF BCP 47 pour une meilleure découverte de contenu et correspondance de relais ([#2159](https://github.com/nostr-protocol/nips/pull/2159))
- **[NIP-69](/fr/topics/nip-69/)** - Ajout du support d'expiration des ordres pour le trading P2P avec les tags `expires_at` et `expiration` ([#2118](https://github.com/nostr-protocol/nips/pull/2118))
- **[NIP-59](/fr/topics/nip-59/)** - Les événements Gift wrap peuvent maintenant être supprimés via les requêtes NIP-09/NIP-62 ([#2131](https://github.com/nostr-protocol/nips/pull/2131))
- **[NIP-51](/fr/topics/nip-51/)** - Suppression des tags hashtag et URL des signets génériques ; les hashtags utilisent maintenant le kind 30015 ([#2133](https://github.com/nostr-protocol/nips/pull/2133))
- **[NIP-18](/fr/topics/nip-18/)** - Amélioration des reposts génériques pour les événements remplaçables avec support du tag `a` ([#2132](https://github.com/nostr-protocol/nips/pull/2132))
- **[NIP-17](/fr/topics/nip-17/)** - Formulation affinée et ajout du support de réaction kind 7 aux DMs ([#2098](https://github.com/nostr-protocol/nips/pull/2098))
- **[NIP-11](/fr/topics/nip-11/)** - Ajout du champ `self` pour l'identification de la clé publique du relais ([#1764](https://github.com/nostr-protocol/nips/pull/1764))

## Analyse approfondie NIP : NIP-01 et NIP-19 {#nip-deep-dive-nip-01-and-nip-19}

Pour ce numéro inaugural, nous couvrons deux NIPs fondamentaux que chaque développeur Nostr devrait comprendre. Consultez nos pages thématiques pour [NIP-01](/fr/topics/nip-01/) et [NIP-19](/fr/topics/nip-19/).

### NIP-01 : Protocole de base

[NIP-01](/fr/topics/nip-01/) définit le protocole de base. Tout dans Nostr se construit sur cette spécification.

**Les événements** sont le seul type d'objet. Chaque événement contient :
- `id` : Hash SHA256 de l'événement sérialisé (l'identifiant unique de l'événement)
- `pubkey` : La clé publique du créateur (hex 32 octets, secp256k1)
- `created_at` : Horodatage Unix
- `kind` : Entier catégorisant le type d'événement
- `tags` : Tableau de tableaux pour les métadonnées
- `content` : La charge utile (l'interprétation dépend du kind)
- `sig` : Signature Schnorr prouvant que la clé publique a créé cet événement

**Les kinds** déterminent comment les relais stockent les événements :
- Événements réguliers (1, 2, 4-44, 1000-9999) : Stockés normalement, toutes les versions conservées
- Événements remplaçables (0, 3, 10000-19999) : Seul le dernier par clé publique est conservé
- Événements éphémères (20000-29999) : Non stockés, juste transmis aux abonnés
- Événements adressables (30000-39999) : Dernier par combinaison clé publique + kind + tag `d`

Le Kind 0 représente les métadonnées utilisateur (profil), le kind 1 est une note textuelle (le post de base), le kind 3 est la liste d'abonnements.

**Kind 1 : Notes textuelles** sont le cœur du Nostr social. Un événement kind 1 est un post court, similaire à un tweet. Le champ `content` contient le texte du message (texte brut, bien que les clients rendent souvent le markdown). Les tags permettent les réponses, mentions et références :

```json
{
  "id": "<32-byte-hex>",
  "pubkey": "<32-byte-hex>",
  "created_at": 1734480000,
  "kind": 1,
  "content": "Bonjour Nostr ! Découvrez le travail de @jb55 sur Damus.",
  "tags": [
    ["e", "<replied-to-event-id>", "wss://relay.example.com", "reply"],
    ["p", "<jb55-pubkey>"]
  ],
  "sig": "<64-byte-hex>"
}
```

Le tag `e` avec le marqueur "reply" indique qu'il s'agit d'une réponse (voir [NIP-10](/fr/topics/nip-10/) pour les conventions de threading). Le tag `p` mentionne un utilisateur, permettant aux clients de le notifier et d'afficher son nom au lieu de la clé publique brute. Les clients récupèrent l'événement kind 0 de l'utilisateur mentionné pour obtenir son nom d'affichage et son image.

Pour construire une timeline, un client s'abonne aux événements kind 1 des clés publiques suivies : `["REQ", "feed", {"kinds": [1], "authors": ["<pubkey1>", "<pubkey2>", ...], "limit": 50}]`. Le relais renvoie les notes correspondantes, et le client les affiche chronologiquement.

**Les événements adressables** (30000-39999) fonctionnent comme les événements remplaçables mais utilisent un tag `d` comme identifiant supplémentaire. Le relais ne conserve que la dernière version de chaque combinaison clé publique + kind + tag d. Cela permet des articles modifiables, des fiches produits, ou tout cas où vous avez besoin de plusieurs éléments remplaçables par utilisateur.

**Les tags** sont des tableaux où le premier élément est le nom du tag. Les tags standards à une seule lettre (`e`, `p`, `a`, `d`, `t`) sont indexés par les relais pour une interrogation efficace. Par exemple, `["e", "<event-id>"]` référence un autre événement, `["p", "<pubkey>"]` référence un utilisateur.

**La communication Client-Relais** utilise des connexions WebSocket avec des tableaux JSON comme messages. Le premier élément identifie le type de message.

Du client au relais :
- `["EVENT", <event>]` - Publier un événement sur le relais
- `["REQ", <sub-id>, <filter>, ...]` - S'abonner aux événements correspondant au(x) filtre(s)
- `["CLOSE", <sub-id>]` - Terminer un abonnement

Du relais au client :
- `["EVENT", <sub-id>, <event>]` - Livre un événement correspondant à votre abonnement
- `["EOSE", <sub-id>]` - « Fin des événements stockés » - le relais a envoyé toutes les correspondances historiques et n'enverra maintenant que les nouveaux événements à leur arrivée
- `["OK", <event-id>, <true|false>, <message>]` - Accuse réception de l'acceptation ou du rejet d'un événement (et pourquoi)
- `["NOTICE", <message>]` - Message lisible par l'humain du relais

Le flux d'abonnement : le client envoie `REQ` avec un ID d'abonnement et un filtre, le relais répond avec des messages `EVENT` correspondants, puis envoie `EOSE` pour signaler qu'il a rattrapé l'historique. Après `EOSE`, tout nouveau message `EVENT` est en temps réel. Le client envoie `CLOSE` quand il a terminé.

**Les filtres** spécifient quels événements récupérer. Un objet filtre peut inclure : `ids` (IDs d'événements), `authors` (clés publiques), `kinds` (types d'événements), `#e`/`#p`/`#t` (valeurs de tags), `since`/`until` (horodatages), et `limit` (résultats max). Toutes les conditions dans un filtre utilisent la logique AND. Vous pouvez inclure plusieurs filtres dans un `REQ`, et ils se combinent avec la logique OR - utile pour récupérer différents types d'événements en un seul abonnement.

### NIP-19 : Identifiants encodés en Bech32

[NIP-19](/fr/topics/nip-19/) définit les formats conviviaux que vous voyez partout dans Nostr : npub, nsec, note, et plus encore. Ceux-ci ne sont pas utilisés dans le protocole lui-même (qui utilise l'hex), mais ils sont essentiels pour le partage et l'affichage.

**Pourquoi bech32 ?** Les clés hex brutes sont sujettes aux erreurs de copie et difficiles à distinguer visuellement. L'encodage Bech32 ajoute un préfixe lisible par l'humain et une somme de contrôle. Vous pouvez immédiatement distinguer un `npub` (clé publique) d'un `nsec` (clé privée) ou `note` (ID d'événement).

**Formats de base** encodent des valeurs brutes de 32 octets :
- `npub` - Clé publique (votre identité, peut être partagée)
- `nsec` - Clé privée (gardez-la secrète, utilisée pour signer)
- `note` - ID d'événement (référence un événement spécifique)

Exemple : La clé publique hex `3bf0c63fcb93463407af97a5e5ee64fa883d107ef9e558472c4eb9aaaefa459d` devient `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`.

**Identifiants partageables** incluent des métadonnées utilisant l'encodage TLV (Type-Length-Value) :
- `nprofile` - Profil avec indications de relais (aide les clients à trouver l'utilisateur)
- `nevent` - Événement avec indications de relais, clé publique de l'auteur et kind
- `naddr` - Référence d'événement adressable (clé publique + kind + tag d + relais)

Ceux-ci résolvent un problème clé : si quelqu'un partage un ID de note, comment savez-vous quel relais l'a ? Un `nevent` regroupe l'ID de l'événement avec les relais suggérés, rendant le partage plus fiable.

**Important :** N'utilisez jamais les formats bech32 dans le protocole lui-même. Les événements, messages de relais et réponses NIP-05 doivent utiliser l'hex. Bech32 est purement pour les interfaces humaines : affichage, copier/coller, codes QR et URLs.

## Sorties {#releases}

**Amber v4.0.4** - L'application de signature Android corrige une NullPointerException, améliore les performances sur l'écran d'activité et ajoute des traductions pour certains types d'événements. La version précédente v4.0.3 avait ajouté une interface de chiffrement/déchiffrement remaniée, l'export/import de comptes, la gestion de relais par compte, le support ping bunker et les rapports de crash. [Version](https://github.com/greenart7c3/Amber/releases/tag/v4.0.4)

**Coracle 0.6.28** - Version de correction de bugs pour le client web. Correction des flux de topics, de la gestion des images quand imgproxy est désactivé, et de la création de liens pour les sources de surlignage non-lien. [Version](https://github.com/coracle-social/coracle/releases/tag/0.6.28)

**Flotilla v1.6.2** - Le client de communautés de style Discord corrige le défilement des modales et les problèmes de style. Les versions précédentes de ce cycle avaient ajouté des badges et sons optionnels pour les notifications, un rendu de liens amélioré, le scan de codes QR pour les liens d'invitation et une configuration de portefeuille simplifiée. [Version](https://github.com/coracle-social/flotilla/releases/tag/1.6.2)

**nak v0.17.2** - L'outil Nostr en ligne de commande a ajouté une nouvelle commande `nip` pour la consultation rapide des références NIP, plus des corrections pour la gestion des dépôts git et le traitement des événements stdin. [Version](https://github.com/fiatjaf/nak/releases/tag/v0.17.2)

**White Noise v0.2.1** - Version majeure pour l'application de messagerie chiffrée basée sur MLS ajoutant le partage d'images via Blossom, la synchronisation en arrière-plan, les notifications push, la localisation en 8 langues et la gestion des membres de groupe. [Version](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.2.1%2B14)

**Amethyst v1.04.2** - Version fonctionnelle introduisant les listes/packs de suivi, de nouveaux filtres de timeline, une galerie d'images et la compression vidéo H.265 (fichiers 50% plus petits). Migration Kotlin Multiplatform terminée. [Version](https://github.com/vitorpamplona/amethyst/releases/tag/v1.04.2)

**Mostro v0.15.5** - Mise à jour de la plateforme de trading P2P avec support d'expiration des ordres NIP-69 et réponses améliorées de l'historique des trades. [Version](https://github.com/MostroP2P/mostro/releases/tag/v0.15.5)

**Nosflare v8.9.26** - Relais Nostr serverless construit sur l'infrastructure Cloudflare. Cette version apporte un correctif critique adressant un bug qui pouvait causer des échecs de websocket, assurant des connexions plus stables pour les utilisateurs et applications qui dépendent du relais. [Version](https://github.com/Spl0itable/nosflare/releases/tag/v8.9.26)

**Noscall v0.4.1** - Application d'appels audio et vidéo sécurisés basée sur Nostr. Cette version améliore l'interface popup sur la page Me et corrige plusieurs problèmes connus, résultant en une meilleure stabilité et fiabilité des appels. [Version](https://github.com/sanah9/noscall/releases/tag/v0.4.1-release)

**Gitplaza v0.25.0** - Client Nostr de bureau axé sur l'activité liée à Git. Cette version introduit un filtre de kind avancé pour le flux inbox, inclut les zaps réguliers dans les filtres et simplifie le formatage du texte des onglets. Les améliorations de performance optimisent le chargement de l'arbre des commentaires, réduisent les requêtes de base de données inutiles et utilisent des branches de commentaires en cache pour un affichage plus rapide. [Version](https://codeberg.org/dluvian/gitplaza/releases/tag/v0.25.0)

## Changements notables de code et documentation {#notable-code-and-documentation-changes}

### Damus (iOS) {#damus}

Focus sur la stabilité avec des corrections de crash et d'interface : [correction du saut de curseur](https://github.com/damus-io/damus/pull/3377) pour la vue de composition, [refonte de l'interface NostrDB](https://github.com/damus-io/damus/pull/3366) utilisant les types Swift `~Copyable` pour la sécurité des transactions, [stabilité de l'interface de thread](https://github.com/damus-io/damus/pull/3341) corrigeant la réinstanciation de la barre d'actions, [gel de la liste de mutes](https://github.com/damus-io/damus/pull/3346) dû aux cycles AttributeGraph, et [crash de profil](https://github.com/damus-io/damus/pull/3334) du nettoyage de transaction inter-thread. Ajout également de [AGENTS.md](https://github.com/damus-io/damus/pull/3293) avec des directives pour les agents de codage IA.

### Notedeck (Desktop/Mobile) {#notedeck}

[Stockage sécurisé des clés](https://github.com/damus-io/notedeck/pull/1191) déplace nsec vers le magasin sécurisé du système d'exploitation avec migration automatique. [Filtrage des notes futures](https://github.com/damus-io/notedeck/pull/1201) cache les événements datés de plus de 24 heures dans le futur (anti-spam). [Copie de nevent](https://github.com/damus-io/notedeck/pull/1183) inclut maintenant les indications de relais. Aussi : [ajout rapide de colonne de profil](https://github.com/damus-io/notedeck/pull/1212), [navigation au clavier](https://github.com/damus-io/notedeck/pull/1208), [optimisation du chargement média](https://github.com/damus-io/notedeck/pull/1210).

### Amethyst (Android) {#amethyst}

[[NIP-46](/fr/topics/nip-46/) signature distante](https://github.com/vitorpamplona/amethyst/pull/1555) support pour Nostr Connect. [Organisation des signets](https://github.com/vitorpamplona/amethyst/pull/1586) avec gestion des listes publiques/privées. [Correction de compatibilité strfry](https://github.com/vitorpamplona/amethyst/pull/1596) pour les cas limites d'analyse des infos de relais.

### Primal (Android) {#primal}

[Deep links Nostr Connect](https://github.com/PrimalHQ/primal-android-app/pull/788) pour les URLs `nostrconnect://`. [Connexion distante](https://github.com/PrimalHQ/primal-android-app/pull/787) via scan QR pour les connexions bunker. [Correction de condition de course de connexion](https://github.com/PrimalHQ/primal-android-app/pull/783).

### White Noise (Messagerie chiffrée) {#white-noise}

[Correction de rétention des données d'application](https://github.com/marmot-protocol/whitenoise/pull/890) désactive la sauvegarde automatique Android pour la confidentialité. [Comportement de défilement du chat](https://github.com/marmot-protocol/whitenoise/pull/861) préserve la position lors de la lecture de l'historique.

### Zeus (Portefeuille Lightning) {#zeus}

[[NIP-47](/fr/topics/nip-47/) paiements parallèles](https://github.com/ZeusLN/zeus/pull/3407) pour un débit de zaps en lot amélioré.

## Bonnes pratiques pour développeurs

**Validez les événements Auth de manière défensive** - go-nostr a corrigé un [panic dans la validation NIP-42](https://github.com/nbd-wtf/go-nostr/pull/182) quand le tag relay était manquant. Vérifiez toujours les tags requis avant d'y accéder, même dans les flux d'authentification où vous attendez des événements bien formés.

**Limitez le débit selon l'état d'authentification** - khatru a ajouté [la limitation de débit basée sur NIP-42](https://github.com/fiatjaf/khatru/pull/57), permettant aux relais d'appliquer différentes limites pour les connexions authentifiées vs anonymes. Considérez des limites par paliers basées sur le statut d'authentification plutôt que des restrictions générales.

**Utilisez la pagination par curseur pour les listes** - Blossom a [remplacé la pagination basée sur la date](https://github.com/hzrd149/blossom/pull/65) par la pagination par curseur sur l'endpoint `/list`. La pagination basée sur la date échoue quand les éléments partagent des horodatages ; les curseurs fournissent une itération fiable.

**Validation de schéma pour les types d'événements** - Le projet [nostrability/schemata](https://github.com/nostrability/schemata) fournit des schémas JSON pour valider les événements conformes aux NIP. Considérez l'intégration de la validation de schéma en développement pour attraper les événements malformés avant qu'ils n'atteignent les relais.

---

C'est tout pour cette semaine. Vous construisez quelque chose ? Vous avez des nouvelles à partager ? Vous voulez que nous couvrions votre projet ? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contactez-nous via DM NIP-17</a> ou trouvez-nous sur Nostr.

