---
title: "Protocole Marmot"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---

Marmot est un protocole de messagerie de groupe chiffrée de bout en bout construit sur Nostr, utilisant le standard Message Layer Security (MLS) pour la confidentialité persistante et la sécurité post-compromission.

## Fonctionnement

Marmot étend Nostr avec le chiffrement basé sur MLS pour les discussions de groupe. Contrairement aux DMs NIP-17 qui sont un-à-un, Marmot gère la communication de groupe sécurisée où les membres peuvent rejoindre et quitter tout en maintenant les garanties de chiffrement.

## Fonctionnalités clés

- Confidentialité persistante et sécurité post-compromission via MLS
- Gestion des clés de groupe pour l'adhésion dynamique
- Notifications push préservant la vie privée via MIP-05

---

**Sources principales :**
- [Dépôt du protocole Marmot](https://github.com/marmot-protocol/marmot)

**Mentionné dans :**
- [Newsletter #1 : Actualités](/fr/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1 : Sorties](/fr/newsletters/2025-12-17-newsletter/#releases)

**Voir aussi :**
- [MIP-05 : Notifications push préservant la vie privée](/fr/topics/mip-05/)
- [NIP-17 : Messages directs privés](/fr/topics/nip-17/)
- [NIP-59 : Gift Wrap](/fr/topics/nip-59/)

