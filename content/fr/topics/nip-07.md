---
title: "NIP-07 : Signataire par extension navigateur"
date: 2026-01-28
translationOf: /en/topics/nip-07.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - Signing
  - Security
---

NIP-07 définit une interface standard permettant aux extensions navigateur de fournir des capacités de signature aux clients Nostr web, en gardant les clés privées en sécurité dans l'extension plutôt que de les exposer aux sites web.

## Fonctionnement

Les extensions navigateur injectent un objet `window.nostr` que les applications web peuvent utiliser :

```javascript
// Obtenir la clé publique
const pubkey = await window.nostr.getPublicKey();

// Signer un événement
const signedEvent = await window.nostr.signEvent(unsignedEvent);

// Chiffrer (NIP-04, hérité)
const ciphertext = await window.nostr.nip04.encrypt(pubkey, plaintext);

// Déchiffrer (NIP-04, hérité)
const plaintext = await window.nostr.nip04.decrypt(pubkey, ciphertext);

// Méthodes NIP-44 (modernes, si supportées)
// const ciphertext = await window.nostr.nip44.encrypt(pubkey, plaintext);
// const plaintext = await window.nostr.nip44.decrypt(pubkey, ciphertext);
```

## Modèle de sécurité

- **Isolation des clés** : les clés privées ne quittent jamais l'extension
- **Approbation utilisateur** : les extensions peuvent demander confirmation pour chaque requête de signature
- **Contrôle par domaine** : les extensions peuvent restreindre quels sites peuvent demander des signatures

NIP-07 améliore la garde des clés, mais ne supprime pas la confiance envers l'extension elle-même. Une extension malveillante ou compromise peut toujours signer la mauvaise chose, fuiter des métadonnées ou accorder des permissions trop larges.

## Notes d'interopérabilité

La difficulté principale de NIP-07 n'est pas la forme de l'API, mais la variation des capacités. Certaines extensions ne supportent que `getPublicKey()` et `signEvent()`. D'autres exposent aussi `nip04`, `nip44` ou des méthodes optionnelles plus récentes. Les applications web ont besoin de détection de fonctionnalités et de replis raisonnables plutôt que de supposer que chaque signataire injecté se comporte de la même manière.

L'expérience d'approbation utilisateur modifie aussi le comportement. Un site qui attend silencieusement un accès en arrière-plan peut fonctionner avec une extension et sembler cassé avec une autre qui demande confirmation à chaque requête. Les bonnes applications NIP-07 traitent la signature comme une frontière de permission interactive.

## État de l'implémentation

Les extensions NIP-07 populaires incluent :
- **Alby** : portefeuille Lightning avec signature Nostr
- **nos2x** : signataire Nostr léger
- **Flamingo** : extension Nostr riche en fonctionnalités

## Limites

- Navigateur uniquement (pas de support mobile)
- Nécessite l'installation d'une extension
- Chaque extension a une expérience d'approbation différente

Pour la signature multi-appareils ou mobile, NIP-46 et NIP-55 sont généralement plus adaptés.

---

**Sources principales :**
- [Spécification NIP-07](https://github.com/nostr-protocol/nips/blob/master/07.md)
- [PR #2233](https://github.com/nostr-protocol/nips/pull/2233) - proposition `peekPublicKey()`

**Mentionné dans :**
- [Newsletter #7 : NIP Updates](/fr/newsletters/2026-01-28-newsletter/#nip-updates)
- [Newsletter #8 : News](/fr/newsletters/2026-02-04-newsletter/#news)
- [Newsletter #11 : News](/fr/newsletters/2026-02-25-newsletter/#news)

**Voir aussi :**
- [NIP-04 : Messages directs chiffrés (obsolète)](/fr/topics/nip-04/)
- [NIP-44 : Charges utiles chiffrées](/fr/topics/nip-44/)
- [NIP-46 : Nostr Connect](/fr/topics/nip-46/)
- [NIP-55 : Applications de signature Android](/fr/topics/nip-55/)
