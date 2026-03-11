---
title: "NIP-99 : Annonces classées"
date: 2026-03-11
translationOf: /en/topics/nip-99.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Commerce
  - Marketplaces
---

NIP-99 définit des événements d'annonces classées adressables pour des biens, services, emplois, locations et autres offres. Il donne aux applications de marketplace un modèle d'événement plus simple que l'ancienne spécification de marketplace [NIP-15](/fr/topics/nip-15/), ce qui explique pourquoi de nombreux clients de commerce actuels s'appuient plutôt sur NIP-99.

## Comment cela fonctionne

Les annonces actives utilisent le kind `30402`, tandis que les brouillons ou annonces inactives utilisent le kind `30403`. La pubkey de l'auteur est celle du vendeur ou du créateur de l'offre. Le champ `content` contient la description lisible par un humain en Markdown, et les tags portent des champs structurés tels que le titre, le résumé, le prix, la localisation et le statut.

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

L'événement est adressable, donc un vendeur peut mettre à jour l'annonce tout en conservant le même tuple d'identité composé de la pubkey, du kind et du tag `d`. Cela rend les révisions d'annonces plus propres pour les clients que la publication d'une nouvelle note immuable pour chaque changement de prix ou de statut.

## Pourquoi c'est important

La force de NIP-99 est de laisser de la place à différents designs de marketplaces tout en standardisant la forme de base de l'annonce. Un client peut se concentrer sur les petites annonces locales, un autre sur les abonnements, et un autre sur des catalogues produits mondiaux. S'ils s'accordent tous sur la structure de l'événement, les vendeurs peuvent publier une seule fois et obtenir malgré tout une certaine visibilité inter-client.

Cette flexibilité explique aussi pourquoi les projets de marketplace actuels le privilégient. La spécification est suffisamment structurée pour supporter la recherche et l'affichage, mais elle ne force pas chaque application à adopter un seul flux d'escrow, d'expédition ou de paiement.

## Notes d'implémentation

- Les tags `price` peuvent décrire des paiements uniques ou récurrents en ajoutant un champ de fréquence optionnel.
- Les tags `t` servent de catégories ou de mots-clés de recherche.
- Les tags `image` permettent aux clients d'afficher des galeries sans analyser le corps Markdown.
- Une annonce peut lier des événements ou documents associés avec des tags `e` ou `a` lorsqu'une marketplace veut un contexte produit plus riche.

## Implémentations

- [Shopstr](https://github.com/shopstr-eng/shopstr) - Marketplace Nostr utilisant des annonces NIP-99 avec des endpoints MCP exposés aux agents
- [Milk Market](https://github.com/shopstr-eng/milk-market) - Marketplace alimentaire construite sur la même couche d'annonces avec des options de paiement mixtes

---

**Sources principales :**
- [Spécification NIP-99](https://github.com/nostr-protocol/nips/blob/master/99.md)
- [Shopstr PR #234](https://github.com/shopstr-eng/shopstr/pull/234) - Endpoints de commerce MCP au-dessus des annonces NIP-99
- [Milk Market PR #10](https://github.com/shopstr-eng/milk-market/pull/10) - Abonnements et checkout multi-marchands au-dessus des annonces de marketplace

**Mentionné dans :**
- [Newsletter #13 : Shopstr et Milk Market ouvrent des surfaces de commerce MCP](/fr/newsletters/2026-03-11-newsletter/#shopstr-et-milk-market-ouvrent-des-surfaces-de-commerce-mcp)

**Voir aussi :**
- [NIP-15 : Offres de marketplace](/fr/topics/nip-15/)
- [NIP-47 : Nostr Wallet Connect](/fr/topics/nip-47/)
- [NIP-60 : Cashu Wallet](/fr/topics/nip-60/)
