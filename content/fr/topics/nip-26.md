---
title: "NIP-26 : Signature déléguée des events"
date: 2026-09-30
draft: false
categories:
  - NIPs
  - Identity
translationOf: /en/topics/nip-26.md
translationDate: 2026-10-01
---

NIP-26 décrit une méthode permettant à une clé Nostr d'autoriser une autre clé à signer un ensemble limité d'events. Sa spécification actuelle porte les mentions **brouillon** et **déconseillé** ; elle consigne donc une conception antérieure plutôt que des recommandations pour une nouvelle intégration.

## Fonctionnement

La clé du compte signe un jeton de délégation qui désigne la clé déléguée et les conditions. Ces conditions peuvent restreindre les kinds des events et les valeurs de `created_at`. Le délégataire signe l'event avec sa propre clé et joint le jeton dans un tag `delegation`. Le lecteur doit vérifier à la fois la signature de l'event et le jeton de délégation au regard de ces conditions. Les relays qui prennent en charge ce mécanisme peuvent également effectuer des recherches par délégant.

Ce modèle permet à une application de publier sans détenir la clé de signature principale du compte. Ses exigences supplémentaires en matière de validation et de recherche sur les relays expliquent pourquoi les implémentations ne peuvent pas considérer une signature d'event ordinaire comme une preuve suffisante d'une identité déléguée. La [spécification actuelle](https://github.com/nostr-protocol/nips/blob/master/26.md) indique explicitement que cette approche est déconseillée.

---

**Sources primaires :**
- [Spécification NIP-26 et statut actuel](https://github.com/nostr-protocol/nips/blob/master/26.md)
- [Texte de septembre 2022 sur la signature déléguée](https://github.com/nostr-protocol/nips/commit/b62aa418d)

**Mentionné dans :**
- [Lettre d'information n° 42 : septembre 2022](/fr/newsletters/2026-09-30-newsletter/#september-2022-chat-and-delegated-actions-enter-the-specifications)
