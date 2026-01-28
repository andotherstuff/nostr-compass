---
title: "NIP-52 : Événements de calendrier"
date: 2026-01-28
translationOf: /en/topics/nip-52.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Calendar
  - Events
---

NIP-52 définit les types d'événements pour la fonctionnalité calendrier sur Nostr, permettant la planification, les RSVP et la coordination d'événements.

## Types d'événements

### Kind 31922 : Événement de calendrier basé sur la date
Pour les événements s'étalant sur un ou plusieurs jours sans heures spécifiques :

```json
{
  "kind": 31922,
  "tags": [
    ["d", "identifiant-unique"],
    ["title", "Meetup Nostr"],
    ["start", "2026-02-15"],
    ["end", "2026-02-15"],
    ["location", "Austin, TX"]
  ]
}
```

### Kind 31923 : Événement de calendrier basé sur l'heure
Pour les événements avec des heures de début et de fin spécifiques :

```json
{
  "kind": 31923,
  "tags": [
    ["d", "identifiant-unique"],
    ["title", "Appel hebdomadaire"],
    ["start", "1706900400"],
    ["end", "1706904000"],
    ["start_tzid", "America/New_York"]
  ]
}
```

## Support RSVP

Les événements kind 31925 permettent aux utilisateurs de répondre aux événements de calendrier :

- `accepted` - Participera
- `declined` - Ne participera pas
- `tentative` - Pourrait participer

## Fonctionnalités

- **Adressable** : Les événements peuvent être mis à jour sans créer de doublons
- **Support des fuseaux horaires** : Gestion appropriée des fuseaux horaires via les identifiants IANA
- **Localisation** : Lieux de réunion physiques ou virtuels
- **Récurrence** : Support des événements récurrents (extension proposée)

## Voir aussi

- [NIP-22](/fr/topics/nip-22/) - Commentaires (pour les discussions sur les événements de calendrier)
- [NIP-51](/fr/topics/nip-51/) - Listes (pour les collections de calendrier)
