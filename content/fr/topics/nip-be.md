---
title: "NIP-BE : Bluetooth Low Energy"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Connectivity
---

NIP-BE spécifie comment les applications Nostr peuvent communiquer et se synchroniser via Bluetooth Low Energy, permettant aux applications capables de fonctionner hors ligne de synchroniser les données entre appareils à proximité sans connectivité Internet.

## Structure GATT

Utilise un Nordic UART Service avec deux caractéristiques :
- **Caractéristique d'écriture** - Le client envoie des données au serveur
- **Caractéristique de lecture** - Le serveur envoie des données au client (via notifications)

## Cadrage des messages

Le BLE a des limites de charge utile petites (20-256 octets selon la version), donc les messages sont :
- Compressés avec DEFLATE
- Divisés en morceaux avec un index de 2 octets et un flag de lot final
- Limités à une taille maximale de 64KB

## Négociation des rôles

Les appareils comparent les UUIDs annoncés lors de la découverte :
- L'UUID plus élevé devient le serveur GATT (rôle de relais)
- L'UUID plus bas devient le client GATT
- Des UUIDs prédéterminés existent pour les appareils à rôle unique

## Synchronisation

Utilise la communication semi-duplex avec les types de messages Nostr standard (`EVENT`, `EOSE`, `NEG-MSG`) pour coordonner la synchronisation des données à travers les connexions intermittentes.

## Cas d'utilisation

- Synchronisation d'événements hors ligne entre appareils à proximité
- Propagation de messages de type mesh sans Internet
- Connectivité de secours quand le réseau n'est pas disponible

---

**Sources principales :**
- [Spécification NIP-BE](https://github.com/nostr-protocol/nips/blob/master/BE.md)

**Mentionné dans :**
- [Newsletter #1 : Actualités](/fr/newsletters/2025-12-17-newsletter/#news)

