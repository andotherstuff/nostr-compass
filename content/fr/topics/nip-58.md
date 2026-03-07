---
title: "NIP-58 : Badges"
date: 2026-01-28
translationOf: /en/topics/nip-58.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Identity
  - Reputation
---

NIP-58 définit un système de badges pour Nostr. Un événement définit le badge, un autre l'attribue, et un troisième permet au destinataire de choisir s'il l'affiche sur son profil.

## Fonctionnement

### Définition de badge (Kind 30009)

Les émetteurs créent des définitions de badges comme événements adressables :

```json
{
  "kind": 30009,
  "tags": [
    ["d", "early-adopter"],
    ["name", "Early Adopter"],
    ["description", "Joined before 2024"],
    ["image", "https://example.com/badge.png"],
    ["thumb", "https://example.com/badge-thumb.png"]
  ]
}
```

### Attribution de badge (Kind 8)

Les émetteurs attribuent des badges à un ou plusieurs utilisateurs :

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

Dans un événement de badges de profil, les clients doivent lire les tags `a` et `e` comme des paires ordonnées. Un tag `a` sans son événement d'attribution correspondant, ou un tag `e` sans sa définition de badge correspondante, doit être ignoré.

## Cas d'utilisation

- **Appartenance à une communauté** : montrer l'appartenance à des groupes ou communautés
- **Accomplissements** : reconnaître les contributions ou les jalons
- **Attestations** : permettre à un tiers de se porter garant d'un rôle ou d'un statut
- **Contrôle d'accès** : restreindre des fonctionnalités ou des espaces à l'aide de badges émis par une autorité

## Modèle de confiance

La valeur d'un badge dépend entièrement de la réputation de l'émetteur. N'importe qui peut créer des badges, donc les clients doivent :

- Afficher les informations de l'émetteur de manière visible
- Permettre aux utilisateurs de filtrer par émetteurs de confiance
- Ne pas traiter les badges comme faisant autorité sans contexte

Les attributions de badges sont immuables et non transférables. Cela rend les badges adaptés aux attestations et aux reconnaissances, mais pas aux identifiants portables au sens tokenisé.

## Notes d'implémentation

Les définitions de badges sont des événements adressables, donc les émetteurs peuvent mettre à jour les visuels ou les descriptions d'un badge sans changer l'identifiant du badge. L'événement d'attribution est l'enregistrement durable qui lie un destinataire à cette définition à un moment donné.

Les clients ont aussi une latitude dans la présentation. La spécification leur permet explicitement d'afficher moins de badges que ceux listés par un utilisateur et de choisir la taille de miniature adaptée à l'espace disponible.

---

**Sources principales :**
- [Spécification NIP-58](https://github.com/nostr-protocol/nips/blob/master/58.md)

**Mentionné dans :**
- [Newsletter #7 : Cinq ans de janviers Nostr](/en/newsletters/2026-01-28-newsletter/)
- [Newsletter #15 : Cinq ans de févriers Nostr](/en/newsletters/2026-03-04-newsletter/)

**Voir aussi :**
- [NIP-51 : Listes](/fr/topics/nip-51/)
- [Web of Trust](/fr/topics/web-of-trust/)
