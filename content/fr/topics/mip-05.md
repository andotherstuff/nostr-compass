---
title: "MIP-05 : Notifications push préservant la vie privée"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Messaging
  - Protocol
---

MIP-05 définit un protocole pour les notifications push qui maintiennent la vie privée des utilisateurs, résolvant le problème que les systèmes push traditionnels exigent que les serveurs connaissent les jetons d'appareil et les identités des utilisateurs.

## Fonctionnement

- Les jetons d'appareil sont chiffrés avec ECDH+HKDF et ChaCha20-Poly1305
- Les clés éphémères empêchent la corrélation entre les notifications
- Un protocole de propagation à trois événements (kinds 447-449) synchronise les jetons chiffrés entre les membres du groupe
- Les jetons leurres via l'emballage cadeau NIP-59 cachent la taille des groupes

## Garanties de confidentialité

- Les serveurs de notifications push ne peuvent pas identifier les utilisateurs
- L'appartenance au groupe n'est pas révélée par les modèles de notification
- Les jetons d'appareil ne peuvent pas être corrélés entre les messages

## Kinds d'événements

- **Kind 447** : Publication de jeton d'appareil chiffré
- **Kind 448** : Demande de synchronisation de jeton
- **Kind 449** : Réponse de synchronisation de jeton

---

**Sources principales :**
- [PR MIP-05](https://github.com/marmot-protocol/marmot/pull/18)

**Mentionné dans :**
- [Newsletter #1 : Actualités](/fr/newsletters/2025-12-17-newsletter/#news)

**Voir aussi :**
- [Protocole Marmot](/fr/topics/marmot/)
- [NIP-59 : Gift Wrap](/fr/topics/nip-59/)

