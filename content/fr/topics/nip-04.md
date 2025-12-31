---
title: "NIP-04 : Messages Directs Chiffrés (Obsolète)"
date: 2025-12-31
translationOf: /en/topics/nip-04.md
translationDate: 2025-12-31
draft: false
categories:
  - Confidentialité
  - Messagerie
---

NIP-04 définit les messages directs chiffrés utilisant le chiffrement AES-256-CBC. C'était la méthode originale pour la messagerie privée sur Nostr, mais elle a été dépréciée en faveur de NIP-17 en raison de limitations significatives en matière de confidentialité.

## Fonctionnement

Les messages utilisent des événements de kind 4 avec le schéma de chiffrement suivant :
1. Un secret partagé est généré en utilisant ECDH avec la clé publique du destinataire et la clé privée de l'expéditeur
2. Le message est chiffré avec AES-256-CBC
3. Le texte chiffré est encodé en base64 avec le vecteur d'initialisation ajouté
4. Un tag `p` identifie la clé publique du destinataire

## Limitations de sécurité

NIP-04 présente des lacunes significatives en matière de confidentialité :

- **Fuite de métadonnées** - La pubkey de l'expéditeur est publiquement visible sur chaque message
- **Pas de confidentialité de l'expéditeur** - N'importe qui peut voir qui envoie des messages à qui
- **Horodatages exacts** - Le timing des messages n'est pas randomisé
- **Implémentation non standard** - Utilise uniquement la coordonnée X du point ECDH plutôt que le hash SHA256 standard

La spécification avertit explicitement qu'elle "n'approche pas l'état de l'art en matière de communication chiffrée".

## Statut de dépréciation

NIP-04 est obsolète en faveur de NIP-17, qui utilise l'emballage cadeau (gift wrapping) de NIP-59 pour masquer l'identité de l'expéditeur. Les nouvelles implémentations devraient utiliser NIP-17 pour la messagerie privée.

---

**Sources principales :**
- [Spécification NIP-04](https://github.com/nostr-protocol/nips/blob/master/04.md)

**Mentionné dans :**
- [Newsletter #3 : Récapitulatif de Décembre](/fr/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Voir aussi :**
- [NIP-17 : Messages Directs Privés](/fr/topics/nip-17/)
- [NIP-59 : Gift Wrap](/fr/topics/nip-59/)
