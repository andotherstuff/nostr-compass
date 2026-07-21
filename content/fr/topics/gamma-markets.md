---
title: "Gamma Markets"
date: 2026-07-15
translationOf: /en/topics/gamma-markets.md
translationDate: 2026-07-15
draft: false
categories:
  - Commerce
  - Marketplace
  - Protocol
---

Gamma Markets est un ensemble de conventions e-commerce construites directement sur les annonces classées [NIP-99](/fr/topics/nip-99/), développées de manière collaborative par un groupe de travail de développeurs de places de marché Nostr : les équipes derrière Shopstr, Cypher, Plebeian Market et Conduit Market. Il comble les conventions d'expédition, de flux de commandes, de collections et d'avis que NIP-99 lui-même laisse indéfinies.

## Fonctionnement

Gamma Markets ajoute cinq types d'events autour de l'event d'annonce kind `30402` existant de NIP-99, sans modifier la forme de cet event :

- **Kind 30405** - collections de produits, regroupant plusieurs annonces ensemble via des tags `a`
- **Kind 30406** - options d'expédition, avec tarification par pays et règles de coût optionnelles basées sur le poids ou la distance
- **Kind 16** - messages de commande : création (type 1), demandes de paiement (type 2), mises à jour de statut (type 3) et mises à jour d'expédition (type 4)
- **Kind 14** - communication générale acheteur/vendeur
- **Kind 17** - reçus de paiement
- **Kind 31555** - avis sur les produits, adressés à un pubkey vendeur spécifique et au tag `d` de l'annonce

Les préférences de paiement d'un vendeur sont déclarées via un tag `payment_preference` sur ses métadonnées de profil kind `0`, et les clients découvrent les applications compatibles via les recommandations d'applications [NIP-89](/fr/topics/nip-89/). La communication des commandes s'appuie sur les messages privés [NIP-17](/fr/topics/nip-17/), sans nouveau schéma de chiffrement propre.

Le choix de conception déterminant de la spécification est que rien ne se propage en cascade : une annonce qui appartient à une collection, ou qui utilise une option d'expédition, la référence explicitement avec un tag `a` au lieu d'hériter automatiquement des paramètres de son parent. C'est un départ délibéré de l'ancien modèle de stall [NIP-15](/fr/topics/nip-15/), où un produit héritait silencieusement de la devise et du tableau d'expédition de son stall.

### Exemple : création de commande (kind 16, type 1)

```json
{
  "kind": 16,
  "content": "Please leave the package with the doorman.",
  "tags": [
    ["p", "<merchant-pubkey>"],
    ["subject", "New order"],
    ["type", "1"],
    ["order", "order-8f21"],
    ["amount", "115000"],
    ["item", "30402:<merchant-pubkey>:keyboard-mx-blue-01", "1"],
    ["shipping", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

## Pourquoi c'est important

NIP-99 seul ne standardise que l'annonce elle-même, une petite annonce signée et adressable. Avant Gamma Markets, chaque client construisant du véritable e-commerce sur NIP-99 inventait ses propres conventions privées pour l'expédition, le paiement et les avis, ce qui signifiait que deux clients conformes à NIP-99 pouvaient chacun afficher une annonce correctement mais n'avaient aucun moyen partagé de finaliser une commande entre eux. Gamma Markets comble cette lacune sans toucher au format d'annonce NIP-99 lui-même, de sorte que les annonces NIP-99 existantes restent valides sans modification.

## Implémentations

- [Shopstr](https://github.com/shopstr-eng/shopstr) - place de marché Nostr, l'un des quatre projets ayant rédigé la spécification
- [Conduit Mono](https://github.com/Conduit-BTC/conduit-mono) - protocole de place de marché construisant son propre flux d'état des commandes et de paiement dans le même espace de conception

---

**Sources primaires :**
- [Dépôt de la spécification Gamma Markets](https://github.com/GammaMarkets/market-spec)
- [Extension de cas d'utilisation e-commerce NIP-99, PR #1784](https://github.com/nostr-protocol/nips/pull/1784) - lien fusionné depuis le document canonique NIP-99 vers la spécification Gamma Markets

**Mentionné dans :**
- [Bulletin #31 : Analyse approfondie : NIP-99 et l'extension commerce Gamma Markets](/fr/newsletters/2026-07-15-newsletter/#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension)

**Voir aussi :**
- [NIP-99 : Annonces classées](/fr/topics/nip-99/)
- [NIP-15 : Place de marché Nostr](/fr/topics/nip-15/)
- [NIP-17 : Messages privés directs](/fr/topics/nip-17/)
