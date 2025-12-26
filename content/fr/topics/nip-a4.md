---
title: "NIP-A4 : Messages publics"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
---

NIP-A4 définit les messages publics (kind 24) conçus pour les écrans de notification, avec un support client large comme objectif.

## Fonctionnement

Contrairement aux conversations threadées, ces messages n'ont pas de concept d'historique de chat ou de chaînes de messages. Ce sont de simples messages ponctuels destinés à apparaître dans le flux de notifications d'un destinataire.

## Structure

- Utilise des tags `q` (citations) plutôt que des tags `e` pour éviter les complications de threading
- Pas d'état de conversation ni d'historique
- Conçu pour des notifications publiques simples

## Cas d'utilisation

- Reconnaissances publiques ou mentions
- Messages diffusés à un utilisateur
- Notifications qui n'ont pas besoin de threading de réponse

---

**Sources principales :**
- [PR NIP-A4](https://github.com/nostr-protocol/nips/pull/1988)

**Mentionné dans :**
- [Newsletter #2 : Mises à jour NIP](/fr/newsletters/2025-12-24-newsletter/#nip-updates)

**Voir aussi :**
- [NIP-01 : Protocole de base](/fr/topics/nip-01/)
- [NIP-10 : Threading des notes textuelles](/fr/topics/nip-10/)

