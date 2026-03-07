---
title: "NIP-BE : Bluetooth Low Energy"
date: 2025-12-17
translationOf: /en/topics/nip-be.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocole
  - Connectivité
---

NIP-BE spécifie comment les applications Nostr peuvent communiquer et se synchroniser via Bluetooth Low Energy, permettant aux applications capables de fonctionner hors ligne de synchroniser les données entre appareils à proximité sans connectivité Internet.

## Comment ça fonctionne

NIP-BE réutilise les trames de messages Nostr normales sur BLE au lieu d'inventer un modèle d'événement séparé. Les appareils annoncent un service BLE ainsi qu'un UUID d'appareil, comparent leurs UUID quand ils se rencontrent, puis décident de manière déterministe quel côté devient serveur GATT et quel côté devient client GATT.

Le service GATT adopte une forme proche de Nordic UART, avec une caractéristique d'écriture et une caractéristique de lecture/notification. Cela garde le transport assez simple pour des piles mobiles contraintes tout en transportant des messages Nostr ordinaires.

## Cadrage des messages

BLE a de petites limites de charge utile, donc NIP-BE compresse les messages avec DEFLATE, les découpe en fragments indexés et n'envoie qu'un message à la fois. La spécification limite les messages à 64 KB, ce qui rappelle utilement que ce transport vise la synchronisation et la propagation locale, pas le transfert de gros volumes.

## Modèle de synchronisation

Une fois la connexion établie, les pairs utilisent un flux de synchronisation semi-duplex fondé sur les messages de negentropy de [NIP-77](https://github.com/nostr-protocol/nips/blob/master/77.md), comme `NEG-OPEN`, `NEG-MSG`, `EVENT` et `EOSE`. Ce choix compte parce qu'il permet aux implémentations de réutiliser la logique de synchronisation de relay existante au lieu de construire un algorithme de réplication propre à BLE.

La règle du semi-duplex reflète aussi la réalité des liens BLE instables. Les connexions courtes et intermittentes à courte portée fonctionnent mieux quand chaque côté sait exactement à quel moment il doit parler.

## Pourquoi c'est important

NIP-BE donne aux applications Nostr une voie vers un réseau local-first. Deux téléphones peuvent synchroniser des notes ou l'état d'un relay directement quand ils sont proches, même si aucun des deux n'a d'accès Internet fonctionnel. Cela rend BLE utile pour la résistance à la censure, les scénarios de catastrophe et les applications sociales en faible connectivité.

Les contraintes comptent tout autant : la bande passante BLE est faible, les connexions sont de courte durée et les gros historiques s'y prêtent mal. En pratique, NIP-BE convient surtout à la synchronisation incrémentale et à la propagation locale de messages, pas à la réplication d'archives complètes.

---

**Sources principales :**
- [Spécification NIP-BE](https://github.com/nostr-protocol/nips/blob/master/BE.md)
- [PR #1979](https://github.com/nostr-protocol/nips/pull/1979)

**Mentionné dans :**
- [Newsletter #1 : Actualités](/fr/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #3 : Récapitulatif de Décembre](/fr/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Voir aussi :**
- [NIP-01 : Protocole de base](/fr/topics/nip-01/)
