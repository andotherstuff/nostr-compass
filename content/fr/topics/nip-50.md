---
title: "NIP-50: Search"
date: 2025-12-31
translationOf: /en/topics/nip-50.md
translationDate: 2025-12-31
draft: false
categories:
  - Protocole
  - Relais
---

NIP-50 définit une capacité de recherche généralisée pour les relays Nostr, permettant aux clients d'effectuer des recherches en texte intégral au-delà des requêtes structurées par tags ou IDs.

## Comment Ça Fonctionne

Le protocole ajoute un champ `search` aux objets de filtre dans les messages REQ :

1. Les clients soumettent des requêtes de recherche lisibles par l'homme (ex. "meilleures apps nostr")
2. Les relays interprètent et font correspondre les requêtes aux données d'événements, principalement le champ `content`
3. Les résultats sont classés par pertinence plutôt que par ordre chronologique
4. Le filtre `limit` s'applique après le tri par pertinence

Les filtres de recherche peuvent être combinés avec d'autres contraintes comme `kinds` et `ids` pour des requêtes plus spécifiques.

## Extensions de Recherche

Les relays peuvent optionnellement supporter ces paramètres d'extension :

- `include:spam` - Désactive le filtrage de spam par défaut
- `domain:<domain>` - Filtre par domaine NIP-05 vérifié
- `language:<code>` - Filtre par code de langue ISO
- `sentiment:<value>` - Filtre par sentiment négatif/neutre/positif
- `nsfw:<true/false>` - Inclut ou exclut le contenu NSFW

## Considérations pour les Clients

- Les clients doivent vérifier les capacités du relay via le champ `supported_nips`
- La vérification des résultats côté client est recommandée
- Tous les relays n'implémentent pas la recherche ; elle reste une fonctionnalité optionnelle

---

**Sources primaires :**
- [Spécification NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md)

**Mentionné dans :**
- [Newsletter #3 : Récap de Décembre](/fr/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Voir aussi :**
- [NIP-11: Informations Relay](/fr/topics/nip-11/)
