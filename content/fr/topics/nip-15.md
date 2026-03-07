---
title: "NIP-15 : Place de marché Nostr"
date: 2026-01-28
translationOf: /en/topics/nip-15.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Commerce
  - Marketplace
---

NIP-15 définit un protocole pour les places de marché décentralisées sur Nostr, permettant aux marchands de lister des produits et aux acheteurs d'effectuer des achats en utilisant Bitcoin et Lightning.

## Fonctionnement

### Étals marchands (Kind 30017)

Les marchands créent des étals comme événements adressables :

```json
{
  "kind": 30017,
  "tags": [
    ["d", "my-stall"],
    ["name", "Bob's Electronics"],
    ["description", "Quality used electronics"],
    ["currency", "sat"],
    ["shipping", "{...shipping options...}"]
  ]
}
```

### Produits (Kind 30018)

Les produits sont listés au sein des étals :

```json
{
  "kind": 30018,
  "tags": [
    ["d", "product-123"],
    ["stall_id", "my-stall"],
    ["name", "Raspberry Pi 4"],
    ["price", "50000"],
    ["quantity", "5"],
    ["images", "https://..."]
  ]
}
```

## Flux d'achat

1. L'acheteur parcourt les produits sur plusieurs étals
2. L'acheteur envoie un message de commande chiffré au marchand
3. Le marchand répond avec une facture Lightning
4. L'acheteur paie la facture
5. Le marchand expédie le produit

## Pourquoi c'est important

- **Décentralisé** : Pas d'opérateur de place de marché central
- **Interopérable** : N'importe quel client NIP-15 peut parcourir n'importe quel marchand
- **Privé** : Les commandes sont chiffrées entre acheteur et vendeur
- **Natif Bitcoin** : Paiements Lightning intégrés

Le gain pratique est la portabilité. Un marchand peut publier ses données de catalogue une seule fois et laisser plusieurs clients les afficher, au lieu d'être lié à un seul front-end de place de marché.

## Compromis

NIP-15 standardise les annonces, pas la confiance. Les acheteurs doivent encore décider si un marchand est légitime, si l'inventaire est réel, et comment les litiges sont gérés. Le protocole fournit des structures de données et un flux de messages communs, mais la réputation et l'exécution des commandes restent des problèmes au niveau applicatif.

Les paiements et la livraison ne sont aussi que partiellement standardisés. Un client peut comprendre les étals et les produits tout en ayant besoin de logique spécifique pour les factures, l'état des commandes ou le suivi de livraison.

## État des implémentations

- **Plebeian Market** - Place de marché NIP-15 complète
- **Shopstr** - Commerce Bitcoin sans permission
- **Amethyst** - Listes de produits intégrées dans le fil social

---

**Sources principales :**
- [Spécification NIP-15](https://github.com/nostr-protocol/nips/blob/master/15.md)

**Mentionné dans :**
- [Newsletter #7 : January 2024 Protocol Hardening](/en/newsletters/2026-01-28-newsletter/#january-2024-protocol-hardening)

**Voir aussi :**
- [NIP-44 : Encrypted Payloads](/fr/topics/nip-44/)
- [NIP-57 : Lightning Zaps](/fr/topics/nip-57/)
