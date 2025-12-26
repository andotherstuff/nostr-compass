---
title: "NIP-69 : Trading pair-à-pair"
date: 2025-12-17
draft: false
categories:
  - Trading
  - Protocol
---

NIP-69 définit un protocole pour le trading pair-à-pair sur Nostr, créant un carnet d'ordres unifié à travers plusieurs plateformes plutôt que des pools de liquidité fragmentés.

## Kind d'événement

- **Kind 38383** - Événements d'ordre P2P

## Structure d'ordre

Les ordres utilisent des tags pour spécifier les paramètres de trade :

- `d` - ID d'ordre
- `k` - Type d'ordre (achat/vente)
- `f` - Devise fiat (code ISO 4217)
- `amt` - Montant Bitcoin en satoshis
- `fa` - Montant fiat
- `pm` - Méthodes de paiement acceptées
- `premium` - Pourcentage de prime/remise sur le prix
- `network` - Couche de règlement (onchain, lightning, liquid)
- `expiration` - Quand l'ordre expire

## Cycle de vie de l'ordre

Les ordres progressent à travers des statuts :
- `pending` - Ouvert et disponible pour correspondance
- `in-progress` - Trade initié avec une contrepartie
- `success` - Trade complété
- `canceled` - Retiré par le maker
- `expired` - Temps d'expiration dépassé

## Sécurité

Le tag `bond` spécifie un dépôt de garantie que les deux parties doivent payer, fournissant une protection contre l'abandon ou la fraude.

---

**Sources principales :**
- [Spécification NIP-69](https://github.com/nostr-protocol/nips/blob/master/69.md)

**Mentionné dans :**
- [Newsletter #1 : Mises à jour NIP](/fr/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #1 : Sorties](/fr/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #2 : Actualités](/fr/newsletters/2025-12-24-newsletter/#news)

