---
title: "NIP-99 : Annonces classifiées"
date: 2026-03-11
translationOf: /en/topics/nip-99.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Commerce
  - Marketplaces
---

NIP-99 définit des événements adressables d'annonces classifiées pour les biens, services, emplois, locations et autres offres. Il donne aux applications de marketplace un modèle d'événement plus simple que l'ancienne spécification marketplace [NIP-15](/fr/topics/nip-15/), c'est pourquoi de nombreux clients de commerce actuels se construisent sur NIP-99.

## Comment ça fonctionne

Les annonces actives utilisent le kind `30402`, tandis que les brouillons ou annonces inactives utilisent le kind `30403`. La pubkey de l'auteur est le vendeur ou créateur de l'offre. Le champ `content` porte la description lisible en Markdown, et les tags contiennent les champs structurés tels que titre, résumé, prix, localisation et statut.

```json
{
  "id": "b3e392b11f5d4f28321cedd09303a748acfd0487aea5a7450b3481c60b6e4f87",
  "pubkey": "a695f6b60119d9521934a691347d9f78e8770b56da16bb255ee286ddf9fda919",
  "created_at": 1741699200,
  "kind": 30402,
  "tags": [
    ["d", "shopstr-handmade-wallet-001"],
    ["title", "Handmade leather wallet"],
    ["summary", "Brown bifold wallet with Bitcoin and Nostr branding"],
    ["published_at", "1741699200"],
    ["location", "Austin, TX"],
    ["price", "75000", "SAT"],
    ["status", "active"],
    ["t", "merch"],
    ["t", "bitcoin"]
  ],
  "content": "Full listing description in Markdown, shipping details, and contact terms.",
  "sig": "4a5c7e8f9012ab34cd56ef7890ab12cd34ef56ab78cd90ef12ab34cd56ef78900112233445566778899aabbccddeeff00112233445566778899aabbccddeeff"
}
```

L'événement est adressable, donc un vendeur peut mettre à jour l'annonce en conservant le même tuple d'identité composé de la pubkey, du kind et du tag `d`. Cela rend les révisions d'annonces plus propres pour les clients que la publication d'une nouvelle note immuable pour chaque changement de prix ou de statut.

## Pourquoi c'est important

La force de NIP-99 est qu'il laisse de la place pour différentes conceptions de marketplace tout en standardisant la forme de base de l'annonce. Un client peut se concentrer sur les annonces locales, un autre sur les abonnements, et un autre sur les catalogues de produits mondiaux. S'ils s'accordent tous sur la structure de l'événement, les vendeurs peuvent publier une seule fois et obtenir quand même une certaine visibilité inter-clients.

Cette flexibilité explique aussi pourquoi les projets de marketplace actuels le privilégient. La spécification est suffisamment structurée pour supporter la recherche et l'affichage, mais elle n'impose pas à chaque application un flux unique de séquestre, d'expédition ou de paiement.

## Notes d'implémentation

- Les tags `price` peuvent décrire des paiements ponctuels ou récurrents en ajoutant un champ de fréquence optionnel.
- Les tags `t` agissent comme des catégories ou mots-clés de recherche.
- Les tags `image` permettent aux clients de rendre des vues galerie sans analyser le corps Markdown.
- Une annonce peut se lier à des événements ou documents associés avec des tags `e` ou `a` lorsqu'une marketplace souhaite un contexte produit plus riche.

## Implémentations

- [Shopstr](https://github.com/shopstr-eng/shopstr) - Marketplace Nostr utilisant les annonces NIP-99 avec des endpoints MCP orientés agents
- [Milk Market](https://github.com/shopstr-eng/milk-market) - Marketplace alimentaire construite sur la même couche d'annonces avec des options de paiement mixtes

---

**Sources principales :**
- [Spécification NIP-99](https://github.com/nostr-protocol/nips/blob/master/99.md)
- [Shopstr PR #234](https://github.com/shopstr-eng/shopstr/pull/234) - Endpoints de commerce MCP au-dessus des annonces NIP-99
- [Milk Market PR #10](https://github.com/shopstr-eng/milk-market/pull/10) - Abonnement et paiement multi-marchands au-dessus des annonces de marketplace

**Mentionné dans :**
- [Newsletter #13 : Shopstr et Milk Market ouvrent des surfaces de commerce MCP](/en/newsletters/2026-03-11-newsletter/#shopstr-and-milk-market-open-mcp-commerce-surfaces)

**Voir aussi :**
- [NIP-15 : Offres de marketplace](/fr/topics/nip-15/)
- [NIP-47 : Nostr Wallet Connect](/fr/topics/nip-47/)
- [NIP-60 : Cashu Wallet](/fr/topics/nip-60/)
