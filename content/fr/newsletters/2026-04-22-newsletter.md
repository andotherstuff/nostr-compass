---
title: 'Nostr Compass #19'
date: 2026-04-22
translationOf: /en/newsletters/2026-04-22-newsletter.md
translationDate: 2026-04-22
draft: false
type: newsletters
---

Bienvenue dans Nostr Compass, votre guide hebdomadaire sur Nostr.

**Cette semaine :** [Amethyst](https://github.com/vitorpamplona/amethyst) livre une grosse vague de travail autour de [Marmot](/fr/topics/marmot/), des communautés [NIP-72](/fr/topics/nip-72/), des objectifs de zap [NIP-75](/fr/topics/nip-75/) et des salons audio sur Media over QUIC. [TollGate](https://github.com/OpenTollGate/tollgate) stabilise l'accès internet pay-per-use sur Nostr et Cashu avec [v0.1.0](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0). [nostream](https://github.com/Cameri/nostream) clôt une grosse semaine de travail relay autour de [NIP-45](/fr/topics/nip-45/), [NIP-62](/fr/topics/nip-62/), de la compression et du durcissement des requêtes. [Forgesworn](https://github.com/forgesworn) publie une pile complète de signature, d'identité et d'API payante pour Nostr. [ShockWallet](https://github.com/shocknet/wallet2) poursuit la synchronisation native à Nostr de wallet Lightning, et les suites Formstr, StableKraft, Keep, topaz, WoT Relay et Flotilla complètent les sorties notables. Les deep dives de la semaine couvrent [NIP-72](/fr/topics/nip-72/) et [NIP-57](/fr/topics/nip-57/).

## Actualités

### Amethyst livre la conformité MIP de Marmot, les communautés NIP-72, les objectifs de zap et les salons audio MoQ

[Amethyst](https://github.com/vitorpamplona/amethyst) a fusionné 57 PRs cette semaine. Les thèmes dominants sont la conformité des groupes chiffrés [Marmot](/fr/topics/marmot/), la prise en charge native des communautés modérées [NIP-72](/fr/topics/nip-72/), les objectifs de zap [NIP-75](/fr/topics/nip-75/) sur les live streams [NIP-53](/fr/topics/nip-53/) et une nouvelle pile de salons audio reposant sur Media over QUIC.

Sur Marmot, les [PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462), [#2435](https://github.com/vitorpamplona/amethyst/pull/2435), [#2436](https://github.com/vitorpamplona/amethyst/pull/2436), [#2466](https://github.com/vitorpamplona/amethyst/pull/2466), [#2471](https://github.com/vitorpamplona/amethyst/pull/2471), [#2477](https://github.com/vitorpamplona/amethyst/pull/2477) et [#2493](https://github.com/vitorpamplona/amethyst/pull/2493) ferment progressivement les écarts d'interop, de framing MLS, de KeyPackage Relay List et de validation cryptographique. [PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) ajoute aussi `amy`, un CLI piloté depuis l'implémentation d'Amethyst pour les opérations de groupe Marmot et MLS. Côté communautés, [PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468) ajoute la création et la modération de communautés [NIP-72](/fr/topics/nip-72/). Côté live streaming, [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) branche les objectifs de zap [NIP-75](/fr/topics/nip-75/) dans l'UI [NIP-53](/fr/topics/nip-53/), et [PR #2494](https://github.com/vitorpamplona/amethyst/pull/2494) ajoute le transport MoQ et les salons audio en temps réel.

### TollGate v0.1.0 stabilise l'accès internet pay-per-use sur Nostr et Cashu

[TollGate](https://github.com/OpenTollGate/tollgate) a publié [v0.1.0](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0) le 21 avril, premier snapshot tagué de ses spécifications d'accès réseau pay-per-use. Le protocole permet à un routeur WiFi, un switch Ethernet ou un partage Bluetooth de publier ses tarifs, d'accepter des tokens ecash [Cashu](/fr/topics/cashu/) et de gérer des sessions prépayées sans comptes, sans abonnements et sans KYC.

La release fixe trois couches : [TIP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md) pour les événements de base (Advertisement, Session, Notice), [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md) pour les paiements Cashu, [HTTP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/HTTP-01.md) à HTTP-03 pour l'interface HTTP, [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md) pour le transport via relays Nostr et [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md) pour le medium WiFi captive portal. Le nouvel article de sujet [TollGate](/fr/topics/tollgate/) couvre toute cette pile plus en détail.

### nostream fusionne 53 PRs pour NIP-45, NIP-62, la compression et le durcissement des requêtes

[nostream](https://github.com/Cameri/nostream), l'implémentation relay TypeScript de Cameri, a fusionné 53 PRs en une semaine. [PR #522](https://github.com/Cameri/nostream/pull/522) ajoute le support `COUNT` [NIP-45](/fr/topics/nip-45/), [PR #544](https://github.com/Cameri/nostream/pull/544) ajoute [NIP-62](/fr/topics/nip-62/) à la liste de fonctionnalités annoncées, [PR #548](https://github.com/Cameri/nostream/pull/548) étend le schéma de filtre aux tags majuscules `#A` à `#Z`, et [PR #514](https://github.com/Cameri/nostream/pull/514) ajoute gzip et xz pour l'import/export d'événements.

[PR #534](https://github.com/Cameri/nostream/pull/534) ajoute un harness de benchmarks et optimise la traduction filtre-vers-SQL, [PR #524](https://github.com/Cameri/nostream/pull/524) corrige un bug de matching pubkey sur whitelist/blacklist, [PR #553](https://github.com/Cameri/nostream/pull/553) durcit `upsertMany` en cas d'égalité de `created_at`, [PR #493](https://github.com/Cameri/nostream/pull/493) limite la confiance dans `X-Forwarded-For` aux proxies déclarés, et [PR #557](https://github.com/Cameri/nostream/pull/557) amène le relay à une parité complète avec [NIP-11](/fr/topics/nip-11/).

## Sorties

### Primal Android livre un onglet Explore, la vérification NIP-05 et un lecteur audio

[Primal Android](https://github.com/PrimalHQ/primal-android-app) a poussé 11 PRs fusionnées après la refonte du flux de la semaine dernière. [PR #1021](https://github.com/PrimalHQ/primal-android-app/pull/1021) ajoute un onglet Explore construit autour des utilisateurs populaires, des follow packs et de flux curés, [PR #1015](https://github.com/PrimalHQ/primal-android-app/pull/1015) ajoute un éditeur de flux alimenté par le DSL Advanced Search de Primal, [PR #994](https://github.com/PrimalHQ/primal-android-app/pull/994) ajoute l'UI de vérification [NIP-05](https://github.com/nostr-protocol/nips/blob/master/05.md), et [PR #997](https://github.com/PrimalHQ/primal-android-app/pull/997) embarque un lecteur audio in-feed. [PR #1018](https://github.com/PrimalHQ/primal-android-app/pull/1018) ajoute aussi le pairing `nostr-connect` [NIP-46](/fr/topics/nip-46/) depuis le scanner QR du wallet.

### strfry ajoute des métriques Prometheus sur le chemin d'écriture et corrige l'enveloppe AUTH NIP-42

[strfry](https://github.com/hoytech/strfry) a livré une série d'améliorations destinées aux opérateurs. [PR #194](https://github.com/hoytech/strfry/pull/194) ajoute un exporter dédié de métriques Prometheus sur le chemin d'écriture et [PR #197](https://github.com/hoytech/strfry/pull/197) journalise les bytes échangés par connexion ainsi que les ratios de compression. [PR #192](https://github.com/hoytech/strfry/pull/192) rend configurable à l'exécution la limite de tags de filtre. [PR #201](https://github.com/hoytech/strfry/pull/201) corrige enfin les réponses d'échec AUTH [NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) pour utiliser l'enveloppe `OK` prévue par la spécification au lieu de `NOTICE`.

### Shopstr durcit la sécurité de ses vitrines à travers 13 PRs

[Shopstr](https://github.com/shopstr-eng/shopstr) a fusionné 13 PRs dominées par des correctifs de sécurité. [PR #434](https://github.com/shopstr-eng/shopstr/pull/434) ferme un trou de JavaScript stocké dans les liens de vitrines, [PR #417](https://github.com/shopstr-eng/shopstr/pull/417) échappe le rendu HTML des policies de boutique, [PR #418](https://github.com/shopstr-eng/shopstr/pull/418) corrige une API de suppression d'événements en cache accessible sans auth, [PR #433](https://github.com/shopstr-eng/shopstr/pull/433) exige une authentification pour lire les messages en cache, et plusieurs autres PRs corrigent SSRF, revalidation de remises et robustesse de file de publication.

### Nostria v3.1.26 à v3.1.28 ajoutent la lecture de musique en arrière-plan sur Android

[Nostria](https://github.com/nostria-app/nostria) a livré six versions cette semaine, de [v3.1.22](https://github.com/nostria-app/nostria/releases/tag/v3.1.22) à [v3.1.28](https://github.com/nostria-app/nostria/releases/tag/v3.1.28). La nouveauté principale de [v3.1.26](https://github.com/nostria-app/nostria/releases/tag/v3.1.26) est la lecture musicale en arrière-plan sur Android avec contrôles média dans la barre de notifications et sur l'écran verrouillé. [v3.1.27](https://github.com/nostria-app/nostria/releases/tag/v3.1.27) et [v3.1.28](https://github.com/nostria-app/nostria/releases/tag/v3.1.28) durcissent cette nouvelle surface de service média.

### Wisp v0.18.0-beta ajoute le mode Normie, le flux For You et la configuration de groupe NIP-29

[Wisp](https://github.com/barrydeen/wisp) a livré [v0.18.0-beta](https://github.com/barrydeen/wisp/releases/tag/v0.18.0-beta) le 16 avril. [PR #462](https://github.com/barrydeen/wisp/pull/462) ajoute un mode Normie qui affiche les montants en fiat dans toute l'application, [PR #464](https://github.com/barrydeen/wisp/pull/464) revoit l'onboarding, [PR #469](https://github.com/barrydeen/wisp/pull/469) ajoute un flux For You, [PR #471](https://github.com/barrydeen/wisp/pull/471) ajoute la configuration de groupes [NIP-29](/fr/topics/nip-29/) et [PR #478](https://github.com/barrydeen/wisp/pull/478) corrige la séquence AUTH [NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) avant les événements de groupe.

### NoorNote v0.8.4 ajoute les posts programmés et les zaps sur live stream

[NoorNote](https://github.com/77elements/noornote) a livré [v0.8.4](https://github.com/77elements/noornote/releases/tag/v0.8.4) et [v0.8.5](https://github.com/77elements/noornote/releases/tag/v0.8.5). La nouveauté principale est un add-on de posts programmés : l'application remet un événement déjà signé à un relay opéré par NoorNote, qui le publie à l'heure prévue sans que la clé privée quitte l'appareil. La même release ajoute les zaps en un geste depuis les cartes de live streams [NIP-53](/fr/topics/nip-53/).

### topaz v0.0.2 livre un relay Nostr pour Android

[topaz](https://github.com/fiatjaf/topaz), nouveau relay Nostr de [fiatjaf](https://github.com/fiatjaf) qui tourne directement sur téléphone Android, a publié [v0.0.2](https://github.com/fiatjaf/topaz/releases/tag/v0.0.2) le 17 avril. Le projet est encore très étroit en surface mais livre déjà l'essentiel : un relay fonctionnel dans un package Android installable.

### StableKraft v1.0.0 livre sa première release PWA stable musique-et-podcast

[StableKraft](https://github.com/ChadFarrow/stablekraft-app) est une PWA Next.js pour découvrir, organiser et streamer de la musique récupérée depuis des flux de podcasts, avec Nostr pour l'auth et les fonctions sociales, et Lightning pour le V4V. L'application atteint [v1.0.0](https://github.com/ChadFarrow/stablekraft-app/releases/tag/v1.0.0) le 18 avril. La même semaine, l'ingestion des feeds a été durcie avec un cache OPML de 15 minutes et une suppression de XML illégal, puis la fenêtre de reparse nocturne a été réduite de 720 heures à 24 heures.

### NipLock livre un gestionnaire de mots de passe basé sur NIP-17

[NipLock](https://gitworkshop.dev/npub1z5jf78uhd68znuwwwu926th55rzd0wy8nd9clkr03cx22mwme0jqazk56h/relay.ngit.dev/passwd) est un gestionnaire de mots de passe qui stocke et synchronise les identifiants entre appareils via des messages directs gift-wrapped [NIP-17](/fr/topics/nip-17/). Chaque entrée est un DM NIP-17 envoyé de la clé de l'utilisateur à elle-même, ce qui permet la réplication vers n'importe quel appareil authentifié avec la même clé. La signature fonctionne avec un `nsec` brut, des extensions navigateur comme [nos2x](https://github.com/fiatjaf/nos2x) ou [Amber](https://github.com/greenart7c3/Amber) via [NIP-46](/fr/topics/nip-46/).

### flotilla-budabit polit sa surface de dépôt NIP-34

Le fork communautaire Budabit de [Flotilla](https://gitea.coracle.social/coracle/flotilla), [flotilla-budabit](https://github.com/Pleb5/flotilla-budabit), a livré plusieurs correctifs de son workflow git-over-nostr [NIP-34](/fr/topics/nip-34/). Les changements restaurent les contrôles de discussion de dépôt, gardent les onglets épinglés visibles sur les pages de détail, chargent les annonces de dépôts depuis les relays GRASP enregistrés et maintiennent le statut des patchs appliqués par les mainteneurs synchronisé.

### rx-nostr 3.7.2 à 3.7.4 ajoutent un vérificateur par défaut et des arguments constructeur optionnels

[rx-nostr](https://github.com/penpenpng/rx-nostr) a livré [3.7.2](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.2), [3.7.3](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.3) et [3.7.4](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.4). [PR #192](https://github.com/penpenpng/rx-nostr/pull/192) ajoute un vérificateur Schnorr par défaut, et [PR #195](https://github.com/penpenpng/rx-nostr/pull/195) rend optionnels les arguments de `createRxNostr()` pour des intégrations plus rapides.

### Keep Android v1.0.0 livre des builds reproductibles et zéro tracker

[Keep](https://github.com/privkeyio/keep-android), gestionnaire natif Nostr de mots de passe et de secrets, a livré [v1.0.0](https://github.com/privkeyio/keep-android/releases/tag/v1.0.0) le 21 avril. [PR #241](https://github.com/privkeyio/keep-android/pull/241) ajoute une recette de build reproductible, [PR #248](https://github.com/privkeyio/keep-android/pull/248) remplace Google ML Kit par ZXing, [PR #252](https://github.com/privkeyio/keep-android/pull/252) publie un scan Exodus Privacy montrant zéro tracker, et [PR #256](https://github.com/privkeyio/keep-android/pull/256) ajoute un manifeste `zapstore.yaml`.

### Flotilla 1.7.3 et 1.7.4 ajoutent l'enveloppement kind-9 pour des salons NIP-29 plus riches

[Flotilla](https://gitea.coracle.social/coracle/flotilla), client de groupes [NIP-29](/fr/topics/nip-29/) de hodlbod, a livré [1.7.3](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.3) et [1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4). Le changement protocolaire principal est l'enveloppement kind `9` de contenus non orientés chat, annoncé dans [la note de release de hodlbod](nostr:nevent1qvzqqqqqqypzp978pfzrv6n9xhq5tvenl9e74pklmskh4xw6vxxyp3j8qkke3cezqyvhwumn8ghj76rzwghxxmmjv93kcefwwdhkx6tpdshszrnhwden5te0dehhxtnvdakz7qgawaehxw309a5x7ervvfhkgtnrdaexzcmvv5h8xmmrd9skctcqyrrclae7mhmm5dnumwfzhg3fxu74a4hh24jd8pvn8v0hye9w3g6tuljtr85) et aligné avec [PR #2310](https://github.com/nostr-protocol/nips/pull/2310). Le même cycle ajoute aussi sondages, connexion [NIP-46](/fr/topics/nip-46/) via Aegis, partages natifs, mentions de salon, brouillons et vidéo dans les appels.

### WoT Relay v0.2.1 migre son eventstore vers LMDB

[WoT Relay](https://github.com/bitvora/wot-relay) a livré [v0.2.1](https://github.com/bitvora/wot-relay/releases/tag/v0.2.1) le 22 avril. [PR #97](https://github.com/bitvora/wot-relay/pull/97) migre l'eventstore vers LMDB et retune les fetches bootstrap du web of trust, [PR #99](https://github.com/bitvora/wot-relay/pull/99) met à jour `golang.org/x/crypto`, et [PR #100](https://github.com/bitvora/wot-relay/pull/100) ajuste l'URL logicielle et la version annoncées via [NIP-11](/fr/topics/nip-11/).

### Suite Formstr : passe sécurité Pollerama, i18n de Forms, support RRULE de Calendar

La suite Formstr a fusionné 26 PRs réparties entre Pollerama, Formstr Forms et Nostr Calendar. [Pollerama](https://pollerama.fun) durcit la gestion des clés, expire les DMs en cache à la déconnexion, déplace la clé locale dans un stockage navigateur sécurisé et protège le parsing JSON des profils kind `0`. [Formstr](https://formstr.app) ajoute le support des URLs audio et vidéo, introduit l'i18n web et livre un importeur Google Forms. [Nostr Calendar by Formstr](https://calendar.formstr.app) a livré [v1.3.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.3.0) et [v1.4.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.4.0) avec le support de RRULE multiples et personnalisés, l'interprétation UTC des dates flottantes et plusieurs améliorations de partage et de notifications sur [NIP-52](/fr/topics/nip-52/).

### Aussi livré : notedeck, nostr.blue, cliprelay, Captain's Log

Quelques clients ont livré des releases incrémentales sans fonctionnalité phare unique. [notedeck](https://github.com/damus-io/notedeck) a publié [v0.10.0-beta.4](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.4) avec des correctifs de rendu en colonnes et de pool de relays. [nostr.blue v0.8.6](https://github.com/patrickulrich/nostr.blue/releases/tag/v0.8.6) met à jour Dioxus et débloque Android. [cliprelay](https://github.com/tajava2006/cliprelay) a livré des builds desktop et Android pour le partage de presse-papiers entre appareils via Nostr, et [Captain's Log](https://github.com/nodetec/comet) ajoute notamment la détection de liveness des relays de sync.

## En développement

### whitenoise-rs se refactorise autour de vues de compte à portée de session

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs) a fusionné 15 PRs faisant progresser un refactor multi-phase depuis des singletons globaux vers des vues `AccountSession` par compte. Le but est de casser un monolithe partagé en surfaces par compte plus simples à raisonner, tester et faire évoluer. Les phases récentes ont migré handles relay, brouillons et paramètres, opérations de messages, lecture et écriture de groupes, appartenance, notifications push, lectures de KeyPackage, création de groupes et, depuis [PR #770](https://github.com/marmot-protocol/whitenoise-rs/pull/770), le dispatch d'événements côté session.

### White Noise ajoute l'UI de blocage/déblocage, le départ de groupe et les notices hors ligne

[White Noise](https://github.com/marmot-protocol/whitenoise) a ajouté les contrôles manquants de cycle de vie des groupes. [PR #578](https://github.com/marmot-protocol/whitenoise/pull/578) ajoute l'UI de block/unblock au-dessus du hook livré dans [PR #573](https://github.com/marmot-protocol/whitenoise/pull/573), [PR #571](https://github.com/marmot-protocol/whitenoise/pull/571) et [PR #572](https://github.com/marmot-protocol/whitenoise/pull/572) branchent `clear_chat`, `delete_chat` et `leave_and_delete_group` côté Rust, [PR #569](https://github.com/marmot-protocol/whitenoise/pull/569) et [PR #576](https://github.com/marmot-protocol/whitenoise/pull/576) ajoutent des notices hors ligne, et [PR #585](https://github.com/marmot-protocol/whitenoise/pull/585) restreint la suppression aux anciens KeyPackages hérités.

### MDK ajoute le support des invitations entre versions mixtes et la convergence du format wire SelfUpdate

[MDK](https://github.com/marmot-protocol/mdk) a fusionné sept PRs autour de la compatibilité. [PR #261](https://github.com/marmot-protocol/mdk/pull/261) calcule `RequiredCapabilities` comme le LCD des capacités des invités, débloquant les invitations entre Amethyst et White Noise. [PR #264](https://github.com/marmot-protocol/mdk/pull/264) fait converger le format wire de SelfUpdate, tandis que [PR #262](https://github.com/marmot-protocol/mdk/pull/262), [PR #256](https://github.com/marmot-protocol/mdk/pull/256), [PR #259](https://github.com/marmot-protocol/mdk/pull/259) et [PR #265](https://github.com/marmot-protocol/mdk/pull/265) durcissent le parsing, la validation et l'exposition d'état.

### nostter ajoute le chiffrement NIP-44 aux listes de personnes, bookmarks et mutes

[nostter](https://github.com/SnowCait/nostter) a fusionné 10 PRs. [PR #2088](https://github.com/SnowCait/nostter/pull/2088), [PR #2089](https://github.com/SnowCait/nostter/pull/2089) et [PR #2090](https://github.com/SnowCait/nostter/pull/2090) migrent respectivement mutes, bookmarks et listes de personnes vers le chiffrement [NIP-44](/fr/topics/nip-44/), en s'éloignant de [NIP-04](/fr/topics/nip-04/). [PR #2087](https://github.com/SnowCait/nostter/pull/2087) supprime un ancien chemin de migration kind-30000 devenu inutile.

### zap.cooking livre le scoring Nourish et un fil de commentaires réutilisable

[zap.cooking](https://github.com/zapcooking/frontend) a fusionné 20 PRs. Les plus visibles ajoutent le module de scoring de recettes Nourish, refactorisent le module de commentaires vers un `CommentThread` réutilisable, et améliorent l'upload média, l'onglet Replies du profil et la mise à l'échelle des recettes.

### ridestr extrait un coordinateur partagé pour les riders

[ridestr](https://github.com/variablefate/ridestr) a fusionné 10 PRs, refactorisant ses écrans Compose et extrayant la logique protocolaire riders/drivers dans un module partagé `:common` ([PR #70](https://github.com/variablefate/ridestr/pull/70)). [PR #60](https://github.com/variablefate/ridestr/pull/60) ajoute aussi un récepteur de ping de conducteur kind `3189` pour le versant Roadflare de l'application.

### Blossom ébauche un header BUD-01 Sunset pour l'expiration des blobs

[Blossom](https://github.com/hzrd149/blossom) a ouvert [PR #99](https://github.com/hzrd149/blossom/pull/99) pour ajouter un header `Sunset` à BUD-01. L'idée est qu'un serveur puisse annoncer à l'avance le moment où il cessera de servir un blob, en s'appuyant sur la sémantique standard [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html).

## Nouveaux projets

### Forgesworn publie une boîte à outils cryptographique de 29 dépôts pour Nostr

[Forgesworn](https://github.com/forgesworn) a publié 29 dépôts open source en cinq jours couvrant la signature, l'identité, les attestations, le web of trust et la découverte d'API payantes sur Nostr. La pile de signature s'ancre sur [nsec-tree](https://github.com/forgesworn/nsec-tree), [Heartwood](https://github.com/forgesworn/heartwood), [Sapwood](https://github.com/forgesworn/sapwood) et [heartwood-esp32](https://github.com/forgesworn/heartwood-esp32). Côté identité, [Signet](https://github.com/forgesworn/signet) atteint [v1.6.0](https://github.com/forgesworn/signet/releases/tag/v1.6.0), [nostr-attestations](https://github.com/forgesworn/nostr-attestations) définit un kind `31000` pour les credentials et endorsements, et [nostr-veil](https://github.com/forgesworn/nostr-veil) construit un web of trust privé avec signatures de groupe LSAG.

La partie monétisation couvre aussi les API payantes sur Lightning et Nostr avec [toll-booth](https://github.com/forgesworn/toll-booth), [toll-booth-dvm](https://github.com/forgesworn/toll-booth-dvm), [toll-booth-announce](https://github.com/forgesworn/toll-booth-announce), [402-announce](https://github.com/forgesworn/402-announce) et [402-indexer](https://github.com/forgesworn/402-indexer). L'ensemble est écrit en TypeScript et publié via [anvil](https://github.com/forgesworn/anvil), un outil bash-only de supply chain durcie.

### ShockWallet livre une synchronisation Lightning native à Nostr et des connexions multi-node

[ShockWallet](https://github.com/shocknet/wallet2) est un wallet Lightning qui utilise Nostr comme transport pour se connecter à des nœuds Lightning auto-custodial. L'application se paire avec un ou plusieurs nœuds [Lightning.Pub](https://github.com/shocknet/Lightning.Pub) via un `nprofile`, puis signe de bout en bout les autorisations de paiement entre le wallet et le nœud. [PR #608](https://github.com/shocknet/wallet2/pull/608) ajoute une nouvelle vue dashboard pour les canaux, accompagnée de [PR #606](https://github.com/shocknet/wallet2/pull/606) et [PR #607](https://github.com/shocknet/wallet2/pull/607).

ShockWallet utilise des événements de données spécifiques à l'application [NIP-78](/fr/topics/nip-01/) pour synchroniser l'état du wallet entre appareils, ce qui le place une couche en dessous de [NIP-47](/fr/topics/nip-47/). En parallèle, l'équipe pousse aussi [CLINK](https://github.com/shocknet/CLINK), un protocole de pairage de sessions basé sur Nostr.

### Les issues Nostrability migrent vers git over Nostr après la censure GitHub

[Nostrability](https://gitworkshop.dev/elsat@habla.news/nostrability/issues), le tracker d'interop d'elsat pour les clients et relays Nostr, déplace son workflow d'issues vers git over Nostr après la fermeture de l'organisation Nostrability sur GitHub et deux semaines sans réponse du support GitHub. Le tracker vit désormais sur GitWorkshop/ngit.

### nowhere encode des sites web complets dans des fragments d'URL et route les commandes via Nostr

[nowhere](https://github.com/5t34k/nowhere) est un nouveau projet AGPL-3.0 de [5t34k](https://github.com/5t34k) qui sérialise un site entier dans le fragment d'URL après `#`, le compresse puis l'encode en base64url. Comme les fragments ne sont pas envoyés au serveur, l'hôte qui livre la page ne voit jamais le contenu, et le site lui-même n'est jamais stocké sur un serveur. Les types nécessitant de la communication live utilisent des clés éphémères avec chiffrement [NIP-44](/fr/topics/nip-44/) sur des relays Nostr.

### Petites nouvelles surfaces : relayk.it et Brainstorm Search

Deux petits projets méritent une mention rapide. [relayk.it](https://relayk.it), construit par [sam](https://nostr.com/sam@relayk.it) de l'équipe Soapbox, est un client de découverte de relays généré avec Shakespeare et entièrement exécuté dans le navigateur. [Brainstorm Search](https://brainstorm.world) se lance comme interface de recherche Nostr en page unique.

## Travail sur le protocole et les spécifications

### Mises à jour des NIP

Propositions et discussions récentes dans le [dépôt NIPs](https://github.com/nostr-protocol/nips) :

**PRs ouvertes et discussions :**

- **[NIP-67](/fr/topics/nip-67/) : EOSE Completeness Hint** ([PR #2317](https://github.com/nostr-protocol/nips/pull/2317)) : ajoute un troisième élément optionnel à `EOSE` pour permettre à un relay d'indiquer qu'il a réellement livré tous les événements stockés correspondant au filtre.
- **NIP-5D : Nostr Applets** ([PR #2303](https://github.com/nostr-protocol/nips/pull/2303)) : propose un nouveau kind pour distribuer des applets interactives sur Nostr, à mi-chemin entre [NIP-5A](/fr/topics/nip-5a/) et [NIP-5C](/fr/topics/nip-5c/).
- **NIP-29 : spécification des sous-groupes** ([PR #2319](https://github.com/nostr-protocol/nips/pull/2319)) : étend [NIP-29](/fr/topics/nip-29/) avec une hiérarchie de sous-groupes.
- **NIP-29 : permissions explicites sur le kind 39003** ([PR #2316](https://github.com/nostr-protocol/nips/pull/2316)) : définit un schéma explicite de permissions par rôle.
- **NIP-11 : champ `access_control` pour la découverte de relays fermés** ([PR #2318](https://github.com/nostr-protocol/nips/pull/2318)) : permet d'annoncer le mode d'accès du relay et l'endpoint où demander l'autorisation.
- **NIP-63a : Minimal Payment Gateway Descriptor** ([PR #2315](https://github.com/nostr-protocol/nips/pull/2315)) : poursuit son itération sur le shape kind `10164`.
- **NIP-XX : Agent Reputation Attestations (kind 30085)** ([PR #2320](https://github.com/nostr-protocol/nips/pull/2320)) : propose des attestations signées sur des agents et services autonomes sur Nostr, en particulier dans le contexte [NIP-90](/fr/topics/nip-90/).
- **NIP-TPLD : Transient Private Location Data** ([PR #2309](https://github.com/nostr-protocol/nips/pull/2309)) : poursuit l'itération sur le kind `20411`, le chiffrement [NIP-44](/fr/topics/nip-44/) par destinataire et la sémantique du tag `ttl`.
- **PR de release marmot-ts 0.5.0** ([PR #70](https://github.com/marmot-protocol/marmot-ts/pull/70)) : regroupe les premiers changements cassants du client Marmot TypeScript, notamment le support conjoint des KeyPackages kinds `443` et `30443`.

## Deep Dive NIP : NIP-72 (communautés modérées)

[NIP-72](https://github.com/nostr-protocol/nips/blob/master/72.md) définit un modèle de communautés thématiques dans lequel les modérateurs curent une vue de lecture au-dessus d'écritures autrement ouvertes. Une communauté est définie par un événement adressable kind `34550` contenant un slug `d`, des tags `name`, `description`, `image`, `rules`, des tags `p` marqués `moderator` et, éventuellement, des tags `relay` annotés `author`, `requests` ou `approvals`.

Les utilisateurs soumettent des posts en publiant un événement Nostr ordinaire et en ajoutant un tag `a` pointant vers la coordonnée `34550:<creator_pubkey>:<slug>`. L'approbation est un événement séparé kind `4549` publié par un modérateur, qui référence la soumission par tag `e`, l'auteur par tag `p`, la communauté par tag `a`, et embarque une copie stringifiée de la soumission dans `content`. Ce modèle rend la modération transparente, forkable et révocable côté lecture, tout en gardant la publication ouverte à n'importe quel relay qui transporte les kinds nécessaires.

## Deep Dive NIP : NIP-57 (Zaps)

[NIP-57](https://github.com/nostr-protocol/nips/blob/master/57.md) définit les zaps, c'est-à-dire l'association d'un paiement Lightning à une identité ou à un contenu Nostr avec publication d'un reçu vérifiable sur les relays. Le flux implique un client expéditeur, un endpoint LNURL destinataire, le paiement Lightning lui-même et un reçu kind `9735` publié après paiement. La demande signée kind `9734` déclare le `p` tag du destinataire, un éventuel `e` ou `a` tag pour la cible, un tag `amount`, une liste `relays` et éventuellement un tag `k`.

Le point décisif est la validation. Un client sérieux doit vérifier que la signature du reçu correspond au `nostrPubkey` annoncé dans la réponse LNURL, que le montant de la facture `bolt11` correspond au `amount` de la demande embarquée, que le hash de description de la facture s'engage sur cette demande et que le `preimage` correspond au `payment_hash` de la facture. Les zaps privés et anonymes ajoutent ensuite une couche de confidentialité, et [NIP-75](/fr/topics/nip-75/) réutilise ces reçus pour totaliser les objectifs de financement.

---

C'est tout pour cette semaine. Si vous construisez quelque chose ou avez des nouvelles à partager, envoyez-nous un DM sur Nostr ou retrouvez-nous sur [nostrcompass.org](https://nostrcompass.org).
