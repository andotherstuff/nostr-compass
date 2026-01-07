---
title: 'Nostr Compass #4'
date: 2026-01-07
publishDate: 2026-01-07
draft: false
type: newsletters
---

Bienvenue dans Nostr Compass, votre guide hebdomadaire de l'écosystème du protocole Nostr.

**Cette semaine :** Primal Android intègre la signature à distance [NIP-46](/fr/topics/nip-46/) et le support du signataire local [NIP-55](/fr/topics/nip-55/), en faisant un hub de signature complet pour les autres applications Android. L'équipe du [Protocole Marmot](/fr/topics/marmot/) a répondu aux conclusions d'un audit de sécurité avec 18 PR fusionnées renforçant la messagerie chiffrée basée sur [MLS](/fr/topics/mls/). Citrine atteint la v1.0 et Applesauce livre la v5.0 sur l'ensemble de sa suite de bibliothèques. TENEX développe la supervision des agents IA sur Nostr, et Jumble ajoute un pooling intelligent des relais. Une correction de la spec NIP-55 clarifie les champs de retour de `nip44_encrypt`, et une PR [NIP-50](/fr/topics/nip-50/) propose des extensions d'expressions de requête pour la recherche avancée. Dans notre analyse approfondie, nous expliquons [NIP-04](/fr/topics/nip-04/) et [NIP-44](/fr/topics/nip-44/) : pourquoi le chiffrement historique présente des failles de sécurité et comment le remplacement moderne les corrige.

## Actualités

**Primal Android devient un hub de signature complet** - La [version 2.6.18](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18) ajoute à la fois la signature à distance [NIP-46](/fr/topics/nip-46/) et la signature locale [NIP-55](/fr/topics/nip-55/), transformant Primal en un signataire complet pour les autres applications Nostr. La signature à distance via NIP-46 permet aux utilisateurs de se connecter aux services bunker via les relais Nostr, gardant les clés entièrement hors de leur appareil. La signature locale via NIP-55 expose Primal comme un fournisseur de contenu Android, permettant aux applications comme Amethyst ou Citrine de demander des signatures sans jamais toucher à la clé privée. [Plusieurs PR de suivi](https://github.com/PrimalHQ/primal-android-app/pull/839) ont corrigé des problèmes de compatibilité avec l'exigence de pubkey hexadécimale de la spec NIP-55, et amélioré l'analyse des URI `nostrconnect://` malformées. La version inclut également la pré-mise en cache des médias pour un défilement plus fluide, des temps de chargement des fils améliorés et la pré-mise en cache des avatars.

**Le Protocole Marmot renforce la sécurité après un audit** - Le [Marmot Development Kit](https://github.com/marmot-protocol/mdk) (mdk), qui implémente la messagerie chiffrée de bout en bout basée sur MLS [NIP-104](/fr/topics/nip-104/), a reçu d'importants correctifs de sécurité cette semaine. Dix-huit pull requests fusionnées ont traité les conclusions de l'audit, notamment : la [vérification de hachage pour les images de groupe chiffrées](https://github.com/marmot-protocol/mdk/pull/97) pour prévenir les attaques de substitution de blobs au niveau du stockage, la [pagination des welcomes en attente](https://github.com/marmot-protocol/mdk/pull/110) pour prévenir l'épuisement de la mémoire, la [fuite d'ID de groupe MLS dans les messages d'erreur](https://github.com/marmot-protocol/mdk/pull/112), et l'[application de l'encodage base64](https://github.com/marmot-protocol/mdk/pull/98) pour les packages de clés. La [spec Marmot elle-même a été mise à jour](https://github.com/marmot-protocol/marmot/pull/20) avec le versionnement MIP-04 v2 et des améliorations de sécurité. Des PR actives continuent de traiter la réutilisation de nonce, la mise à zéro des secrets et les vecteurs de pollution du cache.

**Nostrability suit le support des indications de relais** - Un nouveau [tracker de compatibilité des indications de relais](https://github.com/nostrability/nostrability/issues/270) documente comment les clients construisent et consomment les indications de relais à travers l'écosystème. Le tracker révèle que bien que la plupart des clients construisent maintenant des indications selon [NIP-10](/fr/topics/nip-10/) et [NIP-19](/fr/topics/nip-19/), la consommation varie largement : certains clients incluent des indications dans les événements sortants mais n'utilisent pas les indications entrantes pour la récupération. Six clients ont obtenu le statut "Full" pour une implémentation complète. Le tracker est utile pour les développeurs vérifiant l'interopérabilité et pour les utilisateurs se demandant pourquoi certains clients trouvent du contenu que d'autres ne peuvent pas trouver.

**Nostria 2.0 livre une refonte des fonctionnalités multi-plateformes** - Le client [Nostria](https://nostria.app) [a publié la version 2.0](https://njump.me/nevent1qqs9z4l8z82zphszjlmrjkr8whpvupnlaxc7xk5gfg9syzj0thygtzgpz4mhxue69uhhyetvv9ujuerpd46hxtnfduhszxthwden5te0wfjkccte9enrw73wd9hsz9nhwden5te0wfjkccte9ec8y6tdv9kzumn9wsq3gamnwvaz7tmjv4kxz7fwv3sk6atn9e5k7qgkwaehxw309aex2mrp0yhxgctdw4eju6t09uq32amnwvaz7tmwdaejumr0dshsz9mhwden5te0wfjkccte9ec82c30989ksmfnv9kzumn9wshsqgzxsnsv7pfqqd7rw4fvr0jnkpqmwzfqq3znlc4pqunagxrkl84u66y7fq9) le 30 décembre avec des ajouts significatifs sur iOS (TestFlight), Android (Play Store), Web et Windows. La version ajoute le support natif de la musique avec création de playlists, téléchargement de pistes, paiements aux artistes via zaps et un lecteur style WinAmp avec égaliseur fonctionnel. Le streaming en direct bénéficie de l'intégration de l'API de jeu montrant des métadonnées enrichies pendant les streams de gameplay. Une nouvelle fonctionnalité Résumé génère des digests d'activité horaires, quotidiens ou hebdomadaires sous forme de vues de timeline compressées. La section Découvrir offre des listes curatées pour trouver du contenu et des profils. La publication de médias est simplifiée avec la génération automatique de publications courtes pour la découvrabilité inter-clients. Les connexions aux signataires distants fonctionnent maintenant via scan de code QR sans configuration manuelle. La découverte de profils répond à un point douloureux courant de Nostr : lorsque les utilisateurs changent de relais sans emporter leurs métadonnées, Nostria localise leur profil et le republie sur leurs relais actuels. Les abonnés Premium bénéficient de l'intégration de chaînes YouTube, de Memos privés, de tableaux de bord analytiques et de sauvegardes automatiques de la liste de suivi avec options de fusion/restauration.

## Mises à jour des NIP

Changements récents dans le [dépôt NIPs](https://github.com/nostr-protocol/nips) :

**Fusionné :**
- **[NIP-55](/fr/topics/nip-55/)** - Correction du champ de retour pour la méthode `nip44_encrypt` ([#2184](https://github.com/nostr-protocol/nips/pull/2184)). Les signataires Android doivent maintenant retourner le payload chiffré dans le champ `signature` (comme `nip44_decrypt`) plutôt que dans un champ séparé. Cela aligne la spec avec les implémentations existantes dans Amber et Primal.

**PR ouvertes :**
- **[NIP-50](/fr/topics/nip-50/)** - Extensions d'expressions de requête ([#2182](https://github.com/nostr-protocol/nips/pull/2182)) propose d'étendre la recherche NIP-50 avec des expressions de requête structurées. La PR ajoute des opérateurs comme `kind:1`, `author:npub1...`, et des combinaisons booléennes (`AND`, `OR`, `NOT`), permettant des requêtes de recherche plus précises au-delà de la simple correspondance de texte. Cela permettrait aux clients de construire des interfaces de recherche avancées tout en maintenant la compatibilité ascendante avec les chaînes de recherche basiques.

## Analyse approfondie des NIP : NIP-04 et NIP-44

Cette semaine, nous couvrons les standards de chiffrement de Nostr : le NIP-04 historique que vous rencontrerez encore, et son remplacement moderne NIP-44 qui corrige des failles de sécurité critiques.

### [NIP-04](/fr/topics/nip-04/) : Messages directs chiffrés (historique)

[NIP-04](https://github.com/nostr-protocol/nips/blob/master/04.md) était la première tentative de Nostr pour la messagerie chiffrée, utilisant des événements kind 4. Bien que simple à implémenter, il présente des faiblesses de sécurité connues et est déprécié en faveur de NIP-44.

**Comment ça fonctionne :** NIP-04 utilise ECDH (Elliptic Curve Diffie-Hellman) pour dériver un secret partagé entre l'expéditeur et le destinataire, puis chiffre avec AES-256-CBC.

```json
{
  "id": "<event-id>",
  "pubkey": "<sender-pubkey>",
  "created_at": 1736200000,
  "kind": 4,
  "tags": [["p", "<recipient-pubkey>"]],
  "content": "base64-ciphertext?iv=base64-iv",
  "sig": "<signature>"
}
```

Le flux de chiffrement :
1. Calculer le point partagé : `shared = ECDH(sender_privkey, recipient_pubkey)`
2. Dériver la clé : `key = SHA256(shared_x_coordinate)`
3. Générer un IV aléatoire de 16 octets
4. Chiffrer : `ciphertext = AES-256-CBC(key, iv, plaintext)`
5. Formater le contenu : `base64(ciphertext)?iv=base64(iv)`

**Problèmes de sécurité :**

- **Pas d'authentification :** AES-CBC fournit la confidentialité mais pas l'intégrité. Un attaquant qui contrôle un relais pourrait modifier les bits du texte chiffré, causant des changements prévisibles au texte clair (attaques par inversion de bits).
- **IV en clair :** Le vecteur d'initialisation est transmis avec le texte chiffré, et le mode CBC avec des IV prévisibles permet des attaques à texte clair choisi.
- **Pas de validation du padding :** Les implémentations varient dans leur gestion du padding PKCS#7, permettant potentiellement des attaques par oracle de padding.
- **Exposition des métadonnées :** La pubkey de l'expéditeur, la pubkey du destinataire et l'horodatage sont tous visibles par les relais.
- **Réutilisation de clé :** Le même secret partagé est utilisé pour tous les messages entre deux parties, indéfiniment.

**Pourquoi il existe encore :** De nombreux anciens clients et relais ne supportent que NIP-04. Vous le rencontrerez lors d'interactions avec des systèmes héritage. Les signataires comme Amber et les applications comme Primal implémentent encore `nip04_encrypt`/`nip04_decrypt` pour la compatibilité ascendante.

### [NIP-44](/fr/topics/nip-44/) : Chiffrement versionné

[NIP-44](https://github.com/nostr-protocol/nips/blob/master/44.md) est le standard de chiffrement moderne, conçu pour corriger les failles bien connues de NIP-04. Un audit de sécurité Cure53 des implémentations NIP-44 a identifié 10 problèmes (incluant des attaques temporelles et des préoccupations de confidentialité persistante) qui ont été traités avant la finalisation de la spec. Il utilise ChaCha20-Poly1305 avec une dérivation de clé appropriée et un chiffrement authentifié.

**Améliorations clés par rapport à NIP-04 :**

| Aspect         | NIP-04                     | NIP-44                  |
|:---------------|:---------------------------|:------------------------|
| Chiffrement    | AES-256-CBC                | XChaCha20-Poly1305      |
| Authentification | Aucune                   | MAC Poly1305            |
| Dérivation de clé | SHA256(shared_x)        | HKDF avec sel           |
| Nonce          | IV 16 octets, patron réutilisé | Nonce aléatoire 24 octets |
| Padding        | PKCS#7 (fuite de longueur) | Padding puissance de 2  |
| Versionnement  | Aucun                      | Octet de version préfixé |

**Flux de chiffrement :**

1. **Clé de conversation :** Dériver une clé stable pour chaque paire expéditeur-destinataire :
   ```
   shared_x = ECDH(sender_privkey, recipient_pubkey).x
   conversation_key = HKDF-SHA256(
     ikm = shared_x,
     salt = "nip44-v2",
     info = ""
   )
   ```

2. **Clés de message :** Pour chaque message, générer un nonce aléatoire de 32 octets et dériver les clés de chiffrement/authentification :
   ```
   keys = HKDF-SHA256(
     ikm = conversation_key,
     salt = nonce,
     info = "nip44-v2"
   )
   chacha_key = keys[0:32]
   chacha_nonce = keys[32:44]
   hmac_key = keys[44:76]
   ```

3. **Padding du texte clair :** Padding à la puissance de 2 suivante (minimum 32 octets) pour masquer la longueur du message :
   ```
   padded = [length_u16_be] + [plaintext] + [zeros to next power of 2]
   ```

4. **Chiffrer et authentifier :**
   ```
   ciphertext = XChaCha20(chacha_key, chacha_nonce, padded)
   mac = HMAC-SHA256(hmac_key, nonce + ciphertext)
   ```

5. **Formater le payload :**
   ```
   payload = [version=0x02] + [nonce] + [ciphertext] + [mac]
   content = base64(payload)
   ```

**Octet de version :** Le premier octet (`0x02`) indique la version de chiffrement. Cela permet des mises à niveau futures sans casser les messages existants. La version `0x01` était un brouillon antérieur qui n'a jamais été largement déployé.

**Déchiffrement :**

1. Décoder le base64, vérifier que l'octet de version est `0x02`
2. Extraire le nonce (octets 1-32), le texte chiffré et le MAC (derniers 32 octets)
3. Dériver la clé de conversation en utilisant la clé privée du destinataire et la clé publique de l'expéditeur
4. Dériver les clés de message à partir de la clé de conversation et du nonce
5. Vérifier le MAC avant de déchiffrer (rejeter si invalide)
6. Déchiffrer le texte chiffré, extraire le préfixe de longueur, retourner le texte clair sans padding

**Propriétés de sécurité :**

- **Chiffrement authentifié :** Le MAC Poly1305 garantit que toute altération est détectée avant le déchiffrement
- **Confidentialité persistante (partielle) :** Chaque message utilise un nonce unique, donc compromettre un message ne révèle pas les autres. Cependant, compromettre une clé privée révèle toujours tous les messages passés (pas de ratcheting).
- **Masquage de longueur :** Le padding en puissance de 2 obscurcit la longueur exacte du message
- **Résistance aux attaques temporelles :** Comparaison à temps constant pour la vérification du MAC

**Utilisation en pratique :** NIP-44 est la couche de chiffrement pour :
- Les messages directs privés [NIP-17](/fr/topics/nip-17/) (à l'intérieur du gift wrap)
- La communication avec les signataires distants [NIP-46](/fr/topics/nip-46/)
- Le chiffrement seal [NIP-59](/fr/topics/nip-59/)
- Les messages de groupe [Protocole Marmot](/fr/topics/nip-104/), où NIP-44 enveloppe le contenu chiffré MLS en utilisant une clé dérivée du secret exportateur MLS
- Toute application nécessitant un chiffrement sécurisé point-à-point

**Guide de migration :** Les nouvelles applications devraient utiliser exclusivement NIP-44. Pour la compatibilité ascendante, vérifiez si le client d'un contact supporte NIP-44 (via les métadonnées d'application [NIP-89](/fr/topics/nip-89/) ou le support du relais) avant de revenir à NIP-04. Lors de la réception de messages, tentez d'abord le déchiffrement NIP-44, puis revenez à NIP-04 pour le contenu héritage.

## Versions

**Primal Android v2.6.18** - La [version complète](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18) ajoute la signature à distance [NIP-46](/fr/topics/nip-46/) et la signature locale [NIP-55](/fr/topics/nip-55/), transformant Primal en hub de signature pour les autres applications Android. Les améliorations de performance incluent la pré-mise en cache des médias, la pré-mise en cache des avatars et un chargement plus rapide des fils. Les corrections de bugs traitent les auto-mentions dans les bios, les crashs de la galerie média et les replis de titres de stream. Sur iOS, Primal utilise la lecture audio en arrière-plan pour garder l'application active pour recevoir les demandes de signature NIP-46 ; les utilisateurs peuvent changer le son ou le couper entièrement dans les paramètres.

**Mostro v0.15.6** - La [dernière version](https://github.com/MostroP2P/mostro/releases/tag/v0.15.6) du bot de trading Bitcoin P2P [NIP-69](/fr/topics/nip-69/) complète l'implémentation du fonds de développement avec les événements d'audit Phase 4. Les paiements de frais de développement sont maintenant suivis via des événements Nostr kind 38383 publiés après chaque paiement réussi, permettant la vérification et l'analyse par des tiers. Les calculs de montants ont été corrigés pour les messages acheteur/vendeur, et la logique de premium a été alignée avec l'implémentation de référence lnp2pbot.

**Aegis v0.3.5** - Le signataire multi-plateforme [ajoute le mode sombre](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.5), un affichage amélioré des icônes d'application et des mises en page UI plus propres. Les corrections de bugs traitent les conflits iCloud Private Relay sur iOS et les problèmes d'analyse d'événements. La version améliore également la façon dont le JSON d'événement est passé à la fonction de signature Rust.

**Citrine v1.0.0** - L'application relais Android [atteint la 1.0](https://github.com/greenart7c3/Citrine/releases/tag/v1.0.0). Citrine vous permet d'exécuter un relais Nostr personnel directement sur votre appareil Android, utile pour le cache local, la sauvegarde ou comme compagnon NIP-55. Cette version ajoute un gestionnaire de rapports de crash, améliore l'efficacité des requêtes de base de données et met à jour les traductions via Crowdin.

**Applesauce v5.0.0** - La suite de bibliothèques TypeScript de hzrd149 [livre une version majeure](https://github.com/hzrd149/applesauce/releases) avec des changements cassants axés sur la correction et la simplicité. Le package core [vérifie maintenant les signatures d'événements par défaut](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%405.0.0) et renomme les méthodes de coordonnées pour utiliser une terminologie "address" plus claire (`parseCoordinate` -> `parseReplaceableAddress`). Le package relay [réduit les tentatives par défaut de 10 à 3](https://github.com/hzrd149/applesauce/releases/tag/applesauce-relay%405.0.0) et ignore les relais inaccessibles par défaut, plus ajoute `createUnifiedEventLoader` pour une récupération d'événements plus simple. Le package wallet gagne la [découverte de mint Cashu NIP-87](/fr/topics/nip-87/). Les dépendances directes à `nostr-tools` ont été supprimées dans tous les packages, réduisant la taille du bundle et les conflits de versions.

## Changements notables de code et de documentation

*Ce sont des pull requests ouvertes et des travaux en phase initiale, parfaits pour obtenir des retours avant fusion. Si quelque chose attire votre attention, envisagez de réviser ou commenter !*

### Damus (iOS)

Une série de PR améliore l'expérience des articles longs. Les [améliorations UX de lecture](https://github.com/damus-io/damus/pull/3496) ajoutent une barre de progression, un temps de lecture estimé, un mode sépia, une hauteur de ligne ajustable et un mode focus qui masque la navigation pendant le défilement. Les [corrections d'images](https://github.com/damus-io/damus/pull/3489) garantissent que les images dans le contenu markdown s'affichent avec les bons ratios d'aspect en pré-traitant les images autonomes comme éléments de niveau bloc. Les [cartes d'aperçu d'articles longs](https://github.com/damus-io/damus/pull/3497) remplacent le texte inline `@naddr1...` par des cartes d'aperçu riches montrant le titre et les métadonnées de l'article. Une nouvelle [suite de tests d'intégration relais](https://github.com/damus-io/damus/pull/3508) ajoute 137 tests liés au réseau incluant la vérification du protocole [NIP-01](/fr/topics/nip-01/) et le comportement sous conditions réseau dégradées (simulation 3G).

### Bitchat (Messagerie chiffrée)

Renforcement de la sécurité dans le messager Nostr+Cashu iOS. L'[effacement des secrets DH du protocole Noise](https://github.com/permissionlesstech/bitchat/pull/928) corrige six emplacements où les secrets partagés n'étaient pas mis à zéro après l'accord de clé Diffie-Hellman, restaurant les garanties de confidentialité persistante. La [sécurité des threads pour les files d'accusés de réception](https://github.com/permissionlesstech/bitchat/pull/929) ajoute la synchronisation par barrière pour prévenir les conditions de course dans NostrTransport. L'[optimisation du déduplicateur de messages](https://github.com/permissionlesstech/bitchat/pull/920) améliore les performances avec des volumes de messages élevés, et le [renforcement de l'analyse des chaînes hexadécimales](https://github.com/permissionlesstech/bitchat/pull/919) prévient les crashs dus à des entrées malformées.

### Frostr (Signature à seuil)

Le protocole de signature à seuil basé sur [FROST](/fr/topics/frost/) [a ajouté l'affichage de codes QR](https://github.com/FROSTR-ORG/igloo-desktop/pull/62) pour les identifiants de groupe et les identifiants de partage pendant l'onboarding et dans l'interface du signataire. Cela facilite la configuration lors de la distribution des parts de clé sur plusieurs appareils, permettant aux utilisateurs de scanner les identifiants au lieu de copier manuellement de longues chaînes.

### Marmot mdk (Bibliothèque)

Au-delà des correctifs de sécurité mentionnés ci-dessus, des PR actives traitent les conclusions d'audit restantes : le [type Secret<T> pour la mise à zéro](https://github.com/marmot-protocol/mdk/pull/109) introduit un type wrapper qui met automatiquement à zéro les données sensibles à la destruction, la [pagination des requêtes de messages](https://github.com/marmot-protocol/mdk/pull/111) prévient l'épuisement de la mémoire lors du chargement de l'historique de chat, et le [stockage chiffré](https://github.com/marmot-protocol/mdk/pull/102) ajoute le chiffrement au repos pour la base de données SQLite stockant l'état du groupe et les messages.

### Amethyst (Android)

Une semaine chargée de corrections de stabilité dans le client Android. L'[analyse JSON tolérante](https://github.com/vitorpamplona/amethyst/commit/2c42796) prévient les crashs dus aux événements malformés en rendant la sérialisation Kotlin plus indulgente. La validation des événements [vérifie maintenant la taille du champ kind](https://github.com/vitorpamplona/amethyst/commit/40f9622) avant traitement pour éviter les exceptions dues à des valeurs surdimensionnées. L'UI du score de confiance a reçu une icône plus petite pour réduire l'interférence visuelle, et la [journalisation des erreurs améliorée](https://github.com/vitorpamplona/amethyst/commit/69c53ac) aide à diagnostiquer les problèmes de connexion aux relais. Les mises à jour de traduction sont arrivées via Crowdin, et plusieurs avertissements SonarQube ont été traités.

### TENEX (Agents IA)

Le framework d'agents IA natif Nostr a vu 81 commits cette semaine développant des capacités autonomes. Le nouveau [système de supervision des agents](https://github.com/tenex-chat/tenex/pull/48) implémente des heuristiques comportementales pour surveiller les actions des agents et intervenir si nécessaire. La [transparence de délégation](https://github.com/tenex-chat/tenex/commit/b244c10) ajoute la journalisation des interventions utilisateur aux transcriptions de délégation, permettant aux utilisateurs d'auditer ce que les agents ont fait en leur nom. Le [registre de fournisseurs LLM](https://github.com/tenex-chat/tenex/pull/47) a été modularisé pour une intégration plus facile de différents backends IA. Le support de conversation inter-projets permet aux agents de maintenir le contexte à travers plusieurs projets basés sur Nostr.

### Jumble (Client Web)

Le client web axé sur les relais a ajouté plusieurs améliorations de l'expérience utilisateur. Le [pool de relais intelligent](https://github.com/CodyTseng/jumble/commit/695f2fe) gère intelligemment les connexions selon les patterns d'utilisation. Le [toggle de flux en direct](https://github.com/CodyTseng/jumble/commit/917fcd9) permet aux utilisateurs de basculer entre le streaming en temps réel et le rafraîchissement manuel. L'[affichage automatique des nouvelles notes](https://github.com/CodyTseng/jumble/commit/d1b3a8c) en haut fait remonter le contenu frais sans nécessiter de rechargement de page. Le [cache persistant](https://github.com/CodyTseng/jumble/commit/fd9f41c) pour le flux de suivi et les notifications améliore les temps de chargement lors des visites de retour. Les utilisateurs peuvent maintenant [changer les relais par défaut](https://github.com/CodyTseng/jumble/commit/53a67d8) via les paramètres.

---

C'est tout pour cette semaine. Vous construisez quelque chose ? Vous avez des nouvelles à partager ? Vous voulez que nous couvrions votre projet ? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contactez-nous via DM NIP-17</a> ou trouvez-nous sur Nostr.
