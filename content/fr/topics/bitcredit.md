---
title: "Bitcredit"
date: 2026-03-25
translationOf: /en/topics/bitcredit.md
translationDate: 2026-04-01
draft: false
categories:
  - Finance
  - Commerce
  - Infrastructure
---

Bitcredit est un système de financement commercial par effets de commerce électroniques pour les entreprises. Le site public présente Bitcredit Core comme un logiciel pour émettre, endosser, payer et gérer des lettres de change électroniques, tandis que le dépôt open-source implémente une couche de transport Nostr aux côtés de la logique métier et des crates de persistance.

## Comment ça fonctionne

Bitcredit modélise le crédit commercial sous forme de lettres de change électroniques, ou ebills. Un acheteur émet une ebill avec une date d'échéance future, le porteur peut l'endosser à une autre entreprise, et le porteur final peut demander le paiement à maturité.

Le site Bitcredit décrit également un chemin de liquidité basé sur un mint. Au lieu d'attendre l'échéance, un porteur peut demander une offre à un mint Bitcredit, recevoir de l'ecash immédiatement, puis utiliser cet ecash pour payer des fournisseurs ou des employés.

## Notes d'implémentation

Le dépôt `Bitcredit-Core` divise le système en plusieurs crates Rust. `bcr-ebill-core` gère le modèle de données, `bcr-ebill-api` contient la logique métier, `bcr-ebill-persistence` gère le stockage, et `bcr-ebill-transport` fournit l'API de transport réseau avec une implémentation Nostr.

Cette architecture est importante car Bitcredit n'est pas simplement un site web ou un flux de portefeuille. C'est un système de documents commerciaux avec transport, état et logique de règlement séparés en composants réutilisables, incluant un point d'entrée WASM pour les déploiements web.

## Travaux récents

Compass a couvert Bitcredit pour la première fois en mars 2026 lorsque `v0.5.3` a ajouté des champs API pour les actions de paiement et l'état des effets, et corrigé la gestion des adresses de signature pour les signataires anonymes. La version suivante, `v0.5.4`, a poursuivi ce travail d'API en adaptant `BitcreditBillResult`, en affinant l'état de paiement et d'acceptation, et en ajoutant une gestion plus explicite des champs optionnels.

Ces changements sont modestes par rapport au concept plus large de Bitcredit, mais ils montrent la direction de l'implémentation : une meilleure ergonomie frontend, un état de cycle de vie des effets plus clair, et une meilleure gestion des flux de signature anonymes ou au porteur.

---

**Sources principales :**
- [Site web Bitcredit](https://www.bit.cr/)
- [Bitcredit : Comment ça fonctionne](https://www.bit.cr/how-it-works)
- [Dépôt Bitcredit-Core](https://github.com/BitcreditProtocol/Bitcredit-Core)
- [Index de documentation Bitcredit-Core](https://github.com/BitcreditProtocol/Bitcredit-Core/blob/master/docs/index.md)
- [Bitcredit v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3)
- [Bitcredit v0.5.4](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.4)
- [PR #846 : Amélioration des drapeaux de statut et ajout des actions de paiement](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846)
- [PR #849 : Correction de l'adresse de signature et du signataire pour les signataires anonymes](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849)

**Mentionné dans :**
- [Newsletter #13 : Bitcredit v0.5.3](/en/newsletters/2026-03-11-newsletter/#bitcredit-v053)
