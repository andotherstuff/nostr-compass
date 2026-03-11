---
title: "NIP-39 : Identités externes dans les profils"
date: 2026-02-11
translationOf: /en/topics/nip-39.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Identity
---

NIP-39 définit comment les utilisateurs attachent des revendications d'identité externes à leurs profils Nostr en utilisant des tags `i`. Ces tags relient une pubkey Nostr à des comptes sur des plateformes externes comme GitHub, Twitter, Mastodon ou Telegram.

## Comment cela fonctionne

Les utilisateurs publient des revendications d'identité dans des événements de kind 10011 sous forme de tags `i`. Chaque tag contient une valeur `platform:identity` ainsi qu'un pointeur de preuve qui permet à un client de vérifier la revendication :

```json
{
  "id": "5f1c7b7e2c6f3d4a9b0e6a2d8c1f7e3b4a6d9c0e1f2a3b4c5d6e7f8091a2b3c4",
  "pubkey": "3bf0c63fcb8d0d8b6a8fcb3c7f5cb2a972f8a0b5a3d6d8790bb2d4e4f0d6b1c2",
  "created_at": 1741699200,
  "kind": 10011,
  "tags": [
    ["i", "github:alice", "9f5df4e2a8b14c1f9e6d2b7c4a1e8f90"],
    ["i", "twitter:alice_dev", "1898123456789012345"]
  ],
  "content": "",
  "sig": "8f4c62d8a7e9b1c3d5f7091a2b4c6d8e0f1234567890abcdeffedcba09876543211223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

Les clients reconstruisent l'URL de preuve à partir de la plateforme et de la valeur de preuve, puis vérifient que la publication externe contient le `npub` de l'utilisateur. Cela garde la revendication portable entre clients sans exiger de vérificateur central.

## Modèle de preuve

Le détail important est que NIP-39 prouve le contrôle de deux identités à la fois : la clé Nostr et le compte externe. Si l'un des côtés de cette preuve disparaît, la vérification devient plus faible. Un gist ou un tweet supprimé n'invalide pas l'événement historique, mais il retire la preuve en direct dont la plupart des clients dépendent.

Un autre point d'implémentation utile concerne la stratégie de récupération. Comme les revendications vivent désormais hors du kind 0, les clients peuvent décider de ne les demander que dans les vues détaillées du profil, seulement pour les utilisateurs suivis, ou pas du tout. Cela évite d'ajouter du poids au chemin kind 0 déjà très sollicité.

## Implémentations

- [Amethyst PR #1747](https://github.com/vitorpamplona/amethyst/pull/1747) - Publie des identités externes comme événements kind 10011 dédiés
- [PR #2256](https://github.com/nostr-protocol/nips/pull/2256) - Ajoute une référence explicite au registre kind 10011 dans l'ensemble des NIPs

## État actuel

Selon la spécification actuelle, les revendications d'identité vivent dans des événements kind 10011 dédiés au lieu des métadonnées kind 0. Cette séparation vient de l'effort plus large visant à alléger les récupérations de profil kind 0.

---

**Sources principales :**
- [NIP-39 : External Identities in Profiles](https://github.com/nostr-protocol/nips/blob/master/39.md)
- [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) - Déplace les revendications d'identité hors du kind 0
- [PR #2256](https://github.com/nostr-protocol/nips/pull/2256) - Ajoute une référence explicite au kind 10011

**Mentionné dans :**
- [Newsletter #9 : Mises à jour des NIP](/fr/newsletters/2026-02-11-newsletter/#mises-à-jour-des-nip)
- [Newsletter #12 : Amethyst](/fr/newsletters/2026-03-04-newsletter/#amethyst)
- [Newsletter #13 : Mises à jour des NIP](/fr/newsletters/2026-03-11-newsletter/#mises-à-jour-des-nip)

**Voir aussi :**
- [NIP-05 : Vérification basée sur DNS](/fr/topics/nip-05/)
