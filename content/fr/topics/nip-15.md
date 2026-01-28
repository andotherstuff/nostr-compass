---
title: "NIP-15 : Place de marché Nostr"
date: 2026-01-28
translationOf: /en/topics/nip-15.md
translationDate: 2026-01-28
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
    ["d", "mon-etal"],
    ["name", "Électronique de Bob"],
    ["description", "Électronique d'occasion de qualité"],
    ["currency", "sat"],
    ["shipping", "{...options de livraison...}"]
  ]
}
```

### Produits (Kind 30018)

Les produits sont listés au sein des étals :

```json
{
  "kind": 30018,
  "tags": [
    ["d", "produit-123"],
    ["stall_id", "mon-etal"],
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

## Caractéristiques clés

- **Décentralisé** : Pas d'opérateur de place de marché central
- **Interopérable** : N'importe quel client NIP-15 peut parcourir n'importe quel marchand
- **Privé** : Les commandes sont chiffrées entre acheteur et vendeur
- **Natif Bitcoin** : Paiements Lightning intégrés

## Implémentations

- **Plebeian Market** - Place de marché NIP-15 complète
- **Shopstr** - Commerce Bitcoin sans permission
- **Amethyst** - Listes de produits intégrées dans le fil social

## Voir aussi

- [NIP-44](/fr/topics/nip-44/) - Messages chiffrés pour les commandes
- [NIP-57](/fr/topics/nip-57/) - Zaps Lightning
