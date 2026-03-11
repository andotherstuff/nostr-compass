---
title: "NIP-52 : Événements de calendrier"
date: 2026-01-28
translationOf: /en/topics/nip-52.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - Calendar
  - Events
---

NIP-52 définit les événements de calendrier, les calendriers et les RSVP sur Nostr. Il offre aux clients un moyen standard de publier des événements basés sur le temps ou la date sans inventer un modèle d'événement personnalisé pour chaque application.

## Types d'événements

### Kind 31922 : Événement de calendrier basé sur la date

Le kind `31922` sert pour les événements sur une journée entière ou plusieurs jours, où l'heure précise n'a pas d'importance.

```json
{
  "kind": 31922,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Nostr Meetup"],
    ["start", "2026-02-15"],
    ["end", "2026-02-16"],
    ["location", "Austin, TX"]
  ]
}
```

### Kind 31923 : Événement de calendrier basé sur l'heure

Le kind `31923` sert pour les événements avec des heures de début et de fin précises.

```json
{
  "kind": 31923,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Weekly Call"],
    ["start", "1706900400"],
    ["end", "1706904000"],
    ["D", "19755"],
    ["start_tzid", "America/New_York"]
  ]
}
```

Les événements basés sur l'heure requièrent aussi un ou plusieurs tags `D`, chacun contenant le timestamp Unix à granularité journalière pour les jours que couvre l'événement. Ce tag existe pour que les relais et clients puissent indexer par jour sans analyser chaque timestamp complet.

## Calendrier et support RSVP

Le kind `31924` est un calendrier, une liste adressable d'événements de calendrier. Le kind `31925` est un RSVP qui pointe vers un événement de calendrier spécifique avec un tag `a` et optionnellement vers une révision spécifique avec un tag `e`.

Les événements de kind `31925` permettent aux utilisateurs de répondre avec :

- `accepted` - Participera
- `declined` - Ne participera pas
- `tentative` - Pourrait participer

Les RSVP peuvent aussi inclure des valeurs `fb` de `free` ou `busy`, ajoutant un contexte de planification au-delà du statut de participation.

## Notes d'implémentation

- **Adressable** : les événements et calendriers peuvent être mis à jour sans créer de doublons
- **Support des fuseaux horaires** : les événements basés sur l'heure peuvent utiliser les identifiants de fuseaux IANA
- **Données de localisation** : les tags peuvent inclure des lieux lisibles par l'humain, des liens et des geohashes
- **Requêtes collaboratives** : les auteurs d'événements peuvent demander l'inclusion dans le calendrier d'un autre utilisateur en le taguant

Les événements récurrents sont intentionnellement hors périmètre. La spécification délègue les règles de récurrence aux clients, ce qui simplifie l'indexation côté relais et évite les cas limites habituels autour des changements d'heure d'été et des exceptions.

## Pourquoi c'est important

NIP-52 fait plus que décrire une réunion. Il sépare la définition de l'événement, l'appartenance au calendrier et les réponses des participants en différents kinds d'événements. Cela permet à une application de publier un événement, à une autre d'agréger les calendriers, et à une troisième de gérer l'état des RSVP sans que les trois partagent le même backend.

---

**Sources principales :**
- [NIP-52 Specification](https://github.com/nostr-protocol/nips/blob/master/52.md)
- [PR #1752: Day-Granularity Timestamp Tag](https://github.com/nostr-protocol/nips/pull/1752)

**Mentionné dans :**
- [Newsletter #7 : Notedeck Calendar App Draft](/fr/newsletters/2026-01-28-newsletter/#notedeck-progress-calendar-app-and-ux-polish)
- [Newsletter #10 : NIP Updates](/fr/newsletters/2026-02-18-newsletter/#nip-updates)
- [Newsletter #10 : NIP Deep Dive](/fr/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-52-calendar-events)

**Voir aussi :**
- [NIP-22 : Comment](/fr/topics/nip-22/)
- [NIP-51 : Lists](/fr/topics/nip-51/)
