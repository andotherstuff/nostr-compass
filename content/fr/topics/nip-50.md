---
title: "NIP-50 : Search"
date: 2025-12-31
translationOf: /en/topics/nip-50.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Relay
---

NIP-50 définit une capacité de recherche générale pour les relais Nostr. Il ajoute des requêtes de type texte intégral en complément des filtres par correspondance exacte de NIP-01.

## Fonctionnement

Le protocole ajoute un champ `search` aux objets de filtre dans les messages `REQ` :

1. Les clients soumettent une chaîne de requête lisible par l'humain, comme `best nostr apps`.
2. Les relais interprètent cette requête par rapport aux données d'événements, principalement le champ `content`.
3. Les résultats sont triés par qualité de correspondance, pas par `created_at`.
4. La valeur `limit` s'applique après le tri par pertinence.

Les filtres de recherche peuvent être combinés avec `kinds`, `ids`, auteurs et autres champs de filtre standard pour des requêtes plus spécifiques.

## Extensions de recherche

Les relais peuvent optionnellement supporter ces paramètres d'extension :

- `include:spam` - Désactive le filtrage de spam par défaut
- `domain:<domain>` - Filtre par domaine NIP-05 vérifié
- `language:<code>` - Filtre par code de langue ISO
- `sentiment:<value>` - Filtre par sentiment négatif, neutre ou positif
- `nsfw:<true/false>` - Inclut ou exclut le contenu NSFW

Les relais doivent ignorer les extensions qu'ils ne supportent pas, les clients doivent donc les traiter comme des indications, pas des garanties.

## Notes d'interopérabilité

- Les clients doivent vérifier les capacités du relais via le champ `supported_nips`
- La vérification côté client des résultats est recommandée
- Tous les relais n'implémentent pas la recherche ; elle reste une fonctionnalité optionnelle

Le classement étant défini par l'implémentation, la même requête peut retourner des ensembles de résultats différents sur des relais différents. Les clients qui se soucient du rappel devraient interroger plus d'un relais de recherche et fusionner les résultats.

## Pourquoi c'est important

Les filtres structurés fonctionnent bien quand on connaît déjà l'auteur, le kind ou le tag recherché. La recherche sert au cas inverse : la découverte. Cela rend NIP-50 utile pour les annuaires d'applications, les archives longues et la recherche de notes publiques, mais signifie aussi que la qualité de la recherche dépend fortement des choix d'indexation et de filtrage anti-spam de chaque relais.

---

**Sources principales :**
- [NIP-50 Specification](https://github.com/nostr-protocol/nips/blob/master/50.md)

**Mentionné dans :**
- [Newsletter #3 : December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #7 : NIP Updates](/en/newsletters/2026-01-07-newsletter/#nip-updates)

**Voir aussi :**
- [NIP-11 : Relay Information](/fr/topics/nip-11/)
