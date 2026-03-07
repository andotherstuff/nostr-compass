---
title: "NIP-39 : Identités externes dans les profils"
date: 2026-02-11
translationOf: /en/topics/nip-39.md
translationDate: 2026-03-07
draft: false
categories:
  - NIPs
  - Identity
---

NIP-39 définit comment les utilisateurs attachent des revendications d'identité externe à leurs profils Nostr en utilisant des tags `i`. Ces tags lient une pubkey Nostr à des comptes sur des plateformes externes comme GitHub, Twitter, Mastodon ou Telegram.

## Fonctionnement

Les utilisateurs publient des revendications d'identité dans des événements kind 10011 sous forme de tags `i`. Chaque tag contient une valeur `plateforme:identité` ainsi qu'un pointeur de preuve permettant au client de vérifier la revendication :

```json
{
  "kind": 10011,
  "tags": [
    ["i", "github:username", "gist-id"],
    ["i", "twitter:handle", "tweet-id"]
  ]
}
```

Les clients reconstituent l'URL de preuve à partir de la plateforme et de la valeur de preuve, puis vérifient que la publication externe contient le `npub` de l'utilisateur. Cela rend la revendication portable entre clients sans nécessiter de vérificateur central.

## Modèle de preuve

Le point important est que NIP-39 prouve le contrôle de deux identités simultanément : la clé Nostr et le compte externe. Si l'un des côtés de cette preuve disparaît, la vérification s'affaiblit. Un gist ou un tweet supprimé n'invalide pas l'événement historique, mais supprime la preuve en direct dont la plupart des clients dépendent.

Un autre point d'implémentation utile concerne la stratégie de récupération. Comme les revendications vivent désormais en dehors du kind 0, les clients peuvent décider de ne les demander que sur les vues de profil détaillées, uniquement pour les utilisateurs suivis, ou pas du tout. Cela évite d'alourdir le chemin déjà très sollicité du kind 0.

## État actuel

Selon la spécification actuelle, les revendications d'identité vivent dans des événements kind 10011 dédiés plutôt que dans les métadonnées kind 0. Cette séparation provient de l'effort plus large visant à alléger les récupérations de profil kind 0.

---

**Sources principales :**
- [NIP-39 : External Identities in Profiles](https://github.com/nostr-protocol/nips/blob/master/39.md)
- [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) - Extraction des revendications d'identité hors du kind 0

**Mentionné dans :**
- [Newsletter #9 : Mises à jour NIP](/en/newsletters/2026-02-11-newsletter/#nip-updates)
- [Newsletter #12 : Amethyst](/en/newsletters/2026-03-04-newsletter/#amethyst-nip-39-nip-c0-nip-66)

**Voir aussi :**
- [NIP-05 : Vérification basée sur DNS](/fr/topics/nip-05/)
