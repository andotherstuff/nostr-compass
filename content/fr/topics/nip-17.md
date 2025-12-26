---
title: "NIP-17 : Messages directs privés"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-17 définit les messages directs privés utilisant l'emballage cadeau NIP-59 pour la confidentialité de l'expéditeur. Contrairement aux DMs NIP-04 qui exposent l'expéditeur, les messages NIP-17 cachent qui a envoyé le message. Le destinataire reste visible dans l'emballage cadeau externe.

## Fonctionnement

Les messages sont enveloppés dans plusieurs couches de chiffrement :
1. Le contenu réel du message (kind 14)
2. Un sceau qui chiffre le contenu pour le destinataire
3. Un emballage cadeau qui cache l'identité de l'expéditeur

L'emballage cadeau externe utilise une paire de clés jetables aléatoire pour que les relais et observateurs ne puissent pas déterminer qui a envoyé le message.

## Structure du message

- **Kind 14** - Le contenu réel du DM (à l'intérieur du sceau)
- Utilise le chiffrement NIP-44 pour le contenu
- Supporte les réactions (kind 7) dans les conversations DM

## Garanties de confidentialité

- Les relais ne peuvent pas voir l'expéditeur (caché par la paire de clés jetable de l'emballage cadeau)
- Le destinataire est visible (dans le tag `p` de l'emballage cadeau)
- Les horodatages des messages sont randomisés dans une fenêtre
- Pas de threading ou regroupement de conversation visible sur le relais

## Comparaison avec NIP-04

Les DMs NIP-04 chiffrent le contenu mais laissent les métadonnées visibles :
- La clé publique de l'expéditeur est publique
- La clé publique du destinataire est dans le tag `p`
- Les horodatages sont exacts

NIP-17 cache l'expéditeur au prix d'une implémentation plus complexe.

---

**Sources principales :**
- [Spécification NIP-17](https://github.com/nostr-protocol/nips/blob/master/17.md)

**Mentionné dans :**
- [Newsletter #1 : Mises à jour NIP](/fr/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #2 : Actualités](/fr/newsletters/2025-12-24-newsletter/#news)

**Voir aussi :**
- [NIP-59 : Gift Wrap](/fr/topics/nip-59/)

