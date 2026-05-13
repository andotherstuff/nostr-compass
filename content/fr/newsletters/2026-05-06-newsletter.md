---
title: 'Nostr Compass #21'
date: 2026-05-06
publishDate: 2026-05-06
draft: false
type: newsletters
translationOf: /en/newsletters/2026-05-06-newsletter.md
translationDate: 2026-05-13
---

Bienvenue dans Nostr Compass, votre guide hebdomadaire de Nostr.

**Cette semaine :** Marmot Protocol livre MDK 0.8.0 avec les premiers primitives de notification MIP-05, des paquets de clés NIP-51 adressables et une revue de sécurité renforcée. LaWallet NWC livre v0.10.0, la plus grande version depuis le financement OpenSats, apportant un tableau de bord administrateur complet, un portefeuille utilisateur, un journal d'activité de bout en bout, et le nouveau schéma LightningAddress 1→N et NWCConnection. Amethyst effectue un sprint de stabilisation de Nests avec élimination des coupures audio lors du renouvellement JWT, des abonnements aux données de clés tenant compte du cycle de vie, une reconnexion relay keep-alive, et un indicateur animé du participant en train de parler. ngit livre v2.4.2 et v2.4.3 corrigeant la détection des serveurs GRASP pour les soumissions de PR et le filtrage des événements d'état multi-remote. GRAIN livre v0.5.4 avec un durcissement de production et une correction silencieuse de perte de données. Mostro Core livre v0.10.1 avec des artefacts de version signés PGP. Clave lance v0.2.0 avec la gestion multi-comptes sur iOS.

## Actualités principales

### MDK 0.8.0 ajoute les primitives de notification MIP-05 et les paquets de clés adressables

MDK, la bibliothèque Rust principale du protocole Marmot, a livré v0.8.0 le 4 mai. Cette version embarque les premiers blocs de construction de notification MIP-05, fait passer les paquets de clés MIP-00 en événements adressables pour qu'un paquet de clés utilisateur puisse être remplacé sur place, améliore la compatibilité des groupes à versions mixtes, élargit la couverture UniFFI pour les bindings mobiles, et resserre les chemins de validation autour des actions d'administration, des commits, du stockage, des bornes de chiffrement et de la gestion des replays. Les primitives MIP-05 incluent des helpers d'index de feuille ajoutés dans la PR #235, qui donnent aux clients aval suffisamment d'informations pour livrer des notifications push par destinataire sans révéler la structure du groupe. La PR #273 restaure la publication de crates.io de mdk-core, et la PR #269 expose le module test_util derrière une fonctionnalité Cargo test-utils pour que les suites de tests clients externes puissent partager le harnais de test de Marmot.

### LaWallet NWC v0.10.0 livre le monorepo complet et le portefeuille utilisateur

LaWallet NWC, l'implémentation NIP-47 Nostr Wallet Connect de l'équipe LaWallet, a livré v0.10.0 le 30 avril. C'est la plus grande version depuis que le projet a reçu un financement OpenSats. Elle embarque le monorepo complet, le tableau de bord administrateur intégral, un portefeuille utilisateur, un journal d'activité de bout en bout, une marque dynamique, et le nouveau schéma LightningAddress 1→N et NWCConnection. Le portefeuille utilisateur livré dans la PR #191 couvre l'intégration, l'accueil, l'envoi/réception, le scan, les devises, un fil d'activité et un cache hors ligne.

### Amethyst stabilise Nests avec keep-alive, résilience JWT et abonnements de cycle de vie

Amethyst, le client Android riche en fonctionnalités, a poursuivi les travaux sur les salles audio NIP-53 Nests avec un sprint de stabilisation axé sur les modes de défaillance qui cassaient les appels en production. Le correctif de coupure audio dans la PR #2733 chevauche l'acquisition de nouveaux identifiants avec le flux actif lors du renouvellement JWT. Un nouveau mécanisme keep-alive dans la PR #2730 reconnecte les relais déconnectés sans nécessiter d'action manuelle de l'utilisateur, et la PR #2728 remplace l'ancien KeyDataSourceSubscription par LifecycleAwareKeyDataSourceSubscription. La PR #2724 ajoute un indicateur animé en anneau externe qui met en surbrillance le participant en train de parler lors des sessions multi-intervenants.

### ngit v2.4.2 et v2.4.3 corrigent la détection des serveurs GRASP et les événements d'état multi-remote

ngit, l'outil en ligne de commande et le plugin git pour la collaboration NIP-34, a livré v2.4.2 le 28 avril et v2.4.3 le 1er mai. v2.4.2 corrige une discordance de normalisation d'URL où repo_grasps contenait des noms d'hôtes normalisés mais la comparaison était effectuée par rapport aux URL de clone complètes. v2.4.3 corrige une ambiguïté d'événement d'état qui apparaissait lorsqu'un dépôt possède plusieurs remotes nostr:// partageant le même identifiant.

### GRAIN v0.5.4 apporte un durcissement de production et corrige une perte de données silencieuse

GRAIN, le relais Nostr et la bibliothèque client basés sur Go, a livré v0.5.4 le 30 avril. La version regroupe six correctifs accumulés depuis v0.5.3, dont un bug de perte de données silencieuse dans le démarrage rapide Docker qui supprimait auparavant des événements lors du redémarrage du conteneur, et un bug de correction de la couche de stockage dans les lectures d'événements adressables.

### Mostro Core v0.10.1 ajoute des artefacts de version signés PGP

Mostro Core, la bibliothèque Rust fournissant des fonctionnalités pair à pair pour le démon Mostro, a livré v0.10.1 le 28 avril. Cette version ajoute des artefacts de version signés PGP et un flux de vérification de version pour que les empaqueteurs aval puissent confirmer la provenance des artefacts.

## Versions publiées

### Clave v0.2.0 lance la gestion multi-comptes sur iOS avec la signature NIP-46 (Nostr Connect)

Clave, l'application iOS de signature distante NIP-46, a livré v0.2.0 le 5 mai. La principale nouveauté introduit la gestion multi-comptes : Clave peut désormais gérer jusqu'à quatre comptes sur un seul appareil, avec un sélecteur en un appui et une isolation par compte. La PR #23 ajoute la plomberie iOS pour le multi-comptes, et la PR #22 ajoute un champ signer_pubkey à la charge utile APNs pour que l'appareil sache à quel compte appartient une demande de signature distante.

### Wisp livre des travaux de stabilité v1.0.3 → v1.0.5

Wisp, le client Android, a livré v1.0.3, v1.0.4 et v1.0.5 le 4 mai avec des travaux de stabilité. La PR #506 ajoute Thumbhash pour les aperçus d'images floutées pendant le chargement des médias complets, et la PR #514 réduit les saccades lors du changement d'onglets inférieurs.

### Amber 6.1.0-pre1 livre des corrections de mise en page et de stabilité

Amber, l'application de signature Android pour NIP-55 et NIP-46, a livré v6.1.0-pre1 avec une passe de mise en page sur le flux de connexion des nouvelles applications et plusieurs corrections de plantage. La PR #416 corrige la mise en page d'ActivityStatsBar et les problèmes de débordement de texte.

### Routstr Core v0.4.3 améliore le paiement, les remboursements et le reporting d'utilisation

Routstr Core a livré v0.4.3 en pré-version le 1er mai avec des améliorations du traitement des paiements et remboursements, du suivi des coûts et du reporting d'utilisation.

### Nostria v3.1.37 à v3.1.41 ajoutent les signets Web et un thème automatique

Nostria, le client Nostr multi-plateforme, a livré v3.1.37 à v3.1.41 avec la prise en charge des signets Web NIP-B0, un thème automatique suivant les paramètres de l'appareil, et la consultation de PDF dans l'application.

### NoorNote v0.8.9 corrige l'écran vide au premier lancement sur bureau

NoorNote a livré v0.8.9 le 28 avril corrigeant un bug d'écran vide au premier lancement de l'application de bureau.

### Kubo v0.3.4 à v0.4.1 lancent une plateforme vidéo Nostr sécurisée pour les enfants avec contrôles parentaux et curation Web of Trust

Kubo, une plateforme vidéo sécurisée pour enfants sur Nostr, a livré v0.3.4 à v0.4.1 les 4 et 5 mai. Chaque enfant dispose d'une paire de clés Nostr distincte et d'un fil centré sur la vidéo où les parents contrôlent les limites de temps (15 à 180 minutes par jour), les plages horaires autorisées et la visibilité des actions de publication.

## Changements non publiés

### Sprout livre Desktop v0.0.4 et v0.0.5 avec l'authentification d'agent NIP-OA et le sidecar relay de jumelage

Sprout, le client Nostr de Block avec un relay intégré, a livré Desktop v0.0.4 le 5 mai et v0.0.5 le 6 mai. La PR #471 intègre l'authentification d'agent NIP-OA dans le flux d'adhésion NIP-43 du relay afin qu'un agent autonome puisse prouver qu'une clé publique humaine spécifique a autorisé ses actions. Un nouveau relay sidecar éphémère pour le jumelage d'appareils NIP-AB arrive dans la PR #467 sous la forme de sprout-pair-relay.

### nostream ajoute la prise en charge du relay Marmot et les réactions NIP-25

nostream, l'implémentation de relay Node.js, a fusionné la prise en charge du relay Marmot Protocol couvrant les MIPs 00 à 03 dans la PR #602, la prise en charge des réactions NIP-25 dans la PR #589, et la correspondance de préfixe geohash pour les filtres #g dans la PR #586.

### strfry ajoute l'observabilité par connexion et réduit le plafond nofiles

strfry, le relay Nostr en C++, a fusionné 14 PR ciblant l'observabilité. La PR #218 ajoute l'observabilité des sorties en attente par connexion et un plafond de contre-pression configurable. La PR #224 supprime les allocations de tas std::function du fanout du moniteur par événement.

### Damus remplace les GIF Tenor par un proxy Purple et livre une interface de compaction

Damus a fusionné la PR #3737 remplaçant l'intégration GIF Tenor par un proxy Damus Purple.

### Primal Android peaufine Explore, les alertes et le badge vérifié NIP-05

Primal Android a fusionné la PR #1043 corrigeant un badge vérifié NIP-05 qui clignotait pour les utilisateurs avec des identifiants _@domaine.

### Alby Hub ajoute les paiements NWC depuis les connexions d'applications

Alby Hub a fusionné la PR #2267 permettant les paiements depuis les connexions d'applications.

### routstrd-auth : un Routstrd Dockerisé pour les équipes avec authentification NIP-98 et RBAC npub

routstrd-auth, créé le 27 avril, est une variante Dockerisée de Routstrd pour les déploiements en équipe multi-utilisateurs avec contrôle d'accès basé sur les rôles via npub et authentification HTTP NIP-98.

### Routstrd intègre Hermes pour les clients démons et le mode distant

Routstrd a fusionné la PR #22 ajoutant l'intégration avec Hermes Agent afin que le fichier de configuration de l'agent soit peuplé des fournisseurs de modèles et des clés API que Routstrd découvre via Nostr.

### whitenoise-rs livre l'isolation de base de données par compte et les mises à niveau de propositions

whitenoise-rs a fusionné la PR #796 déplaçant les tables de projection de messages dans des bases de données par compte, et la PR #791 ajoute des mises à niveau de propositions pour que les groupes puissent étendre les fonctionnalités avec de nouveaux types de propositions.

### Angor 0.2.21 livre des flux d'application compacts et un durcissement du fournisseur de clés et du changement de réseau

Angor a livré 0.2.21 le 6 mai avec des améliorations de performances de conception mobile, des flux d'application compacts et un fournisseur de clés sécurisé.

## Nouvellement suivis et découverts

### BitMacro Signer : un bunker NIP-46 auto-hébergeable avec chiffrement de clé côté client

BitMacro Signer est un outil de signature Nostr auto-hébergeable utilisant le modèle bunker NIP-46. Les clés sont chiffrées côté client avant stockage, de sorte que le serveur ne détient jamais le texte en clair.

La découverte de dépôts NIP-34 a fait apparaître 26 nouvelles annonces de dépôts cette semaine, dont quatre se distinguent :

### gnostr : une implémentation git construite directement sur Nostr

gnostr est une implémentation git construite directement sur Nostr, livrant ses propres commandes d'arbre de travail en tant que client de contrôle de version natif Nostr construit de zéro.

### nostr-archive : une spécification d'archive adressée par le contenu sur Nostr et Blossom

nostr-archive est une spécification provisoire et une implémentation de référence pour les archives adressées par le contenu sur Nostr et Blossom.

### flower-cache : un serveur de cache Blossom local

flower-cache est un serveur de cache Blossom local, utile pour les clients qui souhaitent un miroir local chaud de l'ensemble de blobs d'un serveur Blossom distant.

### micro-vpn-ansible : des playbooks Ansible pour le déploiement VPN via NIP-34

micro-vpn-ansible est une petite collection de playbooks Ansible pour déployer un micro VPN, hébergé en tant que dépôt NIP-34.

## Travaux sur le protocole

### Mises à jour NIP

- Un marché de hashrate sans courtier sur Nostr (proposition provisoire) : Un brouillon NIP anonyme arguant que les acteurs actuels du marché de hashrate sont des courtiers dépositaires qui vérifient l'identité des utilisateurs. Propose un marché de hashrate P2P sur des événements Nostr.
- Curated Feeds : une alternative plus simple aux flux DVM (proposition provisoire) : Argumente que les DVMs NIP-90 sont trop lourds pour la curation de flux simple ; propose des événements adressables minces avec des listes ordonnées d'identifiants d'événements à la place.
- Profile Colors : identité visuelle déterministe (proposition provisoire) : Nouveau brouillon NIP pour dériver des couleurs lisibles déterministes à partir d'une clé publique Nostr pour une identité visuelle cohérente entre les clients.
- NIPs Namecoin-Track : ancrage de l'identité, des relais, du TLS et de la réputation (cluster provisoire) : Un cluster de NIP provisoires déplaçant les pièces de la pile Nostr dans des enregistrements ancrés Namecoin.

## NIP Deep Dive : NIP-34 (git stuff)

NIP-34 définit des types d'événements pour héberger des dépôts git, des patches, des pull requests, des issues et des statuts de fusion sur des relais Nostr. Un dépôt est annoncé comme un événement adressable de type 30617. Les patches utilisent le type 1617 transportant la sortie git format-patch. Les pull requests utilisent le type 1618. Les issues utilisent le type 1621 avec du contenu markdown. Les événements de statut font passer un fil entre Open (1630), Applied/Merged ou Resolved (1631), Closed (1632) et Draft (1633). L'actualité NIP-34 cette semaine est la même que le lancement GitWorkshop v2 de la semaine dernière : le bouton de fusion de PR dans le navigateur fonctionne parce que les serveurs GRASP, ngit et le schéma d'URL clone nostr:// ferment ensemble la boucle sur une forge entièrement décentralisée.

## NIP Deep Dive : NIP-53 (Live Activities)

NIP-53 définit la surface d'événements standard pour les activités en direct sur Nostr : diffusions en direct, espaces de réunion persistants, événements de conférence programmés, présence des auditeurs et chat en direct. Une diffusion en direct est annoncée comme un événement adressable de type 30311. NIP-53 sépare la salle persistante de l'événement programmé qui s'y déroule : un Meeting Space de type 30312 définit une salle, et un Conference Event de type 30313 représente une réunion programmée ou en cours dans cette salle. La surface des activités en direct sur Nostr est intentionnellement légère : NIP-53 annonce l'activité, tandis que d'autres NIPs gèrent les préoccupations adjacentes comme les zaps (NIP-57), les objectifs de zap (NIP-75) et les enregistrements vidéo (NIP-71).

---

C'est tout pour cette semaine. Si vous construisez quelque chose ou avez des nouvelles à partager, envoyez-nous un DM sur Nostr ou retrouvez-nous sur nostrcompass.org.
