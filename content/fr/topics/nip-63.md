---
title: "NIP-63 : Paywall / Contenu premium"
date: 2025-12-17
translationOf: /en/topics/nip-63.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Monetization
---

NIP-63 est un standard proposé pour la gestion du contenu à accès restreint dans le protocole Nostr, permettant aux créateurs d'exiger un paiement avant de révéler le contenu.

## Fonctionnement

Les créateurs de contenu peuvent publier des événements où le contenu complet est chiffré ou caché derrière un paywall. Après vérification du paiement, le contenu est déverrouillé pour l'utilisateur payant.

La proposition porte intentionnellement sur la surface protocolaire du contenu premium, pas sur l'imposition d'un seul rail de paiement ou modèle commercial. Cela la garde flexible, mais signifie aussi que les portefeuilles, les clients et les éditeurs doivent encore s'accorder sur le flux de déverrouillage en pratique.

## Pourquoi c'est important

Sans un format partagé, chaque système de paywall Nostr devient son propre silo. Un NIP commun permettrait à un client de publier du contenu premium et à un autre client de comprendre que le contenu est restreint, ce qu'il faut payer, et quand il doit être révélé.

Cela ne garantit pas encore la portabilité. NIP-63 est toujours une proposition dans le [PR #2156](https://github.com/nostr-protocol/nips/pull/2156), donc les implémentations peuvent encore diverger pendant que la conception est en discussion.

## Cas d'utilisation

- Articles réservés aux abonnés
- Contenu média premium
- Événements en paiement à la séance
- Accès exclusif aux créateurs

## Compromis

Les métadonnées de paywall peuvent être publiques même lorsque la charge utile premium ne l'est pas. Cela donne aux clients assez d'informations pour présenter une offre, mais cela signifie aussi que l'existence du contenu payant est visible par quiconque peut lire l'événement.

Les créateurs doivent aussi réfléchir à ce qui se passe après le déverrouillage. Une fois le texte brut montré à un utilisateur payant, le protocole ne peut pas empêcher cet utilisateur de le copier ailleurs.

---

**Sources principales :**
- [Proposition NIP-63 (PR #2156)](https://github.com/nostr-protocol/nips/pull/2156)

**Mentionné dans :**
- [Newsletter #1 : Mises à jour NIP](/en/newsletters/2025-12-17-newsletter/#nip-updates)

**Voir aussi :**
- [NIP-57 : Zaps](/fr/topics/nip-57/)
