---
title: "NIP-70 : Événements protégés"
date: 2026-03-11
translationOf: /en/topics/nip-70.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Relay
  - Access Control
---

NIP-70 définit un moyen pour les auteurs de marquer un événement comme protégé avec le simple tag `[["-"]]`. Un événement protégé ne peut être accepté que lorsqu'un relay choisit de supporter ce comportement et vérifie que le publisher authentifié est la même pubkey que l'auteur de l'événement.

## Comment cela fonctionne

La règle centrale est courte. Si un événement contient le tag `[["-"]]`, un relay doit le rejeter par défaut. Un relay qui veut supporter les événements protégés doit d'abord exécuter le flux `AUTH` de [NIP-42](/fr/topics/nip-42/) et confirmer que le client authentifié publie son propre événement.

Cela fait de NIP-70 une règle d'autorité de publication, et non une règle de chiffrement. Le contenu peut rester lisible. Ce qui change, c'est qui a le droit de placer cet événement sur un relay qui respecte le tag. Cela permet aux relays de supporter des flux semi-fermés et d'autres contextes où les auteurs veulent qu'un relay refuse la republication par des tiers.

```json
{
  "id": "cb8feca582979d91fe90455867b34dbf4d65e4b86e86b3c68c368ca9f9eef6f2",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1707409439,
  "kind": 1,
  "tags": [
    ["-"]
  ],
  "content": "hello members of the secret group",
  "sig": "fa163f5cfb75d77d9b6269011872ee22b34fb48d23251e9879bb1e4ccbdd8aaaf4b6dc5f5084a65ef42c52fbcde8f3178bac3ba207de827ec513a6aa39fa684c"
}
```

## Implications du flux AUTH

Les événements protégés ne sont utiles que lorsque les relays appliquent réellement l'identité de l'auteur au moment de la publication. C'est pourquoi NIP-70 dépend si directement de [NIP-42](/fr/topics/nip-42/). Un relay qui accepte des événements `[["-"]]` sans vérification d'auth correspondante traite le tag comme une décoration, pas comme une politique.

## Comportement et limites des relays

NIP-70 ne promet pas que le contenu restera confiné pour toujours. Tout destinataire peut encore copier ce qu'il voit et publier un nouvel événement ailleurs. La spécification ne donne aux relays qu'une manière standard de respecter l'intention de l'auteur et de rejeter la republication directe d'événements protégés.

C'est pour cela que le travail de suivi compte. [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) étend la règle aux reposts qui intègrent des événements protégés, fermant un contournement simple où l'événement d'origine restait protégé mais pas l'événement enveloppe.

## Implémentations

- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - Ajoute le support de l'auth NIP-42 pour les événements protégés
- [strfry PR #176](https://github.com/hoytech/strfry/pull/176) - Rejette les reposts qui intègrent des événements protégés
- [SNSTR v0.3.3](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.3) - Ajoute un support utilitaire lié à la gestion des événements protégés

---

**Sources principales :**
- [Spécification NIP-70](https://github.com/nostr-protocol/nips/blob/master/70.md)
- [PR #1030](https://github.com/nostr-protocol/nips/pull/1030) - Ajoute NIP-70 au dépôt NIPs
- [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) - Rejeter les reposts qui intègrent des événements protégés
- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - Implémentation relay pour l'auth NIP-42 et les événements protégés

**Mentionné dans :**
- [Newsletter #13 : NIP Updates](/fr/newsletters/2026-03-11-newsletter/#mises-à-jour-des-nip)
- [Newsletter #13 : NIP Deep Dive](/fr/newsletters/2026-03-11-newsletter/#analyse-approfondie-du-nip-nip-70-événements-protégés)

**Voir aussi :**
- [NIP-42 : Authentification du client](/fr/topics/nip-42/)
- [NIP-11 : Document d'information du relay](/fr/topics/nip-11/)
