---
title: "NIP-07 : Signataire par extension navigateur"
date: 2026-01-28
translationOf: /en/topics/nip-07.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Signing
  - Security
---

NIP-07 définit une interface standard pour les extensions navigateur afin de fournir des capacités de signature aux clients Nostr basés sur le web, gardant les clés privées sécurisées dans l'extension plutôt que de les exposer aux sites web.

## Fonctionnement

Les extensions navigateur injectent un objet `window.nostr` que les applications web peuvent utiliser :

```javascript
// Obtenir la clé publique
const pubkey = await window.nostr.getPublicKey();

// Signer un événement
const signedEvent = await window.nostr.signEvent(unsignedEvent);

// Chiffrer (NIP-04, legacy)
const ciphertext = await window.nostr.nip04.encrypt(pubkey, plaintext);

// Déchiffrer (NIP-04, legacy)
const plaintext = await window.nostr.nip04.decrypt(pubkey, ciphertext);

// Méthodes NIP-44 (moderne, si supporté)
// const ciphertext = await window.nostr.nip44.encrypt(pubkey, plaintext);
// const plaintext = await window.nostr.nip44.decrypt(pubkey, ciphertext);
```

## Modèle de sécurité

- **Isolation des clés** : Les clés privées ne quittent jamais l'extension
- **Approbation utilisateur** : Les extensions peuvent demander confirmation pour chaque requête de signature
- **Contrôle de domaine** : Les extensions peuvent restreindre quels sites peuvent demander des signatures

## Implémentations

Les extensions NIP-07 populaires incluent :
- **Alby** - Portefeuille Lightning avec signature Nostr
- **nos2x** - Signataire Nostr léger
- **Flamingo** - Extension Nostr riche en fonctionnalités

## Limitations

- Navigateur uniquement (pas de support mobile)
- Nécessite l'installation d'une extension
- Chaque extension a une UX différente pour les approbations

## Alternatives

- [NIP-46](/fr/topics/nip-46/) - Signature à distance via les relais Nostr
- [NIP-55](/fr/topics/nip-55/) - Signataire local Android

## Voir aussi

- [NIP-44](/fr/topics/nip-44/) - Chiffrement moderne (remplaçant NIP-04)
- [NIP-46](/fr/topics/nip-46/) - Signature à distance
