---
title: 'Nostr Compass #2'
date: 2025-12-24
publishDate: 2025-12-24
draft: false
type: newsletters
---

Bon retour sur Nostr Compass, votre guide hebdomadaire de l'écosystème du protocole Nostr.

**Cette semaine :** Trois implémentations de signers [NIP-55](/fr/topics/nip-55/) reçoivent des mises à jour : Amber ajoute la mise en cache des performances, Aegis gagne le support des URI `nostrsigner:`, et Primal Android les rejoint en tant que signer local complet. Shopstr introduit les « Zapsnags » pour les ventes flash via zaps. Mostro ajoute un fonds de développement. Quatre mises à jour NIP sont déployées, incluant les Messages Publics (kind 24) et des améliorations de confidentialité des groupes. Les requêtes de cache NDK accélèrent de 162x, Applesauce ajoute les réactions et le support de portefeuille NIP-60, et Tenex introduit l'architecture RAL pour la délégation d'agents IA. Dans notre analyse approfondie, nous expliquons [NIP-02](/fr/topics/nip-02/) (listes d'abonnements) et [NIP-10](/fr/topics/nip-10/) (threading des réponses), des spécifications fondamentales pour construire des timelines sociales et des conversations.

## Actualités {#news}

**Primal Android devient un signer NIP-55** - S'appuyant sur le [support Nostr Connect de la semaine dernière](/fr/newsletters/2025-12-17-newsletter/#primal-android), Primal a implémenté des capacités complètes de signature locale à travers huit pull requests fusionnées. L'implémentation inclut un `LocalSignerContentProvider` complet qui expose les opérations de signature aux autres applications Android via l'interface content provider d'Android, suivant la spécification [NIP-55](/fr/topics/nip-55/). L'architecture sépare proprement les responsabilités : `SignerActivity` gère les flux d'approbation côté utilisateur, `LocalSignerService` gère les opérations en arrière-plan, et un nouveau système de permissions permet aux utilisateurs de contrôler quelles applications peuvent demander des signatures. Cela fait de Primal une alternative viable à Amber pour les utilisateurs Android qui veulent garder leurs clés dans une seule application tout en utilisant d'autres pour différentes expériences Nostr.

**Shopstr Zapsnags : Ventes flash via Lightning** - La place de marché native Nostr a introduit les [« Zapsnags »](https://github.com/shopstr-eng/shopstr/pull/211), une fonctionnalité de vente flash qui permet aux acheteurs d'acheter des articles directement depuis leur flux social avec un seul zap. L'implémentation filtre les notes kind 1 taguées avec `#shopstr-zapsnag` et les affiche comme des cartes produit avec un bouton « Zap to Buy » au lieu du flux panier standard. Quand un acheteur zappe, le système génère une demande de paiement utilisant [NIP-57](/fr/topics/nip-57/), interroge le reçu de zap kind 9735 pour confirmer le paiement, puis chiffre les informations de livraison en utilisant l'emballage cadeau [NIP-17](/fr/topics/nip-17/) avant de les envoyer en privé au vendeur. La fonctionnalité stocke les détails de l'acheteur localement pour les achats répétés et inclut un tableau de bord marchand pour créer des annonces de vente flash. C'est une combinaison astucieuse de primitives sociales, de paiement et de confidentialité qui démontre comment la conception composable de Nostr permet des modèles de commerce innovants.

**Mostro introduit un fonds de développement** - La plateforme de trading Bitcoin P2P [NIP-69](/fr/topics/nip-69/) a [implémenté des frais de développement configurables](https://github.com/MostroP2P/mostro/pull/555) pour soutenir une maintenance durable. Les opérateurs peuvent définir `dev_fee_percentage` entre 10-100% des frais de trading Mostro (par défaut 30%), qui achemine automatiquement vers un fonds de développement à chaque trade réussi. L'implémentation ajoute trois colonnes de base de données (`dev_fee`, `dev_fee_paid`, `dev_fee_payment_hash`) pour suivre les contributions et valide le pourcentage au démarrage du daemon. La documentation technique dans [`docs/DEV_FEE.md`](https://github.com/MostroP2P/mostro/blob/main/docs/DEV_FEE.md) explique le système. Ce modèle opt-in permet aux opérateurs de soutenir le développement continu tout en maintenant une transparence totale sur l'allocation des frais.

## Mises à jour NIP {#nip-updates}

Changements récents dans le [dépôt NIPs](https://github.com/nostr-protocol/nips) :

**Nouveaux NIPs :**
- **[NIP-A4](/fr/topics/nip-a4/) (Messages Publics, kind 24)** - Un nouveau kind pour les messages d'écran de notification conçu pour un support client large ([#1988](https://github.com/nostr-protocol/nips/pull/1988)). Contrairement aux conversations threadées, ces messages n'ont pas de concept d'historique de chat ou de chaînes de messages. Ils utilisent des tags `q` (citations) plutôt que des tags `e` pour éviter les complications de threading, les rendant idéaux pour des notifications publiques simples qui apparaissent dans le flux de notifications d'un destinataire sans créer d'état de conversation.

**Changements significatifs :**
- **[NIP-29](/fr/topics/nip-29/)** - Clarification majeure de la sémantique des groupes ([#2106](https://github.com/nostr-protocol/nips/pull/2106)). Le tag `closed` signifie maintenant « incapable d'écrire » (lecture seule pour les non-membres), découplé des mécaniques d'adhésion. Un nouveau tag `hidden` empêche les relais de servir les métadonnées ou événements de membres aux non-membres, permettant des groupes véritablement privés qui sont indécouverts sans invitation hors bande. Le tag `private` contrôle la visibilité des messages tout en permettant des métadonnées publiques pour la découverte.
- **[NIP-51](/fr/topics/nip-51/)** - Ajout du kind 30006 pour les ensembles d'images curées ([#2170](https://github.com/nostr-protocol/nips/pull/2170)), suivant le modèle de 30004 (articles) et 30005 (vidéos). Déjà implémenté dans Nostria.
- **[NIP-55](/fr/topics/nip-55/)** - Clarification de l'initiation de connexion pour les signers Android ([#2166](https://github.com/nostr-protocol/nips/pull/2166)). Les développeurs implémentant des sessions multi-utilisateurs utilisaient incorrectement `get_public_key` en l'appelant depuis des processus en arrière-plan. La spécification mise à jour recommande de l'appeler seulement une fois lors de la connexion initiale, prévenant une erreur d'implémentation courante.

## Analyse approfondie NIP : NIP-02 et NIP-10 {#nip-deep-dive-nip-02-and-nip-10}

Cette semaine, nous couvrons deux NIPs essentiels pour les fonctionnalités sociales : comment les clients savent qui vous suivez et comment les conversations sont threadées.

### [NIP-02](/fr/topics/nip-02/) : Liste d'abonnements

[NIP-02](https://github.com/nostr-protocol/nips/blob/master/02.md) définit les événements kind 3, qui stockent votre liste d'abonnements. Ce mécanisme simple alimente le graphe social qui rend les timelines possibles.

**Structure :** Un événement kind 3 contient des tags `p` listant les clés publiques suivies :

```json
{
  "id": "d7a8f...",
  "pubkey": "a3b9c...",
  "created_at": 1734912000,
  "kind": 3,
  "tags": [
    ["p", "91cf9..af5f", "wss://alicerelay.example.com", "alice"],
    ["p", "14aeb..8dad", "wss://bobrelay.example.com", "bob"],
    ["p", "612ae..982b", "", ""]
  ],
  "content": "",
  "sig": "e4f8a..."
}
```

Chaque tag `p` a quatre positions : le nom du tag, la clé publique suivie (hex), une indication de relais URL optionnelle, et un « petname » optionnel (un surnom local). L'indication de relais dit aux autres clients où trouver les événements de cet utilisateur. Le petname vous permet d'assigner des noms mémorables aux contacts sans vous fier à leurs noms d'affichage auto-déclarés.

**Comportement remplaçable :** Le Kind 3 tombe dans la plage remplaçable (0, 3, 10000-19999), donc les relais ne gardent que la dernière version par clé publique. Quand vous suivez quelqu'un de nouveau, votre client publie un nouveau kind 3 complet contenant tous vos abonnements plus le nouveau. Cela signifie que les listes d'abonnements doivent être complètes à chaque fois ; vous ne pouvez pas publier de mises à jour incrémentales.

**Construction des timelines :** Pour construire un flux d'accueil, les clients récupèrent le kind 3 de l'utilisateur, extraient toutes les clés publiques des tags `p`, puis s'abonnent aux événements kind 1 de ces auteurs :

```json
["REQ", "home", {"kinds": [1], "authors": ["91cf9...", "14aeb...", "612ae..."], "limit": 50}]
```

Le relais renvoie les notes correspondantes, et le client les affiche. Les indications de relais dans le kind 3 aident les clients à savoir quels relais interroger pour chaque utilisateur suivi.

**Petnames et identité :** Le champ petname permet un schéma de nommage décentralisé. Plutôt que de faire confiance au nom qu'un utilisateur revendique dans son profil, vous pouvez assigner votre propre étiquette. Un client pourrait afficher « alice (Ma Sœur) » où « alice » vient de son profil kind 0 et « Ma Sœur » est votre petname. Cela fournit un contexte que les noms d'utilisateur globaux ne peuvent pas offrir.

**Considérations pratiques :** Parce que les événements kind 3 sont remplaçables et doivent être complets, les clients devraient préserver les tags inconnus lors de la mise à jour. Si un autre client a ajouté des tags que votre client ne comprend pas, écraser aveuglément perdrait ces données. Ajoutez les nouveaux abonnements plutôt que de reconstruire à partir de zéro.

### [NIP-10](/fr/topics/nip-10/) : Threading des notes textuelles

[NIP-10](https://github.com/nostr-protocol/nips/blob/master/10.md) spécifie comment les notes kind 1 se référencent mutuellement pour former des fils de réponses. Comprendre ceci est essentiel pour construire des vues de conversation.

**Le problème :** Quand quelqu'un répond à une note, les clients doivent savoir : À quoi est-ce une réponse ? Quelle est la racine de la conversation ? Qui devrait être notifié ? NIP-10 répond à ces questions à travers les tags `e` (références d'événements) et les tags `p` (mentions de clés publiques).

**Tags marqués (préféré) :** Les clients modernes utilisent des marqueurs explicites dans les tags `e` :

```json
{
  "id": "f9c2e...",
  "pubkey": "a3b9c...",
  "created_at": 1734912345,
  "kind": 1,
  "tags": [
    ["e", "abc123...", "wss://relay.example.com", "root"],
    ["e", "def456...", "wss://relay.example.com", "reply"],
    ["p", "91cf9..."],
    ["p", "14aeb..."]
  ],
  "content": "Excellent point ! Je suis d'accord.",
  "sig": "b7d3f..."
}
```

Le marqueur `root` pointe vers la note originale qui a commencé le fil. Le marqueur `reply` pointe vers la note spécifique à laquelle on répond. Si vous répondez directement à la racine, utilisez seulement `root` (pas besoin de tag `reply`). La distinction compte pour l'affichage : le `reply` détermine l'indentation dans une vue de fil, tandis que `root` regroupe toutes les réponses ensemble.

**Règles de threading :**
- Réponse directe à la racine : Un tag `e` avec marqueur `root`
- Réponse à une réponse : Deux tags `e`, un `root` et un `reply`
- Le `root` reste constant tout au long du fil ; `reply` change selon ce à quoi vous répondez

**Tags pubkey pour les notifications :** Incluez des tags `p` pour tous ceux qui devraient être notifiés. Au minimum, taguez l'auteur de la note à laquelle vous répondez. La convention est aussi d'inclure tous les tags `p` de l'événement parent (pour que tout le monde dans la conversation reste dans la boucle), plus tous les utilisateurs que vous @mentionnez dans votre contenu.

**Indications de relais :** La troisième position dans les tags `e` et `p` peut contenir une URL de relais où cet événement ou le contenu de cet utilisateur pourrait être trouvé. Cela aide les clients à récupérer le contenu référencé même s'ils ne sont pas connectés au relais original.

**Tags positionnels dépréciés :** Les premières implémentations Nostr déduisaient le sens de la position des tags plutôt que des marqueurs : le premier tag `e` était la racine, le dernier était la réponse, ceux du milieu étaient des mentions. Cette approche est dépréciée car elle crée de l'ambiguïté. Si vous voyez des tags `e` sans marqueurs, ils proviennent probablement de clients plus anciens. Les implémentations modernes devraient toujours utiliser des marqueurs explicites.

**Construction des vues de fil :** Pour afficher un fil, récupérez l'événement racine, puis interrogez tous les événements avec un tag `e` référençant cette racine :

```json
["REQ", "thread", {"kinds": [1], "#e": ["<root-event-id>"]}]
```

Triez les résultats par `created_at` et utilisez les marqueurs `reply` pour construire la structure d'arbre. Les événements dont le `reply` pointe vers la racine sont des réponses de premier niveau ; les événements dont le `reply` pointe vers une autre réponse sont des réponses imbriquées.

## Sorties {#releases}

**Zeus v0.12.0** - S'appuyant sur le [support de paiements parallèles NWC de la semaine dernière](/fr/newsletters/2025-12-17-newsletter/#zeus), la [version majeure](https://github.com/ZeusLN/zeus/releases/tag/v0.12.0) du portefeuille Lightning livre un service Nostr Wallet Connect [NIP-47](/fr/topics/nip-47/) complet avec support de relais personnalisé et suivi de budget. Une [correction de rechargement de budget](https://github.com/ZeusLN/zeus/pull/3455) assure que les connexions utilisent les limites actuelles. [La copie d'adresse Lightning](https://github.com/ZeusLN/zeus/pull/3460) n'inclut plus le préfixe `lightning:`, corrigeant les problèmes de collage dans les champs de profil Nostr.

**Amber v4.0.6** - Le signer Android [NIP-55](/fr/topics/nip-55/) [ajoute la mise en cache des performances](https://github.com/greenart7c3/Amber/releases/tag/v4.0.6) aux opérations de signature et améliore la gestion des erreurs lors du déchiffrement de contenu malformé. La fiabilité de connexion améliorée avec une logique de réessai pour les événements de connexion relais, et plusieurs corrections de crash adressent les cas limites autour des URI `nostrconnect://` invalides et des interactions de l'écran de permissions.

**nak v0.17.3** - La [dernière version](https://github.com/fiatjaf/nak/releases/tag/v0.17.3) de l'outil Nostr en ligne de commande restreint les builds LMDB à Linux, corrigeant les problèmes de compilation cross-platform.

**Aegis v0.3.4** - Le signer Nostr cross-platform [ajoute le support](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.4) du schéma URI `nostrsigner:` défini dans [NIP-55](/fr/topics/nip-55/), correspondant au flux de connexion d'Amber. Les données de relais local peuvent maintenant être importées et exportées pour la sauvegarde, et la version inclut des corrections de bugs pour les erreurs de socket relais et des améliorations UI pour l'interface du relais local.

## Changements notables de code et documentation {#notable-code-and-documentation-changes}

*Ce sont des pull requests ouvertes et du travail en phase précoce, parfaits pour obtenir des retours avant fusion. Si quelque chose attire votre attention, considérez la review ou les commentaires !*

### Damus (iOS) {#damus}

[Persistance de la liste de mutes](https://github.com/damus-io/damus/pull/3469) corrige un problème où les listes de mutes étaient effacées au démarrage à froid. La correction ajoute des gardes pour prévenir les écrasements accidentels pendant l'initialisation de l'application. [Timing du flux de profil](https://github.com/damus-io/damus/pull/3457) élimine un délai d'environ 1 seconde avant que les profils en cache n'apparaissent. Précédemment, les vues attendaient le redémarrage des tâches d'abonnement ; maintenant `streamProfile()` renvoie immédiatement les données en cache de NostrDB, supprimant la fenêtre où les clés publiques abrégées et les images placeholder s'affichaient.

### White Noise (Messagerie chiffrée) {#white-noise}

[Streaming de messages en temps réel](https://github.com/marmot-protocol/whitenoise/pull/919) remplace le mécanisme de polling précédent par une architecture basée sur les streams. Le nouveau `ChatStreamNotifier` consomme directement le stream de messages du SDK Rust, maintenant l'ordre chronologique et gérant les mises à jour incrémentales efficacement. Les tests ont montré une amélioration significative de la réactivité. Une [API de liste de chats](https://github.com/marmot-protocol/whitenoise/pull/921) ajoute `get_chat_list` pour récupérer les résumés de conversation, et une [correction de tri stable](https://github.com/marmot-protocol/whitenoise/pull/905) prévient les boucles de réordonnancement de messages en utilisant `createdAt` avec l'ID de message comme critère de départage.

### NDK (Bibliothèque) {#ndk}

Deux pull requests ont livré des améliorations dramatiques de performance du cache. [PR #371](https://github.com/nostr-dev-kit/ndk/pull/371) a corrigé un bug où les événements lus depuis le cache SQLite étaient immédiatement réécrits, causant 100% d'écritures dupliquées au démarrage de l'application. La correction ajoute une garde `fromCache` et implémente une vérification de doublons O(1) via un Set en mémoire. Pour les petits ensembles de résultats (<100 événements), le transfert JSON direct remplace le surcoût d'encodage binaire. [PR #372](https://github.com/nostr-dev-kit/ndk/pull/372) a supprimé les appels `seenEvent` inutiles pour les événements en cache. La recherche dans le cache LRU coûtait 0.24-0.64ms par événement ; pour 5 700 événements en cache, cela ajoutait environ 1.4 secondes de surcoût. Résultat : les requêtes de cache sont passées d'environ 3 690ms à environ 22ms (162x plus rapide).

### rust-nostr (Bibliothèque) {#rust-nostr}

[Support REQ multi-filtres](https://github.com/rust-nostr/nostr/pull/1176) a été restauré après avoir été supprimé dans un refactoring précédent. Le SDK accepte à nouveau `Vec<Filter>` pour les requêtes d'abonnement, permettant des requêtes efficaces qui combinent plusieurs conditions de filtre avec la logique OR. [La provenance du relais](https://github.com/rust-nostr/nostr/pull/1156) a été ajoutée aux méthodes `stream_events*`, donc chaque événement streamé inclut maintenant le `RelayUrl` dont il provient et un `Result` indiquant le succès ou l'échec, utile pour suivre la fiabilité des relais et déboguer les problèmes de connexion. Une [correction de sécurité](https://github.com/rust-nostr/nostr/pull/1179) a supprimé la dépendance `url-fork` suite à RUSTSEC-2024-0421, éliminant une vulnérabilité connue.

### Applesauce (Bibliothèque) {#applesauce}

La bibliothèque TypeScript alimentant [noStrudel](https://github.com/hzrd149/nostrudel) a connu un développement significatif cette semaine. Les nouveaux modèles incluent un [système de réactions](https://github.com/hzrd149/applesauce) et le casting de groupes d'utilisateurs. Les fonctionnalités de portefeuille se sont étendues avec le support NIP-60, un onglet d'envoi et des outils de récupération de tokens améliorés. Une nouvelle propriété `user.directMessageRelays$` expose la configuration des relais DM. Toutes les actions ont été refactorisées pour utiliser des interfaces async (supprimant les générateurs async), et des corrections de bugs ont adressé la restauration de contenu chiffré et les cas limites des filtres d'événements basés sur le temps.

### Tenex (Agents IA) {#tenex}

Le [système de coordination multi-agents](https://github.com/tenex-chat/tenex) construit sur Nostr a introduit l'architecture RAL (Request-Action-Lifecycle) dans [cinq PRs fusionnés](https://github.com/pablof7z/tenex/pull/38). RAL permet aux agents de se mettre en pause lors de la délégation de tâches et de reprendre quand les résultats arrivent, avec une persistance d'état limitée à la conversation. Les outils de délégation (`delegate`, `ask`, `delegate_followup`, `delegate_external`) publient maintenant des événements Nostr et retournent des signaux d'arrêt au lieu de bloquer. Le refactoring inclut la migration AI SDK v6, l'infrastructure de test VCR pour l'enregistrement déterministe des interactions LLM, et le support d'images multimodal.

---

C'est tout pour cette semaine. Vous construisez quelque chose ? Vous avez des nouvelles à partager ? Vous voulez que nous couvrions votre projet ? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contactez-nous via DM NIP-17</a> ou trouvez-nous sur Nostr.

