---
title: "NIP-04 : Messages directs chiffrés (obsolète)"
date: 2025-12-31
translationOf: /en/topics/nip-04.md
translationDate: 2026-04-22
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-04 définit les messages directs chiffrés via les événements kind 4 et un secret partagé dérivé par ECDH. C'était le premier système de messagerie privée de Nostr, mais il s'agit désormais d'une technologie héritée, et le développement de la messagerie privée s'est déplacé vers NIP-17.

## Fonctionnement

Les messages utilisent des événements kind 4 selon le flux suivant :

1. L'expéditeur dérive un secret partagé avec secp256k1 ECDH.
2. Le texte en clair est chiffré avec AES-256-CBC.
3. L'événement inclut un tag `p` désignant le destinataire.
4. Le texte chiffré est encodé en base64 et stocké dans `content` avec le vecteur d'initialisation (IV).

L'événement lui-même reste un événement Nostr signé ordinaire, de sorte que les relais peuvent voir les métadonnées extérieures même s'ils ne peuvent pas lire le texte en clair.

## Limites de sécurité et de confidentialité

NIP-04 présente des lacunes significatives en matière de confidentialité :

- **Fuite de métadonnées** : la pubkey de l'expéditeur est publiquement visible sur chaque message
- **Pas de confidentialité de l'expéditeur** : tout le monde peut voir qui communique avec qui
- **Horodatages exacts** : les moments d'envoi ne sont pas randomisés
- **Gestion des clés non standard** : le schéma n'utilise que la coordonnée X du point ECDH, ce qui a compliqué la cohérence entre bibliothèques et laissé peu de marge pour l'évolution du protocole

La spécification avertit explicitement que le système « n'approche en rien l'état de l'art en matière de communication chiffrée ».

## Pourquoi il a été remplacé

NIP-04 chiffre le contenu des messages, mais ne masque pas le graphe social. Les opérateurs de relais peuvent toujours voir qui a envoyé l'événement, qui le reçoit et quand il a été publié. Ces métadonnées suffisent à cartographier les conversations sans déchiffrer la charge utile.

NIP-17 résout ce problème en combinant le chiffrement de charge utile NIP-44 avec l'enveloppement cadeau NIP-59, qui masque l'expéditeur vis-à-vis des relais et des observateurs. Les nouvelles implémentations devraient traiter NIP-04 comme réservé à la compatibilité.

## État de l'implémentation

Les clients et signataires hérités exposent toujours les méthodes encrypt/decrypt de NIP-04 parce que d'anciennes conversations et applications plus anciennes sont encore en circulation. Cette couche de compatibilité est importante pour la migration, mais construire de nouvelles fonctionnalités sur les événements kind 4 revient généralement à perpétuer les anciennes limites de confidentialité.

---

**Sources principales :**
- [Spécification NIP-04](https://github.com/nostr-protocol/nips/blob/master/04.md)

**Mentionné dans :**
- [Newsletter #4 : NIP Deep Dive](/fr/newsletters/2026-01-07-newsletter/)
- [Newsletter #3 : Récapitulatif de décembre](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #19 : migration NIP-44 de nostter](/en/newsletters/2026-04-22-newsletter/)

**Voir aussi :**
- [NIP-44 : Charges utiles chiffrées](/fr/topics/nip-44/)
- [NIP-17 : Messages directs privés](/fr/topics/nip-17/)
- [NIP-59 : Gift Wrap](/fr/topics/nip-59/)
