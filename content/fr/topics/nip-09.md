---
title: "NIP-09 : Demande de suppression d'événement"
date: 2026-02-25
translationOf: /en/topics/nip-09.md
translationDate: 2026-03-07
draft: false
categories:
  - Moderation
  - Protocol
---

NIP-09 définit un moyen pour les auteurs de demander la suppression d'événements qu'ils ont précédemment publiés. Il s'agit d'un signal de suppression côté relais, pas d'une fonction d'effacement à l'échelle du réseau.

## Fonctionnement

Les utilisateurs publient des événements kind 5 contenant des références aux événements qu'ils souhaitent supprimer. Les relais qui supportent NIP-09 devraient cesser de servir les événements correspondants du même auteur et peuvent les retirer du stockage.

La suppression est une demande, pas une garantie. Les relais peuvent ignorer les demandes de suppression, et les événements peuvent avoir déjà été propagés vers des relais qui ne supportent pas la suppression. Les utilisateurs ne devraient pas compter sur NIP-09 pour la suppression de contenu sensible du point de vue de la confidentialité.

## Pourquoi c'est important

NIP-09 offre aux clients et aux relais un moyen commun d'exprimer « cet événement ne devrait plus apparaître », ce qui est utile pour les publications accidentelles, le renouvellement d'état de portefeuille et les flux de modération. Mais l'auteur ne peut demander la suppression que de ses propres événements. Ce n'est pas un mécanisme de retrait généralisé pour le contenu de tiers.

## Compromis

Le point faible est la propagation. Une fois qu'un événement a été répliqué sur plusieurs relais, la suppression fonctionne au mieux. Certains relais le supprimeront, d'autres le marqueront comme supprimé, et d'autres continueront à le servir indéfiniment. Les clients qui présentent la suppression comme définitive exagèrent ce que le protocole garantit.

Un autre problème pratique est celui des références. Les utilisateurs et applications peuvent encore détenir l'événement supprimé localement, ou le citer ailleurs, même après qu'un relais conforme a cessé de le servir.

---

**Sources principales :**
- [Spécification NIP-09](https://github.com/nostr-protocol/nips/blob/master/09.md)

**Mentionné dans :**
- [Newsletter #11 : NIP-60 Deep Dive](/en/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-60-cashu-wallet)
- [Newsletter #12 : News](/en/newsletters/2026-03-04-newsletter/#news)

**Voir aussi :**
- [NIP-01 : Protocole de base](/fr/topics/nip-01/)
- [NIP-60 : Cashu Wallet](/fr/topics/nip-60/)
