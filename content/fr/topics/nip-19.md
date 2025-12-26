---
title: "NIP-19 : Entités encodées en Bech32"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Identity
---

NIP-19 définit des formats conviviaux pour partager les identifiants Nostr. Ces chaînes encodées en bech32 sont utilisées pour l'affichage et le partage mais ne sont jamais utilisées dans le protocole lui-même (qui utilise l'hex).

## Pourquoi Bech32 ?

Les clés hex brutes sont sujettes aux erreurs de copie et visuellement indiscernables. L'encodage Bech32 ajoute un préfixe lisible par l'humain et une somme de contrôle, rendant immédiatement clair quel type de données vous regardez.

## Formats de base

Ceux-ci encodent des valeurs brutes de 32 octets :

- **npub** - Clé publique (votre identité, peut être partagée)
- **nsec** - Clé privée (gardez-la secrète, utilisée pour signer)
- **note** - ID d'événement (référence un événement spécifique)

Exemple : La clé publique hex `3bf0c63f...` devient `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`.

## Identifiants partageables

Ceux-ci utilisent l'encodage TLV (Type-Length-Value) pour inclure des métadonnées :

- **nprofile** - Profil avec indications de relais (aide les clients à trouver l'utilisateur)
- **nevent** - Événement avec indications de relais, clé publique de l'auteur et kind
- **naddr** - Référence d'événement adressable (clé publique + kind + tag d + relais)

Ceux-ci résolvent le problème de découverte : quand quelqu'un partage un ID de note, comment les clients savent quel relais l'a ? En regroupant les indications de relais dans l'identifiant, les liens partagés deviennent plus fiables.

## Notes d'implémentation

- Utilisez bech32 uniquement pour les interfaces humaines : affichage, copier/coller, codes QR, URLs
- N'utilisez jamais les formats bech32 dans les messages du protocole, événements ou réponses NIP-05
- Toute communication du protocole doit utiliser l'encodage hex
- Lors de la génération de nevent/nprofile/naddr, incluez les indications de relais pour une meilleure découvrabilité

---

**Sources principales :**
- [Spécification NIP-19](https://github.com/nostr-protocol/nips/blob/master/19.md)

**Mentionné dans :**
- [Newsletter #1 : Analyse approfondie NIP](/fr/newsletters/2025-12-17-newsletter/#nip-19-bech32-encoded-identifiers)

**Voir aussi :**
- [NIP-01 : Protocole de base](/fr/topics/nip-01/)
- [NIP-21 : Schéma URI nostr:](https://github.com/nostr-protocol/nips/blob/master/21.md)

