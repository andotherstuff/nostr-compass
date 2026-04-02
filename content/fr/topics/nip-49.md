---
title: "NIP-49 : Chiffrement de clé privée"
date: 2026-03-11
translationOf: /en/topics/nip-49.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Key Management
  - Security
---

NIP-49 définit comment un client peut chiffrer la clé privée d'un utilisateur avec un mot de passe et encoder le résultat sous forme de chaîne `ncryptsec`. L'objectif est la portabilité avec des valeurs par défaut plus sûres que le stockage d'un `nsec` brut, tout en gardant la clé chiffrée facile à déplacer entre les clients.

## Comment ça fonctionne

Le client part de la clé privée secp256k1 brute de 32 octets, et non d'une chaîne hexadécimale ou bech32. Il dérive une clé symétrique temporaire à partir du mot de passe de l'utilisateur avec scrypt, en utilisant un sel aléatoire par clé et un facteur de travail ajustable stocké sous forme de `LOG_N`. Il chiffre ensuite la clé privée avec XChaCha20-Poly1305, ajoute en préfixe les métadonnées de versionnage et de gestion de clé, et encode le résultat en bech32 sous le préfixe `ncryptsec`.

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

L'événement ci-dessus est un exemple de conteneur, pas une exigence de NIP-49. NIP-49 standardise le format de clé chiffrée lui-même, pas un kind d'événement dédié pour le publier. Les clients peuvent stocker un `ncryptsec` localement, le synchroniser via un stockage spécifique à l'application, ou le présenter comme une exportation de sauvegarde.

## Modèle de sécurité

NIP-49 fait deux choses à la fois. Il transforme un mot de passe utilisateur en une véritable clé de chiffrement, et il ralentit les tentatives de récupération par force brute avec un KDF à mémoire élevée. Le facteur de travail compte. Des valeurs `LOG_N` plus élevées rendent le déchiffrement plus lent pour les utilisateurs légitimes, mais elles augmentent aussi le coût de la recherche hors ligne pour les attaquants.

Le format porte également un octet de drapeau décrivant si la clé a déjà été manipulée de manière non sécurisée avant le chiffrement. Cela ne change pas le texte chiffré lui-même, mais donne aux clients un moyen de distinguer une sauvegarde protégée nouvellement générée d'une clé qui a déjà été copiée-collée en clair avant d'être enveloppée.

## Notes d'implémentation

- Les mots de passe sont normalisés en Unicode NFKC avant la dérivation de clé afin que le même mot de passe puisse être saisi de manière cohérente entre les clients.
- XChaCha20-Poly1305 utilise un nonce de 24 octets et un chiffrement authentifié, de sorte que toute altération du texte chiffré échoue proprement lors du déchiffrement.
- La clé symétrique doit être mise à zéro et supprimée après utilisation.
- La spécification ne recommande pas de publier les clés chiffrées sur les relays publics, car la collecte de nombreuses clés chiffrées améliore la position de craquage hors ligne d'un attaquant.

## Implémentations

- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - Ajoute la compatibilité d'inscription utilisant les clés privées chiffrées NIP-49

---

**Sources principales :**
- [Spécification NIP-49](https://github.com/nostr-protocol/nips/blob/master/49.md)
- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - Flux d'inscription côté client utilisant NIP-49

**Mentionné dans :**
- [Newsletter #13 : Formstr](/en/newsletters/2026-03-11-newsletter/#formstr)
- [Newsletter #13 : NIP Deep Dive](/en/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-49-private-key-encryption)

**Voir aussi :**
- [NIP-46 : Nostr Connect](/fr/topics/nip-46/)
- [NIP-55 : Android Signer Application](/fr/topics/nip-55/)
