---
title: "NIP-05 (Vérification de domaine)"
date: 2026-02-04
description: "NIP-05 permet des identifiants lisibles par l'homme pour les pubkeys Nostr grâce à la vérification de domaine."
---

NIP-05 associe les clés publiques Nostr à des identifiants internet lisibles par l'homme comme `utilisateur@exemple.com`. Cela fournit un moyen de vérifier l'identité par la propriété du domaine sans nécessiter de confiance dans une autorité centrale.

## Fonctionnement

Un utilisateur revendique un identifiant en ajoutant un champ `nip05` aux métadonnées de son profil. L'identifiant suit le format `nom@domaine`. Les clients vérifient la revendication en récupérant `https://domaine/.well-known/nostr.json` et en vérifiant que le nom correspond à la pubkey de l'utilisateur.

Le fichier JSON au chemin well-known contient un objet `names` associant les noms locaux aux pubkeys hexadécimales :

```json
{
  "names": {
    "alice": "abc123...",
    "bob": "def456..."
  }
}
```

Lorsque la vérification réussit, les clients peuvent afficher l'identifiant au lieu de ou à côté du npub. Certains clients affichent une coche ou un autre indicateur pour les identifiants vérifiés.

## Indices de relais

Le fichier `nostr.json` peut optionnellement inclure un objet `relays` associant les pubkeys à des tableaux d'URLs de relais. Cela aide les clients à découvrir où trouver les événements d'un utilisateur particulier.

## Implémentations

La plupart des clients majeurs supportent la vérification NIP-05 :
- Damus, Amethyst, Primal affichent les identifiants vérifiés
- De nombreux services de relais offrent des identifiants NIP-05 comme fonctionnalité
- De nombreux fournisseurs NIP-05 gratuits et payants existent

## Sources principales

- [Spécification NIP-05](https://github.com/nostr-protocol/nips/blob/master/05.md)

## Mentionné dans

- [Newsletter #8 (2026-02-04)](/fr/newsletters/2026-02-04-newsletter/) - PR exigeant les minuscules pour les clés hex et les noms
