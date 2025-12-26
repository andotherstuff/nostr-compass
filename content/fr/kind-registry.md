---
title: Registre des Kinds
url: /fr/kind-registry/
translationOf: /en/kind-registry.md
translationDate: 2025-12-26
---

Les kinds d'événements sont des entiers qui catégorisent les événements Nostr. Ce registre liste tous les kinds standardisés avec leurs descriptions et les NIPs qui les définissent.

**Plages de kinds** (selon [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)) :
- **0-999** : Événements réguliers (toutes les versions conservées)
- **1000-9999** : Événements réguliers (suite)
- **10000-19999** : Événements remplaçables (seul le plus récent par pubkey est conservé)
- **20000-29999** : Événements éphémères (non stockés, seulement relayés)
- **30000-39999** : Événements adressables (plus récent par pubkey + kind + d-tag)

## Événements de base (0-99)

| Kind | Description | NIP |
|------|-------------|-----|
| 0 | Métadonnées utilisateur | [01](https://github.com/nostr-protocol/nips/blob/master/01.md) |
| 1 | Note textuelle courte | [10](https://github.com/nostr-protocol/nips/blob/master/10.md) |
| 2 | Recommandation de relais (obsolète) | [01](https://github.com/nostr-protocol/nips/blob/master/01.md) |
| 3 | Abonnements | [02](https://github.com/nostr-protocol/nips/blob/master/02.md) |
| 4 | Messages directs chiffrés | [04](https://github.com/nostr-protocol/nips/blob/master/04.md) |
| 5 | Demande de suppression d'événement | [09](https://github.com/nostr-protocol/nips/blob/master/09.md) |
| 6 | Repost | [18](https://github.com/nostr-protocol/nips/blob/master/18.md) |
| 7 | Réaction | [25](https://github.com/nostr-protocol/nips/blob/master/25.md) |
| 8 | Attribution de badge | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 9 | Message de chat | [C7](https://github.com/nostr-protocol/nips/blob/master/C7.md) |
| 10 | Réponse filetée de chat de groupe (obsolète) | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 11 | Fil de discussion | [7D](https://github.com/nostr-protocol/nips/blob/master/7D.md) |
| 12 | Réponse de fil de groupe (obsolète) | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 13 | Seal | [59](https://github.com/nostr-protocol/nips/blob/master/59.md) |
| 14 | Message direct | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 15 | Message fichier | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 16 | Repost générique | [18](https://github.com/nostr-protocol/nips/blob/master/18.md) |
| 17 | Réaction à un site web | [25](https://github.com/nostr-protocol/nips/blob/master/25.md) |
| 20 | Image | [68](https://github.com/nostr-protocol/nips/blob/master/68.md) |
| 21 | Événement vidéo | [71](https://github.com/nostr-protocol/nips/blob/master/71.md) |
| 22 | Vidéo portrait courte | [71](https://github.com/nostr-protocol/nips/blob/master/71.md) |
| 40 | Création de canal | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 41 | Métadonnées de canal | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 42 | Message de canal | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 43 | Masquer message de canal | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 44 | Rendre muet utilisateur de canal | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 62 | Demande de disparition | [62](https://github.com/nostr-protocol/nips/blob/master/62.md) |
| 64 | Échecs (PGN) | [64](https://github.com/nostr-protocol/nips/blob/master/64.md) |

## Chiffrement MLS (443-445)

| Kind | Description | NIP |
|------|-------------|-----|
| 443 | KeyPackage | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 444 | Message de bienvenue | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 445 | Événement de groupe | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |

## Événements réguliers (1000-9999)

| Kind | Description | NIP |
|------|-------------|-----|
| 1018 | Réponse au sondage | [88](https://github.com/nostr-protocol/nips/blob/master/88.md) |
| 1021 | Enchère | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 1022 | Confirmation d'enchère | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 1040 | OpenTimestamps | [03](https://github.com/nostr-protocol/nips/blob/master/03.md) |
| 1059 | Gift Wrap | [59](https://github.com/nostr-protocol/nips/blob/master/59.md) |
| 1063 | Métadonnées de fichier | [94](https://github.com/nostr-protocol/nips/blob/master/94.md) |
| 1068 | Sondage | [88](https://github.com/nostr-protocol/nips/blob/master/88.md) |
| 1111 | Commentaire | [22](https://github.com/nostr-protocol/nips/blob/master/22.md) |
| 1222 | Message vocal | [A0](https://github.com/nostr-protocol/nips/blob/master/A0.md) |
| 1244 | Commentaire de message vocal | [A0](https://github.com/nostr-protocol/nips/blob/master/A0.md) |
| 1311 | Message de chat en direct | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 1337 | Extrait de code | [C0](https://github.com/nostr-protocol/nips/blob/master/C0.md) |
| 1617 | Patches | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1618 | Pull Requests | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1619 | Mises à jour de Pull Request | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1621 | Issues | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1984 | Signalement | [56](https://github.com/nostr-protocol/nips/blob/master/56.md) |
| 1985 | Étiquette | [32](https://github.com/nostr-protocol/nips/blob/master/32.md) |
| 2003 | Torrent | [35](https://github.com/nostr-protocol/nips/blob/master/35.md) |
| 2004 | Commentaire Torrent | [35](https://github.com/nostr-protocol/nips/blob/master/35.md) |
| 4550 | Approbation de publication communautaire | [72](https://github.com/nostr-protocol/nips/blob/master/72.md) |
| 5000-5999 | Demande de tâche | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 6000-6999 | Résultat de tâche | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 7000 | Retour de tâche | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 7374 | Jetons de portefeuille Cashu réservés | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 7375 | Jetons de portefeuille Cashu | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 7376 | Historique du portefeuille Cashu | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 8000 | Ajouter utilisateur | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 8001 | Supprimer utilisateur | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 9000-9030 | Événements de contrôle de groupe | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 9041 | Objectif de zap | [75](https://github.com/nostr-protocol/nips/blob/master/75.md) |
| 9321 | Nutzap | [61](https://github.com/nostr-protocol/nips/blob/master/61.md) |
| 9734 | Demande de zap | [57](https://github.com/nostr-protocol/nips/blob/master/57.md) |
| 9735 | Zap | [57](https://github.com/nostr-protocol/nips/blob/master/57.md) |
| 9802 | Surlignages | [84](https://github.com/nostr-protocol/nips/blob/master/84.md) |

## Événements remplaçables (10000-19999)

| Kind | Description | NIP |
|------|-------------|-----|
| 10000 | Liste de comptes masqués | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10001 | Liste épinglée | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10002 | Métadonnées de liste de relais | [65](https://github.com/nostr-protocol/nips/blob/master/65.md) |
| 10003 | Liste de favoris | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10004 | Liste de communautés | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10005 | Liste de chats publics | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10006 | Liste de relais bloqués | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10007 | Liste de relais de recherche | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10009 | Groupes d'utilisateurs | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10012 | Liste de relais favoris | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10013 | Liste de relais d'événements privés | [37](https://github.com/nostr-protocol/nips/blob/master/37.md) |
| 10015 | Liste d'intérêts | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10019 | Recommandation de mint Nutzap | [61](https://github.com/nostr-protocol/nips/blob/master/61.md) |
| 10020 | Abonnements médias | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10030 | Liste d'émojis utilisateur | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10050 | Liste de relais pour recevoir des DM | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 10051 | Liste de relais KeyPackage | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 10063 | Liste de serveurs utilisateur | Blossom |
| 10166 | Annonce de moniteur de relais | [66](https://github.com/nostr-protocol/nips/blob/master/66.md) |
| 10312 | Présence dans la salle | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 13194 | Info portefeuille | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 13534 | Listes de membres | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 17375 | Événement de portefeuille Cashu | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |

## Authentification et portefeuille (22000-27999)

| Kind | Description | NIP |
|------|-------------|-----|
| 22242 | Authentification client | [42](https://github.com/nostr-protocol/nips/blob/master/42.md) |
| 23194 | Demande de portefeuille | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 23195 | Réponse de portefeuille | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 24133 | Nostr Connect | [46](https://github.com/nostr-protocol/nips/blob/master/46.md) |
| 24242 | Blobs stockés sur les serveurs médias | Blossom |
| 27235 | Authentification HTTP | [98](https://github.com/nostr-protocol/nips/blob/master/98.md) |

## Contrôle d'accès (28000-29999)

| Kind | Description | NIP |
|------|-------------|-----|
| 28934 | Demande d'adhésion | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 28935 | Demande d'invitation | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 28936 | Demande de départ | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |

## Événements adressables (30000-39999)

| Kind | Description | NIP |
|------|-------------|-----|
| 30000 | Ensembles d'abonnements | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30002 | Ensembles de relais | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30003 | Ensembles de favoris | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30004 | Ensembles de curation | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30005 | Ensembles de vidéos | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30007 | Ensembles de kinds masqués | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30008 | Badges de profil | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 30009 | Définition de badge | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 30015 | Ensembles d'intérêts | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30017 | Créer ou mettre à jour un stand | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30018 | Créer ou mettre à jour un produit | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30019 | UI/UX Marketplace | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30020 | Produit vendu aux enchères | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30023 | Contenu long format | [23](https://github.com/nostr-protocol/nips/blob/master/23.md) |
| 30024 | Brouillon de contenu long format | [23](https://github.com/nostr-protocol/nips/blob/master/23.md) |
| 30030 | Ensembles d'émojis | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30063 | Ensembles d'artefacts de release | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30078 | Données spécifiques à l'application | [78](https://github.com/nostr-protocol/nips/blob/master/78.md) |
| 30166 | Découverte de relais | [66](https://github.com/nostr-protocol/nips/blob/master/66.md) |
| 30267 | Ensembles de curation d'applications | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30311 | Événement en direct | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30312 | Salle interactive | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30313 | Événement de conférence | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30315 | Statuts utilisateur | [38](https://github.com/nostr-protocol/nips/blob/master/38.md) |
| 30402 | Petite annonce | [99](https://github.com/nostr-protocol/nips/blob/master/99.md) |
| 30403 | Brouillon de petite annonce | [99](https://github.com/nostr-protocol/nips/blob/master/99.md) |
| 30617 | Annonces de dépôt | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 30618 | Annonces d'état de dépôt | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 30818 | Article wiki | [54](https://github.com/nostr-protocol/nips/blob/master/54.md) |
| 30819 | Redirections | [54](https://github.com/nostr-protocol/nips/blob/master/54.md) |
| 31234 | Événement brouillon | [37](https://github.com/nostr-protocol/nips/blob/master/37.md) |
| 31922 | Événement de calendrier basé sur la date | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31923 | Événement de calendrier basé sur l'heure | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31924 | Calendrier | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31925 | RSVP d'événement de calendrier | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31989 | Recommandation de gestionnaire | [89](https://github.com/nostr-protocol/nips/blob/master/89.md) |
| 31990 | Information de gestionnaire | [89](https://github.com/nostr-protocol/nips/blob/master/89.md) |
| 34550 | Définition de communauté | [72](https://github.com/nostr-protocol/nips/blob/master/72.md) |
| 38172 | Annonce de mint Cashu | [87](https://github.com/nostr-protocol/nips/blob/master/87.md) |
| 38173 | Annonce Fedimint | [87](https://github.com/nostr-protocol/nips/blob/master/87.md) |
| 38383 | Événements d'ordre pair-à-pair | [69](https://github.com/nostr-protocol/nips/blob/master/69.md) |
| 39000-39009 | Événements de métadonnées de groupe | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 39089 | Packs de démarrage | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 39092 | Packs de démarrage média | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 39701 | Favoris web | [B0](https://github.com/nostr-protocol/nips/blob/master/B0.md) |

*Dernière mise à jour : décembre 2025*

Voir le [dépôt NIPs](https://github.com/nostr-protocol/nips) pour la source officielle.
