---
title: "NIP-09"
date: 2026-02-25
translationOf: /en/topics/nip-09.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - Protocol
---

NIP-09 définit Event Deletion, un mécanisme permettant aux utilisateurs de demander que les relays suppriment leurs événements précédemment publiés.

## Comment ça fonctionne

Les utilisateurs publient des événements kind 5 contenant des tags `e` référençant les IDs d'événements qu'ils souhaitent supprimer. Les relays qui supportent NIP-09 devraient cesser de servir les événements référencés et peuvent les supprimer du stockage.

La suppression est une requête, pas une garantie. Les relays peuvent ignorer les requêtes de suppression, et les événements peuvent avoir déjà propagé vers des relays qui ne supportent pas la suppression. Les utilisateurs ne devraient pas compter sur NIP-09 pour la suppression de contenu sensible à la confidentialité.

## Fonctionnalités clés

- Événements de requête de suppression kind 5
- Référencement des événements supprimés par ID via tags e
- Champ de raison optionnel pour le contexte de suppression
- La conformité du relay est volontaire

---

**Sources principales :**
- [Spécification NIP-09](https://github.com/nostr-protocol/nips/blob/master/09.md)

**Mentionné dans :**
- [Newsletter #11 : Approfondissement NIP-60](/fr/newsletters/2026-02-25-newsletter/#approfondissement-nip--nip-60-cashu-wallet)

**Voir aussi :**
- [NIP-60 : Cashu Wallet](/fr/topics/nip-60/)
