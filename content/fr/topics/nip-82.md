---
title: "NIP-82 proposé (non attribué) : catalogue d’applications logicielles"
date: 2026-06-17
lastmod: 2026-10-28
translationOf: /en/topics/nip-82.md
translationDate: 2026-10-28
draft: false
categories:
  - Proposals
  - Apps
---

Le catalogue d’applications logicielles décrit sur cette page est une proposition en cours d’examen. Ce n’est pas un NIP accepté. Il figure dans la [pull request #2526 de nostr-protocol/nips](https://github.com/nostr-protocol/nips/pull/2526), intitulée « Zapstore spec ». À la date de la dernière mise à jour de cette page, cette pull request est ouverte et non fusionnée, et la branche master officielle des NIPs ne contient aucun fichier `82.md`. « NIP-82 » est le label que la proposition s’attribue à elle-même. Il ne s’agit pas d’un numéro de NIP officiel. Les kinds d’event, les tags et le comportement peuvent évoluer avant une éventuelle fusion. Selon la pull request, elle remplace la [pull request #1336](https://github.com/nostr-protocol/nips/pull/1336), plus ancienne.

## Kinds d’event proposés

Le brouillon répartit un catalogue logiciel entre plusieurs kinds d’event :

- **Kind 32267, application :** un event adressable qui décrit une app.
- **Kind 30063, version :** un event adressable consacré à une version donnée de cette app. Il référence les fichiers de cette version.
- **Kind 3063, fichier :** un event régulier qui décrit un fichier téléchargeable.
- **Kind 30267, curation :** une liste adressable qu’un curateur publie pour regrouper ou recommander des apps.
- **Kind 30509, lien de certificat de signature :** un event adressable qui relie un certificat X.509, par exemple un certificat de signature d’APK, à la clé Nostr qui publie le logiciel, afin que les clients sachent quels certificats cet éditeur contrôle. Son tag `d` correspond au hachage SHA-256 du certificat encodé en DER. Il porte une signature réalisée avec la clé privée du certificat ainsi qu’une date d’expiration sous forme d’horodatage Unix, et peut, de manière facultative, marquer le lien comme révoqué.
- **Kind 10067, liste de relays :** une liste remplaçable des relays où trouver les events du catalogue.

## Plateforme, intégrité et validité

Les events de fichier portent des identifiants de plateforme et d’environnement d’exécution, ce qui permet à un client de n’afficher que les fichiers adaptés à un appareil. Chaque fichier porte aussi un hachage. Grâce à lui, un client peut vérifier que les octets téléchargés correspondent à ce que l’éditeur a signé. Pour les paquets Android, le brouillon inclut l’empreinte du certificat de signature. Avant de proposer une mise à jour, un installateur peut la comparer au certificat d’une app déjà installée. Avant d’installer un paquet Android, les clients DEVRAIENT (SHOULD) récupérer l’event de kind 30509 à partir du hachage du certificat. Ils devraient vérifier sa signature de certificat par rapport au certificat intégré à l’APK et par rapport à l’éditeur du fichier, puis s’assurer que la preuve n’a ni expiré ni été révoquée.

## Limites de confiance

Une signature valide montre seulement qu’une clé donnée a publié un event. Elle ne prouve ni que cette clé appartient au véritable développeur, ni que le logiciel est sûr, ni que la liste d’un curateur est digne de confiance. La proposition n’offre aucune garantie concernant des éditeurs quelconques. C’est aux clients et aux utilisateurs de décider à quelles clés d’éditeurs et de curateurs se fier. Cette page ne revendique aucun audit de sécurité ni aucune interopérabilité en production.

## Relation avec NIP-89

Les events de gestionnaire de [NIP-89](/fr/topics/nip-89/) annoncent quelles applications peuvent traiter quels kinds d’event. Cette proposition décrit quant à elle les artefacts logiciels et l’endroit où les obtenir ; les deux couvrent donc des besoins distincts.

---

**Sources primaires :**
- [PR #2526 de nostr-protocol/nips : Zapstore spec](https://github.com/nostr-protocol/nips/pull/2526) (ouverte, non fusionnée ; remplace la [PR #1336](https://github.com/nostr-protocol/nips/pull/1336))

**Mentionné dans :**
- [Newsletter n° 27 : couverture de la version v1.12.0 d’Amethyst (référence historique)](/en/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
- [Newsletter n° 46 : catalogue d’applications logicielles proposé comme NIP-82](/fr/newsletters/2026-10-28-newsletter/#software-application-catalog-proposed-as-nip-82)

**Voir aussi :**
- [NIP-89 : gestionnaires d’applications](/fr/topics/nip-89/)
