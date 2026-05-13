---
title: 'Nostr Compass #22'
date: 2026-05-13
publishDate: 2026-05-13
draft: false
type: newsletters
translationOf: /en/newsletters/2026-05-13-newsletter.md
translationDate: 2026-05-13
---

Bienvenue dans Nostr Compass, votre guide hebdomadaire du développement du protocole Nostr.

**Cette semaine :** Nostr VPN livre huit versions en sept jours, d'un flux de jumelage d'appareils repensé à un échange AEAD FIPS qui double environ le débit TCP. Marmot Protocol (la fondation de White Noise) livre une version frontend complétant la fonctionnalité de blocage des utilisateurs et 31 PR fusionnées dans MDK et le backend. Grain livre v0.6.0 avec quatre nouvelles implémentations NIP en un seul jalon. Citrine livre v3.0.0-pre1 avec Tor intégré et agrégation de relais. Amber livre v6.1.0-pre2 avec des améliorations du flux de connexion et de la signature. Alby Hub livre v1.22.2 avec une page IA et Agents et l'intégration Core Lightning. Mostro livre des cautions de preneur concurrentes et mostro-core v0.11.0. Jumble livre cinq versions avec l'historique de recherche récent et des corrections de persistance des données de compte. Nostrord livre trois versions avec des modales de partage de groupe et des paquets Arch Linux. Flotilla livre 1.8.0 avec des appels vidéo, le rendu d'e-mails et les mentions de salles. Calendar by Formstr livre v1.5.1 avec la planification de rendez-vous et la synchronisation du calendrier Android. Tamagostrich lance un Tamagotchi NIP-78 décentralisé avec des récompenses en sats.

## Actualités principales

### Nostr VPN livre huit versions culminant en v4.0.10

Nostr VPN, le VPN mesh décentralisé basé sur Rust utilisant Nostr pour la découverte de pairs, a livré huit versions de v4.0.1 à v4.0.10 sur macOS, Linux, Windows et Android. Le changement phare dans v4.0.8 : l'AEAD est passé du backend logiciel RustCrypto chacha20poly1305 au ChaCha20-Poly1305 de BoringSSL dans ring 0.17, qui utilise NEON optimisé à la main sur aarch64 et AVX2/AVX-512 sur x86_64. Les benchmarks Docker sur matériel identique ont montré le débit TCP direct à 2 nœuds passer de 437 à 1097 Mbps. v4.0.9 a ajouté le batching sendmmsg(2) sur le chemin d'envoi UDP, poussant le TCP single-stream de 1066 à 1548 Mbps (1,45×). v4.0.10 a livré une refonte complète de l'interface utilisateur pour le jumelage d'appareils.

### Marmot / White Noise livre une version frontend complétant le blocage d'utilisateurs et 31 PR fusionnées dans MDK et le backend

White Noise a livré v2026.5.7+24 le 7 mai complétant l'ensemble de fonctionnalités de blocage. Un utilisateur bloqué est désormais masqué des invitations, des aperçus de chat, des fils de messages, des résultats de recherche et des notifications, et ses messages ne comptent plus dans les badges non lus. MDK a intégré la PR #258 avec le format wire de l'extension v3 et le schéma disappearing_message_secs, posant les bases des messages éphémères.

### Grain v0.6.0 ajoute NIP-40, NIP-50, NIP-70 et NIP-45

Grain a livré v0.6.0 le 6 mai avec quatre nouvelles implémentations NIP. L'expiration d'événements NIP-40 permet aux éditeurs de définir un horodatage d'expiration pour que le relais supprime les événements après leur expiration. La recherche plein texte NIP-50 permet aux clients d'émettre des filtres de recherche dans les messages REQ. Les événements protégés NIP-70 empêchent les relais de repartager des événements sans la permission explicite de l'auteur. Les requêtes de comptage NIP-45 permettent aux clients de demander à un relais de renvoyer un décompte des événements correspondants.

## Publications de la semaine

### Citrine v3.0.0-pre1 intègre Tor et l'agrégation de relais

Citrine a livré v3.0.0-pre1 avec le support Tor intégré pour un accès aux relais préservant la confidentialité et l'agrégation de relais, où Citrine peut récupérer des événements depuis plusieurs relais amont et les servir aux clients locaux. La PR #139 ajoute le support NIP-77 (Negentropy Reconciliation) pour la synchronisation d'événements efficace basée sur la réconciliation d'ensembles.

### Amber v6.1.0-pre2 améliore le flux de connexion des nouvelles applications

Amber a livré v6.1.0-pre2. Les principaux correctifs : la boîte de dialogue de signature se ferme maintenant correctement après avoir accepté une demande bunker, les demandes bunker malformées affichent un écran de demande invalide, et une limitation de débit est ajoutée pour les demandes de signature basées sur les intentions.

### Alby Hub v1.22.2 ajoute la page IA et Agents et le support Core Lightning

Alby Hub a livré v1.22.2. La nouvelle page IA et Agents expose les capacités Lightning et NWC d'Alby Hub aux agents IA et aux outils compatibles MCP. Core Lightning (CLN) est désormais un backend pris en charge aux côtés de LND et LDK.

### Mostro livre des cautions de preneur concurrentes et mostro-core v0.11.0

Mostro a fusionné 11 PR faisant avancer la fonctionnalité de caution de preneur. La PR #733 implémente des cautions de preneur concurrentes où plusieurs preneurs peuvent soumettre des factures de caution simultanément et le premier à verrouiller gagne. mostro-core a livré v0.11.0 avec la PR #144 ajoutant Action::PayBondInvoice et Status::WaitingTakerBond. mostro-cli a livré v0.15.0.

### Jumble livre cinq versions avec la recherche récente et la persistance des comptes

Jumble a livré v26.5.2 à v26.5.6. v26.5.5 ajoute l'historique de recherche récent. Un bug de persistance critique est corrigé dans v26.5.6 : les comptes et les données en cache survivent désormais à un redémarrage complet de l'application.

### Nostrord livre des modales de partage de groupe, le téléversement de médias et des paquets Arch Linux

Nostrord a livré v1.0.0, v1.0.1 et v1.0.2. v1.0.1 livre des paquets Arch Linux via AUR sous le nom nostrord-bin avec des artefacts signés PGP, un bouton de saut au dernier message, et le collage d'images/médias dans le chat. v1.0.2 ajoute le partage de groupe via la PR #49 avec une modale de partage générant à la fois un URI nostr:naddr et un lien nostrord.com/open/.

### FIPS v0.3.0 livre une portée multiplateforme, la découverte de pairs Nostr et une passerelle pour les LAN non modifiés

FIPS a livré v0.3.0, un jalon majeur passant de Linux uniquement à Linux, macOS, Windows et OpenWrt. Les nœuds publient désormais des annonces d'overlay signées en tant qu'événements remplaçables paramétrés kind:37195 sur des relais Nostr publics. Le même échange ring 0.17 ChaCha20-Poly1305 qui a alimenté le gain de débit de Nostr VPN arrive également dans FIPS v0.3.0.

### Camelus v1.10.1 livre des versions bureau

Camelus a livré v1.10.1 avec des versions bureau Windows et Linux, élargissant sa distribution au-delà du mobile uniquement.

### Flotilla 1.8.0 livre des appels vidéo, le rendu d'e-mails et les mentions de salles

Flotilla a livré 1.8.0. Les salles vocales prennent désormais en charge la vidéo : les participants peuvent activer leurs caméras ou partager leur écran en cours d'appel. Le rendu d'e-mails arrive via une mise à jour de la bibliothèque welshman. Les mentions de salles permettent aux utilisateurs de référencer d'autres salles et relais avec des liens inline cliquables.

### Calendar by Formstr livre v1.5.1 avec la planification de rendez-vous et la synchronisation du calendrier Android

Calendar by Formstr a livré v1.5.0 le 10 mai et v1.5.1 le 11 mai. La planification de rendez-vous permet aux utilisateurs de créer des créneaux réservables. L'intégration du calendrier Android en lecture seule synchronise les événements Nostr avec le calendrier de l'appareil.

## En développement

### Amethyst ajoute les publications programmées, les règles de communauté NIP-9A et un relay local bureau

Amethyst a fusionné 78 PR cette semaine. Les publications programmées arrivent dans la PR #2765. Une version bureau gagne un relay local intégré avec persistance des événements SQLite dans la PR #2841. Trois PR implémentent les règles de communauté NIP-9A : la PR #2798 valide les publications par rapport aux règles de communauté avant l'envoi, la PR #2799 ajoute un éditeur de règles NIP-9A structuré, et la PR #2800 ajoute un filtre de fil NIP-9A optionnel.

### Shopstr ajoute la journalisation d'audit MCP et la sécurité des sessions

Shopstr a fusionné cinq PR. La journalisation d'audit pour la couche d'outils MCP arrive dans la PR #456. La sécurité des sessions se renforce dans la PR #477 avec l'épinglage de session à la clé API d'origine et l'éviction TTL.

### Dart NDK ajoute le support web et la vérification des signatures de sceau

Dart NDK a fusionné six PR. Le support web arrive dans SembastCacheManager via la PR #571. La vérification des signatures de sceau arrive dans la PR #595 pour le flux NIP-59 Gift Wrap.

## Nouveaux projets

### Tamagostrich lance un Tamagotchi NIP-78 décentralisé avec des récompenses en sats

Tamagostrich est un jeu d'animal de compagnie virtuel basé sur le navigateur lancé à l'IDENTITY Hackathon 2026 où un bébé autruche, Nori, évolue grâce à votre activité sociale Nostr. L'état de l'animal vit dans un événement NIP-78 kind:30078 pour la synchronisation multi-appareils. Les récompenses de jalons sont versées en sats via NIP-47 : 50 sats au niveau 5, 210 sats au niveau 10, et 420 sats au niveau maximum 21, envoyés à l'adresse lud16 de l'utilisateur.

## Travaux sur le protocole et les spécifications

Cinq nouvelles propositions ont été ouvertes cette semaine :

La PR #2331 propose NIP-9A : Verifiable Community Rules, introduisant kind:34551 pour des documents de règles de communauté cryptographiquement signés et lisibles par machine.

La PR #2335 propose des Reservation Events pour les marchés Nostr, définissant kind:32122 (événements de réservation remplaçables paramétrés), kind:1326 (enregistrements d'audit de transition en ajout uniquement), et kind:32124 (avis post-transaction). La négociation est privée via des messages enveloppés NIP-59 Gift Wrap.

La PR #2334 propose des Escrow Services pour les marchés Nostr utilisant kind:30303 pour que les opérateurs d'entiercement déclarent leur adresse de contrat EVM et leur grille tarifaire.

La PR #2333 propose des Accommodation Listing Profiles pour NIP-99 Marketplace Listings, étendant NIP-99 avec des balises g d'index géospatial H3 pour les annonces de location courte durée.

La PR #2332 propose NIP-BC : Onchain Zaps (kind 8333), exploitant l'identité directe entre les clés Nostr et les adresses Bitcoin Taproot. Le numéro de kind reflète NIP-57 : 9735 est le port P2P Lightning ; 8333 est le port P2P du mainnet Bitcoin.

## NIP Deep Dive : NIP-78 (données spécifiques aux applications)

NIP-78 définit une façon standard pour les applications de stocker des données privées ou publiques arbitraires pour le compte d'un utilisateur en utilisant des événements Nostr. Le type d'événement principal est 30078, un événement remplaçable paramétré où le tag d est une chaîne d'identifiant définie par l'application. Une application donne à son emplacement de stockage un tag d unique et publie un événement 30078 avec le contenu JSON ou texte qu'elle doit persister. La motivation principale est la synchronisation multi-appareils sans serveur centralisé. Pour les données d'application privées, les événements NIP-78 peuvent chiffrer le champ de contenu en utilisant NIP-44 avant la publication. Les utilisateurs actuels incluent Tamagostrich (synchronisation de l'état de l'animal), Wisp (sauvegarde du portefeuille et paramètres de sécurité), NosPress (état d'orchestration CMS), et plusieurs implémentations de synchronisation des paramètres de clients Nostr.

---

Sources principales :
- Spécification NIP-78 : https://github.com/nostr-protocol/nips/blob/master/78.md
- Tamagostrich : https://github.com/Negr087/tamagostrich

Voir aussi : NIP-51 Lists, NIP-65 Relay List Metadata

## NIP Deep Dive : NIP-98 (HTTP Auth)

NIP-98 définit un schéma d'authentification HTTP permettant aux paires de clés Nostr d'autoriser les requêtes aux serveurs HTTP, éliminant les noms d'utilisateur, les mots de passe ou les tokens OAuth. Un client construit un événement Nostr de courte durée de type 27235, le signe avec sa clé privée, encode le JSON en base64, et l'envoie dans un en-tête HTTP Authorization: Nostr <base64>. L'événement de type 27235 inclut la méthode HTTP dans un tag method, l'URL complète de la requête dans un tag u, et un horodatage created_at. Le serveur valide la signature, vérifie que la méthode et l'URL correspondent, et contrôle que l'horodatage est récent pour prévenir les attaques par rejeu. NIP-98 est utilisé dans Blossom (BUD-01) pour l'authentification des téléversements de blobs, Routstr pour le contrôle d'accès API par requête, Sprout pour l'authentification du transport git, et Alby Hub pour l'authentification de l'API d'administration.

---

Sources principales :
- Spécification NIP-98 : https://github.com/nostr-protocol/nips/blob/master/98.md
- BUD-01 : https://github.com/hzrd149/blossom/blob/master/buds/01.md

Voir aussi : NIP-96 HTTP File Storage Integration

---

C'est tout pour cette semaine. Si vous construisez quelque chose ou avez des nouvelles à partager, envoyez-nous un DM sur Nostr ou retrouvez-nous sur nostrcompass.org.
