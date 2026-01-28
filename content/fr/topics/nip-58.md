---
title: "NIP-58 : Badges"
date: 2026-01-28
translationOf: /en/topics/nip-58.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Identity
  - Reputation
---

NIP-58 définit un système de badges pour Nostr, permettant aux émetteurs de créer des badges et de les attribuer aux utilisateurs qui peuvent ensuite les afficher sur leurs profils.

## Fonctionnement

### Définition de badge (Kind 30009)

Les émetteurs créent des définitions de badges comme événements adressables :

```json
{
  "kind": 30009,
  "tags": [
    ["d", "early-adopter"],
    ["name", "Adopteur précoce"],
    ["description", "A rejoint avant 2024"],
    ["image", "https://example.com/badge.png"],
    ["thumb", "https://example.com/badge-thumb.png"]
  ]
}
```

### Attribution de badge (Kind 8)

Les émetteurs attribuent des badges aux utilisateurs :

```json
{
  "kind": 8,
  "tags": [
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["p", "recipient-pubkey"]
  ]
}
```

### Affichage de badge (Kind 30008)

Les utilisateurs choisissent quels badges afficher sur leur profil :

```json
{
  "kind": 30008,
  "tags": [
    ["d", "profile_badges"],
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["e", "award-event-id"]
  ]
}
```

## Cas d'utilisation

- **Appartenance à une communauté** : Prouver l'appartenance à des groupes ou communautés
- **Accomplissements** : Reconnaître les contributions ou les jalons
- **Vérification** : Attestations tierces (employé, créateur, etc.)
- **Contrôle d'accès** : Restreindre le contenu ou les fonctionnalités en fonction de la possession de badges

## Modèle de confiance

La valeur des badges dépend entièrement de la réputation de l'émetteur. N'importe qui peut créer des badges, donc les clients devraient :
- Afficher les informations de l'émetteur de manière visible
- Permettre aux utilisateurs de filtrer par émetteurs de confiance
- Ne pas traiter les badges comme faisant autorité sans contexte

## Voir aussi

- [NIP-51](/fr/topics/nip-51/) - Listes
- [Toile de confiance](/fr/topics/web-of-trust/)
