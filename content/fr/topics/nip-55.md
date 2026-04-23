---
title: "NIP-55 : Application de signature Android"
date: 2025-12-17
translationOf: /en/topics/nip-55.md
translationDate: 2026-04-22
draft: false
categories:
  - Signing
  - Mobile
---

NIP-55 définit comment les applications Android demandent des opérations de signature et de chiffrement à une application de signature séparée. Il offre aux clients Android une alternative native aux extensions de navigateur et aux bunkers distants.

## Fonctionnement

NIP-55 utilise deux mécanismes Android :

- **Intents** pour les flux en avant-plan avec approbation explicite de l'utilisateur
- **Content resolvers** pour les flux en arrière-plan après que l'utilisateur a accordé une permission persistante

Le flux de connexion habituel commence par `get_public_key`. Le signataire retourne la clé publique de l'utilisateur et le nom du package du signataire, et le client est censé mettre les deux en cache. Répéter `get_public_key` dans des boucles en arrière-plan est une erreur d'implémentation courante contre laquelle la spécification met explicitement en garde.

## Opérations clés

- **get_public_key** - Récupérer la clé publique de l'utilisateur et le nom du package du signataire
- **sign_event** - Signer un événement Nostr
- **nip04_encrypt/decrypt** - Chiffrer ou déchiffrer les messages NIP-04
- **nip44_encrypt/decrypt** - Chiffrer ou déchiffrer les messages NIP-44
- **decrypt_zap_event** - Déchiffrer les charges utiles d'événements liés aux zaps

## Notes de sécurité et d'UX

NIP-55 garde les clés sur l'appareil, mais dépend toujours des frontières d'application Android et de la gestion des permissions du signataire. Le support des content resolvers offre une UX bien plus fluide que les demandes répétées via intents, mais uniquement après que l'utilisateur a accordé une approbation durable à ce client.

Pour les applications web sur Android, NIP-55 est moins ergonomique que NIP-46. Les flux basés sur le navigateur ne peuvent pas recevoir de réponses directes en arrière-plan comme le font les applications Android natives, de sorte que de nombreuses implémentations se rabattent sur les URLs de callback, le transfert par presse-papiers ou le collage manuel.

---

**Sources principales :**
- [NIP-55 Specification](https://github.com/nostr-protocol/nips/blob/master/55.md)

**Mentionné dans :**
- [Newsletter #1 : Releases](/fr/newsletters/2025-12-17-newsletter/)
- [Newsletter #2 : News](/fr/newsletters/2025-12-24-newsletter/)
- [Newsletter #2 : NIP Updates](/fr/newsletters/2025-12-24-newsletter/)
- [Newsletter #3 : December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #7 : NIP Updates](/fr/newsletters/2026-01-07-newsletter/)
- [Newsletter #11 : NIP Deep Dive](/fr/newsletters/2026-02-25-newsletter/)

**Voir aussi :**
- [NIP-46 : Nostr Connect](/fr/topics/nip-46/)
