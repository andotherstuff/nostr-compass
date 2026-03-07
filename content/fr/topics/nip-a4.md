---
title: "NIP-A4 : Messages publics"
date: 2025-12-24
translationOf: /en/topics/nip-a4.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocole
  - Social
---

NIP-A4 définit les messages publics (kind 24) conçus pour les écrans de notification, avec un large support client comme objectif.

## Fonctionnement

Le kind `24` est un message signé en texte clair adressé à un ou plusieurs destinataires. Le corps du message se trouve dans `content`, et les tags `p` identifient les destinataires visés. La spécification indique que les clients devraient envoyer ces événements vers les inbox relays des destinataires définis par [NIP-65](/fr/topics/nip-65/) ainsi que vers l'outbox relay de l'émetteur.

Contrairement aux conversations threadées, ces messages n'ont pas de notion d'historique de chat, d'état de salon ni de racine de thread. Ils sont faits pour apparaître dans une surface de notification et rester compréhensibles seuls.

## Règles du protocole

- Utilise des tags `p` pour identifier les destinataires
- Ne doit pas utiliser de tags `e` pour le threading
- Peut utiliser des tags `q` pour citer un autre événement
- Fonctionne mieux avec les tags d'expiration [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md) afin que les messages de type notification disparaissent avec le temps

## Pourquoi il existe

NIP-A4 donne aux clients une primitive de message public plus simple qu'une note threadée complète. C'est utile pour des messages de type mention, des salutations publiques légères ou des notifications ponctuelles, quand construire un arbre de conversation durable ajouterait plus de complexité que de valeur.

Le compromis, c'est que ces messages sont publics. Ils sont faciles à afficher dans une interface de notification justement parce qu'ils ne créent pas d'état de session privé. N'importe qui peut les lire et y répondre s'il les voit.

## Notes d'interopérabilité

NIP-A4 peut être confondu avec des protocoles de messages directs parce qu'il vise des destinataires nommés, mais il reste un kind d'événement public. Les clients ne devraient pas présenter le kind `24` comme une messagerie privée ni supposer une quelconque confidentialité au-delà du choix des relays.

---

**Sources principales :**
- [Spécification NIP-A4](https://github.com/nostr-protocol/nips/blob/master/A4.md)
- [PR NIP-A4](https://github.com/nostr-protocol/nips/pull/1988)

**Mentionné dans :**
- [Newsletter #2 : Mises à jour NIP](/fr/newsletters/2025-12-24-newsletter/#nip-updates)
- [Newsletter #3 : Récapitulatif de Décembre](/fr/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Voir aussi :**
- [NIP-01 : Protocole de base](/fr/topics/nip-01/)
- [NIP-10 : Threading des notes textuelles](/fr/topics/nip-10/)
