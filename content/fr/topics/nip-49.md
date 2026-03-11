---
title: "NIP-49 : Chiffrement de clé privée"
date: 2026-03-11
translationOf: /en/topics/nip-49.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Key Management
  - Security
---

NIP-49 définit comment un client peut chiffrer la clé privée d'un utilisateur avec un mot de passe et encoder le résultat sous forme de chaîne `ncryptsec`. L'objectif est la portabilité avec des valeurs par défaut plus solides que le stockage d'un `nsec` brut, tout en gardant la clé chiffrée facile à déplacer entre clients.

## Comment cela fonctionne

Le client part de la clé privée secp256k1 brute de 32 octets, et non d'une chaîne hex ou bech32. Il dérive une clé symétrique temporaire à partir du mot de passe de l'utilisateur avec scrypt, en utilisant un salt aléatoire par clé et un facteur de travail ajustable stocké comme `LOG_N`. Il chiffre ensuite la clé privée avec XChaCha20-Poly1305, préfixe le résultat avec des métadonnées de version et de manipulation de clé, puis l'encode en bech32 sous le préfixe `ncryptsec`.

```json
{
  "id": "4d47f4f0a6f6edbc1bbd7f4e2a45ec68f27cba91d6c6ab5cf28d8d87b0f3d57e",
  "pubkey": "1f8b4c3e7b0f9451d4f9b8a7c6e5d4c3b2a1908f7e6d5c4b3a29181716151413",
  "created_at": 1741699200,
  "kind": 30078,
  "tags": [
    ["d", "encrypted-key-backup"],
    ["format", "ncryptsec"],
    ["encryption", "nip49"]
  ],
  "content": "ncryptsec1qgg9947rlpvqu76pj5ecreduf9jxhselq2nae2kghhvd5g7dgjtcxfqtd67p9m0w57lspw8gsq6yphnm8623nsl8xn9j4jdzz84zm3frztj3z7s35vpzmqf6ksu8r89qk5z2zxfmu5gv8th8wclt0h4p",
  "sig": "6a8f6e4b2d1901735f0ad4b6e8c1f3a579d0e2b4c6f8a1d3e5f7091b2c3d4e5f11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

L'événement ci-dessus est un conteneur d'exemple, pas une exigence de NIP-49. NIP-49 standardise le format de clé chiffrée lui-même, pas un kind d'événement dédié pour la publier. Les clients peuvent stocker un `ncryptsec` localement, le synchroniser via un stockage spécifique à l'application ou le présenter comme export de sauvegarde.

## Modèle de sécurité

NIP-49 fait deux choses à la fois. Il transforme un mot de passe utilisateur en véritable clé de chiffrement et il ralentit les tentatives de récupération par force brute avec une KDF memory-hard. Le facteur de travail compte. Des valeurs `LOG_N` plus élevées ralentissent le déchiffrement pour les utilisateurs légitimes, mais elles augmentent aussi le coût des tentatives hors ligne pour les attaquants.

Le format transporte aussi un indicateur d'un octet décrivant si la clé a déjà été manipulée de manière non sûre avant le chiffrement. Cela ne change pas le ciphertext lui-même, mais cela donne aux clients un moyen de distinguer une sauvegarde protégée nouvellement générée d'une clé qui avait déjà été copiée en clair avant d'être encapsulée.

## Notes d'implémentation

- Les mots de passe sont normalisés en Unicode NFKC avant la dérivation de clé afin que le même mot de passe puisse être saisi de manière cohérente entre clients.
- XChaCha20-Poly1305 utilise un nonce de 24 octets et un chiffrement authentifié, donc toute altération du ciphertext échoue proprement lors du déchiffrement.
- La clé symétrique doit être effacée et supprimée après usage.
- La spécification ne recommande pas de publier des clés chiffrées sur des relays publics, car collecter de nombreuses clés chiffrées améliore la position d'un attaquant pour le cassage hors ligne.

## Implémentations

- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - Ajoute la compatibilité d'inscription avec des clés privées chiffrées NIP-49

---

**Sources principales :**
- [Spécification NIP-49](https://github.com/nostr-protocol/nips/blob/master/49.md)
- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - Flux d'inscription côté client utilisant NIP-49

**Mentionné dans :**
- [Newsletter #13 : Formstr](/fr/newsletters/2026-03-11-newsletter/#formstr)
- [Newsletter #13 : NIP Deep Dive](/fr/newsletters/2026-03-11-newsletter/#analyse-approfondie-du-nip-nip-49-chiffrement-de-clé-privée)

**Voir aussi :**
- [NIP-46 : Nostr Connect](/fr/topics/nip-46/)
- [NIP-55 : Application de signature Android](/fr/topics/nip-55/)
